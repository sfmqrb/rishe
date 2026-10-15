# Verification process log — verify-page-508


## [2026-10-15T02:44:16.346Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 508 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-508.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-508.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-508.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 508` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.416Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.602Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.655Z] TOOL RESULT

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


## [2026-10-15T02:44:21.670Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-508.txt; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ | head -100"
}
```


### [2026-10-15T02:44:22.165Z] TOOL RESULT

```
=== PDF page 508 (book page 478) ===
--- entry 0 ---
ROOT Teu 2 -> redirect to Steu 2
--- entry 1 ---
ROOT [Indo-European] Teub, Tebh, Tebhos : side  (refs IEC:1371,1676)
#1 (parent #0) [Persian] refs=IEC:1371,1676; MON:1158 | tŭ «تو ٢» : fold, plait, inside | extra: توی ، توه
#2 (parent #0) [Pahlavi] refs=HRN:165; MON:1942 | sŭk, sôk : side, direction
  #3 (parent #2) [Persian] refs=BQT:1182; MON:1942; IEC:1371,1676 | sŭ «سو» : direction, path | extra: سوی ، چهارسو
    #4 (parent #3) [Arabic] refs=FVF:380 | sôq : path
      #5 (parent #4) [Persian] refs=BQT:1182; MON:1955 | sŭq «سوق» : inroads of a bazaar ; sŭqî «سوقی» : bazaar man, businessman | extra: چهارسوق ، اسواق ؛ سوقیّه
#6 (parent #0) [Armenian] refs=IEC:1371,1676 | kov : side, rib
--- entry 2 ---
ROOT Teuk -> redirect to Tĕu 1
--- entry 3 ---
ROOT Teuk-os -> redirect to Keku
--- entry 4 ---
ROOT Teup -> redirect to Steu 2
--- entry 5 ---
ROOT [Indo-European] Teus : empty  (refs POK:1085)
#1 (parent #0) [Avestan / Old Persian] refs=POK:1085; SYN:933 | taoš, tuš, tusen, tussya : empty
  #2 (parent #1) [Pahlavi] refs=BQT:539; SNS:151 | tihîk, tuhîk : empty
    #3 (parent #2) [Persian] refs=BQT:539,537; HRN:90 | tah «ته» : bottom ; tahî «تهی» : empty | extra: تهی
#4 (parent #0) [Latin] refs=POK:1085 | tesqua : empty
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
```


## [2026-10-15T02:44:26.184Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 80,200p data/verification/sources/SOURCE_MATRIX.md; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','MON','BQT','FVF','FVQ','SNS','HRN','POK','SYN']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700])\n\"; cat tools/verify_check.py | head -150"
}
```


### [2026-10-15T02:44:26.545Z] TOOL RESULT

```
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
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

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Rec
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/de
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


## [2026-10-15T02:44:37.832Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/508.jpg; python3 -m json.tool data/extracted/batch/page-508.json | head -150; ls data/verification/page-50*.json; "
}
```


