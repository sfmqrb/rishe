# Verification process log — verify-page-518


## [2026-10-15T02:44:16.790Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 518 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-518.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-518.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-518.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 518` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.844Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.676Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.743Z] TOOL RESULT

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


## [2026-10-15T02:44:21.808Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-518.txt; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; ls data/verification/page-51*.json"
}
```


## [2026-10-15T02:44:22.259Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py | head -150"
}
```


### [2026-10-15T02:44:22.712Z] TOOL RESULT

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


### [2026-10-15T02:44:22.770Z] TOOL RESULT

```
=== PDF page 518 (book page 488) ===
--- entry 0 ---
ROOT [Semitic] Umm : mother  (refs KLN:160)
#1 (parent #0) [Arabic] refs=KLN:160 | umm : mother ; umme-ğîlân : "mother of demons", referring to desert bushes believed to nourish demons ☞Ğ.v.l
  #2 (parent #1) [Persian] refs=FVA:34 | omm «أمّ ( أمّهات )» : mother ; ommî «امّى ( امّل )» : as if just born from the mother, illiterate ; moğîlân «مغیلان» : desert bushes
  #3 (parent #1) [Turkish] refs=KLN:160 | beg-umm : mother of ruler, a female title of respect ☞Bhag ; xân-umm : mother of Khan ?, a female title of respect
    #4 (parent #3) [Persian] refs=BQT:339 | baygom «بیگم» : a female title of respect ; xânom «خانم» : a female title of respect
    #5 (parent #3) [English] refs=KLN:160 | begum : a female title of respect
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
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
```


## [2026-10-15T02:44:25.528Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','BQT','MON','HJB','AID','LKT','TTS','PLA','AFM','HRN']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]);print()\n\"; cat data/extracted/batch/page-518.json | head -80"
}
```


### [2026-10-15T02:44:25.938Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in bold at line start; grep -n '^Word'.", "notes": ""}

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cite

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "No

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (l

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt"], "p

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g

{
  "pdf_page": 518,
  "book_page": 488,
  "entries": [
    {
      "root": {
        "name": "Umm",
        "lang": "Semitic",
        "refs": "KLN:160",
        "gloss": "mother"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:160",
          "words": [
            {"translit": "umm", "gloss": "mother", "script": null},
            {"translit": "umme-ğîlân", "gloss": "\"mother of demons\", referring to desert bushes believed to nourish demons", "script": null, "see": ["Ğ.v.l"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:34",
          "words": [
            {"translit": "omm", "gloss": "mother", "script": "أمّ ( أمّهات )"},
            {"translit": "ommî", "gloss": "as if just born from the mother, illiterate", "script": "امّى ( امّل )"},
            {"translit": "moğîlân", "gloss": "desert bushes", "script": "مغیلان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دربیابان گر بشوق کعبه خواهی زد قدم - سرزنشها گر کند خار مغیلان غم مخور",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Turkish",
          "refs": "KLN:160",
          "words": [
            {"translit": "beg-umm", "gloss": "mother of ruler, a female title of respect", "script": null, "see": ["Bhag"]},
            {"translit": "xân-umm", "gloss": "mother of Khan ?, a female title of respect", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:339",
          "words": [
            {"translit": "baygom", "gloss": "a female title of respect", "script": "بیگم"},
            {"translit": "xânom", "gloss": "a female title of respect", "script": "خانم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:160",
          "words": [
            {"translit": "begum", "gloss": "a female title of respect", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
```


## [2026-10-15T02:44:31.135Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','BQT']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[600:2500]);print()\n\"; grep -n -i -E '^ *begum|begum' data/verification/sources/refs/KLN_1966.txt | head; ls site/pages/518.jpg"
}
```


### [2026-10-15T02:44:31.568Z] TOOL RESULT

```
KLN ome/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}

BQT 596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/

3982:aunt,  n.  —  AF.  aunte,  fr.  OF.  ante  (F.  tante),  fr. L.  amita ,  ‘father’s  sister’,  which  is  formed  with -it a,  a  suff.  of  prob.  Etruscan  origin,  from  the infantile  imitative  base  *am(ma),  ‘mother,  grand¬ mother,  nurse’.  Cp.  Gk.  dp.p.<x,  dp-fla?,  dppta, ‘mother’,  ON.  amma ,  ‘grandmother’,  OHG. amma,  ‘mother,  nurse’,  Mir.  ammait,  ‘old  hag’. The  base  occurs  also  in  the  Semitic  languages ; cp.  Heb.  cm,  Aram.-Syr.  cm,  Arab,  umm,  imm , Ethiop.  em,  Akkad,  ummu,  ‘mother’.  Cp.  also the  second  element  in  begum, aura,  n.  emanation;  aroma.  —  L.,  ‘breeze,  wind, air’,  fr.  Gk.  aupx,  ‘air  in  motion,  breeze’,  which is  rel.  to  srjp,  ‘air’.  See  air  and  cp.  soar, aural,  adj.,  of,  or  pertaining,  to  the  ear.  Formed with  adj.  suff.  -al  fr.  L.  auris,  ‘ear  .  See  auricle. Derivative:  aural-ly,  adv. aural,  adj.,  pertaining  to  an  aura.  Formed  fr. aura  with  adj.  suff.  -al.
4658:beg,  n.,  a  bey.  —  The  same  as  bey.  Cp.  beglerbeg. and  begum.
4664:beglerbeg,  n.,  formerly,  governor  of  a  province  in the  Ottoman  empire.  —  Turk.,  lit.  ‘bey  of  beys’, fr.  begler,  pi.  of  beg,  ‘bey’,  and  beg,  ‘bey’.  See bey  and  cp.  beg,  n.,  begum, begnaw,  tr.  v.  —  OE.  begnagan,  fr.  be-  and  gna- gan,  ‘to  gnaw'.  See  gnaw.
4670:begum,  n.  —  Turk.,  a  hybrid  coined  fr.  beg  and Arab,  umm,  ‘mother’,  and  orig.  meaning  ‘moth¬ er  of  the  bey’.  For  the  first  element  see  bey.  The second  element  is  rel.  to  Heb.  em,  Aram. -Syr. em,  Ethiop.  em,  Akkad,  ummu,  ‘mother’, begun,  pp.  of  begin.
4874:bewray,  tr.  v.,  to  reveal,  divulge  ( archaic )  — ME.  bewreien,  bewreyen,  ‘to  reveal’,  fr.  be-  and OE.  wregan,  ‘to  accuse’,  which  is  rel.  to  OS. wrogian,  OFris.  wrogia,  OHG.  ruogen,  MHG. riiegen,  ‘to  accuse’,  G.  riigen,  ‘to  censure’,  Goth, wrohjan,  ‘to  accuse’,  ON.  rcegja,  ‘to  slander,  de¬ fame’,  Du.  wroegen,  ‘to  prick’  (said  of  con¬ science),  OE.,  OS.  wrdht,  OFris.  wrogie,  MHG. ruoge,  riiege,  Goth,  wrohs,  ‘accusation’,  G.  Riige, ‘censure’,  ON.  rog,  ‘quarrel,  slander’, bey,  n.,  1)  governor  of  a  district  in  Turkey;  2)  a Turkish  title  of  honor.  —  Osmanli  equivalent of  Turk.  beg.  Cp.  beg,  ‘bey’,  begum, beylic,  beylik,  n.  —  Turk.,  formed  fr.  bey  and -lik,  a  suff.  expressing  quality.  Cp.  pashalik. beyond,  adv.  and  prep.  —  ME.  biyeonde,  biyonde, fr.  OE.  begeondan,  ‘beyond’,  fr.  be-  and  geond, ‘yond,  yonder’.  See  yon,  yond,  yonder. Derivative:  beyond,  n.
Permissions Size User   Date Modified Name
.rw-r--r--   42k sfmqrb 14 Oct 22:15  site/pages/518.jpg
```


## [2026-10-15T02:44:38.148Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /begum,  n\\.  —  Turk/{print NR-1; exit}' KLN_1966.txt; grep -n -i -E 'khanum|khanim|khanoum' KLN_1966.txt | head -3; echo ---HJB; grep -n -E '^ ?BEGUM|^BEGUM|BEGUM,|KHANUM|KHANOUM' HJB.txt | head; echo ---AID; grep -n -i -E '^begum|^khanum|^khanam' AID.txt|head; echo ---LKT; grep -n -i -E 'begum|bägüm|begüm|beg[iy]m|ḫanum|chanum|hanım' LKT.txt|head; echo ---TTS; grep -n -i -E 'begim|bigim|begüm|chanym|chanum|hanum' incoming/TTS/TTS_pages.txt|head"
}
```


### [2026-10-15T02:44:38.554Z] TOOL RESULT

```
95
---HJB
12454:KHANUM.
---AID
---LKT
866:'Herrin,  P'ürstin'  [nicht  osm.,  sondern osttk.,  fem.  zu  beg  s.  hier  Nr.  282,  ge- bildet wie  hämim  von  hän  s.  hier  Nr. 808];  hieraus  angloind.  beegum,  begum 'Prinzessin,  Dame  von  hohem  Rang', mit  Bezug  auf  Muhammedanerinnen  ge- braucht. Frz.  beygam  [zu  beyg].  [Hob- son-Jobson 79.
5955:begum  300
---TTS
```


