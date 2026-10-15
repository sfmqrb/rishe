# Verification process log — verify-page-506


## [2026-10-15T02:44:16.279Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 506 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-506.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-506.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-506.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 506` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.333Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.382Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.411Z] TOOL RESULT

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


## [2026-10-15T02:44:21.225Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-506.txt; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-50*.json"
}
```


## [2026-10-15T02:44:21.650Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py | head -150"
}
```


### [2026-10-15T02:44:22.103Z] TOOL RESULT

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


### [2026-10-15T02:44:22.134Z] TOOL RESULT

```
=== PDF page 506 (book page 476) ===
--- entry 0 ---
ROOT [Indo-European] Ters : dry, to dry  (refs POK:1078)
#1 (parent #0) [Avestan] refs=POK:1078; KLN:1592 | taršu : dry ; taršna : thirst
  #2 (parent #1) [Pahlavi] refs=None | tišn : thirst ; tišnak : thirsty
    #3 (parent #2) [Persian] refs=BQT:499 | tešneh «تشنه ( تشنگی )» : thirsty
#4 (parent #0) [Latin] refs=AHD; KLN | terra : dry land, earth ; medi-terrâneous : midland (sea) ☞Medhyo ; turrěre : to dry, toast
  #5 (parent #4) [French] refs=AHD:1329 | terrasse : pile of earth ; Mediterranee
    #6 (parent #5) [Persian] refs=MON:1060; MON6:1941 |  | extra: تراس ، مدیترانه
    #7 (parent #5) [English] refs=AHD | terrace
  #8 (parent #4) [English] refs=AHD | terrain, terrestrial, territory ; Mediterranean, subterranean ; toast
#9 (parent #0) [Germanic] refs=AHD | thurs : thirst
  #10 (parent #9) [English] refs=None | thirst
--- entry 1 ---
ROOT [Indo-European] Teter : chatter  (refs POK:1079)
#1 (parent #0) [Pahlavi] refs=POK:1079; KLN:1596 | titar : pheasant
  #2 (parent #1) [Persian] refs=BQT:478; IEC:1388 | tazarv «تذرو» : pheasant
  #3 (parent #1) [Sogdian] refs=SOD:392 | tt`rw : pheasant
#4 (parent #0) [Medit] refs=IEC:1388 | tetatos, taturas : pheasant
#5 (parent #0) [Sanskrit] refs=IEC:1388 | tittirah : pheasant
#6 (parent #0) [Greek] refs=POK:1079; KLN:1596 | tetraon : a bird | NOTE: POK claims this is derived from Persian
  #7 (parent #6) [Latin] refs=None | tetrâô, turtur, turtura
    #8 (parent #7) [English] refs=None | turtle, tortoise
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