### [2026-10-15T02:44:38.359Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   64k sfmqrb 14 Oct 22:15  site/pages/508.jpg
{
    "pdf_page": 508,
    "book_page": 478,
    "entries": [
        {
            "root": {
                "name": "Teu 2",
                "redirect": "Steu 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Teub, Tebh, Tebhos",
                "lang": "Indo-European",
                "refs": "IEC:1371,1676",
                "gloss": "side"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "IEC:1371,1676; MON:1158",
                    "words": [
                        {
                            "translit": "t\u016d",
                            "gloss": "fold, plait, inside",
                            "script": "\u062a\u0648 \u0662"
                        }
                    ],
                    "script_extra": "\u062a\u0648\u06cc \u060c \u062a\u0648\u0647",
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0631 \u062f\u0644 \u062e\u0648\u06cc\u0634 \u0637\u0627\u0647\u0631\u0627 \u06af\u0634\u062a \u0648 \u0646\u062f\u06cc\u062f \u062c\u0632 \u062a\u0631\u0627 - \u0635\u0641\u0647 \u0628\u0647 \u0635\u0641\u0647 \u0644\u0627\u0628\u0647 \u067e\u0631\u062f\u0647 \u0628\u0647 \u067e\u0631\u062f\u0647 \u062a\u0648 \u0628\u0647 \u062a\u0648",
                        "poet": "T\u00e2her\u00ee Ghazv\u00een\u00ee"
                    }
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Pahlavi",
                    "refs": "HRN:165; MON:1942",
                    "words": [
                        {
                            "translit": "s\u016dk, s\u00f4k",
                            "gloss": "side, direction",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:1182; MON:1942; IEC:1371,1676",
                    "words": [
                        {
                            "translit": "s\u016d",
                            "gloss": "direction, path",
                            "script": "\u0633\u0648"
                        }
                    ],
                    "script_extra": "\u0633\u0648\u06cc \u060c \u0686\u0647\u0627\u0631\u0633\u0648",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u062c\u0627\u0646 \u0627\u0648 \u06a9\u0647 \u0628\u0634\u06a9\u0631\u0627\u0646\u0647 \u062c\u0627\u0646 \u0628\u0631\u0627\u0641\u0634\u0627\u0646\u0645 - \u0627\u06af\u0631 \u0628\u0633\u0648\u06cc \u0645\u0646 \u0622\u0631\u06cc \u067e\u06cc\u0627\u0645\u06cc \u0627\u0632 \u0628\u0631 \u062f\u0648\u0633\u062a",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Arabic",
                    "refs": "FVF:380",
                    "words": [
                        {
                            "translit": "s\u00f4q",
                            "gloss": "path",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "BQT:1182; MON:1955",
                    "words": [
                        {
                            "translit": "s\u016dq",
                            "gloss": "inroads of a bazaar",
                            "script": "\u0633\u0648\u0642"
                        },
                        {
                            "translit": "s\u016dq\u00ee",
                            "gloss": "bazaar man, businessman",
                            "script": "\u0633\u0648\u0642\u06cc"
                        }
                    ],
                    "script_extra": "\u0686\u0647\u0627\u0631\u0633\u0648\u0642 \u060c \u0627\u0633\u0648\u0627\u0642 \u061b \u0633\u0648\u0642\u06cc\u0651\u0647",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Armenian",
                    "refs": "IEC:1371,1676",
                    "words": [
                        {
                            "translit": "kov",
                            "gloss": "side, rib",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Teuk",
                "redirect": "T\u0115u 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Teuk-os",
                "redirect": "Keku"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Teup",
                "redirect": "Steu 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Teus",
                "lang": "Indo-European",
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
```


## [2026-10-15T02:44:41.009Z] TOOL CALL #5: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/508.jpg"
}
```


### [2026-10-15T02:44:41.034Z] TOOL RESULT

```

```


## [2026-10-15T02:44:45.020Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 699 700 701; do echo \"=== leaf $l\"; awk -v n=$((l+1)) 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -n -i -E 'teub|tebh|tebhos|kov|side' ; done; grep -n -i -E 'tebh|t[eē]ub' IEC.txt | head -20"
}
```


### [2026-10-15T02:44:45.492Z] TOOL RESULT

```
=== leaf 699
7:WP II, 672 Skt. sphürjami, v. (“burst forth'. Skt. -j- se- condary); Av. (o-gde) sparoga-, v. 'shoot'; Gk. spargein, v. *wanton, be passionate' beside spárge, f. ‘passion’; spargáo, denom. ‘teem’; spharagéomai (variant: ‘bulge, be teeming’); Latv. spirgstu, spirgt, v. “recover, be strong. Nominal types in Skt. sphürjah, m. (2) *out- break’; Gk. spáragos, m. ‘whizz’; Av. sporogo, m. ‘shoot’; cf. Gk. a-spáragos (for *as-sparagos *asparagus) and krambo-spáragon 'sprout- ing broccoli? and the plant in Skt. sphürja- kah; OCS prüga, f. ‘new wheat, but Pol. pierzga = ‘caulking’ and Cz. prha = ‘arnica’; Li. spirgas & spirgis, gs: -io, m. ‘fried bacon, crackling’; spirgu, eti, v. “fry, sizzle’. (A type *sprugl- is represented in W ffrwyl, m. *drizzle, sea-spray; Du. sprokkel, m. “dry under- growth’; LG sprockeln, v. ‘sizzle’. Here also Srb. pržiti, inf. (fry: Li. spirgeti); o-gde in Cz. praZit, inf. id.)
10:sprið (sph-) (2) “blow, scatter’. WP II, 668 (e-gde in) Skt. spharami v. “discharge, diffuse’; (e-gde in) Arm. prem, v. ‘spread, unfurl’; (prob. o-gde in) parat, adj. (/scattered'. See sporod-); Hitt. sparhi, v. (1) ‘spread’; Gk. cf. speíro, Aeol. spérro, aor. pass. e-spáren, v. ‘sow?’ beside sparnós, adj. “scattered; rare’; a-spaíro ‘pant’; Alb. fryej, fryj, aor. fryna, fryra & fryjta, v. ‘blow’; m-fry,, v. ‘inflate’; Srb. cf. (o-gde) spore adv. ‘quickly’
22:sprk- (sph-) (1) ‘urge’ Ir. spriocaim, v. id. beside siorc, pl. -anna, m. (jerk, toss’, fr. *sp-); Pol. cf. szparki, adj. *nimble'
=== leaf 700
3:sprn- (sphrn-) (2) “kick, tread'. Cf. spero, spern- Hitt. sparhi, v. (2) ‘trample’ beside sparnumi, v. *destroy'; (e-gde in) Lat. sperno, ére, v. ‘despise’; Ir. cf. sparnaim, spairnim, v. (struggle, fr. *sphorn-); OHG cf. fir-spurnan beside -spirnan, v. *kick'; OE spurnan, v. ‘kick; bump; stumble; spurn' beside spyrnan, v. *stumble'; ON sporna, v. ‘trample on; spurn”
6:spüd- (sphüd-) ‘stab; dart, dash forth, thrust'. Cf. speud-, spoud- Alb. (ambig.) fus, aor. futa, v. (thrust", from speud- or sputio); Du. spuiten, tr. ‘inject; intr. ‘spurt’; ME spouten, v. ‘spout; Sw. sputa, v. id.; Li. spüdZiu, spüdéti, v. (“have stitch in the side: ON spýta, v. inf. ‘to skewer’; mod. ‘to spurt’). Nominal types: Du. spuit, f. ‘squirt, jet, waterspout'; Li. spüdus, adj. ‘tight; spüdis, gs: spüdZio, m. ‘squeeze’
13:spurg- (spurĝ-) ‘fibre, tuft. Cf. WP II, 674 Arm. (variant) purc, s. ‘tussock, wad, tuft; Li. spurgas, m. ‘tuft’ beside spurgala, f. ‘tuft, fibre, clump’; Latv. spurdze, f. ‘catkin’
27:sphált- “bang, burst. WP II, 677 Skt. sphatami, pp: sphatitáh, v. id. beside phat! “bang! phut!"; Gk. sphalásso, v. ‘cut, stab’; Br. fauta, tr. & intr. inf. ‘split; faut, pp. id.; MLG spalden, MHG spalten, sv. 7. ‘split’; Fris. spálte, id.; Icel. cf. speldi, n. "flap, valve'
=== leaf 701
6:spherð, io (1) cf. sprio , sperió (1) Skt. phalàmi, v. “bound, dash, burst forth? beside spharáyàmi, v. ‘diffuse, radiate, dis- charge, expand’; redup. in pharpharàye, v. “dart about": Arm. prem, v. ‘scatter’; Hitt. cf. sparhi, v. (1) “spread, cover’; Gk. speiro, v. ‘scatter’; Br. speria, inf. (conceive, become
12:sphétos, is, ios (expanded; expanse’. Cf. spét- (?) and WP II, 657; sphëið Skt. sphatih, f. “growth? beside sphitab “abun- dant’; sphità, f. ‘wellbeing’; Go. cf. sped- in spediza, comp. "ater; OHG spáti, MHG spaete, adj. ‘late’; Du. spade, adj. ‘slow, late’; Sw. späd, adj. ‘young, tender’; cf. späda, v. *rarefy'; Li. spétas, m. “leisure, idleness’
13:(sphar-, cf. sphétos, sphéió beside sporos (1) to (4). Slav. ambig. Skt. sphiráh, adj. ‘fat; OCS (ambig.) sporü, adj. ample, abundant’; R spóryj, adj. “thriv- ing, profitable")
26:Sw. spricka, Norw. sprekke, v. ‘burst, crack beside Norw. sprike, v. ‘sprawl, stretch; bristle; jut out’; Li. sprigis, sprygis, gs: -io, m. ‘rap, fillip, tap’; sprige, mf. ‘testy person’. Cf. spxeg-, sprog-. (Norw. ambig., but cf. sprette, v. “leap, kick, start" beside spretten, adj. ‘frisky’ if for an extn. of type *sprigto-). Latv. cf. spridzigs, adj. ‘agile’; spridzinàát, inf. ‘sputter, crackle’. Metathesis in OE spircan, v. 'sprinkle; sparkle?
17218:(steubh-, see Supt:S)
18235:tāp- — tebh-, us
18248:tebh-, us (?) 'side'. Cf. Supt. tueb-, toib-
18251:tebhe, tebhei, ds. ‘to thee’. Cf. teue. Alb. ambig. Alb. ambig. ty, id. cf. teue; also dial. tyj; Lat. tibi; Osc. tifei, Umb. tefe, id.; OPr. tebei, id. (but OCS and com. Sl. tebe, acc. sg.)
18258:tebhe, tebhei — tek-
18443:terp- — teubh- (tubh-)
18459:teub- ‘sway’ Srb. cubam se, v. ‘swing, sway’; Lat. cf. (re- dup.) titubo, are, v. ‘stagger, hesitate; stam- mer
18460:teubh- (tubh-) (1) 'struggle; fight, attack". Cf. WP I, 714
18463:teubh- (2) ‘tuft, clump, hump’. Cf. tūbhos Arm. (ambig.) Éov, u, u, s. (tuft. See SEM: Arm. & IE: $8 56, 75, 87); Lat. cf. über, gs: -eris, n. (formerly an -es-/-os- stem) “lump”; Lat. LW fr. Umb. tüfa, f. ‘plume’; Ir. cf. tua- bhal & tua(bh), m. ‘burdock’; Srb. Cuba, f. ‘crest of hen’; OCS Cubü, m. id.; R Cub "Tore, lock’; Pol. czub ('tuft^, fr. *teubh- (teub-), or fr. *Fkeubh- (keub-) ?); (zero-gde in) OE pàf, m. id. (and ‘tuft of leaves’), cf. byfel, m. ‘shrub’; Upper G Düppel, s. “lump”; ON püfa, f. ‘mound’; Li. tübas, tübà, mf. ‘felt’; tübe, f. ‘mullein’?
18467:teubh- — teukso, ið
18517:teue, teui, teu, “thee, to thee". Cf. tebhe, tü, teuos Doric cf. teŭ “of thee’; tei ‘to thee’; Gk. cf. teu in phr: antía teu “before thee’; Alb. (am- big.) ty, acc. & dat. “thee, to thee’; Osc. cf. tiú, tiium, nom. ‘thou’; Umb. tiom, acc. ‘thee’; Li. tav, tau, acc. id.; OLi. taui, id.; Latv. tevi, acc. id.; tev, dat. ‘to thee’
18519:teuos 'thy, thine'. Cf. teue, teui, tebhe & tuos. (Pronominal variants)
18532:(to, w.s.p. form of teue, tebhi, etc. in Alb. té “thee, to thee’; OLi. ti, id.; cf. W dy “thy, thine’)
18846:(toui, see teui & tebhi. O-gde by assimilation in OLi. taui ‘to thee’; Li. táu, id.; beside Alb. ty, id. and Latv. tev, id.)
19409:tue- (oblique theme) ‘thee’. Cf. te, teue, tebhi, etc. Skt. cf. tva, id.; Arm. cf. z-Ke-z, id. (fr. *&e-tue- ĝe); Cretan twé (Hes.); Hitt. cf. (wei gen. “Of thee’; twe-tac & twe-dac, abl. “from thee’
```


## [2026-10-15T02:44:48.041Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 18244,18250p IEC.txt; grep -n -E '^ *(tueb|toib|tēbh|tebhos|tewbh)' IEC.txt|head; grep -n -E 'tueb-|toib-' IEC.txt | head"
}
```


### [2026-10-15T02:44:48.400Z] TOOL RESULT

```
tàuió (1) “melt, dissolve’. Variant of type tàio (1), q.v. OS thóian, v. ‘thaw, digest; MHG douwen, dóuwen, v. “digest, consume'; OE pawian v. ‘thaw’ Du. dooien, id.; dooi, m. id.; ON beyja, v. id.; beyr, pl. peyir, m. id.; Sw. (oa, v. id.; Cz. tavit, inf. ‘melt, smelt’
tauiü (2) “silence; be silent". Variant tauuió W tewi, inf., taw, 3sg. "be silent’; ON þagga, v. ‘silence’
te, correlative particle of type que, q. v. ‘that, so that, let.. ? Per. tà, cj. ‘that’; Romani te, subjunctive part.; Arm. cf. tẹ (“or”, fr. *te siet “that it be"); Myc. cf. o-te, adverbial conj. ‘when’; Gk. hó-te, Lesb. o-ta, id., cf. also Gk. -te in deü-te! ‘come here!; Lycian ti, pt. ‘may, shall; Alb. të, subjunctive pt. as in té jetë (fr. *te sjét); doubly represented as a jussive part. in EMAIb. té vem-té “let us go’; OLat. cf. on. Lat. u-t, subjunctive pt.; Br. cf. holla-ta! (^hel- lo-there', fr. *-to); OE pe, cj. ‘when; then; or: op be “until; pe... pe... “either ... or; OFris. the, cj. as OE; OCS, Srb. te, cj. rand: R cf. pólno-te! *enough!; pojdjóm-te! “let us Sol: Cz. cf. na-te! “there you are"; Li. te! “behold! voilà" beside OLi. te-esmi ‘may I be’; te-sié “let him be’; te-bünié! te-gyvuoja! “let him be, long live!, etc. beside Zemaite testa (let him be fr. te esto!); Latv. te, cj. “then, there’; as adv. te... te... (now... now ...). Variant in Ober tya, cj. “that, so that beside mà-tya ‘lest’; Lüneb. Wendish tja, sub- junctive part. As a suffix, cf. also Go. du-pe, du-h-p&, adverbial cj. “because?
te “thee” Tokh. B cf. -c, enclitic, id.; Lat. te; Cz. tě, id. but R te, ds. ‘to thee?
tebh-, us (?) 'side'. Cf. Supt. tueb-, toib-
1371
Oss. Gw s. “face, of dice’; Per. tav, tū, s. “fold, plait; Hitt. tapus, s. ‘side’. (The phonol. is obscure, as also that of Arm. Kov ‘side’; Per. sü, suy, id.; Ir. taobh, id.; W tu, id.)
19410:tuebó “worship, sanctify’. (Lat. forms ambig. Cf. dhueb-) Gk. sébo, v. “worship, honour’; Lat. cf. fe- bruus, adj. ‘hallowed, purified"; februa, npl. ‘feast of atonement; sacrifices to the dead’; Sabine februm, n. ‘purification’; Du. dwepen, v. ‘dote on, idolize’
3369:dhuebo ‘worship, honour, sanctify’. A pos- sible alternative to tuebó, q. v. Gk. sébo; Lat. februus; februa; Sabine februm (*dhueb- or *tueb-); Du. dwepen (‘dote on, idolize'. Gmc. parallels absent)
18248:tebh-, us (?) 'side'. Cf. Supt. tueb-, toib-
```


## [2026-10-15T02:44:51.954Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'toib|tueb|taobh' IEC.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==854 || NR==853' IEC.txt | grep -n -i -E 'side|tueb|toib' | head"
}
```


### [2026-10-15T02:44:52.631Z] TOOL RESULT

```
3369:dhuebo ‘worship, honour, sanctify’. A pos- sible alternative to tuebó, q. v. Gk. sébo; Lat. februus; februa; Sabine februm (*dhueb- or *tueb-); Du. dwepen (‘dote on, idolize'. Gmc. parallels absent)
17673:sthoibos, à, ios “pile, mound, stuffing, stif- fening'. WP II, 648 Gk. stoibé, f. ‘heap; stuffing’; G Steife, f. “stay, strut; stiffening'; E stope, s. 'seam-gap in mining’; Li. stíebas, m. “mast, pole; pith, core, haulm' beside stáibis, io, m. “pile, post; lower leg’. Extn. in LG steiper, m. ‘prop’; (Latv. stiebrs ‘stem’ is ambig. (*sthembr-?))
18248:tebh-, us (?) 'side'. Cf. Supt. tueb-, toib-
18250:Oss. Gw s. “face, of dice’; Per. tav, tū, s. “fold, plait; Hitt. tapus, s. ‘side’. (The phonol. is obscure, as also that of Arm. Kov ‘side’; Per. sü, suy, id.; Ir. taobh, id.; W tu, id.)
19410:tuebó “worship, sanctify’. (Lat. forms ambig. Cf. dhueb-) Gk. sébo, v. “worship, honour’; Lat. cf. fe- bruus, adj. ‘hallowed, purified"; februa, npl. ‘feast of atonement; sacrifices to the dead’; Sabine februm, n. ‘purification’; Du. dwepen, v. ‘dote on, idolize’
11:uisuos, ios “equal, equable' Skt. cf. visvam, n. acc. ‘equinox’; visu-, cpds. "bilateral, equal; Myc. wis(0)wo- ‘equal’; Ar- cad. wíswos, id.; Gk. ísos, f: eíse, id.; Hes. issos, s. ‘calm at sea’; Olr. fo, adj. ‘equal’; OBr. cf. an-guo 'un-equal'; Go. wis, s. ‘calm at sea' beside G wau, adv. (‘dead calm”. Pho- nol. of Wau ‘dye-plant’ fr. *uisios or sim.)
13:uit- (1) ‘withy, twisted root, twist, branch, wind'. WP I, 224. Cf. uitus, uitikos & uits- as separate entries Oss. wis, pl. wistä ‘withy’; Per. bid ‘willow’; Tokh. AB cf. witsako, s. ‘root’; Gk. cf. 1téa, f. ‘willow; wicker shield’; Lat. vitis, gpl: -ium, f. ‘vine’; OHG wida, MHG wide, f. ‘willow’; OE wióige, wm. ‘withy’; ON víðir, gs: víðis, m. ‘willow’ beside vió, pl. -jar, f., and viója, f. ‘withy’; Sw. vidja, f. id.; OCS viti, f. “twist, rope"; Pol. wić, f. ‘withy’; Ukr. vit, f. branch’; OCS cf. also po-viti, f. ‘shoot, runner’, and vica, f. (switch, rog’, fr. *uitika); Li. vytis, -iĉs, f. ‘withy, branch, shoot’; Latv. vits ‘twisted strand”; vite, f. ‘hank, screw thread, tendril, creeper’. (Short vowel in ON við E viðja (withy'; mod. ‘skein’); Ir. feath, m. "wood. bine’; OCor. guiden, later gūzen, pl. -ennow, f. (withy, bond, faggot’: Ir. feathan, m. (2) ‘band, ring), W gwden, pi. -i, f. ‘withy’. A variant arises in MIr. feithe, gs. ‘of woodbine’; Ir. féith, f. ‘withy’, fr. a type *ųeiti-. Iso- phone: W gwid, m. ‘sudden turn’)
35:gwden, f. ‘withe’ beside gwd, m. “wind, twist, turn’; Go. cf. kuna-wida, f. ‘fetter’; OE cyne- wióóe, f. ‘diadem’; wióóe, f. “band, thong; ON vió, pl. -jar, ^withy, collar? beside mod. vóóvi, m. ‘muscle’; MHG wit, wid, wide, sf. ‘lash of withies'; LG Wiede, Widde, f. ‘withe’; Blg. vitva, f. (clematis', fr. *uit-); Li. cf. vytu- vas, m. “roll, spool
```


## [2026-10-15T02:44:56.393Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 850 851 852 853 854 855 856 857; do echo \"== $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | grep -o -E '^.{0,60}' | head -40 | tr '\\n' '|'; echo; done"
}
```


### [2026-10-15T02:44:56.958Z] TOOL RESULT

```
== 850
 cf. am- usin, s. (spouse, fr. *som-uiKin-, cf. Lat. uxor, i|uiKmti (uiKomti, uim) ‘twenty’. Cf. ui-, px. and dui-; dekmt|(uiKpotis, see uoiKpotis)|uiKt- (uiKit-) ‘restful, quiet'. Cf. uik- and|uoik- Skt. cf. sam-vistab, adj. ‘resting’; Ober cf. vi- šta-|uil- (1) «twisted, twisty, cunning; deceit. Cf. ueilis, uoil|uil- (2) “a sea-bird, mew’. Cf. uail- (1).|Onomat. OBr. cf. guilan, pl. -annu ‘gull’ (LW in Fr. goéland|uil- (uilio) (3) “look, watch, expect, hope’. Gk. ambig. Cf.|uiK- — uin-|15|20|25|30|35|40|45|1542|Gk. ? (ambig.) hil&mi, hiláo, v. “be favourable’; hílaos ‘pr|uileuos? ‘turning, round; turn, roll" Cf. ui- luó, ið. Ambig|uiltos, ios troguery; rogue’. Cf. uil- (1) Skt. vitah, m. ‘r|uiluo, ið “turn, wind, twist. Cf. ueluó (1), uoluó, ulu- and|unmnn- (uimnt-) (twist. Cf. ueio (uiieio) (1). Variants: uim|uin- (1) (uinis, ios, io) ‘kinsman, friend’. Cf. n-uin-. |
== 851
WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. |1543|id.; ON vinr, m. pl: vinir, beside vina, f. ‘friend’; Sw. vä|uïn- (2) (uīnis, ios, à, io) ‘twist, bend’. Cf. ulio, uifor-|uind- ‘see, discover, know’. (Infixed variant of type uid-, |uinghlos (or uinghul-) ON vingull, m. “penis of horse’; Li. |(uing- ‘elm’. Variant of type uif (2), q.v. in Pol. wiąz, R |(uink-, nasal-infixed variant of type uik- (1) in Lat. vinco|uip- “shake; shaky, tremulous'. Cf. uoip- (1) Skt. vip, mfn.|uir- (1) “boil, seethe; eddy, whirl, spin’. WP I, 269 Br. gw|uir- (2) ‘twist, cable, wire’. Variant of type|uin- — uiruos, is, io|20|25|30|35|40|45|1544|uiior-, q. v. Same as (1) (?) Cf. uiruos. Lat. víria ‘neckla|uir- (3), see uiros and next|uirátos (uirotos) «team of men, troop’. Cf. uiros Skt. cf. v|uiréio “be a man, be strong’. Cf. ulros. Lat. ambig. Cf. uis|uiring- (uiruig- ?) “twist; twisting, writhing’. Cf. uiruos,|uiros |
== 852
“man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. |uiruos, is, io ‘twist, twine, gut, string, spiral. Cf. uir- |1545|‘written character’; Gk. cf. iris, dial. wiris, gs; -idos, f|uis (1) “strength, youth'. Cf. guis, uis- (5) and uisàaió, e|uis- (2) ‘colouring matter, dye’. WP I, 236. (Variant ui- ?)|uls- (3) (uisos, ios, iom) ‘poison’. Cf. uis- dhlo-. WP I, 2|uis- (4) Av. viš-, v. ‘wet’; Hitt. wisis or wesis, s. *pas- |uis- (5) (uisis, os, uisuos, uisios, uisiuos) “all; totality|uisãið, eio “get strong’. Ambiguity in Gk. and Lat. Cf. uis |uis — uisg-|10|15|20|25|30|35|40|45|1546|Cf. also: guis, guiseros Gk. iáomai, Ion. fut. iésomai, v. “|uis-dhlom, à (uisdhil-), extn. of type uis- (2), q. v. and c|uisolos (1) (uislos) ‘poisonous, foul". Cf. uis- (3) and uis|
== 853
rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isopho|uisolos (2) (uislos, us) 'abundant, produc- tive’. Cf. uis (|uisalos, à (uisul-) (3) ‘weasel, ferret, pine- marten' or si|uisəros (uisros) (1) ‘gory, foul’. Var. of uiso- los (1). Cf|uisoros (2) ‘vigorous’. Cf. uisalos (2) and uis (1) Gk. dial|uisg- (1) (uizg-) *haulm, stick, twig, bunch, faggot Lat. vi|1547|f, feag, m. ‘rush, reed; OHG wisk, sm. n. “bunch?|uisg- (2); uisghnos; uisgheuor; uisghus, see supt: U W gwysg|(uistis, os, see uidtis, os)|uisuos, ios “equal, equable' Skt. cf. visvam, n. acc. ‘equin|uit-, radical form of the following entries: ‘wind, twist, b|uit- (1) ‘withy, twisted root, twist, branch, wind'. WP I, 2|uit- (2) “hunt, chase’. Cf. uoit- and ueið (2), ueit- Skt. v|uisg- — ultsis, os|20|25|30|35|40|45|1548|Li. výtas, pp. ‘chased, hunted: výtis, gs: -čio, m. ‘horsema|uit- (3) (uirtós) ‘gone, away, afar’. Cf. ueió (2) and uit- |uit- (4) ‘pleasant, acceptable’; uitis *plea|
== 854
- sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.;|uit- (5) *withered, outworn'. Variant: uiiet-, cf. ueió (uii|ul-teros ‘further, more aloof. Cf. uwi- and -teros. WP I, 31|uitolos, à “small creature, stunted creature, dwarf. Cf. WP |uitikos, à *withy'. Cf. uit- (1), uitus, uits-. Dim. sense: |uifsis, os, variant of type uit- (1), and cf.|1549|uitikos, à „Skt. vithih, f. frow, line’; Oss. wis, pl. wístà|Br. cf. gwéden ‘withy round a faggot; W|gwden, f. ‘withe’ beside gwd, m. “wind, twist, turn’; Go. cf|uiu- ‘wail; wailing creature, widgeon’ or sim. Onomat. W cf.|ufuédh-, redup. form of type uedh- (1), q. v. Hitt. (queried|uífuégh-, redup. of type ue£h-, q.v. Skt. cf. vivahab, m. ('|(uluðið, redup. of type ueið (1) in Du. wuiven, v.; Fris. wi|(ufuéK-, redup. of type ueK- (1) in Skt. vivas- & vava$-, v.|uitulos, uituros, ios — ulost- (ulott-)|10|15|20|25|J0|35|40|45|1550|ufuéqu- (uruéqumi, ufuéquio) “call, ask, say’. Redup. form o|
== 855
Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (H|uluerá, is ‘squirrel’. Cf. ultio. WP I, 264, 287 Lat. (Pliny|uiuid-, redup. of type uid-, q.v. and extns. Skt. cf. vivitt|(uiðið, see ueið, uiieió (1) and (2))|(uielos, see uiiolos)|ulaio (ulàio) ‘surge, seethe’. Cf. ulm- and uln- (2). WP I, |ulam- ‘mud, marsh, ooze, lowland’. WP II, 386 Oss. lámi, s. |ulost- (ulott-), residual form of type *uldht-, cf. ueldho, |1551|gion’; Li. cf. valstius, m. ‘region’; valstybe, f. “politica|ulon-, residual form of type uln- (1) (ulna) ‘wool’, q.v. WP|ulid- “show, pomp, splendour, display, ap- pearance’. (Gmc. |uliqu- “wet; liquid in (1) uliquó, ið, eið Jiquesce; liquefy|
== 856
Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet';|ulobhos (?) *top, head, hill Gk. lóphos, m. ‘neck, mane, tuf|ulod- “evil, harmful, poisonous; harm, poi- son. (Lat. ambig|ulon- — ulg-|20|25|30|35|40|45|1552|Skt. cf. a-vrade, mp. ‘grow soft’; Lat. cf. lolium, n. ‘tare|(ulong-, see Supt: U)|uldh- (1) ‘grow strong, thrive". Skt. ambig. Cf. ueldho, but|uldh- (2) “mild, lukewarm' W gwlydd, adj. ‘mild, soft, tende|(ule-, cf. uelaio. Zero-gde perh. in Gk. aleé, f. “flight, a|ulëið (@ul-, uol-, *uol-) “be strong’. See ual- (2) and cf. |ulg- *wet, damp; dampen'. WP I, 306. Cf. uelg-, (variant uol|1553|‘moisture’; OCS vlaZinú, Cz. vlahý and vlažný ‘damp’, fr. *u|ulgh- ‘tepid’. Variant of ulg- (?). Cf. uolgh- Arm. gayğ, Le|ulguó, v., ulguos, us, s. ‘surge’. Variant in ON ulguh-? but|
== 857
bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelat|(ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið)|ulksuos, à (ul'suos, à) (?) ‘sorcerer, prophet Gk. cf. (?) á|ulm- ‘surge, billow; wide mouth, gulf’. WP I, 298. Gk. ambig|uln- (1) (ulna, ulon-) ‘wool’. WP I, 206. (Var- iant initial|ulgh- — ulquos, is|20|25|30|35|40|45|1554|uln- (2) (ulnis, à) ‘surge, wave’. WP I, 302- 3. (Gk. ambig.|(ulnio (1) see uluið; (2) see ulaið) |
```


## [2026-10-15T02:45:01.132Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 910 925); do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt > /tmp/claude-1000/iec508.txt 2>/dev/null || awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt > $HOME/iec508.txt; done; awk 'BEGIN{RS=\"\\f\"} NR>=905 && NR<=930 {print \"=== \" NR; print}' IEC.txt | grep -n -E '^=== |\\b16[67][0-9]\\b|tueb|toib|side' | head -60"
}
```


### [2026-10-15T02:45:01.818Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:04.845Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; rm -f $HOME/iec508.txt /tmp/claude-1000/iec508.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' IEC.txt; grep -n -E '^ *16(6[0-9]|7[0-9])\\s*$' IEC.txt | head; grep -n -i -E 'Supplement|^tueb|tueb- ' IEC.txt | head"
}
```


### [2026-10-15T02:45:05.237Z] TOOL RESULT

```
858
23:11. 1987. 1573-1684 (uolobhis-uupsios + Supplement + Corrigenda)
127:VAN Wu. N.: Etymologisch Wb. der nederlandse Taal, 1912. With Supplement by C. B. van Haeringen, 1936. Reprint Staatsdrukkerij- en Uitgeverijbedrijf, den Haag 1949
3756:eulos ‘damp’. (For Gk. eule: supplementary note to IE. eul-) Skt. olah; W ul, id.
8570:Kar- (1) (Karie, Károi) (?) ‘trappings, harness’ Per. cf. cpd. af-sar “bridle halter'; Arm. sar, u-st. ‘trappings’ beside sarik, -eac, -eawK, pl. type ‘ropes, trappings’. Li. Sórai, mpl. Char. ness”, though a perfect isogloss, may be a LW fr. Pol. szory, id., a LW also in R &óry, id. fr. G (ge-)schirr with vowel-breaking, see AP: ESRJa, supplement by S. P. Obnorskil, 1949, p. 103, and AB: SEJP: szor, p. 552a. Cf. how- ever Li. Sons, Sorys, m. *troof-saddle, coping")
19410:tuebó “worship, sanctify’. (Lat. forms ambig. Cf. dhueb-) Gk. sébo, v. “worship, honour’; Lat. cf. fe- bruus, adj. ‘hallowed, purified"; februa, npl. ‘feast of atonement; sacrifices to the dead’; Sabine februm, n. ‘purification’; Du. dwepen, v. ‘dote on, idolize’
```


## [2026-10-15T02:45:08.887Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==187' HRN.txt | head -80"
}
```


### [2026-10-15T02:45:09.327Z] TOOL RESULT

```
- 165 -
747. Aeny 'Stein ; Gewicht, Würde', senrjin.
ap. ad^a(n)(jaina' steinern'; phlv. sa{n)(j (P.-V. z. B.
vd. 19 (13)), sang (AV.)
Allgemein entlehnt, z. B. kurd. senk^ seng; af/.
sang ; bei. sing (289) ; sangL. song,
Np. senjJdm (mit sekundärem Infinitiv se/ten —
phlv. sa/tan, sanßt , PP61. ; g. satnmn, Käs. örsaten,
örsatman, verset — PPP. sf?;^^e, Sahn. I, 1 Vers 10)
^wiegen* ist ein sekundäres Denominativum von seng,
Nöldeke (mündliche Mitteilung) schlägt vor, das
altpersische Wort (wie Spiegel, (jlossar) mit an-
lautendem d zu lesen, indem er dieses a in np.
murd]aseng 'Bleiglätte' und must\aseng \Schleuderstein'
wiederfindet. Auch denkt er an Zusammenhang mit
ai. ägman- 'Stein* (vergl. np. rts, No. 22) und (mit
Spiegel und Darmestete r) dem schwierigen aw.
asengöl.gäum (yt. 19, 43)^).
748. sün Stil 'Richtung, Seite', "^ID (Jer. 17, 1).
phlv. sük *Seite, Richtung' 2).
Eine ältere Form ist nicht vorhanden; das np. l
•ff
beruht auf Übertragung (vergl. No. 373). Ursprüng-
lich soft, wie skr. LW. söya- beweist (Weber, Pär.
des Kpn.).
749. suwär, eswär (Lex.) 'Reiter'.
ap. as(s)a]bära- 'Reiter' (doch wohl = *aspabara- ^) ;
phlv. (tsbär 'Reiter, aspwar Ritter (Nöldeke, Karn.
39 Note 2)4).
LW. kurd. suvär ; afy. spör, swör ; bei. sawär (232).
750. sötten 'anzünden, verbrennen, Praes. söz-em^ söz,
nw-^^yü (Qiss. Dan.).
') Zu derselben Auffassung über aw. aaehyö.gäum ist soeben auch
Burtholomae, Indog. Forsch. II, 268 gelangt (Correkturnote).
^) Arab. LW. cahärsüj *Markt', syr. LW. "^IDlNnii^ scheinen
herher zu gehören (ursprünglich *Vierseit, Viereck'); dann etwa auch
die mit s beginnenden, zuletzt von Hübschmann, ZDMG. 46, 247
No. 90 zusammengestellten Worte?
^) Aspa- auch in aw. A8(s)a\hana- {ß. pr.)?
^) Savärdk (vd. 1 (24 J) kann nicht *Reiter* sein.
```


## [2026-10-15T02:45:15.513Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\bs[oō]g\\b|swk' PHD_mackenzie.txt | head; grep -n -E '\\btuhīg|tuhig|twhyk|\\btōy|\\btō\\b' PHD_mackenzie.txt | head; grep -n -E '\\bs[uū]k\\b|sōk|tuhīk|tuhik|tuhīg' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:45:15.869Z] TOOL RESULT

```
611:       2 sog       add N '" 'grief'.
612:for    Sosyans ... read Solins [swk~'ns ...
2283:fiHisofa [pyPswkp)y] philosopher.
3570:miJiig [myc-, myswk/ I N mizii] lentil.
4355:rasiig [lswk' I (N rasa)] weasel.
4557:·Skandar [swkndl I N sihandar] = Aleksandar.
4579: SoAyans [swkfydns = Av. saofyas] saviour (especially the final Saviour
5889:abortion wisudag.                         advantage bahrwarih, sog, sud; v.
6117:   mardanagih.                         burning (n.) dazisn, sog, sozisn,
6235:combustion sog, sozisn.                  conduct (v.) franaftan.
5019:tuhig [twhyk I M twhyg, N tuhi] empty, vain.
6500:emptiness tuhigih.                           essence     ceih, cihr(ag), gohr(ag),
6501:empty tuhig.                                    madag, madayan, xwadih, uruspar.
7877:unhappiness axwarih, axwasih, dus-       vain tuhig.
7940:void (n.) tuhigih.                           tuwiingarih, xwastag.
8207:tanomandih        ~t6~"",               tuhig                             I~,,.
8305:tuhigih             "'U~,~           tast
1760:4. partitive: hac fradandan + han mart kasé anyone of the children of that man 25; hac šmāh xiönän ke hast ke ...? 25” ete.; fratom hac ax" i astomand 53%; xuastom hac z"arisnàn the most delicious of dishes 7413; ete. — 5. in comparison ‘than’: hac apārīk kanicakän āžarmīktar 422; Zarristan ke... zan-ē hac či hucihr- tar nest 259-19; hac tē veh 411; kū-š suk mas būt hac apdrik gāv 492°; more emphatically yuvattar (g. v.) hac hàn + huhömikän homtar 40°’. — 6. causative: hac hàn dušxvār sahist by this he was very much shocked 4?-?; hac hàn 1 devan sārēnišn 3774-25 : causal conj. : hac hàn cigon because 4511; hac han i with a nominal clause 48!. — 7. forming adverbs: hac pas, hac pes, hac be, hac apar (hacapar), hacadar; prepositions: pas hac, peš hac (= patiš hac 368), yuvat hac, bé hac; frame prepositions: hac. . . rād owing to 1525-26; hac .. . bérén 20%; hac . . . yuvatāk 76°. — Av. (1746 sqq.) hacé; OP haca; MPrth ^c, "Z; MPrs 'c, "z; Paz. ez (eži-ca); NP az.
3803:tuhikéh [twhykyh] emptiness, vacuity; the Vacuum in a cosmic sense 929. — From tuhik ‘empty’, from Av. (624) taoš-, pres. tusa-; MPrs twhyg; Paz. ihi (SGV);J.-Prs. twhy; NP tuhi, tihi, tahi; v. Nyberg, Geiger Vol. 1931, 214 sq., and against him Gershevitch and Mayrhofer, v. Mayrhofer, Osterr. Ak. d. Wiss., Anz. d. phil-hist. Kl. 1968, So. 1.p.15 (dubious hypotheses).
5389:täcaya-: täxtan tafnah-, tafnu-: täp (vi-)tak-: vitäxtan taka-: tak taxma-: tahm tanu-: tan tanu.pereda-: tanā- puhrak l taoš-, tusa-: tuhīkēh
6144:tw'n: tuvan tw’ngr: tuvan-karčh twhmg’n: töhmak twhyg: tuhikéh twxš-, twxšyn-: tuxšitan twx8’g: tuxšak twzyšn: töxtan
6826:Oihi: tuhikčh
7487:tuhi, tihi, tahi: tuhikéh tuxmah: töhmak Tužav: "Tucap uftadan, uft-: öpastan ummčd: ömöt ustuvän: ästavän
```


## [2026-10-15T02:45:20.572Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'side,? direction|direction, side|\\bsog\\b.*side|\\bsu\\b' PHD_mackenzie.txt | head; grep -n -i -E '^sog|^sōg|^soy' PHD_mackenzie.txt PHD.txt | head; grep -n -i -E '\\bsōk\\b|\\bsok\\b|\\bsōg\\b' NYB_vol2_glossary.txt | head"
}
```


## [2026-10-15T02:45:20.702Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4588,4600p PHD_mackenzie.txt; grep -n -E 'swk' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:45:21.249Z] TOOL RESULT

```
 spah [sp)h I N sipah] army.
    .....,bed [-pt l I N -bud] general, commander.
 spandan [spnd)n' I N sip....,] mustard seed.
 Spandarmad [spndrmt ' ] N isfandarmufJ] Holy Thought, the fourth
         Amahraspand, earth goddess; cal. 12th month; 5th day.
 spar [spl I M (spr, N sipar] shield.
 spar-,v. spurdan.
 spas [sp)s I M )s-, (sp)s, N sipas] service, gratitude, thanks.
spls dastan                                                      srOd
spls dlstan, '" han~ardan: thank, give thanks.
spas. dar [sp)sd)lj N sip,...,] grateful, thankful.
 ",ih: gratitude.
spasl-eAnas [sp)sfn)s] grateful.
1608:gih [g’s] l. place 6" etc, passim; pat ~ on the spot (?) 447; v. farrax*-gàh, kat- gah, stör-gäh. — 2. time 678, 8914-15; cg ~ at what time? 722. — Av. (517) gätu-, OP gādu-; Ps. g’sy ‘bed’, g’swky ‘throne’ ; MPrthPrs g’h, Arm lw. gah; Paz. NP gah.
3456:185k [swk'] side 321; 4 ~ 4 gētē the four cardinal points of the world (North etc.) 1201. — NP sū, sūy.
3459:— Another swk' to be read sik, v. this w.
3460:sökand [swknd] oath; ~ xtartan to swear an oath (pat by) 2118-23, 2225, 2322. — Ps. swkndy; MPrs swgnd; Paz. sawagand (SGV); NP saugand.
3461:Sokandar [swkndl] = Alaksandar, 113}. 1145. — Probably the Arab. Iskandar with elision of %- and inserting of an auxiliary vowel between s and k, cf Sikandar < Iskandar.
3462:Sošans [swš'ns, swkš'ns] the last of the three unborn sons of Zartuxst who will appear at the end of the world’s existence, “the last Saviour’’, presiding over the Resurrection of the dead and the Reno- vation (fraškart, g. v.) of the world: 12”. 649-12, 7115, 8820, 99—100, passim. 1022-26-27,
3559:Sugud [swkwd] Sogd, Sogdiana: this is the only possible reading 113! (swknd = sókand, q.v., gives no sense, still less dénkart, Cat. 3). — Av. (1582) Suyóa- (Gr Zöydor), Arab Sugd or Sugd; the coinci- dence with OP Suguda- must be fortui- tous, -kwd being a graphic attempt to keep the sounds y and 6 distinct. Sūi-gāv [swd TWR?’] n. pr. 47%. — BdA, p. 2294-5 swk-TWR^? [but BdJ 7717 sy’k TWR? = siyd(k)-gav; DkM 75° swdk’dy = süi-gài].— ‘Having horned cattle’: sit, Ps. swdy ‘horn’ < OP *guva- < "Oruva-, Av. (1647) .srii, srvà ‘nail, horn’, v. sruv. As to BdA swk-, v. next w.
3560:sik [swk'] horn 492. — < OP *euva-ka-, v. above. l
3696:(out of a set of items) = ‘sum total’, This cannot be the rendering of Syr swkyhwn = saukaihon ‘their branches’; in all probability it goes back to a variant (or corruption) swykhwn = suy- yakhon ‘their sum total’, from sayyek ‘to bring to an end, to limit, to contain, to comprise’.
```


### [2026-10-15T02:45:21.288Z] TOOL RESULT

```
3363:lkust [kwst ] side, direction; district.
3705: --ag [1zymk ' I N --a] half, side, direction.
4568:ssog [swh I N so(y)] side, direction.
PHD_mackenzie.txt:4570:sOgand [S'lvknd I M swgnd, N saugand] oath.
PHD_mackenzie.txt:4850:soy-, v. sustan.
PHD_mackenzie.txt:4851:soy [fwd IN ......] husband.
PHD_mackenzie.txt:10900:sogand
2478:mas [ms] great, big, also used as comp. (+ hac ‘than’), sup. masist [msst'] and mahist [mhst']: kū-š sok mas bit hac apürik gäv its hoofs were bigger than (those of) the other cows 49?-? (gl.); great of rank 38. 52%; ~ martin (pl. cas.
4245:to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
5324:saokā-: "sok
7417:sü: ?sOk
```


## [2026-10-15T02:45:25.566Z] TOOL CALL #16: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-15T02:45:25.578Z] TOOL RESULT

```


```


## [2026-10-15T02:45:28.009Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سو",
 "prompt": "Give the Persian section's etymology (for 'side, direction') verbatim, plus any Middle Persian/Proto-Iranian forms and cited sources."
}
```


## [2026-10-15T02:45:29.157Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تهی",
 "prompt": "Give the Persian etymology verbatim, with all older forms and PIE root cited."
}
```


## [2026-10-15T02:45:29.711Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سوق",
 "prompt": "Give the Arabic etymology of سُوق 'market' verbatim (Akkadian, Aramaic cognates/borrowing) and the Persian section if any."
}
```


## [2026-10-15T02:45:30.891Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tewh₂s-",
 "prompt": "Give the meaning and all descendants listed (Indo-Iranian, Avestan, Persian, Latin tesqua, etc.), verbatim."
}
```


### [2026-10-15T02:45:31.804Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:45:34.400Z] TOOL RESULT

```
# Persian Etymology for "سو" (Side/Direction)

**Etymology 1 (Direction/Side):**

The entry states: "From Middle Persian swk' (sōg, 'side, direction')."

No Proto-Iranian forms are explicitly cited in the etymology section. The document provides no additional sources beyond noting the Middle Persian origin.
```


### [2026-10-15T02:45:34.524Z] TOOL RESULT

```
# Persian Etymology of تهی

The word تهی (tuhī/tohi) derives from **Middle Persian twhyg** (tuhīg, "empty; vain, illusory; barren"), which comes from **Proto-Iranian \*tuŝyás**. This traces back to **Proto-Indo-Iranian \*tuŝćyás**, ultimately from **Proto-Indo-European \*tus-sḱ-yós**, rooted in **\*tews-** meaning "to be empty."

The entry notes cognation with Vedic Sanskrit तुच्छ्य (tucchyá).
```


### [2026-10-15T02:45:38.536Z] TOOL RESULT

```
# Etymology of سُوق (Market)

## Arabic Etymology

From Aramaic שׁוּקָא (šūqā'), which derived from Akkadian 𒋻 (sūqum, "street"). The Akkadian term itself came from 𒅆𒀀𒄣 (siāqum, "to become narrow").

## Persian Section

The Persian entry shows **سوق** (sawq/sowġ) borrowed from Arabic سَوْق (sawq), meaning "push" or "impelling." It includes the derived term **سوق دادن** (sawq dādan/sowġ dâdan).
```


## [2026-10-15T02:45:40.860Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tews-",
 "prompt": "Give the meaning and all descendants listed (Avestan, Persian, Latin tesqua, Sanskrit), verbatim."
}
```


## [2026-10-15T02:45:42.004Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/تو",
 "prompt": "Give the etymology of Persian تو meaning 'inside / fold, layer' (tu, tōy), verbatim, with older forms and sources."
}
```


## [2026-10-15T02:45:42.700Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/քով",
 "prompt": "Give the Old Armenian / Armenian etymology of քով (kʿov 'side') verbatim, with cited sources."
}
```


## [2026-10-15T02:45:43.231Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ته",
 "prompt": "Give Persian etymology of ته 'bottom' verbatim, with older forms."
}
```


### [2026-10-15T02:45:46.704Z] TOOL RESULT

```
Based on the Wiktionary entry, here is the Persian etymology of ته (tah, "bottom"):

The word is "inherited from Middle Persian [script needed] (th /⁠tah⁠/), possibly from Proto-Indo-European *tews- ('to be empty, drain'), and thus cognate with تهی (tohi, 'empty, hollow')."

The entry notes it may relate to Sanskrit तुच्छ्य (tucchya, "empty, vain") and suggests comparison with Persian تک (tak, "bottom").
```


### [2026-10-15T02:45:47.389Z] TOOL RESULT

```
# Etymology of քով (kʻov, 'side')

Based on the Wiktionary article, the etymology is unclear:

**Ačaṙean's assessment:** "considers 'side, flank' to be the original meaning and does not know the origin" (1979, Armenian Etymological Dictionary, vol. IV, p. 588b).

**Alternative hypothesis:** Ačaṙean's 1913 Provincial Dictionary "derives from _կող_ (koł)" (Armenian Provincial Dictionary, pp. 1121–1122).

The article notes that Middle Armenian քով may derive from Old Armenian քո (kʻo, "your, thy") in the instrumental singular, with semantic shift from "by your" → "near you" → "near." However, when քով means "side/flank," its origin remains undetermined according to the cited etymological sources.
```


### [2026-10-15T02:45:47.917Z] TOOL RESULT

```
# Proto-Indo-European Root *tews-

## Etymology 1: "Empty"

**Meaning:** "to be empty; to drain"

**Descendants:**
- **Avestan:** 𐬙𐬎𐬯𐬆𐬥 (tusən, 3.pl.inj)
- **Persian:** تهی (tohi, "empty")
- **Latin:** tesqua ("desert")
- **Sanskrit:** तुच्छ्य (tucchyá, "empty")

## Etymology 2: "Happy"

**Meaning:** "to be calm, content, happy"

**Descendants:**
- **Avestan:** 𐬙𐬀𐬊𐬱𐬀𐬌𐬌𐬈𐬙𐬌 (taošaiieti, 3.sg.pres.ind)
- **Sanskrit:** तुष्यति (túṣyati, "to be pleased") and तोषयति (toṣáyati, "to please")
- **Persian:** See Etymology 1 above (shared descendant)

The page notes these represent two distinct homonymic roots sharing the same form but different semantic origins.
```


### [2026-10-15T02:45:50.871Z] TOOL RESULT

```
# Etymology of Persian تو (tu/tōy) - "Inside/Fold"

Based on the Wiktionary entry, the etymologies for these senses are incomplete. Under **Etymology 2** and **Etymology 3**, the page explicitly states:

> "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

For **Etymology 2** (pool/puddle sense), no older forms or sources are provided.

For **Etymology 3** (fold/twist/turn sense), similarly no etymological information is given.

**Etymology 4** (the "inside" sense) is also marked as incomplete, with no documented older forms or historical sources cited.

The entry acknowledges these gaps rather than providing the detailed etymological chain you've requested. To obtain this information, contributors would need to consult the Etymology scriptorium or add to the dictionary themselves.
```


## [2026-10-15T02:45:54.035Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'tesqua' POK_03.txt POK_full.txt WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt LEW_1910.txt LAT.txt AHD_watkins1985.txt IEC.txt SYN.txt | head -20"
}
```


### [2026-10-15T02:45:54.702Z] TOOL RESULT

```
POK_03.txt:4659:Av.  Kaus.  taosayeiti  ,macht  los,  läßt  los'  (*touseiö),  Inchoativ  (*tus-skö) av.  tusdn  ,sie  verlieren  die  Fassung*,  baludi  tusag,  thuay  ,verlassen  werden' ; ai.  tucchd-j  tucchyd-  {^tus-sko-,  *tus-sk-io-)  ,leer,  öde,  nichtig',  afghan.  tas ,leer*;  lat.  tesqua  n.  PI.  »Einöden'  (^^tueskua)-^  ags.  dost  , Dünger',  ahd. iost  ds.  (,* Ausleerung');  aksl.  t^Hh  „-nsvög",  russ.  tö§cij  ,leer;  mager,  hager' usw.  (=  ai.  tucchyd').
SYN.txt:23607:Ir. terc, NIr. tearc ‘scarce’, used often in the sense of ‘little’ and ‘few’ (e.g. terca gl. ‘exigua’ MI. 48c30; ba terc for bith mnat ‘few women in the world’, Passions and Homilies 1.830, p. 64, etc., NIr. sometimes used for ‘few’ like beag above, perh. : Lat. tesca, tesqua ‘waste, un- cultivated regions’. Pedersen 1.81. Er- nout-M. 1035.
incoming/WLD/WLD_Bd1_pages.txt:67407:(Bthl. Wb. 797 f.), desgleichen die von lat. tesqua etwa „Einoden, diistere
incoming/WLD/WLD_Bd1_pages.txt:69928:                                 tesqua; letzteres aus nach *si-sku- „trocken“
POK_full.txt:86495:abandoned, forsaken, worthless', afghan. tas^ empty, bare, lacking'; Latin tesquau. PI. 
LAT.txt:64191:7,8, templum tescumque festo in sinistrum), tesca {tesqua),-o rum:
```


## [2026-10-15T02:45:57.870Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4650,4660p POK_03.txt | cut -c1-400; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"tesqua\")) print NR}' POK_03.txt; grep -n -E 'tuš|taoš' BRT.txt | head -15; grep -n -i -E 'empty' SYN.txt | head -5"
}
```


### [2026-10-15T02:45:58.640Z] TOOL RESULT

```
WP.  I  706ff,  WH.  II  650ff.,  112L,  714,  715f,  718f,  721,  Trautmann 3l4f.,  331  f.,  Vasmer  3,  149,  154,  160f.,  161f.;  Krähe  Sprache  u.  Vorzeit 65  ff.,  Mayrhofer  1,  490,  513  f.
^üif-  ;,Keim,  Same^  Nachkommenschaft^
Ai.  tüC'  f.  ^Kinder,  Nachkommenschaft^  (daneben  iüj-  f.  ds.  mit  volks- sprachlicher Erweichung  der  Tenuis);  tokdm  n.  ^Nachkommenschaft, Kinder';  tökman-  n.  ^junger  Halm,  Schößling',  av.  taoxman-  n.  ,Same, ^eim',  PI.  , Verwandtschaft',  apers.  taumä  f.  , Familie,  Same,  Keim*;  kho- tansak.  ttlman-  n.  _,Same',  np.  tum,  afghan.  töma  ,Same';  mhd.  diehter ^EnkeF
WP.  I  713,  Vasmer  3,  149,  Mayrhofer  508,  527;  vielleicht  zu  teu-k- ^schwellenS  oben  S.  1081.
jßup'  ;sich  niederkauern,  auch  um  sich  zu  verstecken'.
Gr.  ivrvTtag  Adv.,  II.  24,  163,  wenn  ,kauernd,  hockend'  bedeutend; vermutlich  aisl.  ßopta  f.  ,Ruderbank'  (,auf  der  gehockt  wird'),  ahd.  dofta f.,  mnd.  ducht  f.,  ags.  dofi  ds.  (wozu  aisl.  ßopti  m.  ,Mitruderer',  ags. ^edofta  , Genosse',  ahd.  gidufto  , Mitruderer,  Genosse*)  und  got.  piubjö jheimlich',  ßiubs  ,Dieb',  aisl.  pjöfr,  ags.  deof^  as.  thiof,  ahd
lit.  tüpiü,  tüpti  ,sich  hinhocken,  in  die  Knie  setzen',  tüpiü,  tupUi ,hocken,  in  den  Knien  sitzen',  lett.  tupt  , hockend
WP.  I  714.
teus-  ,leeren';  tus-sko-,  -sk-io-  ,leer'.
Av.  Kaus.  taosayeiti  ,macht  los,  läßt  los'  (*touseiö),  Inchoativ  (*tus-skö) av.  tusdn  ,sie  verlieren  die  Fassung*,  baludi  tusag,  thuay  ,verlassen  werden' ; ai.  tucchd-j  tucchyd-  {^tus-sko-,  *tus-sk-io-)  ,leer,  öde,  nichtig',  afghan.  tas ,leer*;  lat.  tesqua  n.  PI.  »Einöden'  (^^tueskua)-^  ags.  dost  , Dünger',  ahd. iost  ds.  (,* Ausleerung');  aksl.  t^Hh  „-nsv
WP.  I  714,  WH.  II  675,  Trautmann  333,  Vasmer  3,  130,  Mayrhofer  1, 508  f.
329
1376:Rum. fluviu, rt; pirtt Tr. ab(a); sruth; glais NIr.  abha; sruth; sruthan afon; ffrwd; nant, afonig Br. «ster (aven); gouer Between the large ‘river’ emptying into the sea and the tiny ‘brook’ there are infinite gradations, and often a wealth of words for these, which must be mostly ignored here. But generally Oe are distinctive words for ‘river’ and ‘brook’, and also one for ‘stream’, a generally for all forms of running te ee Mainly for those intermediate a : one the extremes of ‘river’ and : te for ‘brook’ may be diminutives Ose for ‘river’ river’. Conversely, a word
3670:2. Grk. xhpa, fem. of xfpos ‘bereft, empty’: xfros ‘want’, xwpis ‘apart’, xpos ‘(empty) place’, Skt. hd- ‘leave’, pass. hiyate ‘is left, deserted’, etc. Walde-P. 1.542 ff.
7062:Many of the verbs listed, and some of the nouns, belong to inherited groups re- flecting a variety of roots, in part, of the imitative or nursery type, which were apparently applied already in the IE pe- tiod to this bodily function. In the Gme. group and several of the other words the development is from ‘sepa- Tate’, whence ‘discharge from the body’. The countless euphemistic expressions are mostly ignored, as for example those meaning lit. ‘discharge, empty one’s self, Wythe ne sli doone’sneed’, andespecial- : a eta use of the simple verbs defecate shows eas me Hy au finned fe ecent Specialization of
7301:6. ChSl. neprazdina (cf. Jagié, Ent. stehungsgesch. 369), lit. ‘not empty’ epd, of neg. ne- and prazdint (see 13.22), So also Bulg. neprazdna.
8226:2. Lat. caecus (> It. cieco, Sp. ciego) : Ir. caech ‘one-eyed’, ‘squinting, blind’ (K. Meyer, Contrib. 297), NIr. caoch ‘blind, dim-eyed’ (‘blind’ by influence of Latin?), W. coeg ‘empty, foolish’ (coeg-
```


## [2026-10-15T02:46:02.349Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==957 || NR==958' SYN.txt | grep -n -i -E 'tuh|tus|empty|13\\.2' | head -20; grep -n -i -E 'tah[iī]|tuh[iī]|tihi' SYN.txt | head"
}
```


### [2026-10-15T02:46:02.824Z] TOOL RESULT

```
2:7. ChSI. kratiékd, ete., general Slavic : ChSI. sii-kratiti ‘shorten’, Russ.-ChS]. critu, crésti ‘cut’, fr. the root in Lat. cur- tus, OE sceort, etc. (above, 3, 5). Berne- ker 576f. Walde-P. 2.579.
5:Grk. — xAarts, ebpts Goth. braibs Lith. platus
7:Lat. latus Dan. bred, vid ChSl. Srokit
19:f. llyda ns Lith. platus, Lett. plats; spread ny. poragu-; Arm. lian.
24:4, Lat. latus (> Rum. lat), prob. fr. ‘ulatos (cf. stlatta, Festus) : ChSl. sttlati ‘spread out’, stelt, postelja ‘bed’. Walde- P, 2.643, Ernout-M. 527f. Walde-H. 1.172,
36:7. Lith. platus, Lett. plats, above, 1.
51:Lat. angustus (> It. angusto, Sp. an- gosto, Rum. tngust); Br. enk, cpds. Ir. cum-ung, Nir. cumhang, W. cyf-yng; Goth. aggwus, ON ongr, OF enge, ange, OHG angi, engi, MHG enge, Du., NHG eng; Lith. ankstas; ChSl. qztki, SCr. uzak, Boh. tzky, Pol. wazki, Russ. uzkij; Skt. anhu- (only in comp. anhtyas- and in cpd.) beside arihas- ‘fear, oppression’, Av. qzah- ‘need, op- pression’; Arm. anjuk.
```


## [2026-10-15T02:46:05.397Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'EMPTY|empty \\(adj|13\\.22' SYN.txt | head; grep -n -E 'tus-|tuščy|tuc' SYN.txt | head"
}
```


### [2026-10-15T02:46:06.133Z] TOOL RESULT

```
747:Grk. aidy ‘lifetime, age’ (:Lat. aevum, aetas, etc., 14.12) is used in the NT for ‘worldly life, this world’ in sense c, e.g. Mt. 13.22, Mk. 4.19 4 pépyuva (ak Hépiuvat) rod alvas robrov ‘the care(s) of this world’. Although this use itself was not extended to ‘world’ in other senses in Greek, it is important for the history of other words used to translate it.
770:ON vergld, OF weorold, OHG weralt, etc. general Gmc. except Gothic, a cpd. of wer ‘man’ (2.21) and a noun form of adjs. for ‘old’ (14.15), hence ‘age of man’. Thus it was equivalent to and followed Lat. saeculwm in its ecclesiasti- cal use (above, 2). For the early period this is the prevailing use, e.g. in the OF gospels, Mt. 12.32, 13.22 (Grk. aiwy, Vulgate saeculum). The further de- velopment was from this sense c to sense b and eventually to sense a, until the words in question became the common expressions for ‘world’ in all senses in all the Gmc. languages. NED s.v. world. Falk-Torp 1368.
774:ChSl. svétz ‘light’ (1.61) is used once in the gospels (Mt. 13.22) to translate Grk. diay (above, 2). The semantic de- velopment was from ‘light’ to the ‘realm of light, life’ (cf. the association between ‘light’ and ‘life’, e.g. Grk. doris pas dpa ‘whoever sees the light’ = ‘lives’), hence ‘world’ in sense c, later ‘world’ in all senses, as in the present Slavic lan- guages.
2094:‘fire’, etc. (Walde-P. 2.158f.) G. S. Lane, Language 13.22.
7301:6. ChSl. neprazdina (cf. Jagié, Ent. stehungsgesch. 369), lit. ‘not empty’ epd, of neg. ne- and prazdint (see 13.22), So also Bulg. neprazdna.
19329:ChSl. ottStetiti (Supr., etc.), SCr. ostetitt, derivs. of ChSl. tisteta, SCr. Steta ‘harm, injury’ : ChSl. ist? ‘empty’ (13.22). Leskien, Serbo-Croat. Gram. 55.
21861:3. Ir. bun, W. bon (both also ‘trunk’ or ‘stump’ of a tree), perh. orig. ‘blow’ (cf. W. bonclust ‘box on the ear’), fr. root *bhen- in Goth. banja ‘blow, wound’ (Walde-P. 2.149), with semantic devel- opment ‘blow’ > ‘club’ > ‘stock, trunk of a tree’ > ‘bottom’. Cf. Fr. bout ‘end’, orig. ‘blow’ (12.35). G.S. Lane, Lan- guage 13.22 f.
22830:But words that are used for ‘hollow’ only in this latter sense as NG xobguos (: Gri. xodpos ‘light, unsubstantial’, late also ‘empty’), and others listed under ‘empty’ (13.22), Pol. prézny, Russ. pustoj, Skt. ¢unya-, are not included in this list.
23362:13.22 Enpry
23731:13.22 EMPTY Grk. _xevds Goth. laus Lith. tudéias NG Gdeos, ddecavds ON tomr (lauss) Lett. tuk&s Lat. vacuus, indnis, vanus Dan. tom ChSl. tiger It. vuoto Sw. tom SCr.  prazan Fr. vide OE idel, @mlig, tom, Boh.  prdzdny Sp. vacto (ge)l@re Pol. —_ préany Rum. gol, desert ME _— em(p)ti, toom, idel, lere Russ. pustoj Tr. Jass, folam NE emply Skt. gilnya-, rikta-, tuecha- Nir.  folamh "Du. —_ledig Avy. iS a W. gwag OHG ital, lari, zuomig Br. goullo MHG _ itel, lzr(e)
1764:4. Goth. peihwd, prob. fr. *tenkwa- : ChSl. tqéa ‘shower’, Russ. tuca ‘dark cloud’, SCr. tuéa ‘hail’, Lith. tankus ‘thick’. Development through ‘thick cloud’, ‘thundercloud’ to ‘thunder’. Walde-P. 1.726 (with doubt). Feist 495,
3291:Chl. bratu-cedt, in Supr. ‘nephew and ‘cousin’, SCr. bratuced, fem. hea tuéeda ‘cousin’, epd. of bratié ‘brother (bratu gen.-loc. dual, Vondrak 1.675) and éedo ‘child’.
4035:Grk. rounhy, B puntos ON hirdir piemuo : yieg Dan. hyrde, kvegvogler Lett. gans NG room avns Sw. herde, boskapsherde ChSl. pastyrt, pastuchit Lat. ee OE hirde SCr. pastir, éoban, kravar, It. Dice berger, etc. ME herde etc. Yr. P lop vaquero, ma- NE herdsman; -herd Boh. pastyr, pastucha, kra- Sp. Das ee Du. herder, veehoeder vGk, ete. ‘oban (pistor) OHG  hirti Pol. —pastuch, pasterz
4036:a Fecha agatre MHG hirt(e), herter Russ. pastuch ae buachaill, aodhaire NHG shirt yee gopa-, pacupa-, etc. W. bugail v. vastar- Br. bugel
4060:6. ChSI. pastyr?, pastucht, fr. past; ‘pasture’ (3.16), and so the other Slavic words. Beside these and in more com- mon use in some of the Slavic languages is a series of specific terms derived from the names of the animals, as SCr. gove- dar, kravar, ovéar, svinjar, kozar ‘cattle-, cow-, shep-, swine-, goat-herd’, Boh. kravdk, ovéak, etc., like Fr. bouvier, va- cher, berger, etc.
4571:SCr. pastuh : ChSl. pastuchti ‘herds- man, shepherd’, (3.18), hence ‘stallion’ as protector of the stud(?).
4704:Pol. _—kura, kokosz kogut, pietuch kapton kura, kokosz _—ikurcze
4705:Russ. kura petuch kaplun kurica cyplenok
4763:ChSl. pételi, SCr. pijetao, Russ. petuch (> Pol. pietuch) ‘cock’ : ChSl. peti ‘sing’. Briickner 404.
9071:1, Grk. épr0s; generally called Oh Sir But the deriv. Tr Gea apapigne Von, fit, prepare’ 1s possible, euuher ei the general sense of prepared (Prellwitz), or through the literal sense as applied to the loaf ‘fitted’ in the bak- ing pot (xXtBavos). For dpros is, from Homer down, distinctively the ‘loaf’, pl. pro ‘loaves’, normally of wheat bread (in Hat. 2.92 of Egyptian loaves made from lotus-root).
```


## [2026-10-15T02:46:08.250Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23732,23760p SYN.txt | grep -n -i -E 'Av\\.|tuc|tus|Iran|NPers' | cut -c1-500"
}
```


### [2026-10-15T02:46:08.773Z] TOOL RESULT

```
6:2. Lat. vacuus : vacare ‘be empty, be free’, prob. fr. an extension of the root in Lat. vanus ‘empty, idle, vain’, Goth. wans, ON vanr ‘lacking’, Skt. ana-, Av. una- ‘insufficient’, NPers, vang, Arm. unayn ‘empty’. Walde-P. 1.108. Er- nout-M, 1068 f.
9:It. vuoto, Fr. vide, OF r. vuide (also OFr. voide > ME voide, NE void), fr. VLat. *vocitus, deriv. of VLat. vocuus, for Lat. vacwus (above). Cf. Lat. vocivus Plaut. and inser. vocatid = vacatid. Er- nout-M. 1069. REW 9429.
12:Rum. desert (= Fr. désert ‘desert’, etc.), fr. Lat. desertus ‘deserted, aban- doned’. REW 2592.
13:3. Ir. fass : Lat. vastus ‘waste, desert’, OHG wuosti, ete. ‘waste’, prob. fr. an extension of the root in Lat. vacwus, etc., above, 2. Walde-P. 1.219. Ernout-M. 1075 f.
28:5. Lith. tusias, Lett. tukSs, disputed, but prob. : ChSl. tigi (renders xevés), Skt. tuccha-, tucchya ‘empty, vain’, Av. tus- in caus. taogsaya- ‘let loose, free’, etc. Miihl.-Endz. 4.256 ff. Trautmann 333. Walde-P. 1.714.
29:6. ChSl. disti: Skt. tuccha-, ete. (above, 5).
```


## [2026-10-15T02:46:12.468Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *[0-9]+\\. +t(a|u|i)h' HRN.txt | head; grep -n -E 'taoš|taos-|tus-' BRT.txt | head -8; grep -n -E '\\[pdf page' BQT_v1_pages.txt | head -3"
}
```