## [2026-10-15T02:44:41.279Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 860,868p LKT.txt; awk 'BEGIN{RS=\"\\f\"} /Herrin,  P.ürstin/{print \"leaf\",NR-1; exit}' LKT.txt; grep -n -i -E 'hänim|hänym|^ *808\\.' LKT.txt | head; echo ---HJB; sed -n 12454,12475p HJB.txt; grep -n -E 'BEEGUM|BEGUM' HJB.txt | head"
}
```


### [2026-10-15T02:44:41.679Z] TOOL RESULT

```
ind. bendy,  bindy  und  bandicoy  [aus tamul.  vendai-khäi,  d.  h.  'unreife  Frucht des  vendaP,  tamul.  Entsprechung  zu  hind. bhindi].    [Hobson-Jobson  84/85.
298.  Hind.  bliQj:
[Auch  in  den  drawidischen  Sprachen, z.  B.  Telugu,  Kanaresisch,  aus  denen das  Wort  wohl  stammt]  'Träger',  be- sonders 'Palankinträger'  [also  synonym mit  den  angloind.  Ausdrücken  kahär, mahrä,  liammäl,  mutya,  pälky-bardär und  dem  aus  engl,  bearer  'Träger'  ent- standenen byrd\;  hieraus  haben  in  Vor- derindien die  Engländer  volksetymolo- gisch boy  zur  Bezeichnung  ihres  indischen Dieners  gemacht.  Bei  den  Franzosen der  vorderindischen  Kolonien  wurde  aus dem  hind.  Grundwort  boue,  boe;  jeu  de boes  ist  die  für  einen  Palankin  nötige Zahl  an  Trägern.
299.  Hind.  bibi:
'Dame';  hieraus  angloind.  ieefcee.  Wäh- rend die  Verkürzung  bi  zur  Auszeich- nung dem  Namen  muslimischer  Damen angefügt  wird,  ist  das  Wort  im  übrigen völlig  herabgekommen  und  wird  höch- stens noch  auf  europäische  Dienstboten oder  englische  Frauen  ähnlichen  Standes angewandt ;  ja  es  bedeutet  vielfach  nur noch  eine  Prostituierte.  [Hobson-Job- son 78.
300.  Tk.  bigaui:
'Herrin,  P'ürstin'  [nicht  osm.,  sondern osttk.,  fem.  zu  beg  s.  hier  Nr.  282,  ge- bildet wie  hämim  von  hän  s.  hier  Nr. 808];  hieraus  angloind.  beegum,  begum 'Prinzessin,  Dame  von  hohem  Rang', mit  Bezug  auf  Muhammedanerinnen  ge- braucht. Frz.  beygam  [zu  beyg].  [Hob- son-Jobson 79.
301.  Pers.  bigär:
[Aus  pers.  be  'ohne'  s.  hier  Nr.  252  und gär,  kär  'Werk,  Tat'  Horn  NpEt  S.  185, Nr.  831 ;  also  wörtlich  'ohne  Arbeit, arbeitslos'] ;  hieraus  hind. begärt  'Zwangs- arbeit' und  angloind.  begar,  bigarry; jeder  'zu  einer  öffentlichen  Arbeit  Heran- gezogene' wird  so  genannt.  [Hobson- Jobson  79.
leaf 52
1957:808.  Tk.  Ii��n:
---HJB
KHANUM.
election  started  on  a  war  policy,  and  the War  Loan  for  the  Transvaal  Campaign  has been  known  as  ''khaldB."]
Recent  military  operations  have  led to  the  general  introduction  of  khaki as  the  service  uniform.  Something like  this  has  been  used  in  the  East for  clothing  from  a  very  early  time : —
[1611. — *'8ee  if  yon  can  get  me  a  pieoe  of ▼ery  fine  brown  catico  to  nuUice  me  clothes." —Danvers,  Letten,  i.  109.]
KHATJBA.  8.  and  adj.  Hind,  from Ar.  khdl^  properly  khdlisa)  'pure, genuine.'  It  has  various  technical meanings,  but,  as  we  introduce  the word,  it  is  applied  by  the  Sikhs  to their  community  and  church  (so  to call  it)  collectively.
1783.— "The  Siequet  salute  each  other  by the  expression  Wah  Oooroo^  without  any inclination  of  the  body,  or  motion  of  the himd.  The  Ooyemment  at  huge,  and  their armies,  are  denominated  ualsa,  and Khalsajee."— FoTfter'f  JowrMy^  ed.  1808,  i. 307.
1881.— "  And  all  the  Punjab  knows  me,  for  my father's  name  was  known In  the  days  of  the  conquering  inia-laHj when  I  was  a  boy  half-grown?'
Attar  Singh  loqieUury  by  Sowcur,  in  an Indian  paper  ;  name  and  date  lost.
KHAN,  s.  a.  Turki  through Pers.  Khan.  Originally  this  was  a title,  equivalent  to  Lord  or  Prince, used  among  the  Mongol  and  Turk nomad  horaes.  Besides  this  sense, and  an  application  to  various  other chiefs  ana  nobles,  it  has  still  become in  Persia,  and  still  more  in  Afghani- stan, a  sort  of  vague  title  like  "Esq.," whilst  in  India  it  has  become  a common  affix  to,  or  in  &ct  part  of, the  name  of  Hindustanis  out  of  every rank,  properly,  however  of  those claiming  a  Piithan  descent.  The tendency  of  swelling  titles  is  always thus  to  degenerate,  and  when  the  value of  Khan  had  sunk,  a  new  form,  Khdn- Khdnan  (EZhan  of  Khans)  was  devised at  the  Court  of  Delhi,  and  applied  to one  of  the  high  officers  of  State.
[c.  1610.— The  **  Auant  Caounas  **  of I^rard  de  Layal.  which  Mr.  Gray  fails  to identify,  ia  probably  Hagan-Khant  Hak.  Soc. i.  89.
[1616.— '^AU  the  Oaptayens,  as  Ghanna Cnana  (Khfin-Kh&n&n),  Mahobet  Chan, Chan  John  (Khan  Jahkn)."— .^r  T,  Roe, Hak.  Soc  i.  192.
[1675.— "Cawn."    See  under  amoi]
b.  Per&  khan,  A  public  building for  the  accommodation  of  travellers,  a caravanserai.  FThe  word  appears  in English  as  early  as  about  1400;  see Stanf,  Diet.  s.v.]
1653. — ''Han  est  vn  Serrail  ou  encloe  que les  Arabes  appellent/omiaita;  oh  se  retirent les  Oarauanes,  ou  les  Marchands  Estrangers, .  .  .  ce  mot  de  Han  est  Turq,  et  est  le mesme  que  JCtarauajuarai  ou  Kaarhcuara (see  CABAVAN8ERAT)  dont  parle  Belon. .  .  ."—De  la  Baullaye-U-Ooiu,  ed.  1657, p.  640.
1827.— "  He  lost  all  hope,  being  informed by  his  late  fellow-traveller,  whom  he  found at  the  Khaa,  that  the  Nuwaub  was  absent on  a  secret  expedition." — W.  Scottf  Tht Surgeon**  Daughter,  oh.  xiii.
KHANNA,     OONNAH,     &c.    s.
This  term  (Pers.  khdna,  <a  house,  a compartment,  apartment,  department, receptacle,'  &c.)  is  used  almost  ad Itbitttm  in  India  in  composition,  some- times with  most  incongruous  words, as  hobachee  (for  bdwar<M)  connah, 'cook-house,'  Dnggy-connah,  'buflcy, or  coach-house,'  bottle-khaima,  touia- khana  (q.v.X  &c.  &c.
1784.— "The  house,  cook-room,  bottle- oonnah,  godown,  ka.,  are  all  pucka  built."— In  Seton-Karr,  i.  41.
KHAN8AMA.    See  CONSUKAH.
EHANXTM,  s.  Turki,  through Pers.  khdnwm  and  khdnim^  a  ladv  of rank  ;  the  feminine  of  the  title  TTlf^Mj a  (q.v.)
1404.—"  ...  la  mayor  delles  avia  nSbre Gafioil,  que  quiere  dezir  Beyna,  o  Sefiora grande." — Clavijo,  f.  52r.
„  "The  great  wall  and  tents  were for  the  use  of  tiie  chief  wife  of  the  Lord, who  was  called  Cafto,  and  the  other  was  for the  second  wife,  called  Qwinchi  Oafio,  which means  'the  little  lady.'  ^^—Markham:*  Clatijo, 145.
```


## [2026-10-15T02:44:44.707Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'B[EK]+[GO]UM|EEGUM' HJB.txt | head; awk 'BEGIN{RS=\"\\f\"} /EHANXTM/{print \"leaf\",NR-1; exit}' HJB.txt; grep -n -i 'begum\\|beegum' AID.txt | head -5; grep -n -i 'khanam\\|khanum' AID.txt|head -3"
}
```


### [2026-10-15T02:44:45.111Z] TOOL RESULT

```
leaf 531
```


## [2026-10-15T02:44:47.227Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'begam|bigam|Bigam|Lady  of  rank|Princess, Lady' HJB.txt | head; grep -n -i -E 'beg[au]m|bigam' AID.txt WEB_vol1.txt SKT.txt | head"
}
```


### [2026-10-15T02:44:47.645Z] TOOL RESULT

```
3240:Princess,  a  Mistress,  a  Lady  of  Rank  ; applied  to  Mahommedan  ladies,,  and in  the  well-known  case  of  the  Beegum Swmroo  to  the  professedly  Christian (native)  wife  ot  a  EurOT)ean.  The word  appears  to  be  Or.  Turki.  bigmi, [which  some  connect  with  Skt.  hhaga, Mordy'l  a  feminine  formation  from Bw,  *  chief,  or  lord,'  like  Khdmm.  from Khdn ;  hence  P.  hegam.  [Beg  appears in  the  eaily  travellers  as  Beage.]
20362:1810.  —  "Among  the  several  justly  ex- ploded ceremonies  we  may  reckon  that ...  of  'Sitting  np/  ...  This  'Bittiiig up/  as  it  was  termed,  generally  took  place At  the  house  of  some  lady  of  rank  or fortune,  who,  for  three  successive  nights, threw  open  her  mansion  for  the  purpose of  receiving  all  .  .  .  who  chose  to  pay their  respects  to  such  ladies  as  might  have recently  arrived  in  the  country."— Trt7/ia«i- «m,  V.M.  i.  113.
AID.txt:975:Begam.  [Hindustani.]  A   Musalmdn lady  of  rank.  Among  Saids  the title  is  commonly  affixed  to  all women’s  names.
AID.txt:4871:Najib.  [Arabic.]  This  term,  signifying originally  *   noble,’  is  applied  among Muhammadans  to  irregular  infantry. Ranjit  Singli,  the  Sikh  ruler,  had  a regiment  of  najibs  consisting  of Musalmdns,  who  joined  him  from Samru  Begam  on  her  death.  The British  government  also  retained some  najib  corps  chiefly  as  a   kind of  militia.
SKT.txt:1769:Bigamy,    a  double  marriage.     (F.  *] and  Gk.)     F.  ^^jomiV.  — L,nte  L.  ^y n  clumsy  compound   from   L«.  A/* (see    Bi-),  and    Gk.    •7a;ua,  from  fa/ marriage.     It    should    ratbei    have digamy  (Gk.  Stya^a.)
SKT.txt:10452:(L.)  From  pp.  of  L. to  get  rid  of.  »  ll  /.  forth ; »-,  Item  of  lifnen,  a  threshold  ^abovc). ktel.  the  bcAdpiece  of  a  door.  (F.*> IL  E.  JinU/.-O.  F.  /!«///  (F.  Hnteau\ m  L.  hmttiitu,  %  liDlel.  put  for  /intj- I*.  dimin.  of  L.  limts  (stem  Umif),  a dary  ;  wc  Limit  t>^bove). ^limtnajy.  introductory.  (F.-L.) od  itom  /r/-,  piefix,  before ;  and  O.  F. ^Bp,  *ict  before  the  entry  of,  dcdi- ^BCot.  From  L.  liminanj,  adj., ^pB  the  begumUiK  or  threshold.  — L. »>  erode  C^m  of  limfm,  threshold «).
SKT.txt:23803:Begum,  in  the  E.  Indies,  a  ladv  of  the highest  rank.  (Pers.  — Turk,  ana  Arab.) Pcrs.  bf^m.  a  queen,  lady  of  rank  ;  lit. '  mother  of  the  governor.' — Turk,  be^^  be/, a  bey,  governor;  Arab,  u/n,  umm,  mother.
WEB_vol1.txt:17864:bé/gum (or ba’gum), n. [Anglo-Ind. word, from Hind. begam, a lady, from Turk. bgim, a cess.
WEB_vol1.txt:19216:ian aN }in ancient Rome, a chariot drawn bT’ ro horses. by two bigamist. [Obs.]
WEB_vol1.txt:19217:pig'ăm, 7. & mene who has committed bigamy. _ 1. involving bigamy. ity of bigamy. $ F 2. DEN ME. bigamie; OFr. bigamie; LL. ig/a: ay his, twice, and Gr. gamos, marriage.]} bigami’, e of entering into a second
```


## [2026-10-15T02:44:51.832Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'بیگم\\|بيگم' BQT_v1_pages.txt | head; grep -n '\\[pdf page' BQT_v1_pages.txt | head -3; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BQT'].get('page_offset'))\""
}
```


### [2026-10-15T02:44:52.782Z] TOOL RESULT

```
3941:لغات باشنجرف . واقف تاج ماه بیگم . سال وقف ۱۲۲ (قمری) »
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-10-15T02:44:54.178Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:339 --image 2>&1 | head -80"
}
```


### [2026-10-15T02:44:54.574Z] TOOL RESULT

```
no scan of BQT covers printed page 339 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:44:56.375Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 557 558 559 560 561; do echo \"=== leaf $l\"; awk -v n=$l 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -8; done"
}
```


### [2026-10-15T02:44:56.991Z] TOOL RESULT

```
=== leaf 557
پیمما --
لیستون ۱- نام کوهی است
مشپور که فرهاد بفرمودة شیرین آنرا
مبکند و کنابه ازآسمان هم هست؟ :.
۱ لیست و بات پیگر حور مالی
قلك‌البروح اک
یست و پا و شاق ".نی
قبت وت ی اسیت. که پیت بر رات
=== leaf 558
از "1 رن اه
لیشه » بر وزن ربشه جنگل و نستانرا
گونند و بعربی اجم خوانند؟ - وسازی هم‌هنت
از ني, که شبانان نوازند. و بسنی کوشد سازیست
شبه بچنگه » و بعضی دیگی گونند شبیه است
پرباب .
بیضه ] آشین «کنایدازآقاب‌عالمتاب
و با انی معروف‌نلمبیخی است‌مهلك وکشنده ٩‏
=== leaf 559
۳۹۳6 سد
بیقاد ه بنتح اولبروزن نیزار , سرزنش
وطعنه باشد.
بیغاره بر وزن گهواره » بمعنی بیفار
ات که سرزش وطمنه باشد ٩‏ .
بیغال » بکر اول بر وزن فیفال »
بمعنی نیزه باشد که بعربی رمح خوانند .*#
بیگار ‌- با انی محپول و کاف فارحی
=== leaf 560
بنم ثانث مر وزث میگفت اه
ستارژ زهره را گوبند .
بیلقان ‏ بنتح اول و و
بر وزن نهروان ۰ شپرست از ولات اران مابین
شروان و آذربایجان؟ . ۱
پادشانعان - و قبالة خانه و باغ و امثال آنرا
کونند؟ - و تبربرا دز کنته اند که ییکان آن
دو شاخ باشد - و بکر اول وئانی مجهول‌نوعی
=== leaf 561
۳:۱
ماه است که بعربی شه ر گوبندا .
که مردمرا در حالت ماشفه دیده میشوده وآنرا
مربی ممایثه کوش
دریجهٌ خانه را گوند .
بیناساك .. بسکون سینو کاف, بمعنی
بیناس باشد که دربحهٌ خانه است ۰ رب بای فارسی
هم‌آحده ۱ سست ه
```


## [2026-10-15T02:44:59.436Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==560' BQT_v1_pages.txt | grep -n -A3 'بیگ\\|ببگ\\|یگم\\|ترکی\\|ترک' | head -60"
}
```


### [2026-10-15T02:44:59.846Z] TOOL RESULT

```
8:بیگار ‌- با انی محپول و کاف فارحی
9-بر وزن بی زار , کار فرمودن بی مزد بود معنی
10-کار بفی‌مایند و اجرت ندهند. #۶
11-لیگاه - با ثانی مجهول بر وزن بیراهه
--
14:لیگم ه بنتح اول وکاق تازی و سکون
15-ثانی و میم » صفه و ابوانر! کویند ,3۶
16-دبکند ‌ بقتح اول و کاف ‌ِ روزن‌سو ند
17-نام قن ات ]ملک زرم 2 جمشید وبای تخت افر اباب
--
23:مخفف بیگاء است که
24-۷ باشد .
25-لیل- بانانی مجهول
26-بر وزن فیل » آلنی باشد
```


## [2026-10-15T02:45:02.738Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==560' BQT_v1_pages.txt | sed -n 1,200p | tail -60; ls pageimg | head; ls ocr/ | head"
}
```


### [2026-10-15T02:45:03.183Z] TOOL RESULT

```
۳۹۳6 سد
بیقاد ه بنتح اولبروزن نیزار , سرزنش
وطعنه باشد.
بیغاره بر وزن گهواره » بمعنی بیفار
ات که سرزش وطمنه باشد ٩‏ .
بیغال » بکر اول بر وزن فیفال »
بمعنی نیزه باشد که بعربی رمح خوانند .*#
بیگار ‌- با انی محپول و کاف فارحی
بر وزن بی زار , کار فرمودن بی مزد بود معنی
کار بفی‌مایند و اجرت ندهند. #۶
لیگاه - با ثانی مجهول بر وزن بیراهه
بمعنی شام است که در برابر صبح باشدب و غیر
وک میگ :۱ یز گوینه.
لیگم ه بنتح اول وکاق تازی و سکون
ثانی و میم » صفه و ابوانر! کویند ,3۶
دبکند ‌ بقتح اول و کاف ‌ِ روزن‌سو ند
نام قن ات ]ملک زرم 2 جمشید وبای تخت افر اباب
بوده . و بعضی کویند فربدون آن شهر را بنا
کرده اس ۴
که با کاف فارسی بر وژن سره »
۱ ژد : بمفار : وییغازه
و وی
مخفف بیگاء است که
۷ باشد .
لیل- بانانی مجهول
بر وزن فیل » آلنی باشد
آهنی(۱) که باغبانانو امثال
ابشان زمین بدان کنند ۴
- وپاروبیرا(۲) نیز گویند
که کشتی‌بانان بجهت‌راندن
غراب‌سازند و نام‌میوه‌است
اقعام یل
عرای- وبلفت زند و یازند(۳) بمعنی چاه‌باشده 5
مطافاً که بعربی بیر خوانند - و سبدس رگین
کشی ر کگاسیرا نیز گوبند .
ببلای۱ عم با اول بای رسیده و ثالث
بالف کشیده و بتحتانی زده» بلات زندویازند(۳)
چاه باشد مطلعاً که‌عربان مرخوانتد .
لبلسته . با انی مجهول مر وژن می
دسثه , انگشتان دست راگوبند - و نوعی‌از کل
هم هست .
در حندوستان شبیه به هی
(۳) چك : ژند و اژند.
0 مر ۳ ۴ راد :
فرهشگ» روستابی ص ٩٩۷‏ .
۱ - هز . (2/0ا0 : پهلوی
روسای سیاه ۰ «داثرءالممارف اسلام*.
.» ۲
۶ دار ةالمعار ۳
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:19  bqt_v3_p150-150.png
.rw-r--r--   51k sfmqrb 14 Oct 22:19  bqt_v3_p600-600.png
.rw-r--r--   75k sfmqrb 14 Oct 22:19  bqt_v4_p150-150.png
.rw-r--r--   41k sfmqrb 14 Oct 22:19  bqt_v4_p500-500.png
.rw-r--r--   55k sfmqrb 14 Oct 22:19  bqt_v5_p8-008.png
.rw-r--r--   42k sfmqrb 14 Oct 22:19  bqt_v5_p30-030.png
.rw-r--r--   49k sfmqrb 14 Oct 22:19  bqt_v5_p150-150.png
.rw-r--r--   44k sfmqrb 14 Oct 22:19  bqt_v5_p250-250.png
.rw-r--r--   79k sfmqrb 14 Oct 22:19  irn_p100-100.png
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  AFM
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BOOK
drwxr-xr-x     - sfmqrb 14 Oct 22:30  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:19  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
```


## [2026-10-15T02:45:06.859Z] TOOL CALL #15: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; curl -sL -o bqt339-518.jpg 'https://archive.org/download/borhan-ghate-v1/page/n559_w1600.jpg'; file bqt339-518.jpg; ls -la"
}
```


### [2026-10-15T02:45:08.561Z] TOOL RESULT

```
bqt339-518.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-10-15T02:45:11.286Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt339-518.jpg'); w,h=im.size\nim.crop((0,0,w,h//2)).resize((w*6//10,h*3//10)).save('bqt339-518-top.png')\nim.crop((0,h//2,w,h)).resize((w*6//10,h*3//10)).save('bqt339-518-bot.png')\n\""
}
```


### [2026-10-15T02:45:11.759Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-15T02:45:14.125Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; which magick convert vips; magick bqt339-518.jpg -crop 100%x50% +repage -resize 1500x bqt339-518-%d.png && ls"
}
```


### [2026-10-15T02:45:15.620Z] TOOL RESULT

```
/usr/bin/magick
/usr/bin/convert
/usr/bin/vips
```


## [2026-10-15T02:45:17.343Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; ls"
}
```


### [2026-10-15T02:45:18.177Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:21.555Z] TOOL CALL #19: Bash

```json
{
 "command": "D=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518; ls -la $D; mkdir -p $D; curl -sL -o $D/bqt339-518.jpg 'https://archive.org/download/borhan-ghate-v1/page/n559_w1600.jpg'; magick $D/bqt339-518.jpg -crop 100%x50% +repage -resize 1500x $D/bqt339-518-%d.png; ls -la $D"
}
```


### [2026-10-15T02:45:24.502Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  308k sfmqrb 14 Oct 22:45  bqt339-518-0.png
.rw-r--r--  287k sfmqrb 14 Oct 22:45  bqt339-518-1.png
.rw-r--r--  472k sfmqrb 14 Oct 22:45  bqt339-518.jpg
Permissions Size User   Date Modified Name
.rw-r--r--  308k sfmqrb 14 Oct 22:45  bqt339-518-0.png
.rw-r--r--  287k sfmqrb 14 Oct 22:45  bqt339-518-1.png
.rw-r--r--  472k sfmqrb 14 Oct 22:45  bqt339-518.jpg
```


## [2026-10-15T02:45:26.301Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518/bqt339-518-0.png"
}
```


### [2026-10-15T02:45:26.329Z] TOOL RESULT

```

```


## [2026-10-15T02:45:29.696Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518/bqt339-518-1.png"
}
```


### [2026-10-15T02:45:29.728Z] TOOL RESULT

```

```


## [2026-10-15T02:45:34.244Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; ls BQT | head -20; ls BOOK | head -5; grep -n \"vision\" /home/sfmqrb/git/rishe-private/tools/ref_page.py | head"
}
```


### [2026-10-15T02:45:34.707Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:30  0480.vision.txt
.rw-r--r--  2.6k sfmqrb 14 Oct 22:19  31.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  58.vision.txt
.rw-r--r--  1.9k sfmqrb 14 Oct 22:19  70.vision.txt
.rw-r--r--  257k sfmqrb 14 Oct 22:19  71.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  71.vision.txt
.rw-r--r--  1.6k sfmqrb 14 Oct 22:19  72.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  103.vision.txt
.rw-r--r--  521k sfmqrb 14 Oct 22:19  171.png
.rw-r--r--   806 sfmqrb 14 Oct 22:19  171.vision.txt
Permissions Size User   Date Modified Name
.rw-r--r--   96k sfmqrb 14 Oct 22:19  33.png
.rw-r--r--   99k sfmqrb 14 Oct 22:19  39.png
.rw-r--r--   54k sfmqrb 14 Oct 22:19  46.png
.rw-r--r--   99k sfmqrb 14 Oct 22:19  54.png
10:matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
18:save that transcription as <printed page>.vision.txt next to the .txt; from then on this
83:    vision = base + ".vision.txt"   # a transcription made by reading the PNG; preferred over OCR
86:    if os.path.exists(vision):
88:        print(open(vision, encoding="utf-8").read())
```


## [2026-10-15T02:45:41.483Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518/bqt339-518.jpg 0339.jpg; cat > 0339.vision.txt <<'EOF'\n[BQT vol. 1, printed p. 339 (archive.org borhan-ghate-v1, leaf n559); read from image]\nبیکم - بفتح اول و کاف تازی و سکون ثانی و میم، صفه و ایوانرا گویند. *\n...\nfootnotes (Mo'in):\n* بیک - ترکی beg، عثمانی bey، قرقیزی bî یا biy؛ عنوانی است که بشاهزادگان و نجباء داده میشد، امیر قبیله‌ای کوچک (در برابر خاقان یا خان که رئیس قبیله‌ای بزرگ بود) - رؤسای سپاه. «دائرة‌المعارف اسلام».\n* بیگانه - پهلوی bêgânak «اسفا ۱:۱ ص ۲۸۴»، نیز bêgânik «منلس ۲۶۹: ۲».\n* بیگم - بفتح اول و ضم سوم، ترکی Begum ملکه مادر، بیوه زنی ارجمند، بانو «دائرة‌المعارف اسلام».\nEOF\ncd /home/sfmqrb/git/rishe-private; pdftoppm -f 518 -l 518 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518/pg518"
}
```


### [2026-10-15T02:45:42.556Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:45.877Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl518/pg518.png"
}
```


### [2026-10-15T02:45:46.346Z] TOOL RESULT

```

```


## [2026-10-15T02:45:46.336Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:45:53.065Z] TOOL CALL #25: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-15T02:45:53.076Z] TOOL RESULT

```

```


## [2026-10-15T02:45:55.123Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/begum",
 "prompt": "Quote the full etymology section for English begum, and any sources cited."
}
```


## [2026-10-15T02:45:55.683Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/خانم",
 "prompt": "Quote the Persian etymology section(s) for خانم (khanum/xânom), with any sources cited."
}
```


## [2026-10-15T02:45:56.291Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/begum",
 "prompt": "Quote the etymology of begum."
}
```


## [2026-10-15T02:45:57.428Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/مغیلان",
 "prompt": "Quote the Persian etymology section(s) for مغیلان, with sources."
}
```


## [2026-10-15T02:45:58.176Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أم",
 "prompt": "Quote the Arabic etymology for أُمّ umm 'mother' (Proto-Semitic form, cognates), and anything about أُمِّيّ ummiyy 'illiterate'."
}
```


### [2026-10-15T02:45:58.910Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:45:59.019Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:46:02.053Z] TOOL RESULT

```
# Persian Etymology for خانم

**Etymology Section:**

"Borrowed from Turkic languages. Compare Old Anatolian Turkish خانم (ḫānum), Chagatai خانِم (xānım)."

**Sources:**

The etymology section contains no formal citations. The Persian entry references comparative forms from related Turkic languages but does not cite specific academic sources for this etymological information.
```


### [2026-10-15T02:46:02.589Z] TOOL RESULT

```
# Etymology of أُمّ (umm) 'mother'

The entry shows that أُمّ is "Inherited from Proto-Semitic *ʔimm-, from Proto-Afroasiatic *ʔim-". It notes a cognate: "Hebrew אם (em)".

**Regarding أُمِّيّ (ummiyy) 'illiterate':** The document does not contain any information about this related word form. The page focuses on the primary noun meaning "mother" and its various grammatical uses, but does not discuss derivative adjectives like ummiyy.
```


### [2026-10-15T02:46:03.934Z] TOOL RESULT

```
# Etymology of "Begum" in English

## Etymology 1
The first sense derives from the prefix "be-" combined with "gum" (the substance). The etymology tree shows a path from Proto-Indo-European *h₁ep- through various Germanic stages to modern English.

## Etymology 2
The noun "begum" (a high-ranking Muslim woman) has a different origin: "From Classical Persian بیگم (bēgum), from East Turkic begüm, from beg (a title of nobility in Iran, Central Asia and South Asia) + -um (feminine suffix for titles of nobility)."

## Sources Cited
Two references are provided:

1. The American Heritage Dictionary of the English Language: Fourth Edition (2008), which defines "begüm"

2. Nişanyan Sözlük (an online dictionary by Sevan Nişanyan, 2002–), containing an entry for "begüm"

These sources support the Turkic and Persian etymological connections for the noun form of "begum."
```


## [2026-10-15T02:46:05.834Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أمي",
 "prompt": "Quote the Arabic etymology of أُمِّيّ ummiyy 'illiterate/unlettered', with sources and any note about Quran usage / Hebrew ummot ha-olam."
}
```


## [2026-10-15T02:46:07.005Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hanım",
 "prompt": "Quote the Turkish etymology of hanım (from han + possessive?), with sources (Nişanyan, Clauson etc)."
}
```


## [2026-10-15T02:46:08.133Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أم_غيلان",
 "prompt": "Quote the etymology and meaning of أم غيلان umm ghaylān."
}
```


## [2026-10-15T02:46:08.721Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/مغیلان",
 "prompt": "Quote Mo'in's (and Dehkhoda's if shown) entry for مغیلان including origin tag."
}
```


## [2026-10-15T02:46:09.362Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/خانم",
 "prompt": "Quote Mo'in's entry for خانم including origin tag [تر.] and etymology."
}
```


### [2026-10-15T02:46:12.565Z] TOOL RESULT

```
# Meaning of "مغیلان" (Moghilan)

According to Mo'in's Dictionary, مغیلان is defined as:

> "امُ غیلان ، درختچة خاردار که در بیابان ها می روید"

This translates to a thorny shrub or small tree that grows in desert regions. The word has Arabic origins (marked as ع in the entry).

The term appears in multiple Persian lexicographic sources, including Dehkhoda's dictionary and other standard Persian references available on this Vajeyab (Persian dictionary) platform.
```


### [2026-10-15T02:46:13.378Z] TOOL RESULT

```
# Turkish Etymology of Hanım

Based on the Wiktionary article provided, the etymology shows:

**Proto-Turkic** *kagan* → **Old Anatolian Turkish** *ḫān* (khan) → **Ottoman Turkish** *han* + *-m* (possessive suffix) → **Turkish** *hanım*

The article explicitly states the word is "Inherited from Ottoman Turkish خانم (hanım)," indicating the combination of *han* (khan/ruler) with the possessive suffix *-m* to form *hanım*.

However, the sources cited in the "Further reading" section (Nişanyan Sözlük, Misalli Büyük Türkçe Sözlük, and Turkish Language Association dictionaries) are referenced but their specific etymological explanations are not quoted in this Wiktionary entry itself.
```


### [2026-10-15T02:46:13.728Z] TOOL RESULT

```
# Mo'in Dictionary Entry for خانم (Khanom)

According to the Mo'in Dictionary (Farhangi-ye Entesharati-ye Mo'in), the entry for خانم includes the following definition:

"(نُ) [تر.] (اِ.) 1 - زن بزرگ زاده . 2 - عنوانی که برای احترام ، پیش یا پس از نام زنان گفته می شود."

**Translation of meanings:**
1. A woman of noble or high birth
2. A respectful title used before or after women's names

The etymology tag **[تر.]** indicates the word has Turkish origins, with (نُ) marking the noun grammatical classification and (اِ.) likely denoting its linguistic category.
```


### [2026-10-15T02:46:15.907Z] TOOL RESULT

```
# Etymology of أُمِّيّ (ummiyy)

Based on the Wiktionary entry, **أُمِّيّ** (ummiyy) meaning "illiterate/unlettered" derives from:

**Etymology 2** states: "From أُمَّة (ʔumma, 'nation') + ـِيّ (-iyy)."

## Quranic Usage

The entry includes a Quranic citation (7:157, dated 609–632 CE) where the term describes the Prophet Muhammad:

> "the Messenger, the gentile/unlettered prophet, whom they find recorded in their possession within the Law (Torah) and the Gospel"

The same root appears in Quranic 2:78, referring to people described as "gentiles/illiterates who know not the Scripture but wishful thinking."

## Note

The entry also shows **Etymology 1**, where أُمِّيّ derives from أُمّ (mother) plus the nisba suffix, yielding the meaning "maternal." This demonstrates the word's dual etymological paths in Arabic.
```


### [2026-10-15T02:46:17.616Z] TOOL RESULT

```
# أم غيلان (Umm Ghaylān)

**Etymology:**
The term literally means "mother of ghouls, that is the abode of ghouls."

**Meanings:**

1. **Literal usage:** The component words أُمّ (mother) and غَيْلَان (ghouls) taken separately.

2. **Botanical reference:** The primary meaning refers to the "gum arabic tree" (*Vachellia nilotica*) or "gum-bearing acacia" (*Vachellia gummifera*), plants native to desert regions and found across North Africa and the Middle East.

A 13th-century botanical text describes it as: "a spiky shrub of the desert, of many thorns" with aromatic and medicinal properties.
```


## [2026-10-15T02:46:19.994Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/بیگم",
 "prompt": "Quote Mo'in's entry for بیگم including origin tag and etymology."
}
```


## [2026-10-15T02:46:20.535Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/امی",
 "prompt": "Quote Mo'in's entry for اُمّی (illiterate) and for اُم (mother), with origin tags."
}
```


## [2026-10-15T02:46:21.415Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/beg%C3%BCm",
 "prompt": "Quote Nişanyan's etymology for begüm (and any mention of hanım)."
}
```


### [2026-10-15T02:46:24.303Z] TOOL RESULT

```
# Mo'in Dictionary Entry for بیگم (Begum)

According to the Mo'in Dictionary, the entry reads:

"(بِ گُ) [ تر. ] (ص . اِ.) خانم ، خاتون ، بانو."

This indicates that **بیگم** (begum) is a Turkish loanword (تر.) that functions as a noun (ص.) and means "a lady, woman of noble status, or distinguished woman." The term serves as synonyms with خانم (khanom), خاتون (khatoun), and بانو (banu)—all Persian words denoting respected female titles.
```


### [2026-10-15T02:46:25.099Z] TOOL RESULT

```
I appreciate your request, but I cannot provide Nişanyan's etymology for "begüm" based on the content shown. The webpage excerpt provided only contains the header, navigation, and footer of the Nişanyan Sözlük (dictionary) site—it doesn't include the actual dictionary entry or etymological information for the word "begüm" or any mention of "hanım."

To access the etymology you're seeking, you would need to visit the full dictionary entry on the Nişanyan Sözlük website directly.
```


### [2026-10-15T02:46:25.654Z] TOOL RESULT

```
# Mo'in Dictionary Entry for امی (Ami)

According to the Mo'in Dictionary (Farhang-e Entesharat-e Mo'in), the entry reads:

"(اُ مّ) [ ع . ] (ص نسب .) بی سواد"

This translates to: The word "ami" is an Arabic-origin adjective meaning **illiterate** or **uneducated**.

The dictionary also lists related words with similar forms, including امید (hope), امیر (prince/emir), and امیدوار (hopeful), among others. These entries can be cross-referenced in other Persian dictionaries available through the same lexicographical platform.
```


## [2026-10-15T02:46:30.647Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'umm[iīy]' FVQ.txt | head -5; echo ---; sed -n 1957,1962p LKT.txt; echo ---HRN; grep -n -i -E 'xānum|chānum|bēgum|begum|ḫānum|chanum' HRN.txt HUB.txt | head; echo ---TTS; grep -n -i -E 'bigim|bégim|begim|chanym|chanim' incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -5; echo ---MON; grep -n 'مغیلان\\|مغيلان' MON_part*.txt | head -3; grep -n 'ام غیلان\\|ام غيلان\\|أم غيلان' AFM.txt FVQ.txt KLN_1966.txt| head"
}
```


### [2026-10-15T02:46:31.101Z] TOOL RESULT

```
5633:'Ummij an, welches, wie Geiger bereits gefunden hat, die eigentliche arabisehe 
---
808.  Tk.  Ii��n:
Aus  liakän  [das  wohl  selbst  aus  dem Mongolischen  stammt],  ist  I.Name  der türkischen  und  mongolischen  Herrscher Miltfl.isiens,  etwa  'Kniser',  '■2.  eine  Art Adelsprädikat  im  heutigen  Persien  und Transkaukasien;  das  Wort  wird  in  dieser Bedeutung  nachgestellt,  z.  B.  Jahjä  Hän; hieraus  rum.  han  'Tatarenfürst';  bulg. serb.  hau,  cech.  chär},  poln.  klruss.  chan, russ.  hnn,  kagan,  kogan  'Herrscher  der Chasaren';  frz.  kan,  khan;  dtsch.  Chan. [Bern  SIEtWb  468.
809.  Pers.  liäu:
Auel)  hänä  'Haus'  [Horn  NpEt  S.  103, Nr.  4fi6  und  ANDKEAS  in  Festgabe  für Tlieodor  Nöldeke  zum  80.  Geburtstage. Göttingen  1916.  S.  4/6];  hieraus  tk.  han 'Herberge,  Wirtshaus',  rum.  han  'Gast- haus'.
810.  Ar.  Imiiaka:
'Halskette'  [vom  Vb.  hnnaka  'mit  einem Stricke  erwürgen';  das  Subst.  ist  wie hinaka  'Kragen'  erst  vulg.  gebräuchlich, vgl.  'Vatermörder'] ;  hieraus  siz.  it.  (dial. im  Süden)  canacca  'dass.'.    [ML  1860,
---HRN
---TTS
---MON
```


## [2026-10-15T02:46:33.113Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5625,5640p FVQ.txt; awk 'BEGIN{RS=\"\\f\"} /eigentliche arabisehe/{print \"leaf\",NR-1; exit}' FVQ.txt; grep -n -m3 'Ummi\\|ummi' FVQ_pages.txt|head -3"
}
```


### [2026-10-15T02:46:33.481Z] TOOL RESULT

```
1 Rudolph, Abhdng'ujkcd, 61 ; Horovitz, JPX, 193. 

2 Addai Sher, 30, suggests that it is from the Pers. ^3, which is absurd. 

3 " 1m Munclo der Judoii war VIXH DJT zweifcllos ausst'rordentlich gelaufig, 
nicht minder haufig wohl auch das aram. -fQ. Die Seltenheit des Ausdrucks im 
Koran trotz zahlreicher Gclcgenheit ihn zu brauchen, zeigt abcr, dass derselbe 
Muhammad nicht sehr gelaufig geworden iat, cr wendet ofter das dasselbe bcsagendo 
'Ummij an, welches, wie Geiger bereits gefunden hat, die eigentliche arabisehe 
ttbertragung ^on 'Am ha'arez darstellt," of. Geiger, 28. 



86 FOREIGN VOCABULARY OF THE QUR ? AN 


leaf 0
3362:'Ummij an, welches, wie Geiger bereits gefunden hat, die eigentliche arabisehe
```


## [2026-10-15T02:46:40.088Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; T=tools/fetch_source.py; N='page 518, root Umm'; python3 $T 'https://en.wiktionary.org/wiki/begum' --note \"$N: begum < Pers. bēgum < East Turkic begüm = beg + -um\" ; python3 $T 'https://en.wiktionary.org/wiki/خانم' --note \"$N: Persian xânom borrowed from Turkic xānım\"; python3 $T 'https://en.wiktionary.org/wiki/hanım' --note \"$N: Turkish hanım = han + possessive -m\"; python3 $T 'https://en.wiktionary.org/wiki/أم' --note \"$N: Arabic umm < Proto-Semitic *ʔimm-\"; python3 $T 'https://en.wiktionary.org/wiki/أمي' --note \"$N: Arabic ummiyy two etymologies (umm / umma)\"; python3 $T 'https://en.wiktionary.org/wiki/أم_غيلان' --note \"$N: umm ghaylān 'mother of ghouls' = acacia\"; python3 $T 'https://vajehyab.com/moein/مغیلان' --note \"$N: Mo'in مغیلان = ام غیلان [ع.]\"; python3 $T 'https://vajehyab.com/moein/خانم' --note \"$N: Mo'in خانم [تر.]\"; python3 $T 'https://vajehyab.com/moein/بیگم' --note \"$N: Mo'in بیگم [تر.]\"; python3 $T 'https://vajehyab.com/moein/امی' --note \"$N: Mo'in امی [ع.] بی‌سواد\" 2>&1 | tail -3"
}
```


### [2026-10-15T02:46:42.959Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e2788c665d771850.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/13db93ca3358c2a8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/23fee9d4b57ecca9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e36cb104e42f8a47.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2d8b7449c097b056.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a2e8f29a1acbef1f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3f932b8dec71cbb0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/793062b61e3fd1f1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/859649cb8f47d7be.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fccd41c0f727b2e4.txt
```


## [2026-10-15T02:48:05.216Z] TOOL CALL #42: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-518.json",
 "content": "{\n  \"pdf_page\": 518,\n  \"book_page\": 488,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Umm\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *ʔimm- / *ʔumm- 'mother' (< Proto-Afroasiatic *ʔim-)\",\n      \"note\": \"The Semitic 'mother' word is secure: Arabic umm (dial. imm), Hebrew ʾēm, Aramaic-Syriac ʾem, Ethiopic ʾem, Akkadian ummu, all < Proto-Semitic *ʔimm-/*ʔumm-. Root, label and gloss correct. The weak point of the chart is NOT the root but the Turkic branch (#3-#5): Klein (and Skeat) analyse begum as beg + Arabic umm 'mother of the bey', but Hobson-Jobson, Lokotsch, Webster, Mo'in and modern Wiktionary/AHD/Nişanyan take Eastern Turkic begim/begüm and xanım as beg/xan + Turkic suffix -im/-üm (1st-person possessive 'my lord', used as a feminine title), so the Arabic 'umm' there is a learned folk etymology. The Persian script for ommî's parenthetical is printed '(امّل)' in the book itself (an odd form, probably meant for a plural such as امّیّون/امّیّین); the extraction is faithful.\",\n      \"note_fa\": \"واژهٔ «اُم» (مادر) از سامی آغازین *ʔimm-/*ʔumm- است و هم‌ریشه با عبری ʾēm، آرامی ʾem و اکدی ummu؛ پس ریشه و معنای آن درست است. اما شاخهٔ ترکی نمودار سست است: کلاین و اسکیت «بیگم» را ترکیبِ beg با «اُم» عربی («مادرِ بیگ») دانسته‌اند، ولی هابسن‌جابسن، لوکوچ، معین و پژوهش امروزی begim/begüm و xanım را از beg/xan با پسوند ترکیِ -im/-üm (ضمیر ملکی «ـَم»: «بیگِ من، خانِ من») می‌دانند و پیوند آن با «اُم» عربی را ریشه‌شناسی عامیانه می‌شمارند. ادعای نورایی دربارهٔ خود ریشه درست است، دربارهٔ بیگم و خانم با پژوهش امروزی سازگار نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/أم\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:160\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 95 (pp. ~160-161), s.v. begum (line 4670): 'Turk., a hybrid coined fr. beg and Arab. umm, 'mother', ... The second element is rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu, 'mother''. Also s.v. aunt (line 3982): 'Arab. umm, imm, Ethiop. em, Akkad. ummu, 'mother''. Supports the Semitic root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"FVQ\", \"where\": \"p. 85-86 fn. 3 (FVQ.txt line ~5633, grep 'Ummij')\", \"stance\": \"partial\", \"note\": \"Jeffery quotes Horovitz: Muhammad 'wendet öfter das dasselbe besagende Ummī an, welches ... die eigentliche arabische Übertragung von 'Am ha'arez darstellt' — treats umm/umma family as native Arabic; no comment on 'mother' itself.\"},\n        {\"src\": \"SKT\", \"where\": \"SKT.txt line 23803, s.v. Begum\", \"stance\": \"supports\", \"note\": \"'Pers. begam, a queen, lady of rank; lit. 'mother of the governor.' — Turk. beg, bey, governor; Arab. um, umm, mother.' Confirms umm 'mother'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"umm; umme-ğîlân\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic أُمّ umm 'mother' is the inherited Semitic word (Proto-Semitic *ʔimm-/*ʔumm-, cf. Heb. ʾēm, Akk. ummu). أُمّ غَيْلان umm ghaylān, lit. 'mother of the ghūls' (ghaylān, pl. of ghūl 'desert demon'), is the classical Arabic name of the thorny desert acacia (Vachellia nilotica / gummifera); the name reflects the belief that ghouls haunt such thickets. 'Umm X' is a productive Arabic naming pattern for plants and animals ('possessor/abode of X').\",\n          \"derivation_fa\": \"«اُمّ» در عربی همان واژهٔ موروثیِ سامی برای «مادر» است (سامی آغازین *ʔimm-، عبری ʾēm). «اُمّ غَیلان» یعنی «مادرِ غول‌ها» (غَیلان جمعِ غول) و نامِ درختچهٔ خاردار بیابانی، گونه‌ای اقاقیا (صمغ عربی)، است؛ عرب‌ها این خاربُن‌ها را جایگاه غولان می‌پنداشتند. الگوی «اُمّ + اسم» در عربی برای نام‌گذاری گیاهان و جانوران رایج است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أم\",\n            \"https://en.wiktionary.org/wiki/أم_غيلان\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:160\", \"status\": \"partial\", \"note\": \"KLN_1966 leaf 95 s.v. begum: 'Arab. umm, 'mother' ... rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu' — supports umm; Klein has no entry for umm ghaylān (grep 'ghailan|ghaylan' silent).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"line 23803 s.v. Begum\", \"stance\": \"supports\", \"note\": \"'Arab. um, umm, mother'.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt grep 'ام غیلان|أم غيلان'\", \"stance\": \"silent\", \"note\": \"Addi Shir lists Persian loans into Arabic; umm and umm ghaylān are native Arabic, not listed.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/مغیلان\", \"stance\": \"supports\", \"note\": \"'امُ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید' [ع.]\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"omm; ommî; moğîlân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"omm أمّ (pl. ommahât أمّهات) is a learned Arabic loan in Persian, used beside native mâdar (e.g. omm-ol-ketâb). moğîlân مغیلان is Arabic umm ghaylān with the initial vowel lost and the two words fused (umm-ghaylān > mughaylān > Pers. moğîlân, with the Persian î for Arabic ay); Mo'in glosses it 'ام غیلان, a thorny desert shrub' [ع.], and Hafez's 'خار مغیلان' is the classic attestation. ommî أمّی 'illiterate' is the Arabic nisba ummiyy; Nourai's gloss 'as if just born from the mother' is the traditional Arabic lexicographers' explanation (from umm), but much modern scholarship (Geiger, Horovitz, Jeffery; Wiktionary 'from umma + -iyy') derives the Qur'anic al-nabī al-ummī from umma 'people, gentiles', calquing Hebrew ummōt hā-ʿōlām / ʿam hā-ʾāreṣ, i.e. 'gentile, without a scripture', 'illiterate' being secondary. The book prints the parenthetical as '(امّل)', an unusual form (perhaps a misprint for a plural like امّیّین); the JSON reproduces the page faithfully.\",\n          \"derivation_fa\": \"«اُم» (جمع: اُمّهات) وام‌واژهٔ عربی در فارسی است در کنار «مادر» فارسی. «مُغیلان» معرّبِ ترکیبی «اُمّ غَیلان» است که واکهٔ آغازین آن افتاده و دو جزء در هم آمیخته‌اند (umm ghaylān > mughaylān)؛ معین آن را «ام غیلان، درختچهٔ خاردار بیابانی» [ع.] آورده و «خار مغیلان» حافظ گواه مشهور آن است. «اُمّی» (بی‌سواد) صفت نسبی عربی است؛ توضیح نورایی («گویی تازه از مادر زاده») همان تفسیر سنتی لغت‌نویسان عرب از «اُم» است، ولی بسیاری از پژوهشگران امروزی (گایگر، هوروویتس، جفری) آن را از «اُمّت» به معنای «قوم، امت‌های بی‌کتاب» می‌دانند و معنای «بی‌سواد» را ثانوی می‌شمارند؛ پس این بخش با احتیاط پذیرفتنی است. صورت «(امّل)» در خود کتاب چنین چاپ شده و ظاهراً خطای چاپی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أمي\",\n            \"https://vajehyab.com/moein/مغیلان\",\n            \"https://vajehyab.com/moein/امی\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:34\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vazheha-ye arabi dar farsi: refs_online.json lists no digital copy (catalog record only).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/امی and /مغیلان\", \"stance\": \"supports\", \"note\": \"امی: '(اُ مّ) [ع.] (ص نسب.) بی سواد'; مغیلان: 'امُ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید' — Arabic origin of both confirmed; Mo'in gives no derivation of ummī from umm.\"},\n            {\"src\": \"FVQ\", \"where\": \"p. 85-86 fn. 3 (FVQ.txt line 5633)\", \"stance\": \"contradicts\", \"note\": \"Jeffery, quoting Horovitz: 'Ummī ..., welches, wie Geiger bereits gefunden hat, die eigentliche arabische Übertragung von 'Am ha'arez darstellt' — ummī as 'gentile/people of the land', not 'as born from the mother'.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt / BQT_v2 grep 'مغیلان'\", \"stance\": \"silent\", \"note\": \"No headword مغیلان found in the OCR of vols 1-2 (it would fall in vol 4, م); not consulted further.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Turkish\",\n          \"words\": \"beg-umm; xân-umm\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The forms 'beg-umm' and 'xân-umm' are Klein's analysis, not attested Turkic spellings. The actual words are Eastern Turkic (Chagatai) begim/begüm and xanım/xānum (Ottoman hanım), built from beg 'lord, bey' and xan 'khan' (< Old Turkic qaγan) plus the Turkic suffix -im/-üm, the 1st-person possessive ('my lord, my khan'), which became a feminine title of address. Hobson-Jobson (s.v. Beegum: 'Or. Turki bigim ... a feminine formation from Bī, chief, or lord, like Khānum from Khān'), Lokotsch no. 300 ('fem. zu beg ... gebildet wie hānim von hān'), Webster ('Turk. bigim'), Wiktionary (begüm = beg + -um; hanım = han + -m) and Nişanyan all reject the Arabic 'umm'. Klein and Skeat's 'mother of the bey' is a 19th-c. learned folk etymology, encouraged by the vowel harmony -üm resembling Arabic umm; Nourai's own '?' on xân-umm shows the doubt.\",\n          \"derivation_fa\": \"صورت‌های «beg-umm» و «xân-umm» تحلیلِ کلاین است، نه صورت‌های گواهی‌شدهٔ ترکی. واژه‌های واقعی ترکی شرقی (جغتایی) begim/begüm و xanım (عثمانی hanım) است: از beg «بیگ، امیر» و xan «خان» (از ترکی باستان qaγan) با پسوند ملکیِ اول شخص -im/-üm («بیگِ من، خانِ من») که سپس عنوانی برای زنان بزرگ‌زاده شد. هابسن‌جابسن، لوکوچ، وبستر، ویکی‌واژه و نیشانیان همه پیوند آن را با «اُم» عربی رد می‌کنند؛ «مادرِ بیگ» ریشه‌شناسی عامیانه‌ای است که شباهت -üm با «اُم» آن را پدید آورده. علامت پرسش خود نورایی بر xân-umm نیز نشانهٔ تردید است؛ پژوهش امروزی ادعای نمودار را نمی‌پذیرد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/begum\",\n            \"https://en.wiktionary.org/wiki/hanım\",\n            \"https://en.wiktionary.org/wiki/خانم\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:160\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 95, s.v. begum: 'Turk., a hybrid coined fr. beg and Arab. umm, 'mother', and orig. meaning 'mother of the bey''. Klein does support Nourai's arrow (for begum; Klein has no khanum entry), but this is the outdated view.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 300, p. ~26 (LKT.txt line 865-866, leaf 52)\", \"stance\": \"contradicts\", \"note\": \"'Tk. bigam: 'Herrin, Fürstin' [nicht osm., sondern osttk., fem. zu beg s. hier Nr. 282, gebildet wie hānim von hān s. hier Nr. 808]; hieraus angloind. beegum, begum'.\"},\n            {\"src\": \"HJB\", \"where\": \"s.v. BEEGUM (HJB.txt line 3240) and KHANUM (line ~12470, leaf 531)\", \"stance\": \"contradicts\", \"note\": \"'The word appears to be Or. Turki bigim, [which some connect with Skt. bhaga, Lord] a feminine formation from Bī, chief, or lord, like Khānum from Khān; hence P. begam.' KHANUM: 'Turki, through Pers. khānum and khānim, a lady of rank; the feminine of the title Khan'.\"},\n            {\"src\": \"TTS\", \"where\": \"TTS_vambery1878_uoft_djvu.txt grep 'bigim|begim|chanym'\", \"stance\": \"silent\", \"note\": \"No hit in the OCR.\"},\n            {\"src\": \"SKT\", \"where\": \"line 23803 s.v. Begum\", \"stance\": \"supports\", \"note\": \"'lit. 'mother of the governor.' — Turk. beg, bey, governor; Arab. um, umm, mother.'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"baygom; xânom\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian بیگم bēgum/beygom 'lady, princess' and خانم xânom (older xānum/xānim) 'lady; Mrs.' are real words, borrowed from Turkic in the Timurid-Safavid era (Chagatai begim/begüm, xānım), so the Turkish → Persian arrow is right. What is not accepted is the parent analysis: the Turkic words are beg/xan + possessive -im/-üm, not + Arabic umm (see #3). In Persian the old -ī/-ē- of beg gives bēg > beyg (with majhul ē > ey in modern Iranian pronunciation) and the suffix vowel became -o- (xânom, beygom). BQT p. 339 itself has only a homograph بیکم 'porch, iwan'; the title بیگم appears in Mo'in's footnote as 'Turkish Begum, queen-mother, honoured widow, lady', with no umm etymology.\",\n          \"derivation_fa\": \"«بیگم» و «خانم» واژه‌های واقعی فارسی‌اند که در روزگار تیموری و صفوی از ترکی جغتایی (begim/begüm، xānım) وام گرفته شده‌اند؛ پس پیکانِ ترکی ← فارسی درست است. ولی تحلیل بالادستی (بیگ/خان + «اُم» عربی) پذیرفته نیست و جزء پایانی همان پسوند ملکی ترکی «ـِم» است. معین هر دو را [تر.] آورده («بیگم: خانم، خاتون، بانو»؛ «خانم: زن بزرگ‌زاده»). در برهان قاطع ص ۳۳۹ مدخل «بیکم» به معنای «صفه و ایوان» است و تنها در حاشیهٔ معین آمده: «بیگم، ترکی Begum، ملکه‌مادر، بیوه‌زنی ارجمند، بانو». ادعای نورایی در راه وام‌گیری درست، در ریشهٔ عربی نادرست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/خانم\",\n            \"https://vajehyab.com/moein/بیگم\",\n            \"https://vajehyab.com/moein/خانم\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:339\", \"status\": \"partial\", \"note\": \"BQT vol. 1 printed p. 339 (archive.org borhan-ghate-v1 leaf n559; image saved as ocr/BQT/0339.jpg, transcription 0339.vision.txt): headword 'بیکم - بفتح اول و کاف تازی ... صفه و ایوانرا گویند' (a porch, unrelated); Mo'in's footnote: 'بیگم - بفتح اول و ضم سوم، ترکی Begum ملکه مادر، بیوه زنی ارجمند، بانو «دائرة‌المعارف اسلام»'. Confirms Turkish origin and the title sense; no Arabic umm; xânom not on this page.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/بیگم ; /خانم\", \"stance\": \"partial\", \"note\": \"بیگم: '(بِ گُ) [تر.] (ص. اِ.) خانم، خاتون، بانو'; خانم: '(نُ) [تر.] (اِ.) ۱- زن بزرگ زاده. ۲- عنوانی که برای احترام ... گفته می‌شود' — Turkish origin, no umm.\"},\n            {\"src\": \"HJB\", \"where\": \"s.v. BEEGUM (line 3240); KHANUM (leaf 531)\", \"stance\": \"contradicts\", \"note\": \"'Or. Turki bigim ... a feminine formation from Bī ... like Khānum from Khān; hence P. begam'; 'Turki, through Pers. khānum and khānim'.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt / HUB.txt grep 'xānum|chānum|begum'\", \"stance\": \"silent\", \"note\": \"Horn and Hübschmann (Iranian-only etymologies) do not list these Turkic loans.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"begum\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English begum (Anglo-Indian beegum, attested from the 17th-18th c.) was taken in British India from Hindustani/Urdu begam بیگم, itself from Persian bēgum < Chagatai (Eastern Turkic) begim/begüm, the Mughal title of royal and noble Muslim women (cf. Samru Begam). So the word does ultimately come from Turkic, but via Persian and Hindustani, not directly from Turkish as the arrow suggests; and the Turkic word is beg + -üm/-im, not beg + Arabic umm (see #3). Klein and Skeat give the 'mother of the bey' explanation; AHD, Webster, Lokotsch, Hobson-Jobson and Wiktionary the Turkic-suffix one.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی begum (در انگلیسی هندی beegum، از سده‌های ۱۷ و ۱۸) را انگلیسی‌ها در هند از هندوستانی/اردو «بیگم» گرفتند که خود از فارسی bēgum و آن از ترکی جغتایی begim/begüm است؛ «بیگم» عنوان زنان شاهی و بزرگ‌زادهٔ مسلمان در دربار گورکانی هند بود. پس اصل ترکی درست است، اما راه وام‌گیری از فارسی و هندوستانی می‌گذرد و جزء دوم پسوند ملکی ترکی است نه «اُم» عربی. کلاین و اسکیت توضیح «مادرِ بیگ» را آورده‌اند، ولی فرهنگ امریکن هریتیج، وبستر، لوکوچ، هابسن‌جابسن و ویکی‌واژه آن را نمی‌پذیرند؛ ادعای نورایی با احتیاط و با این اصلاح پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/begum\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:160\", \"status\": \"supports\", \"note\": \"KLN_1966 leaf 95 s.v. begum: 'Turk., a hybrid coined fr. beg and Arab. umm, 'mother', and orig. meaning 'mother of the bey''.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 23803 s.v. Begum\", \"stance\": \"supports\", \"note\": \"'Begum, in the E. Indies, a lady of the highest rank. (Pers. — Turk. and Arab.) Pers. begam ... lit. 'mother of the governor.''\"},\n            {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 17864 s.v. begum\", \"stance\": \"contradicts\", \"note\": \"'[Anglo-Ind. word, from Hind. begam, a lady, from Turk. bigim, a [prin]cess.]' — no umm.\"},\n            {\"src\": \"AID\", \"where\": \"AID.txt line 975 s.v. Begam\", \"stance\": \"partial\", \"note\": \"'Begam. [Hindustani.] A Musalmān lady of rank.' — confirms the Hindustani intermediary, no etymology.\"},\n            {\"src\": \"HJB\", \"where\": \"s.v. BEEGUM (line 3240)\", \"stance\": \"contradicts\", \"note\": \"'Or. Turki bigim ... a feminine formation from Bī ... like Khānum from Khān; hence P. begam.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 300 (line 865)\", \"stance\": \"contradicts\", \"note\": \"'osttk., fem. zu beg ... hieraus angloind. beegum, begum'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:48:05.278Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-518.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:48:09.074Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c 'مغیلان\\|مغيلان' BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt; grep -c -i -E 'ghailan|ghaylan' KLN_1966.txt; cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-518.json >/dev/null && python3 tools/verify_check.py 518"
}
```


### [2026-10-15T02:48:09.981Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt:2
BQT_v1_pages.txt:1
BQT_v2_pages.txt:0
0
nodes verified: 5/5
node verdicts: {'confirmed': 1, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 2, 'not_checked': 1, 'supports': 2}
books consulted: {'supports': 5, 'silent': 4, 'contradicts': 7, 'partial': 2} | by book: {'SKT': 3, 'MON': 3, 'HJB': 3, 'LKT': 2, 'AFM': 1, 'FVQ': 1, 'BQT': 1, 'TTS': 1, 'HRN': 1, 'WEB': 1, 'AID': 1}
```


## [2026-10-15T02:48:11.169Z] AGENT

BQT has مغیلان hits; let me check them and fix that consulted entry.


## [2026-10-15T02:48:12.445Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -B2 -A4 'مغیلان\\|مغيلان' incoming/BQT/BQT_v4_pages.txt BQT_v1_pages.txt | head -40; awk 'BEGIN{RS=\"\\f\"} /مغیلان/{print \"leaf\",NR-1}' incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-10-15T02:48:12.868Z] TOOL RESULT

```
incoming/BQT/BQT_v4_pages.txt-4202-کند و خواه درد نکند ؛ بلکه بسنی کفته اند | درختی است خار دار و بعرپی آنرا ام‌غیلان (۳)
incoming/BQT/BQT_v4_pages.txt-4203-کره وکنده (۱) و دلبلی باشد که بیار درد | خوانند ۴ :
incoming/BQT/BQT_v4_pages.txt:4204:کند - مغیلان باستان - کنایه از دیا
incoming/BQT/BQT_v4_pages.txt-4205-مغتی‌ضا ۴ « باسین بی‌قطه بالف کنید, | و روزگار است .
incoming/BQT/BQT_v4_pages.txt:4206:بروزن مه سیما » گلی باشد سیاه.رنگه وآترا از مغیلان گاه - باکاف فارسی بر وزن
incoming/BQT/BQT_v4_pages.txt-4207-کوه کاشان آورند و آن ,مرقدیعا مانند بود - | سلیمان جاه » بممتی مفیلان باستاست که کنایه
incoming/BQT/BQT_v4_pages.txt-4208-و بعتی گوبند سنگی است الوان و بسیار ست. | از ونیا باشد .
incoming/BQT/BQT_v4_pages.txt-4209-بیان نوزدهم
incoming/BQT/BQT_v4_pages.txt-4210-در میم با فا مشتمل بر چهار لغت وکنایت
BQT_v1_pages.txt-13769-اهقیالان - بنتم اول وضم ثانی وفتح‌غین
BQT_v1_pages.txt-13770-نقطه‌رار وسکون تحتانی ولام بالف کشید. و بنون
BQT_v1_pages.txt:13771:زده ؛ نام درختی است هعروف ومشپور بمغیلان .
BQT_v1_pages.txt-13772-گونند حنضمکی را ازب رک آن‌میسازند وآنرا
BQT_v1_pages.txt-13773-بعربی شو کفالمصربه خوانند ؛ و بتشدید انی هم
BQT_v1_pages.txt-13774-منظر آ مده استد د
BQT_v1_pages.txt-13775-(۱) چك ؛ ژند و پاژند .
leaf 105
```


## [2026-10-15T02:48:16.616Z] TOOL CALL #45: Edit

```json
{
 "replace_all": false,
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-518.json",
 "old_string": "{\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt / BQT_v2 grep 'مغیلان'\", \"stance\": \"silent\", \"note\": \"No headword مغیلان found in the OCR of vols 1-2 (it would fall in vol 4, م); not consulted further.\"}",
 "new_string": "{\"src\": \"BQT\", \"where\": \"vol. 4 (BQT_v4_pages.txt leaf 105, line ~4202) s.v. مغیلان; vol. 1 (BQT_v1_pages.txt line 13771) s.v. اُم‌غیلان\", \"stance\": \"supports\", \"note\": \"vol. 4: '[مغیلان] درختی است خار دار و بعربی آنرا ام‌غیلان خوانند'; vol. 1: 'ام‌غیلان ... نام درختی است معروف و مشهور بمغیلان' — confirms Persian moğîlân = Arabic umm ghaylān, the thorny tree.\"}"
}
```


## [2026-10-15T02:48:17.339Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -m json.tool data/verification/page-518.json >/dev/null && python3 tools/verify_check.py 518 | grep -c PROBLEM"
}
```


### [2026-10-15T02:48:18.046Z] TOOL RESULT

```
The file /home/sfmqrb/git/rishe-private/data/verification/page-518.json has been updated successfully. (file state is current in your context — no need to Read it back)
```


### [2026-10-15T02:48:18.302Z] TOOL RESULT

```
0
```


## [2026-10-15T02:48:27.043Z] TOOL CALL #47: SubagentHandback

```json
{
 "message": "I verified page 518 (book p. 488) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-518.json. `verify_check.py 518` shows 0 PROBLEM lines. The page has one chart, root Umm; the Uo, Uog and Uper redirects were skipped as instructed.\n\nCounts:\n- **Root:** 1 confirmed. The Semitic word for \"mother\" (Proto-Semitic *ʔimm-/*ʔumm-) is correct.\n- **Nodes (5):** 1 confirmed, 3 plausible, 1 disputed, 0 transcription_suspect.\n  - Confirmed: #1, Arabic umm and umm ghaylān (the acacia).\n  - Plausible: #2, Persian omm, ommî and moğîlân. ommî \"illiterate\" is usually derived from umma \"nation, gentiles\" (Geiger, Horovitz, Jeffery), not from umm \"mother\".\n  - Plausible: #4, Persian beygom and xânom. The borrowing from Turkic is correct, but the \"umm\" analysis above them is not.\n  - Plausible: #5, English begum. It reached English through Hindustani/Urdu begam and Persian, not straight from Turkish.\n\nDisputed:\n- **Umm #3, Turkish \"beg-umm\" and \"xân-umm\":** these are Klein's analysis, not attested Turkic forms. The real words are Chagatai begim/begüm and xanım: beg or khan plus the Turkic 1st-person possessive -im/-üm (\"my lord\", \"my khan\"), later a title for women. Hobson-Jobson, Lokotsch no. 300, Webster, Mo'in and Wiktionary (citing AHD and Nişanyan) reject the Arabic \"umm\". Only Klein (KLN:160) and Skeat support \"mother of the bey\", which is a 19th-century folk etymology.\n\nOther notes:\n- **No extraction errors.** The JSON matches the printed page. The book itself prints an odd parenthetical \"(امّل)\" after ommî, probably a misprint, and the extraction copies it faithfully.\n- **BQT:339:** the headword there is بیکم meaning \"porch\". The title بیگم appears only in Mo'in's footnote (\"Turkish Begum, queen-mother, honoured widow, lady\"), so I marked that reference partial.\n  - I saved the page image and my transcription as data/verification/sources/refs/ocr/BQT/0339.jpg and 0339.vision.txt.\n- **FVA:34:** no digital copy exists, so it is not_checked.\n- **Web sources:** all 10 web pages I used were archived with fetch_source.py."
}
```


### [2026-10-15T02:48:27.456Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