## [2026-10-15T02:44:25.711Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','MON6','IEC','SOD','AHD','WLD','PHD','NYB','HRN','HUB','BRT','ARY','SYN','SKT']:\n  v=d.get(k); print(k, json.dumps({x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint','scans']} if v else None, ensure_ascii=False)[:400])\n\"; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'));e=d['entries'][0];print(json.dumps(e,ensure_ascii=False)[:3000])\""
}
```


### [2026-10-15T02:44:26.160Z] TOOL RESULT

```
POK {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint
KLN {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf o
BQT {"kind": "archive_djvu+local_scan_ocr", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt 
MON {"kind": "website+archive_djvu", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_A
MON6 null
IEC {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstr
SOD {"kind": "archive_djvu", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers
AHD {"kind": "archive_djvu+website+archive_restricted", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so
WLD {"kind": "archive_djvu", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD
PHD {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, fo
NYB {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II
HRN {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. 
HUB {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries lo
BRT {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (
ARY {"kind": "local_scan_ocr", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page cit
SYN {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each sec
SKT {"kind": "archive_djvu", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SK
{"entry": 0, "root": "Tel", "verdict": "confirmed", "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)", "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).", "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-", "https://en.wiktionary.org/wiki/Ἄτλας", "https://en.wiktionary.org/wiki/τάλαντον"], "ref_check": [{"ref": "POK:1060", "status": "supports", "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."}, {"ref": "KLN:122", "status": "supports", "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τάλαντον, ... L. tollere 'to lift up, raise', t
```


## [2026-10-15T02:44:28.060Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root /lemma: ters\\|Root /lemma: teter\\|Root /lemma: tet\" POK_full.txt | head"
}
```


### [2026-10-15T02:44:28.403Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:44:29.963Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s): 107[89]\" POK_full.txt | head; grep -n -i \"lemma.*ters\\b\\|lemma.*teter\" POK_full.txt|head"
}
```


### [2026-10-15T02:44:30.393Z] TOOL RESULT

```
86390:Page(s): 1078-1079 
86460:Page(s): 1079-1080 
86339:Root / lemma: ters-
```


## [2026-10-15T02:44:31.810Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 86335,86470p POK_full.txt"
}
```


### [2026-10-15T02:44:32.159Z] TOOL RESULT

```
Page(s): 1077-1078 



Root / lemma: ters- 

Meaning: dry; thirst 

Material: Old Indie //•sya// "durstet, lechzt' (= Gothic l=>aursjan), tarsayat/" aWows dursten, 

languish ' (= Latin torreo. Old High German derren), tarsa-m. " thirst ', trsta- 'arid, rough, 

jolting, hoarse', trsu- " greedy, lechzend' = Avestan tarsu-'6ry, that is to say not fluid' (= 

apart from pronunciation of Gothic Paursus, Old Latin /o/TY/s'torridus'); Old Indie frsna' 

thirst, yearning', Avestan tarsna-m. ' thirst '; Old Indie trsna-j- " thirsty '; 

Armenian t'aramim, f'arsam/m '\Ne\ke' , far' shaft, pole zum Trocknen from Trauben ' 
{* trsa or * trs/a: gr. rpaaia); 

gr. T£pao|jai (£T£par|v) 'werde dry', Tspaaivu) "make dry', rpaaia, rapaia "Darre', lapooq, 
rappoc; 'Darre, Dorr- or Trockenvorrichtung'; dubious rpauAoc; (*TpaauA6(;?) 'lisping'; 

alb. /eA'trockne (trans.) an the air'; 

Latin torreo, -ere, -ui, tostum 'dehydrate, desiccate, fry, rosten, singe' {tostus= Old Indie 
trsta-). Old Latin torrus, extended /o/r/io'^s 'ausgetrocknet, arid', /o/r/is 'blaze, burning piece 
of wood', torrens' burning, sengend, erhitzt; violent, roaring, rapid in the current', Subst. 
"Wildbach' ('in summer austrocknend'?); 

here also Latin terrai. 'earth' (: eA-Zo/r/is 'verba nnt' = tellus: meditullium), Oscan 
teei{um], /em/77 'territorium', /eras 'terra e' from Italian *terso-, *tersa, Indo Germanic *ters-, 
to Old Irish //?n. es-stem ' region, area', corn. bret. acymr. //r'tellus'. Old Irish *//?, tirim 
'dry'; also basic form *teros-, *teres-, Latin terres-tris, terrenus aiter terra; Old Irish tart' 
thirst '(tz-s/o-); 

Italian terrene : Spanish tierra : French terrain : Furlan teren : Portuguese terrene ; terra : 
Romagnolo tiren : Sardinian Campidanesu (*terranea) tanca ; terra : Albanian (*tanca) toka 
' soil ; ground '; 

Gothic gaf^a/rsan stem V. ' wilt' (= gr. Tspaopai); gat^aursnan ds. = Old Icelandic t^orna 
ds.; Old High German dorren ds.; Old High German derren' dry make, dehydrate, 
desiccate'. Old Icelandic tierra' dry' (= Old Indie tarsayati, Latin torreo); Gothic t^aursjan 
'diJrsten', Old Icelandic Ay/'s//' (Gothic *t^aursiPs) ' thirsty ', whereof Gothic t^aursteii.. Old 
Icelandic t^orstirw.. Old English t^urst. Old High German durst' thirst '; Gothic t^aursus{s 
instead of znach t^airsan =Q\d Indie trsu-). Old Icelandic t^urr. Old English t^yrre. Old High 



German durr/'and'; Old High German c/arra, Swedish /a/ye'Gestell zum Trocl<nen, Darre'; 
probably also Old Icelandic t^orskr. Middle Low German dorsch^ codfish ("*the to 
Trocknende'). 

References: WP. I 737 f., WH. II 636 f., 694. 
Page(s): 1078-1079 

Root / lemma: tet(e)r- 

Meaning: to quack (expr. root) 

Material: Old Indie tittira-, tittirf-, tittfri-xw. " partridge, game bird '; Armenian tatrak 

"turtledove"; 

npers. tadarv^ pheasant' (also gr. TaTupa(;, itia^oc, ds. are of pers. origin); 

gr. TSTpaojv, m. ' grouse ' (*T£TpaF-(jov), rsipa^ (out of it Latin tetrax) 'Perlhuhn' {*tetrks), 
T£Tpa5u)v, TSTpaTov, TEipawv Vogelname by Hesych., TEipi^ "ein bird'; neologism Middle 
Irish /e/^/a 'crow' {*tetoria). Old Icelandic t^idurr^ grouse ' {*t^et^uraz)\ Old Prussian 
/a/5/w/s'Birkhuhn', Lithuanian/e/e/'i/5sds., Latvian teter/s {Gen. teterja, from *tetervis), 
Lithuanian /e'/e/'i///75s"Birkhahn, grouse ', /eZ/rKa'Birkhenne' (Latvian //?5/'s Truthahn' 
influenced from fftet, s. ti-ti-), russ. -Church Slavic tetrevikVk. PI. 'cpaaiavouq', Serbo- 
Croatian tethjeb^ grouse ', Old Czech tetrevds., russ. /e/e/iei/'Birkhahn' {teterka 
"Birkhenne, Birkhuhn'); 

verbal gr. Terpa^u) "gackere, gluckse (from the hen)', Latin tetrinnid, -Tre, tetrissito, -are " 
chatter (from Enten)'; 

also in other onomatopoeic words kehrt t-ras characteristic element again, compare 
e.g. Latin /^/Y^A'turtledove', "s/OAOs'Star', the thrush-names (see 1096), streTg-, streTd{h)- 
"hiss, schwirren', gr. Tpu^u) "girre', Tpuyibvf. 'turtledove', TspsTi^u) "zirpe'. 

Maybe alb. /iy/Yi/// 'turtledove' a Latin loanword. 

References: WP. I 718, WH. II 677 f., Trautmann 320 ff., Vasmer 3, 101; compare tor-S. 
1088 f., Mayrhofer 1 , 500. 
Page(s): 1 079 

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
```


## [2026-10-15T02:44:43.054Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/506.jpg; cat data/extracted/batch/page-506.json | head -c 4000"
}
```


## [2026-10-15T02:44:43.410Z] TOOL CALL #9: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/506.jpg"
}
```


### [2026-10-15T02:44:43.448Z] TOOL RESULT

```

```


### [2026-10-15T02:44:43.477Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   63k sfmqrb 14 Oct 22:15  site/pages/506.jpg
{
  "pdf_page": 506,
  "book_page": 476,
  "entries": [
    {
      "root": {
        "name": "Ters",
        "lang": "Indo-European",
        "refs": "POK:1078",
        "gloss": "dry, to dry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1078; KLN:1592",
          "words": [
            {"translit": "taršu", "gloss": "dry", "script": null},
            {"translit": "taršna", "gloss": "thirst", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "tišn", "gloss": "thirst", "script": null},
            {"translit": "tišnak", "gloss": "thirsty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:499",
          "words": [
            {"translit": "tešneh", "gloss": "thirsty", "script": "تشنه ( تشنگی )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "آب دریا گر همه نتوان کشید - پس بقدر تشنگی باید چشید",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "terra", "gloss": "dry land, earth", "script": null},
            {"translit": "medi-terrâneous", "gloss": "midland (sea)", "script": null, "see": ["Medhyo"]},
            {"translit": "turrěre", "gloss": "to dry, toast", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:1329",
          "words": [
            {"translit": "terrasse", "gloss": "pile of earth", "script": null},
            {"translit": "Mediterranee", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:1060; MON6:1941",
          "words": [],
          "script_extra": "تراس ، مدیترانه",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "terrace", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "terrain, terrestrial, territory", "gloss": null, "script": null},
            {"translit": "Mediterranean, subterranean", "gloss": null, "script": null},
            {"translit": "toast", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "thurs", "gloss": "thirst", "script": null}
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
            {"translit": "thirst", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
```


## [2026-10-15T02:44:51.442Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; pdftoppm -f 506 -l 506 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg506 && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg506.png data/verification/sources/refs/ocr/BOOK/506.png; cd data/verification/sources/refs; grep -n -i \"tittir\\|tatyr\\|tetar\\|tetra\" IEC.txt | head -30"
}
```


### [2026-10-15T02:44:53.172Z] TOOL RESULT

```
2516:drdh- “linger, laze, doze Cf. drm- Gk. dartháno, darthéo; Cz. (ambig.) drdol "dot: Li. cf. dirdénu, -dénti ‘crawl, as traf- fic’. (For Arm. tartam ‘hesitant’, cf. Gk. tetra- maíno ‘tremble’, qua *títrém-)
12096:oKtou (okto, oKdo, oKdou, oKdmi) “eight. Cf. eK- (oK-) and duou (?). WP I, 173 Skt. astaü, astá (perh. 2 tetrads'. MacDonell); Av. asta; Per. hast (infl. of haft geven: Oss. ast; Tokh. A okát, B okt; Arm. ut, i-st.; Gk. októ; Lat. octó; Alb. tetë (aphetic w. added -të); Olr. ocht; Br. eiz; W wyth; Cor. eth; OHG ahtowi, pl.; MHG ehtewe, pl. beside aht, eht; Go. ahtau; OE eahta; ON átta; cf. vari- ants in OCS osmí (and com. Sl.); Li. aštuoni CG Lat. octoni ‘eight each"); Latv. astoni, id.
18458:teteruos (tetruos), a, is *heathcock, caper- cailie'. WP I, 718. Onomat. Skt. cf. (z-gde onomat.) tittirab, m. ‘francolin, partridge’; Medic tétaros, tatüras, s. (phea- sant’; Per. tazarv, s. id. (and “jungle-cock); Gk. cf. tétrix & tétrax, m. 'guinea-fowl, heath- cock’; (LW in) Arm. tatrak, i, av, s. *wood- pigeon’; ON pióurr, pl: piórar, m. *capercailie'; Sw. tjäder, id.; OCS tetrěví, gs: -i, m. “phea- sant ` R téterev, m. fheathcock'; Cz. tetřev *capercailie'; Li. tetervà, tetirvà, f. “black grouse, heath-fowl; Latv. teteris, id.; OPr. tatarwis, f. id.
18619:Skt. cf. tittiráh, -íh, m. ‘francolin’; Gk. cf. tettix, m. 'tree-cricket'; Lat. titus, gs: -1, m. ‘woodpigeon’; cf. also titius, m. *birdwatcher' and titiae aves ‘wild pigeons’; Li. cf. tytaras,
```


## [2026-10-15T02:44:56.887Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tt'rw\\|tt[\\`’']rw\\|ttrw\\|pheasant\" SOD_pages.txt | head; grep -n -i \"pheasant\\|tadarw\\|tidar\\|titar\\|tazarw\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt HUB.txt | head -20"
}
```


### [2026-10-15T02:44:57.338Z] TOOL RESULT

```
31736:     pheasant                                                      MDii p2l3; S W, BSOAS 38, 133; twYw, TSP
39074:parchment      8228                      penetrating      1466                    . pheasant      9698
43611:   iVAbv <Ym <yu* <rvv <r&r ^u                               trwttrw <?m<Y*^ j,-^
PHD.txt:590:tà [OD < A “d | (M d’), N ~] until; so that. tab [tp | N ~] fever. tab-, —išn, v. taftan. tüb- , ~išn, v. tāftan. хабар [r5k! | N taba] frying-pan. tabāh [tp?% | N ~] ruined, spoilt, destroyed. 7h : ruin, destruction. tabāhīhistan, tabāhīh- [tp’hyh-sin' | J th’hh-] be ruined. tabangóg [ipngwk! | N tabangó] box, chest. tabarzad [tpizt' | N ~] manna. tābestān [P stn! | N ~] summer. tábidan [P 5ytn! | N ~] = tāftan. tadan, tan- [itn!, tn- | N tan-] spin (thread). tadar(w) [ttl | (N tačarw)] pheasant. taftan, tab- [tp-tn'] grow hot; shine. —išn: heat, fever. táftan, tāb- [2°p-tn' | P РЬ-, N ~] heat, burn; shine. ~išn: burning. taftīg [tptyk' | (P tft)] burning, ardent, fervent. tag [tk' | N ~] running, attack. — kardan abar, ó: attack. мар (Pk! | N ta] item, unit; alone, single. ңар [Ok | N tā] branch. tagarg [tklg | M erg, N ~] hail. tagig [tkyk!] swift, strong. ~ih: speed, strength. tah [th | N ~] bottom. tak6k [tkwk! | N ~] drinking vessel. talag [t/k' | N tala] snare, trap. ~-€in [-cyn'] fowler. tambiir [tm-, tnbwl | N ~] cither, lute. ~ag [-k'] tambour (?). tan [tn' | = M, N ~] body, person. tan-, v. tadan. *tanāpuhl [tr?pwhl = Av. tanu.parada- | (N tanáfür)] a degree of sin.
PHD.txt:3113:pheasant tadar(w).
PHD_mackenzie.txt:4877: tadar(w) [ttl I (N ta8arw)] pheasant.
```


## [2026-10-15T02:45:01.338Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"9698\\|969[0-9] \" SOD_pages.txt | head; sed -n 31725,31740p SOD_pages.txt"
}
```


### [2026-10-15T02:45:01.709Z] TOOL RESULT

```
31698:9690 trzmnw      B                           ^ftw-i^               3.203, 218; Dhu. 113, Dhy. 366; C2; STii 598;
31705:9691 trzmnw      S =» trzmnw                                     tawandistar ©comp. adj.
31706:9692 trzmny =* tr'zmnyh                                          more powerful
31707:9693 trzmnyh      B =$ tr'zmnyh                                  MSP blO
31708:9694 ts B, S                              (jz)jj'<s~?       9703 tw*prn(y)   M                      o^^UI     < vl^*JU
31715:9695 ts- C                                           j^J         GcOpay
31723:9696 tsycq M                         oJL <J^- / ^*j^             heap, mass
31728:9697 tVr S                                            j&    9706 twdy C =» tw8>k
31733:9698 ttr'w B                                   Jj»v<j>-          TSP 3.9, 14, 6.33, 7.133, 8.151, 156; Frag. Len. 13
31739:9699 9ty>q C                        J^j <c^Lj <&£-?         9709 twya S                               '^Oi
     tasice, tasicak ^t's-
     axe, spade                                                    BSTii 857.1 1:"C2, 17V4, 22V 13; Sogdica. 56.28,
     GMS 1012; Sund. Man. Lett. 305.18; 307 n 20
9697 tVr S                                            j&    9706 twdy C =» tw8>k
     tatar ©ob. -y                                          9707 tw8yh M =» tw6>k
     Tatar                                                  9708 twy1 B, M, S                                ^^txs
                                                                 tux ©Skt. takva =*twytr, twx
     S W-Ham. CII 1990 p86                                       fast
9698 ttr'w B                                   Jj»v<j>-          TSP 3.9, 14, 6.33, 7.133, 8.151, 156; Frag. Len. 13
     tatarw ©Pahl. tadarw
                                                                   Rl; GMS 254; Sogdica. 40.13; Tales. 481.44;
     pheasant                                                      MDii p2l3; S W, BSOAS 38, 133; twYw, TSP
     TSP 3239
                                                                   2.415
9699 9ty>q C                        J^j <c^Lj <&£-?         9709 twya S                               '^Oi
     Gatyak ? ©fOam\ Av. Oamnahvant "solicitous";                toy ©Khwar. twT\ Arm. tugam =>twz-, twyt-
```


## [2026-10-15T02:45:05.908Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[:2500]); print(json.dumps(d['MON'],ensure_ascii=False)[:2000])\""
}
```


### [2026-10-15T02:45:06.513Z] TOOL RESULT

```
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "covers_etymology": true, "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and ca
```


## [2026-10-15T02:45:07.750Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:499 2>&1 | head -80"
}
```


### [2026-10-15T02:45:08.171Z] TOOL RESULT

```
no scan of BQT covers printed page 499 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:45:09.567Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"تشنه\\|تذرو\" BQT_v1_pages.txt | head -20"
}
```


### [2026-10-15T02:45:10.033Z] TOOL RESULT

```
27614:تشنهٌ جام می روم شاید اکر سبو شوم .
29156:تفج بفتح اول و ثانی وسکون رای تذرو زر یخ- کتابه از انکشت
29159:بود صحرابی شبیه بخروی تذرو ذدین پر- کنایه از آتاب
29160:تذروا.
29175:برسر سرو زند پردة عشاق تذرو ورشان نای زند برسر هزمفروسی .
29368:گفته‌انه تذرو است که خروی صحرایی باشف 5
30202:تشنه [رك: نشنه] ؛ عطش.
31717:8 رله: ترنکت وتذرو .
```


## [2026-10-15T02:45:13.236Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 29156 29368 30202; do head -n $l BQT_v1_pages.txt | grep -c $'\\f'; head -n $l BQT_v1_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; done; sed -n 30185,30215p BQT_v1_pages.txt; sed -n 29355,29375p BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:14.021Z] TOOL RESULT

```
695
699
717
نب هتح آول بروزن چمن » بمعنی
و لفزنده » آزعدس 2 داروهای چشم
بکار ند » و بکسر اول هم‌آمده است .
فشناث « بر وزن چشمك , از پیش سر
جایی را گویند کمدر کود کی نرموجهندمباشد »
وآنرا بمربی بافوخ خوانند .#
قشنه جچگر - کنابه از اختیاق باشد .
عم 8 یحو کی کف ایا
اشنه چیزی بودن» کنابه از | گکوبند که از سنگهای الوان وسخت‌سازندوبدان
اثتیاق هرچیز(۱) است . باژی کنند ۰
(۱) چش: هرچیزی .
. )( ر۵ : نت‎ ٩
ولف درفرهنکه شاهنامه تسی‌را بممنی جانوری: آورده که آن‌را پیشتر عشی کویند»‎ - ۴
و آن حیوالی است مانند خاریشت بزر که که خارهابی مانند نی‌های پرمرغ دارد ودر موفع دفاع‎
ازخود سوی دشمن برتاب میکند وآنرا چوله 3 عوام كٍِِ . «فرهنگه‎
شاهنامه »۰ درطبری نطعهه «واژه‌نامه ۶۲۱۷ . کر‎
نه فشنگی - بکسراول وسوم (درلهجه م رکزی)؛ 21 ۱۳ بحاصل فصتر از
تشنه [رك: نشنه] ؛ عطش.
۵ ثنه - بکر اول و سوم (در لهج مر‌کزی) »بهلوی 15002۴ از 3500 از
0 »۵ . اومتابی 2۲51112 «بارترلمه ۹464». سانسکرت 651192 «نیی رکه ۷۷۵ و۰۲۲۹
«اسشق ۳۸۸ ,اورامانی 205026) «۵. اورامان ۰۱۲۷ , گیلکی 26۵10086) .فریزندی وبرنی
قهز2 : طنری 1۵8کقا «2. + س 2۲۹۳ , سمنانی 25100 , سنکری 5960تاکها .
صرخه 0 یه ۰ لاسگردی صوطوها ». شهمیرزادی اقا د 4. ۲ ص۱44 ؛ عطشان ۳
دارندة عطش, که تشنگی دارد ؛ جمم» تشنگان ۳
کس نه بیندکه ندنگان حجاز پلپ آب شور کرد آیشد .
دکلستان ۰۳۲ . رد: تش»کوبندا ‏ و بمعنی خوردلی وآذوقه ورأتب‌هم
آمده است - و بمعتی‌پیمانه هم هست - و نقاه
بر وزن شراره هم عیگویند .
ب‌- بنم هردو تای قرشت و سکون
هر دو غن نقطه دار . چیزی باه مالند کله
و قفیز که غله بدان پیمابند - و بعضی کویند
(بوند) . ۴ - رك : تريك
مت 4 6ج
قر آرلگه بفتح اول وفوقانی بروزن شبد
پرك » نام مرضکی است که آنرا در ماوراه‌النهر
دخثر صوفی میگویند وبعربی صعوه میخوانند -
وضم اول و فوفانی جابی است درکوه چل مفام
شیراز که مردم بانجا روند و صنگی دد زس
خود نهاده از یلا لفزیده بیبین آیند ٩‏ -
وبکسر اول وفوقالی» مردم سبك و بی‌تمکین‌را
کمک
قر نگ ده بم اول و الت وسکون ثانی
و کاف. کبك راکوبند . و آن پرنده ایست که
آو را مرغ آشخواره ی میگونند - و بضی
گفته‌انه تذرو است که خروی صحرایی باشف 5
و باين معنی بجای حرف ثالی زای نقطه دار نیز
اسف ات
ثرت وهر سته با تای فردت بر وزن
هرج ومرح . اینلفت ازائباع است بمعنی تاخت
و تاراج. وزیر وزیرو پراکنده ویریشان- وبزبان
رفته ونقصان آمده واز هم افتاده.
تر جمان- باجیم ومیم بر‌وزن نردبان *
```


## [2026-10-15T02:45:18.283Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==718' BQT_v1_pages.txt | head -5; awk 'BEGIN{RS=\"\\f\"} NR==718' BQT_v1_pages.txt | grep -n \"^[۰-۹]\\{3\\}\\|[۰-۹]\\{3\\}$\" | head; grep -n \"تذرو\\s*-\\|^تذرو\\|تذرو ب\" BQT_v1_pages.txt | head"
}
```


### [2026-10-15T02:45:19.367Z] TOOL RESULT

```
ودرو غ باشد؟ .
ترك نیمرود » کنابه از آقتاب
جهان | راست و
ر‌ گون با کاف فارسی‌بروزن‌مجنون»
تر کند - بروزن فرزند» ممعثی درو غ-
29160:تذروا.
```


## [2026-10-15T02:45:21.717Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29140,29185p BQT_v1_pages.txt; grep -n \"pdf page\" BQT_v1_pages.txt | head -3"
}
```


### [2026-10-15T02:45:22.167Z] TOOL RESULT

```
دچار ؛ نام بادشاه دهستان است کهاز مبارژان
لشکر کیخضرو بوده .
لو » بفتح اول وانی بوا و کشیده » نام
مرغی است صحرایی شبیه بخروس درنهات خوش
روبی وخوش رفتاری۷ .
(۱) چش: سیم.
٩‏ سس رک 0 بشگگ.
بهلوی 0۳021 ۶ آ براهامبان» .
للم بنتح اول و انی » بمعثی تنیده
باشد که ازننبدن مدنقاست۸ .
(۳) چك : بکرخا.
۴ - از: نخم ۰-۳ ( فسبت )»
ومانند تنقل‌خورند .
«بوستی. تام نامه» «فرهنگه شاهنامد» .
۷۲ - رث :نذرو .بیان هشتم
در تاي قرشت با ذال نقطه دار مشتمل برپنج لفت و کنایت
تفج بفتح اول و ثانی وسکون رای تذرو زر یخ- کتابه از انکشت
بی نقطه وجیم , معرب نذرو است» و آن هرغی و زغال افروخته باشد.
۱ اف کته تن وم ۳ ۱
بود صحرابی شبیه بخروی تذرو ذدین پر- کنایه از آتاب
تذروا.
ی عالمتاب است - وآش را یز گویند .
باواوءبمعتی نذر "
7 نو » بنتح اول و ثانی بواو کشیده .
۱ ۳ جانوریست سرخ رنگ ویردار که بشتردرحمامها
صبدراسی ضیبه
قتی ) و متوضامی باشد , و او را بعربی ابن وردان
بخ روی باس ۹ گوند۴ .
درتای قرشت با رای قرشت مشتمل‌بر دکصد وشصت لفت و کنات.
است کوچك وکم سکون وخوش آواز که بعربی و کتابه از شخصی است که باندك چیزی از جا
صموه خوانندش؟ » و باین معتی بلزای قطه دار | درآیدب وشخص ی که درفمار منازعت کند با آنجه
۱ - پپلوی عتقان) « اونوالا ۵۵۱ »۰ بودانی 1602۳05 , در سانسکریت ات4100
بممنی کيك «اسشق ٩۳۷۹‏ .عمرب‌آن ندرج ونفرح؛ پرنده‌ای ازخانوادة ۳1325121010665 که‌اصل
آنها از مشرق است» ودارای طول نبة بلنداست و انواع مختاف دارد . گوشت آن لذبذ و پرش
درخشان است؛:
برسر سرو زند پردة عشاق تذرو ورشان نای زند برسر هزمفروسی .
«منوچهری‌دامغانی 4۱۰۵
۴ -سومك سرخ که بیشتر در حمامها ودر بالوعه‌ها باشد. سنگم.« مهذب‌الاسماء *»
موسکه فخلاص نطنزی» راك : لفت‌نامه * ابن‌وردان».
۴ - 08۳۷2۵ 2۷15 62808۵ ۵ 0650205 087۲0 < فولری ‏ :
5 « اسشق ۳۸۳ » « حوشمن ۳۸۳ .
یه درصفحة 1۷۹پاخته بائد پس کیرد - و کنابه از مردم ملوث
ومردار و فاسق حم هست۷ .
فا بفتح اول بر وزن سرا ؛ دبوار
ودیوارفلعه وکاروان سرا - وسدی و دیواربرا لیز
کفته‌اند که دریش جزی یکفند؟ و دیواری
```


## [2026-10-15T02:45:28.164Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^thirst\\|^tetrao\\|^turtle\\|^tortoise\\|^terra\\b\\|^terrace\\|^territory\\|^toast\\|^torrid\" KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:45:28.646Z] TOOL RESULT

```
38688:terra
39066:thirst,  intr.  v.  —  ME.  thirsten,  fr.  OE.  pyrstan,  fr. purst,  ‘thirst’.  Cp.  ON.  pyrsta  (fr.  pursti)  and OHG.  dursten,  MHG.  diirsten,  dursten,  G.  dur- sten  (fr.  OHG.,  MHG.,  G.  durst),  ‘to  thirst’,  and see  thirst,  n.
39391:toast,  tr.  and  intr.  v.  —  ME.  tosten,  fr.  MF.  fos¬ ter,  ‘to  roast',  fr.  OF.,  fr.  VL.  *tostdre  (whence also  It.  tostare,  Sp.,  Port,  tostar, ‘to  roast'),  freq. of  L.  torrere  (pp.  tostus ),  to  parch,  roast’,  fr. I.-E.  base  *trs-,  ‘to  be  dry',  whence  also  OL. torrus  (for  *torsus),  ‘dry’,  L.  terra  (for  *tersa), ‘earth’,  lit.  ‘dry  land'.  See  terra  and  cp.  words there  referred  to.
39393:toast,  n.  —  ME.  toste,  fr.  tosten.  See  toast,  v. Derivatives:  toast-y,  adj.,  toasti-ness,  n.
39631:torrid,  adj.,  very  hot.  —  L.  torridus,  ‘parched, torrid,  dried  up’,  fr.  torrere,  ‘to  parch’,  which  is rel.  to  OL.  torrus  (for  *  tor  sits),  ‘dry’,  and  to  L. terra  (for  *tersa-),  ‘earth’,  lit.  ‘dry  land’.  See terra  and  cp.  torrent.
39645:tortoise
39647:tortoise,  n.,  turtle.  —  ME.  tortuce ,  fr.  MF.  ( —
40513:turtle,  n.,  tortoise.  —  Sailor's  alteration  of  F.  tor- tue,  ‘tortoise’,  after  turtledove.  See  tortoise. Derivative:  turtle,  intr.  v.
```


## [2026-10-15T02:45:31.539Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38686,38700p KLN_1966.txt | cut -c1-1500; grep -n -a \"^thirst, n\\|^terrace\\|^territory\\|^Mediterranean\\|^tetrao\\|^turtle\\|^turtledove\\|^tortoise, n\" KLN_1966.txt; sed -n 39060,39066p KLN_1966.txt | cut -c1-1200; sed -n 39645,39650p KLN_1966.txt|cut -c1-1200; for l in 39066 38688 40513; do head -n $l KLN_1966.txt | grep -c $'\\f'; done"
}
```


### [2026-10-15T02:45:32.479Z] TOOL RESULT

```
terpodion,  n.,  a  keyboard  instrument,  invented  in 1816  by  Buschmann  in  Berlin  ( mus .)  —  ModL., coined  from  the  stem  of  Gk.  xipTreiv,  ‘to  glad¬ den’,  and  4>Srj,  ‘song’.  See  next  word  and  ode.
Terpsichore,  n.,  the  Muse  of  the  dance  (Creek  and
terra
tessitura
I  J7£
I  J7J
Roman  mythol.)  —  L.  Terpsichore,  fr.  Gk.  Tsp- lit.  ‘enjoyment  of  dance’,  a  name  com¬ pounded  of  T£<p4^,  ‘enjoyment,  gladness,  de¬ light’,  and  x°po?,  ‘dance’.  The  first  element  is  a derivative  of  Teptretv,  ‘to  delight,  please ,  fr. I.-E.  base  *terp-,  ‘to  satisfy’,  whence  also  OI. trpyati,  trpnoti,  tarpati ,  ‘takes  one  s  fill ,  Avestic &rafda-,  ‘satiated,  satisfied’,  Toch.  AB  tsdrw-,  ‘to rejoice",  tsarwo,  ‘joy’,  Lith.  tarpstii,  tafpti !,
‘to  thrive,  prosper’,  tarpa,  ‘thriving,  prosperity  , Lett,  tarpa,  of  s.m.,  OPruss.  en-terpo,  ‘it  is  use¬ ful’,  en-terpen,  en-terpon ,  ‘useful .  Cp.  Euterpe. For  the  second  element  see  chorus.
Derivative:  Terpsichore-art,  adj.,  pertaining  to Terpsichore;  hence,  pertaining  to  dance, terra,  n.,  earth.  —  L.,  prob.  for  *tersa-  and  lit. meaning  ‘dry  land’  and  rel.  to  OL.  torrus  (for *torsus),  ‘dry’,  L.  torrere,  ‘to  parch,  roast’,  and cogn.  with  OIr.  Ur  (for  *teros),  ‘land’,  fr.  I.-E. base  *ters-,  *trs-,  ‘to  be  dry’,  whence  also  OI. tar$dvati,  ‘dries  up’,  tr?yati,  ‘thirsts’,  tfftah, ‘hoarse',  trsuh,  ‘greedy,  desirous’,  Avestic tarshu-,  ‘dry,  solid’,  Arm.  Tafamim,  ‘I  wither, dry  up',  erasht,  metathesized  fr.  *trast  (for  I.-E. *trsti),  ‘dryness, drought’,  Gk.TspnenHat,  ‘to  be or  become  dry,  dry  up',  Tspaodvciv,  ‘to  make dry,  to  dry',  xapoo;,  ‘wickerwork;  flat  of  the foot;  ankle’,  xpama,  Ion.  xapai r„  ‘a  crate  for drying  figs'.  Alb.  ter,  ‘I  lay  out’,  Goth.  p aursus, ‘dry,  barren',  OHG.  thurri ,  durri,  MHG.  durre, diirre,  G.  diirr,  Du.  dor,  OS.  thurri,  ON.  purr,  OE. pyrre,  'dry',  OHG.  darra,  MHG.,  G.  darre,  'kiln drying'.  Cp.  inter, ‘to  bury’,  mediterranean,  par¬ terre,  subterranean,  tarsus,  terrace,  terra  cotta, terrain,  terramara,terramycin,  terrane,terrestrial, terrier  (in  both  senses),  terrine,  territory,  thirst, toast,  torrid,  trass,  traulism,  tureen  and  the  sec¬ ond  element  in  verditer.  Cp.  also  torsk. terrace,  n.  —  MF.  terrasse,  terrace,  ‘pile  of  earth, terrasse'  (whence  F.  terrasse),  fr.  O  Pro  vent,
terrain,  n.,  a  tract  of  land.  —  F„  fr.  L.  terrenum. See  terrene.
terramara,  n.,  an  earthy  deposit.  -  Dial.  It.,  for terramarna,  fr.  It.  terra,  ‘earth',  and  dial.  It.  ma- ra  (for  It.  mama),  ‘marl’  (see  terra  and  marl) ;  so called  because  made  of  dry  earth, terramycin,  n.,  an  antibiotic  derived  from  an earth  mold.  —  Coined  fr.  L.  terra,  ‘earth’,  Gk. [it>x7;c,  'fungus',  and  suff.  -in.  See  terra  and myco-.
terrane,  n.,  a  geological  formation.  F.  terrain, fr.  L.  terrenum,  ‘land,  ground’  (whence  also  Sp.
terreno,  OProven?.  terren),  prop.  neut.  of  ter¬ renus,  ‘of  earth',  used  as  a  noun.  See  terrene, terraneous,  adj.,  terrestrial.  —  See  terra  and -aneous.
terrapin,  n.,  name  of  several  species  of  turtles.  —
Of  Algonquian  origin.
40513:turtle,  n.,  tortoise.  —  Sailor's  alteration  of  F.  tor- tue,  ‘tortoise’,  after  turtledove.  See  tortoise. Derivative:  turtle,  intr.  v.
Derivatives:  third,  n.,  third-ling,  n.,  third-ly, adv.
thirl,  n.,  a  hole,  aperture.  —  ME.,  fr.  OE.  pyrel.
See  thrill.
thirl,  tr.  and  intr.  v.,  to  pierce,  thrill  (Engl,  dial.)
—  ME.  thirlen,  fr.  OE.  pyrlian,  fr.  pyrel.  See prec.  word.
thirl,  tr.  v.,  to  restrict.  —  Related  to  thrall.  The orig.  meaning  of  thirl  was  ‘to  reduce  to  slavery’, thirst,  n.  —  ME.  thirst,  fr.  earlier  thurst,  fr.  OE. purst,  rel.  OS.  thurst,  ON.  porsti,  Dan.  terst, Swed.  torst,  MDu.,  Du.  durst,  OHG.,  MHG., G.  durst,  Goth,  paurstei,  fr.  I.-E.  base  *trs~,  ‘to be  dry’,  whence  also  OL.  torrus  (for  *  torsos), ‘dry’,  L.  torrere,  ‘to  parch,  roast’,  terra  (for *tersa-),  ‘earth’.  See  terra  and  cp.  words  there referred  to.
thirst,  intr.  v.  —  ME.  thirsten,  fr.  OE.  pyrstan,  fr. purst,  ‘thirst’.  Cp.  ON.  pyrsta  (fr.  pursti)  and OHG.  dursten,  MHG.  diirsten,  dursten,  G.  dur- sten  (fr.  OHG.,  MHG.,  G.  durst),  ‘to  thirst’,  and see  thirst,  n.
tortoise
tournure
tortoise,  n.,  turtle.  —  ME.  tortuce ,  fr.  MF.  ( —
F.)  tortues ,  pi.  of  tortue ,  fr.  earlier  Proven?,  tor- tuga,  fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derives  fr.  VL.  tartaruca,  lit.  ‘the  infernal animal’,  fr.  L.  Tartarus',  see  Tartarus.  The Proven?,  form  tortuga  is  due  to  the  influence  of L.  tortus,  ‘twisted’.  Folk  etymology  found  in  the name  of  the  animal  a  reference  to  its  twisted legs.  Cp.  turtle,  ‘tortoise’, tortricid,  adj.,  pertaining  to  the  Tortricidae.  —  See next  word.
Tortricidae,  n.  pi.,  a  family  of  moths  (zoo/.)  — ModL.,  formed  with  suff.  -idae  fr.  Tortrix,  gen. Tortricis.  See  next  word.
Tortrix,  n.,  a  genus  of  moths  (zoo/.)  —  ModL., formed  fr.  tortus,  ‘twisted,  bent’,  pp.  of  torquere. See  torque  and  -trix.
852
843
883
```


## [2026-10-15T02:45:36.552Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^tetrao\\|^Tetrao\\|^tetrad\\|turtledove,\\|^turtle,  n.,  t\\|^turtle\" KLN_1966.txt | head; grep -n -a -i \"tetra.n\\|tatur\" KLN_1966.txt | head"
}
```


### [2026-10-15T02:45:36.921Z] TOOL RESULT

```
38764:tetrad,  n.,  1)  the  number  four;  a  group  of  four things.  —  Gk.  xsxpdp,  gen.  xexpaSop,  rel.  to Att.  Gk.  xexxapep,  Gk.  TeanapEc;,  ‘four’.  See tessara-,  and  -ad.
40513:turtle,  n.,  tortoise.  —  Sailor's  alteration  of  F.  tor- tue,  ‘tortoise’,  after  turtledove.  See  tortoise. Derivative:  turtle,  intr.  v.
2324:almud,  almode,  n.,  a  dry  measure.  —  Arab,  al- mudd,  fr.  al-,  ‘the’,  and  mudd,  ‘a  com  measure’, fr.  madda,  ‘he  extended,  stretched’,  which  is  rel. to  Heb.  madad,  ‘he  measured’,  midddh,  ‘meas¬ ure,  stature,  size’,  Akkad,  madadu,  ‘to  measure’, almuerzo,  n.,  breakfast.  —  Sp.,  fr.  almorzar,  ‘to breakfast’,  fr.  L.  admorsus,  pp.  of  admordere, ‘to  bite  into’,  fr.  ad-  and  mordere,  ‘to  bite’.  See mordant.
36563:stamen,  n.,  the  pollen-bearing  organ  of  a  flower. —  L.  stamen,  ‘warp  in  the  upright  loom,  thread, fiber',  cogn.  with  Gk.  axYjp.wv,  ‘warp’,  fr.  I.-E. base  *st(h)a-,  ‘to  stand’,  whence  also  OI.  sthd- man,  ‘place  for  standing,  station’,  Toch.  A shtdm,  ‘tree’,  Goth,  stoma,  ‘base,  material’,  Lith. stomuo,  stuomud,  ‘stature’,  Ir.  tamum,  ‘stem  of  a tree’.  See  state  and  cp.  stamin,  stamina.  Cp.  also etamine,  stem,  n.,  Stemona,  tammy,  ‘woolen fabric’.
36632:holder,  stadium,  stage,  staith,  stall  and  words there  referred  to,  stamen  and  words  there  re¬ ferred  to,  stamnos,  stance,  stanch,  stanchion, stanza,  stapes,  stasis,  stater,  static,  Statice,  sta¬ tion,  stationer,  statistics,  stato-,  stator,  stato- scope,  statue,  stature,  statute,  stay,  ‘to  prop,  sup¬ port’,  stay,  ‘to  stand  still’,  stead,  steed,  steel, sterling,  stet,  stool,  stound,  stow,  ‘to  pack’,  stud of  horses,  stud,  ‘peg,  nail’,  Stundist,  subsist,  sub¬ stance,  substantive,  substituent,  substitute,  super¬ stition,  system,  thana,  thermostat,  vestibule  and the  suff.  in  celestial.
36655:stature,  n.  —  ME.,  fr.  OF.  (=  F.)  stature,  fr. earlier  estature,  fr.  L.  statura,  ‘height,  size, stature’,  lit.  ‘an  upright  posture’,  fr.  stat-(um), pp.  stem  of  stare,  ‘to  stand’.  See  state  and  -ure. Derivative:  statur-ed,  adj. status,  n.  —  L.,  ‘mode  of  standing,  position,  at¬ titude’,  fr.  stat-(um),  pp.  stem  of  stare,  ‘to  stand’. See  state.
38776:tetrandrous,  adj.,  having  four  stamens  (bot.)  — Compounded  of  tetra-  and  -androus. Tetraonidae,  n.  pi.,  a  family  of  birds  (ornithol.)  — ModL.,  formed  with  suff.  -idae  fr.  L.  tetrad , ‘heath  cock’,  fr.  Gk.  xExpacov,  which,  together with  tit pa^  (whence  L.  tetrax),  name  of  a bird,  derives  from  a  base  of  imitative  origin.  Cp. 01.  tittirah,  tittirih,  ‘partridge’,  ModPers. tadarv,  ‘pheasant’,  L.  tetrinnire,  ‘to  quack’,  tur- tur,  ‘turtledove’,  Arm.  t'rt'rak,  ‘a  good  speaker’, OSlav.  tetrivi,  ‘pheasant’,  Lith.  terra ,  ‘black grouse’,  Russ,  totorit ’,  ‘to  babble,  chatter’.  Cp. turtle,  ‘turtledove’.
40512:Turritella,  n.,  a  genus  of  gastropods  with  long turretlike  shells  ( zool .)  —  L.,  dimin.  of  turris, ‘tower’.  See  tower  and  -ella, tursio,  n.,  the  bottle-nosed  dolphin  (zool.)  — ModL.,  fr.  L.  tursio,  ‘dolphin,  porpoise',  fr.  Gk. ffupoicov,  of  s.m.,  which  is  possibly  related  to D-upaop,  ‘a  straight  shaft’.  See  thyrsus, turtle,  n.,  turtledove  (archaic).  —  ME.,  fr.  OE. turtle,  formed  fr.  L.  tur  tur  (with  dissimilation  of the  second  r  into  /),  which  is  of  imitative  origin. Cp.  Tetraonidae.
```


## [2026-10-15T02:45:52.157Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i \"tarsna\\|taršna\\|tarshna\\|tar[sš]u-\" BRT.txt | head -8; echo ---PHD; grep -n -a -i \"tišn\\|tisn\\|tišnag\" PHD_mackenzie.txt | head -5; echo ---NYB; grep -n -a -i \"tišn\\|tisn\\|ti[šs]nak\\|tišnak\" NYB_vol2_glossary.txt | head -5; echo ---HRN; grep -n -a -i \"tišna\\|tišne\\|ti[sš]na\\b\\|tišnah\" HRN.txt | head -5; echo ---HUB; grep -n -a -i \"tišna\\|tišne\\|tišnah\\|tisna\" HUB.txt | head -5"
}
```


### [2026-10-15T02:45:52.819Z] TOOL RESULT

```
12122:j.  tarSna-  m.  'Durst':  dva  yaska  . . yasca  ^S  yasi'a  'nS  V,  7.70; —  baoointS suhm  °mmca  Yt/p.  69;  96;  —  vanät haurväsca  amantasca  tiva  Si^antta  'n^mca Yt  ig.  96;  g.  10;  —  aodra  vä  *na  (IS.) va  N.  IS' "'. Aus  ir.  '(r^*.  I?-  9-  >6i'  —  ™P-  (Pö-)t  "P- liin,   ai.  vgl.  Iffnä-  f.    —    ')    Das   erste  Mal
---PHD
1142:a-poltisn [)j)whSn ] incorruptible.
5090:   ......-paristisnih: idolatry.
6458:dwelling estisn, man, manisn, manist,           tuxsisn.
6835:    paristisnih.                         incapable anabziir, aniidug.
6968:lasting estisn.                           liberality riidih.
---NYB
509:apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
716:astišn [Pstšn'] persistence 3515 = ēstišn; hence with preceding determinant
717:āstišnēh: mēnēi ~ existence at the heav- enly stage of development 3821; gētē m existence at the earthly stage of develop- ment 393-28; pas hac dam pat menči m after the existence of the creation at the heavenly stage (= after the creation had entered upon the heavenly existence) 3871-22; rai ~ ever-lastingness of splen- dour 5918,
933:bastan [bstn', inser. bstny ; '"SLWN-tn'] band-, to bind (hand and foot) 32!?; to fetter 74??. 115! (be ~); to fasten 2026; asp apar rahy ~ to harness a horse to the car 5416; andar ~ (apar rahy) id. 5418-14 (gl); dar bé ~ to shut the door 7514; puhlv, vitiry ~ to construct a bridge F:1-3.6; menišn i...6...~ to fix a p.’s mind upon = to suggest to his mind to (do ...) 4021-22; ddisr i... pat ménisn be ~ to obstruct the spiritual eye (sight) of a p. 5226-27 (ef. bastišn) — Av. (926) band- = OP; MPrth bstn bnd-; MPrs bstn, subju. byn’d = bennād,
938:bastišn [bstšn] v. n. of bastan: ~ % venisn i cašm the state of the eyesight having been barred, shut = loss of eyesight, blindness 6627. — As to the formation cf MPrthPrs dydysn from ditan (S, A-H II, III), MPrs ’mdysn, -nyh from ämatan (S, A-H II).
---HRN
---HUB
3261:an tisna 'durstig entstanden, wie afgh. va^ai 'hungrig'
5074:b) Np. tiS 'Durst', tisna 'durstig' = zd. iarsna- 'Durst',
5159:sow, cultivate, till', gila 'complaint', tisnaJ 'thirst' im Shk.
5184:p. 205, tisn 'thirst' p. 122, tisnak 'thirsty p. 123.
7583:tisna 'durstig beeinflusst, oben p. 92), dessen s freilich nicht
```


## [2026-10-15T02:45:56.042Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i \"tarsu-\\|tar[sšs]u- \" BRT.txt | head -4; grep -n -a \"thirsty\\|^tišn\\|tišnag\\|tisnag\" PHD_mackenzie.txt | head -5; grep -n -a -i \"tišn\\b\\|tišnak\\|tisnak\" NYB_vol2_glossary.txt | head; grep -n -a \"تشنه\\|تشن\" HRN.txt | head -3; grep -n -a -i \"durst\\|tisna\\|ti[sš]na\" HRN.txt | head; sed -n 5070,5078p HUB.txt"
}
```


### [2026-10-15T02:45:56.671Z] TOOL RESULT

```
5000: ti~nag [tylnk l I M tyIng, N -a] thirsty.
7753:taste casnig, caxsagih, caxsisn,          thirst tisn, tisnagih.
7754:  . mizag(darih).                         thirsty tisnag.
8296:tisnagih        ~~ t"\Y ¥'           tabestan                 \ t'" tUJ .,.,..
8297:tisnag               \~ t"\Y~        tlibisn                      ,~V"~
509:apar-āstišnēh [’pl’stSnyh] the act of ac- cepting and taking care of: ~ % én den rād 589, with the gl. kū tà? pat én den bē éstat (subju. 3d p. sg., v. estátan) ; 5919. — < apar + ēstātan; as to the alternation é-: à- cf ästenisn.
716:astišn [Pstšn'] persistence 3515 = ēstišn; hence with preceding determinant
717:āstišnēh: mēnēi ~ existence at the heav- enly stage of development 3821; gētē m existence at the earthly stage of develop- ment 393-28; pas hac dam pat menči m after the existence of the creation at the heavenly stage (= after the creation had entered upon the heavenly existence) 3871-22; rai ~ ever-lastingness of splen- dour 5918,
933:bastan [bstn', inser. bstny ; '"SLWN-tn'] band-, to bind (hand and foot) 32!?; to fetter 74??. 115! (be ~); to fasten 2026; asp apar rahy ~ to harness a horse to the car 5416; andar ~ (apar rahy) id. 5418-14 (gl); dar bé ~ to shut the door 7514; puhlv, vitiry ~ to construct a bridge F:1-3.6; menišn i...6...~ to fix a p.’s mind upon = to suggest to his mind to (do ...) 4021-22; ddisr i... pat ménisn be ~ to obstruct the spiritual eye (sight) of a p. 5226-27 (ef. bastišn) — Av. (926) band- = OP; MPrth bstn bnd-; MPrs bstn, subju. byn’d = bennād,
938:bastišn [bstšn] v. n. of bastan: ~ % venisn i cašm the state of the eyesight having been barred, shut = loss of eyesight, blindness 6627. — As to the formation cf MPrthPrs dydysn from ditan (S, A-H II, III), MPrs ’mdysn, -nyh from ämatan (S, A-H II).
1456:ēstišn [Pystšn', ystšn'] v. n. of ēstātan, used as pred.: has to, must stand fast, persevere 65’; subst. persistence 34?!; standstill, cessation of progress, of the stars 57. — V. also dstisn(éh).
1642:gartišn [gltšn'] turning, rotation, revo- lution 1206.16.20. — MPrs pres. grd- ‘to turn, to become’ (BBB), caus. grdnydn trans. ‘to turn’ (S); NP gaštan or gardidan gard-, gardiš; etymologically not identical with vart- (v. vaštan) by which it is semasialogically influenced. OIr *gart- probably ‘to twist, to wreathe’, cf Skr jata ‘plait’, probably a Sanskritized Prakrit-w. < *jartä. Hence girt (g. v.).
1665:girt [glt'] round 941%; ~ kartak 38%4, ~ kart 394 "fully developed (?); [späh pat vas marak ~ kart he brought to- gether an army of a large number KnS IV, 12 = KnA p. 22?-10]. - MPrs gyrd ‘all around’ (S), subst. ‘round’ (A-H I); Paz. NP gird; NP gird kartan ‘to collect, to assemble, to bring together”; Güräni gi(rd), gist ‘all, everyone’ (KPF III, II, 248 sg.). From gart-, v. gartišn.
2119:attempt a p.'s life 109-95; vas koxštišn i ~ hard struggle for one’s own life 742”. — MPrthPrs gyn; KZSPrth 1. 4 gyn Gr. v. Blog; < *vyāna-, cf Av. (1478) vyānā-; Paz. jan, NP jan.
2228:-kart [-krt'] -gart [.glt'] -fold: cahär- kart, haft[7]-gart fourfold, sevenfold in- tertwined 20%, 12027, — Probably quite simply from kartan, and at all events influenced by it; or from gart- ‘to turn, to twist’ (v. gartišn)?
3644:388. tis *Durst\ tisne {tesne Sahn. I, 59, 481), tisnegl, tesnegi
3647:aw. tarsna- 'Durst*; phlv. tisn , tisnak, tisncfklh;
3651:'durstig, fun 'Durst' (396); wa/. tax, ^^'/^j sar. tür^
10930:168. *pöi9n 'Durst' in apöisn 'nicht dürstend' (Men., Bund.,
Vgl. § 23. In den Dialekten von Kasan, Semnan u. s. w.
ist ur regelmassig zu ar, er geworden, wie im Ossetischen
der r-Vokal zu dfr, dl (s. meine Etym. u. Lautl. p. 77—78)
geworden ist.
b) Np. tiS 'Durst', tisna 'durstig' = zd. iarsna- 'Durst',
skr. trsnd- 'Durst', trsnaj 'durstig, trsu- 'lechzend'; kisvar
'Erdtheil*, phi. kisvar = zd. karSvare (aus *krsvar-) ; dil 'Herz'
== zd. zeredr-f skr. Ar d-, hrdaya- ; histan *lassen' (aus *hirstan
--- ^hrstan), 3. pr. hUad (aus ap. *hrdatiy) = skr. srjdii, zd.
```


## [2026-10-15T02:46:00.355Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"tarSu\\|tarsu-\\|tar§u\" BRT.txt | head -5; grep -n -a -B2 \"tarSna-  m\" BRT.txt | head -3; head -n 12122 BRT.txt | grep -c $'\\f'; grep -n -a \"^ters-\\|ters-\\.\" AHD_watkins1985.txt | head; grep -n -a -i \"^ters-\\|ters- \" IEC.txt | head -3"
}
```


### [2026-10-15T02:46:00.754Z] TOOL RESULT

```
12120-j.  tarstay-  t  'Schrecken,  Furcht
12121-KompE.  —  Zum  V.  %rah- ;  vgl.  zu  larllO:
12122:j.  tarSna-  m.  'Durst':  dva  yaska  . . yasca  ^S  yasi'a  'nS  V,  7.70; —  baoointS suhm  °mmca  Yt/p.  69;  96;  —  vanät haurväsca  amantasca  tiva  Si^antta  'n^mca Yt  ig.  96;  g.  10;  —  aodra  vä  *na  (IS.) va  N.  IS' "'. Aus  ir.  '(r^*.  I?-  9-  >6i'  —  ™P-  (Pö-)t  "P- liin,   ai.  vgl.  Iffnä-  f.    —    ')    Das   erste  Mal
373
1082:ters-
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
12786:pers- (2), persno-, see pters- Av. pāšnō, m. (heel; Skt. cf. parsnih, f. id.; Go. faírzna, OHG férsana, f. id.; Lat. perna, id.; Hitt. c£. (queried) parsinus (for *parsnus, pl. (knees in view of parsna-, v. ‘kneel, crouch’). For W ffern, f. 'ankle-bone': Gk. ptérna, see ptersna
18421:terimno-, see termn- (2), and cf. terĝ-, ters- (D
18434:termn- (termnos, terios) (2) ‘dry’. Variant extn. tertos. Cf. ters- (1), terĝ- (1) Alb. cf. i terëm, adj. ('dry'. Ambig. cf. terĝ-); Ir. cf. tirim, adj. id. (and 'kiln-dried"); W cf. tarn, pl. au. m. ‘wiping, drying’. Variant in Gk. (?) seirós, adj. scorching’, fr. *terjós?); and in Alb. i terté ‘dry’; Ir. cf. tiortha, adj. id.
```


## [2026-10-15T02:46:03.396Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o \"TERRICO-.\\{0,500\\}\" AHD_watkins1985.txt | head -2; grep -n -a \"^ters- (1)\\|^tersos\\|^tersā\\|^terso\" IEC.txt | head; grep -n -a \"^tet(e)r\\|tetr\" WLD_band3.txt | head -3; ls incoming/WLD/; grep -n -a \"ters-\\b\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-15T02:46:03.832Z] TOOL RESULT

```
1083:TERRICO-
Permissions Size User   Date Modified Name
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  WLD_Bd1_1930_dli_70244_djvu.txt
.rw-r--r--   42M sfmqrb 14 Oct 22:19  WLD_Bd1_1930_dli_70244_text.pdf
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  WLD_Bd1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  WLD_Bd2_1927_dli_106624_djvu.txt
.rw-r--r--   95M sfmqrb 14 Oct 22:19  WLD_Bd2_1927_dli_106624_text.pdf
.rw-r--r--  2.8M sfmqrb 14 Oct 22:19  WLD_Bd2_pages.txt
```


## [2026-10-15T02:46:06.954Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i \"tittir\\|ttttir\" incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -a -i \"tar[sšS]na\\|torreo\" incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -a \"CORE\\|TERRICO\" AHD_watkins1985.txt | head -3"
}
```


### [2026-10-15T02:46:07.402Z] TOOL RESULT

```
67721:      Ai. tittira-h , tittiri-h „Rebhuhn“,
67725:tittirah ,dessen erstes i durch Ass. an das -ir-    idg. 6 r der 2. Silbe behufs          =
69851:                                                         lat. torreo   -ere, -ui, tostum                           ,
69866:„trocken machen, dorren            aisl. perra „trocknen“ (= ai. tarsayati lat. torreo );                                  ,
69926:u. terra torreo (s. auch testa
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
```


## [2026-10-15T02:46:10.483Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1084p AHD_watkins1985.txt | cut -c1-700; grep -n -a \"tetra\\|teter\\|tet(e)r\" AHD_watkins1985.txt | cut -c1-200 | head; sed -n 67710,67730p incoming/WLD/WLD_Bd1_pages.txt; sed -n 69845,69870p incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:46:11.222Z] TOOL RESULT

```
teu-
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old Eng
654:four (genitive tessardn): TESSERA; DIATESSARON. c. Greek tetras, group of four: TETRAD; d. zero-grade form *k¥t(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordi- nal adjective *ketur-to-. 1. Germani
                                                               ,

„dick, Dickling“ (-s- nach Luchs Fuchs beru’nen und nicht vom Dachsbau
                                        )              ,



(*teks- „zimmern“) den Namen haben •wird, ist wahrscheinlich „fett“ von
Tieren und Menschen die Gdbed. von *tegu-.

tet(e)r- redupl. Schallwort „gackern, hiihnerartige Vogel u. dgl.“.
      Ai. tittira-h , tittiri-h „Rebhuhn“,
                                     aisl. pipurr „Auerhahn“ *pepuruz
                                                                (
                                                                              ai.                                             —
tittirah ,dessen erstes i durch Ass. an das -ir-    idg. 6 r der 2. Silbe behufs          =
Walirung des Reduplikationscharakters erklarbar ist);
   npers. iu&arv „Fasan“ (auch gr. xaxvgag, xexagog ds. sind pers. Ursprungs),
apr. tatarwis „Birkhuhn“, lit. teterrns ds., lett. tderis (gen. teterja aus
                                                                                                                                  ,


Dorr- oder Trockenvorrichtung“                       „troekne (trans.) an der Luft“
                                                            ;
                                                                alb. ter
(u. dgl.     ;
                     G. Meyer      BB. 8, 187,             Alb. Wb. 427);
                                                         lat. torreo   -ere, -ui, tostum                           ,



,. dorren,   braten, rosten, sengen“ ( tostus aus *torsitos        ai. tarsita-h   kaum                =                         ,

=   ai. trsta-h   Ciardi-Dupre BB. 26,204), forms alat. (s. o.), erweitert tor-
                        ;


ridas „ausgetrocknet, dfirr", torris ,, Brand, brennendes Scheit‘, torrens
„brennend, sengend, erbitzt; heftig, brausend, reiBend in der Stromung“,
Subst. „Wildbach“ (dies eig. ,.im Sommer austrocknend ‘? Persson Beitr.
730); air. tart „Durst“ (*trsto-t) ; got. gapalrsan st. Y. „verdorren“ (= gr.
Tf goo/uai)-, gapaiirsnan ds. = aisl. porna ds.; abd. dorren ds.; ahd. derren
„trocken machen, dorren            aisl. perra „trocknen“ (= ai. tarsayati lat. torreo );                                  ,


got. putirsjan  2  „dfirsten“, aisl. pyrstr (got. *paursips) „durstig“, wovon' got.
paurstei f., aisl. porsti m., a,gs.purst, ahd. durst „Durst“ got, paursus is statt z
```


## [2026-10-15T02:46:15.763Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 69815,69844p incoming/WLD/WLD_Bd1_pages.txt | grep -v \"^\\s*[,;]*\\s*$\"; sed -n 69870,69935p incoming/WLD/WLD_Bd1_pages.txt | grep -a -i \"terra\\|tdrra\\|turtur\" | head; grep -n -a \"pdf page\\|^\\s*[0-9]\\{3\\}\\s*$\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1>67600 && $1<70000' | head"
}
```


### [2026-10-15T02:46:16.224Z] TOOL RESULT

```
mim fariamim „welke”' (Hiibschmann Arm. St. I 31, Arm. Gr. I 442, Peder-
sen KZ. 39, 371, 403; unrichtig Bugge IvZ. 32, 6S), crast ,,Troekenheit                                                                                                                                                                -
(ist          die andere Yokalstellung durch                                                                                           die Stellung vor der Doppclkons.
bedingt?    Hiibschmann aaO., Bgm. I 2 4(52; Pedersen KZ. 38,208 nach
                            s.
Bugge leitet es mit Suffix -ti- vom Inehoativst. *erar- ab und vergleicht
lit.          trdJcitu,                       frokiau                ,
                                                                                   troksti                        „diirsten,                  wonacli lechzcn'                            unter              Wechsel
sJe       :       sq,       wie                   arm.               air                         ,,Untersuchung u                         :    lit.     ieskoti           ,
                                                                                                                                                                              suchen“),                      arm.                 far
„Stange zum Trocknen von Trauben u. dgl.“ (Liden Arm. St. 45f., Gdf.
*trsa oder *trsia gr. roaoid)-, gr. zeooopai (hsootir) „werde trocken“, reo-
                                                           :
oatveo „mache trocken‘     roaoid zagoid ,,Darre‘. zagoog, zaggog „Darre,                  £
                                                                                                 ,                        ,
138                                                                 tel-
auch        lat.      terra     ,.Erde'"       (:   extorris        ,,verbannt“      = tellus                  :   medihdliiim),     osk.
teer\um\,            teriim „territorium“,                terns „terrae“ aus           ital.               *terso-,        *tcrsd (siehe
und lieB (Vendryes Msl. 13, 385) auch lat. ferres-tris terrenns ein nach terra                 ,
Vf. LEWb. u. terra).      Es darf aber nicht (trotz Thurneysen Hdb. 37) ver-
gabe ir. *terr[) und daB der c-s-St. tlr „terra entweder erst im Kelt, vom       ‘
u. terra torreo (s. auch testa
```


## [2026-10-15T02:46:20.344Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^تراس\\|تِراس\\|تراس (\\|مدیترانه\\|مديترانه\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt | head; echo ---ARY; grep -n -a \"تشنه\\|تذرو\\|تذرو\" incoming/ARY/ARY_pages.txt | head; grep -n -a -i \"TESHNE\\|TAZARV\\|TADARV\" incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-15T02:46:20.931Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt:27371:اين گیاه را نواحی , بحر الروم (مدیترانه) ذ کر 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:42160:تراسا 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:52680:احمر و بحر الروم (مدیترانه) صید می‌شود 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:53737:(مدیترانه) و افریقا و هندوستان و جنوب 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:53868:آسیا و نواحی بحر الرومی (مدیترانه‌یی) 
MON_part2.txt:27371:اين گیاه را نواحی , بحر الروم (مدیترانه) ذ کر 
MON_part2.txt:42160:تراسا 
MON_part2.txt:52680:احمر و بحر الروم (مدیترانه) صید می‌شود 
MON_part2.txt:53737:(مدیترانه) و افریقا و هندوستان و جنوب 
MON_part2.txt:53868:آسیا و نواحی بحر الرومی (مدیترانه‌یی) 
---ARY
5759:تشنه» نش تشنگو ]۱۹۷
```


## [2026-10-15T02:46:23.184Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5745,5775p incoming/ARY/ARY_pages.txt; head -n 5759 incoming/ARY/ARY_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; grep -n -a \"تراس\" MON_part1.txt | head -5"
}
```


### [2026-10-15T02:46:23.738Z] TOOL RESULT

```
چم این واژه در سانسکریت: بر علف
چم این واژه در زبان‌های ژرمتی: غار :
تخاری ۸ (۸ [۸ل1۸7ل708): 71 0
تخاری 8 (8 [(4ل7۸ل707)+ 711 آلمانی (0/(7 022 لد ۱ + دی زا۱
برنانی (07885): 1818818 ,۳۵73108 انگلیسی کهن (4ل20/08 صا0):
لاتین (047100: 78856 ,۳02۸3۴ 717۸1۸ ,۳۸۲۸
اسپانیایی (82۸(18): 0۸ انگلیسی (#ادلاه/8): 7080 ,۲80
ایتالیایی (/(۵ له ): ال ال زا ۷ اسلاوی کهن (ع1/اماد کنات صزه):

۱ پرتغالی (00870010258: ۳1۸ در
ساکسونی کهن 5420/0 صا0): (فلق 12 ینوی (فللاین زرم 0
آلمانی کهن ((05794۸ 107 صان): ایرلندی کهن (نزولم! صاه). جفتاتمهی7 ۱
[pdf page 196]
‎٩ ۹‏ یی
تشنه» نش تشنگو ]۱۹۷
پسگشت‌ها ۳5 3 (7180) ,ف65 17330۷0 :7هطزک ْ
1071 امات ک نا برهان قاطع + ۵و ۵۳۲
دای ادا آغت‌نامه دهخدا : ۶۶۹۶
6 (7133) ,1139 (18090) فرهنگ معین : ۱۱۶۴
9 (183) ,920 1130۷ :۷8ا0زب(0
یادداشت.
۱- چم پیشین این واجريشه در زبان‌های ژرمنی: چرخیدن» غلنیدن» افکندن.
چم این واژه در زبان‌های تخاری: گمراه شدن» از مسیر چرخیدن.
چم این واژه در زبان ایرلندی کهن: مته.
۲- واژه‌ی (شاید) شامل همه‌ی واژه‌های اين فهرست می‌شود.
اوستایی (487۸۸): 1۸35170۸ ایسلندی کهن (/(010۸41۵/نی5 2ا0):
پهلوی (11ماتتم۳): لاد وا و ای (۸) ۷۰
15۸61 ,718710 ,17182۸361 نورس کهن (۸07۶8 صا0):
کردی (080/30): 788730731 ,۳83811 ۸ ,780887
اففانی (پشتو) (0)1فا۳0ه): ساکسونی کهن (/242002 0ا): 7177887
۸ ,75277 آلمانی کهن (/0272440 0۲اب ها۵):
[pdf page 196]
12078:عتراستت. جاره ارت ) 
14845:افتراس: عقع [ع ۰] (مصم 0( انکندن 
39567:تراس: د۱5 (.) بام» پشت‌بام. ایوان 
39570:۳۳ فرهنگ فارسی معین تراسخ 
39575:تراسخ: ها [ع.] (مصل.) (فد. مد.)
```


## [2026-10-15T02:46:28.083Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 39566,39569p MON_part1.txt; grep -n -a \"^تذرو\\|تذرو:\" MON_part1.txt | head -3; grep -n -a \"^تشنه\" MON_part1.txt | head -3"
}
```


### [2026-10-15T02:46:28.565Z] TOOL RESULT

```
تراس: د۱5 (.) بام» پشت‌بام. ایوان
```


## [2026-10-15T02:46:32.103Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | grep -v \"^import\""
}
```


### [2026-10-15T02:46:32.441Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""

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
```


## [2026-10-15T02:46:38.638Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=\"python3 tools/fetch_source.py\"; \n$F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ters-' --note 'page 506, root Ters: PIE *ters- descendants';\n$F 'https://en.wiktionary.org/wiki/تشنه' --note 'page 506, root Ters: Persian tešne etymology';\n$F 'https://en.wiktionary.org/wiki/terra' --note 'page 506, root Ters: Latin terra etymology';\n$F 'https://en.wiktionary.org/wiki/torreo' --note 'page 506, root Ters: Latin torreo';\n$F 'https://en.wiktionary.org/wiki/terrasse' --note 'page 506, root Ters: French terrasse';\n$F 'https://www.etymonline.com/word/thirst' --note 'page 506, root Ters: English thirst';\n$F 'https://www.etymonline.com/word/territory' --note 'page 506, root Ters: territory';\n$F 'https://www.etymonline.com/word/toast' --note 'page 506, root Ters: toast';\n$F 'https://www.etymonline.com/word/terrace' --note 'page 506, root Ters: terrace';\n$F 'https://en.wiktionary.org/wiki/تذرو' --note 'page 506, root Teter: Persian tazarv/tadarv';\n$F 'https://en.wiktionary.org/wiki/τετράων' --note 'page 506, root Teter: Greek tetraon';\n$F 'https://en.wiktionary.org/wiki/turtur' --note 'page 506, root Teter: Latin turtur';\n$F 'https://www.etymonline.com/word/tortoise' --note 'page 506, root Teter: tortoise (unrelated)';\n$F 'https://www.etymonline.com/word/turtle' --note 'page 506, root Teter: turtle (dove vs reptile)';\n$F 'https://en.wiktionary.org/wiki/tittiri' --note 'page 506, root Teter: Sanskrit tittiri';\n$F 'https://en.wiktionary.org/wiki/Mediterranean' --note 'page 506, root Ters: Mediterranean'"
}
```


### [2026-10-15T02:46:39.164Z] TOOL RESULT

```
Exit code 127
(eval):2: no such file or directory: python3 tools/fetch_source.py
(eval):3: no such file or directory: python3 tools/fetch_source.py
(eval):4: no such file or directory: python3 tools/fetch_source.py
(eval):5: no such file or directory: python3 tools/fetch_source.py
(eval):6: no such file or directory: python3 tools/fetch_source.py
(eval):7: no such file or directory: python3 tools/fetch_source.py
(eval):8: no such file or directory: python3 tools/fetch_source.py
(eval):9: no such file or directory: python3 tools/fetch_source.py
(eval):10: no such file or directory: python3 tools/fetch_source.py
(eval):11: no such file or directory: python3 tools/fetch_source.py
(eval):12: no such file or directory: python3 tools/fetch_source.py
(eval):13: no such file or directory: python3 tools/fetch_source.py
(eval):14: no such file or directory: python3 tools/fetch_source.py
(eval):15: no such file or directory: python3 tools/fetch_source.py
(eval):16: no such file or directory: python3 tools/fetch_source.py
(eval):17: no such file or directory: python3 tools/fetch_source.py
```


## [2026-10-15T02:46:45.108Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F() { python3 tools/fetch_source.py \"$@\"; }\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ters-' --note 'page 506, root Ters: PIE *ters- descendants'\nF 'https://en.wiktionary.org/wiki/تشنه' --note 'page 506, root Ters: Persian tešne etymology'\nF 'https://en.wiktionary.org/wiki/terra' --note 'page 506, root Ters: Latin terra etymology'\nF 'https://en.wiktionary.org/wiki/torreo' --note 'page 506, root Ters: Latin torreo'\nF 'https://en.wiktionary.org/wiki/terrasse' --note 'page 506, root Ters: French terrasse'\nF 'https://www.etymonline.com/word/thirst' --note 'page 506, root Ters: English thirst'\nF 'https://www.etymonline.com/word/territory' --note 'page 506, root Ters: territory'\nF 'https://www.etymonline.com/word/toast' --note 'page 506, root Ters: toast'\nF 'https://www.etymonline.com/word/terrace' --note 'page 506, root Ters: terrace'\nF 'https://en.wiktionary.org/wiki/تذرو' --note 'page 506, root Teter: Persian tazarv/tadarv'\nF 'https://en.wiktionary.org/wiki/τετράων' --note 'page 506, root Teter: Greek tetraon'\nF 'https://en.wiktionary.org/wiki/turtur' --note 'page 506, root Teter: Latin turtur'\nF 'https://www.etymonline.com/word/tortoise' --note 'page 506, root Teter: tortoise (unrelated)'\nF 'https://www.etymonline.com/word/turtle' --note 'page 506, root Teter: turtle (dove vs reptile)'\nF 'https://en.wiktionary.org/wiki/tittiri' --note 'page 506, root Teter: Sanskrit tittiri'\nF 'https://en.wiktionary.org/wiki/Mediterranean' --note 'page 506, root Ters: Mediterranean'"
}
```


### [2026-10-15T02:46:52.158Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/aa6f0d8047293ab4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c4def12721924ea1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4ca9987ace409c9a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c38527810fffabd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b7a469885e47b178.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1c22424a43101156.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1d092592b1e55549.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c11e428dc47ba508.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c74ae1f6b2316c38.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c82037d5eaa48588.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c5c0da1cc855b941.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/74f951316cd600f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3033cfd5fd05824f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c549c182ac3dddd0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f2f07fb223d79027.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/91d1dafa283ae9e0.txt
```


## [2026-10-15T02:46:54.344Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in aa6f0d8047293ab4 c4def12721924ea1 4ca9987ace409c9a c82037d5eaa48588 c5c0da1cc855b941 74f951316cd600f7 1d092592b1e55549; do echo \"=== $f $(wc -c < $f.txt)\"; grep -i -m6 -A3 \"Etymology\" $f.txt | head -30 | cut -c1-600; done"
}
```


### [2026-10-15T02:46:54.797Z] TOOL RESULT

```
=== aa6f0d8047293ab4 6953
=== c4def12721924ea1 5130
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( tyšnk' /⁠tišnag⁠/ ) , from Old Persian , from Proto-Iranian *tŕ̥šnakah , from Proto-Iranian *tŕ̥šnah , from Proto-Indo-Iranian *tŕ̥šnas , from Proto-Indo-European *tr̥s-nó-s , from *ters- ( “ dry ” ) .
=== 4ca9987ace409c9a 37888
 Etymology 

 1.2 
 Noun 
--
 Etymology 

 2.2 
 Pronunciation 
--
 Etymology 

 3.2 
 Pronunciation 
--
 Etymology 

 4.3 
 Pronunciation 
--
 Etymology 

 6.2 
 Verb 
--
 Etymology 

 8.2 
 Pronunciation 
=== c82037d5eaa48588 5944
 Etymology 

 1.2 
 Verb 
--
 Etymology 

 2.2 
 Noun 
--
 Etymology 

 3.3 
 Pronunciation 
--
 Etymology
 [ edit ] 

 See the etymology of the corresponding lemma form.

 Verb
 [ edit ] 
--
 Etymology
 [ edit ] 

=== c5c0da1cc855b941 4404
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 

 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 

 Pronunciation
 [ edit ] 
=== 74f951316cd600f7 7093
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 

 2.2 
 Pronunciation 
--
 Etymology 

 3.2 
 Pronunciation 
--
Particularly: “etymology lacks a clearly identifiable source”

 turtur (turtle dove) 
 Etymology
 [ edit ] 

 Onomatopoeic , from the bird's coo .
--
 Etymology
 [ edit ] 

 Borrowed from Latin turtur ( “ turtle² (turtledove) ” ) , of imitative origin. (See André Cherpillod: Vortaro Volapük-Esperanto kaj Esperanto-Volapük — turtur ( “ cooing ” ) = kverado ( “ cooing ” ) from kveri ( “ to coo ” ) (p. 101) [1] )
=== 1d092592b1e55549 136
```


## [2026-10-15T02:46:59.078Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c 1c22424a43101156.txt 1d092592b1e55549.txt c11e428dc47ba508.txt c74ae1f6b2316c38.txt 3033cfd5fd05824f.txt c549c182ac3dddd0.txt f2f07fb223d79027.txt 91d1dafa283ae9e0.txt 7c38527810fffabd.txt b7a469885e47b178.txt; cat 1d092592b1e55549.txt; grep -n -i \"Iranian\\|Persian\\|Latin\\|Germanic\" aa6f0d8047293ab4.txt | head -30 | cut -c1-200; grep -n -A4 \"Latin\" 4ca9987ace409c9a.txt | grep -i -A3 \"ters\\|tersa\" | head -10; cat c82037d5eaa48588.txt | sed -n 1,80p | grep -v \"^\\s*$\" | head -40"
}
```


### [2026-10-15T02:46:59.746Z] TOOL RESULT

```
  133 1c22424a43101156.txt
  136 1d092592b1e55549.txt
  132 c11e428dc47ba508.txt
  134 c74ae1f6b2316c38.txt
  135 3033cfd5fd05824f.txt
  133 c549c182ac3dddd0.txt
  133 f2f07fb223d79027.txt
12445 91d1dafa283ae9e0.txt
 7884 7c38527810fffabd.txt
 8931 b7a469885e47b178.txt
30196 total
URL: https://www.etymonline.com/word/territory
FETCHED: 2026-10-15T02:46:48Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden145: Proto-Germanic: *þersaną ( see there for further descendants )
153: Proto-Germanic: 
157: Latin: torrēns ( see there for further descendants )
171: > ? Latin: *te(r)skʷom 
172: Latin: tesquum , tescum 
175: Proto-Germanic: *þurstiz ( see there for further descendants )
180: Proto-Germanic: *þurstuz ( see there for further descendants )
186: Proto-Germanic: *þursuz ( see there for further descendants )
188: Proto-Indo-Iranian: *táršuš 
189: Proto-Iranian: *táršuš 
192: Middle Persian: tšknk' [ 7 ] 
197: Proto-Germanic: *þurskaz ( “ cod ” ) ( see there for further descendants )
200: Proto-Indo-Iranian: *tŕ̥šnas ( see there for further descendants )
206: Proto-Germanic: *þarzṓ 
222: > ? Latin: torrus 
242: ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [1] , 1st edition, Oxford: University Press, →ISBN 
246: ^ De Vaan, Michiel ( 2008 ), “ torreō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN 
248: ↑ 5.0 5.1 De Vaan, Michiel ( 2008 ), “ terra ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill,
729: From Latin terra , from Proto-Italic *tersā . Cognates include Gallurese tarra , Italian terra and French terre .
730-
731- Pronunciation
732- [ edit ] 
--
955: Inherited from Latin terra , from Proto-Italic *tersā , from Proto-Indo-European *ters-eh₂ , from *ters- ( “ dry ” ) .
956-
957- Alternative forms
958- [ edit ] 
--
URL: https://en.wiktionary.org/wiki/تذرو
FETCHED: 2026-10-15T02:46:49Z
STATUS: 200
TITLE: تذرو - Wiktionary, the free dictionary
تذرو - Wiktionary, the free dictionary 
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
```


## [2026-10-15T02:47:03.355Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -A3 \"Etymology$\\|Etymology \\[\\|^ Etymology$\" c82037d5eaa48588.txt | grep -v \"^\\s*$\\|edit\\|--\" | head; grep -n \"From\\|Borrowed\\|Inherited\" c82037d5eaa48588.txt c5c0da1cc855b941.txt 91d1dafa283ae9e0.txt 7c38527810fffabd.txt b7a469885e47b178.txt | cut -c1-400 | head -20"
}
```


### [2026-10-15T02:47:04.407Z] TOOL RESULT

```
 Etymology
 See the etymology of the corresponding lemma form.
 Etymology
 Etymology tree
 Etymology
 Inherited from Proto-Iranian *tatr̥wáh .
c5c0da1cc855b941.txt:135: From Wiktionary, the free dictionary
7c38527810fffabd.txt:154: From Wiktionary, the free dictionary
7c38527810fffabd.txt:173: Inherited from Proto-Italic *torseō ( “ to burn, scorch ” ) , from Proto-Indo-European *torséyeti ( “ to make dry, cause to be dry ” ) , from *ters- ( “ dry ” ) + *-éyeti . The fourth principal part tostum is for *torstum . [ 1 ] 
b7a469885e47b178.txt:250: From Wiktionary, the free dictionary
b7a469885e47b178.txt:260: From French terrasse ( “ terrace ” ) . Doublet of terrace .
b7a469885e47b178.txt:292: From French terrasse ( “ terrace ” ) .
b7a469885e47b178.txt:368: From terre , probably influenced by Old Occitan terrassa .
b7a469885e47b178.txt:450: From Latin terra , via Old Occitan terrassa and French terrasse .
b7a469885e47b178.txt:484: From Latin terra , via Old Occitan terrassa and French terrasse .
c82037d5eaa48588.txt:165: From Wiktionary, the free dictionary
c82037d5eaa48588.txt:204: Borrowed from Persian تذرو ( tazarv ) .
c82037d5eaa48588.txt:247: Inherited from Proto-Iranian *tatr̥wáh .
91d1dafa283ae9e0.txt:171: From Wiktionary, the free dictionary
91d1dafa283ae9e0.txt:222: From Latin mediterrāneus ( “ inland ” , from medius ( “ middle ” ) +‎ terra ( “ earth, land ” ) +‎ -āneus ( adjectival suffix ) ) +‎ -an .
```


## [2026-10-15T02:47:06.775Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 240,275p c82037d5eaa48588.txt | grep -v \"^\\s*$\"; grep -n -i \"Proto\\|Etymology\\|tetra\\|imitat\\|onomat\" c5c0da1cc855b941.txt | head; grep -c . f2f07fb223d79027.txt; cat f2f07fb223d79027.txt | head -5"
}
```


### [2026-10-15T02:47:07.189Z] TOOL RESULT

```
 [ edit ] 
 تدرو ( tadarv ) 
 Etymology
 [ edit ] 
 Inherited from Proto-Iranian *tatr̥wáh .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ta.ˈðarw/ 
 ( Dari, formal ) IPA ( key ) : [t̪ʰä.ˈzäɾw] 
 ( Dari, formal ) IPA ( key ) : [t̪ʰä.ˈzäɾw] 
 ( Kabuli ) IPA ( key ) : [t̪ʰä.ˈzäɾw] 
 ( Hazaragi ) IPA ( key ) : [t̪ʰä.ˈzäɾw] 
 ( Iran, formal ) IPA ( key ) : [t̪ʰæ.ˈzæɹv] 
 ( Tajik, formal ) IPA ( key ) : [t̪ʰä.ˈzäɾw] 
 Rhymes: -arw 
 Readings
 Classical reading ? 
 taḏarw
 Dari reading ? 
 tazarw
62: Etymology 
140: Etymology
143: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
197: toîn tetraṓnoin 
200: tôn tetraṓnōn 
208: toîn tetraṓnoin 
5
URL: https://en.wiktionary.org/wiki/tittiri
FETCHED: 2026-10-15T02:46:51Z
STATUS: -1
TITLE:
```


## [2026-10-15T02:47:11.418Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F() { python3 tools/fetch_source.py \"$@\"; }\nfor w in thirst terrace territory toast tortoise turtle subterranean terrestrial terrain; do F \"https://en.wiktionary.org/wiki/$w\" --note \"page 506, English $w etymology\"; done\nF 'https://en.wiktionary.org/wiki/तित्तिरि' --note 'page 506, root Teter: Sanskrit tittiri'\nF 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/tatŕ̥wáh' --note 'page 506, root Teter: Proto-Iranian pheasant'\nF 'https://en.wiktionary.org/wiki/Méditerranée' --note 'page 506, root Ters: French Méditerranée'\nF 'https://en.wiktionary.org/wiki/تراس' --note 'page 506, root Ters: Persian teras from French'"
}
```


### [2026-10-15T02:47:24.481Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8564fd725d95d95e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8077fc3067a878a6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/99f06a73383e066f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6af03c88137ac5b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f002ae8354a7b76e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6b0cc521858082b8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e182ca79930b92f0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/50ae1734894860f1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ad855c1b8ce78e5d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/845e583b7fa7d026.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fc5d2682a95ecf57.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ee19fbe81df7bf2d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e64ff9dd77611d7.txt
```


## [2026-10-15T02:47:27.452Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 8564fd725d95d95e 8077fc3067a878a6 99f06a73383e066f 6af03c88137ac5b8 f002ae8354a7b76e 6b0cc521858082b8 e182ca79930b92f0 50ae1734894860f1 ad855c1b8ce78e5d 845e583b7fa7d026 fc5d2682a95ecf57 ee19fbe81df7bf2d 3e64ff9dd77611d7; do echo \"=== $f $(head -1 $f.txt) $(sed -n 3p $f.txt)\"; grep -m3 \"From \\|Inherited\\|Borrowed\\|Onomat\\|imitative\" $f.txt | cut -c1-450; done"
}
```


### [2026-10-15T02:47:27.934Z] TOOL RESULT

```
=== 8564fd725d95d95e URL: https://en.wiktionary.org/wiki/thirst STATUS: 200
 From Wiktionary, the free dictionary
 From Middle English thirst , thurst , from Old English þurst , from Proto-West Germanic *þurstu , from Proto-Germanic *þurstuz , from Proto-Indo-European *ters- ( “ dry ” ) .
 Inherited from Old English þurst (with vocalism modified after þyrstan ), from Proto-West Germanic *þurstu , from Proto-Germanic *þurstuz .
=== 8077fc3067a878a6 URL: https://en.wiktionary.org/wiki/terrace STATUS: 200
 From Wiktionary, the free dictionary
 Borrowed from French terrasse , from Old Occitan terrassa , from Vulgar Latin *terrācea , from terra ( “ land ” ) . Doublet of terrasse .
=== 99f06a73383e066f URL: https://en.wiktionary.org/wiki/territory STATUS: 200
 From Wiktionary, the free dictionary
 Inherited from Middle English territorie , from Latin territōrium .
=== 6af03c88137ac5b8 URL: https://en.wiktionary.org/wiki/toast STATUS: 200
 From Wiktionary, the free dictionary
 From Middle English tost , from the verb tosten (see below).
 From Middle English tosten , from Old French toster ( “ to roast, grill ” ) , from Late Latin tostō , -āre , frequentative of torreō ( “ to burn, grill ” ) from its perfect passive participle tostus ( “ grilled, burnt ” ) .
=== f002ae8354a7b76e URL: https://en.wiktionary.org/wiki/tortoise STATUS: 200
 From Wiktionary, the free dictionary
 From Middle English tortuse , tortuce , tortuge , from Medieval Latin tortuca , of uncertain origin. May be from Late Latin tartarūcha , from tartarūchus , from Ancient Greek ταρταροῦχος ( tartaroûkhos , literally “ holder of Tartarus [the land of the damned dead in Greek myths] ” ) , because it used to be thought that tortoises and turtles came from the underworld and they were commonly paired with such infernal beasts; see Τάρταρος ( Tártaros 
=== 6b0cc521858082b8 URL: https://en.wiktionary.org/wiki/turtle STATUS: 200
 From Wiktionary, the free dictionary
 From Middle English turtle , tortle , turtel , turtul , from Old English turtle , turtla ( “ turtledove ” ) , ultimately from Latin turtur ( “ turtledove ” ) , of imitative origin.
 Ultimately from Latin turtur ( “ turtledove ” ) , of imitative origin.
=== e182ca79930b92f0 URL: https://en.wiktionary.org/wiki/subterranean STATUS: 200
 From Wiktionary, the free dictionary
 From Latin subterrāneus +‎ -an . [ 1 ] Compare subterrane and subterraneous .
=== 50ae1734894860f1 URL: https://en.wiktionary.org/wiki/terrestrial STATUS: 200
 From Wiktionary, the free dictionary
 From Middle English terrestrialle , from terrestre or Latin terrestris , from terra ( “ land, earth, ground ” ) , with the suffix -al . [ 1 ] 
 ^ “ terrestriā̆l, adj. ”, in MED Online , Ann Arbor, Mich.: University of Michigan , 2007 : “ From terrestre adj. or L terrestris ” . 
=== ad855c1b8ce78e5d URL: https://en.wiktionary.org/wiki/terrain STATUS: 200
 From Wiktionary, the free dictionary
 Inherited from Old French terrain , terrein , from Vulgar Latin *terranum , from Latin terrēnum .
 From Vulgar Latin *terranum , from Latin terrenum .
=== 845e583b7fa7d026 URL: https://en.wiktionary.org/wiki/तित्तिरि STATUS: 200
 From Wiktionary, the free dictionary
=== fc5d2682a95ecf57 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/tatŕ̥wáh STATUS: -1
=== ee19fbe81df7bf2d URL: https://en.wiktionary.org/wiki/Méditerranée STATUS: 200
 From Wiktionary, the free dictionary
 From mer Méditerranée , from méditerranée , originally an epicene adjective, now considered the feminine of méditerrané .
=== 3e64ff9dd77611d7 URL: https://en.wiktionary.org/wiki/تراس STATUS: 200
 From Wiktionary, the free dictionary
 Inherited from Arabic تَرَّاس ( tarrās ) .
```


## [2026-10-15T02:47:31.732Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i \"persian\\|french\\|terrasse\" 3e64ff9dd77611d7.txt | head; grep -n -i \"terra\\|terre\" 99f06a73383e066f.txt | head -5 | cut -c1-300; grep -n -i \"etymolog\\|onomat\\|imitat\\|partridge\\|PIE\\|Proto\" 845e583b7fa7d026.txt | head | cut -c1-300"
}
```


### [2026-10-15T02:47:32.174Z] TOOL RESULT

```
74: Persian 
76: Toggle Persian subsection 
182: Persian
202: Persian lemmas 
203: Persian nouns 
65: Etymology 
190: Etymology
207: partridge 
300: female partridge
394: Mayrhofer, Manfred ( 1992 ), “ tittirá- ”, in Etymologisches Wörterbuch des Altindoarischen [ Etymological Dictionary of Old Indo-Aryan ]‎ [1] (in German), volume 1, Heidelberg: Carl Winter Universitätsverlag, pages 645-646
```


## [2026-10-15T02:47:34.195Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 180,200p 3e64ff9dd77611d7.txt | grep -v \"^\\s*$\"; sed -n 188,210p 845e583b7fa7d026.txt | grep -v \"^\\s*$\"; sed -n 160,200p 99f06a73383e066f.txt | grep -v \"^\\s*$\" | head -20"
}
```


### [2026-10-15T02:47:34.733Z] TOOL RESULT

```
 → Tarifit: atarras 
 Persian
 [ edit ] 
 Noun
 [ edit ] 
 تراس • ( terâs ) 
 terrace 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=تراس&oldid=91160522 "
 Categories : Moroccan Arabic terms belonging to the root ت ر س 
 Moroccan Arabic terms inherited from Arabic 
 Moroccan Arabic terms derived from Arabic 
 Moroccan Arabic 2-syllable words 
 Moroccan Arabic terms with IPA pronunciation 
 Moroccan Arabic lemmas 
 Moroccan Arabic nouns 
 𑨙𑨁𑨙𑩇𑨙𑨁𑨫𑨁 ( Zanabazar Square script ) 
 Etymology
 [ edit ] 
 Variant of तित्तिर ( tittirá ) .
 Pronunciation
 [ edit ] 
 ( Vedic ) IPA ( key ) : /tit.ti.ɾi/ , [tit̚.ti.ɾi] 
 ( Classical Sanskrit ) IPA ( key ) : /t̪it̪.t̪i.ɾi/ , [t̪it̪̚.t̪i.ɾi] 
 Noun
 [ edit ] 
 ति॒त्तिरि॑ or ति॒त्ति॒रि • ( tittíri or tittirí ) stem ,  m 
 partridge 
 ( dance ) kind of step
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
 English
 [ edit ] 
 Etymology
 [ edit ] 
 Inherited from Middle English territorie , from Latin territōrium .
 Pronunciation
 [ edit ]
```


## [2026-10-15T02:47:39.226Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a \"^ters\\|^tersa\\|^trs\" IEC.txt | head -5; grep -n -a -i \"tarsna\\|taršna\\|tišn\\|teshn\\|tishn\" SYN.txt | head -5; grep -n -a \"^TERRACE\\|^TURTLE\\|^TORTOISE\\|^THIRST\\|^TOAST\\|^TERRITORY\" SKT.txt | head"
}
```


### [2026-10-15T02:47:39.591Z] TOOL RESULT

```
18441:ters- (terso) (1) ‘rub, dry’. WP I, 737 Skt. (z-gde) trsyami, v. ‘thirst (o-gde in) targah ‘thirst’; tarsitab, adj. ‘thirsty’; Arm. terem, v. scorch’. Kerestedjian); Gk. térsomai, v., térso (Alexandr. poets) “get dry”; tersaíno, tr. ‘dry’; (phonol. obscure in) Alb. ter, v. “dry, wipe’; Lat. cf. terra, f. (lit. ‘dry land"). For testa, f. see těgō above, not “tosta. . .torre(0). Ainsworth, 1736); Olr. (Gei tirim, tírm, adj. “dry”; tírad, inf. ‘to dry’; Go. ga-pairsan, v. ‘parch’; ON perra, v. ‘dry, wipe’. Nominal forms in OLat. tersus, adj. (“fine — of weather. Fest.) beside terra, f. ‘earth’; Osc. terüm, tee- rúm, n. ‘land’; MIr. tír, m. id.; tirim, gsf: tiorma, adj. (‘dry’, fr. *tersimos); OBr., W tir, m. “land”, pl. -oedd in W. (fr. *tersos, -eos, n.); Cor. tyr, pl. -yow, m. id.; ON perra, f. (towel, lit. *drier); Cz. cf. ü-térka, f. dim. ‘duster, wiper’. (The Arm. form terem is doubtful in the initial, cf. next)
18442:ters- (2) (tersó), variant of type tres, q. v. ‘tremble’. WP I, 760 & trs- (2) Av. taros-, v. id.; Per. tarsam, 1dan, v. ‘fear’; tars, s. “fear”; tarsü, adj. ‘fearful’; Oss. türság, ‘fearful and Grein. v. ‘fear’; tas, s. (sic) ‘fear’; Hitt. cf. (?) tarr(ami), v. (queried: ‘tremble’, but the cluster -rs- occurs elsewhere); Lat. terreo, ere, v. ‘frighten, scare off; OCS cf. trésto, iti, v. ('shake', fr. *tersK-), cf. trásnü,
18453:terskos ‘rough, wild; wilderness’ Lat. tescus, adj. ‘rough, wild, desert; tescum, n. ‘rough common, retreat, remoteness, fast- ness’; Ir. (?) tearc, adj. ‘scant, scare’; OCS cf. tréska, f. ‘brushwood’; Li. cf. terškiu, térksti, v. “get frosted, get misted — of glass’. (Isophonic: OCS tréskü, m. ‘noise’: Li. terk- šiù, éti *bang")
19188:trs- (1) ‘dry; parched; dryness, drought. WP I, 737. Cf. trstos Skt. trs, trsa, f. (thirst; Av. tərəš-, Per. tis, ti$ne, id.; Gk. tarrós, tarsós, m., trasiá f. *dry- ing-rack'; cf. tár-ikhos, mn. & tárikhon, n. (mummy; dried meat or fish’, fr. *tars- + iskho “hold, keep"); (LW in) Arm. tarex ber: ring’; Lat. torris, gs: torrium, m. ‘firebrand’; Ir. & Olrish tur, adj. ‘dry’; OW cf. (variant) tarren, f. (fallow land’, fr. *tersen-); Go. paur- sjan, v. ‘thirst’; OHG thurri, durri, adj. ‘dry’; thurrën, durrēn, v. ‘go dry, be dry; MHG dürre, adj. “dry”; f. ‘dryness’; OE pyrre, Du. dor, ON þurr, Sw. torr, adj. ‘dry’; ON porna, v. ‘dry up’; Du. dorren, v. as OHG; Fris. toar, adj. ‘dry’, toarje, toarre & toerre, v. id.
19189:trs- (2) (zero-gde of types ters- and tres-, q. v.) ‘tremble, shake; fear, rush’ Skt. cf. trsúh, adj. 'eager' beside trasami, v. ‘shake, tremble’; Av. toerosai(mi), v. “fear”; Ober. tarsa-, id.; Oss. cf. tálxà ‘haste, dash’; Alb. (ambig.) cf. turr, türrem, v. (crush, but cf. tuer- & tur-); Lat. cf. ex-torris, adj. *exiled'; mf. ‘exile’ (semantics of Li. tremti, v. ‘exile, banish’); cf. also Lat. torrens, pp. & adj. ‘hasty, violent'; Umb. cf. tursitu! “let him tremble"; Cz. trsat, inf. “jerk, jive’; Big. trásja, v. tr. ‘shake’; trás, m. ‘trot; quake; shock’, trásà, f.
8465:8. Skt. irsnd-, Av. tarsna-, above, 1.
20317:TURTLE.
```


## [2026-10-15T02:47:43.900Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 8420,8466p SYN.txt | grep -a -i \"thirst\\|^[0-9]\\.[0-9]\\|Pers\\|tisn\\|teshn\" | head; sed -n 20317,20330p SKT.txt; grep -n -a \"^TERRACE\\|^TERRESTRIAL\\|^TERRAIN\\|^TEERACE\" SKT.txt | head -3"
}
```


### [2026-10-15T02:47:44.297Z] TOOL RESULT

```
5.13 DRINK (vb.)
Ir. lind (NIz. lionn ‘ale’), W. llyn, prob. the same word as Ir. lind (s-stem), W. llyn ‘lake, pond’ (1.48). Pedersen 1.37. Persson, Beitriige 878. But sepa- rated by Walde-P. 2.438.
7. Skt. ksudh-, ksudha-, Av. sud-, NPers. gud : Skt. ksudh- ‘be hungry’; outside connections?
;00D AND DRINK; COOKING AND UTENSILS 333 5.15 THIRST (sb.) Goth. aurstei Lith. troSkulys, tro’kimas
siya, 51005 ON _porsti Lett. slapes Gtk. ite Dan. ¢¢rst ChSl. Zezda NG wits ee torst SCr. Zed Lat. ae OE purst, byrst Boh,  Zizert It. soif ME thurst, thirst Pol. —pragnienie Boe a NE _ thirst Russ. Zazda a i yee Du durst Skt. irsna-, pity fart OHG  durst Av. tar$na- Nir. tart, iola MHG durst W. ile NHG durst
longing’ (as & from ‘thirst for’). 1, Derivs. of IE *ters- in Grk. répco-
ua ‘become dry’, Lat. torrere ‘make dry’, Goth. paursjan ‘be thirsty’, OHG derran ‘make dry’, Skt. trs- ‘be thirsty, etc. Walde-P. 1.737f. Ernout-M. 1048. Pedersen 1.81.
Ir. fart; Goth. Jaurstez, OE purst, etc. general Gme.; Lith. troskulys, troskimas (trokstt ‘be thirsty’, trogskus ‘thirsty’); Skt. irsnd-, Av. targna-.
6. Lett. slapes : slapt ‘be thirsty, be- come weak’, Lith. slopti ‘become weak or choke with thirst’ prob. fr. a parallel form of the root (*slap- in ON slafast ‘slacken’): Lith. slabnas, ChSl. slabi ‘weak’, etc. (Walde-P. 2.432, but with- out inclusion of Lett. sldpes, etc.). Miuhl.-Endz. 3.924.
Pol. pragnienie, fr. pragnaé ‘be thirsty’ : Boh. prahnouti ‘be parched’ (as with thirst), Pol. prazyé, etc. ‘roast’ (5.18). Briickner 434.
TURTLE.
Cot.;  lit  to  turn  round  togctbcr.wF. (—  L.   cQtt-^  for    cum),   togelha  ;  0. terrier f  to  turn.
detour,  a  winding  way,   (F.  —  h) detour,    a    circuit  ;    verbal    sb.    frooi dJtourtur,  to  turn  aside.  —  F.  de-  (  =  L  fio-l aside,  apart ;  tourucr,  to  tuni
retum.vb. (F.  — L,>  F, fr/.:-
-  F.  «-  (  =  L.  rf),  back  ;  taurner,  lu  in tornado,    a    horricauc.    (Spatj.  •  1
Properly  tomada,  *  i.  e.  a  retam,  or  \yam about,  a  sadden  storm  al  sea;'  HlouaL Span,  tomada,  a  return,  turn  about;  <^ fern,  of  pp.  of  torrtar,  to  tum.  ^I*  /ptm to  tum  ^abovc). tour,  a  drcuit  (F.— L.)     Lit.  'aUB
—  F.  tour,  lit.  a  tum  ;    verbal  sb.  frtdB tcunur,  to  tum ;  see  Turn.
tournament  (F.  -  L.)  M.  E.  ttr mcni.^O.  F.  tomoiemeHt,  a  toumcia (Burguy^  —  O.  F.  toumjicr,  to  joiat O.  F.  tomoi,  ioruei^  a  tourney,  joust ;  ill turning  about  — O.  F.  iaruer,  to  nun Turn.
tourney.  (F.-L.)  O.F./<»niw(abOT toumiquot.  (F.  —  L.)  \' Joumi^ud,\ '  that  which  tuin$  about  ;*  a  name  gms a  stick  turned  round  to  tighten  a  tiAodii to  stop  a  flow  ol'  blood.  — F.  fottnur, tum  (above).
turnpike.  C^-  -  L. ;  oik/  C^    Ff merly  a  name  given  to  the  old-fasbi tum-stile,  which  icvqIvc^I  on  the  top  ol post.     From  Tum  and  Pike.
Turnip,  Tumep.  a  plant.  (F.  -  1 and  L.)  The  laltei  part  of  the  woid M.E.  rtej^e,  a  lumip,  A.S.  ui/>,  borroii from  L,  Hdfms,  a  kind  of  turnip ;  cf.  \i and  Gael.  niip»  a  turnip,  p.  The  fom part  appears  lo  be  F.  tour  m  the  seni '  wheel,*  lo  signify  its  round  shajic  ;  It  1 as  if  it  had  been  turned.  A  tuincf**  whi was  formerly  called  a  turn  isx  Eag tuur  in  French.     Sec  Turn
Turpentine :  see  T«r«bintli.
Turpitude.  (.F,-L.)   F./wr turpitude  baseness.- L.  hiwfu.
Turquoise ;  see  Turkey.
```


## [2026-10-15T02:48:01.096Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i \"tadarv\\|taSarv\\|tadarw\\|ta8arv\\|taöarv\\|Fasan\" HRN.txt HUB.txt NYB_vol2_glossary.txt | head; grep -n -a \"تذرو\\|تدرو\" incoming/ARY/ARY_pages.txt | head -3"
}
```


### [2026-10-15T02:48:01.566Z] TOOL RESULT

```
HUB.txt:1604:379. Die zu np. tadarv Tasan ^ (Fird. I, 485, Z. 3) ge-
HUB.txt:6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
HUB.txt:6708:*Feuer*, taSarv 'Fasan* fRebhuhn* nach Sal. Shuk.), kdyaS *Papier*
HUB.txt:10748:taSarv 47.
HRN.txt:3564:'Birkhuhn, ksl. teMüi *Fasan*, urverwandt mit skr.
```


## [2026-10-15T02:48:03.432Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3555,3570p HRN.txt; sed -n 1600,1612p HUB.txt; for l in 3560 ; do head -n $l HRN.txt | grep -c $'\\f'; done; head -n 1604 HUB.txt | grep -c $'\\f'"
}
```


### [2026-10-15T02:48:03.847Z] TOOL RESULT

```
töxnmk bezw. tu/m/ak, päz. tti/m, arm. LW. tohm;
ai. tokman- 'Schössling'.
kurd. töm; wa/. tay^Hy sar. töym, yidg. tüyum.
*) Pehlv. pancötak hat ein mir unverständliches ö; darum scheinen
mir auch de Goeje's (ZDMG. 35, 340) auf ihm beruhende, sonst sehr
ansprechende arab. dahötah^ Instötah zweifelhaft.— 85 —
379. teöerv Tasan'.
med. TBxaQoq, mrvonu; Tasan' (Athen. IX, p. 387 DE).
Lit. tetervas, tetervinas ^Birkhahn', apreuss. tatanvis
'Birkhuhn, ksl. teMüi *Fasan*, urverwandt mit skr.
tittirU^ tittiri' *Rebhuhn', lit. tytaras 'Truthahn', gr. LW.
TbXQai etc.^), an, piäurr *Auerhahn' (Fick, Et. Wort.).
380. {i)-ter Comparativsuffix, vergl. hetterter,
ap. -tara- (in apatara-); aw. ai. -tara-; phlv. -tar
(sogar azadihatar Aogem.).
kurd. 'ter ^ auch vor dem Adjektiv; oss. d. -der,
phi. tuxsak 'diligent* Shk. 269 etc. Wurzel ist tvaks
(= zd. d^waxS) auf mittlerer Stufe, tuk^ (= phi. paz.
tux§) auf der Nullstufe. Uebrigens ist tux^a ein Parsen-
wort, siehe die Belegstelle bei Vullers.
379. Die zu np. tadarv Tasan ^ (Fird. I, 485, Z. 3) ge-
h5rigen Worter sind nach Hehn* p. 355 medischen
Ursprungs, wahrend Schrader (ebenda p. 357) mit
F i c k einen idg. Vogelnamen "^feiero-, Hetervo- ansetzt.
383. Horn hatte die Bemerkungen von Ah reus und
Hoffmann mittheilen sollen, um die Gleichung: np.
tar *ein Vogel' (avis parva, parum quiescens et canora',
Vullers) =^ lat. sturnus, d. Staar wahrscheinlich zu
machen. Der 'Staar heisst sonst im Np. sar.
99
49
```


## [2026-10-15T02:48:09.143Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo $(( $(head -n 31733 SOD_pages.txt | grep -c $'\\f') - 66 )); head -n 30202 BQT_v1_pages.txt | grep -c $'\\f'; head -n 29150 BQT_v1_pages.txt | grep -c $'\\f'; head -n 39567 MON_part1.txt | grep -c $'\\f'"
}
```


### [2026-10-15T02:48:09.844Z] TOOL RESULT

```
391
717
694
0
```


## [2026-10-15T02:50:50.547Z] TOOL CALL #48: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-506.json",
 "content": "{\n  \"pdf_page\": 506,\n  \"book_page\": 476,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ters\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ters- 'to be dry, to dry' (Pokorny ters- 1078-1079; Watkins/AHD ters-; Wiktionary *ters-)\",\n      \"note\": \"Pokorny IEW 1078-1079 'ters- dry; thirst' lists exactly the material of this chart: Avestan taršu-, taršna- 'thirst', Latin torreō, terra, Germanic *þurs- (Gothic þaurstei, OE þurst). Watkins (AHD) ters- 'to dry' derives THIRST, TERRACE, TERRAIN, TERRESTRIAL, TERRITORY, MEDITERRANEAN, SUBTERRANEAN from it; Klein s.v. terra and toast likewise. Root, label and gloss are correct. Problems are small: the book prints Latin 'turrĕre' for torrēre (author's misprint), 'medi-terrâneous' is an anglicized rendering of Latin mediterrāneus, Germanic 'thurs' is only the stem *þurs- of *þurstuz, and English 'territory' (Latin territōrium) is usually but not universally referred to terra. No extraction errors: the JSON matches the printed page.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ters- «خشک بودن، خشکیدن» است؛ پوکورنی (ص۱۰۷۸–۱۰۷۹) آن را با معنای «خشک؛ تشنگی» آورده و اوستایی taršu- «خشک» و taršna- «تشنگی»، لاتین terra و torreō و ژرمنی *þurs- (گوتی þaurstei، انگلیسی کهن þurst) را زیر آن گذاشته است؛ واتکینز و کلاین نیز همین را می‌گویند. پس ریشه، برچسب زبان و معنای نورایی درست است. اشکال‌ها جزئی است: «turrĕre» در کتاب خطای چاپی به جای torrēre است، «thurs» تنها ستاکِ ژرمنی است، و پیوند territory با terra پذیرفتهٔ بیشترِ منابع است ولی همگانی نیست. خطای استخراج دیده نشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ters-\",\n        \"https://en.wiktionary.org/wiki/terra\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1078\", \"status\": \"supports\", \"note\": \"POK_full.txt line 86339 'Root / lemma: ters- Meaning: dry; thirst' (Page(s): 1078-1079): 'Avestan tarsu- dry, that is to say not fluid'; 'Avestan tarsna-m. thirst'; 'Latin torreo, -ere, -ui, tostum'; 'here also Latin terra earth'; 'Gothic þaurstei, Old English þurst, Old High German durst thirst'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 737 f. (WLD_Bd1_pages.txt ~l. 69815-69935)\", \"stance\": \"supports\", \"note\": \"'lat. torreo -ere, -ui, tostum dorren, braten, rosten'; 'auch lat. terra Erde ... aus ital. *terso-, *tersā'; 'got. þaursjan dürsten ... ags. þurst, ahd. durst Durst'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt line 1083 s.v. ters-\", \"stance\": \"supports\", \"note\": \"'ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst ... THIRST ... 2. Suffixed form *ters-ā- in Latin terra, \\\"dry land,\\\" earth ... TERRACE, (TERRAIN) ... TERRESTRIAL ... TERRITORY ... MEDITERRANEAN ... SUBTERRANEAN'.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 18441 ters- (1); line 19188 trs- (1)\", \"stance\": \"supports\", \"note\": \"'ters- (1) rub, dry. WP I, 737 ... Lat. cf. terra (lit. dry land)'; 'trs- (1) dry; parched ... Av. tərəš-, Per. tiš, tišne'.\"},\n        {\"src\": \"SYN\", \"where\": \"5.15 THIRST (SYN.txt ~l. 8460)\", \"stance\": \"supports\", \"note\": \"'Derivs. of IE *ters- in Grk. τέρσομαι become dry, Lat. torrere make dry, Goth. þaursjan be thirsty ... Walde-P. 1.737f.'; 'Skt. tṛṣṇā-, Av. taršna-'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"taršu; taršna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. taršu- 'dry, solid (not liquid)' continues Proto-Iranian *táršuš < PIE *tr̥s-ú- (= Skt. tṛṣú- 'greedy, thirsting', Goth. þaursus 'dry'); Av. taršna- m. 'thirst' continues PIr. *tŕ̥šnah < PIE *tr̥s-nó- (= Skt. tṛṣṇā- 'thirst'). Both are zero-grade *tr̥s- forms; PIE syllabic *r̥ before s gives Avestan ar, and *s after r becomes š by the ruki rule.\",\n          \"derivation_fa\": \"اوستایی taršu- «خشک، جامد» و taršna- «تشنگی» هر دو از درجهٔ صفرِ ریشه، یعنی *tr̥s-، ساخته شده‌اند: *tr̥s-ú- و *tr̥s-nó-؛ r هجایی در اوستایی ar شده و s پس از r بنا بر قاعدهٔ «روکی» به š بدل شده است. همتای سنسکریت آن‌ها tṛṣú- و tṛṣṇā- است. بارتولومه taršna- را «تشنگی» معنا کرده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ters-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1078\", \"status\": \"supports\", \"note\": \"POK_full.txt l. 86342-86346: 'Avestan tarsu- dry, that is to say not fluid' ... 'Avestan tarsna-m. thirst'.\"},\n            {\"ref\": \"KLN:1592\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l. 38688 s.v. terra: 'fr. I.-E. base *ters-, *trs-, to be dry, whence also OI. tarṣayati, tṛṣyati thirsts ... Avestic tarshu-, dry, solid'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt l. 12122 (col. ~646)\", \"stance\": \"supports\", \"note\": \"'tarSna- m. Durst' with Yt and Vd citations; 'ai. vgl. tṛṣṇā- f.'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l. 5074\", \"stance\": \"supports\", \"note\": \"'Np. tiš Durst, tišna durstig = zd. taršna- Durst, skr. tṛṣṇā- Durst, tṛṣnaj durstig, tṛṣu- lechzend'.\"},\n            {\"src\": \"IEC\", \"where\": \"l. 19188 trs- (1)\", \"stance\": \"supports\", \"note\": \"'Av. tərəš-, Per. tiš, tišne'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"tišn; tišnak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian tišn 'thirst' and tišnag [tyšnk'] 'thirsty' continue Old Iranian *tr̥šna- (Av. taršna-) with -aka- suffix; Old Iranian syllabic *r̥ after a dental gives MP i (cf. *tr̥š- > tiš-). MacKenzie and Horn give exactly these forms.\",\n          \"derivation_fa\": \"فارسی میانهٔ tišn «تشنگی» و tišnag (به خط پهلوی tyšnk') «تشنه» از ایرانی باستان *tr̥šna- (اوستایی taršna-) و پسوند -aka- آمده‌اند؛ r هجایی ایرانی باستان پس از دندانی در فارسی میانه به i بدل شده است. مکنزی و هرن همین صورت‌ها را آورده‌اند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تشنه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The book cites no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt l. 5000 (and index l. 7753)\", \"stance\": \"supports\", \"note\": \"'tišnag [tyšnk | M tyšng, N ~a] thirsty'; English index 'thirst tišn, tišnagīh'.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"grep 'tišn', 'tišnak', 'tisn' found no headword (only -išn verbal nouns).\"},\n            {\"src\": \"HRN\", \"where\": \"no. 388, HRN.txt l. 3644-3647\", \"stance\": \"supports\", \"note\": \"'388. tiš Durst, tišne ... aw. taršna- Durst; phlv. tišn, tišnak, tišnakīh'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"tešneh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP tešne/tešna (تشنه) 'thirsty' < MP tišnag with loss of final -g and lowering of i to e in Iranian Persian; tešnegi 'thirst' is the abstract in -egi. Ultimately PIr. *tŕ̥šnakah < PIE *tr̥s-nó-. The verse 'āb-e daryā gar hame natvān kešid / pas be qadr-e tešnegi bāyad češid' is from Rumi's Masnavi.\",\n          \"derivation_fa\": \"«تشنه» از فارسی میانهٔ tišnag است؛ گ پایانی افتاده و i در فارسی ایران به e گراییده است (tešne). «تشنگی» اسم معنا با پسوند -گی است. ریشهٔ دورتر ایرانی باستان *tŕ̥šnakah و هندواروپایی *tr̥s-nó- است. معین در حاشیهٔ برهان، هرن و هوبشمان همین سیر را آورده‌اند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تشنه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:499\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt l. 30202-30205 (block 717, printed p. ~499): headword 'تشنه' with Mo'in's footnote (OCR rough): 'پهلوی tišnak از tišn ... اوستایی taršna «بارتلمه ۶۴۶» سانسکرت tṛṣṇā ... اورامانی ... گیلکی ...'; 'دارندهٔ عطش، که تشنگی دارد'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 388\", \"stance\": \"supports\", \"note\": \"'tiš Durst, tišne (tešne Šāhn.), tišnegī ... aw. taršna-; phlv. tišn, tišnak'.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l. 5074 (p. ~92)\", \"stance\": \"supports\", \"note\": \"'Np. tiš Durst, tišna durstig = zd. taršna-'.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt l. 5759, pdf p. 196 = printed p. 197\", \"stance\": \"supports\", \"note\": \"entry 'تشنه، تش، تشنگی' under the 'dry' root, citing برهان قاطع and فرهنگ معین ۱۱۶۴ (OCR of the forms garbled).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"terra; medi-terrâneous; turrěre\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Latin terra 'earth, (dry) land' < Proto-Italic *tersā < PIE *ters-eh₂ 'the dry' (de Vaan; Oscan teerúm 'territory'), -rs- assimilated to -rr-. Latin mediterrāneus 'inland, in the middle of the land' = medius + terra + -āneus (the book's 'medi-terrâneous' is an anglicized spelling). The verb is torrēre 'to parch, roast' (pp. tostus) < Proto-Italic *torseō < PIE causative *tors-éye-; the book prints 'turrĕre', which is Nourai's misprint for torrēre (the JSON is faithful to the page).\",\n          \"derivation_fa\": \"لاتین terra «زمین، خشکی» از ایتالیک آغازین *tersā و هندواروپایی *ters-eh₂ «خشکی» است و rs در آن به rr همگون شده است. mediterrāneus «میان‌زمینی» از medius «میانه» + terra + پسوند -āneus ساخته شده (صورت medi-terrâneous در کتاب املای انگلیسی‌شده است). فعل «خشکاندن، برشته کردن» در لاتین torrēre است (صفت مفعولی tostus) از سببیِ *tors-éye-؛ «turrĕre» کتاب خطای چاپی نورایی است و استخراج درست است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"turrĕre\",\n          \"correct_form\": \"torrēre\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/terra\",\n            \"https://en.wiktionary.org/wiki/torreo\",\n            \"https://en.wiktionary.org/wiki/Mediterranean\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 ters-: 'Suffixed form *ters-ā- in Latin terra, \\\"dry land,\\\" earth ... MEDITERRANEAN, SUBTERRANEAN'.\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l. 38688 s.v. terra: 'L., prob. for *tersa- and lit. meaning dry land and rel. to OL. torrus (for *torsus) dry, L. torrere, to parch, roast'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1078\", \"stance\": \"supports\", \"note\": \"'Latin torreo, -ere, -ui, tostum dehydrate, desiccate, fry'; 'here also Latin terra earth ... from Italian *terso-, *tersa'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 737 f.\", \"stance\": \"supports\", \"note\": \"'lat. torreo -ere, -ui, tostum'; 'lat. terra Erde ... aus ital. *terso-, *tersā'.\"},\n            {\"src\": \"IEC\", \"where\": \"l. 18441\", \"stance\": \"supports\", \"note\": \"'Lat. cf. terra, f. (lit. dry land)'.\"}\n          ],\n          \"page_image\": \"data/verification/sources/refs/ocr/BOOK/506.png\"\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"terrasse; Mediterranee\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French terrasse 'terrace' (Middle French terrace/terrasse 'pile of earth, platform') comes from Old Occitan terrassa < Vulgar Latin *terrācea, a derivative of terra. French (mer) Méditerranée is from the Latin adjective mediterrāneus 'inland', applied in late Latin (Isidore, mare Mediterraneum) to the sea 'in the middle of the lands'.\",\n          \"derivation_fa\": \"فرانسوی terrasse «تراس، سکوی خاکی» از اوکسیتانی کهن terrassa و لاتین عامیانهٔ *terrācea، برساخته از terra، است. Méditerranée از صفت لاتین mediterrāneus «میان‌زمینی» آمده که در لاتین متأخر برای دریای «میان سرزمین‌ها» به کار رفت. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/terrasse\",\n            \"https://en.wiktionary.org/wiki/Méditerranée\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1329\", \"status\": \"supports\", \"note\": \"1976 AHD page not online; Watkins 1985 ters- has 'Latin terra ... (> French and Old French terre, earth, ground): TERRACE ... MEDITERRANEAN'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. terrace (after l. 38688)\", \"stance\": \"supports\", \"note\": \"'terrace, n. — MF. terrasse, terrace, pile of earth, terrasse (whence F. terrasse), fr. OProvenç. ...' — the source of Nourai's gloss 'pile of earth'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"grep '^TERRACE' found no separate headword in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"(script only) تراس ، مدیترانه\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian terās (تراس) 'terrace, balcony' and Mediterāne (مدیترانه) are 19th-20th-century loans from French terrasse and Méditerranée; the older native name of the sea is baḥr-e rum (بحر الروم).\",\n          \"derivation_fa\": \"«تراس» و «مدیترانه» وام‌واژه‌های تازهٔ فارسی از فرانسوی terrasse و Méditerranée‌اند که در دورهٔ قاجار و پهلوی وارد زبان شدند؛ نام کهن‌تر این دریا در فارسی «بحرالروم» بوده است (معین هم «بحرالروم (مدیترانه)» می‌نویسد). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تراس\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1060\", \"status\": \"partial\", \"note\": \"Only the 2-vol Adena abridgement is on disk: MON_part1.txt l. 39567 'تراس: [فر.] (اِ.) بام، پشت‌بام، ایوان' (origin tag garbled in OCR as 'د۱5'); confirms the word and its French tag, page 1060 of the 6-vol ed. cannot be mapped.\"},\n            {\"ref\": \"MON6:1941\", \"status\": \"not_checked\", \"note\": \"Mo'in's proper-name volume 6 is not online or on disk; MON_part2.txt only shows 'بحر الروم (مدیترانه)' in definitions (l. 27371, 52680).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt l. 39567; MON_part2.txt l. 27371\", \"stance\": \"supports\", \"note\": \"'تراس: ... بام، پشت‌بام، ایوان'; 'بحر الروم (مدیترانه)'.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'تراس', 'مدیترانه' found nothing (ARY covers native IE words only).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"terrace\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English terrace (late 15th c.) is borrowed from Middle French terrace/terrasse 'platform, pile of earth' < Old Occitan terrassa < VL *terrācea < Latin terra; doublet of the modern borrowing terrasse.\",\n          \"derivation_fa\": \"انگلیسی terrace در سدهٔ پانزدهم از فرانسوی میانه terrace/terrasse «سکوی خاکی» وام گرفته شده که از اوکسیتانی کهن terrassa و سرانجام لاتین terra است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/terrace\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 ters-: TERRACE listed under Latin terra (> French terre).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. terrace\", \"stance\": \"supports\", \"note\": \"'terrace, n. — MF. terrasse, terrace, pile of earth'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"no separate TERRACE headword found by grep.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"terrain, terrestrial, territory; Mediterranean, subterranean; toast\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"terrain < French terrain < Latin terrēnum 'ground'; terrestrial < Latin terrestris; Mediterranean < Latin mediterrāneus; subterranean < Latin subterrāneus (sub + terra) — all from terra. toast < ME tosten < Old French toster < Late Latin *tostāre, frequentative of torrēre (pp. tostus), i.e. from the verb, not from terra. territory < Latin territōrium: traditionally 'land around a town' from terra (Watkins, Klein), but an alternative derivation from terrēre 'to frighten' ('place from which people are warned off') is also discussed, so this one item is only plausible; terrain also came via French, not straight from Latin.\",\n          \"derivation_fa\": \"terrain از فرانسوی terrain و لاتین terrēnum، terrestrial از لاتین terrestris، Mediterranean از mediterrāneus و subterranean از subterrāneus (sub «زیر» + terra) همه از terra «زمین» آمده‌اند. toast از فرانسوی کهن toster و لاتین متأخر *tostāre، بسامدیِ torrēre «برشته کردن»، است. territory از لاتین territōrium است که بیشتر منابع آن را از terra می‌دانند ولی برخی از terrēre «ترساندن» گرفته‌اند؛ پس این یک قلم با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/terrain\",\n            \"https://en.wiktionary.org/wiki/terrestrial\",\n            \"https://en.wiktionary.org/wiki/territory\",\n            \"https://en.wiktionary.org/wiki/subterranean\",\n            \"https://en.wiktionary.org/wiki/Mediterranean\",\n            \"https://en.wiktionary.org/wiki/toast\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 ters-: '(TERRAIN), TERRAN, TERRENE, TERRESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN'. (TOAST is not listed there; Watkins puts torrēre under ters- in other editions.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 39391 s.v. toast; l. 38688 s.v. terra\", \"stance\": \"supports\", \"note\": \"'toast ... fr. MF. toster, to roast, fr. OF., fr. VL. *tostare ... freq. of L. torrere (pp. tostus), to parch, roast, fr. I.-E. base *trs-, to be dry'; terra: 'Cp. ... mediterranean, ... subterranean, ... terrain, ... terrestrial, ... territory, thirst, toast, torrid'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"greps for '^TERRITORY', '^TOAST' gave no clean headwords in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"thurs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *þurs- is the zero grade *tr̥s- (PIE *r̥ > Gmc ur, *t > þ by Grimm's law); with the suffix -tu- it gives *þurstuz 'thirst' (Gothic þaurstei, ON þorsti, OHG durst, OE þurst). The book's 'thurs' is this stem (Watkins' 'Germanic *thurs-'), not an attested word.\",\n          \"derivation_fa\": \"ژرمنی آغازین *þurs- درجهٔ صفر ریشه (*tr̥s-) است: r هجایی به ur و t بنا بر قانون گریم به þ بدل شده؛ با پسوند -tu- واژهٔ *þurstuz «تشنگی» (گوتی þaurstei، انگلیسی کهن þurst، آلمانی کهن durst) پدید آمده است. «thurs» کتاب همان ستاک است نه واژه‌ای مستقل؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ters-\",\n            \"https://en.wiktionary.org/wiki/thirst\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 ters-: 'Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1078-1079\", \"stance\": \"supports\", \"note\": \"'Gothic þaursjan dürsten ... Gothic þaurstei, Old Icelandic þorsti, Old English þurst, Old High German durst thirst'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 737 f.\", \"stance\": \"supports\", \"note\": \"'got. þaursjan dürsten ... got. þaurstei f., aisl. þorsti m., ags. þurst, ahd. durst Durst'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"thirst\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English thirst < ME thirst, earlier thurst < OE þurst < Proto-West-Germanic *þurstu < PGmc *þurstuz; the vowel i (with r-metathesis in ME thirst) was taken over from the verb þyrstan (i-umlaut of u).\",\n          \"derivation_fa\": \"انگلیسی thirst از انگلیسی میانه thurst/thirst و انگلیسی کهن þurst و ژرمنی آغازین *þurstuz است؛ واکهٔ i زیر تأثیر فعل þyrstan (با دگرگونی i-umlaut) جای u را گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/thirst\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The book cites no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 39065 s.v. thirst, n.\", \"stance\": \"supports\", \"note\": \"'thirst, n. — ME. thirst, fr. earlier thurst, fr. OE. þurst ... Goth. þaurstei, fr. I.-E. base *trs-, to be dry'.\"},\n            {\"src\": \"SYN\", \"where\": \"5.15 THIRST\", \"stance\": \"supports\", \"note\": \"'Goth. þaurstei, OE þurst, etc. general Gmc.' from IE *ters-.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Teter\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *tet(e)r- reduplicated onomatopoeic root 'to cackle, quack; gallinaceous bird' (Pokorny tet(e)r- 1079; WP I 718)\",\n      \"note\": \"Pokorny 1079 'tet(e)r- to quack (expr. root)' with Skt. tittira-, NP tadarv 'pheasant', Greek τετράων 'grouse', Lith. tetervas, OCS tetrěvь. Nourai's 'chatter' is a fair gloss of 'gackern'. Problems are in the descendants: (1) the Pahlavi form is tadar(w) [ttl] (MacKenzie), not 'titar'; (2) Sogdian is ttr'w tatarw (Gharib 9698), not 'tt'rw', and it is a sister of Middle Persian, not a descendant; (3) the 'Medit' box is Horn's/Mann's 'med.'/'Medic' = Median, and 'tetatos' is a misprint for τέταρος; (4) Latin turtur and English turtle(dove) are parallel imitative words, not derived from Greek τετράων, and English tortoise/turtle 'reptile' are unrelated (tortoise < Medieval Latin tortuca; turtle 'reptile' is an alteration of French tortue). The NOTE 'POK claims this is derived from Persian' misstates Pokorny: he says Greek τατύρας, τέταρος (not τετράων) are of Persian origin (following Walde-Pokorny and Hehn). No extraction errors: the JSON matches the printed page.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی *tet(e)r- ریشه‌ای تکراری و نام‌آوا برای «قدقد کردن» و نام پرندگان ماکیان‌سان است (پوکورنی ص۱۰۷۹)؛ «Teter: وراجی کردن» نورایی پذیرفتنی است. ولی در شاخه‌ها چند خطا هست: صورت پهلوی «tadar(w)» است نه «titar»؛ صورت سغدی ttr'w (tatarw) است و سغدی هم‌ریشهٔ پهلوی است نه برگرفته از آن؛ «Medit» همان «مادی» است و «tetatos» خطای چاپی به جای τέταρος است؛ لاتین turtur و انگلیسی turtle (قمری) نام‌آوای جداگانه‌اند و از یونانی τετράων نیامده‌اند، و tortoise «لاک‌پشت» اصلاً ربطی به این ریشه ندارد. یادداشت کتاب هم سخن پوکورنی را درست نقل نکرده: او τατύρας و τέταρος یونانی را برگرفته از فارسی (مادی) می‌داند، نه τετράων را. خطای استخراج دیده نشد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/تذرو\",\n        \"https://en.wiktionary.org/wiki/τετράων\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1079\", \"status\": \"supports\", \"note\": \"POK_full.txt l. ~86392 'Root / lemma: tet(e)r- Meaning: to quack (expr. root)': 'Old Indie tittira-, tittirī- partridge'; 'npers. tadarv pheasant (also gr. τατύρας, τέταρος ds. are of pers. origin)'; 'gr. τετράων m. grouse'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I 718 (WLD_Bd1_pages.txt l. 67719-67726)\", \"stance\": \"supports\", \"note\": \"'tet(e)r- redupl. Schallwort gackern, hühnerartige Vogel u. dgl. Ai. tittira-h, tittiri-h Rebhuhn ... npers. tadarv Fasan (auch gr. τατύρας, τέταρος ds. sind pers. Ursprungs)'.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt l. 18458 s.v. teteruos\", \"stance\": \"supports\", \"note\": \"'teteruos (tetruos) heathcock, capercailie. WP I, 718. Onomat. Skt. tittirah francolin, partridge; Medic tétaros, tatúras pheasant; Per. tazarv id.; Gk. cf. tétrix & tétrax'.\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 38776 s.v. Tetraonidae\", \"stance\": \"supports\", \"note\": \"'L. tetrao, heath cock, fr. Gk. τετράων ... derives from a base of imitative origin. Cp. OI. tittirah, ModPers. tadarv pheasant, L. ... turtur turtledove'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"titar\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Middle Persian word for 'pheasant' is written ttl (= tdr) and read tadar(w) by MacKenzie (N taδarw), continuing Proto-Iranian *tatr̥wa- (Wiktionary *tatr̥wáh), a reduplicated imitative bird name. The book prints 'titar', a non-standard reading of the ambiguous Pahlavi spelling (perhaps influenced by Skt. tittira-); the JSON copies the book faithfully, so the error is Nourai's.\",\n          \"derivation_fa\": \"واژهٔ پهلوی «قرقاول» به خط پهلوی ttl نوشته می‌شود و مکنزی آن را tadar(w) می‌خواند (فارسی نو تَذَرو)؛ از ایرانی باستان *tatr̥wa-، نامی تکراری و نام‌آوا برای پرنده. «titar» کتاب خوانشی نادرست از این املای مبهم است (شاید زیر تأثیر سنسکریت tittira-)؛ استخراج با کتاب یکی است و خطا از خود نورایی است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"titar\",\n          \"correct_form\": \"tadar(w)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تذرو\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1079\", \"status\": \"partial\", \"note\": \"Pokorny cites only 'npers. tadarv pheasant' — no Pahlavi form.\"},\n            {\"ref\": \"KLN:1596\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l. 38776 s.v. Tetraonidae: 'ModPers. tadarv, pheasant' — no Pahlavi form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt l. 4877 (p. 81)\", \"stance\": \"contradicts\", \"note\": \"'tadar(w) [ttl | (N taδarw)] pheasant' — the reading is tadar(w), not titar.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"grep 'tadar', 'titar', 'pheasant' found nothing.\"},\n            {\"src\": \"SOD\", \"where\": \"entry 9698\", \"stance\": \"contradicts\", \"note\": \"Gharib compares Sogdian tatarw with 'Pahl. tadarw'.\"}\n          ],\n          \"page_image\": \"data/verification/sources/refs/ocr/BOOK/506.png\"\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"tazarv\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP tazarv/tadarv (تذرو, Classical taḏarw) 'pheasant' < MP tadarw < PIr. *tatr̥wa-; post-vocalic d became the fricative ḏ (ذ) in Early New Persian, later z in Iranian pronunciation. Arabic tadruǧ/taḏruǧ (تدرج، تذرج) is an Arabicization of the Persian word. The verse 'be bālā-ye bekardār-e āzād sarv / be rox čun bahār-o be raftan tazarv' is from Ferdowsi.\",\n          \"derivation_fa\": \"«تذرو» (در فارسی کلاسیک taḏarw، امروز tazarv) از فارسی میانهٔ tadarw و ایرانی باستان *tatr̥wa- است؛ دِ پس از واکه در فارسی دری به ذال سایشی و سپس در تلفظ ایرانی به ز بدل شده است. «تدرج/تذرج» عربی معرّبِ همین واژهٔ فارسی است. معین در حاشیهٔ برهان، هرن و هوبشمان همین را آورده‌اند؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تذرو\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:478\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt l. ~29140-29175 (block 694-695): 'تذرو ... نام مرغی است صحرایی شبیه بخروس در نهایت خوش‌رویی و خوش‌رفتاری'; Mo'in's footnote (OCR rough): 'پهلوی tatarv ... در سانسکریت tittiri بمعنی کبک «اسشق ۳۷۹». معرب آن تدرج و تذرج' and the Manuchehri verse 'برسر سرو زند پردهٔ عشاق تذرو'.\"},\n            {\"ref\": \"IEC:1388\", \"status\": \"supports\", \"note\": \"IEC.txt l. 18458: 'Per. tazarv, s. id. (and jungle-cock)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 379, p. 85 (HRN.txt l. 3561-3566)\", \"stance\": \"supports\", \"note\": \"'379. teδerv Fasan. med. τέταρος, τατύρας Fasan (Athen. IX, p. 387 DE) ... urverwandt mit skr. tittiri- Rebhuhn'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 39, no. 379 (HUB.txt l. 1604)\", \"stance\": \"partial\", \"note\": \"'Die zu np. tadarv Fasan (Fird. I, 485) gehörigen Wörter sind nach Hehn medischen Ursprungs, während Schrader mit Fick einen idg. Vogelnamen *tetero-, *tetervo- ansetzt'.\"},\n            {\"src\": \"PHD\", \"where\": \"l. 4877\", \"stance\": \"supports\", \"note\": \"'tadar(w) [ttl | (N taδarw)] pheasant'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"tt`rw\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Gharib no. 9698 gives Buddhist Sogdian ttr'w, read tatarw 'pheasant', compared with Pahlavi tadarw. The book prints tt'rw (aleph misplaced); the JSON copies the book, so the slip is Nourai's. Sogdian tatarw also does not come from Pahlavi as the arrow implies: both continue Proto-Iranian *tatr̥wa-, Sogdian keeping intervocalic t.\",\n          \"derivation_fa\": \"قریب (شمارهٔ ۹۶۹۸) صورت سغدی بودایی را ttr'w با خوانش tatarw «قرقاول» آورده و آن را با پهلوی tadarw سنجیده است. کتاب tt'rw چاپ کرده (الف جابه‌جا شده) و استخراج همان را آورده است، پس خطا از کتاب است. افزون بر این، سغدی از پهلوی نیامده بلکه هر دو از ایرانی باستان *tatr̥wa- هستند و سغدی t میان‌واکه‌ای را نگه داشته است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"tt'rw\",\n          \"correct_form\": \"ttr'w (tatarw)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/تذرو\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:392\", \"status\": \"partial\", \"note\": \"SOD_pages.txt l. 31733-31736 (printed p. ~391-392): '9698 ttr'w B tatarw cf. Pahl. tadarw pheasant TSP 3.9, 14 ...' — word and meaning confirmed, spelling ttr'w not tt'rw, and Gharib marks Pahlavi as a comparison, not a source.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entry 9698\", \"stance\": \"partial\", \"note\": \"'ttr'w B tatarw ... Pahl. tadarw ... pheasant'.\"},\n            {\"src\": \"PHD\", \"where\": \"l. 4877\", \"stance\": \"supports\", \"note\": \"Pahlavi cognate 'tadar(w) pheasant'.\"}\n          ],\n          \"page_image\": \"data/verification/sources/refs/ocr/BOOK/506.png\"\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Medit\",\n          \"words\": \"tetatos, taturas\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"These are the Greek glosses τέταρος (Hesychius) and τατύρας (Athenaeus IX 387, the pheasant reared by Ptolemy) for 'pheasant', which Horn labels 'med.' (Median) and Mann 'Medic tétaros, tatúras', regarded since Hehn as loans from a Median/Iranian *tatarwa-. The book's label 'Medit' is a misprint or mis-copy of Mann's 'Medic', and 'tetatos' is a misprint for tetaros; the JSON faithfully reproduces the printed page.\",\n          \"derivation_fa\": \"این دو، واژه‌های یونانیِ τέταρος (در هسوخیوس) و τατύρας (در آتنایوس، کتاب نهم، ص۳۸۷) به معنای «قرقاول»اند که هرن آن‌ها را «مادی» و مان «Medic» نامیده‌اند و از زمان هِن وام‌واژه‌ای از مادی/ایرانی *tatarwa- دانسته می‌شوند. «Medit» در کتاب خطای چاپی یا رونویسی نادرستِ «Medic» (مادی) است و «tetatos» خطای چاپی به جای tetaros؛ استخراج با کتاب یکی است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Medit: tetatos, taturas\",\n          \"correct_form\": \"Median (Greek glosses) tetaros, tatyras\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1388\", \"status\": \"supports\", \"note\": \"IEC.txt l. 18458: 'Medic tétaros, tatúras, s. (pheasant)' — Nourai's 'Medit ... tetatos' is a mis-copy of this line.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 379, p. 85\", \"stance\": \"supports\", \"note\": \"'med. τέταρος, τατύρας Fasan (Athen. IX, p. 387 DE)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 718\", \"stance\": \"supports\", \"note\": \"'auch gr. τατύρας, τέταρος ds. sind pers. Ursprungs'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1079\", \"stance\": \"supports\", \"note\": \"'also gr. τατύρας, τέταρος ds. are of pers. origin'.\"}\n          ],\n          \"page_image\": \"data/verification/sources/refs/ocr/BOOK/506.png\"\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"tittirah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sanskrit tittira- / tittiri- (nom. tittiraḥ) is real and belongs to this reduplicated imitative root (Pokorny, Mayrhofer EWAia I 645-646), but it means 'partridge, francolin', not 'pheasant' as the chart glosses it; the first i is assimilated to the -ir- of the second syllable.\",\n          \"derivation_fa\": \"سنسکریت tittira-/tittiri- (حالت فاعلی tittiraḥ) واژه‌ای واقعی و از همین ریشهٔ تکراری نام‌آواست (پوکورنی، مایرهوفر)، ولی معنای آن «کبک، دُرّاج» است نه «قرقاول»؛ پس پیوند درست ولی معنای داده‌شده دقیق نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/तित्तिरि\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1388\", \"status\": \"supports\", \"note\": \"IEC.txt l. 18458: 'Skt. ... tittirah, m. francolin, partridge' — Mann himself glosses it 'partridge'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1079\", \"stance\": \"supports\", \"note\": \"'Old Indie tittira-, tittirí-, tittírī- partridge, game bird'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I 718\", \"stance\": \"supports\", \"note\": \"'Ai. tittira-h, tittiri-h Rebhuhn'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"tetraon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek τετράων (gen. τετράωνος) 'grouse, capercaillie' (Aristophanes, Aristotle) is an inherited reduplicated imitative bird name from *tet(e)r-, matching Lith. tetervas, OCS tetrěvь, ON þiðurr. The NOTE on this box ('POK claims this is derived from Persian') misreads Pokorny: he (after Walde-Pokorny and Hehn) says only τατύρας and τέταρος 'pheasant' are of Persian (Median) origin; τετράων itself is listed as a native cognate, as in Klein and Mann.\",\n          \"derivation_fa\": \"یونانی τετράων «باقرقره، خروس کوهی» نام پرنده‌ای تکراری و نام‌آوا از ریشهٔ *tet(e)r- است و با لیتوانیایی tetervas و اسلاوی کلیسایی tetrěvь هم‌ریشه است. یادداشت کتاب که «پوکورنی آن را برگرفته از فارسی می‌داند» درست نیست: پوکورنی تنها τατύρας و τέταρος را برگرفته از فارسی (مادی) می‌داند و τετράων را واژهٔ بومی یونانی شمرده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/τετράων\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:1079\", \"status\": \"partial\", \"note\": \"Pokorny lists 'gr. τετράων m. grouse (*τετραϝ-ων)' as a native cognate; the Persian-origin remark applies to τατύρας, τέταρος, not to τετράων as the book's note claims.\"},\n            {\"ref\": \"KLN:1596\", \"status\": \"supports\", \"note\": \"KLN s.v. Tetraonidae: 'Gk. τετράων ... derives from a base of imitative origin. Cp. OI. tittirah ... ModPers. tadarv'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 718\", \"stance\": \"supports\", \"note\": \"τετράων listed among the native forms; Persian origin only for τατύρας, τέταρος.\"},\n            {\"src\": \"IEC\", \"where\": \"l. 18458\", \"stance\": \"supports\", \"note\": \"'Gk. cf. tétrix & tétrax, guinea-fowl, heath-cock' as cognates.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"tetrâô, turtur, turtura\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin tetrao 'grouse' (Pliny) is indeed borrowed from Greek τετράων. Latin turtur 'turtledove' is however an independent onomatopoeic reduplication imitating the bird's coo, related to τετράων only as a parallel imitative formation (Klein 'cp.'), not derived from it; 'turtura' is a Late Latin by-form. The arrow Greek → Latin holds for tetrao only.\",\n          \"derivation_fa\": \"لاتین tetrao «باقرقره» به راستی از یونانی τετράων وام گرفته شده است. ولی turtur «قمری» نام‌آوایی جداگانه و تکراری از آواز این پرنده است و تنها ساختی همانند τετράων دارد، نه این‌که از آن آمده باشد؛ turtura صورت متأخرِ آن است. پس پیکان یونانی ← لاتین تنها برای tetrao درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/turtur\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The book cites no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Tetraonidae (l. 38776) and turtle 'turtledove' (l. 40512)\", \"stance\": \"partial\", \"note\": \"'L. tetrao, heath cock, fr. Gk. τετράων'; 'turtle ... fr. L. turtur ... which is of imitative origin. Cp. Tetraonidae' — tetrao borrowed, turtur only compared.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1079\", \"stance\": \"partial\", \"note\": \"'compare e.g. Latin turtur turtledove' among 'other onomatopoeic words' — a parallel, not a derivative.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"turtle, tortoise\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English turtle 'turtledove' (OE turtle, turtla) is from Latin turtur with dissimilation of r to l, so it belongs with the Latin box. But turtle 'sea reptile' (17th c.) is a sailors' alteration of French tortue, and tortoise (ME tortuce) comes from Medieval Latin tortuca, probably from Late Latin tartarūchus 'of Tartarus' with influence of tortus 'twisted' — neither has anything to do with turtur or τετράων. Only 'turtle (dove)' fits the chart.\",\n          \"derivation_fa\": \"انگلیسی turtle به معنای «قمری» (انگلیسی کهن turtle) از لاتین turtur با دگرشدن r دوم به l آمده و به این شاخه تعلق دارد؛ ولی turtle به معنای «لاک‌پشت دریایی» دگرگون‌شدهٔ فرانسوی tortue در زبان ملوانان است و tortoise از لاتین سده‌های میانه tortuca و احتمالاً tartarūchus «دوزخی» می‌آید. پس tortoise و turtle به معنای لاک‌پشت هیچ پیوندی با این ریشه ندارند و پژوهش امروزی ادعای نورایی را در این بخش رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/turtle\",\n            \"https://en.wiktionary.org/wiki/tortoise\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The book cites no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt l. 39647 tortoise; l. 40513 turtle 'tortoise'; l. 40512 turtle 'turtledove'\", \"stance\": \"contradicts\", \"note\": \"'tortoise ... fr. OProvenç. tartuga, fr. It. tartaruga, which derives fr. VL. tartaruca, lit. the infernal animal, fr. L. Tartarus'; 'turtle, n., tortoise. — Sailor's alteration of F. tortue'; 'turtle, n., turtledove ... fr. L. turtur ... of imitative origin'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l. 20317 TURTLE\", \"stance\": \"silent\", \"note\": \"headword found but the OCR around it is unreadable.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:50:50.612Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-506.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:50:53.443Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-506.json > /dev/null && echo ok; python3 tools/verify_check.py 506"
}
```


### [2026-10-15T02:50:54.182Z] TOOL RESULT

```
ok
nodes verified: 18/18
node verdicts: {'confirmed': 10, 'transcription_suspect': 4, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 14, 'not_checked': 5, 'partial': 5}
books consulted: {'supports': 29, 'silent': 7, 'contradicts': 3, 'partial': 4} | by book: {'KLN': 6, 'POK': 5, 'WLD': 5, 'PHD': 4, 'HRN': 4, 'SKT': 4, 'HUB': 3, 'IEC': 3, 'NYB': 2, 'ARY': 2, 'SOD': 2, 'BRT': 1, 'MON': 1, 'SYN': 1}
```


## [2026-10-15T02:51:02.068Z] TOOL CALL #50: SubagentHandback

```json
{
 "message": "I verified page 506 (book page 476) and wrote the results to /home/sfmqrb/git/rishe-private/data/verification/page-506.json. The JSON is valid, and `verify_check.py 506` covers all 18 of 18 nodes with 0 PROBLEM lines.\n\n**Counts:**\n- **Roots:** 2 confirmed (Ters, Teter).\n- **Nodes:** 10 confirmed, 3 plausible, 1 disputed, 4 transcription_suspect.\n\n**Disputed:**\n- **Teter #8, English \"turtle, tortoise\":** only turtle meaning \"turtledove\" comes from Latin turtur. Turtle meaning the reptile is a sailors' alteration of French tortue. Tortoise comes from Medieval Latin tortuca (probably from tartarūchus, \"of Tartarus\"). Neither is related to this root.\n\n**Transcription_suspect (all are errors in the printed book; the JSON copies the page faithfully):**\n- **Ters #4, Latin \"turrĕre\":** the book's misprint for torrēre.\n- **Teter #1, Pahlavi \"titar\":** MacKenzie reads the Pahlavi spelling ttl as tadar(w), \"pheasant\".\n- **Teter #3, Sogdian \"tt'rw\":** Gharib (no. 9698) has ttr'w, read tatarw. Sogdian is also a sister form of Pahlavi, not derived from it as the arrow shows.\n- **Teter #4, \"Medit: tetatos, taturas\":** this is Mann's \"Medic\" (Median), the Greek glosses τέταρος and τατύρας. \"Tetatos\" is a misprint for tetaros.\n\n**Other points:**\n- The chart's NOTE \"POK claims this is derived from Persian\" misreads Pokorny. He says only τατύρας and τέταρος are of Persian origin. He treats τετράων as a native Greek word.\n- Latin turtur is plausible, not confirmed: it is a separate imitative word, so only tetrao was borrowed from Greek.\n- Sanskrit tittiri means \"partridge\", not \"pheasant\".\n- For English \"territory\", the derivation from terra is the usual view but not certain.\n\n**Extraction errors the owner must fix:** none.\n\nThe 300 dpi page image is saved at /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/506.png. Etymonline returned 403 errors, so I used Wiktionary instead and cite only the archived pages that loaded."
}
```


### [2026-10-15T02:51:02.387Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