### [2026-10-15T02:46:12.895Z] TOOL RESULT

```
3774:404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
21797:•  j.  yÖiÖTff ah-  :  yaltus-  Adj.,  PPf A. :  s. yat-.
```


## [2026-10-15T02:46:15.886Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3774,3790p HRN.txt; grep -n -E 'taos|taoa' BRT.txt | head -8; head -c 600 BQT_v1_pages.txt; grep -c $'\\f' BQT_v1_pages.txt"
}
```


### [2026-10-15T02:46:16.392Z] TOOL RESULT

```
404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
g. tohl,
aw. tusen^^ie entleeren sich' (Bartholomae, Studien
n, 52); phlv. tuhik 'leer; ai. tuöchyä-, skr. ^wccÄa- 'leer'.
bei. tnsag , n. fusay ausgehen, erlöschen, verlassen
*) Die Originalwörterbücher geben dem häufigen klnetoz (Stellen
in der Sahn. - Ausgabe I, p. XVIII) die Bedeutung 'Rache wünschend'
und fassen daher tö/ien als Verlangen, wünschen*.
Arm. toiz könnte übrigens entlehnt sein, vergl. Bartholomae
Studien II, 34.
') Vielleicht zu emendiren in törak', Justins Polemik (Bund. s. v.)
gegen de Lagarde, Ges. Abh. 53 Note 3 ist hinfällig, wenn sie sich
nur auf die Autorität der Handschriften stützt. Im Pehlevl wird gerade
der grösste Unsinn auch mit der grössten Consequenz von den Schreibern
immer wiederholt.
V
'j Belegt in FR und FJ durch einen Vers Qaträn^s (Metr.
2931:'b^eifeo,  verstehen  lernen':  ydäia  . . kliayeni  hutaosqm  . ,  yä  me  daüiqm  . , trmtat  (sd.)  däi  apica  aotät  Yt^.26.
3375:Satz:  aat  may^m  ava  kanöil  . .  paiti  dim abarBil  ''^a  ''imqm  vacS  framruyä  V.J7. S;  5.12,  27,  29;  — yö ..varasasca  *Aqm.- razayäte  . ,  '^5«  dim  *upa.taosayeiti  . .  raS- sayaca  (sd.)  V.  !■].  a.  5)  den  Nachsatz
5218:—  t^m  yaxata  kutaosa  vJsS 'vi  naoiaranqm   :
6305:•  j.  aäavasta-  n.  'Besitz,  Erwerb  des (höchsten)  Anrechts':^»  "^wä yäsämahi havauhum  't*m?a  haosravaahftn  Imru- mauii  Yt  10.33;  —  yüimäkim  yasnäica paimaUa  yal  am3sanam  spmtanqm  a/imä- ifM    hmHiauhäica    °täica  yal  taosyantqm
10060:mit  «r  1)  'herab-,  herunterkommen'; a)  absolut:  yat  lialna  (sd.)  nijasäni  ax»tn bri^rS  Yt,  15.28;  —  ya%a  nä  snaiüis asne  niymat»m"^  paiti  vaSnSit  .  .  "wie wenn  einer  eine  Waffe  nahe  (auf  sich) herunterkommen  sieht . .''  P.  21,  b)  mit Dat.  'zu  . ,':  fravasayü  . .  yä  ..  pisanithu taoa  nijas»ti  xsttvtwyd  ".  .  die  damals  zu den.W,  ..herabkamen"  Yt./y.37.  2) 'in einen  Zustand  (Akk.)  gelangen':  aet^a  .. näirika  .  .  apu'^rTmlsÄ.)  nijasät  usustana V.5.45;  Vd,  ;p.  3)  absolut  'zu  Ende kommen,  den  Abschluss  erreichen':  akra mäi  fra/asaiti  baxia  (sd.)  <^at  nijasaiü V,5.8"'.        [S.  noch  nijämaya-,  No.  i.]
10690:'yantake  Yt  10.  36;  —  i7fi  haSnayä  °ytitis (AP£)  Yt/o.S;  15.49 ■',  /')-54  (wo  "''-O- PPA.,  ans  *xn-is'ya;  den.  Praes.  31.  —  Vgl. ai.  krafi;.  n.  'Aas',  ksl.  Wfol  •Blut'.  —  Vgl. xrii:  —  Pü.  (nach  Dst.):  ifarak  x^äk,  erl.: T/i  iuiiil],);  Sü.!  /liifayili.  ~  ')  Mit  (  Yl.  /J. 33,  /o.  8j  /f,  45  sieht  xriiisy',  %  268.  iz  c —  »)  Gegen  S  /'iJ''  d  «-  —  3)  S.  in  xrüta-. j.  j«cö  F.  zj  b;  lies  xtaosyd.
11045:Aqscay.31.11;  32.11, !tJ.iS,45.'i;  —  ivaya ..dn-alai^a  asoonaita  Yt, /o.  2; — /.iuyan- taScä  västryäicä  Y.  2p,  6 ;  —  Aaväi  kämäica taosSua  YtJj,33;  —  yavas^a  yavaSätae'a Yt/j.So;  —  n>r»byasca  näiribyascä  Y.54. i;  —  niayal^a  upa.b»ntayal^a  N.  4S',  — tayäal^ä  Aazatghaicä  Y.  12.  2 ;  —  asnaatca xsafnaat^a  Yt  5, 1 5 ;  —  aiwtta^aca  spasi- 'ta^acaYtig.6;  —  %waAmaj  3'^riis^a mana»Aas/ä  Y.46.T, — glusca  vastraheca Yt/J.ioo; — apB  yat  snaliintylica  sras- äntySica  V, 6. 36  (s. dagegen  33 ;  Sp.564m.);
11797:•  j.  taoä-  V.  'leer,  los  sein'.  Praes. 14  (Inkoh.)  tuta-,  30  (Kaus.)  taosaya-.
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�766
```


## [2026-10-15T02:46:19.123Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11797,11812p BRT.txt | cut -c1-600; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BQT'].get('page_offset'))\""
}
```


### [2026-10-15T02:46:20.169Z] TOOL RESULT

```
•  j.  taoä-  V.  'leer,  los  sein'.  Praes. 14  (Inkoh.)  tuta-,  30  (Kaus.)  taosaya-.
i)  Inkofa.  'leer  sva.  schwach  werden, die  Fassung  verlieren':  yai  sulu/  (sd.) dayäj  äat  dasua  tusm  ". .  dann  verlieren die  D.  die  Fassung"  V.j,32.  2)  Kaus.
'los  machen  sva.  loslassen,  fallen  lassen in  — '  {paili  mit  Akk.):  yö  bansma  *taosa- yäti'-^  draos  (sd.)  vS  paiti  ss'inma  "wer einen  Ä-Stengel  fallen  lässt  in  .  ."  N.  loo. mit  dpa  (Kaus.)  'leer  sva.  schwach, (Ohren)  stumpf  machen':  narqm  mii:rö.- drujqm  .  .  apa  gaola  taosayeiti  Vt/0.48. mit  upa  Kaus.  dnwS.  2 :  yS  .  .  vars- sas^a  hqm.räsaydti  . .  srvaica  upa^wsr»- sinti  a'ka  d'tm  *upa.taosayäti  *utiähva  dim ralsayaca  (sd.)  V.  17.2.
mit  nt  '(ein  Gewand)  fallen  lassen,'  aus- ziehen' :  y3  aiwyärshayäite  kantssla  .  . pas^a  *aiwyäst»m  nitaosayäti  .  .  N.  197. Vgl,  afy.  lai  'leer',  PDw.  läiam  'ich  leere  aus'; ai.  tucckyä-  Adj.  'leer',  sbal.  tusag  'verlassen weiden',  np.  lik  'leer';  s.  dazu  Bthl.  IF.  8. 252,  Gor.  GIrPh.  i  b.  299.  —  Pü.  (zu  V.  f: tukik  bvtan,  (mV. /;>):  afar  löshüUm,  (zoN.): *nitdiimlan  (zT.  in  Aw.-Bnchsl.li  (zu  N.  Sj) erL. :  hai  Jröt  griflan,  —  ')  Hds.  taosy',  — ')  NA.  •yeinli;  s.  Var.
•  j.  taozya-  Adj.,  wohl  Bezeichnung  eines Volks:  upa  aoialiu  ranhayä  .  .  ake  pait- yänm  fräkirtntal  atsrü  matnyuS zyqm'a . . 'yäca'^  daiiiAusuiiwisiära  (si.)  V.J.  19.
PQ.:  fehlt;  Npü.:  an  samisiän  silambaiar  dar an  iahr  i  Hä,  —  ')  VgL  anairyäca  Jaiiilius.- aiwistära  V.  1.   17.
.  •  j.  tak-  V.  'laufen  (von  Menschen) ;  fliessen i(vora  Wasser  usw.)'.  Praes.  2  iaca-, I  24  tat.caya-'^,  30  (Kaus.)  tälfaya-;  Per£ 1  tat.k-.  —  Inf  'tacahi;  AbsoL  tacinitm. I  i)  'laufen':  taca^paoirfm  h^nm,frala atäi  tacsit . .  tacat  paoirfm  upäiÜ(sd)"eT soU  das  erste  /£  weit  laufen;  weiter  soll
dby  Google
6»S
tak-  mit  a
er  dann  laufen  .  .  er  soll  laufen,  bis den  ersten  (ihm  aufstossenden  Menschen)  j erreicht"  V.A'.ioo;  103;  —  yff  yrff/(sd.)  [ *tacS  {'SS.y  Aam^rvhaoa  .  .Vt.io.ji;  — ' nffij  ^usyaj  (sd.)  tacS  (NS.)  nsil  *msyqs Aog.60;  —  /acintä  (HP.)  ndit  apayänti ,  ,  barTntS  . .  vas)titö  YL  10. 20;  —  taca (aS.)  F./&  S.  noch  tacan-,  i)  ins-| besondere  von  Flüssigkeiten  'fliessen, strämen':  ka^a  xä  .  .  apqm  taisnti  nava "wann  werden  die  Wasserquellen  aufs  neue fliessen?"  Yt.  8.  5;  —  anham  raya  . .  gps Uieinti\t.i^.\\;  io,V.5.i9;  —  aptm  ta
mit  apa  i)  'fort-,  weglaufen,  sich  fort- machen' :  parqs  larstS  apatalai . .  kmsäspS Y.  5. 1 1 ;  —  tat  n^armS  apalacat  Yt.  ig. 56.  2)  'sich  verlaufen,  versickern',  vom Wasser:  yat  .  .  nyincö  (sd.)  apataan  V. 5.13.
mitiirä'>'herzufliessen':z'I'{^a«^«i&  apqm aiwi.tacaintqm  Vd.  ^
mit  anu  'mitüufen,  folgen':  yat  a^a  *yS apfmiayüi!!  sraoH  (sd.)   vä  anu.tahiti'^
N.7.
mit  aoi  und  frä  'herzufiiessen  zu  — ' (Akte):  yat  hii  aoi  fratacaitt  .  .  andvt Y.Ö5-4-
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-10-15T02:46:23.607Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:539 --image 2>&1 | head -80"
}
```


### [2026-10-15T02:46:24.058Z] TOOL RESULT

```
no scan of BQT covers printed page 539 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:26.665Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=760 && NR<=777 {print \"=== leaf \" NR-1; print substr($0,1,300)}' BQT_v1_pages.txt | grep -E '===|تهی|ته ' | head -40"
}
```


### [2026-10-15T02:46:27.354Z] TOOL RESULT

```
=== leaf 759
=== leaf 760
=== leaf 761
=== leaf 762
=== leaf 763
=== leaf 764
=== leaf 765
و بینی وامثالآن؟ - ولای و ته را نیز گونند
=== leaf 766
و بعربی نراب خوانند - و بمعنی‌تهی‌وخالی ۷ -
وبرهته و عربان هم هت .
=== leaf 767
وعربان - وتهی وخالی باشدا .<
پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
=== leaf 768
مخفف تهی است که خالی باشد .
سر کشته ومدهوش و بی‌فرار وشتاب زده همآحده
=== leaf 769
۲ - نام فرشته ایست ٩‏ که بر ستوران
=== leaf 770
=== leaf 771
=== leaf 772
=== leaf 773
=== leaf 774
=== leaf 775
گوته .
=== leaf 776
ثینه - مر وژن. کته ,آب دهن را
```


## [2026-10-15T02:46:30.535Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 766 767 768 769; do echo \"=== leaf $((n-1))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n -E 'تهی|ته |tuh|tah|tih|tuš|tus|leer|tucch|پهلوی|اوستا' | head -20; done"
}
```


### [2026-10-15T02:46:31.176Z] TOOL RESULT

```
=== leaf 765
6:و بینی وامثالآن؟ - ولای و ته را نیز گونند
=== leaf 766
6:و بعربی نراب خوانند - و بمعنی‌تهی‌وخالی ۷ -
7:وبرهته و عربان هم هت .
12:عدیل و نظیر نداشته باشد ۰ و تهمتن مر کب
19:است ۱ ععنی‌ننی که عدیل ونظیر نداشته باشد
23:ای زهر مردمی تهی ونهك
=== leaf 767
3:وعربان - وتهی وخالی باشدا .<
7:پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
21:بهیته - بر وزن همشه , نام شهری
25:تهی و تهاكث ۰ با ای فرشت و ها
27:برهنه و عربان - وتهی وخالی ۰
28:۴ در اوستا ۱۲۷۳2 31100[ ؛ جزو
=== leaf 768
2:مخفف تهی است که خالی باشد .
8:سر کشته ومدهوش و بی‌فرار وشتاب زده همآحده
15:آن» بمعئی سر گشته ومدهوش وییقرار وحیران
```


## [2026-10-15T02:46:33.895Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==767' BQT_v1_pages.txt | sed -n 20,60p; echo ======; awk 'BEGIN{RS=\"\\f\"} NR==766' BQT_v1_pages.txt | head -12"
}
```


### [2026-10-15T02:46:34.595Z] TOOL RESULT

```
Exit code 1
و بم‌نی سپهدار ولشکر کش وخداوند سیاه هم
هست - وبند کی و فرمان برداری کردنرا نیز
و
ای زهر مردمی تهی ونهك
مردمان تزد توچرا پابد(باد. دحخدا).
بوشکور بلخی, «لفت فری ۲۵۷*.
«اسشق ۶۰۵ :
کرا بخت وشمیشر ودینار باشد
وبالا وتن نهم ونسبت کیانی. دقیفی‌طوسی.
«لت فری۳۳۸».
هم همست در بهلوانی زبان
بمردی فزرن ز اژدهای دمان .
«یشنها ۲ ص۱۳۹ ».
۴ - تهمتن بخندید کورا بدید
٩‏ -کنون ای‌تهمتن تو در کار من
یکی تیغ تیز ازه‌یان بر کشد .
فردوسی طوسی. *لغت‌فرس ۳۳۸*.
نگه کن بآزار و کردار من.
فردوسی طوسی» گفتار رستم باسفندیار .
و کوبروارمفرب بقزوین وساوهطول آن ازهشرق‌بمغزب (غر قآ باد تا فدروژ کوه) ۲۹۰ وعرض‌ازشمال
بجنوب (ا زگردنة کندوان تا درباچهُ ق) *۱۲ کیلومتر و صساحت آن فربب ۳۱۰۰۰ کیلو متر
مربع است. شهرتهران پابئخت ابران دربن ابالت است. درفدیم نهران عکیاز فربه‌ه‌ای کوچكری
بوده» اصطخری وابن‌حوفل ومسمودی نام‌تهران را در کتب خود ذ کر کرده‌اند. «جقرافای سیاسی .
کیهان ۳۱۱- ۳۹۹. درسال ۱۲۱۰ آغا محمدخال قاجار آنرا باشخت ابران فرارداد . جمیت
نپران قوب ۱۰۰۰۰۰۰ نن است. راجم‌بوجه اشتفاق نهران وسور مختلف تلفظ و کتابت آن» رك:
بقبه درصفحةٌ ۰۳۹
(eval):1: ===== not found
```


## [2026-10-15T02:46:38.846Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==768' BQT_v1_pages.txt | grep -n -E 'اوستا|پهلوی|tuh|tah|tih|tus|ته ' ; awk 'BEGIN{RS=\"\\f\"} NR==768' BQT_v1_pages.txt | sed -n 1,40p"
}
```


### [2026-10-15T02:46:39.520Z] TOOL RESULT

```
7:پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
21:بهیته - بر وزن همشه , نام شهری
28:۴ در اوستا ۱۲۷۳2 31100[ ؛ جزو
تهمك - بر وزن لك لك , مصفر تهم
اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
وعربان - وتهی وخالی باشدا .<
بهمو درس - بنتح اول نامشخصی است
که او وا تهمورث دیو ند می خوانند؟ ت ورنفی
تهمیشه » بر وزن اندیشه . نام
پشته است در دارالم‌رز نزديك‌به بشه نارون؟ .
هو - منم اول و نانی » بروزنوهعنی
تفواست که آب دهن - وآب دهن انداخثن باشد
ویک اول مخمقف تسهواست ۹ وآن برنده‌است
خبیه بکيك. ایک نکوچکتراست از کیال
4 و بالا » بیمنی زیر و زبرباشد که
تحت و فوق است - و کنابه از اضطراب
و وف تپك رتپيك (ذیل: نهی).
وبیتراری هم ست وحصول مطلس دو سرامرد
باق فزکلاسک وا
ی - بکسر اول و نانی و سکون
تحتانی نام شپری و مدینه است* - و یمعنی
خالی۷ هم‌هست که در مقابل پراست۸ » و باین
معنی بفتح اول وضم اول هم گفنه‌اند .
بهیته - بر وزن همشه , نام شهری
است که فربدرن پوسنه و دام جر آنجا
می بوده . ۱
نهیگاه - ما ین شکم وپهلو را کویند.
تهی و تهاكث ۰ با ای فرشت و ها
بروزن زمی و فلكث» این‌لفت ازاتباع است بمعنی
برهنه و عربان - وتهی وخالی ۰
۴ در اوستا ۱۲۷۳2 31100[ ؛ جزو
سفق نمعدی يك فسم -ت.
زب
۵ سرله: نهو.
ا ورف *سشق ۰ ۰
۵ تهمورث - رك : نهمورسی .
شه ارصفحه ۵۳۸
نامهای شپرها ودبه‌های ابران. احمد
(بدون‌نام نوسن ») .مجلهٌکاوه دور جدید سالدوم شمارء۷ صی۱۱-۸؛ طهران.عسمد قزوشی.مجلةً
کاوه دور جدید. سال‌دوم شمار #ص۱۵-۱4؛ طهران با تهران؟ سمید نفیسی. محله آشده سال
دوم شمارء 4۰۷۰۱
```


## [2026-10-15T02:46:43.552Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==768' BQT_v1_pages.txt | sed -n 40,90p"
}
```


### [2026-10-15T02:46:43.996Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:47.633Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tuh[iī]k|tuhig|tusen|tusən|tuhī' BQT_v1.txt BQT_alt_v1.txt BQT_v1_pages.txt | head; grep -n -i -E 'tuh[iī]k|tuhīg' BQT_v2_pages.txt MON_part1.txt MON_part2.txt| head"
}
```


### [2026-10-15T02:46:48.236Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:50.879Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1182 --image 2>&1 | head -120"
}
```


### [2026-10-15T02:46:51.810Z] TOOL RESULT

```
no scan of BQT covers printed page 1182 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:54.871Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in $(seq 634 645); do awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n -E 'سوق|sôk|sōk|sōg|swk|^سو ' | sed \"s/^/leaf $n: /\" | head -8; done"
}
```


### [2026-10-15T02:46:56.216Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:59.158Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c $'\\f' BQT_v2_pages.txt; grep -n -E '\\[pdf page' BQT_v2_pages.txt | tail -3; grep -n -E 'سوق|چهارسو' BQT_v2_pages.txt | head; grep -n -E 'سوق|چهارسو' incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-15T02:46:59.874Z] TOOL RESULT

```
680
373:‫وکاف بروزن چارسوق » داسی راگوبند که بدان‬                                                             ‫آمدن باشد ‪.‬‬
7711:    ‫٭ چهارسو ‪ -‬فتح اول و دوم = چپارسوک = چارسوق » پپلوی ‪ 805‬هه‬
14742:  ‫خواندندی ‪.‬انست که معرب سوق الاهواز گفتند» «مجمل‌التواریخ والقصص ‪۲٩6‬‏ صحیح كلمة اخیر‬
38927:                       ‫‪.‬‬          ‫(‪kês‬‏ معربآن‌سوق در «چهارسوق» «اسشقس ‪06‬‬            ‫یر که ‪6۶‬‬
39335: ‫کشیده‪ .‬تاموزبر کیقبادبن فیروز پدر انوشیروان‬      ‫سوق ‪ - ۴‬بن‪ ,‬اول و سکون ثالی وفاء‬
39337: ‫سوق طالیه ‪ - ۷‬قومی‌اند ازحکای‬                                                            ‫رگاونند ‪.‬‬
39339: ‫سوقطون ‪ -‬بفتح الك و سکون‬                         ‫و اوانیی باد که از کل پخته باشند مانند کوزه‬
3979:_مخصوساً کشتی های شرامی را- بطرف «قصد مافران سوق دهد:
7741:‏سوق کوبند .
7762:بهلوی ۷۵6۵۲ ۰ بازار ‎Gb ۲۸۲ Sy‏ : سوق (عر)
31702:‎bein‏ قبلح۹آمده . یاقوت درمج‌البلدان درذ کر «اهواز» وید : « وللك کثرت بسوق‌الاهواز
```


## [2026-10-15T02:47:02.718Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38900,38935p BQT_v2_pages.txt | cut -c1-250; grep -n -E '\\[pdf page' BQT_v2_pages.txt | awk -F: '$1<38930' | tail -1; grep -n -E '\\[pdf page' BQT_v2_pages.txt | head -2"
}
```


### [2026-10-15T02:47:03.579Z] TOOL RESULT

```
               ‫را نز گفته‌اید ‪.‬‬   ‫و موح آب‬      ‫‪-‬‬
                                                     ‫ابت در ولات طوس و بچشمة سبزاشتهار دارد ‪.‬‬
‫یا بای فارسی بالف کشنده»‬    ‫سوار با‪-‬‬                 ‫کویند بزدجرد بن بهرام بن شاپور را که پادشاه‬
                                                     ‫چشمه اسبی برزمین‬     ‫کنار آن‬    ‫طالمی بوده در‬
 ‫بمعنی‌پاسواراست ککنهابه‌ازيبادة چست‌وچابك‬
                                          ‫باشث ‪.‬‬     ‫کوفت با لگدی بروی زد وبکشت ‪ -‬وبضم اول‬
                                                      ‫یمعنی جالب وطرف‌باشد ‪ - ۷‬و بمعنی‌مثل‌ومالند‬
‫سوار سیستان » کنابه راسزتم زال‬                      ‫هم هت ‪ -‬و مخفف سود باشد ‪ ۴‬که در مقابل ‪.‬‬
                                                     ‫زبان است ‪ -‬وروشنایی را بز کفته‌اند ‪ ۴‬که خد‬

‫سوار ك ب = باکاف بمعنی سواران‬                                  ‫تاریکی است ‪ -‬و بترکی آ براکوبند‪.‬‬

      ‫آب است که حباب ‪ -‬وموجةٌ آب باشد‪.‬‬               ‫بفتح اول بروزن جواب ‪ ,‬پلا‬       ‫سواب ‏‬
                                                     ‫هدن رچکدن آبراکونند ازچیزی همسو که‬
 ‫سوار ون = بفتح اول وشم رای‌قرشت‬
                                                                                 ‫ماست وامثال آن ‪۰‬‬
 ‫بروزن فلاطون » تخم خاکشی باشد وآ را بعربی‬
                           ‫بذرالخمخم خوانند‪*#.‬‬
‫بضم اول وثاای بالف کشیده‬      ‫سوا لك ه‬                 ‫پر کف زراکوشه موا ت وانکه مغر‬
                                                                            ‫خصوصاً ‪#.‬‬
 ‫و بکاف زده » زردبی باشد که برروی‌غلمزارشیند‬
                                                     ‫سواران آب‌وسوار گان !ب ه‌ِ‬
‫» و آن چوبی باشد که در وقت لماز کردن‬           ‫ات‬     ‫کنابه از حباب است آون‌قبه‌ای باشد ششه‌مالند‬

                                                                     ‫(‪ )۱‬چش ‪ :‬ودوم ‪.‬‬


                       ‫‪.‬‬          ‫(‪kês‬‏ معربآن‌سوق در «چهارسوق» «اسشقس ‪06‬‬            ‫یر که ‪6۶‬‬
  ‫طبری ‪ûs‬‏ (روشنی) «ساب‌طری ‪١٤٤۰‬‏ > گیلکی ‪ûs‬‏‬              ‫‪۴‬‬             ‫رك‪ :‬سود ‪.‬‬   ‫‪۳‬‬   ‫‪۳‬‬

  ‫‪1‬ر که‪:‬یاسوار‪.‬‬     ‫رك‪ :‬سوارك آب ‪.‬‬         ‫©‬    ‫‪( - ۴‬عر) لفة بمعنی تاحية بز رکه ‪.‬‬    ‫( زوشنایی) ‪۰‬‬

  ‫] کردی‬
       ‫[رك ‪ :‬اسواره اسوبار ‪,‬‬      ‫کزی) و درقدم ‪"۲۷۵2‬‬       ‫‏‪ H‬سو ار‪-‬بفتح اول (درلهحة مر‬

  ‫‪ , 7‬افغانى ‪ ۲6۳5‬و ‪ . ۲۵۷3‬بلوچی ‪ « ۲2۷2۹‬اسذق ‪ » ۹4۲۷‬کلمة فارسی ‪= ۲0۳15‬‬
```


## [2026-10-15T02:47:11.101Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -38927 BQT_v2_pages.txt | grep -c $'\\f'; sed -n 7705,7715p BQT_v2_pages.txt | cut -c1-200; head -7711 BQT_v2_pages.txt | grep -c $'\\f'; sed -n 39330,39340p BQT_v2_pages.txt | cut -c1-200; head -39335 BQT_v2_pages.txt | grep -c $'\\f'"
}
```


### [2026-10-15T02:47:11.600Z] TOOL RESULT

```
644
                                                                   ‫‪ ¥‬چهارپایه ‏ رك ‪ :‬چاریابه ‪.‬‬
  ‫‪ › > ۱۳۱:۲‬اوسا‬    ‫ما‬           ‫‪«۱‬‬            ‫*‪ #‬چهارده ‪-‬بفتح اول و دوم وپنجم > بهلوی ‪7‬‬
   ‫استی ‪. 4 »5680۲680۳1‬‬               ‫هندی باستانی ‪« 4920۳0020‬اسفا‪۱:۲‬ص> ‪۱۱‬‬                       ‫‪2‬‬
                 ‫عدد اصلی‌میان سیزده و بانزده‪ ,‬ده سلاو چهار ‪.‬‬                 ‫کگلکی ‪«2‬‬            ‫است ‪۹‬‬
  ‫‪ #‬چهار دهم ‪ -‬بفتح اول ودوم و پنجم وضم ششم ‪ .‬بهلوی حناحا‪2‬تقطی › از‪:‬‬
                             ‫چهارده ‪٣‬‏ ام ) یوند عدد ) ؛ عدد ترئیبی چهارده ‪ ۰‬درمرتبةٌ چهارده ‪.‬‬
    ‫٭ چهارسو ‪ -‬فتح اول و دوم = چپارسوک = چارسوق » پپلوی ‪ 805‬هه‬
   ‫(در ترکی ل‪ ( 5۴3‬دارای چهارجانب )‪ .‬فس ‪ :‬لانیتی ‪ ۰ )0۳2۷1۷170200‬چهارطرف ‪ ۰‬چهار‬
   ‫جانب_چپار راه ‪* :‬اهل البصرة اذاالنقت اربع طرق «سمونپامرسة» وسمنها اهللكوفه‪:‬الجهارسوه‬
   ‫و الجهارسو بالفارسية » « البيان والتبيين جاحظ طبع حسن الندوبى ج اص ‪ > ۳۳‬همین عبارت‬
  ‫در طبع حن افندی الفاکهانی ص ‪ « ۰۱‬جپارسوك» آمده واین اصح است‪ -‬اکنون میدالی‌را که‬
131
 ‫دو کچه » ریز هرچیز راگوبند ‪ -‬وبه‌نیشوشة‬          ‫وین قطه دار »‬
                                                              ‫سوغه ‪ -‬بنتح اول غ‬
                          ‫زر وسیم همآ هده است‪.‬‬
                                                   ‫مرسومی باشد‪ .‬کهمپاهیان از علوفه وماهیانخود‬
 ‫قرا‪ -‬بقتح اك ورای بی‌طه‌بالف‬       ‫سو‬                                        ‫بنوبند گان دهند ‪.‬‬
 ‫کشیده‪ .‬تاموزبر کیقبادبن فیروز پدر انوشیروان‬      ‫سوق ‪ - ۴‬بن‪ ,‬اول و سکون ثالی وفاء‬
                                          ‫و‬       ‫بلفت بونانی بمعنی حکمت باشد سووفی حکیم‬
 ‫سوق طالیه ‪ - ۷‬قومی‌اند ازحکای‬                                                            ‫رگاونند ‪.‬‬
                                         ‫باطل ‪.‬‬    ‫مودار » ظروف‬    ‫سوفار ‪ ۴‬د بر وزن‬
 ‫سوقطون ‪ -‬بفتح الك و سکون‬                         ‫و اوانیی باد که از کل پخته باشند مانند کوزه‬
‫زده »‬     ‫نوون‬
651
```


## [2026-10-15T02:47:16.191Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/سو",
 "prompt": "Quote verbatim the Mo'in entry/entries for سو (sū, side/direction) including bracketed origin tags like [په.]."
}
```


## [2026-10-15T02:47:17.485Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/تو",
 "prompt": "Quote verbatim the Mo'in entries for تو (tū) meaning fold/layer/inside (تو ۲ etc.), including bracketed origin tags."
}
```


## [2026-10-15T02:47:17.575Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/سوق",
 "prompt": "Quote verbatim the Mo'in entries for سوق (sūq, market) and سوقی, including origin tags like [ع.]."
}
```


### [2026-10-15T02:47:20.981Z] TOOL RESULT

```
I appreciate your request, but I need to be transparent: the webpage content provided doesn't include the detailed entries for تو (2), تو (3), etc. that you're asking me to quote verbatim. 

The page shows links to these alternative meanings—"[تو (2)](/moein/%D8%AA%D9%88-2)" and similar—but the actual dictionary definitions for those entries aren't displayed in the content you've shared. To provide the Mo'in dictionary entries with their origin tags for the fold/layer/inside meanings, I would need access to those actual entry pages, which aren't included here.

If you can provide the full text of those specific entries, I'd be happy to quote them while respecting your 125-character limit and other guidelines.
```


### [2026-10-15T02:47:21.467Z] TOOL RESULT

```
Based on the Mo'in dictionary entry shown in the webpage, here is the verbatim quote:

"(اِ.) طرز، روش ."

This entry defines "سو" (sū) as meaning "manner" or "method" (طرز، روش). The bracketed tag "(اِ.)" indicates the grammatical classification, though the full origin notation you referenced isn't visible in this particular entry on the displayed page.
```


### [2026-10-15T02:47:22.116Z] TOOL RESULT

```
# Mo'in Dictionary Entry for سوق

Based on the webpage content provided, here is the verbatim Mo'in entry:

**سوق**
"[ ع . ] (اِ.) بازار؛ ج . اسواق ."

This entry indicates the word is of Arabic origin [ع.], pronounced as shown, and means "market" (بازار) with the plural form اسواق.

The page also references another entry **سوق (2)**, suggesting there are multiple definitions, though the additional meaning is not displayed in the provided content.
```


## [2026-10-15T02:47:24.809Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/تو-2",
 "prompt": "Quote verbatim the Mo'in entry text including origin tags."
}
```


## [2026-10-15T02:47:25.279Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/سو-2",
 "prompt": "Quote verbatim the Mo'in entry text including origin tags."
}
```


## [2026-10-15T02:47:25.450Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/تهی",
 "prompt": "Quote verbatim the Mo'in entry text including origin tags."
}
```


### [2026-10-15T02:47:27.449Z] TOOL RESULT

```
# Entry from Mo'in Dictionary

The Mo'in (Moein) dictionary entry for "تهی" (tahī) is:

**"(تُ) (ص .) خالی"**

This translates to: The word is marked as an adjective (ص .) with the meaning "empty" or "vacant" (خالی).
```


### [2026-10-15T02:47:28.434Z] TOOL RESULT

```
# Definition of "سو" from Mo'in Dictionary

According to the Mo'in Dictionary entry provided, the word "سو" is defined as:

**"[ تر. ] (اِ.) آب"**

This indicates the term is a Turkish loanword (تر. = Turkish) marked as a noun (اِ.), with the meaning **"water"** (آب).

The page also notes there are multiple other meanings of this word (referenced as سو (1), سو (3), and سو (4)), which would be found in different entries within the same dictionary.
```


### [2026-10-15T02:47:30.324Z] TOOL RESULT

```
# Entry for "تو" from Mo'in Dictionary

According to the Mo'in Dictionary (Entesharat-e Mo'in), the entry for "تو" includes:

**Definition:** "لب رفتن ( ~. رَ تَ) (مص ل .) مأیوس شدن ، دمق شدن"

This translates to losing hope or becoming discouraged/despondent.

The page also indicates this word has multiple meanings, with references to entries labeled تو (1) through تو (6), and notes that the term appears in various Persian dialects and translation dictionaries (including Persian-to-Arabic, Persian-to-English, and Persian-to-Turkish).
```


## [2026-10-15T02:47:35.217Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\s*[0-9]+\\.\\s*(tihi|tuhi|tahi|sü|sū|su|tu|tö|tü)\\b' HUB.txt | head; grep -n -E 'tuhik|tuhīk|tihī|tuhī' HUB.txt | head -5; grep -n -E 'TOHI|TAHI|TOHĪ|TUHI' incoming/ARY/ARY_latin_index_pages.txt | head -5; grep -n -E 'تهی' incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-10-15T02:47:35.594Z] TOOL RESULT

```
4882:zd. apu&ra- =: *apw^ra-; tihf 'leer = pSz. tihf, phi. tuhik
5690:(OLD CHURCH SLAVIC) 48 5%! SHTIV, SHTIVAIT, TUHIVATI
5985:TUSHCHY RUSSIAN) 9s TUHIK, TIHIK, TUHIG
1024:جهیزبه عروس را تهیه کند. معمولاً مذا کرات وابسته به زناشویی طولانی بود.
3045:تخاری 8 (8 7087۸7/4(۷): ۳0168 ,۳۸04 آلمانی کهن (انمانتهی :8700
6098:۸ تهی
8092:ایرلندی کهن (#ذلقا ۵م): ۸7823805 0 (#تهیم :قاط
9693:زوت» زوتر زاوتر (به چم "موبد زرتشتی مامور تهیه کردن آب مقدس") / ۳۲۹
```


## [2026-10-15T02:47:38.928Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4878,4884p HUB.txt; sed -n 5980,5988p incoming/ARY/ARY_latin_index_pages.txt; head -5985 incoming/ARY/ARY_latin_index_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1; sed -n 6090,6110p incoming/ARY/ARY_pages.txt; head -6098 incoming/ARY/ARY_pages.txt | grep -o '\\[pdf page [0-9]*\\]' | tail -1"
}
```


### [2026-10-15T02:47:39.453Z] TOOL RESULT

```
paz. humdna u. s. w. (oben p. 106) ist wohl humdnd zu
sprechen, wie tuxsd fiir taxsd (oben p. 47) = paz. tuxsa,
phi. tuxsdk. Vgl. auch angabin (A. M.) Honig' = angubln.
§ 24. Inl. u wird zu i in : dbistan *schwanger = phi. apus,
zd. apu&ra- =: *apw^ra-; tihf 'leer = pSz. tihf, phi. tuhik
Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
'Sohn* = pusar (nach Horn durch pidar beeinflusst) ^) ; misk
TOM DANISH) S,lail> HAVESTAN) gle \
TOM (SWEDISH) (5.8 yo TAOSH, TAOSHAEITI
TOM (NORWEGIAN) «533,3 (OLD PERSIAN) gles go 34
(OLD CHURCH SLAVIC) oS 59% TUTHYA, TUSSYA
TOSHTI PAHLAVI) 5 344
TUSHCHY RUSSIAN) 9s TUHIK, TIHIK, TUHIG
TUSHCHIAS —(LITHUANIAN) 53 TASH HAFGHAND) (24) gi}
TUSEM SANSKRIT) oy Sle
‘REFERENCES tenth | *  TESCA ARMENIAN) |)
[pdf page 207]
پهلوی (4۲1اللهه): 7100 یونانی (07882): ۰ 78833085 ,7۸2301
,7۸806 بکلف70 بکقف 78 لاتین (4710): ۰ 73۲5580 ,180758
ارستی (ع083877): 7۲ فرانسه کهن (لل0/0ق۳2 صا0):
کر دی (8701577(). 7102 7 ۲8278
بلرچی (اتاه‌تاننههق: 65شا70 بعشا70 اسپانیایی (82۸7197): رید ابا
سانسکریت (84(8777): 7۸ ایتالیایی (ماسه1): زین ان ابا
[pdf page 207]
1
۸ تهی
پرتغالی (ظ0700188): زد دنا
گوتیکه (007710): 75 پسگشت‌ها 5
ابسلندی کهن (504(0701۵2۷ صا0): 271070 9 . ۹ 80070
71/۸ 11124 : مد ها
انگلیسی (6۸01/34)(از فرانسه‌ی کهن) 40 جتما‌دن 1
7 ومو 1 :0/105
لینرانی (/777۸/4لر): 7۸۸8 635 درا
آلبانی (0ا#لمقلم: 721 برهان قاطع + ۲ و ۵۳۵
یادداشت:
۱- چم این واژه در زبان اوستایی: بچه,
۲- چم این واژه در زبان پهلوی و زبان بلوچی؛ شغال.
۳ این واژه در زبان‌های رومانس و انگلیسی به چم اتازه" و "لطیف" و "تورسیده" هم بکار می‌رود.
[pdf page 207]
```


## [2026-10-15T02:47:47.368Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; \npython3 $F 'https://en.wiktionary.org/wiki/سو' --note 'page 508, root Teub: Persian sū < MP swk sōg side, direction' ;\npython3 $F 'https://en.wiktionary.org/wiki/تهی' --note 'page 508, root Teus: Persian tohi < MP tuhīg < PIr *tušyás < PIE *tews-' ;\npython3 $F 'https://en.wiktionary.org/wiki/سوق' --note 'page 508, root Teub: Arabic sūq < Aramaic šūqā < Akkadian sūqum street' ;\npython3 $F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tews-' --note 'page 508, root Teus: PIE *tews- empty; Av. tusən, Latin tesqua' ;\npython3 $F 'https://en.wiktionary.org/wiki/تو' --note 'page 508, root Teub: Persian tu fold/inside, etymology missing' ;\npython3 $F 'https://en.wiktionary.org/wiki/քով' --note 'page 508, root Teub: Armenian kʿov side, origin unknown (Ačaṙean)' ;\npython3 $F 'https://en.wiktionary.org/wiki/ته' --note 'page 508, root Teus: Persian tah bottom, possibly from *tews-' ;\npython3 $F 'https://vajehyab.com/moein/سوق' --note 'page 508, root Teub: Moin sūq [ع.] bazaar, pl. aswāq' 2>&1 | tail -20"
}
```


### [2026-10-15T02:47:49.094Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/083ee293ca2a88d7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a94193e5d8023a2b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0e82fc0a8ea57ce9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/251de82bdaa71c04.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8add2845f7795843.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8648377177478893.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/71d529bea809fa13.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/406da16bda2fa28b.txt
```


## [2026-10-15T02:47:52.728Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E 'Etymology|Middle Persian|inside|fold' 8add2845f7795843.txt | head -30; grep -n -i -E 'Ačaṙean|side|Iranian|Persian' 8648377177478893.txt | head -15; grep -n -i 'Middle Persian\\|Etymology' 71d529bea809fa13.txt | head"
}
```


### [2026-10-15T02:47:53.289Z] TOOL RESULT

```
62: Etymology 
88: Etymology 1 
103: Etymology 2 
139: Etymology 
162: Etymology 1 
183: Etymology 2 
189: Etymology 3 
195: Etymology 4 
224: Etymology 
255: Etymology 
275: Etymology 1 
293: Etymology 2 
390: Etymology
650: Etymology 1
688: Etymology 2
744: Etymology
797: Etymology 1
800: From Middle Persian 𐭫𐭪 ( LK /⁠tō⁠/ , “ you, thou ” ) , from Old Persian (compare 𐎬𐎺𐎶 ( tuvam ) ), from Proto-Iranian *tuHám (compare Northern Kurdish tu , Pashto ته ( tə ) , Avestan 𐬙𐬏𐬨 ( tūm ) ), from Proto-Indo-Iranian *tuHám , from Proto-Indo-European *túh₂ .
1099: Etymology 2
1102: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
1111: Etymology 3
1114: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
1121: fold , twist , turn 
1123: Etymology 4
1126: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
1138: ( Iran or rare ) inside ; interior 
1147: ( Iran or rare ) in ; inside 
1161: ( Iran or rare ) inside 
1179: Etymology
1182: (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
14: move to sidebar 
51: move to sidebar 
129: move to sidebar 
160: move to sidebar 
214: side , flank 
241: Ačaṙean, Hračʻeay ( 1979 ), “ քով ”, in Hayerēn armatakan baṙaran [ Armenian Etymological Dictionary ] (in Armenian), 2nd edition, a reprint of the original 1926–1935 seven-volume edition, volume IV, Yerevan: University Press, page 588b considers "side, flank" to be the original meaning and does not know the origin
243: Ačaṙean, Hračʻeay ( 1913 ), “ քով ”, in Hayerēn gawaṙakan baṙaran [ Armenian Provincial Dictionary ] (Ēminean azgagrakan žoġovacu; 9) (in Armenian), Tiflis: Lazarev Institute of Oriental Languages, pages 1121–1122 derives from կող ( koł ) 
62: Etymology 1 
71: Etymology 2 
77: Etymology 3 
83: Etymology 4 
102: Etymology 
116: Etymology 1 
125: Etymology 2 
142: Etymology 
165: Etymology 
249: Etymology 1
```


## [2026-10-15T02:47:57.964Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"tapu[sš]|taobh\" POK_full.txt POK_0*.txt WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt AHD_watkins1985.txt | head; grep -n -E \"^ *[0-9]+\\. *t(ü|ū|ö|ō|u)[iy]? .*(Falte|Inner|innen)\" HRN.txt | head; grep -n -E \"'Falte|Falte'\" HRN.txt | head"
}
```


### [2026-10-15T02:47:58.398Z] TOOL RESULT

```
POK_full.txt:67659:Maybe Tadzik PUST, TAXTAPUST, Lahnda PICCHE, Nepali PITH, Kashmiri PYUTHU, 
9927:455. Hierher auch np. cm 'Falte', vergl. däm haz cTden
9928:'das Netz zusammenfalten' (Häfiz 4, 2), azeng 'Falte'
```


## [2026-10-15T02:48:16.140Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '\\bs[uū]q\\b|aswaq|aswāq' FVQ.txt AFM.txt AFA.txt LKT.txt PLA_*.txt incoming/PLA/PLA_pages.txt 2>/dev/null | head; grep -n -i -E '^souk|^suq|^sukh' KLN_1971.txt | head"
}
```


### [2026-10-15T02:48:16.473Z] TOOL RESULT

```
(eval):1: no matches found: PLA_*.txt
158353:sukh , compounded of nain , ‘eye’, and sukh, 
236045:souken , ‘to suck’. See suck and agential suff. -er. 
236066:suqldt, fr. Pers. saqallat , a secondary form of
```


## [2026-10-15T02:48:19.729Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 's[uū]q\\b|sūq|suq,|šūq|shuq' FVQ.txt AFA.txt LKT.txt incoming/PLA/PLA_pages.txt AFM.txt | head -15; grep -n -E 'سوق' AFM.txt TAD.txt ARB_mo3rb.txt | head"
}
```


### [2026-10-15T02:48:20.189Z] TOOL RESULT

```
FVQ.txt:11479:(Suq). 
AFA.txt:6388:Syrien Besitzungen , so Abu SuQän , der in der Heidenzeit
AFM.txt:635:(البازّار) فارسي مخض وهو السوق ومنة الكردي بأحار 
AFM.txt:4513:1 ( الصَيْطر والضصّوطر ) من يدخل السوق بلا راس مال فيحتال ܐ 15 
ARB_mo3rb.txt:2182:ألى عند 5 قال : “لمعت أب بس يقول : من زعم أن قَْ القرآن لسا ّ سوق العرسة 
ARB_mo3rb.txt:6782:و نا خامية هو صدوة 2 # اححسوق 4 ة شعهسا ارال 52 
ARB_mo3rb.txt:9322:« والحد والحدة - ساحل البجر مك » وجدة اهم موطع قرب من ا مسوق مله 6ه 
ARB_mo3rb.txt:10332:ي2 ذاء 6 52 له 1 تلوق ابذووالك ضير > فبسبى له ] ذلك" 6 وطدسوق قم 
ARB_mo3rb.txt:13496:إن عرى عؤور حزايه * كرطئة الى فسوق الرابهه 
ARB_mo3rb.txt:17215:اراد تار عمقل : شي ذاك لمان فى كثرة | أوحوش مَك السوق 0 
ARB_mo3rb.txt:17297:“”غسوق و””غسيّات و””غدق بورد 4 فأس 
ARB_mo3rb.txt:17325:فى ذلكعندى بالصواب قول من قال : هى مايمبل منْ صديدهم لأن ذلك هو الأغلب من موى النسوق» ٠‏
```


## [2026-10-15T02:48:22.417Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11470,11485p FVQ.txt; sed -n 630,637p AFM.txt"
}
```


### [2026-10-15T02:48:22.929Z] TOOL RESULT

```
3 Cf. also Baid. and Bagh. and LA, ix, 199. 

* Barth, Etymol. Stud, 14, and ZATW, xxxiii, 306, wants to make it mean flood, 
but see Horovitz, KU, 13. 



FOREIGN VOCABULARY OF THE QUR*AN 183 

(Suq). 

xxv, 8, 22. 

A street. fr 

It occurs only in the plu. cJ'^f*-' referring to the streets of the 
0 ( البأدنج ) عق بأدنج وهو الحوز المددي. 

# ܐ ضرت من الصقور وهو :اسشد > ارح شكيرا وأضتها خلا 
ܨ ܬܨ 80 ܠ للصند .27 باز ܫ طوغان 

(البازّار) فارسي مخض وهو السوق ومنة الكردي بأحار 

( المأزركان) ܨ ¢ ܐܨ 0207 السرق
```


## [2026-10-15T02:48:24.963Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11485,11505p FVQ.txt"
}
```


### [2026-10-15T02:48:25.595Z] TOOL RESULT

```
It occurs only in the plu. cJ'^f*-' referring to the streets of the 
city. 

In later Arabic Oj~> normally means a market place, but in the 

Qur'an it is used as the p*W of the O.T. and the Targums for street, 
in contradistinction to the Talmudic meaning of broad place or market. 1 



The philologers derive it from \J\* to drive along (LA, xii, 33), but 

Fraenkel, Fremdw, 187, is doubtless right in thinking that it is a word 
taken over by the Arabs from more settled peoples. 2 The Aram. 
Xp127 ; Syr. |oo* commonly mean 55oy, as well as ayopa, 
and in a Palmyrene inscription (De VogiiS, xv, 5) we read 3T Nlffl 
p127, showing that the word was known in N. Arabia. 

From some early Mesopotamian source 3 the word passed into 
Iranian, for we find the Phlv. ideogram **})*{$ shoka meaning market, 
public square, or forum, whence comes the Judaeo-Persian *^10. 4
```


## [2026-10-15T02:48:30.038Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /^[^0-9]*187[^0-9]/ || $0 ~ /\\n *187 *\\n/) print NR}' AFA.txt | head; grep -n -E 'Strasse|Markt' AFA.txt | head"
}
```


### [2026-10-15T02:48:30.428Z] TOOL RESULT

```
218
335
339
350
351
360
3541:S) XXm# «Strasse** dürfte man kaom za ) ^^ a. stellen; eher könnte t'y^
6369:Markt von TJkaz mit einer Karawane, die der oberste
6656:Es bedeutet im Arabischen zunächst den Marktplatz Be^
6657:47 paenult., dann auch den Markt selbst , den Handel BeVrl
9837:aus dem Begriffe der »Strasse*' der Begriff des »Pflasters**
```


## [2026-10-15T02:48:32.496Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6645,6665p AFA.txt"
}
```


### [2026-10-15T02:48:32.960Z] TOOL RESULT

```
arabische Wort in das Syrische gewandert ist.
Von Verkaufsstellen haben zwei aramäische Namen. Zu-
nächst ist das alte Wort {Jjy^ wahrscheinlich nicht arabischer
Herkunft, sondern erst aus Uo^ Kpl2^ Palmyr. py^y De Vogu^
Stfrie Centrale Inscr. XV, 5 entlehnt. Im Ambischen hat ea keine
rechte Ableitung , da \^y^ erst denominativ ron ^y^ ge-
bildet ist ; es ist Tielleicht auch durch das doppelte Geschlecht
verdächtig, jedesfalls aber gehört es zu den Culturwörtem ,
deren Entlehnung am ehesten vorausgesetzt werden kann,
da Märkte in diesem Sinne den ältesten Arabern gefehlt
haben werden. Auch fehlt das Wort dem Äthiopischen.
Es bedeutet im Arabischen zunächst den Marktplatz Be^
47 paenult., dann auch den Markt selbst , den Handel BeVrl
508 , 0; davon abgeleitet ist iS^^» ^amäsa 534. Comment.,
Jalxübi (Houtsma) I. 313. Dagegen ist Si^«« »Pobel" ganz188
dayoQ zu trenuea; das gehört wirklich, wie Gawällki
Morgenl. Forsch. 118, 4 richtig bemerkt, zu ,^L», »treiben".
.Li^j »Laden" (Dozy belogt die anderen Bedeutun-
gen, die das Wort im Arabischen hat, >Bank, Estrade";
dazu kann noch gefügt werden ^Arüch s. v. pT I pUJ'/S
pll NI'JVNl üy 9x^*22^') das die Araber (Gauhari
```


## [2026-10-15T02:48:46.927Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 64188,64200p LAT.txt | cut -c1-300; grep -n -i 'tesca\\|tesqu' LEW_1910.txt | head -3; grep -n -i 'teus-' AHD_watkins1985.txt incoming/WLD/WLD_Bd1_pages.txt | head -5; sed -n 69924,69930p incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:48:47.384Z] TOOL RESULT

```
La racine est celle qui se retrouve, autrement elargie, dans
tremd, v. ce mot.
tescum, -I (dans la formule religieuse citee par Varron, L.L.
7,8, templum tescumque festo in sinistrum), tesca {tesqua),-o rum:
neutre substantive d'un adjectif *tescus, cf.Accius, 554 R 3 , quis
tu es mortalis, qui in deserta et tesca te apportes loca. Defini
par Varr., L.L.7,10 "loca quaedam agrestia, quod alicuius dei sunt ",
et par P.F.489,7 "loca augurio designata. Cicero aspera ait esse
et difficilia ", et le scholiaste d'Hor., Ep.i,14,19, attribue au mot
une origine sabine: loca deserta et difficilia lingua Sabinorum.
Appartient au vocabulaire religieux et poetique; rare et archaique.
fitymologie douteuse. On a rapproche iri. tere "rare, sterile"
(de *tersko-?).tessera
AHD_watkins1985.txt:1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
incoming/WLD/WLD_Bd1_pages.txt:67361:714                                                       teup-   — teus-
incoming/WLD/WLD_Bd1_pages.txt:67398:Gdf. *tus-sk-tio- an). Buga Kalba ir s. 252 geht von einer Wz. teus- „blasen,
incoming/WLD/WLD_Bd1_pages.txt:67412:2.    teus-       „still,      schweigend, zufrieden“.
incoming/WLD/WLD_Bd1_pages.txt:70579:sein“; Wz. tii- td x n- ?, weitere Beziehung zu *teus- „still“??
nach dem Adj. *tcro-, tlr umgebildet ist.
   Ygl. Curtius 224, Fick I 4 61, 225, 444, II 4 130, III 4 183, 188, Yf. LEWb. 2
u. terra torreo (s. auch testa
                 ,
                                 tesqua; letzteres aus nach *si-sku- „trocken“
                                                     ,
```


## [2026-10-15T02:48:49.767Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 67380,67412p incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:48:50.285Z] TOOL RESULT

```
1.    tens- „leeren“, tus-sko -, -sk-io- „leer“.
      A.v.   Kaus. tavsayeiti „macht los, la6t los“ (* tmisevS), Inchoativ (* tussled)
av. tusdn       „sie verlieren die Fassung“, baluci tusag „verlassen werden“;
ai.    tuccha-h     ,
                      tucchya-h ( Hus-sko -, *tus-sk-io-) „leer, ode, nichtig“, afghan.
tas     „leer“          zur ar. Gruppe Bthl. Wb. 624, Bgm. II 2 1, 478); aksl. Mt-b
                        (s.

„x£v6s u      ,
                  russ. toscij „leer, niichtern; mager, hager, diinn u usw. (= ai.
tucehya--, nicht glaublich setzt                          Trautmann Bsl. Wb. 333 wegen lit. tu&cias   ,


n. pi.       m. tuStl,        lett.           am, niichtern u die aber
                                          tuks,   f.   tuksa    „leer,   ledig,
                                                                                         ,

auch nicht z. B. nach Zubaty KZ. 31, 13 aus dem Slav, stammen, eine bsl.
Gdf. *tus-sk-tio- an). Buga Kalba ir s. 252 geht von einer Wz. teus- „blasen,
hauchen w aus.
   Fick I 4 63, 230, 450; seine (ein **teues *tues und *tezis voraussetzende)
                                                                          :




Anreihung von av. {hvuki- n. „Luftraum, Dunstkreis“ ist unwahrscheinlich
(Bthl. Wb. 797 f.), desgleichen die von lat. tesqua etwa „Einoden, diistere
und rauhe Gegenden u (ware diss. aus *tues qua; eher aus tersku-o-, s-ters-
„trocknen“).    Ahd. tlncesben „ausloschen, vertilgen, verderben (Petersson
IF. 20, 367) nicht als „veroden“ hierher (s. u. *ta- „schmelzen“).

2.    teus-       „still,      schweigend, zufrieden“.
```


## [2026-10-15T02:48:54.965Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *teus-|teus-\\.|\\bteus- ' AHD_watkins1985.txt | head; grep -n -i -E 'tesqua|empty' IEC.txt | grep -i -E 'tus|teus|tesq' | head -5"
}
```


### [2026-10-15T02:48:55.422Z] TOOL RESULT

```
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
8577:Skt. $astah, $asitah, pp. 'chastized'; sastih, Sistih, f. ‘reproof; Per. saxt “hard, strong, vio- lent’; Arm. sast, Let ‘reproof; cf. sastik, adj. ‘severe, acute’; Tokh. A (?) kast, B kest *hun- ger; Hitt. kasc & kastan, id. (here ?); Ir. cas ‘peevish, rash, violent? beside MIr. cás, ad]. “hard, cruel; W cas ‘odious’; ON bast. cpds. “harsh, violent; Icel. hastur “harsh, snappy, violent’; OE (*-à-) hæst ‘violent’ (here ?); Latv. cf. (?) sass (unripe, sour”, but this is apparent- ly isophonic with Lat. cassus ‘empty, vain, use- less. The isophone represented in Latin castus, gs -üs ‘rite, ceremony’, and in castus *devout, chaste' is of ambiguous origin, see WH and EM on these wds. though most pro- bably to type kat- “hold”, cf. cat-ena, etc.)
9887:liqutos “left, remaining’. Cf. liquos, etc. WP II, 396 Skt. riktáh “left; empty, destitute’; Arm. lik (*abandoned', but cf. liquos); Lat. cf. re-lictus “abandoned; remaining”; Gk. cf. apo-, ek-leip- téon “fit for leaving’; (the Gmc. forms OHG Iiban, bi-^; fir-leiben: OE læfan; and ON lifat (sic), pp. “left, remaining, fr. lifa, v. are am- biguous, perh. fr. *leip-, loip-, lip-, but cf. the phonol. of ‘seven, wolf); Li. liktas “left, remaining; likütis, usu. pl. liküciai ‘leavings, remains’. (Latv. likt ‘put; leave"; liktenis ‘fate’ is also ambig.)
17313:-stos (-stus) (2) adjective-formant extending a símplex Per. baste (“bound?: bhendh-); Gk. gnostós Cknown": £ndu-); Alb. i angshtë (^wild, rug- ged": angh- or angh-); i lashtë ('early': lad-); Lat. angustus (‘narrow’: angh- or angh-); au- gustus (high': aug); MHG cf. luste (‘plea- sant’: lubh-); OCS pustü (‘empty’: paus-); OPr. pausto, id.; Gk. cf. ápaustos, adj. (“un- ceasing’); Li. añkštas (‘narrow’: ang- or angh-); áukštas (“high?: aug-)
19778:uástos, is 'empty; space’. Cf. WP I, 109 & 219 Lat. vàstus, adj. ‘waste, huge; insatiable’; Olr. fáss, adj. ‘empty’; Ir. fás, adj. ‘desolate, desert- ed'; OHG wuosti, OE weste, Dutch woest, adj. “desert, waste, desolate, empty”; OS cf. wostin, wostinnia, f. ‘desert’; (NB. The Eng. form waste is hybridized with Gmc. via OFr. Cf. guast, whence Fr. gâter ‘to spoil’; It. guasto "waste"
```


## [2026-10-15T02:48:59.407Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,10}teus-.{0,300}' AHD_watkins1985.txt | grep -v CRANIUM | head -5; grep -n -E 'tus-sk|tusc|tus-' IEC.txt | head -5"
}
```


### [2026-10-15T02:48:59.950Z] TOOL RESULT

```
1399: kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX
2617:dusió “mar; be marred'. Cf. WP I, 766 & 816. See dus-, dusa, etc. Skt. düsyami “be spoilt’; Gk. cf. dos *mi- serable'; LG cf. tuschen, tüschen ‘extinguish’; (e-gde in) OE teorian (‘falter; tire, exhaust, fr. *deuséio)
3252:dhuksos ‘blow, breath, sigh, groan’. Cf. dhouks-, dheus-, dhous-. Cf. WP I, 838 & 846 Skt. cf. sam-dhuksaye ‘kindle, animate’; W dych (‘sigh, groan’, fr. *dhuksós, cf. dygaf ‘I carry? in relation to dwg, 3s.); OCS cf. dŭx-nọ, -nọti ‘blow, breathe; Cz. dech ‘breath’; MHG cf. (?) tuschen ‘be quiet’; (?) (*-ū-) tūsch ‘jest, mischief, fraud” (semantics obscure)
3347:dhuskos "dark" Cf. dhus- and cpds. WP I, 846 Lat. fuscus; OE dox, dux ‘fallow’; E cf. dusk; G cf. ver-tuschen, v. *hush up'; Norw. cf.
18506:teus- (teusõ, i0; touseio) (1) ‘quieten; grow quiet’. Cf. tous-, tus- Skt. cf. (o-gde) tosayami, v. ‘appease; gladden’; (z-gde) tusami, v. ‘settle down’; Av. tuš-, v. (3) radical: "be silent; Arm. ğokim, v. ‘sub- side’ fr. an induced formula *teusuio); Slovak čušať, čušiť, inf. “be silent
19379:Olr. toisc, f. ‘need, want’; (mod: ‘case, affair, object); R toska, f.; Cz. s-tesk, m. ‘yearning tusk- (2) (variant: tousk-) ‘dark; darkness’ OE cf. ge-buxod, adj. ‘darkened’; (o-gde in) R tusklyj, adj. ‘dim, dull’. (Isophone: Li. tus-
```


## [2026-10-15T02:51:09.438Z] TOOL CALL #66: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-508.json",
 "content": "{\n  \"pdf_page\": 508,\n  \"book_page\": 478,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-14\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Teub, Tebh, Tebhos\",\n      \"verdict\": \"unverified\",\n      \"modern_form\": \"Mann's *tebh-, *tebhus (?) 'side' (not in Pokorny, Walde-Pokorny or Watkins/AHD)\",\n      \"note\": \"The root is taken from Mann alone. IEC p.1371 (local IEC.txt line 18248-18250): 'tebh-, us (?) side. Cf. Supt. tueb-, toib- ... Per. tav, tū, s. fold, plait; Hitt. tapus, s. side. (The phonol. is obscure, as also that of Arm. kʿov side; Per. sū, suy, id.; Ir. taobh, id.; W tu, id.)'. Mann queries the root himself and says the phonology of the Armenian and Persian 'side' words is obscure. The comparison rests on Hittite tapuš 'side' and Old Irish tóeb / Irish taobh 'side'. Pokorny, Walde-Pokorny and Watkins have no such root. Mann's supplement page 1676 lies beyond the end of the local IEC OCR (it stops near p.1554). None of the four daughter nodes holds up: Pahlavi sōg and Armenian kʿov are phonologically impossible from *t-, Persian tū has no recorded etymology, and Arabic sūq is a Semitic word (Aramaic šūqā < Akkadian sūqu 'street'), not a borrowing from Persian sū.\",\n      \"note_fa\": \"ریشهٔ *tebh- «پهلو» را تنها مان (Mann) آورده، آن هم با نشانهٔ پرسش. او خودش نوشته که پیوند واژه‌های فارسی و ارمنی با آن از نظر آوایی «مبهم» است. پوکورنی، والده-پوکورنی و واتکینز چنین ریشه‌ای ندارند. پایهٔ این مقایسه فقط هیتی tapuš و ایرلندی taobh «پهلو» است. شاخه‌های نمودار هم پذیرفتنی نیستند: «سو» از پهلوی sōg است و آغازه‌اش با t- هندواروپایی نمی‌خواند؛ ریشهٔ «تو» دانسته نیست؛ و «سوق» عربی واژه‌ای سامی است. پس خودِ ریشه نامطمئن است و شاخه‌هایش بیشتر رد می‌شوند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/سو\",\n        \"https://en.wiktionary.org/wiki/تو\",\n        \"https://en.wiktionary.org/wiki/քով\",\n        \"https://en.wiktionary.org/wiki/سوق\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:1371\", \"status\": \"partial\", \"note\": \"IEC.txt line 18248-18250 (p.1371): 'tebh-, us (?) side ... Per. tav, tū, s. fold, plait; Hitt. tapus, s. side. (The phonol. is obscure, as also that of Arm. Kov side; Per. sü, suy, id.; Ir. taobh, id.)'. Mann has the root and the Persian/Armenian words, but queries the root and calls the Persian sū and Armenian kʿov comparisons phonologically obscure.\"},\n        {\"ref\": \"IEC:1676\", \"status\": \"not_found\", \"note\": \"Supplement page (the 'Supt. tueb-, toib-' cross-reference). The local IEC.txt ends at about p.1554 (858 leaves), so the supplement is not on disk.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_full/POK_01-03 grep 'tapus', 'taobh', 'tebh'\", \"stance\": \"silent\", \"note\": \"no root *tebh- 'side'; Hitt. tapuš and Ir. taobh are not cited\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt grep 'taobh', 'tapus'\", \"stance\": \"silent\", \"note\": \"no such root\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt grep 'tebh', 'taobh'\", \"stance\": \"silent\", \"note\": \"no root *tebh- 'side' in Watkins\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"tŭ\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Persian tū / tōy (تو، توی، توه) 'fold, layer; inside', as in tū-be-tū 'fold upon fold' in the Tāherī Qazvīnī verse. The word exists in this sense. Its only link to *tebh- 'side' is Mann's list (IEC 1371: 'Per. tav, tū, s. fold, plait'), and Mann himself queries the root. An inherited *t- would survive in Persian, and *-bh- could in principle give -v- (tav), but no Middle Persian or Old Iranian ancestor of tū 'fold/inside' is attested. Wiktionary marks the etymology of the 'fold' and 'inside' senses as missing. No independent source either confirms or rejects the derivation.\",\n          \"derivation_fa\": \"«تو» (توی، توه) به معنی «لا، چین» و «درون» در فارسی هست؛ در بیت طاهری قزوینی هم «تو به تو» به معنی لا به لا آمده است. تنها مان آن را در کنار ریشهٔ پرسش‌دار *tebh- «پهلو» آورده است. صورت فارسی میانه یا ایرانی باستانی برای این «تو» دیده نشده و ویکی‌واژه هم ریشه‌اش را نامعلوم می‌داند. پیوند آن با این ریشه نه تأیید می‌شود و نه رد؛ ادعای نورایی اثبات‌نشده است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تو\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1371\", \"status\": \"partial\", \"note\": \"IEC.txt line 18250: 'Per. tav, tū, s. fold, plait', listed under 'tebh-, us (?) side' with the remark '(The phonol. is obscure ...)'\"},\n            {\"ref\": \"IEC:1676\", \"status\": \"not_found\", \"note\": \"supplement page beyond the end of the local IEC OCR\"},\n            {\"ref\": \"MON:1158\", \"status\": \"not_checked\", \"note\": \"Mo'in print page; vajehyab's تو entries returned only unrelated senses (e.g. 'لب تو رفتن') and could not be mapped to p.1158\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt grep 'Falte', entries tü/tö\", \"stance\": \"silent\", \"note\": \"Horn has no entry for tū 'Falte/innen'; only no. 455 np. cīn 'Falte' turns up\"},\n            {\"src\": \"POK\", \"where\": \"POK_full grep 'tebh'\", \"stance\": \"silent\", \"note\": \"no root; the Persian tū is not cited anywhere\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt grep TAV / TU\", \"stance\": \"silent\", \"note\": \"no entry for تو 'fold' found\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"sŭk, sôk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real: Pahlavi sōg / sōk [swkʾ] 'side, direction' (MacKenzie: 'sōg [swk] side, direction; N sō(y)'; Nyberg: 'sōk [swk'] side; 4 ~ 4 gētē the four cardinal points ... NP sū, sūy'). Its derivation from IE *tebh- 'side' is impossible. Old Iranian *t- stays t- in Middle Persian and does not become s-, and *-bh- does not yield -k/-g. Horn (no. 748) states that no older form exists. Mann himself (IEC 1371) calls the Persian comparison phonologically obscure. The word has no accepted IE etymology.\",\n          \"derivation_fa\": \"پهلوی sōg / sōk «سو، جهت» در مکنزی و نیبرگ آمده و نیبرگ آن را ریشهٔ «سو» و «سوی» فارسی می‌داند. ولی برگرداندنش به *tebh- از نظر آوایی ناشدنی است: t- ایرانی باستان در فارسی میانه s- نمی‌شود و bh- هم به k/g نمی‌رسد. هرن (شمارهٔ ۷۴۸) می‌گوید صورت کهن‌تری از این واژه در دست نیست. پس واژهٔ پهلوی درست است، ولی پیوندش با این ریشه را پژوهش امروزی نمی‌پذیرد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/سو\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:165\", \"status\": \"contradicts\", \"note\": \"HRN.txt leaf 187 (p.165) no. 748: 'sū, sūi Richtung, Seite ... phlv. sūk Seite, Richtung. Eine ältere Form ist nicht vorhanden'. This supports the Pahlavi form but gives no IE root, so it does not support the arrow from *tebh-.\"},\n            {\"ref\": \"MON:1942\", \"status\": \"not_checked\", \"note\": \"Mo'in print page not mappable online; vajehyab سو returned only the 'manner' and Turkish 'water' senses\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 4568\", \"stance\": \"partial\", \"note\": \"'sōg [swk] side, direction' with NP sō(y). Confirms the word; gives no etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3456\", \"stance\": \"partial\", \"note\": \"'sōk [swk'] side 321; 4 ~ 4 gētē the four cardinal points of the world ... NP sū, sūy'. Confirms the word; gives no IE etymon.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sŭ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian sū / sūy (سو، سوی) 'side, direction' continues Middle Persian sōg [swkʾ] 'side, direction'. Two regular changes produce it: Middle Persian ō became ū in New Persian, and the final -g of the -ōg ending was lost, as in MP dārūg > NP dārū. The variant sūy keeps a glide. The compound čahārsū 'four-sided crossroads, covered bazaar' is old: Jāḥiẓ records al-jahārsūj, and Pahlavi has the *čahār-sōk form. This edge Pahlavi → Persian is uncontroversial. Only the higher link to *tebh- fails (see #2).\",\n          \"derivation_fa\": \"«سو» و «سوی» به معنی «جهت، طرف» از پهلوی sōg / sōk آمده است. ō فارسی میانه در فارسی نو به ū بدل شده و -g پایانی افتاده است، همان‌گونه که dārūg پهلوی «دارو» شده است. «چهارسو» (چهارسوک) به معنی چهارراه و بازار سرپوشیده نیز از همین واژه است. این گام از پهلوی به فارسی را هرن، نیبرگ و معین در حاشیهٔ برهان قاطع تأیید می‌کنند و ادعای نورایی در این گام درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/سو\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1182\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 644 (≈ p.1182-1187), entry سو with Mo'in's footnote; OCR line 38927 reads '(sôk ...) معرب آن سوق در «چهارسوق»'. Mo'in gives Pahlavi sōk and adds that its Arabicized form -sūq appears only in čahārsūq. Also leaf 131 (line 7711): 'چهارسو ... = چهارسوک = چارسوق، پهلوی ...'.\"},\n            {\"ref\": \"MON:1942\", \"status\": \"not_checked\", \"note\": \"Mo'in Farhang page not mappable online\"},\n            {\"ref\": \"IEC:1371\", \"status\": \"partial\", \"note\": \"'Per. sū, suy, id.' cited under tebh-, but Mann says 'the phonol. is obscure'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 748, p.165 (leaf 187)\", \"stance\": \"supports\", \"note\": \"'sū, sūi Richtung, Seite ... phlv. sūk Seite, Richtung'. The footnote names Arab. LW čahārsūj 'Markt' (orig. 'Vierseit').\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3456\", \"stance\": \"supports\", \"note\": \"'sōk [swk'] side ... NP sū, sūy'\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 4568\", \"stance\": \"supports\", \"note\": \"'sōg [swk] side, direction' → N sō(y)\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"sôq\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic sūq (سوق) means 'market, street'. It is not a borrowing of Persian sū 'side'. It comes from Aramaic šūqā 'street, market', which goes back to Akkadian sūqu(m) 'street, alley' (from siāqum 'to be narrow'). The word was already present in North Arabia, since Palmyrene šwqʾ is attested. Fraenkel (p.187) treats the Arabic word as a loan from Aramaic: it has no proper Arabic derivation, because the verb is denominative. Jeffery (p.183) notes that the Qurʾānic aswāq (pl.) means 'streets', matching the Old Testament and Targum šūq. He adds that the word passed from Mesopotamia into Iranian as the Pahlavi Aramaic heterogram ŠWKʾ 'market', so the borrowing ran the other way. The only real Persian → Arabic link is čahārsūq, the Arabicized form of čahārsū(k), whose last syllable was assimilated to Arabic sūq. Note also that the chart's gloss 'path' is secondary; the core meaning is 'street, market'.\",\n          \"derivation_fa\": \"«سوق» عربی به معنی «بازار، کوچه» از «سو»ی فارسی گرفته نشده است. این واژه از آرامی šūqā آمده و آن هم از اکدی sūqu «کوچه، گذر» است. فرنکل آن را وام‌واژهٔ آرامی در عربی می‌داند و جفری در «واژگان بیگانهٔ قرآن» می‌گوید راه وام‌گیری وارونه بوده است: واژهٔ آرامی به صورت هزوارش ŠWKʾ «بازار» به پهلوی رسیده است. تنها «چهارسوق» معرّبِ «چهارسو(ک)» فارسی است که پایانش با «سوق» عربی همسان شده. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/سوق\"],\n          \"ref_check\": [\n            {\"ref\": \"FVF:380\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari's Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi is not accessible here (noorlib/ketabnak need a browser or login)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"FVQ.txt lines 11479-11505, p.183 s.v. Sūq\", \"stance\": \"contradicts\", \"note\": \"'A street ... used as the שוק of the O.T. and the Targums for street ... Fraenkel, Fremdw, 187, is doubtless right in thinking that it is a word taken over by the Arabs from more settled peoples. The Aram. שוקא; Syr. ... From some early Mesopotamian source the word passed into Iranian, for we find the Phlv. ideogram ... shoka meaning market'\"},\n            {\"src\": \"AFA\", \"where\": \"AFA.txt lines 6646-6657, pp.187-188\", \"stance\": \"contradicts\", \"note\": \"'das alte Wort [sūq] wahrscheinlich nicht arabischer Herkunft, sondern erst aus [Aram. šūqā], Palmyr. ... entlehnt. Im Arabischen hat es keine rechte Ableitung'\"},\n            {\"src\": \"HRN\", \"where\": \"p.165 no. 748, footnote 2\", \"stance\": \"partial\", \"note\": \"Horn tentatively wonders whether 'die mit s beginnenden' words collected by Hübschmann (ZDMG 46, 247) belong with sū, ending with a question mark. This is the only old hint in Nourai's direction.\"},\n            {\"src\": \"AFM\", \"where\": \"AFM.txt line 635\", \"stance\": \"silent\", \"note\": \"Addi Shir uses السوق only to gloss البازار (Persian bāzār); he does not list sūq itself as Persian\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"sŭq; sŭqî\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian sūq (سوق) 'market, bazaar street', plural aswāq, is a loan from Arabic sūq, and Mo'in tags it [ع.]. Persian sūqī 'man of the bazaar, tradesman' (pl. sūqiyya 'common people') is the Arabic nisba adjective sūqī. Čahārsūq is the Arabicized spelling of Persian čahārsū(k) 'crossroads bazaar', its final syllable assimilated to Arabic sūq. The edge Arabic → Persian is correct. The upstream claim that the Arabic word comes from Persian sū is not (see #4).\",\n          \"derivation_fa\": \"«سوق» به معنی «بازار» (جمعش «اسواق») و «سوقی» به معنی «بازاری» (جمعش «سوقیّه») از عربی وارد فارسی شده‌اند؛ معین هم «سوق» را با نشان [ع.] آورده است. «چهارسوق» معرّبِ «چهارسو(ک)» فارسی است که با «سوق» عربی درآمیخته. پس این گام از عربی به فارسی درست است، ولی خودِ واژهٔ عربی ریشه در آرامی و اکدی دارد و از «سو»ی فارسی نیست.\",\n          \"sources\": [\"https://vajehyab.com/moein/سوق\", \"https://en.wiktionary.org/wiki/سوق\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:1955\", \"status\": \"supports\", \"note\": \"Mo'in via vajehyab (archived): 'سوق [ع.] (اِ.) بازار؛ ج. اسواق'. Arabic origin and the meaning 'bazaar' are as charted; the print page number could not be mapped online.\"},\n            {\"ref\": \"BQT:1182\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 644, footnote to سو: 'معرب آن سوق در «چهارسوق»'. Mo'in treats only the -sūq of čahārsūq as an Arabicization of Persian sōk; he does not make independent sūq Persian.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"p.183 s.v. Sūq\", \"stance\": \"supports\", \"note\": \"the Arabic word is Aramaic-derived; in later Arabic it 'normally means a market place', which is the source of the Persian loan\"},\n            {\"src\": \"HRN\", \"where\": \"p.165 no. 748 fn. 2\", \"stance\": \"partial\", \"note\": \"'Arab. LW čahārsūj Markt ... (ursprünglich Vierseit, Viereck)'. The compound is Persian; simple sūq is not discussed.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Armenian\",\n          \"words\": \"kov\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Armenian kʿov (քով) 'side, flank; beside' is a real word. It cannot continue PIE *tebh-, because PIE *t- gives Armenian tʿ-, never kʿ-. Mann himself (IEC 1371) calls the phonology of 'Arm. kʿov side' obscure. Ačaṙean (Armenian Etymological Dictionary IV 588b) takes 'side, flank' as the original meaning and leaves the origin unknown. In his Provincial Dictionary (1913, pp.1121-1122) he derives it from koł 'side, rib', which probably explains the chart's gloss 'rib'. Another view takes Middle Armenian kʿov 'near' from the instrumental of kʿo 'thy'.\",\n          \"derivation_fa\": \"واژهٔ ارمنی kʿov «پهلو، کنار» وجود دارد، ولی از *tebh- نمی‌تواند آمده باشد، چون t- هندواروپایی در ارمنی tʿ- می‌شود، نه kʿ-. خودِ مان آوای آن را «مبهم» می‌خواند. آچاریان ریشه‌اش را نمی‌داند و در جای دیگر آن را از koł «پهلو، دنده» می‌گیرد؛ گزارهٔ «دنده» در نمودار احتمالاً از همین‌جا آمده است. پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/քով\"],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1371\", \"status\": \"contradicts\", \"note\": \"IEC.txt line 18250: '(The phonol. is obscure, as also that of Arm. Kov side ...)'. Mann lists kʿov only as a doubtful parallel, not as a regular reflex.\"},\n            {\"ref\": \"IEC:1676\", \"status\": \"not_found\", \"note\": \"supplement page beyond the end of the local IEC OCR\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full grep 'kʿov', 'tebh'\", \"stance\": \"silent\", \"note\": \"Armenian kʿov is not cited\"},\n            {\"src\": \"WLD\", \"where\": \"WLD_Bd1_pages.txt grep\", \"stance\": \"silent\", \"note\": \"no such root or Armenian word\"},\n            {\"src\": \"IEC\", \"where\": \"line 18463 teubh- (2)\", \"stance\": \"partial\", \"note\": \"Mann lists a different Arm. (ambig.) 'Éov' 'tuft' under teubh- 'tuft, clump'. The kʿov 'side' comparison is not his main analysis.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Teus\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *tews- 'to be empty, to empty, drain'; *tus-sk(i̯)o- 'empty'\",\n      \"note\": \"Pokorny IEW 1085: 'teus- leeren; tus-sko-, -sk-io- leer. Av. Kaus. taošayeiti macht los ..., Inchoativ (*tus-skō) av. tusən sie verlieren die Fassung ...; ai. tuccha-, tucchya- leer, öde, nichtig; afghan. taš leer; lat. tesqua n. pl. Einöden ...' (POK_03.txt line 4659). Walde-Pokorny I 714 and Buck 13.22 (via Lith. tuščias) agree; Wiktionary has *tews- 'to be empty; to drain'. The root, its label and its gloss are all correct. A separate homonym *tews- 'be calm, content' (Skt. tuṣyati) should not be confused with it.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tews- «تهی کردن، تهی بودن» با صورت بالیدهٔ *tus-sk(i̯)o- «تهی» در پوکورنی (ص ۱۰۸۵)، والده-پوکورنی و ویکی‌واژه آمده است. شاخه‌های آن اوستایی tusən، سنسکریت tucchya-، پهلوی tuhīg و فارسی «تهی» است. ریشه، برچسب زبان و معنای آن درست است و ادعای نورایی پذیرفته است. نباید آن را با ریشهٔ هم‌آوای *tews- «آرام و خشنود بودن» یکی گرفت.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tews-\",\n        \"https://en.wiktionary.org/wiki/تهی\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1085\", \"status\": \"supports\", \"note\": \"POK_03.txt lines 4658-4659: 'teus- leeren; tus-sko-, -sk-io- leer. Av. Kaus. taosayeiti macht los ... av. tusən ... ai. tuccha-, tucchya- leer, öde, nichtig ... lat. tesqua n. Pl. Einöden'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p.714 (WLD_Bd1_pages.txt lines 67380-67410)\", \"stance\": \"supports\", \"note\": \"'1. teus- leeren, tus-sko-, -sk-io- leer. Av. Kaus. taošayeiti ... av. tusən ... ai. tuccha-, tucchya- leer, öde, nichtig'. WLD rejects tesqua, however (see node #4).\"},\n        {\"src\": \"SYN\", \"where\": \"13.22 EMPTY (SYN.txt line 23759)\", \"stance\": \"supports\", \"note\": \"'Lith. tuščias ... : ChSl. tŭštĭ, Skt. tuccha-, tucchya- empty, vain, Av. tuš- in caus. taošaya- let loose, free ... Walde-P. 1.714'\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\", \"note\": \"Watkins has no entry for *teus- 'empty' (no English reflex)\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"taoš, tuš, tusen, tussya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan taoš- / tuš- 'to be empty, loose' is well attested (Bartholomae col. 624). Its inchoative present tusa- appears in tusən 'they lose composure, grow weak' (V. 3.32), and its causative taošaya- means 'let loose, let fall' (Yt. 10.48). All of these continue PIE *tews- / *tus-sḱé-. 'tussya' is not an attested Avestan word. It mirrors the reconstruction *tus-sk-io- (Skt. tucchya-) behind Middle Persian tuhīg, Proto-Iranian *tušyá-. The label 'Old Persian' is also unsupported, since this root is not attested in the Old Persian inscriptions. The Avestan forms are confirmed; the OP label and 'tussya' as an attested form are not.\",\n          \"derivation_fa\": \"در اوستایی ستاک taoš- / tuš- «تهی و رها بودن» آمده است (بارتولومه، ستون ۶۲۴). صورت آغازی آن tusən «سست شدند، از خود رفتند» است و صورت سببی‌اش taošaya- «رها کردن». این‌ها از *tews- / *tus-sḱé- هندواروپایی‌اند. اما «tussya» در اوستا دیده نشده و بازسازیِ *tus-sk-io- (سنسکریت tucchya-) است. در کتیبه‌های پارسی باستان هم این ریشه نیامده است. پس صورت‌های اوستایی درست‌اند، ولی برچسب «پارسی باستان» و «tussya» با احتیاط پذیرفتنی‌اند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tews-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1085\", \"status\": \"supports\", \"note\": \"'Av. Kaus. taošayeiti macht los, läßt los (*touseiō), Inchoativ (*tus-skō) av. tusən sie verlieren die Fassung' (POK_03.txt line 4659)\"},\n            {\"ref\": \"SYN:933\", \"status\": \"supports\", \"note\": \"Buck 13.22 EMPTY (SYN.txt line 23759): 'Av. tuš- in caus. taošaya- let loose, free'. The page number 933 is consistent with section 13.22.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 624 (BRT.txt line 11797-11800)\", \"stance\": \"supports\", \"note\": \"'taoš- V. leer, los sein. Praes. 14 (Inkoh.) tusa-, 30 (Kaus.) taošaya-. 1) Inkoh. leer sva. schwach werden, die Fassung verlieren: ... dasvā tusən V.3.32 ... Vgl. afγ. taš leer ... ai. tucchya- Adj. leer ... np. tihī leer'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 404 (HRN.txt line 3774-3776)\", \"stance\": \"supports\", \"note\": \"'tihī leer ... aw. tusən sie entleeren sich (Bartholomae); phlv. tuhīk leer; ai. tucchyá-'\"},\n            {\"src\": \"KNT\", \"where\": \"KNT_full.txt grep 'taus', 'tuš'\", \"stance\": \"silent\", \"note\": \"no Old Persian form of this root in Kent's lexicon\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"tihîk, tuhîk\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian tuhīg [twhyk] 'empty, vain' goes back to Proto-Iranian *tušyá- (Proto-Indo-Iranian *tušćyá-, PIE *tus-sk-yó-, cognate with Vedic tucchyá-). Old Iranian intervocalic -š- weakened to -h-, and the suffix *-ya- was extended with -ka-, giving -īg/-īk. The variant tihīk shows u > i assimilation to the following ī, and it surfaces in New Persian tihī.\",\n          \"derivation_fa\": \"پهلوی tuhīg / tuhīk «تهی، بیهوده» از ایرانی آغازین *tušyá- (هندوایرانی *tušćyá-) است و با سنسکریت ودایی tucchyá- هم‌ریشه است. ش میانی ایرانی باستان در فارسی میانه به ه بدل شده و پسوند -ya- با -ka- بالیده و به -īg رسیده است. صورت tihīk همگونیِ u با ī را نشان می‌دهد. مکنزی و نیبرگ هر دو این واژه را دارند و ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تهی\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:539\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaf 767 (p.539, continued from p.538): headword تهی 'بمعنی خالی ۷ هم هست که در مقابل پر است'. The word and meaning are present, but footnote 7 with Mo'in's Pahlavi form is not legible in the OCR, and no scan of p.539 is available (ref_page.py: 'No scan of BQT covers printed page 539').\"},\n            {\"ref\": \"SNS:151\", \"status\": \"not_checked\", \"note\": \"SNS OCR has no page mapping; grep 'tuhīk|tuhik' in SNS.txt/SNS_pages.txt found nothing legible\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 5019\", \"stance\": \"supports\", \"note\": \"'tuhīg [twhyk | M twhyg, N tuhī] empty, vain'\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3803\", \"stance\": \"supports\", \"note\": \"'tuhīkēh emptiness ... From tuhīk empty, from Av. taoš-, pres. tusa-; MPrs twhyg; Paz. tuhī; J.-Prs. twhy; NP tuhī, tihī, tahī'\"},\n            {\"src\": \"HUB\", \"where\": \"§24 (HUB.txt line 4882)\", \"stance\": \"supports\", \"note\": \"'tihī leer = päz. tihī, phl. tuhīk' (u > i)\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"tah; tahî\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"tahī / tuhī / tihī (تهی) 'empty' is the regular continuation of MP tuhīg: the final -g was lost and the vowel varies between tu-, ti- and ta-. This is confirmed by Horn no. 404, Hübschmann §24, Nyberg and Wiktionary. tah (ته) 'bottom' is less certain. Wiktionary derives it from MP tah, 'possibly' from *tews-, and compares tak 'bottom'. The semantic step 'empty' → 'bottom' is not secured, and Horn, MacKenzie and Nyberg do not link tah to tahī. So tahī is confirmed and tah only plausible.\",\n          \"derivation_fa\": \"«تهی» (تُهی، تِهی) دنبالهٔ منظم پهلوی tuhīg است: -g پایانی افتاده و واکهٔ نخست میان u، i و a در نوسان است. هرن، هوبشمان، نیبرگ و ویکی‌واژه این را تأیید می‌کنند. «ته» به معنی «بن» نامطمئن‌تر است: ویکی‌واژه آن را «شاید» از همین ریشه می‌داند و با «تک» می‌سنجد، ولی هرن و مکنزی پیوندی میان «ته» و «تهی» نمی‌گذارند. پس «تهی» درست است و «ته» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/تهی\", \"https://en.wiktionary.org/wiki/ته\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:90\", \"status\": \"supports\", \"note\": \"HRN.txt line 3774 (no. 404, p.90): 'tihī leer, tihī, tehī ... aw. tusən sie entleeren sich; phlv. tuhīk leer; ai. tucchyá-'. This covers tahī; tah 'bottom' is not mentioned.\"},\n            {\"ref\": \"BQT:539\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt leaf 767: 'تهی ... بمعنی خالی ... که در مقابل پر است' and 'ته ... مخفف تهی است که خالی باشد'. Borhan treats one sense of ته as a shortening of تهی, which supports a link, but the etymological footnote is illegible.\"},\n            {\"ref\": \"BQT:537\", \"status\": \"not_checked\", \"note\": \"page with ته 'bottom' (leaf ≈765); its OCR shows only 'ولای و ته را نیز گویند', with no footnote legible\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"line 3803\", \"stance\": \"supports\", \"note\": \"'NP tuhī, tihī, tahī' from MP tuhīk\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 207] / ARY_pages.txt entry ۸ تهی\", \"stance\": \"supports\", \"note\": \"the تهی entry groups 'TAOSH, TAOSHAEITI ... TUTHYA, TUSSYA ... TUHIK, TIHIK, TUHIG ... TESCA' and cites 'برهان قاطع ۲ و ۵۳۵'\"},\n            {\"src\": \"PHD\", \"where\": \"line 5019\", \"stance\": \"supports\", \"note\": \"'tuhīg ... N tuhī'\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"tesqua\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin tesca / tesqua (n. pl.) means 'wild, desolate places', an old augural and Sabine word (Varro, LL 7.8-10; Accius 'deserta et tesca loca'). Pokorny (1085) puts it under *teus- from *tu̯eskua (*tus-sk-), giving the sense 'emptied, deserted lands'. Walde-Pokorny (I 714) rejects this and prefers *tersk- from *(s)ters- 'to dry'. Ernout-Meillet call the etymology 'douteuse' and compare Irish terc 'rare, sterile'. Nourai follows Pokorny, which is a defensible but contested view.\",\n          \"derivation_fa\": \"واژهٔ لاتینی tesca / tesqua (جمع خنثی) به معنی «جاهای وحشی و بیابانی» واژه‌ای کهن، دینی و سابینی است. پوکورنی آن را از *teus- با صورت *tu̯eskua می‌گیرد، یعنی «زمین تهی». ولی والده-پوکورنی این را رد می‌کند و آن را از *ters- «خشکیدن» می‌داند؛ ارنو و میه هم ریشهٔ آن را «مشکوک» خوانده‌اند. نورایی پیرو پوکورنی است، و این پیوند با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tews-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1085\", \"status\": \"supports\", \"note\": \"POK_03.txt line 4659: 'lat. tesqua n. Pl. Einöden (*tueskua)'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I 714 (WLD_Bd1_pages.txt lines 67406-67409)\", \"stance\": \"contradicts\", \"note\": \"'desgleichen die von lat. tesqua etwa Einöden, düstere und rauhe Gegenden (wäre diss. aus *tuesqua; eher aus tersku-o-, s-ters- trocknen)'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. tescum (LAT.txt line 64190-64200)\", \"stance\": \"contradicts\", \"note\": \"'tesca (tesqua) ... loca deserta et difficilia lingua Sabinorum ... Étymologie douteuse. On a rapproché irl. terc rare, stérile (de *tersko-?)'\"},\n            {\"src\": \"SYN\", \"where\": \"SYN.txt line 23607\", \"stance\": \"partial\", \"note\": \"Ir. terc 'scarce' 'perh. : Lat. tesca, tesqua waste, uncultivated regions'. Buck follows the *ters- connection, not *teus-.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-15T02:51:09.488Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-508.json (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:51:15.624Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\np='data/verification/page-508.json'\ns=open(p).read()\nold=\"and 'ته ... مخفف تهی است که خالی باشد'. Borhan treats one sense of ته as a shortening of تهی, which supports a link, but the etymological footnote is illegible.\"\nnew=\"and, in a neighbouring entry whose headword is not legible in the OCR, 'مخفف تهی است که خالی باشد' (a short form of tahī). The etymological footnote is illegible.\"\nassert old in s; s=s.replace(old,new); open(p,'w').write(s)\nEOF\npython3 -m json.tool data/verification/page-508.json >/dev/null && python3 tools/verify_check.py 508"
}
```


### [2026-10-15T02:51:16.222Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'unverified': 1, 'disputed': 3, 'confirmed': 3, 'plausible': 3}
root verdicts: {'unverified': 1, 'confirmed': 1}
ref checks: {'partial': 5, 'not_found': 2, 'not_checked': 6, 'contradicts': 2, 'supports': 6}
books consulted: {'silent': 7, 'partial': 6, 'supports': 12, 'contradicts': 4} | by book: {'HRN': 5, 'PHD': 4, 'NYB': 4, 'POK': 2, 'ARY': 2, 'FVQ': 2, 'WLD': 2, 'AFA': 1, 'AFM': 1, 'IEC': 1, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'LAT': 1, 'SYN': 1}
```


## [2026-10-15T02:51:25.952Z] TOOL CALL #68: SubagentHandback

```json
{
 "message": "I verified page 508 (book page 478) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-508.json`. `verify_check.py 508` shows 10/10 nodes verified and 0 PROBLEM lines.\n\n**Counts:**\n- **Roots (2):** Teus confirmed (Pokorny 1085 *teus- 'empty'); Teub/Tebh unverified, because only Mann lists *tebh- 'side', with a question mark, and Pokorny, Walde-Pokorny and AHD don't have it.\n- **Nodes (10):** 3 confirmed, 3 plausible, 3 disputed, 1 unverified, 0 transcription_suspect.\n\n**Disputed:**\n- **Teub #2, Pahlavi sōk/sōg 'side':** the word is real (MacKenzie, Nyberg), but it can't come from *tebh-, since t- doesn't become s-. Horn says no older form exists, and Mann himself calls the comparison \"phonol. obscure\".\n- **Teub #4, Arabic sūq:** it is not borrowed from Persian sū. It comes from Aramaic šūqā, which goes back to Akkadian sūqu 'street' (Fraenkel p.187, Jeffery p.183). Jeffery says the word passed the other way, into Pahlavi as a written Aramaic form meaning 'market'. Only čahārsūq is an Arabicized Persian word (čahārsū(k)).\n- **Teub #6, Armenian kʿov 'side':** PIE *t- gives Armenian tʿ-, never kʿ-. Ačaṙean says the origin is unknown, and elsewhere derives it from koł 'side, rib'.\n\n**Other caveats:**\n- **Teus #4, Latin tesqua:** marked plausible; Walde-Pokorny rejects the *teus- link (it prefers *ters- 'dry') and Ernout-Meillet call the etymology doubtful.\n- **Teus #1, Avestan forms:** the Avestan words are fine, but \"tussya\" is a reconstruction rather than an attested word, and the \"Old Persian\" label has no support.\n- **Teus #3, tah 'bottom':** only plausible; tahī 'empty' is confirmed.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**References I couldn't check:**\n- IEC:1676 (Mann's supplement): the local copy stops at about p.1554.\n- FVF:380: no access.\n- MON pages: can't be matched to page numbers online.\n- SNS:151: no page mapping in the OCR.\n- BQT:537 and BQT:539: no scan of those pages exists, and the OCR footnotes are illegible."
}
```


### [2026-10-15T02:51:26.343Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
