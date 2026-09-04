# Verification process log — persian-explanations-pages-56-60-101-126-311-345


## [2026-09-04T23:05:15.371Z] INPUT

Task: add Persian explanations to existing verification files. Files: /home/sfmqrb/git/rishe/data/verification/page-{56,57,58,59,60,101,126,311,345}.json.

Read the section "Persian explanation (required)" in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow it exactly. For EVERY node add `derivation_fa` and for EVERY entry (root) add `note_fa`. Base them on the existing `derivation`/`note`, `verdict`, `ref_check` and `consulted` fields — no new research is needed, but read the whole node so the Persian text reflects the actual findings (which sources support/contradict, what the modern view is, whether a transcription flag is the book's misprint or the extraction's — see `error_in`/`book_prints` where present). Write for an educated Persian reader in the idiom of Persian etymological scholarship (as Hasandust, Abolghasemi or Mo'in's Borhan footnotes would put it): Persian terminology (هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی باستان، فارسی میانه، وام‌واژه، دگرگونی آوایی، قلب، ابدال، معرّب، ریشه‌شناسی عامیانه، هم‌ریشه…), Persian-script forms first with older forms in Latin transliteration, the sound changes explained the way Persian philology states them, and a clear Persian statement of what the verdict means (ادعای نورایی درست است / با احتیاط پذیرفتنی / پژوهش امروزی رد می‌کند و می‌گوید … / خطای چاپی کتاب / خطای خوانش اسکن). 2–5 sentences each, formal and natural — NOT a word-for-word translation of the English, and not machine-like. Persian digits are fine. Name sources the way Persian readers know them (پوکورنی، بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، کلاین، ویکی‌واژه).

Edit the files in place, changing nothing else. Validate each with `python3 -m json.tool` and run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 56 57 58 59 60 101 126 311 345` (0 PROBLEM lines). Reply with one line per page: number of nodes given `derivation_fa`, and confirm every entry has `note_fa`.


## [2026-09-04T23:05:17.551Z] AGENT

I'll start by reading the instructions file.


## [2026-09-04T23:05:19.653Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T23:05:19.666Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which
5	this repository (`/home/sfmqrb/git/rishe`) turned into JSON
6	(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
7	are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.
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
38	   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
39	     (a misread letter, an impossible form, a wrong Persian script); say what you think the
40	     book actually printed and why.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	
46	## Checking Nourai's OWN cited references (required)
47	
48	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
49	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
50	You must check them:
51	
52	- The bibliography key (abbreviation → book) is in
53	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
54	- Where each reference can be read online is in
55	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
56	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
57	- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
58	  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
59	  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
60	  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
61	  it actually says what Nourai's arrow says.
62	- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
63	  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
64	  OCR whole books. Fetch only the cited page:
65	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
66	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
67	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
68	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
69	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
70	  surrounding lines you relied on) verbatim to the companion file
71	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
72	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
73	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
74	  note the correct pdf page in your ref_check note.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
76	- Do this for at least ONE cited reference per node (the most authoritative available:
77	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
78	  BQT/MON for Persian). If none of a node's references is accessible, say so.
79	
80	Add to every node a `ref_check` array:
81	
82	```json
83	"ref_check": [
84	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
85	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
86	]
87	```
88	
89	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
90	word but a different/looser derivation) · `contradicts` (the reference says something else)
91	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
92	not accessible online). Quote the key phrase of the reference in `note` when you can.
93	
94	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
95	
96	
97	
98	## Transcription flags: say WHERE the error is (required)
99	
100	For every node you mark `transcription_suspect`, look at the printed page itself — render it
101	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg<pdf page>`
102	(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:
103	
104	```json
105	"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
106	                               // "extraction" = the book prints the correct form; the JSON misread it
107	                               // "unknown" = could not decide from the image
108	"book_prints": "borrāgō",      // what the printed page actually shows
109	"correct_form": "borrāgō"      // the form that should stand (per the sources)
110	```
111	
112	Usually the extraction is faithful and the problem is in the book itself; say so plainly in
113	`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
114	differs from the page is it an extraction error (report those separately in your summary — the
115	owner fixes the data).
116	
117	
118	## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root
119	
120	Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
121	English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
122	برهان قاطع) would explain it to an educated Persian reader:
123	
124	- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
125	  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
126	  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
127	  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
128	- Give the Persian word first in Persian script, then the older forms in Latin transliteration
129	  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
130	  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
131	- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
132	  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
133	- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
134	  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب.
135	- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
136	  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
137	  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).
138	
139	Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.
140	
141	## Process documentation (required)
142	
143	The owner wants to be able to audit every step later. Therefore:
144	
145	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
146	  curl), run
147	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
148	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
149	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
150	  one Bash command to save time.)
151	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
152	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
153	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
154	  be re-run.
155	- Your full transcript (every tool call and result) is exported automatically by the
156	  coordinator; nothing else needed for that.
157	
158	
159	## Use EVERY relevant book on disk (required)
160	
161	Checking only the reference Nourai cites is not enough. For every node, also consult the
162	other books in the local library that could speak to that claim, and record what each says.
163	The list of which books cover which kind of node, with file paths, is
164	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
165	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
166	
167	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
168	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
169	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
170	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
171	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
172	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
173	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
174	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
175	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
176	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
177	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
178	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
179	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
180	
181	Grep each file for the headword (several spellings; Latin transliteration for the Western
182	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
183	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
184	node (separate from `ref_check`, which is only for the references Nourai himself cites):
185	
186	```json
187	"consulted": [
188	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
189	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
190	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
191	]
192	```
193	
194	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
195	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
196	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
197	entries from different books whenever the matrix lists two or more books for its language.
198	
199	## Sources to use (in roughly this order)
200	
201	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
202	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
203	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
204	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
205	  Use URL-encoded Persian/Arabic script for those pages.
206	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
207	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
208	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
209	  appendix; the online appendix is the updated edition of the same list.
210	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
211	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
212	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
213	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
214	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
215	  if needed for a hard case.
216	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
217	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
218	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
219	
220	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
221	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
222	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
223	which are where errors are likelier.
224	
225	## Output — write ONE file per page
226	
227	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
228	
229	```json
230	{
231	  "pdf_page": 126,
232	  "book_page": 96,
233	  "verified_by": "claude-fable-5-1",
234	  "verified_on": "2026-09-04",
235	  "entries": [
236	    {
237	      "entry": 0,
238	      "root": "Dheigh, Dhigha",
239	      "verdict": "confirmed",
240	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
241	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
242	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
250	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
251	        },
252	        {
253	          "id": 9,
254	          "lang": "Greek",
255	          "words": "paradeisos",
256	          "verdict": "confirmed",
257	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
258	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
259	        }
260	      ]
261	    }
262	  ]
263	}
264	```
265	
266	Rules:
267	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
268	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
269	- `words` = the transliterations of the node joined by "; " (copy from the chart).
270	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
271	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
272	- Keep `note` on the entry for root-level comments and for anything cross-cutting
273	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
274	- If a node lists several words, cover each word; if they differ in verdict, use the worst
275	  verdict for the node and explain per word in `derivation`.
276	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
277	  from root Mad"), evaluate it: say which side modern scholarship takes.
278	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array) AND `derivation_fa` (string); every entry has `note_fa`.
279	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
282	  Do not paste the JSON back into your reply.
283	
```


## [2026-09-04T23:05:20.390Z] TOOL CALL #2: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; wc -c /home/sfmqrb/git/rishe/data/verification/page-{56,57,58,59,60,101,126,311,345}.json",
 "description": "List verification files"
}
```


### [2026-09-04T23:05:22.759Z] TOOL RESULT

```
total 1876
drwxrwxr-x 4 sfmqrb sfmqrb  4096 Sep  4 19:03 .
drwxrwxr-x 6 sfmqrb sfmqrb  4096 Sep  4 10:26 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 86233 Sep  4 19:04 page-101.json
-rw-rw-r-- 1 sfmqrb sfmqrb 75899 Sep  4 19:04 page-126.json
-rw-rw-r-- 1 sfmqrb sfmqrb 73989 Sep  4 19:04 page-311.json
-rw-rw-r-- 1 sfmqrb sfmqrb 89309 Sep  4 19:01 page-31.json
-rw-rw-r-- 1 sfmqrb sfmqrb 32633 Sep  4 19:02 page-32.json
-rw-rw-r-- 1 sfmqrb sfmqrb 46382 Sep  4 19:04 page-33.json
-rw-rw-r-- 1 sfmqrb sfmqrb 81781 Sep  4 15:27 page-345.json
-rw-rw-r-- 1 sfmqrb sfmqrb 60196 Sep  4 14:48 page-34.json
-rw-rw-r-- 1 sfmqrb sfmqrb 61041 Sep  4 14:45 page-35.json
-rw-rw-r-- 1 sfmqrb sfmqrb 51890 Sep  4 14:46 page-36.json
-rw-rw-r-- 1 sfmqrb sfmqrb 43364 Sep  4 14:59 page-37.json
-rw-rw-r-- 1 sfmqrb sfmqrb 29055 Sep  4 14:59 page-38.json
-rw-rw-r-- 1 sfmqrb sfmqrb 60665 Sep  4 19:04 page-39.json
-rw-rw-r-- 1 sfmqrb sfmqrb 39518 Sep  4 15:12 page-40.json
-rw-rw-r-- 1 sfmqrb sfmqrb 58153 Sep  4 18:59 page-41.json
-rw-rw-r-- 1 sfmqrb sfmqrb 82252 Sep  4 19:03 page-42.json
-rw-rw-r-- 1 sfmqrb sfmqrb 44722 Sep  4 15:27 page-43.json
-rw-rw-r-- 1 sfmqrb sfmqrb 54207 Sep  4 15:33 page-44.json
-rw-rw-r-- 1 sfmqrb sfmqrb 51017 Sep  4 15:34 page-45.json
-rw-rw-r-- 1 sfmqrb sfmqrb 27483 Sep  4 19:04 page-46.json
-rw-rw-r-- 1 sfmqrb sfmqrb 71378 Sep  4 15:47 page-47.json
-rw-rw-r-- 1 sfmqrb sfmqrb 19007 Sep  4 15:38 page-48.json
-rw-rw-r-- 1 sfmqrb sfmqrb 43664 Sep  4 15:47 page-49.json
-rw-rw-r-- 1 sfmqrb sfmqrb 46040 Sep  4 15:56 page-50.json
-rw-rw-r-- 1 sfmqrb sfmqrb 63823 Sep  4 15:58 page-51.json
-rw-rw-r-- 1 sfmqrb sfmqrb 31491 Sep  4 15:48 page-52.json
-rw-rw-r-- 1 sfmqrb sfmqrb 37919 Sep  4 16:00 page-53.json
-rw-rw-r-- 1 sfmqrb sfmqrb 59712 Sep  4 19:04 page-54.json
-rw-rw-r-- 1 sfmqrb sfmqrb 41999 Sep  4 16:02 page-55.json
-rw-rw-r-- 1 sfmqrb sfmqrb 62487 Sep  4 19:03 page-56.json
-rw-rw-r-- 1 sfmqrb sfmqrb 43914 Sep  4 19:01 page-57.json
-rw-rw-r-- 1 sfmqrb sfmqrb 59780 Sep  4 19:01 page-58.json
-rw-rw-r-- 1 sfmqrb sfmqrb 54555 Sep  4 19:02 page-59.json
-rw-rw-r-- 1 sfmqrb sfmqrb 52537 Sep  4 19:03 page-60.json
drwxrwxr-x 3 sfmqrb sfmqrb  4096 Sep  4 19:04 process
drwxrwxr-x 4 sfmqrb sfmqrb  4096 Sep  4 12:50 sources
---
 62487 /home/sfmqrb/git/rishe/data/verification/page-56.json
 43914 /home/sfmqrb/git/rishe/data/verification/page-57.json
 59780 /home/sfmqrb/git/rishe/data/verification/page-58.json
 54555 /home/sfmqrb/git/rishe/data/verification/page-59.json
 52537 /home/sfmqrb/git/rishe/data/verification/page-60.json
 86233 /home/sfmqrb/git/rishe/data/verification/page-101.json
 75899 /home/sfmqrb/git/rishe/data/verification/page-126.json
 73989 /home/sfmqrb/git/rishe/data/verification/page-311.json
 81781 /home/sfmqrb/git/rishe/data/verification/page-345.json
591175 total
```


## [2026-09-04T23:05:28.290Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nfor p in [56,57,58,59,60,101,126,311,345]:\n    d=json.load(open(f'data/verification/page-{p}.json'))\n    n=0; nfa=0; e=0; efa=0\n    for en in d['entries']:\n        e+=1\n        if 'note_fa' in en: efa+=1\n        for nd in en['nodes']:\n            n+=1\n            if 'derivation_fa' in nd: nfa+=1\n    print(p, 'entries',e,'note_fa',efa,'nodes',n,'derivation_fa',nfa)\nEOF",
 "description": "Count nodes and existing fa fields"
}
```


## [2026-09-04T23:05:28.984Z] TOOL CALL #4: Bash

```json
{
 "command": "cat tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-04T23:05:30.376Z] TOOL RESULT

```
56 entries 1 note_fa 0 nodes 22 derivation_fa 0
57 entries 2 note_fa 0 nodes 11 derivation_fa 0
58 entries 2 note_fa 0 nodes 15 derivation_fa 0
59 entries 1 note_fa 0 nodes 18 derivation_fa 0
60 entries 2 note_fa 0 nodes 18 derivation_fa 0
101 entries 2 note_fa 0 nodes 22 derivation_fa 0
126 entries 1 note_fa 0 nodes 16 derivation_fa 0
311 entries 1 note_fa 0 nodes 20 derivation_fa 0
345 entries 2 note_fa 0 nodes 19 derivation_fa 0
```


### [2026-09-04T23:05:30.416Z] TOOL RESULT

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


## [2026-09-04T23:05:44.976Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-56.json'))\nprint('pdf',d.get('pdf_page'),'book',d.get('book_page'))\nfor en in d['entries']:\n    print('='*80)\n    print('ENTRY',en['entry'],'root:',en['root'],'|verdict:',en['verdict'],'|modern:',en.get('modern_form'))\n    print('NOTE:',en.get('note'))\n    print('ROOT refcheck:',json.dumps(en.get('ref_check'),ensure_ascii=False))\n    for n in en['nodes']:\n        print('-'*60)\n        print('#',n['id'],n.get('lang'),'|',n.get('words'),'| verdict:',n['verdict'])\n        for k in ('error_in','book_prints','correct_form'):\n            if k in n: print(' ',k,':',n[k])\n        print('DER:',n.get('derivation'))\n        print('REF:',json.dumps(n.get('ref_check'),ensure_ascii=False))\n        print('CON:',json.dumps(n.get('consulted'),ensure_ascii=False))\nEOF",
 "description": "Dump page 56 compactly"
}
```


### [2026-09-04T23:05:47.146Z] TOOL RESULT

```
<persisted-output>
Output too large (44.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b7iqprh1f.txt

Preview (first 2KB):
pdf 56 book 26
================================================================================
ENTRY 0 root: Ang, Ank, Anq |verdict: confirmed |modern: PIE *h₂enk- / *h₂eng- 'to bend, curve' (Pokorny '2. ank-, ang- „biegen“', IEW 45–47; Watkins/AHD 'ank-, also ang-. To bend')
NOTE: Root, language label and gloss are all correct and standard. Nourai's three-way root name 'Ang, Ank, Anq' is taken verbatim from Klein, who ends his 'angle (corner)' article (KLN p.75) with 'All these words derive fr. I.-E. base *ang-, resp. *anq-, “to bend”'. Pokorny's article runs IEW 45–47: the headword '2. ank-, ang- „biegen“; Nominalstämme anko-, onko-; ankes-; anku-lo-; anken-, -on-; ankoto-; ankro-' stands on p.45 (so Watkins cites '[Pok. 2. ank-, ang- 45]'), the sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen' with ai. áṅgam / aṅguṣṭha- = av. aṅgušta- and lat. angulus stands on p.46–47 — so POK:46 is a fair citation for the branches Nourai draws from it. Caveat for modern practice: laryngeal-era scholarship splits Pokorny's single lemma. Wiktionary keeps *h₂enk- 'curve, bend' (Skt. áñcati, Gk. ἄγκυρα, ἀγκὼν, Lat. ancus) apart from the 'limb/finger' family *h₂eng- (Skt. áṅga-, aṅguṣṭha-, Av. aṅgušta-, MP angust), and Mann (IEC) lists ang-, anghulos, anguos, ankotos, ankuros as separate lemmata, deriving Lat. angulus from *anghulos rather than *ank-. Nourai's single root box therefore merges two (probably but not certainly related) roots — the traditional Pokorny/Klein/Watkins position. Two whole limbs of the chart are, additionally, cultural loans rather than inherited descent (Gk. ἄγκυρα → Pers. langar; Skt. caturaṅga → Pahl. čatrang), which the chart's arrows do not distinguish; and the French→Persian limb (#20–#21) is wrong, see those nodes.
...
</persisted-output>
```


## [2026-09-04T23:05:57.886Z] TOOL CALL #6: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py <<'EOF'\nimport json,sys\ndef t(s,n=200):\n    s=s or ''\n    return s if len(s)<=n else s[:n]+'…'\nfor p in sys.argv[1:]:\n    d=json.load(open(f'data/verification/page-{p}.json'))\n    print('#'*90); print('PAGE',p,'book',d.get('book_page'))\n    for en in d['entries']:\n        print('='*80)\n        print('ENTRY',en['entry'],'| root:',en['root'],'| verdict:',en['verdict'],'| modern:',en.get('modern_form'))\n        print('NOTE:',t(en.get('note'),1400))\n        print('ROOTREF:',' ; '.join(f\"{r.get('ref')}={r.get('status')}\" for r in (en.get('ref_check') or [])))\n        for n in en['nodes']:\n            print('-'*60)\n            print('#',n['id'],n.get('lang'),'|',n.get('words'),'| verdict:',n['verdict'],\n                  '|', ' '.join(f\"{k}={n[k]}\" for k in ('error_in','book_prints','correct_form') if k in n))\n            print('DER:',t(n.get('derivation'),1200))\n            print('REF:',' ; '.join(f\"{r.get('ref')}={r.get('status')}: {t(r.get('note'),90)}\" for r in (n.get('ref_check') or [])))\n            print('CON:',' ; '.join(f\"{c.get('src')}={c.get('stance')}: {t(c.get('note'),90)}\" for c in (n.get('consulted') or [])))\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 56",
 "description": "Dump page 56 truncated"
}
```


### [2026-09-04T23:05:59.769Z] TOOL RESULT

```
##########################################################################################
PAGE 56 book 26
================================================================================
ENTRY 0 | root: Ang, Ank, Anq | verdict: confirmed | modern: PIE *h₂enk- / *h₂eng- 'to bend, curve' (Pokorny '2. ank-, ang- „biegen“', IEW 45–47; Watkins/AHD 'ank-, also ang-. To bend')
NOTE: Root, language label and gloss are all correct and standard. Nourai's three-way root name 'Ang, Ank, Anq' is taken verbatim from Klein, who ends his 'angle (corner)' article (KLN p.75) with 'All these words derive fr. I.-E. base *ang-, resp. *anq-, “to bend”'. Pokorny's article runs IEW 45–47: the headword '2. ank-, ang- „biegen“; Nominalstämme anko-, onko-; ankes-; anku-lo-; anken-, -on-; ankoto-; ankro-' stands on p.45 (so Watkins cites '[Pok. 2. ank-, ang- 45]'), the sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen' with ai. áṅgam / aṅguṣṭha- = av. aṅgušta- and lat. angulus stands on p.46–47 — so POK:46 is a fair citation for the branches Nourai draws from it. Caveat for modern practice: laryngeal-era scholarship splits Pokorny's single lemma. Wiktionary keeps *h₂enk- 'curve, bend' (Skt. áñcati, Gk. ἄγκυρα, ἀγκὼν, Lat. ancus) apart from the 'limb/finger' family *h₂eng- (Skt. áṅga-, aṅguṣṭha-, Av. aṅgušta-, MP angust), and Mann (IEC) lists ang-, anghulos, anguos, ankotos, ankuros as separate lemmata, deriving Lat. angulus from *anghulos rather than *ank-. Nourai's single root box therefore merges two (probably but not certainly related) roots — the traditional Pokorny/Klein/Watkins position. Two whole limbs of the chart are, additionally, cultural loans rather than inherited descent (Gk. ἄγκυρα → Pers. langar; Skt. caturaṅga → Pahl. čatrang), which the chart's arrows do…
ROOTREF: POK:46=supports
------------------------------------------------------------
# 1 Avestan | angušta | verdict: confirmed | 
DER: Avestan aṅgušta- m. 'toe' (Bartholomae AiW 106; the sense 'finger' only in compounds, Buck 4.34) is the exact match of Sanskrit aṅguṣṭha-ḥ 'thumb, big toe' — Indo-Iranian *Hanguštʰa- built on the 'limb' base *h₂eng-u- (Skt. aṅgúli- 'finger', áṅga- 'limb') with the -stʰ(a)- formant; Indo-Iranian *-stʰ- gives Av. -št- after u. Pokorny prints the equation 'ai. aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m. ‚Zehe‘' (IEW 46), which is the arrow Nourai draws from the root. The word is the everyday Iranian word for 'toe/finger' and is the ancestor of every form in nodes #2 and #3.
REF: KLN:75=supports: KLN_1966.txt leaf 51 (= printed pp.74–76; the page numeral '76' stands in the middle of th…
CON: POK=supports: 'aṅguṣṭha-ḥ ‚große Zehe, Daumen‘ == av. aṅgušta- m. ‚Zehe‘'. ; SYN=partial: 'Av. aṅgušta- (as “finger” only in cpds., otherwise “toe”)' — i.e. the primary Avestan sen… ; HRN=supports: 'aw. angusta- ‚Zehe‘; phlv. angust; skr. aṅguṣṭha- ‚Daumen, grosse Zehe‘'. ; ARY=supports: Aryanpur lists AVESTAN ANGUSHTA beside PAHLAVI ANGUST and SANSKRIT ANGULI/ANGA under the P…
------------------------------------------------------------
# 2 Persian | angošt «انگشت» | verdict: confirmed | 
DER: Old Iranian *angušta- (= Av. aṅgušta-) > Middle Persian angust [ʾNGWST'] 'finger, toe; a unit of length (¾ in.)' (MacKenzie PHD 10) > New Persian angušt / angošt انگشت. Nyberg notes the dialect detail: 'angust ... SW form with -st < -št; NP angušt NW form. Paz. both angust and angušt' — i.e. the standard NP -št is the North-Western (Parthian-type) treatment, the Book-Pahlavi -st the South-Western one, so NP angošt continues the Old Iranian cluster directly rather than the SW Middle Persian output. The derivatives on the chart are transparent NP formations: انگشتر angoštar 'finger-ring' (MP angustarīg, PHD 10), انگ ۱ ang 'mark/stamp made with the finger', انگلک / انگولک angolak 'poking with a finger'. Strictly, the arrow should hang NP angošt on Middle Persian, not directly on Avestan (Avestan is a sister, not the mother, of Persian).
REF: MON:392=not_checked: Mo'in's 6-vol. Farhang-e Farsi (Amir Kabir), vol. 1 p.392, is not on disk: the local MON_p…
CON: PHD=supports: 'angust [ʾNGWSTʹ | (N angušt)] finger, toe; unit of length (¾ in.). ~arīg [-lykʹ] finger r… ; NYB=supports: 'angust [ʾNGWSTʹ] finger 26¹¹, 29¹¹; a linear measure 93⁷⁴, — SW form with -st < -št; NP a… ; HRN=supports: 'engušt ‚Finger, Zehe‘; vergl. engusteri ‚Ring‘, enguštāne ‚Fingerhut‘ ... aw. angusta- ‚Z… ; HUB=supports: 'angust ‚Finger, Zehe‘ = zd. angušta-' (listed among np. -st/-št < idg. -st after i, u). ; MON=silent: definition only, no etymology in this edition.
------------------------------------------------------------
# 3 Sogdian | ʿngwšt | verdict: confirmed | 
DER: Sogdian ʾng(w)št / ʾnkwšt(h) 'finger' — written ʾṅgwšt in the Manichaean script and ʾnkwšt(h) in the Sogdian ('Buddhist') script, both /angušt/ — continues the same Old Iranian *angušta- as Persian angošt; Gharib's dictionary explicitly derives it from the Avestan word. The plural ʾnkwštyt and the compound pʾdʹy ʾngwšt 'toe' (lit. 'foot-finger') are attested in the Buddhist Sogdian Padmacintāmaṇi and Vimalakīrti texts.
REF: SOD:41=supports: Gharib, Sogdian Dictionary. SOD_pages.txt leaf 106 (printed p.41, cf. leaf 107 whose runni…
CON: SOD=supports: see ref_check; Gharib himself writes '©<Av. angusta'. ; POK=partial: Pokorny lists the Avestan and Indic forms but no Sogdian.
------------------------------------------------------------
# 4 Avestan | anku, aka; duž-aka | verdict: plausible | 
DER: Two Avestan words, one secure and one not. (a) aka- m. 'hook, peg' (AiW 359, also in aḵnah- 'rein') and anku- in the hapax anku-pəsəmna- 'adorning oneself with hooks/clasps' are the direct Iranian reflexes of *h₂enk-u- (= Gk. ἀγκὼν, Skt. aṅká-ḥ 'hook'); Pokorny prints both on IEW 45. That part is confirmed. (b) duždka- m. is attested only at Vidēvdād 13.2, where it is the abusive name that 'men of evil speech' (dužvacaŋhō) give the hedgehog (vaŋhāpara-, Bd. gloss xārpušt). Bartholomae's analysis *duž- 'bad' + aka- 'hook' = 'the one that has nasty hooks (spines)' is offered with an explicit '?' after 'Et.?', i.e. as a guess — which is exactly what Nourai's own NOTE says. Two further caveats: the animal is the HEDGEHOG (Igel), not the porcupine; and the first element duž- is the well-known Iranian pejorative prefix (☆ Dus), so if the etymology is right the word is a compound of two roots, only the second of which belongs on this chart.
REF: POK:45=supports: POK_01.txt, between the page markers '45' and '4G'(=46): 'av. anku-pəsəmna- ‚mit Haken, Sp… ; BRT:755=partial: BRT.txt, the spread headed '755 | duš.sravah- ... duzuxta- | 756': 'j. duzaka- m. (gemeine…
CON: BRT=partial: see ref_check. ; HRN=supports: 'žūže ‚Igel‘ ... aw. duzaka- ‚Igel‘ (als Schimpfname des Hundes verwandt); phlv. žūžak' — … ; PHD=partial: 'hedgehog xārpušt, xūkar(ag), zūzag' — the Pahlavi synonyms are all 'hedgehog'; MacKenzie'… ; SNS=supports: the Shayast-ne-Shayast glossary entry for zūzag cites '(AiW. 755) duzaka' — i.e. the same …
------------------------------------------------------------
# 5 Pahlavi | žužag, zuzag, jujag | verdict: confirmed | 
DER: Middle Persian zūzag / žūžag [zwzkʹ] 'hedgehog', from Avestan duždka- by assimilation of the two syllable-initial consonants: *dužaka- > *žužag (d…ž > ž…ž), which Bartholomae states in so many words ('Assimilation der silbenanl. Kons.'). MacKenzie normalises the Book Pahlavi spelling zwzkʹ as zūzag; Bartholomae and Horn read the Pahlavi translation's form as žūžak. Nourai's third variant 'jujag' reflects the Gilaki/dialect form (Horn cites g. jūjīk) and the ambiguity of Pahlavi <z> for /ž/. The gloss should be 'hedgehog'; 'porcupine' is a loose rendering of NP خارپشت.
REF: SNS:168=supports: Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast. The book's own index (SNS_pages.txt) reads 'zūzag … ; BQT:1063=partial: Borhan-e Qate' (Mo'in's ed.), BQT_v2_pages.txt leaf 525 (printed ≈ 1063–1068 on the stated…
CON: PHD=supports: 'zūzag [zwzkʹ | (N žūža)] hedgehog.' — the Pahlavi form and its New Persian outcome, exact… ; HRN=supports: 'aw. duzaka- ‚Igel‘ ...; phlv. žūžak; kurd. LW. ..., žūžī'. ; BRT=supports: 'mp. (Pü.): žūžak; np. žūža; Assimilation der silbenanl. Kons.' ; NYB=silent: no entry for zūzag/žūžag (Nyberg's glossary covers only the texts of Part I).
------------------------------------------------------------
# 6 Persian | žŭž «ژوژ» | verdict: confirmed | 
DER: MP zūzag/žūžag > NP ژوژه žūža by the regular loss of Middle Persian final -g (-ag > -a), with the shortened by-form ژوژ žūž; both are entered in Borhan-e Qate' and both are glossed خارپشت 'hedgehog'. The word survives dialectally as Gilaki jūjīk and was borrowed into Kurdish (žūžī). Nourai's gloss 'porcupine' should read 'hedgehog'.
REF: BRT:755=supports: AiW 755 s.v. duzaka-, closing line: 'mp. (Pü.): žūžak; np. žūža'. ; BQT:1063=supports: BQT_v2_pages.txt leaf 525 (printed ≈ 1063–1068): 'ژوژ ... خارپشت را گویند، وآن جانوری است …
CON: BQT=supports: see ref_check. ; HRN=supports: Horn lemmatises the New Persian word as žūže and derives it from Av. duzaka- via phlv. žūž… ; PHD=supports: '| (N žūža)'. ; MON=silent: no ژوژ entry in the abridgement on disk.
------------------------------------------------------------
# 7 Sogdian | ʿkšye | verdict: confirmed | 
DER: Sogdian ʾksyc / ʾxšyc 'hook' (Manichaean and Christian Sogdian, Henning, Sogdica 30.11a), read by Gharib as akaseč; Gharib derives it directly from Avestan aka- 'hook', i.e. from Nourai's node #4 rather than straight from the root as the chart draws it. Formally it is *aka- plus the diminutive/adjectival suffix -č (Sogd. -c), with the usual Sogdian -k- ~ -x- fluctuation before s. One caveat on the reading: the final letter is Sogdian <c>, not <e> — Nourai's 'ʿkšye' should be ʾkšyc/ʾksyc.
REF: SOD:32=supports: Gharib, entry '837 ʾksyc M, C — akaseč ? (ʾksyʾc) ©Av. aka- ⇒ ʾxšyc — hook — Hen. Sogdica.…
CON: SOD=supports: see ref_check. ; POK=supports: 'av. aka- m. ‚Haken, Zapfen‘' — the Avestan base of the Sogdian word, though Pokorny has n… ; BRT=supports: cited by Pokorny for Av. aka- 'Haken'; the Sogdian is not in Bartholomae.
------------------------------------------------------------
# 8 Greek | ankura | verdict: confirmed | 
DER: Ancient Greek ἄγκῦρα (ánkūra) f. 'anchor', from *h₂enk- 'bend' with the -ūra suffix, beside ἀγκὼν 'elbow, bend', ἀγκύλος 'crooked', ἄγκιστρον 'fish-hook' — the anchor named from its hooks/flukes. Attested from Homeric times onward; the place-name Ἄγκυρα (Ancyra, mod. Ankara) is the same word. Nourai's transliteration 'ankura' is a bare Latinisation of the Greek nominative.
REF: AHD=supports: Watkins s.v. ank-: 'III. Greek ankura, anchor: ANCHOR. ... [Pok. 2. ank-, ang- 45.]' — the…
CON: POK=supports: 'ἀγκύλη ‚Riemen‘ (= anord. ól, ál ds.), ἄγκυρα ‚Anker‘, ἀγκάλη ‚Ellenbogen, Bucht, alles G… ; KLN=supports: lists 'ἄγκυρα “anchor”' among the *ang-/*anq- family; and p.72 s.v. anchor: 'fr. Gk. ἄγκυρ… ; SKT=supports: 'Anchor. (L.–Gk.) ... A.S. ancor' — Latin from Greek.
------------------------------------------------------------
# 9 Persian | langar «لنگر» | verdict: confirmed | 
DER: A Mediterranean culture-word, not an inherited Iranian form: Gk. ἄγκυρα > Lat. ancora, whence Aramaic/Mandaic angarā and thence Middle/New Persian لنگر langar. The l- is the usual Aramaic-mediated treatment of the initial vowel + nasal (cf. the same l-/n- alternation in the Arabic reflex), and the Persian word was in turn Arabicised as أنجر ʾanjar and re-exported to Ottoman Turkish lenger, Uzbek/Turkmen langar, Gujarati, Kazakh, and Mandarin 蘭干. Mo'in's own footnote to the Borhan entry states the borrowing outright. The chart's single arrow Greek → Persian is therefore right in substance but skips the Latin/Aramaic relay. A minority view on Wiktionary keeps an alternative 'of Iranian origin, cognate with Sanskrit लङ्गल (laṅgala)', but Taqizadeh, Mo'in and Asbaghi all take the Greek/Latin route.
REF: BQT:1908=supports: Fetched with tools/ref_page.py BQT:1908 (BQT vol.3 pdf p.705). The page is the لنگر entry …
CON: PLA=supports: 'أنجر – ‚Anker‘ pers. ... aus pers. لنگر langar, mand. angara ← lat. ancora.' — the Latin→… ; RCH=supports: 'p langar, An anchor. A stay or rope for supporting a tent. ... langar andakhtan (or langa… ; LKT=silent: Lokotsch treats only Oriental words that entered European languages; langar is not among t… ; MON=silent: no etymological note in the abridgement.
------------------------------------------------------------
# 10 English | anchor | verdict: confirmed | 
DER: Gk. ἄγκυρα > Lat. ancora (a very early Latin borrowing) > Old English ancor/ancra (borrowed with the ships and the Church) > Middle English anker > anchor; the unetymological -ch- is a late-16c. pedantic spelling based on a corrupt Latin spelling anchora, and the pronunciation stayed /k/. Sense 'presenter of a broadcast' from anchorman, 1903/1965.
REF: AHD=supports: Watkins s.v. ank-: 'III. Greek ankura, anchor: ANCHOR.'
CON: KLN=supports: 'anchor, n. — ME. anker, fr. OE. ancor, fr. L. ancora, fr. Gk. ἄγκυρα “anchor”, which is r… ; SKT=supports: 'Anchor. (L.–Gk.) Better spelt without the h. M.E. anker. A.S. ancor.' ; AHD=supports: as ref_check.
------------------------------------------------------------
# 11 Sanskrit | angam; catur-anga | verdict: confirmed | 
DER: Sanskrit áṅga- n. 'limb, member, part of the body' (< *h₂eng-, the 'limb' branch of Pokorny's ank-/ang-), and the bahuvrīhi catur-aṅga- 'having four limbs/members' (catúr 'four', ☆ Kwetwer). In its original military sense caturaṅga- names the four arms of the Indian army — elephants, chariots, cavalry and infantry (Rigveda 10.92.11 already has catúraṅga-) — and it is from that army metaphor that the 6th-c. board game takes its name, its four pieces being precisely elephant (→ bishop), chariot/rook (→ castle), horse (→ knight) and foot-soldier (→ pawn). Nourai's gloss 'the four parts (castle, Knight, Bishop and Pawn)' therefore names the chess pieces rather than the literal 'four limbs' — the same shortcut Mo'in takes in his Borhan footnote ('شامل چهار جزء: فیل، رخ، اسب، پیاده').
REF: POK:46=supports: IEW 46, sub-article 'ang-, bes. zur Bezeichnung von Gliedmaßen': 'Ai. áṅgam ‚Glied‘, aṅgūl… ; BQT:1254=supports: BQT vol.3, pdf p.45 = printed 1254 (the page numeral '۱۲۵۴' is visible at the foot). Mo'in…
CON: SYN=supports: 'Skt. aṅga- “limb” ... prob. as “crooked” : Lat. angulus “corner”, Walde-P. 1.61.' ; IEC=partial: 'anguos, om, ā (?) “limb; gait” ... Skt. (ambig.) ángam' — Mann accepts the form but marks… ; AHD=supports: 'V. Sanskrit anka, hook, ancati, he bends: PALANQUIN.' ; HJB=silent: Yule has no caturaṅga article.
------------------------------------------------------------
# 12 Pahlavi | catrang | verdict: confirmed | 
DER: Middle Persian čatrang [cʾtʾlʾng], borrowed from Sanskrit caturaṅga- with loss of the unstressed medial -u- (*čaturaṅg > čatrang) and the regular Iranian rendering of Indic -aṅga as -ang; Indic c- = MP č-. It is the title-word of the Pahlavi tract Wīzārišn ī čatrang ud nihišn ī nēw-ardaхšīr ('The Explanation of Chess and the Invention of Backgammon'), which stages the game's arrival from India at Khosrow I's court — the story Borhan-e Qate' repeats. MacKenzie lemmatises it and already flags the Arabic outcome.
REF: None=not_checked: Nourai gives no reference on this node; the claim is however carried by the reference on i…
CON: PHD=supports: 'čatrang [cʾtʾlʾng | (Ar. šatranj)] chess.' ; PLA=supports: 'شطرنج šaṭranj: ‚Schachspiel‘ ... pers. šatrang, mp. čatrang, skr. caturanga.' ; BQT=supports: see node #11 ref_check. ; NYB=silent: the word is not in Nyberg's text-glossary.
------------------------------------------------------------
# 13 Persian | šatrang «شترنگ» | verdict: transcription_suspect | 
DER: The word itself and the chain are certain: MP čatrang > Classical NP چترنگ čatrang / شترنگ šatrang 'chess', Arabicised as شطرنج šaṭranj (Arabic has no /č/, so چ is rendered ش, and the t is written ط by attraction to the emphatic environment), and then re-borrowed into New Persian in that Arabic dress — a Persian→Arabic→Persian round trip. Asadi's Loġat-e Fors p.289 already has Nourai's shahid verse ('تا جز از بیست و چهارش نبود خانهٔ نرد / همچو در سی و دو خانه است نهادش شترنگ'), which Borhan quotes on the very page Nourai cites. What is suspect is the first of the two variants printed in the box, «کترنگ»: *katrang is not a Persian word, and ک vs چ differ only by the three dots — the book must be printing (or the scan misreading) چترنگ čatrang, the direct continuation of the Pahlavi form in node #12 and the form given by Mo'in, MacKenzie and Asbaghi. The second variant شطرنج is correct.
REF: BQT:1254=supports: BQT vol.3 pdf p.45 = printed 1254: headword 'شترنگ «با کاف فارسی» ... بمعنی شطرنج است، و آ… ; FVF:404=not_checked: Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi — no copy on disk and the noo…
CON: PLA=supports: 'šaṭranj: ‚Schachspiel‘ ... pers. šatrang, mp. čatrang, skr. caturanga' — note that Asbagh… ; AFM=supports: quoting Borhan-e Qate': '... والشطرنج معرب شترنك' — šaṭranj is the Arabicised šatrang. ; PHD=supports: 'čatrang ... | (Ar. šatranj)] chess'. ; FRS=silent: the headword could not be located in the OCR text, but Borhan cites it as لغت فرس ۲۸۹ for …
------------------------------------------------------------
# 14 Sanskrit | ancati; pari-ancati; pary-anka, palyanka | verdict: confirmed | 
DER: Skt. áñcati / (zero-grade) ácati 'bends, curves' is the primary verb of *h₂enk- (Pokorny prints 'Ai. ancati (mpers. ancītan) und (tiefstufig) acati ‚biegt, krümmt‘' on IEW 45), with aṅká-ḥ 'bend, hook, the hollow between chest and hip, lap' beside it. Compounded with pári 'around' (☆ Per 1) it gives pary-aṅka- ~ paly-aṅka- m. 'couch, bed, litter' — literally 'that which bends/curves around (the body)'; the ry ~ ly variation is the familiar Indic r/l fluctuation, and it is the l-form that all the borrowed words descend from (Pali pallaṅko, Prakrit pallaṅka). Nourai's gloss 'a bed carried on poles on the shoulder of two or four men … due to the sagging cloth bottom' is his own rationalisation of the palanquin sense; the standard analysis is 'bending around'.
REF: AHD:943=not_checked: AHD:943 is a page of the main 1975 New College dictionary (the 'palanquin' entry), and onl… ; OEW:14=not_checked: Shipley, The Origins of English Words (1984) is lending-only on archive.org and not on dis…
CON: POK=supports: 'Ai. ancati (mpers. ancītan) und (tiefstufig) acati ‚biegt, krümmt‘, Partiz. -akna-, -akta… ; AHD=supports: see ref_check. ; HJB=supports: 'The basis of all the forms is Skt. paryanka, or palyanka, “a bed”, from which we have Hin… ; AID=silent: no headword palanquin/paryanka; the word appears only in caste descriptions ('palanquin-be…
------------------------------------------------------------
# 15 English | palanquin, palankee | verdict: plausible | 
DER: The two ends of the chain are right but the chart's single Sanskrit→English arrow leaves out the actual carriers. Skt. paly-aṅka- > Pali pallaṅko / Prakrit pallaṅka > Javanese and Malay palangki 'litter, sedan' (the Indian Ocean trade term) > Portuguese palanquim (early 16c.; the nasal -m is a standard Portuguese addition, as in mandarim, Bagaim) > English palanquin, first attested in the 1580s. The Anglo-Indian by-form palankeen/palankee comes instead from the Hindi pālkī (< Prakrit pallaṅkī), the light litter itself. Verdict 'plausible' rather than 'confirmed' only because Nourai's arrow suppresses the Prakrit–Malay–Portuguese relay that every source insists on.
REF: AHD=supports: Watkins s.v. ank-: 'V. Sanskrit anka, hook, ancati, he bends: PALANQUIN'; and the index li… ; OEW:14=not_checked: Shipley not on disk (lending-only).
CON: HJB=partial: 'The origin of the word is not doubtful, though it is by no means clear how the Portuguese… ; KLN=supports: Klein likewise routes it Portuguese palanquim < Javanese/Malay palangki < Skt. palyanka-. ; AID=silent: no etymological entry.
------------------------------------------------------------
# 16 Latin | angulus | verdict: confirmed | 
DER: Latin angulus m. 'corner, angle' (Ernout–Meillet: 'coin [d'un édifice], angle (γωνία). Ancien, technique, usuel'), from *ang-olo-, a diminutive-looking -lo- derivative of the same 'bend' base; exact cognates OCS ǫg˕l˕ 'corner' and Armenian angiwn/ankiwn 'corner', with the o-grade beside it in Lat. uncus 'hook'. Derivatives angulāris, angulātus, and the numeral compounds tri-, quadri-, rect-angulus that give English triangle and rectangle. (Mann, alone, sets it up as *anghulos with a voiced aspirate, so the exact root shape is not universally agreed.)
REF: AHD=supports: Watkins s.v. ank-: 'VII. Suffixed form *ang-olo- in Latin angulus, angle, corner: ANGLE.' ; KLN=supports: KLN p.75 s.v. angle, n., corner: 'F., fr. L. angulus, “angle, corner”, which is cogn. with…
CON: POK=supports: 'auch lat. angulus (womit aksl. ǫg˕l˕ ‚Winkel‘ urverwandt ist) ‚Winkel‘ (daneben mit o-Stu… ; LAT=supports: 'angulus, -ī (anglus dans l'app. Probi) m.: coin [d'un édifice], angle (γωνία). — Ancien, … ; IEC=partial: 'anghulos, anghlos, is “angle, corner”. WP I, 61. Cf. ank-, onk-, ōnk- ... Lat. angulus; U… ; LEW=silent: the entry could not be located in the OCR of the 1910 edition on disk.
------------------------------------------------------------
# 17 English | angle, rectangle, triangle | verdict: confirmed | 
DER: All three are learned Latin-via-French borrowings, not native words: L. angulus > Old French/French angle > Middle English angle (14c.) 'corner, angle'; L. tri-angulum > OF triangle > ME triangle; Late L. rect-angulum ('right-angled figure') > F rectangle > E rectangle (16c.). Klein and Skeat both label the English word '(F.–L.)'. Note that the homonym angle 'fish-hook, to fish' is NOT from Latin but the inherited Old English angel (same root, native line) — Nourai rightly keeps it off this branch, though it is the very word that node #18 depends on.
REF: None=not_checked: Nourai gives no reference on this node; the parent node's AHD and KLN cover it.
CON: KLN=supports: 'angle, n., corner. — F., fr. L. angulus ... Cp. angle, “fishhook”, Angle, anchor, ancon, … ; SKT=supports: 'Angle (1), a corner. (F.–L.) M.E. ...' beside 'Angle (2), a hook, fish-hook. (E.) A.S. an… ; AHD=supports: 'Latin angulus, angle, corner: ANGLE.'
------------------------------------------------------------
# 18 Germanic | Angul | verdict: plausible | 
DER: Angul (Old English Angel, Ongel; modern German Angeln, Danish Angel) is the small district on the east coast of the Jutland/Schleswig peninsula between the Schlei and Flensburg fjords, from which the Angles are said to have come. The traditional etymology, going back to Rudolf Much, identifies the name with Gmc *angul- 'fish-hook, angle' (OE angel, ON ǫngull, OHG angul) < *h₂enk-ulo-, i.e. 'the hook-shaped land' — which is exactly Nourai's gloss. It is a good but not a proven etymology: Pokorny reports it as Much's suggestion and objects that it requires 'eine sonst nicht belegte Bed. ‚Winkel; Bucht‘', and Watkins hedges with 'probably'. The language label 'Germanic' is also loose — the name is attested in Latin (Anglii, Tacitus Germania 40) and Old English/Old Norse, not in a reconstructed Proto-Germanic source.
REF: AHD=partial: Watkins s.v. ank-, II.1: 'Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANG… ; OEW:14=not_checked: Shipley not on disk (lending-only on archive.org).
CON: POK=partial: 'Much stellt hierher den lat.-germ. VN Anglii, ags. Angel, Ongel als ‚Anwohner der Holstei… ; KLN=supports: 'L. Anglus, pl. Angli, of Teut. origin. Cp. OE. Angle, Engle, prop. “the people coming fro… ; SKT=supports: 'Angle (2), a hook, fish-hook. (E.) A.S. angel, a fish hook' — the appellative behind the …
------------------------------------------------------------
# 19 Old English | Engle, Angle | verdict: confirmed | 
DER: Old English Engle / Angle (nom. pl.) 'the Angles', Latin Anglī, the Germanic people who, with the Saxons and Jutes, crossed to Britain in the mid-5th century (Bede's traditional date for the adventus Saxonum is 449; Nourai's 'around 450 AD' is the standard rounding). The i-umlaut of a > e before the following i/j of the tribal stem gives Engle beside Angle. From it: Engla land (gen. pl. 'land of the Angles') > England, and Englisc > English; the word first denoted the people, only in late Old English the country — Canute was the first king to style himself 'King of England'. Nourai's parenthesis 'Engle-Land' should be Engla land.
REF: KLN:522=supports: KLN_1966.txt leaf 284 (which carries the page numerals 522 and 523), s.v. English: 'Englis… ; AWH1:129=not_checked: AWH = H. Kinder & W. Hilgemann, Atlas of World History (Anchor Books 1974), vol. 1 p.129 —…
CON: KLN=supports: see ref_check. ; AHD=supports: 'probably Latin Angli, the Angles'. ; FSD=silent: no separate etymological article located in the OCR.
------------------------------------------------------------
# 20 French | angle- | verdict: disputed | 
DER: There is no French form 'angle-' meaning 'English' and no French link in this chain. French for 'English' is anglais, from Middle/Old French anglois, from Latin Anglus / Late Latin Anglenses — i.e. from the LATIN form of the tribal name (Tacitus's Anglii, Bede's Angli), not from Old English Engle as the chart's arrow claims; Latin took the name from Germanic independently of Old English. The French word angle is a different lexeme altogether: 'corner', from Latin angulus, which is Nourai's own node #16. The node therefore conflates two homographs and inserts an intermediary that no source supports; and its child, Persian انگلیس, is not derived from French anyway (see #21).
REF: None=not_checked: no reference given by Nourai on this node.
CON: KLN=contradicts: Klein routes all the 'English' words through Latin, not French: 'Anglican — ML. Anglicanus… ; LAT=contradicts: 'angulus ... coin [d'un édifice], angle' — the source of French angle is the Latin word fo…
------------------------------------------------------------
# 21 Persian | Engelîs «انگلیس» | verdict: disputed | 
DER: Persian انگلیس is a modern European loan, but the accepted source is Italian inglese, most probably relayed through Ottoman Turkish انگلیز ingiliz — the Levantine-trade route by which most early-modern European ethnonyms reached Persian — not the French route Nourai draws (and certainly not from any French 'angle-'). The final -s of انگلیس matches Italian -se, not French -ais /ɛ/; انگلیسی englisi is the ordinary Persian nisba of it, and انگلستان englestān is an internal Persian -stān formation ('land of the English'), not a borrowing at all. The ultimate origin in Latin Anglus < the Germanic tribal name is of course correct; it is the immediate donor language that is wrong.
REF: MON=not_found: Nourai cites Mo'in without a page. Mo'in's انگلیس article, both in the 2-vol. text on disk…
CON: MON=silent: definition only; no etymology. ; LKT=silent: Lokotsch covers Oriental words in European languages, not the reverse; nothing on ingiliz.
------------------------------------------------------------
# 22 English | English, England, Anglo-, Anglo-Saxon | verdict: confirmed | 
DER: OE Englisc (adj. to Engle) > English; OE Engla land 'land of the Angles' > Engleland > England (the modern In- pronunciation is a later shift, probably by analogy with the many -ing- words); Anglo- is a combining form taken from Late Latin Anglī 'the English'; Anglo-Saxon comes from Medieval Latin Anglo-Saxones, earlier Anglī Saxones 'the English Saxons' — as Klein notes, tautological in later use since by Late Latin both elements had come to mean 'the English'.
REF: None=not_checked: no reference given by Nourai; the parent node's KLN:522 covers 'English'.
CON: KLN=supports: 'Anglo-, combining form meaning “English”. — Fr. Late L. Angli, “the English”. See Angle, … ; AHD=supports: 'probably Latin Angli, the Angles: ANGLE.' ; SKT=partial: Skeat connects the tribal name to the fish-hook word but gives no separate England article…
```


## [2026-09-04T23:06:12.363Z] TOOL CALL #7: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py <<'EOF'\nimport json,sys,collections\npage=sys.argv[1]; patch=json.load(open(sys.argv[2]))\npath=f'/home/sfmqrb/git/rishe/data/verification/page-{page}.json'\nd=json.load(open(path),object_pairs_hook=collections.OrderedDict)\ndef ins(od,after,key,val):\n    new=collections.OrderedDict()\n    placed=False\n    for k,v in od.items():\n        new[k]=v\n        if k==after:\n            new[key]=val; placed=True\n    if not placed: new[key]=val\n    od.clear(); od.update(new)\nmiss=[]\nfor en in d['entries']:\n    ei=str(en['entry'])\n    if ei not in patch['entry']: miss.append('entry '+ei)\n    else: ins(en,'note','note_fa',patch['entry'][ei])\n    np=patch['nodes'].get(ei,{})\n    for n in en['nodes']:\n        nid=str(n['id'])\n        if nid not in np: miss.append(f'entry {ei} node {nid}')\n        else: ins(n,'derivation','derivation_fa',np[nid])\nif miss:\n    print('MISSING:',miss); sys.exit(1)\njson.dump(d,open(path,'w'),ensure_ascii=False,indent=2)\nopen(path,'a').write('\\n')\nprint('ok',page)\nEOF\necho written",
 "description": "Write apply helper"
}
```


### [2026-09-04T23:06:12.402Z] TOOL RESULT

```
written
```


## [2026-09-04T23:06:15.803Z] TOOL CALL #8: Bash

```json
{
 "command": "head -c 600 /home/sfmqrb/git/rishe/data/verification/page-56.json; echo; echo ---; tail -c 200 /home/sfmqrb/git/rishe/data/verification/page-56.json | cat -A | tail -3",
 "description": "Check formatting"
}
```


### [2026-09-04T23:06:15.857Z] TOOL RESULT

```
{
  "pdf_page": 56,
  "book_page": 26,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Ang, Ank, Anq",
      "verdict": "confirmed",
      "modern_form": "PIE *h₂enk- / *h₂eng- 'to bend, curve' (Pokorny '2. ank-, ang- „biegen“', IEW 45–47; Watkins/AHD 'ank-, also ang-. To bend')",
      "note": "Root, language label and gloss are all correct and standard. Nourai's three-way root name 'Ang, Ank, Anq' is taken verbatim from Klein, who ends his 'angle (corner)' article (KLN p.75) with 'All these words derive fr. I
---
    }$
  ]$
}$
```


## [2026-09-04T23:06:19.635Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json,collections\np='data/verification/page-56.json'\nd=json.load(open(p),object_pairs_hook=collections.OrderedDict)\ns=json.dumps(d,ensure_ascii=False,indent=2)+'\\n'\nprint(s==open(p).read())\n\"",
 "description": "Test roundtrip fidelity"
}
```


### [2026-09-04T23:06:21.427Z] TOOL RESULT

```
True
```


## [2026-09-04T23:06:32.482Z] TOOL CALL #10: Bash

```json
{
 "command": "python3 -c \"\nimport json\nfor p in [56,57,58,59,60,101,126,311,345]:\n    d=json.load(open(f'data/verification/page-{p}.json'))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if n['verdict']=='transcription_suspect' or 'error_in' in n:\n                print(p,e['entry'],n['id'],n.get('words'),'|',n.get('error_in'),'|',n.get('book_prints'),'|',n.get('correct_form'))\n\"",
 "description": "List transcription_suspect nodes"
}
```


### [2026-09-04T23:06:34.512Z] TOOL RESULT

```
56 0 13 šatrang «شترنگ» | None | None | None
101 1 4 smaraldos | book | smaraldos : a shiny stone, emerald | smaragdos
126 0 1 didâ, děğa-vâra | book | didâ, děğa-vâra : clay wall | didâ, děğa-vâra (= Horn's Old Persian *deghavāra-)
311 0 13 hava-rd | book | hava-rd : well grown, well built, beautiful ☞ Su 1 | hu-raoda (Av. huraoδa-)
```


## [2026-09-04T23:09:52.859Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p56.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشهٔ این نمودار، که نورایی به سه صورت Ang, Ank, Anq آورده، همان *h₂enk-/*h₂eng- هندواروپایی آغازین به معنی «خمیدن، کج شدن» است؛ نام سه‌گانه را از کلاین گرفته و پوکورنی نیز آن را در صفحات ۴۵ تا ۴۷ زیر «۲. ank-, ang- „biegen“» آورده است، پس نام ریشه، برچسب زبانی و معنای آن هر سه درست است. با این همه، در ریشه‌شناسی امروزی که حنجری‌ها را به حساب می‌آورد این مدخل واحد به دو ریشه بخش می‌شود: *h₂enk- «خمیدن» (سنسکریت áñcati، یونانی ἄγκυρα) و *h₂eng- «اندام، انگشت» (سنسکریت áṅga-، اوستایی aṅgušta-، فارسی میانه angust)؛ نورایی به پیروی از سنت پوکورنی و کلاین این دو را یکی گرفته است. افزون بر این، دو شاخهٔ نمودار در حقیقت وام‌واژه‌اند نه میراث مشترک — «لنگر» از یونانی ἄγκυρα از راه لاتینی/آرامی، و «چترنگ» از سنسکریت caturaṅga — و پیکان‌های کتاب این تفاوت را نشان نمی‌دهد؛ شاخهٔ فرانسوی‌ـ‌فارسی (گره‌های ۲۰ و ۲۱) نیز نادرست است.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"اوستایی aṅgušta- «انگشتِ پا» (بارتولومه، فرهنگ ایرانی باستان، ص ۱۰۶) برابر دقیق سنسکریت aṅguṣṭha- «شست، انگشت بزرگِ پا» است و هر دو از هندوایرانی *Hanguštʰa- برساخته بر ستاک *h₂eng-u- «اندام» با پسوند -stʰa- می‌آیند؛ خوشهٔ هندوایرانی *-stʰ- پس از u در اوستایی به -št- بدل شده است. پوکورنی همین برابریِ سنسکریت و اوستایی را در صفحهٔ ۴۶ چاپ کرده، پس پیکانی که نورایی از ریشه به این گره کشیده درست است. تنها نکتهٔ ظریف آنکه معنای اصلی واژه در اوستا «انگشت پا» است و معنی «انگشت دست» جز در ترکیبات دیده نمی‌شود.\",\n\"2\": \"«انگشت» فارسی نو دنبالهٔ ایرانی باستان *angušta- (همان aṅgušta- اوستایی) است که در فارسی میانه angust [ʾNGWST'] «انگشت؛ واحد درازا» شده (مکنزی، ص ۱۰) و از آنجا به فارسی دری رسیده است. نیبرگ نکته‌ای گویشی می‌افزاید: صورت -st در پهلوی کتابی جنوب‌غربی است و -št فارسی نو صورت شمال‌غربی (پارتی‌گونه)، یعنی «انگشت» امروزی خوشهٔ ایرانی باستان را بی‌واسطه نگاه داشته است. مشتقات نمودار همه ساخت‌های درون‌فارسی‌اند: انگشتر (فارسی میانه angustarīg)، انگ و انگولک. ادعای نورایی درست است، جز آنکه پیکان می‌بایست «انگشت» را به فارسی میانه ببندد نه یکراست به اوستایی، چون اوستایی خواهرِ فارسی است نه مادر آن.\",\n\"3\": \"سغدی ʾnkwšt(h) / ʾngwšt «انگشت» — به خط سغدی ʾnkwšt(h) و به خط مانوی ʾngwšt، هر دو خوانای /angušt/ — همان ایرانی باستان *angušta- را ادامه می‌دهد که «انگشت» فارسی نیز از آن است؛ قریب در فرهنگ سغدی خود آن را صریحاً از aṅgušta- اوستایی می‌گیرد. صورت جمع ʾnkwštyt و ترکیب pʾdʹy ʾngwšt «انگشت پا» در متون بودایی سغدی گواه است. ادعای نورایی در این گره درست است.\",\n\"4\": \"این گره دو واژهٔ اوستایی را کنار هم نهاده که یکی استوار است و دیگری نه. نخست aka- «قلاب، چنگک» (بارتولومه ۳۵۹) و anku- در anku-pəsəmna-، که بازتاب مستقیم *h₂enk-u- هندواروپایی‌اند (هم‌ریشه با یونانی ἀγκὼν و سنسکریت aṅká-)؛ پوکورنی هر دو را در صفحهٔ ۴۵ آورده و این بخش پذیرفتنی است. اما duždka-/duzaka- تنها یک بار در وندیداد ۱۳٫۲ آمده، آن هم به عنوان نام دشنام‌آمیزِ خارپشت در زبان «بدگویان»، و تحلیل بارتولومه (duž- «بد» + aka- «قلاب/خار») خود با علامت پرسش همراه است؛ پس این پیوند در حد گمان می‌ماند. دو تذکر: جانور مورد نظر خارپشت است نه تشی، و جزء نخست پیشوند تحقیرِ شناختهٔ ایرانی duš-/duž- است که به این ریشه ربطی ندارد.\",\n\"5\": \"فارسی میانه zūzag / žūžag [zwzkʹ] «خارپشت» از duzaka- اوستایی با همگونی دو همخوان آغازِ هجا پدید آمده است: *dužaka- > *žužag (د…ژ ← ژ…ژ)، و بارتولومه نیز همین را با عبارت «همگونی همخوان‌های آغازِ هجا» بیان کرده است. مکنزی املای پهلوی zwzkʹ را zūzag می‌خواند، حال آنکه بارتولومه و هرن صورت ترجمهٔ پهلوی را žūžak ضبط کرده‌اند؛ صورت سوم نورایی، jujag، بازتاب گونهٔ گیلکی جوجیک و ابهام حرف <z> پهلوی برای /ž/ است. ادعای نورایی درست است، جز آنکه معنی دقیق «خارپشت» است و «تشی» ترجمهٔ آزادِ خارپشت شمرده می‌شود.\",\n\"6\": \"«ژوژه» فارسی نو از فارسی میانه žūžag با افتادن قاعده‌مندِ -g پایانی (ag- > ه) پدید آمده و گونهٔ کوتاه‌شدهٔ «ژوژ» نیز در کنار آن به کار رفته است؛ برهان قاطع هر دو را با معنی «خارپشت» ثبت کرده است. واژه در گویش گیلکی به صورت جوجیک زنده مانده و به کردی (žūžī) نیز وام داده شده است. ادعای نورایی درست است و تنها معادل انگلیسی او («porcupine») باید «hedgehog» یعنی خارپشت باشد.\",\n\"7\": \"سغدی ʾksyc / ʾxšyc «قلاب» (در متون مانوی و مسیحی سغدی)، که قریب آن را akaseč می‌خواند و صریحاً از aka- اوستایی می‌گیرد؛ یعنی این واژه به گرهٔ ۴ می‌پیوندد نه یکراست به ریشه، چنان‌که نمودار کشیده است. از نظر ساخت، *aka- است به‌علاوهٔ پسوند تصغیر/نسبتِ سغدی -č، با نوسان معمول k ~ x پیش از s. یک تصحیح خوانشی: واج پایانی حرف <c> سغدی است نه <e>، پس ضبط نورایی «ʿkšye» باید ʾkšyc باشد.\",\n\"8\": \"یونانی باستان ἄγκῡρα (ánkūra) «لنگر» از همان ریشهٔ *h₂enk- «خمیدن» با پسوند -ūra ساخته شده و در کنار ἀγκὼν «آرنج، خمِ دست»، ἀγκύλος «کج» و ἄγκιστρον «قلاب ماهیگیری» می‌ایستد؛ لنگر را به مناسبت چنگک‌هایش چنین نامیده‌اند. واژه از عهد هومر به بعد گواه دارد و نام شهر Ἄγκυρα (آنکارا) نیز همین کلمه است. ادعای نورایی درست است و ضبط «ankura» صرفاً لاتین‌نویسیِ حالت فاعلی یونانی است.\",\n\"9\": \"«لنگر» واژه‌ای فرهنگی و مدیترانه‌ای است نه میراث ایرانی: یونانی ἄγκυρα به لاتینی ancora رفته، از آنجا در آرامی/مندایی angarā بازتاب یافته و از این راه به فارسی میانه و فارسی نو به صورت «لنگر» رسیده است؛ ل آغازین نتیجهٔ همان میانجی‌گری آرامی است. همین واژهٔ فارسی سپس در عربی به «أنجر» معرّب شده و به ترکی عثمانی (lenger)، ازبکی، ترکمنی و حتی چینی راه یافته است. معین در حاشیهٔ برهان قاطع نیز به همین وام‌گیری تصریح می‌کند و اصباغی آن را تأیید می‌کند؛ پس پیکان «یونانی ← فارسی» در اصل درست است، اما حلقهٔ لاتینی و آرامی را نادیده گرفته است. رأی اقلیتی که «لنگر» را ایرانی و هم‌ریشهٔ سنسکریت laṅgala می‌داند پذیرفته نشده است.\",\n\"10\": \"یونانی ἄγκυρα در دورانی کهن به لاتینی ancora وام داده شد، از آنجا به انگلیسی باستان ancor/ancra (همراه با کشتیرانی و کلیسا) رسید و از راه انگلیسی میانه anker به صورت امروزی anchor درآمد. حرف -ch- در املا ریشه‌شناختی نیست، بلکه افزودهٔ فاضل‌نمایانهٔ سدهٔ شانزدهم بر پایهٔ املای مغلوط لاتینی anchora است و تلفظ همچنان /k/ مانده است. معنی «مجریِ خبر» از anchorman سدهٔ بیستم برخاسته است. ادعای نورایی درست است.\",\n\"11\": \"سنسکریت áṅga- «اندام، عضو» از شاخهٔ «اندام»ِ همین ریشه است و ترکیب بهووریهیِ catur-aṅga- «دارای چهار اندام/رکن» از catúr «چهار» ساخته شده است. معنای نخستِ آن چهار رکن سپاه هند است — پیل، ارابه، سواره و پیاده — و بازیِ سدهٔ ششم میلادی نام خود را از همین استعارهٔ لشکری گرفته، چون مهره‌هایش نیز همان چهارند. توضیح نورایی که آن را «چهار جزء: رخ، اسب، فیل و پیاده» می‌خواند در واقع نام مهره‌هاست نه معنای تحت‌اللفظی واژه؛ همان اختصاری که معین نیز در حاشیهٔ برهان به کار برده است. اصل ادعا درست است.\",\n\"12\": \"فارسی میانه čatrang [cʾtʾlʾng] وام‌واژه‌ای است از سنسکریت caturaṅga- با افتادن -u- بی‌تکیهٔ میانی (*čaturaṅg > čatrang) و بازتاب قاعده‌مند aṅga- هندی به -ang ایرانی؛ c هندی نیز در فارسی میانه چ می‌شود. این واژه عنوان رسالهٔ پهلوی «ویزارشن ی چترنگ اُد نهشن ی نیو-اردخشیر» است که داستان آمدن بازی از هند به دربار خسرو انوشیروان را می‌آورد — همان روایتی که برهان قاطع تکرار کرده است. مکنزی نیز مدخل čatrang را با اشاره به معرّبِ «شطرنج» آورده است؛ ادعای نورایی درست است.\",\n\"13\": \"زنجیرهٔ واژه بی‌گمان است: فارسی میانه čatrang > فارسی دری «چترنگ / شترنگ» > معرّبِ «شطرنج» (عربی چ ندارد و آن را ش می‌نویسد، و ت نیز به مجاورتِ آواهای مطبق به صورت ط نوشته شده) و سپس بازگشت همان صورتِ معرّب به فارسی — یعنی یک رفت‌وبرگشتِ فارسی ← عربی ← فارسی. شاهدی که نورایی می‌آورد در لغت فرس اسدی (ص ۲۸۹) و در همان صفحهٔ برهان قاطع آمده است. آنچه مشکوک است صورت نخستِ درون جعبه، «کترنگ»، است: چنین واژه‌ای در فارسی نیست و ک با چ تنها به سه نقطه فرق دارد، پس اصل باید «چترنگ» باشد، همان که در برهان، معین، مکنزی و اصباغی آمده است؛ به احتمال زیاد خطای خوانشِ اسکن (یا در نهایت غلط چاپی کتاب) است. صورت دوم، «شطرنج»، درست است.\",\n\"14\": \"سنسکریت áñcati «خم می‌شود» (و صورت درجه‌صفرِ آن ácati) فعل اصلی همین ریشه است — پوکورنی در صفحهٔ ۴۵ آن را با اشاره به فارسی میانه ancītan آورده — و در کنار آن اسم aṅká- «خم، قلاب، آغوش» می‌ایستد. با پیشوند pári «پیرامون» ترکیب pary-aṅka- ~ paly-aṅka- «تخت، بستر، تخت‌روان» پدید می‌آید، یعنی «آنچه گرد [تن] خم می‌شود»؛ نوسان ry ~ ly همان تبدیل آشنای r/l در هندی است و همهٔ صورت‌های وام‌گرفته از گونهٔ l-دار (پالی pallaṅko) برخاسته‌اند. توضیح نورایی دربارهٔ «فرورفتن پارچهٔ تخت‌روان» تعبیر شخصیِ اوست؛ تحلیل پذیرفته‌شده همان «خمیده گرداگرد» است.\",\n\"15\": \"دو سر زنجیره درست است اما پیکانِ یک‌مرحله‌ایِ «سنسکریت ← انگلیسی» حلقه‌های میانی را حذف کرده است: سنسکریت palyaṅka- > پالی pallaṅka > مالایی و جاوه‌ای palangki «تخت‌روان» (اصطلاح بازرگانی اقیانوس هند) > پرتغالی palanquim (اوایل سدهٔ شانزدهم؛ -m افزودهٔ معمول پرتغالی است، چنان‌که در mandarim) > انگلیسی palanquin از دههٔ ۱۵۸۰. گونهٔ انگلیسی-هندیِ palankeen/palankee از هندی pālkī آمده است نه مستقیماً از سنسکریت. از این رو حکم «با احتیاط پذیرفتنی» است: خودِ ریشه‌یابی درست، اما مسیر وام‌گیری ناقص نمودار شده است.\",\n\"16\": \"لاتینی angulus «گوشه، زاویه» از *ang-olo-، مشتقی با پسوند -lo- از همان ستاک «خمیدن»، و برابرهای دقیق آن اسلاوی کهن ǫgŭlŭ «گوشه» و ارمنی ankiwn «گوشه» است؛ در کنارشان لاتینی uncus «قلاب» با درجهٔ o می‌ایستد. مشتقات آن angulāris و ترکیب‌های عددیِ tri-/quadri-/rect-angulus است که triangle و rectangle انگلیسی از آنها برخاسته‌اند. واتکینز و کلاین همین را می‌گویند و ادعای نورایی درست است؛ تنها مان (IEC) صورت ریشه را *anghulos با هَ‌واکِ واک‌دار بازسازی می‌کند، پس شکل دقیق ریشه به اجماع کامل نرسیده است.\",\n\"17\": \"هر سه واژه وام‌واژه‌های کتابیِ لاتینی از راه فرانسه‌اند نه واژه‌های بومی: لاتینی angulus > فرانسوی angle > انگلیسی میانه angle (سدهٔ چهاردهم)، لاتینی tri-angulum > فرانسوی triangle، و لاتینی متأخر rect-angulum > فرانسوی rectangle > انگلیسی rectangle (سدهٔ شانزدهم). کلاین و اسکیت هر دو انگلیسیِ angle را «(F.–L.)» برچسب می‌زنند. توجه شود که هم‌نگاشتِ angle به معنی «قلاب ماهیگیری» از این راه نیامده، بلکه دنبالهٔ بومیِ انگلیسی باستان angel است — و نورایی به‌درستی آن را در این شاخه نیاورده، هرچند گرهٔ ۱۸ بر همان واژه استوار است.\",\n\"18\": \"Angul (انگلیسی باستان Angel/Ongel، آلمانی Angeln، دانمارکی Angel) نام ناحیه‌ای کوچک در ساحل شرقی شبه‌جزیرهٔ یوتلاند/شلسویگ است که قوم انگل از آنجا برخاسته‌اند. ریشه‌یابی سنتی، که به رودولف موخ بازمی‌گردد، این نام را همان *angul- ژرمنی «قلاب، خمِ ساحل» (< *h₂enk-ulo-) می‌داند، یعنی «سرزمین قلاب‌مانند» — دقیقاً همان معنایی که نورایی می‌دهد. اما این ریشه‌یابی اثبات‌شده نیست: پوکورنی آن را تنها به عنوان پیشنهاد موخ نقل می‌کند و ایراد می‌گیرد که معنی «خلیج/گوشه» جای دیگری گواه ندارد، و واتکینز نیز با قید «احتمالاً» می‌آورد. برچسب زبانیِ «ژرمنی» نیز مسامحه‌آمیز است، چون نام در لاتینی (Anglii نزد تاسیتوس) و انگلیسی باستان گواه دارد نه در منبعی بازسازی‌شده. پس با احتیاط پذیرفتنی است.\",\n\"19\": \"انگلیسی باستان Engle/Angle (جمع) «انگل‌ها»، لاتینی Anglī، نام قومی ژرمنی است که همراه ساکسون‌ها و یوت‌ها در میانهٔ سدهٔ پنجم میلادی به بریتانیا کوچیدند (تاریخ سنتیِ بید ۴۴۹ است و «حدود ۴۵۰» نورایی گِردکردنِ همان است). صورت Engle در برابر Angle نتیجهٔ اماله (i-umlaut) یعنی بدل شدن a به e در مجاورت i/j ستاک است. از همین نام Engla land «سرزمین انگل‌ها» و Englisc پدید آمده‌اند؛ واژه نخست بر قوم دلالت داشت و تنها در اواخر دورهٔ انگلیسی باستان بر کشور اطلاق شد. ادعای نورایی درست است، جز آنکه ضبط «Engle-Land» باید Engla land باشد.\",\n\"20\": \"در فرانسه نه صورتی به شکل «angle-» به معنی «انگلیسی» هست و نه اصولاً حلقه‌ای فرانسوی در این زنجیره: واژهٔ فرانسویِ «انگلیسی» anglais است، از فرانسوی کهن anglois، از لاتینی Anglus / لاتینی متأخر Anglenses — یعنی از صورتِ لاتینیِ نام قوم، نه از Engle انگلیسی باستان چنان‌که پیکان کتاب می‌گوید؛ لاتینی این نام را مستقل از انگلیسی باستان از ژرمنی گرفته است. واژهٔ فرانسوی angle واژهٔ دیگری است به معنی «گوشه»، از همان لاتینی angulus که خودِ نورایی در گرهٔ ۱۶ آورده است. پس این گره دو هم‌نگاشت را درهم آمیخته و واسطه‌ای ساخته که هیچ منبعی تأیید نمی‌کند؛ پژوهش امروزی آن را رد می‌کند.\",\n\"21\": \"«انگلیس» در فارسی وام‌واژه‌ای نو از زبان‌های اروپایی است، اما منبع پذیرفته‌شده ایتالیایی inglese است، به احتمال زیاد از راه ترکی عثمانی «انگلیز» — همان مسیر تجارت شام که بیشتر نام‌های قومیِ اروپایی از آن به فارسی رسیده‌اند — نه راه فرانسوی که نورایی می‌کشد و به‌ویژه نه از «angle-»ی فرانسوی که وجود ندارد. س پایانیِ «انگلیس» با -se ایتالیایی می‌خواند نه با -ais فرانسوی که /ɛ/ تلفظ می‌شود؛ «انگلیسی» نسبتِ معمول فارسی است و «انگلستان» ساختی درون‌فارسی با پسوند -ستان، نه وام‌واژه. سرچشمهٔ نهایی در لاتینی Anglus و نام قوم ژرمنی البته درست است؛ آنچه نادرست است زبانِ واسطه است، پس پژوهش امروزی این گره را رد می‌کند.\",\n\"22\": \"انگلیسی باستان Englisc (صفت از Engle) به English بدل شده و Engla land «سرزمین انگل‌ها» از راه Engleland به England رسیده است (تلفظ امروزیِ In- دگرگونیِ پسین است، احتمالاً به قیاس واژه‌های -ing-دار). جزء Anglo- صورت ترکیبیِ برگرفته از لاتینی متأخر Anglī «انگلیسی‌ها» است و Anglo-Saxon از لاتینی سده‌های میانهٔ Anglo-Saxones (پیش‌تر Anglī Saxones «ساکسون‌های انگلیسی») می‌آید؛ چنان‌که کلاین یادآور می‌شود، این ترکیب در کاربرد متأخر حشو است، زیرا در لاتینی متأخر هر دو جزء معنی «انگلیسی» یافته بودند. ادعای نورایی درست است.\"\n}\n}\n}\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py 56 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p56.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-56.json > /dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat",
 "description": "Apply Persian to page 56"
}
```


### [2026-09-04T23:09:55.322Z] TOOL RESULT

```
ok 56
JSON_OK
 data/verification/page-34.json | 24 ++++++++++++++++++++++++
 data/verification/page-44.json | 19 +++++++++++++++++++
 data/verification/page-56.json | 23 +++++++++++++++++++++++
 3 files changed, 66 insertions(+)
```


## [2026-09-04T23:09:59.172Z] TOOL CALL #12: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 57 58",
 "description": "Dump pages 57 and 58"
}
```


### [2026-09-04T23:10:01.027Z] TOOL RESULT

```
<persisted-output>
Output too large (47.5KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/binglyom4.txt

Preview (first 2KB):
##########################################################################################
PAGE 57 book 27
================================================================================
ENTRY 0 | root: Angh | verdict: confirmed | modern: PIE *h₂enǵʰ- 'to constrict, tighten; narrow, painfully constricted' (Pokorny angh- 42–43; Watkins/AHD angh- 'tight, painfully constricted, painful')
NOTE: Root form, language label and gloss are all right. Pokorny IEW 42–43 heads the entry 'angh- (kelt. auch engh-) ‚eng, einengen, schnüren‘, z. T. auch von seelischer Beklemmung, Angst' and lists exactly the branches Nourai draws (Avestan verbal forms, Latin ango/angustus, Germanic angr/angust); AHD gives 'angh-. Tight, painfully constricted, painful ... [Pok. ang̑h- 42.]'. Two cross-cutting caveats: (1) the Avestan form printed in the book, 'azaehě', is not a real Avestan word — the PDF page image confirms the book itself prints 'azaehě', so this is Nourai's own corruption (not a scan error) of Av. ǫzaŋhē (Bartholomae AiW 363–4, Pokorny p.42 'ǫzaŋhē'); (2) the ni-āz / niyāz branch is claimed by a different root in current Iranian scholarship: Cheung, Etymological Dictionary of the Iranian Verb (2007) 171–172, files Av. niiāzata / niiāzaiiən and MP/Pth./Sogd./NP niyāz under *Haz 'to drive, lead' (PIE *h₂eǵ-, Skt. aj-, Lat. agō), not under *angh-. Bartholomae, Walde-Pokorny I 62 and Moʼin (following Bartholomae) all support Nourai; Cheung is the dissent.
ROOTREF: POK:42=supports
------------------------------------------------------------
# 1 Avestan | azaehě; ni-az | verdict: disputed | 
...
</persisted-output>
```


## [2026-09-04T23:10:03.733Z] TOOL CALL #13: Read

```json
{
 "file_path": "/home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/binglyom4.txt"
}
```


### [2026-09-04T23:10:04.613Z] TOOL RESULT

```
1	##########################################################################################
2	PAGE 57 book 27
3	================================================================================
4	ENTRY 0 | root: Angh | verdict: confirmed | modern: PIE *h₂enǵʰ- 'to constrict, tighten; narrow, painfully constricted' (Pokorny angh- 42–43; Watkins/AHD angh- 'tight, painfully constricted, painful')
5	NOTE: Root form, language label and gloss are all right. Pokorny IEW 42–43 heads the entry 'angh- (kelt. auch engh-) ‚eng, einengen, schnüren‘, z. T. auch von seelischer Beklemmung, Angst' and lists exactly the branches Nourai draws (Avestan verbal forms, Latin ango/angustus, Germanic angr/angust); AHD gives 'angh-. Tight, painfully constricted, painful ... [Pok. ang̑h- 42.]'. Two cross-cutting caveats: (1) the Avestan form printed in the book, 'azaehě', is not a real Avestan word — the PDF page image confirms the book itself prints 'azaehě', so this is Nourai's own corruption (not a scan error) of Av. ǫzaŋhē (Bartholomae AiW 363–4, Pokorny p.42 'ǫzaŋhē'); (2) the ni-āz / niyāz branch is claimed by a different root in current Iranian scholarship: Cheung, Etymological Dictionary of the Iranian Verb (2007) 171–172, files Av. niiāzata / niiāzaiiən and MP/Pth./Sogd./NP niyāz under *Haz 'to drive, lead' (PIE *h₂eǵ-, Skt. aj-, Lat. agō), not under *angh-. Bartholomae, Walde-Pokorny I 62 and Moʼin (following Bartholomae) all support Nourai; Cheung is the dissent.
6	ROOTREF: POK:42=supports
7	------------------------------------------------------------
8	# 1 Avestan | azaehě; ni-az | verdict: disputed | 
9	DER: Two items. (a) 'azaehě' is a corrupt rendering of Young Avestan ǫzaŋhē, the infinitive of ǫz- 'to lace up, constrict, oppress' (Bartholomae AiW s.v.: 'j. ǫzaŋhe Inf. ‚zu bedrängen, in Not zu bringen‘: avaŋhe narǫm ašaonǫm ǫz° Yt 13.39'), beside the s-stem ǫzah- n. '1) Ein-, Zusammenschnürung der Kehle, Erdrosselung; 2) Bedrängung, Enge, Not; Gefangenschaft' (Yt 10.22, V 16.10, Y 10.17). Phonology: PIE *h₂enǵʰ- > Proto-Iranian *anź- > Av. ǫz- (the nasal is written with the nasalised vowel ǫ before the fricative), the exact match of Lat. angō/angor and Skt. áṃhas-. So Nourai's gloss 'compressed, in need' is right and the arrow root→Avestan is right for this word, but the printed shape is impossible Avestan. (b) 'ni-az' = Av. ǫz- with the preverb ni-, in the lengthened grade *ni-āz-, attested only in finite forms: ni-āzata 'she laces her waist in' (Yt 5.127, of Anāhitā) and ni-āzaiiən 'they shall wedge (it) in' (V 13.30). No Avestan noun *ni-āz- 'need' exists — Nourai's gloss 'that which pushes you down, need' back-projects the Middle Persian abstract. Walde-Pokorny I 62 print exactly this set ('Verbal av. ǫzaŋhe ‚zu bedrängen, in Not zu bringen‘, tiefstufig av. ny-azata ‚sie schnür…
10	REF: POK:42=supports: POK_full.txt s.v. angh-: 'Material: Verbal: Avestan ǫzaŋhē “to press”, lengthened grade Av…
11	CON: BRT=supports: 'j. ǫz- V. ‚schnüren‘. Praes. 3 aza- (nyaza-). Inf. ǫzaŋhe ... mit ni ‚einschnüren, einzwä… ; WLD=supports: 'angh- (kelt. auch engh-) ‚eng, einengen, schnüren‘, z. T. auch von seelischer Beklemmung,… ; CHEUNG=contradicts: '*Haz ‚to drive, lead’. AVESTAN: az- ‚to lead’ || ... (+ *ni-) caus. ‚to straiten’ (cf. De… ; AHD=partial: 'angh-. Tight, painfully constricted, painful. ... [Pok. angh- 42.]' — confirms the root a…
12	------------------------------------------------------------
13	# 2 Pahlavi | niyâz | verdict: confirmed | 
14	DER: Middle Persian niyāz, Book Pahlavi ⟨nydʾc⟩ = ⟨nyʾc⟩, Manichaean MP and Parthian ⟨nyʼz⟩ 'need, want, misery' (MacKenzie, Concise Pahlavi Dictionary s.v.), with the derivatives niyāzōmand 'needy' and niyāzōmandīh 'poverty' and the negated compound abē-niyāz 'free from want'. Formally it is an Old Iranian action-noun *ni-āza- built to the verb seen in Av. ni-āz-: the preverb ni- + ā of the lengthened grade gives MP niyā- (the glide y is automatic between i and ā), and Old Iranian intervocalic -z- is kept, spelt ⟨c⟩ in Book Pahlavi. Age: Armenian took the compound over in the Arsacid period as apeṛniaz / apeniaz 'without need' = MP abē-niyāz (Hübschmann, Persische Studien §91), which shows the word already existed in Middle Iranian; Sogdian nyʼz 'need' and Christian Sogdian nyʼzʼwt 'needy' show the same formation in the eastern branch. Only the ultimate root attribution is contested (see node 1); that MP niyāz contains ni- + the āz- verb is agreed by everyone, Cheung included.
15	REF: MON:4877=partial: The 6-vol Amir Kabir Moʼin is not online in any form, so p.4877 itself cannot be opened. M…
16	CON: PHD=supports: 'niyāz [nydʾc | M nyʼz, N ~] need, want, misery. ~ōmand [-ʼwmnd | N ~mand] needy. ~ōmandīh… ; HUB=supports: 'apeniaz ‚bedürfnisslos‘ = np. be-niyaz' — the Armenian loan proves an Arsacid-era Middle … ; CHEUNG=partial: Gives exactly the same Middle Iranian material ('MIDDLE PERSIAN: (+ *ni-) BMP nydʾc /niyaz… ; NYB=silent: grep -n 'niyāz|niyaz|nyʼc' NYB_vol2_glossary.txt NYB_vol1.txt returns nothing; the word do…
17	------------------------------------------------------------
18	# 3 Persian | niâz; nîâzî | verdict: confirmed | 
19	DER: MP niyāz passes into New Persian unchanged as نیاز niyāz 'need, want', with the derived adjectives نیازمند / نیازومند niyāz(ō)mand 'needy' (= MP niyāzōmand) — exactly the two forms Nourai prints in the box — and the Islamic-era religious sense 'votive offering made to obtain a wish' (Moʼin sense 2; Farhang-e Neẓām, quoted in Moʼin's note to Borhān). The second word نیازی niyāzī 'beloved, sweetheart' is a separate lexicographic item: Asadi Ṭusi's Loghat-e Fors already has «نیاز، دوست بود» with Labībī's line «ایا نیاز بمن ساز و مر مرا مگذار», and Rashīdī corrects him: «لیکن بمعنی دوست، نیازی است نه نیاز» — i.e. in the 'friend/beloved' sense the correct form carries the -ī, which is why Nourai's chart gives 'nîâzî: need, dear friend, sweetheart'; the ʿOsmān Mokhtārī couplet he quotes (دلم خستهٔ ناز توست ای نیازی) uses it in that sense. Semantically the 'sweetheart' sense is the object of one's niyāz, i.e. 'the one one longs for'.
20	REF: BQT:2222=supports: Checked with the local scan of Borhān-e Qāṭeʿ vol. 4 (BQT_v4_pages.txt, [pdf page 305] = p… ; MON:4877=partial: Same as node 2: the 6-vol Moʼin is not online, so the page cannot be opened; the online Mo…
21	CON: BQT=supports: See ref_check: headword نیاز 'need' + Moʼin's footnote deriving it from Pahlavi niyāz < Av… ; MON=supports: '[په.] (اِ.) ۱- حاجت ، احتیاج. ۲- نذری که برای گرفتن مراد و حاجت به کسی یا جایی دهند' — Pa… ; HRN=partial: Horn has no separate entry for niyāz; he cites it only inside the bē- entry: 'phlv. ape- (… ; CHEUNG=partial: '(+ *ni-) NP niyaz ‚need’' — the New Persian word and its ni-āz analysis are confirmed, bu… ; ARY=silent: grep of the Persian text and of the Latin index for نیاز / NIYAZ / ANGH returns no root en…
22	------------------------------------------------------------
23	# 4 Latin |  | verdict: confirmed | 
24	DER: An empty pass-through box standing for the Latin branch of *h₂enǵʰ-: the verb angō, -ere 'to press tight, throttle; to distress' (the exact match of Gk. ἄγχω and Av. ǫzaŋhē), its nouns angor 'constriction of the throat; anguish' and angina 'quinsy', the adjective anxius (< *angh-s-io-) 'uneasy, solicitous', and the s-stem adjective angustus < *angh-os-to-s 'narrow' with its abstract angustia(e) 'narrowness, straits, distress'. Ernout–Meillet stress that the double sense Nourai needs is Latin-internal: 'Ango se dit du physique et du moral; ce même double sens se retrouve dans les substantifs dérivés'. Both English words in the daughter box come out of this Latin material.
25	REF: AHD=supports: AHD_watkins1985.txt s.v. angh-: '4. Latin angere, to strangle, draw tight: ANXIOUS. 5. Suf…
26	CON: LAT=supports: 'ango, -is, -xi, anctum, -ere: étreindre, oppresser, serrer (la gorge) ... Ango se dit du … ; KLN=supports: '... L. angere, ‚to press together, throttle, torment’, angustus, ‚narrow’ ... fr. I.-E. b… ; POK=supports: 'lat. ango ‚beenge, schnüre zu‘ ... lat. angor m. ... angus-tus ‚eng‘ (aus *anghos-to-s); … ; LEW=partial: The local file is only the index volume; it lists 'ango, angul I 46', i.e. the entry stand…
27	------------------------------------------------------------
28	# 5 English | anxious, anguish | verdict: confirmed | 
29	DER: Two different routes out of the Latin box. ANXIOUS is a learned 16th/17th-c. borrowing straight from Latin anxius 'solicitous, uneasy' (formed to angere), with English -ous substituted for Latin -us; the noun anxiety likewise from anxietas, -atis. ANGUISH came by the popular route: Latin angustia (classical plural angustiae) 'narrowness, straits' > Old French anguisse, angoisse 'choking sensation, distress, anxiety, rage' (12th c., Modern French angoisse) > Middle English anguise, angoise (c.1200), whence the verb anguish from OF anguissier, angoissier. The semantic path is 'tightness/choking' > 'straits, difficulty' > 'mental torment'.
30	REF: None=not_checked: The node carries no reference of its own; the parent Latin box's AHD citation covers it ('…
31	CON: KLN=supports: 'anguish, n. — ME. anguise, angoise, fr. OF. anguisse, angoisse (F. angoisse), fr. L. angu… ; SKT=supports: 'Anxious. (L.) See Anguish.' and the angina entry 'L. ... lit. choking. — L. angere, to ..… ; AHD=supports: Index lines: 'ANGUISH angh-', 'ANXIOUS angh-'.
32	------------------------------------------------------------
33	# 6 Germanic |  | verdict: confirmed | 
34	DER: An empty pass-through box for the Germanic branch of *h₂enǵʰ-. The adjective *angwuz 'narrow' (Goth. aggwus, ON ǫngr, OE enge, OS engi, OHG angi/engī, G. eng) continues *anghu-; the s-stem *angaz- (< *anghos-, the same formation as Skt. áṃhas- and Lat. angor) gives ON angr 'grief, affliction'; and *angusti- (< *anghos-ti-, revocalised after *anghu-) gives OHG angust, OFris. angost, German Angst. Nourai's box leads only to English anger, i.e. to the ON angr reflex.
35	REF: AHD=supports: AHD_watkins1985.txt s.v. angh-: '2. Suffixed form *angh-os- in Germanic *angaz in Old Nors…
36	CON: KLN=supports: 'ON. angr ... rel. to ON. ǫngr, OE. enge, ‚narrow, painful’, OS. engi, MDu. enghe, Du. eng… ; SYN=supports: 'ME angre, NE anger, fr. ON angr ‚trouble, affliction’ ... : Lat. angor ‚constriction of t… ; POK=supports: 'anord. angr m. ... ‚Verdruß; Schade, Betrübnis‘; afries. angost, ahd. angust, nhd. Angst …
37	------------------------------------------------------------
38	# 7 English | anger | verdict: confirmed | 
39	DER: Not a native English word: Middle English angre (n., mid-13c., first 'distress, suffering, affliction'; v. c.1200 'to vex, irritate') is a loan from Old Norse angr 'grief, sorrow, affliction' / angra 'to grieve, vex' taken over in the Danelaw — the same Norse layer as e.g. ill, skin, take. The Proto-Germanic base is *angaz < *anghos-. The modern sense arose by transfer from the injury to the feeling it provokes ('the expression was transferred to the feelings of resentment naturally aroused in the mind of the person aggrieved'), giving 'rage, wrath' by the early 14th c., whence angry.
40	REF: None=not_checked: The node carries no reference; the parent Germanic box's AHD citation covers it ('*angh-os…
41	CON: KLN=supports: 'anger, n. — ME., fr. ON. angr, ‚sorrow, affliction’ ... fr. I.-E. base *angh-, ‚to narrow… ; SYN=supports: 'ME angre, NE anger, fr. ON angr ‚trouble, affliction’ (so also ME angre) : Lat. angor ...… ; SKT=partial: Skeat's own 'anger' headword is not legible in the local OCR; the Awe entry gives the fami…
42	================================================================================
43	ENTRY 1 | root: Angwhi | verdict: confirmed | modern: PIE *h₂éngʷʰis 'snake' (Pokorny angʷ(h)i- 43–45; Watkins/AHD angʷhi- 'snake, eel')
44	NOTE: The root box itself is right: Pokorny 43–45 heads 'angʷ(h)i- ‚Schlange, Wurm‘' and AHD 'angʷhi-. Snake, eel.' What Nourai's single box hides is the split Pokorny states in his own first line: 'egʷhi-, ogʷhi- und eghi- ds.; mindestens zwei etymologisch verschiedene, aber früh verschränkte Sippen, deren Verhältnisse noch vielfach unklar sind.' Current handbooks separate *h₂éngʷʰis (Lat. anguis, Lith. angis, OPruss. angis, OCS *ǫzь, Pol. wąż) from *h₁ógʷʰis / *h₃égʷʰis (Skt. áhi-, Av. aži-, Gk. ὄφις, Arm. iž), which is where the Avestan branch of this chart actually belongs (see node 1). Ernout–Meillet put it bluntly: 'Le flottement porte sur l'initiale: e-, o-, an-, et sur les consonnes *gʷ, *gʰ, *gʷʰ ... On ne peut donc restituer un original indo-européen.' Separately, Walde–Pokorny I 65 reject the once-popular idea that *angʷ(h)is 'snake' is a 'constrictor' derived from the neighbouring root angh- 'to press' — 'ist wegen der Gutturalverschiedenheit und sachlich zu bestreiten' — which matters because Nourai prints Angh and Angwhi side by side on this page.
45	ROOTREF: POK:43=supports
46	------------------------------------------------------------
47	# 1 Avestan | aži; aži-dahâkô | verdict: plausible | 
48	DER: Both words are real. Av. aži- (stem ažay-) m. is 'snake' and, by extension, 'dragon, monster' — Bartholomae AiW: 'j. ažay- m. 1) ‚Schlange‘, ein daēvic animal (V 18.65, V 14.5) ... 2) schlangenähnliches Untier ‚Drache, Ungeheuer‘ (Y 9.30 ažiš sairitaʾ, Aog. 78)'; it is the exact cognate of Skt. áhi-, Gk. ὄφις, Arm. iž, Lat. anguis. aži.dahāka- is the three-headed serpent-tyrant of Yt 5.29–35, Yt 9.14, Yt 19.37 and Y 9.8, killed by Θraētaōna; Nourai's shape 'aži-dahâkô' is the Avestan nominative singular ažiš dahākō, the very form used by Horn (Grundriss no. 76 'aw. ažiš dahākō') and Hübschmann ('zd. aži dahākō'). WHY ONLY 'plausible': the arrow from the root box as drawn is phonologically wrong under the modern reconstruction. Av. aži- goes back to Proto-Iranian *Háǰiš < Proto-Indo-Iranian *Háǰʰiš < *h₁ógʷʰis — the NASAL-LESS variant. Pokorny himself puts it there, not under the nasal form: on printed p.44 he writes 'gr. ὄφις ‚Schlange‘ (*ogʷhis): cymr. euod (*ogʷh-): ai. ahi-, av. azi- ‚Schlange‘', i.e. in the *ogʷhi- paragraph, while Latin anguis heads the *angʷhi- paragraph. Klein hedges the same way ('prob. also with OI. ahiḥ, Avestic azish'), and Buck notes the two sets come '…
49	REF: POK:44=supports: POK_01.txt leaf 52 (printed p.44, the '45' numeral follows a few lines later): 'gr. ὄφις ‚… ; KLN:86=partial: Klein does say precisely this, s.v. anguine: 'L. anguinus, fr. anguis, ‚serpent, snake’, w…
50	CON: BRT=supports: 'j. ažay- m. 1) ‚Schlange‘, ein daēvisches Tier ... 2) schlangenähnliches Untier ‚Drache, … ; HRN=supports: '76. eždehä ‚Drache‘. aw. ažiš dahākō; phlv. aže dahäk, arm. LW. aždahak ... aw. aži- ‚Sch… ; SYN=partial: 'Lat. anguis; Lith., OPruss. angis; ChSl. *ǫzь, Pol. wąż, Russ. už; Skt. ahi-, Av. aži-; f… ; ARY=supports: The index page groups under one root: 'AZHI-DAHAKA (AVESTAN), AZHI; AZDAHAG, AZ (PAHLAVI);…
51	------------------------------------------------------------
52	# 2 Persian | eždehâk; eždehâ; aždar | verdict: confirmed | 
53	DER: Old Iranian aži-dahāka- > Middle Persian až(i)dahāg (Book Pahlavi ʿcydhʿk', Manichaean MP ʿzdhʿg) > New Persian اژدها aždahā, by the regular loss of final MP -g and of the intervocalic stop; the fuller اژدهاک eždehāk preserves the -k and, in Borhān, is glossed as the last sense of اژدها, i.e. ضحاک ماران (Moʼin's footnote: 'مخفف اژی‌دهاک، ضحاک'). Horn (no.76) shows the date: the Armenian loan aždahak proves that the Middle Persian pronunciation was already až-, not aǰ-, in Arsacid/Sasanian times. The Semitic round-trip Nourai marks with ضحّاک in the box is real and runs Persian > Arabic > Persian: Asbaghi (PLA 190) has Arabic ضحّاک ḍaḥḥāk, folk-etymologised as the Arabic active participle 'the laugher / name of a king', from Persian aždahā 'Drache' < aži-dahāka > Pazand Dahāk 'evil, demonic king', 'arabisiert in ẓaḥḥāk'; and PLA 5 has a second, unassimilated Arabic borrowing أزدهاق azdahāq 'a particular dragon' straight from Persian. اژدر aždar is the shortened Persian form, from which Turkish ejder/ejderha and Bulgarian/Serbian ažder were taken (PLA 190); Borhān glosses اژدر as 'مار بزرگ ... و سر علم و رایت'. The modern military sense 'torpedo' (اژدر دریایی) is a 20th-c. Persian co…
54	REF: BQT:116,1339=supports: vol. 1: the اژدر / اژدرها / اژدها / اژدهاک cluster stands across ↵-leaves 327–328 of BQT_v… ; PLA:5,190=supports: Asbaghi, Persische Lehnwörter im Arabischen, p. 5 (PLA_pages.txt leaf 20, running head 'ʾa… ; FSF:43=partial: The entry exists and says exactly what Nourai's gloss says, but at a different page in the…
55	CON: HRN=supports: '76. eždehä ‚Drache‘. aw. ažiš dahākō; phlv. aže dahäk, arm. LW. aždahak. arm. aždahak bew… ; HUB=supports: 'aždahā ‚Drache‘ = arm. aždahak, zd. ažiš dahākō' and again 'aždahā ‚Drache‘ = zd. aži dah… ; MON=supports: اژدها is tagged [اَوِس] = Avestan and referred to اژدرها / اژدر, defined as the winged, ta… ; FSF=supports: 'اژدها — کنایه از نیزه' with 'یکی باره زیر اژدهایی به کف' — the source of Nourai's 'also a… ; BQT=supports: See ref_check above; Moʼin's footnotes derive both اژدهاک and ضحّاک from اژی دهاک.
56	------------------------------------------------------------
57	# 3 Latin | anguis | verdict: confirmed | 
58	DER: Latin anguis (m., f. in early Latin) 'snake' is the direct reflex of the nasal form *h₂éngʷʰis and is exactly superposable on Lith. angis, OPruss. angis, Latv. uodze, OCS *ǫzь, Pol. wąż, Russ. už. It is an old religious/poetic word, largely replaced in prose by serpēns and uīpera (Pliny has it 40× against 360× serpēns); its derivatives are anguinus, anguiculus, and the diminutive-shaped anguilla 'eel' (paralleled by OPruss. angurgis, Lith. ungurys, Pol. węgorz for the same 'snake-fish' idea). It is the only word in this chart that the modern reconstruction actually assigns to *angʷʰi-.
59	REF: AHD=supports: AHD_watkins1985.txt: 'angʷhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. …
60	CON: LAT=supports: 'anguis, -is n. (et f. à l'ép. arch.): serpent. Mot ancien, employé dans la l. religieuse … ; POK=supports: 'Lat. anguis = lit. angis (f.), apr. angis ‚Schlange‘ (lett. uodze f.), aksl. *ǫzь, russ. … ; IEC=supports: 'WP I, 63. Cf. ogʷhis. Lat. anguis, cf. anguilla; Br. anv ‚slowworm‘; OCS ǫzь ‚grass-snake… ; SYN=supports: Lists Lat. anguis in the 'snake' table beside Lith. angis and ChSl. *ǫzь.
61	------------------------------------------------------------
62	# 4 English | anguine | verdict: confirmed | 
63	DER: A learned borrowing, not an inherited word: English anguine 'snakelike, pertaining to a serpent' (17th c.) is Latin anguinus, the adjective of anguis, with the Latin -inus ending anglicised as -ine; the parallel anguineous renders anguineus. No French intermediary is needed, and the word has stayed a bookish one. AHD gives ANGUINE (with ANGUILLIFORM) as the English yield of this root through Latin.
64	REF: None=not_checked: The node carries no reference; the parent Latin box's AHD citation covers it ('Latin angui…
65	CON: KLN=supports: 'anguine, adj., pertaining to a serpent. — L. anguinus, fr. anguis, ‚serpent, snake’ ... F… ; WEB=supports: 'an-guinʹe-al, a. anguineous.' / 'an-guinʹe-ous, a. [L. anguineus, from anguis, a snake.] … ; AHD=supports: Index: 'ANGUILLIFORM angʷhi-', 'ANGUINE angʷhi-'.
66	##########################################################################################
67	PAGE 58 book 28
68	================================================================================
69	ENTRY 0 | root: Ap 2 | verdict: confirmed | modern: PIE *h₁ep- 'to take, seize, reach' (Pokorny '1. ap- (richtiger əp-) : ep- "fassen, nehmen, erreichen"', IEW 50-51; Watkins/AHD ap-¹ 'To take, reach'; LIV *h₁ep-)
70	NOTE: Root, language label and gloss are all correct: Pokorny's entry begins at the foot of p.50 (exactly Nourai's POK:50) and runs onto p.51, with Av. apayeiti, Skt. āpnóti, Lat. apiscor/apere/aptus/apex/cōpula and Hitt. epmi — i.e. precisely the two branches Nourai draws. The only correction is that the modern reconstruction has an initial laryngeal (*h₁ep-), which is why Hittite has e-ep-zi and Latin co-ēpī shows e-vocalism. Nourai's numbering 'Ap 2' distinguishes this root from 'Ap 1' = *h₂ep- 'water' (Pokorny 2. āp- p.51), which is the right distinction. The weak point of the page is not the root but the Iranian branch: Cheung 2007 removes MP abām 'loan' from this root altogether (see node 2).
71	ROOTREF: POK:50=supports
72	------------------------------------------------------------
73	# 1 Avestan / Old Persian | ap 1, af, ab : to receive ; apayeiti : received ; abi-âp, abi-âf : to detain | verdict: plausible | 
74	DER: Avestan ap- 'to reach, attain' (present stem apaiia-, 3sg. apaiieiti Yt 10.21, 14.20, 17.19; 1sg. apaiiemi Yt 5.42, 15.43; perf. āpa; OAv. 1pl. opt. apaema Y 41.2) is the regular Iranian continuant of PIE *h₁ep-: *h₁p-eie- > Ir. *apaya-, with intervocalic *p preserved in Avestan. Nourai's 'af, ab' are not Avestan or Old Persian forms at all but retrojections of the later Iranian outcomes, where Old Iranian *p in postvocalic position lenites through *β to Middle/New Persian f (before a consonant / word-finally) and b/w (before a vowel): hence MP ayāft ~ ayāb-, NP yāft ~ yāb-. Old Persian has no attested reflex of this root (Kent's lexicon has none), so the label 'Avestan / Old Persian' overstates the evidence. The compound is Av. aiβi-/avi-ap- (Nyberg: 'ay- probably < abi-, cf Av. avi-ap-'; Cheung: '(+ *abi-) to obtain, find'), and its meaning is 'to obtain, reach, find' — NOT 'to detain'. The scan of p.28 does print 'to detain', so this is Nourai's own slip (probably for 'to obtain'), not a transcription error in the JSON.
75	REF: POK:50=supports: POK_01.txt ff-page 59 (printed 50): 'Ai. āpnóti "erreicht, erlangt" ... av. apayeiti "erre… ; SNS:14=not_found: SNS_pages.txt: the Šāyast nē Šāyast glossary OCR is very poor. The a-/ab- stretch of the g… ; FFD:82=supports: FFD_pages.txt [pdf page 87] = printed p.82, s.v. یافتن: 'یافت < فارسی میانه ayāft < ایرانی…
76	CON: BRT=supports: Bartholomae gives the paradigm apayeiti with senses '1) einholen, nachkommen 2) gelangen z… ; CHEUNG=supports: '*Hap/f "to reach, attain" — *AVESTAN: ap- "to reach, attain" || (+ *abi-) "to obtain, fin… ; WLD=supports: '1. ap- "erreichen". Ai. āpnóti "erreicht, erlangt" ... av. apayeiti "erreicht". Lat. apis… ; AHD=supports: 'ap-¹. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE;… ; KNT=silent: Kent has no Old Persian verb ap-/āp- 'to reach'; the only Bāx-/ap- material in the lexicon…
77	------------------------------------------------------------
78	# 2 Pahlavi | apâm, avâm : loan, something received. | verdict: disputed | 
79	DER: Book Pahlavi ʾpʾm /abām/ 'loan, debt' is well attested (MacKenzie p.4; Nyberg II 22; Parthian ʾbʾmyh 'loan'). Nourai, following Nyberg and Mo'in, analyses it as Old Iranian *(ā-)apamna-, a middle participle of ap- 'to reach, obtain' — literally 'that which the lender has to obtain back', hence his gloss 'something received'. Cheung's Etymological Dictionary of the Iranian Verb (2007) rejects this: he files abām under the root *Hmai¹ 'to (ex)change' (< PIE *h₂mei-, Pok. 710, LIV 426) as a *apa- compound, comparing Sanskrit apa-mitya- 'something borrowed, debt' (Kāṭhaka+) from may- 'to exchange', Parth. ʾbʾmyh, Sogd. pʾmytʾy/pʾmytk 'loan' and Bactrian βαμδοιγο 'loan', and states in as many words that 'the etymology and reconstruction given by Nyberg 1974: 22a … from partic. med. *(ā-)apamna-, is less convincing'. The Sanskrit parallel apamitya- is decisive for Cheung because it gives a perfect semantic and morphological match ('borrowing' = 'exchanging away'), whereas *apamna- would be a unique formation. The modern standard therefore prefers a different origin, so the arrow root→apām is disputed; note that the two etymologies share the preverb *apa- and differ only in the verbal roo…
80	REF: BQT:2254=supports: BQT vol.4 [pdf page 337] = printed p.2254, Mo'in's footnote 6 to وام: 'وام (م.) < فام < با… ; SNS:14=not_found: Same as node 1: SNS_pages.txt ff-leaf 29 (≈p.14) is the ab-/af-/ag- stretch of Tavoosi's g…
81	CON: PHD=supports: MacKenzie: 'abām [ʾpʾm | P ʾbʾmyh, N (a)wām] loan, debt.' — form, meaning and the Parthian… ; NYB=supports: 'apam [ʾpʾm] debt 70⁵. — < OIr *apamna- "that which a p. (the lender) has to obtain (from … ; CHEUNG=contradicts: Under *Hap/f: 'ç On Pth. ʾbʾmyh, BMP ʾpʾm /abām/, NP avam "debt" see *Hmai¹.' Under *Hmai¹… ; HRN=partial: Horn: 'ewām, awām "Schuld", wām. phlv. āpām (PPGL). bel. LW. wām.' Then on p.31: 'Darmeste… ; HUB=silent: grep -i 'awam|āpām|apām' in HUB.txt returns nothing relevant (only *drawam); Hübschmann do…
82	------------------------------------------------------------
83	# 3 Persian | vâm «وام» : loan ; avâm «اوام» : loan | verdict: confirmed | 
84	DER: The Middle Persian→New Persian step is beyond doubt: MP ʾpʾm /abām/ > early NP اوام/آوام awām, āvām (the regular treatment of postvocalic MP -b- as -w-), whence by aphaeresis of the unstressed initial a- the standard form وام wām, already the normal word in the 10th-11th c. (Farrokhi Sistāni: هزار بوسه فروشم بر لب تو مرا / تو وام‌دار منی خیز و وام من بگزار; Ferdowsi, quoted by Nourai: درم خواست فام از پی شهریار). The by-form فام fām listed by Nourai as 'فام ۲' is recorded by Borhān and by Mo'in's footnote in the chain وام < فام < بام < اوام, a spelling variant with f- for the older w-/b-. Mo'in glosses avām and vām identically as 'قرض، دین'. Only the ultimate parentage of MP abām (node 2) is disputed; this edge is not.
85	REF: SNS:14=not_found: As for nodes 1-2: the Šāyast nē Šāyast glossary (SNS_pages.txt ff-leaf 29 ≈ p.14) yields n… ; BQT:2254=supports: BQT vol.4 [pdf page 337] = printed p.2254 s.v. وام, Mo'in's footnote: 'وام (م.) < فام < با… ; AEF:173=not_checked: Khaleqi-Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian translation/expansion of Horn) is not…
86	CON: PHD=supports: 'abām [ʾpʾm | P ʾbʾmyh, N (a)wām] loan, debt' — MacKenzie himself gives the New Persian ou… ; NYB=supports: 'Paz. āwām; NP vām, āvām' — the three-way set Pazand āwām / NP vām / NP āvām matches the c… ; CHEUNG=partial: '*NWIR: (+ *ā-apa-) NP avam "debt"' — Cheung has the same NP form and the same MP antecede… ; HRN=supports: 'ewām, awām "Schuld", wām. phlv. āpām' — Horn lists exactly the New Persian forms of this …
87	------------------------------------------------------------
88	# 4 Pahlavi | ayâf, ayâb : to find | verdict: confirmed | 
89	DER: Book Pahlavi ʾyʾp-tn' /ayāftan/, present stem ʾyʾb- /ayāb-/ 'to obtain, acquire, attain' continues Old Iranian *abi-āp- (preverb *abi- 'to, upon' + the root *(H)āp- of node 1). *abi- regularly loses its -b- before a vowel in Middle Persian and contracts to ay- (Nyberg: 'ay- probably < abi-, cf. Av. avi-ap-'); the root vowel is lengthened in the compound (ā-p-). The two stems Nourai lists are the standard Middle Persian stem pair: past ayāft (< *āpta-, with *pt > ft) beside present ayāb- (< *āpa-, with intervocalic *p > β > b). Manichaean MP has the same ʾyʾb-/ʾyʾpt, and Parthian shows the parallel pari-compound pryʾb-.
90	REF: FFD:82=supports: FFD_pages.txt [pdf page 87] = printed p.82: 'یافتن — یافت < فارسی میانه ayāft < ایرانی باس…
91	CON: PHD=supports: MacKenzie: 'ayāftan, ayāb- [ʾyʾp-tn' | M ʾyʾpt, ʾyʾb-, N yāftan, yāb-] obtain, acquire, at… ; NYB=supports: 'ayāft [yʾpt'] gain, benefaction, from ayāftan ayāb-, to reach, to attain … NP yāftan yāb-… ; CHEUNG=supports: '*MIDDLE PERSIAN: (+ *abi-) MMP ʾyʾb- "to obtain, acquire, attain; to achieve success", BM… ; BRT=partial: Bartholomae has the simple verb ap- (apayeiti) and the noun ayapta- 'Belohnung, Wunschgewä…
92	------------------------------------------------------------
93	# 5 Persian | yâftan «یافتن» : to find ; yâbîdan «یابیدن» : to find | verdict: confirmed | 
94	DER: NP یافتن yāftan / یاب- yāb- is MP ayāftan / ayāb- with loss of the unstressed initial a- (the same aphaeresis as in awām > wām, node 3); the older ayāftan survives in Pahlavi Psalter and Manichaean spellings and in the noun آیفت āyift. The stem alternation yāft ~ yāb reflects *-pt- > -ft- versus intervocalic *-p- > -b-. یابیدن yābīdan is a late, secondary infinitive built inside New Persian on the present stem yāb- with the productive -īdan suffix (the same pattern as دانستن/دانیدن), not an independent inheritance — Nourai's box does not distinguish the two, which is a small imprecision but not an error of derivation. Semantically 'attain, obtain' > 'find' is already complete in Middle Persian.
95	REF: BQT:2419=supports: BQT vol.4 [pdf page 502] = printed p.2419, Mo'in's footnote 5: 'یافتن — بفتح چهارم، از: یا… ; FFD:82=supports: FFD_pages.txt [pdf page 87] = printed p.82 s.v. یافتن, as quoted at node 4: NP یافتن < MP …
96	CON: HRN=supports: Horn: 'yāften "erlangen, erreichen, erfinden", Praes. yāb-em … aw. vergl. ayapta- "Belohnu… ; PHD=supports: MacKenzie explicitly equates the Pahlavi verb with 'N yāftan, yāb-'. ; CHEUNG=supports: Cheung 2007 is the source Wiktionary cites for NP یافتن < MP ayāftan < *Habi- + *Hap- 'to … ; HUB=silent: grep for 'yäften|jäften|ayäftan' in HUB.txt returns nothing; Hübschmann's discussion (cite…
97	------------------------------------------------------------
98	# 6 Latin | apere : to bind, attach, reach ; aptus : fit, suited ; ad-apt-are : to fit, adapt ; ad-eptus : reached ; apex : something, reached, apex ; co-apere : bond together, couple | verdict: confirmed | 
99	DER: Latin has the root in two guises: an obsolete *apiō, apere 'to fasten, bind, attach' (surviving in the imperative gloss ape 'prohibē, compescē' and in the participle aptus 'joined, fitted, suited'), and the inchoative apīscor, aptus sum 'to reach, get hold of', with the prefixed compound adipīscor, ad-eptus 'to attain, reach' (ad- + apīscor, with the regular weakening of medial a to e in an open syllable: ad+aptus > adeptus). From the participle aptus is built the denominative aptāre 'to fit', whence ad-aptāre 'to adjust, fit to'. Latin apex, apicis 'point, tip; the rod-like ornament on a priest's cap' is assigned to this root by Pokorny only with 'vielleicht' ('< something reached'), which is why Watkins prints it as sense 3 but Ernout-Meillet leave it doubtful. 'co-apere' is a reconstruction, not an attested Latin verb: what is attested is cōpula < *co-apula, a diminutive noun formed from the stem of apiō with co(m)- 'together'; Nourai's box would be more accurate as *co-ap- / cōpula.
100	REF: POK:50=supports: POK_01.txt ff-page 59-60 (printed 50-51): 'lat. apiscor "fasse, erreiche", adipiscor "erla… ; AHD=supports: AHD_watkins1985.txt s.v. ap-¹: '1. Latin apere, to attach, join, tie to … 2. Latin apisci,… ; KLN:22,24,96=supports: All three pages check out in KLN_1966.txt. p.22-23 (ff-leaf 23): 'adapt, tr. v. — F. adapt…
101	CON: LAT=supports: 'Apiō a un inchoatif apiscor, -eris, aptus sum … Apiscor … a fourni les composés adipiscor… ; WLD=supports: 'Lat. apiscor "fasse, erreiche", adipiscor "erlange", coepi … Zusammenhang mit lat. *apio,… ; LEW=silent: grep -n 'apiscor' in LEW_1910.txt returns no hit; the a- fascicle is missing or unreadable…
102	------------------------------------------------------------
103	# 7 English | apt, aptitude ; adapt, adept, inept ; apex, attitude ; couple | verdict: confirmed | 
104	DER: All eight words descend from the Latin material of node 6, mostly through French: apt (mid-14c.) from OFr. ate or directly from L. aptus; aptitude from Fr. aptitude < Late Latin aptitūdō; attitude (1660s) via Fr. attitude < It. attitudine < the same Late Latin aptitūdinem, so a doublet of aptitude (the -pt- > -tt- assimilation happened in Italian); adapt from Fr. adapter < L. adaptāre; adept from L. adeptus (the past participle of adipīscor, taken over as a noun/adjective in 17th-c. alchemical Latin adeptus 'one who has attained'); inept from L. ineptus (in- + aptus, with the same a > e weakening); apex directly from L. apex; couple (late 13c.) from OFr. cople < L. cōpula < *co-ap- 'to take together'.
105	REF: AHD=supports: AHD_watkins1985.txt s.v. ap-¹ lists as English derivatives: 'APT, (APTITUDE), ATTITUDE; (I… ; KLN:96=supports: KLN_1966.txt ff-leaf 62 (printed page 96) s.v. apt: 'Cp. adapt, adept, apex, aptitude, att…
106	CON: KLN=supports: See the ref_check quotes; Klein covers every word of the box and derives them all from L. … ; SKT=silent: grep for 'apt'/'balas' in SKT.txt returns no usable entry in this OCR (the file appears to… ; AHD=supports: Same list as in ref_check — Nourai's English node is a transcription of Watkins' derivativ…
107	================================================================================
108	ENTRY 2 | root: Apânk | verdict: plausible | modern: Avestan apāṅk- / apąnc- 'turned backwards, facing away' (= *apa 'away, behind' + *anč-/ak- 'to bend, be directed'; cf. Skt. apā́ñc- 'turned away, backward'); the sense 'north' belongs only to the derivative apāxtara-
109	NOTE: The root box is real but its gloss telescopes two stages. Avestan apāṅk- itself means 'turned backwards / directed away' (Buck: 'apāṅk- "turned backwards", adv. "back"'); 'north' is the meaning of the derived adjective apāxtara-/apāxaδra- 'northern', and it means 'north' only because of the Avesta's southern orientation, in which the north is 'the region behind you' and the abode of the daēvas and of hell. Language label 'Avestan' and the reference SYN:873 are both exact. The chart's real problems are further down: (a) the Balkh branch (nodes 3-4) attaches the city name Bactria/Balx to apāxtar, which no Iranist accepts; (b) the ruby chain (nodes 4-7) goes through Badaxšān, not Balx, as Mo'in's own footnote in Borhān says; (c) the Sogdian node is a cognate of axtar, not a derivative of apāṅk-, which Nourai's own note concedes. On the note at node 2, IEC:260: Mann does link Persian axtar with the 'star' root (see there), but Mann's supporting form 'Av. axtarō' is not an attested Avestan word, and the current view (Eilers, EIr III/2 p.123 s.v. AXTAR) is a backformation from abāxtar 'planet' — i.e. modern scholarship sides with Nourai's arrow, not with Mann.
110	ROOTREF: SYN:873=supports
111	------------------------------------------------------------
112	# 1 Pahlavi | apâxtar : north, north star ; axtar : star | verdict: plausible | 
113	DER: Middle Persian ʾpʾhtl /abāxtar/ continues Av. apāxtara- unchanged except for the regular lenition of intervocalic *p to β/b: *apāxtara- > abāxtar. In Pahlavi it is in fact two lemmas: ¹abāxtar 'planet' (the planets are the 'backward-moving' bodies, because of their retrograde motion, and in Zoroastrian cosmology they are demonic) and ²abāxtar 'the north'. Nourai's gloss 'north, north star' is therefore half right: the second sense is 'planet(s)', not 'north star' — MacKenzie: '¹abāxtar [ʾpʾhtl | M ʾbʾxtr] planet. ²abāxtar [ʾpʾhtl | (N bāxtar "west")] north'. The step abāxtar > axtar 'star, constellation, sign of the zodiac' that Nourai draws is a specific and defensible hypothesis, not a self-evident sound change: Eilers (EIr s.v. AXTAR, followed by Wiktionary) explains axtar as an old backformation from abāxtar 'planet', the initial ab- having been reanalysed as the privative prefix a(b)- — 'un-stars' — because Zoroastrianism treats the planets as maleficent non-stars. Both MacKenzie and Nyberg list axtar as an independent lemma without an etymology, so the arrow is a hypothesis they neither state nor contradict.
114	REF: SYN:870=partial: SYN.txt: printed p.870 (ff-leaf ~940) carries the §12.45 EAST / §12.46 WEST word-table; th… ; BQT:99=supports: BQT vol.1 ff-leaf 301 (printed p. ≈93-99 by the drifting leaf offset; the entry اختر with … ; FSF:58=supports: FSF_pages.txt ff-leaf 73-74 (≈ printed pp.57-58) s.v. باختر: quotes Marquart's Ērānšahr fo…
115	CON: PHD=partial: '¹abāxtar [ʾpʾhtl | M ʾbʾxtr] planet. ²abāxtar [ʾpʾhtl | (N bāxtar "west")] north.' and se… ; NYB=partial: 'apaxtar [ʾpʾhtl] 1. planet … 2. the north. — Av. apāxtara- "northern"; MPrs ʾbʾxtr; Paz. … ; BRT=partial: BRT.txt's OCR of the apāxtara- column is unusable, but the word is quoted in the citation … ; IEC=contradicts: 'oster- (osteren-, ster-) "star". WP II, 635 … Av. stārō, acc. stārəm beside axtarō, id.; …
116	------------------------------------------------------------
117	# 2 Persian | bâxtar «باختر» : north ; axtar «اختر» : star, fate | verdict: plausible | 
118	DER: NP باختر bāxtar is MP abāxtar with the usual New Persian aphaeresis of the unstressed initial a- (compare abām > wām at entry 0 node 3; here ab- > b-). The semantic history is the problem: in the Avesta and in Pahlavi the word means 'north', and Ferdowsi and the Tārīkh-e Sīstān still use it that way ('هر چه حد شمال است باختر گویند'), but in New Persian generally — and in the modern standard language exclusively — باختر means 'west', paired against خاور 'east'; a few early poets even reverse the pair and use باختر for 'east'. Mo'in states this explicitly. Nourai's gloss 'north' is therefore the correct oldest sense but not the ordinary Persian one, which is why MacKenzie and Nyberg gloss the New Persian reflex 'west' / 'the west or the east'. NP اختر axtar 'star, constellation; horoscope, fortune' is MP axtar unchanged; the 'fate/fortune' sense is a natural astrological extension already visible in the Pahlavi compound axtar-mār 'astrologer' and in Ferdowsi's line quoted in the chart ('نبینم همی اختر خویش بد'), and it survives in the derivative اخترشناس axtar-šenās 'astronomer/astrologer' that Nourai lists.
119	REF: BQT:99=partial: The اختر half is confirmed at BQT vol.1 ff-leaf 301 (see node 1): 'اختر … رایت و علم را گو… ; FSF:58=supports: FSF_pages.txt ff-leaf 73-74 s.v. باختر, quoted at node 1: Noushin's Shāhnāme glossary expl…
120	CON: MON=partial: 'باختر: در اوستا اپاختره به معنی شمال آمده و جایگاه اهریمن و دیوان و دوزخ دانسته شده، در پ… ; NYB=partial: 'NP bāxtar "the west" or "the east"' — Nyberg records the New Persian meanings as west/eas… ; PHD=partial: MacKenzie's bracket '(N bāxtar "west")' gives the same warning about the New Persian value… ; IEC=contradicts: Mann's linkage of Persian axtar with sitāre and the *ster- root (the dispute recorded in N…
121	------------------------------------------------------------
122	# 3 Pahlavi | bâxtri, bâxr, balx : a city north of the ancient Iran | verdict: disputed | 
123	DER: The city and province name is genuinely old — Old Persian Bāxtriš (Bisotun I.16, in the list of satrapies), Avestan Bāxδī-/Bāxtrī-, Greek Βακτρία/Βάκτρα, Middle Persian Baxl [bʾhl], New Persian Balx — but it has nothing to do with apāxtar 'north'. Its own etymology is unsettled (it is not a transparent Iranian formation); the -xtr- of Bāxtriš and the -xtar of abāxtar look alike only by accident, since abāxtar is *apa- plus a comparative-type suffix, while Bāxtriš has no *apa- and no -tara-. The Middle Persian development *Bāxδī > Baxl (with -δ-/-r- > -l-) then NP Balx is entirely different from abāxtar > bāxtar. Nourai's middle form 'bâxr' is not an attested word: the Pahlavi form is Baxl (Nyberg, glossary p.72 s.v. Baxl), and 'bâxr' is almost certainly a slip for bâxl. Verdict: the node's words are (with that correction) real, but the edge apāxtar → Bāxtrī/Balx is rejected.
124	REF: MON5:275=not_checked: Mo'in's Farhang vol. 5 (اعلام, proper names) is not in the local library and not online: t… ; BQT:297=partial: BQT vol.1 ff-leaf 517 (≈ printed pp.293-297) does carry the headword بلخ: 'بلخ — بفتح اول …
125	CON: NYB=contradicts: 'Baxl [bʾhl] Balkh 113². — Av. Bāxtrī-, Bāxδī-; NP Balx.' Nyberg derives Balkh from the Av… ; KNT=contradicts: Kent's text of Bisotun I.16 reads '… Parθava : Zraka : Haraiva : Uvārazmiy : Bāxtriš : Sug… ; BRT=silent: The Bāxδī- column is not recoverable from BRT.txt's OCR; no direct quotation possible.
126	------------------------------------------------------------
127	# 4 Persian | balx «بلخ» : an ancient city in Iran famous for its rose-red ruby gems | verdict: disputed | 
128	DER: NP بلخ Balx < MP Baxl < Av. Bāxδī-/OP Bāxtriš is a sound chain, but the second half of the gloss is wrong and it is what carries the rest of the chart: the rose-red spinel of the medieval gem trade is the stone of بدخشان Badaxšān, the district on the upper Oxus in what is now north-eastern Afghanistan, not of Balkh. The gem name is بلخش balaxš ~ بلخشان balaxšān, a variant of بدخشان (Nourai lists both in his script extras). Mo'in himself, in the footnote to بدخش in the very dictionary Nourai cites, quotes Barthold (EI s.v. Badaxšān) and Marquart (Ērānšahr 279) to exactly this effect and says that balaxš was probably first the name of the district and only later of the stone found there. The similarity of Balx and balaxš is coincidental (and encouraged the medieval confusion), so the arrow Balx → Arabic balaxš is rejected.
129	REF: MON5:247=not_checked: As at node 3: Mo'in's vol. 5 (اعلام) is not available locally or online; the local Mo'in l…
130	CON: BQT=contradicts: Mo'in's footnote 8: 'مارکوارت (Ērānšahr) گوید که بدخشان بمعنی «بلاد بذخش balaxš» است و آن … ; KLN=contradicts: 'balas, n., a variety of spinel ruby. — F. balais, fr. Arab. balakhsh, fr. Balakhshān, fr.… ; LKT=contradicts: Lokotsch: 'N. pr. Name des nordöstlichen Teiles des heutigen Afġānistān. Von hier bezog ma… ; AFM=partial: '(اللقار) وهو … في بلخشان، والعجم يقولون له بدخشان (شفاء الغليل) … بدخشان … بلاد بين خراسا…
131	------------------------------------------------------------
132	# 5 Arabic | balaxš : ruby | verdict: plausible | 
133	DER: Arabic بَلَخْش balaḵš 'balas ruby, rose-red spinel' is real and is indeed the form from which the European words were taken, so the node itself is right and its position between the Persian and the Old French node is right. What is wrong is its parent: Arabic balaḵš is a borrowing of Persian بلخش balaxš, a shortened/dissimilated variant of بدخشان Badaxšān (the gem-bearing district), not of بلخ Balx. Arabic geographers write both بلخشان and بدخشان for the same place (Addi Shir, quoting Šifāʾ al-ġalīl: 'والعجم يقولون له بدخشان'), which shows the two are the same name; the stone was then named for its provenance, the standard pattern for medieval gem names. Since Arabic balaḵš is not a native Semitic root formation but a place-name loan, the label 'Arabic' is best read as 'Arabic transmission of a Persian toponym'.
134	REF: AHD:101=partial: Checked in the online American Heritage Dictionary (the local AHD file holds only the Watk…
135	CON: KLN=partial: 'F. balais, fr. Arab. balakhsh, fr. Balakhshān, fr. Pers. Badhakhshān' — Klein has the Ara… ; DEV=partial: 'Balais (Rubis). Esp. balax, balaxo, balaja; portug. balax, ital. balascio, bas lat. balas… ; AFM=supports: Attests بلخشان alongside بدخشان in the Arabic lexicographical tradition (see node 4), i.e.… ; PLA=silent: grep for balaḫš/balahs/Badaḫšān in PLA_asbaghi_1988_ia_djvu.txt returns nothing; Asbaghi d…
136	------------------------------------------------------------
137	# 6 Old French | balais : ruby | verdict: confirmed | 
138	DER: Old French balais (also rubis balais), 13th c., is the Arabic balaḵš adapted to French phonology: the Arabic cluster -ḵš is simplified and the word is refashioned with the productive adjectival ending -ais (as in the parallel Medieval Latin balascius, Italian balascio/balasso, Spanish balax/balaja, Catalan balaix, Portuguese balais). It reached the West through the Levantine gem trade — Marco Polo already calls the country Balasian and the stones balaxi/balasci. In French the word is an adjective qualifying rubis, exactly as in English 'balas ruby'.
139	REF: AHD:101=supports: AHD s.v. balas: '[Middle English, from Old French balais and Old Spanish balax, from Medie…
140	CON: PHN=supports: Pihan lists BALAIS among the French words of Persian origin and gives 'balais, en persan ب… ; DEV=supports: 'De l'arabe بلخش balakhch, venant du persan بدخشان badakhchân, nom du pays d'où l'on tire … ; LKT=supports: 'Über das ar. balaḫš ergab sich als Bezeichnung für eine Rubinart … frz. prov. balais; dts… ; KLN=supports: 'F. balais, fr. Arab. balakhsh'.
141	------------------------------------------------------------
142	# 7 English | balas : a rose-red gem | verdict: confirmed | 
143	DER: Middle English balais/bales, borrowed from Old French balais (with support from Old Spanish balax and Medieval Latin balascus), gives modern English balas, now used almost only attributively in 'balas ruby'. The referent is a rose-red to orange spinel, distinguished from true ruby only after the 18th century — which is why the older English texts treat it as a kind of ruby, exactly Nourai's gloss 'a rose-red gem'.
144	REF: AHD:101=supports: AHD s.v. balas: 'A rose-red to orange spinel used as a semiprecious gem, once confused wit…
145	CON: KLN=supports: 'balas, n., a variety of spinel ruby. — F. balais …' ; AHD=supports: See ref_check; the online AHD is the current edition of the dictionary whose 1975 New Coll… ; SKT=silent: No 'balas' entry recoverable from SKT.txt (grep returns nothing).
146	------------------------------------------------------------
147	# 8 Sogdian | anxar, `ngr : star | verdict: plausible | 
148	DER: Sogdian ʾnγr /anɣar/ 'star' is correctly cited (Gharib no. 1008, Buddhist Sogdian, attested in the Vessantara Jātaka and in the Paris Sogdian texts), and the compounds confirm the meaning: no. 1014 ʾnγrksʾy anɣar-kase 'astrologer' and no. 1017 ʾnγrwzn anɣar-wazan 'zodiac, constellation', which Gharib himself equates with Parthian axtar-wazan. That equation is the point: Sogdian anɣar corresponds to Middle Persian/Parthian axtar, so it belongs with node 1's axtar, not directly under Avestan apāṅk-, and Nourai's own note ('This may be a cognate rather than a derivative') concedes as much. Gharib offers only a tentative *ana-har with a question mark; a derivation from *apāṅk-/*apāxtara- would not yield Sogdian ʾnγr (there is no trace of the *p and no *-tar- suffix). So: the word and gloss are right, the drawn edge is not a derivation but at best a cognate relation.
149	REF: SOD:39=supports: SOD_pages.txt, entry '1008 ʾnγr B — anxar ⊙<*ana-har ? ⊙pl. -t =ʾnxr — star. VJ 25, 17; TS…
150	CON: SOD=partial: Confirms the form and the gloss 'star', but proposes '<*ana-har ?' — not a derivation from… ; NYB=partial: Nyberg keeps Middle Persian axtar and apaxtar apart; the Sogdian word matches the former, … ; ISS_alt_DKS=silent: No Khotanese cognate of anɣar found; nothing bearing on this node.
151	
```


## [2026-09-04T23:14:48.034Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p57.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشهٔ Angh نورایی همان *h₂enǵʰ- هندواروپایی آغازین به معنی «تنگ کردن، فشردن؛ تنگ و دشوار» است؛ پوکورنی در صفحات ۴۲–۴۳ آن را با عنوان «angh- ‚eng, einengen, schnüren‘» آورده و همان شاخه‌هایی را برمی‌شمارد که نورایی کشیده است — فعل‌های اوستایی، لاتینی ango/angustus و ژرمنی angr/angust. پس صورت ریشه، برچسب زبانی و معنا هر سه درست است. دو نکتهٔ سراسری اما هست: نخست آنکه صورت اوستاییِ چاپ‌شده در کتاب، «azaehě»، واژهٔ اوستایی نیست و تصویر صفحه نشان می‌دهد که خودِ کتاب چنین چاپ کرده — یعنی خطای خودِ نورایی است نه خطای خوانشِ اسکن — و صورت درست ǫzaŋhē است. دوم آنکه شاخهٔ نیاز/ni-āz در ایران‌شناسی امروزی به ریشهٔ دیگری بسته می‌شود: چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (۲۰۰۷، ص ۱۷۱–۱۷۲) نیاز را زیر *Haz «راندن، بردن» می‌آورد نه زیر *angh-؛ بارتولومه، والده-پوکورنی و معین با نورایی هم‌داستان‌اند و تنها چونگ مخالف است.\",\n\"1\": \"ریشهٔ Angwhi همان *h₂éngʷʰis هندواروپایی آغازین به معنی «مار» است و جعبهٔ ریشه فی‌نفسه درست است (پوکورنی ۴۳–۴۵؛ واتکینز «angʷhi-. Snake, eel»). آنچه این جعبهٔ یگانه پنهان می‌کند، دوگانگی‌ای است که خود پوکورنی در نخستین سطر اعتراف می‌کند: دست‌کم دو خانوادهٔ ریشه‌شناختیِ متفاوت در کارند که زود در هم آمیخته‌اند. دستنامه‌های امروزی *h₂éngʷʰis (لاتینی anguis، لیتوانیایی angis، اسلاوی کهن) را از *h₁ógʷʰis / *h₃égʷʰis (سنسکریت áhi-، اوستایی aži-، یونانی ὄφις، ارمنی iž) جدا می‌کنند، و شاخهٔ اوستاییِ این نمودار در واقع به دستهٔ دوم، یعنی صورتِ بدون نون، تعلق دارد. افزون بر این، والده-پوکورنی (ج ۱ ص ۶۵) این پندار قدیمی را که *angʷhis «مار» مشتقی از ریشهٔ همسایهٔ angh- «فشردن» باشد صریحاً رد می‌کنند — نکته‌ای که در همین صفحه اهمیت دارد، چون نورایی Angh و Angwhi را کنار هم نهاده است.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"دو مطلب در این جعبه است. نخست «azaehě» که صورتی مخدوش از اوستایی متأخرِ ǫzaŋhē است، مصدرِ فعل ǫz- «تنگ بستن، به تنگنا افکندن» (بارتولومه: «zu bedrängen, in Not zu bringen»، یشت ۱۳٫۳۹)، در کنار اسمِ ستاک-s یعنی ǫzah- «خفه‌کردن گلو؛ تنگنا و نیاز». از نظر آوایی *h₂enǵʰ- هندواروپایی به ایرانی آغازین *anź- و در اوستایی به ǫz- رسیده است (نون پیش از سایشی به شکل واکهٔ خیشومی ǫ نوشته می‌شود)، برابر دقیق لاتینی angō و سنسکریت áṃhas-. دوم ni-āz، که همان ǫz- است با پیشوند ni- در درجهٔ کشیده و تنها در صورت‌های صرف‌شده گواه دارد (ni-āzata «کمر را تنگ بست»، یشت ۵٫۱۲۷)؛ اسمی اوستایی به معنی «نیاز» وجود ندارد و معنایی که نورایی می‌دهد در حقیقت واپس‌افکنیِ مفهوم فارسی میانه است. پس گرچه پوکورنی و بارتولومه پیوند این صورت‌ها را با ریشه تأیید می‌کنند، صورت چاپیِ کتاب ناممکن است و چونگ نیز کل شاخه را به ریشهٔ دیگری می‌برد؛ از این رو حکم «مورد اختلاف» است.\",\n\"2\": \"فارسی میانه niyāz (پهلوی کتابی ⟨nydʾc⟩، فارسی میانهٔ مانوی و پارتی ⟨nyʼz⟩) «نیاز، حاجت، تنگدستی» با مشتقاتش نیازومند و ابی‌نیاز، از نظر ساخت اسمِ مصدری از ایرانی باستان *ni-āza- است: پیشوند ni- به‌علاوهٔ درجهٔ کشیدهٔ ā که میان i و ā واج میانجی y می‌گیرد، و z میان‌واکه‌ای برجای می‌ماند و در پهلوی کتابی با ⟨c⟩ نوشته می‌شود. قدمت واژه را وام‌واژهٔ ارمنیِ عهد اشکانی apeniaz «بی‌نیاز» (هوبشمان، مطالعات فارسی، بند ۹۱) و نیز سغدی nyʼz گواهی می‌کند. تنها ریشهٔ نهایی محل بحث است (گرهٔ ۱)؛ در اینکه niyāz فارسی میانه از ni- و ستاک āz- ساخته شده همه، از جمله چونگ، هم‌داستان‌اند، پس این پیوند درست است.\",\n\"3\": \"«نیاز» فارسی نو همان niyāz فارسی میانه است که بی‌دگرگونی به دری رسیده، با صفتِ مشتقِ «نیازمند/نیازومند» (برابر niyāzōmand پهلوی) و معنای دینیِ دورهٔ اسلامی، یعنی «نذری که برای برآمدن حاجت می‌دهند» (معنای دومِ معین). واژهٔ دومِ جعبه، «نیازی» به معنی «دوست و معشوق»، مدخلی جداگانه در سنت فرهنگ‌نویسی است: اسدی طوسی در لغت فرس «نیاز، دوست بود» آورده و رشیدی تصحیح کرده که «بمعنی دوست، نیازی است نه نیاز» — و بیت عثمان مختاری («دلم خستهٔ ناز توست ای نیازی») همین کاربرد را نشان می‌دهد. از نظر معنایی «نیازی» یعنی آنکه بدو نیاز دارند. ادعای نورایی در این گره درست است.\",\n\"4\": \"این جعبهٔ خالی نمایندهٔ شاخهٔ لاتینیِ ریشه است: فعل angō, -ere «سخت فشردن، خفه کردن؛ به تنگ آوردن» (برابر دقیق یونانی ἄγχω و اوستایی ǫzaŋhē)، اسم‌های angor «تنگیِ گلو، اندوه» و angina، صفت anxius (< *angh-s-io-) و صفت ستاک-s یعنی angustus < *angh-os-to-s «تنگ» با اسم مصدر angustia «تنگنا، سختی». ارنو-مه‌یه تأکید می‌کنند که آن دوگانگی معناییِ «جسمی/روحی» که نورایی بدان نیاز دارد در درون خودِ لاتینی پدید آمده است. هر دو واژهٔ انگلیسیِ جعبهٔ فرزند از همین مادهٔ لاتینی برخاسته‌اند؛ ادعای نورایی درست است.\",\n\"5\": \"دو راهِ متفاوت از جعبهٔ لاتینی بیرون می‌آید. anxious وام‌واژه‌ای کتابی از سده‌های شانزدهم و هفدهم است، یکراست از لاتینی anxius با جانشینیِ پسوند انگلیسیِ ous- به جای us- لاتینی (و همچنین anxiety از anxietas). اما anguish از راه مردمی آمده است: لاتینی angustia «تنگنا» > فرانسوی کهن anguisse/angoisse (سدهٔ دوازدهم) > انگلیسی میانه anguise (حدود ۱۲۰۰). سیر معنایی روشن است: «تنگی و خفگی» ← «تنگنا و سختی» ← «رنج روحی». ادعای نورایی درست است.\",\n\"6\": \"جعبهٔ خالیِ شاخهٔ ژرمنی: صفت *angwuz «تنگ» (گوتی aggwus، نورس کهن ǫngr، انگلیسی باستان enge، آلمانی eng) دنبالهٔ *anghu- است؛ اسم ستاک-s یعنی *angaz- (< *anghos-، همان ساختی که در áṃhas- سنسکریت و angor لاتینی دیده می‌شود) در نورس کهن angr «اندوه، رنج» شده؛ و *angusti- در آلمانی علیای باستان angust و آلمانی امروز Angst بازتاب یافته است. جعبهٔ نورایی تنها به anger انگلیسی می‌رسد، یعنی به بازتابِ نورسیِ angr؛ ادعای او درست است.\",\n\"7\": \"anger واژه‌ای بومیِ انگلیسی نیست: انگلیسی میانه angre (میانهٔ سدهٔ سیزدهم، نخست به معنی «رنج و مصیبت») وام‌واژه‌ای است از نورس کهن angr «اندوه، آزار» که در ناحیهٔ دِین‌لا (Danelaw) گرفته شده است، از همان لایهٔ وام‌واژه‌های اسکاندیناویایی که ill و skin و take بدان تعلق دارند. پایهٔ ژرمنیِ آغازین *angaz < *anghos- است. تحول معنایی از «آزار وارده» به «خشمی که آن آزار برمی‌انگیزد» رخ داده و تا آغاز سدهٔ چهاردهم معنی «خشم» تثبیت شده است. ادعای نورایی درست است.\"\n},\n\"1\": {\n\"1\": \"هر دو واژه اصیل‌اند: اوستایی aži- (ستاک ažay-) «مار» و به گسترش «اژدها، هیولا» — بارتولومه آن را جانوری دیوآفریده می‌شمارد — و هم‌ریشهٔ دقیق سنسکریت áhi-، یونانی ὄφις، ارمنی iž و لاتینی anguis است. aži.dahāka- همان مارِ سه‌سرِ یشت‌ها و یسنا ۹٫۸ است که فریدون (Θraētaōna) او را فرومی‌گیرد، و ضبط «aži-dahâkô» نورایی صورت فاعلیِ مفردِ ažiš dahākō است، همان‌گونه که هرن و هوبشمان آورده‌اند. اما حکم تنها «با احتیاط پذیرفتنی» است، زیرا پیکانی که از جعبهٔ ریشه کشیده شده با بازسازیِ امروزی نمی‌خواند: aži- اوستایی به ایرانی آغازین *Háǰiš و از آنجا به *h₁ógʷʰis می‌رسد، یعنی به گونهٔ بدون نون؛ خودِ پوکورنی نیز آن را در بند *ogʷhi- (ص ۴۴) در کنار ὄφις یونانی آورده است، حال آنکه anguis لاتینی سرِ بندِ *angʷhi- می‌ایستد.\",\n\"2\": \"ایرانی باستان aži-dahāka- در فارسی میانه به až(i)dahāg بدل شده و از آنجا با افتادن قاعده‌مندِ -g پایانی و سایش انسدادیِ میان‌واکه‌ای «اژدها» را داده است؛ صورتِ کامل‌ترِ «اژدهاک» -ک را نگاه داشته و در برهان به «ضحاک ماران» معنی شده است (حاشیهٔ معین: «مخفف اژی‌دهاک، ضحاک»). هرن (شمارهٔ ۷۶) با استناد به وام‌واژهٔ ارمنیِ aždahak نشان می‌دهد که تلفظ اژ- (نه اج-) در دورهٔ اشکانی و ساسانی جا افتاده بوده است. رفت‌وبرگشتِ سامیِ «ضحّاک» که نورایی در جعبه آورده حقیقت دارد و راهش فارسی ← عربی ← فارسی است: اصباغی «ضحّاک» را معرّبِ aždahā می‌داند که با ریشه‌شناسی عامیانه به اسم فاعلِ «خندان» تعبیر شده، و در کنار آن «أزدهاق» را وامی مستقل و دگرگون‌نشده از فارسی ثبت می‌کند. «اژدر» صورت کوتاه‌شدهٔ فارسی است که ترکی ejder و صربی/بلغاری ažder از آن گرفته شده‌اند؛ معنای نظامیِ «اژدر دریایی» ساختی نو در فارسی سدهٔ چهاردهم خورشیدی است. ادعای نورایی درست است.\",\n\"3\": \"لاتینی anguis «مار» بازتاب مستقیمِ گونهٔ نون‌دار *h₂éngʷʰis است و دقیقاً بر لیتوانیایی angis، پروسی کهن angis، لتونیایی uodze و اسلاوی کهن *ǫzь منطبق می‌شود. واژه‌ای کهن و بیشتر دینی و شاعرانه است که در نثر جای خود را به serpēns و uīpera داده است؛ مشتقاتش anguinus و anguilla «مارماهی» است — همان تصویرِ «ماهیِ مارمانند» که در پروسی کهن angurgis و لهستانی węgorz نیز دیده می‌شود. این تنها واژهٔ این نمودار است که بازسازی امروزی هم آن را قطعاً به *angʷʰi- می‌بندد؛ پس ادعای نورایی درست است.\",\n\"4\": \"anguine «مارسان، وابسته به مار» (سدهٔ هفدهم) وام‌واژه‌ای کتابی است، نه واژه‌ای موروثی: مستقیماً از لاتینی anguinus، صفتِ anguis، با انگلیسی‌سازیِ پسوند -inus به -ine؛ و به همین قیاس anguineous از anguineus. واسطهٔ فرانسوی لازم نیست و واژه همواره کتابی مانده است. واتکینز نیز ANGUINE و ANGUILLIFORM را حاصلِ انگلیسیِ این ریشه از راه لاتینی می‌شمارد؛ ادعای نورایی درست است.\"\n}\n}\n}\nEOF\ncat > p58.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشهٔ «Ap 2» نورایی همان *h₁ep- هندواروپایی آغازین به معنی «گرفتن، رسیدن، به چنگ آوردن» است؛ مدخل پوکورنی از پایان صفحهٔ ۵۰ (همان صفحه‌ای که نورایی ارجاع می‌دهد) آغاز می‌شود و به صفحهٔ ۵۱ می‌کشد و همان دو شاخهٔ ایرانی و لاتینی را دربردارد. تنها تصحیح این است که بازسازیِ امروزی حنجریِ آغازین دارد (*h₁ep-)، و همین است که e- در هیتی e-ep-zi و در لاتینی co-ēpī را توضیح می‌دهد. شماره‌گذاریِ «Ap 2» نیز درست است، چون این ریشه را از «Ap 1» یعنی *h₂ep- «آب» جدا می‌کند. ضعف این صفحه در جعبهٔ ریشه نیست، بلکه در شاخهٔ ایرانی است: چونگ (۲۰۰۷) واژهٔ abām «وام» فارسی میانه را یکسره از این ریشه بیرون می‌برد (گرهٔ ۲).\",\n\"2\": \"جعبهٔ ریشه اصیل است اما معنایی که برایش نوشته شده دو مرحله را در هم فشرده است: اوستایی apāṅk- خود یعنی «واپس‌گردانده، رو به پشت» و معنی «شمال» تنها از آنِ صفتِ مشتقِ apāxtara- «شمالی» است، آن هم به سبب جهت‌یابیِ جنوبیِ اوستا که شمال را «سوی پشت سر» و جایگاه دیوان و دوزخ می‌داند. برچسب زبانی و ارجاع SYN:873 هر دو دقیق‌اند. مشکلات اصلی در پایین نمودار است: نخست، شاخهٔ بلخ (گره‌های ۳ و ۴) نام شهر باختری/بلخ را به «اپاختر» می‌بندد که هیچ ایران‌شناسی نمی‌پذیرد؛ دوم، زنجیرهٔ لعل (گره‌های ۴ تا ۷) در واقع از «بدخشان» می‌گذرد نه از بلخ، چنان‌که خودِ حاشیهٔ معین بر برهان می‌گوید؛ سوم، گرهٔ سغدی هم‌ریشهٔ «اختر» است نه مشتقِ apāṅk-، چنان‌که یادداشت خودِ نورایی نیز اذعان دارد. دربارهٔ اختلافی که نورایی از مان (IEC:260) نقل می‌کند نیز باید گفت که صورتِ استنادیِ مان یعنی «Av. axtarō» واژهٔ اوستاییِ گواهی‌شده‌ای نیست و رأی امروزی (آیلرس در ایرانیکا) «اختر» را واپس‌ساختی از «اباختر» می‌داند، یعنی جانب نورایی را می‌گیرد.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"فعل اوستایی ap- «رسیدن، دست یافتن» (ستاک حال apaiia-، سوم‌شخص apaiieiti در یشت‌ها) دنبالهٔ قاعده‌مندِ ایرانیِ *h₁ep- است: *h₁p-eie- > ایرانی *apaya-، با نگاه‌داشتِ p میان‌واکه‌ای در اوستایی. اما «af» و «ab»ی که نورایی در جعبه آورده نه اوستایی‌اند و نه پارسی باستان، بلکه واپس‌افکنیِ برون‌دادهای متأخرِ ایرانی‌اند: p ایرانی باستان پس از واکه از راه β در فارسی میانه و نو پیش از همخوان یا در پایان واژه به f و میان دو واکه به b/w بدل می‌شود (یافت ~ یاب-). پارسی باستان هیچ بازتابِ گواهی‌شده‌ای از این ریشه ندارد (در واژه‌نامهٔ کنت نیست)، پس برچسب «اوستایی/پارسی باستان» بیش از گواهی موجود ادعا می‌کند. ترکیب نیز aiβi-/avi-ap- است و معنایش «به دست آوردن، یافتن» است نه «بازداشتن»؛ تصویر صفحهٔ ۲۸ نشان می‌دهد که «to detain» در خودِ کتاب چاپ شده، پس لغزشِ نورایی است نه خطای استخراج. از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"2\": \"پهلوی کتابی ʾpʾm /abām/ «وام، دِین» به‌خوبی گواهی شده است (مکنزی ص ۴؛ نیبرگ ج ۲ ص ۲۲؛ پارتی ʾbʾmyh). نورایی به پیروی از نیبرگ و معین آن را اسم مفعولِ میانهٔ ایرانی باستان *(ā-)apamna- از فعل ap- «رسیدن، به دست آوردن» می‌داند، یعنی «آنچه وام‌دهنده باید بازستاند». اما چونگ در فرهنگ ریشه‌شناختی فعل ایرانی این تحلیل را رد می‌کند و abām را با پیشوند *apa- زیر ریشهٔ *Hmai «مبادله کردن» می‌نهد و آن را با سنسکریت apa-mitya- «آنچه به وام گرفته شده»، سغدی pʾmytk و بلخی βαμδοιγο می‌سنجد، و تصریح می‌کند که بازسازیِ نیبرگ «کمتر قانع‌کننده» است. برابرِ سنسکریت از نظر معنایی و ساختی کامل است، حال آنکه *apamna- ساختی یگانه و بی‌نظیر می‌بود. پس معیار امروزی سرچشمهٔ دیگری را ترجیح می‌دهد و این پیکان مورد اختلاف است — هرچند دو ریشه‌یابی در پیشوند *apa- مشترک‌اند و تنها در ستاک فعلی اختلاف دارند.\",\n\"3\": \"گذر از فارسی میانه به فارسی نو در این گره تردیدناپذیر است: abām پهلوی نخست به «اوام/آوام» بدل شده (بدل شدن قاعده‌مندِ b پس‌واکه‌ای به w) و سپس با افتادن الفِ آغازینِ بی‌تکیه (تخفیف) صورت «وام» را داده که در سده‌های چهارم و پنجم هجری واژهٔ معمول بوده است (فرخی سیستانی: «تو وام‌دار منی خیز و وام من بگزار»). گونهٔ «فام» را نیز برهان ثبت کرده و معین در حاشیه زنجیرهٔ «وام < فام < بام < اوام» را می‌آورد. تنها تبار نهاییِ abām فارسی میانه (گرهٔ ۲) محل اختلاف است؛ این حلقه بی‌اشکال و ادعای نورایی درست است.\",\n\"4\": \"پهلوی کتابی ʾyʾp-tn' /ayāftan/ با ستاک حالِ ayāb- «به دست آوردن، رسیدن، دست یافتن» دنبالهٔ ایرانی باستان *abi-āp- است، یعنی پیشوند *abi- «بر، به سوی» به‌علاوهٔ همان ریشهٔ گرهٔ ۱. پیشوند *abi- در فارسی میانه پیش از واکه b خود را از دست می‌دهد و به ay- فشرده می‌شود (نیبرگ: «ay- احتمالاً < abi-، سنجیده شود با اوستایی avi-ap-»)، و واکهٔ ریشه در ترکیب کشیده می‌شود. جفت‌ستاکِ ayāft ~ ayāb- بازتابِ دو تحول جداگانه است: *pt > ft در ستاک گذشته و *p میان‌واکه‌ای > β > b در ستاک حال. فارسی میانهٔ مانوی نیز همین ʾyʾb-/ʾyʾpt را دارد؛ ادعای نورایی درست است.\",\n\"5\": \"«یافتن/یاب-» فارسی نو همان ayāftan/ayāb- فارسی میانه است با افتادن الفِ آغازینِ بی‌تکیه — همان تخفیفی که در اوام > وام دیده شد — و صورت کهن‌تر ayāftan هنوز در زبور پهلوی و املاهای مانوی و در اسمِ «آیفت» بازمانده است. نوسان یافت ~ یاب همان دو تحولِ *-pt- > -ft- و *-p- میان‌واکه‌ای > -b- است. اما «یابیدن» مصدری ثانوی و متأخر است که در درون فارسی نو بر ستاک حال یاب- با پسوند زایای -یدن ساخته شده (مانند دانستن/دانیدن)، نه میراثی مستقل؛ نورایی این دو را از هم جدا نکرده که بی‌دقتیِ کوچکی است اما خللی در ریشه‌یابی نمی‌آورد. تحول معناییِ «رسیدن و به دست آوردن» به «یافتن» پیش از فارسی نو و در فارسی میانه کامل شده بود.\",\n\"6\": \"لاتینی این ریشه را به دو صورت دارد: فعلِ متروکِ *apiō, apere «بستن، پیوستن» که تنها در تفسیرِ ape و در اسم مفعولِ aptus «پیوسته، شایسته» بازمانده، و فعلِ آغازیِ apīscor «به چنگ آوردن، رسیدن» با ترکیبِ adipīscor, ad-eptus «دست یافتن» — که در آن a در هجای باز به e تضعیف شده است (ad+aptus > adeptus). از aptus فعلِ اسم‌بنیادِ aptāre و از آن ad-aptāre ساخته شده است. لاتینی apex «نوک، سرِ کلاهِ کاهنان» را پوکورنی تنها با قید «شاید» به این ریشه می‌بندد، از این رو ارنو-مه‌یه آن را مشکوک می‌شمارند. «co-apere» نیز فعلِ گواهی‌شدهٔ لاتینی نیست، بلکه آنچه هست cōpula < *co-apula است؛ جعبه اگر *co-ap-/cōpula می‌نوشت دقیق‌تر بود. با این ملاحظات ادعای نورایی درست است.\",\n\"7\": \"هر هشت واژه از مادهٔ لاتینیِ گرهٔ ۶ برخاسته‌اند، بیشترشان از راه فرانسه: apt (میانهٔ سدهٔ چهاردهم) از aptus؛ aptitude از فرانسوی aptitude < لاتینی متأخر aptitūdō؛ attitude (دههٔ ۱۶۶۰) از راه فرانسوی از ایتالیایی attitudine که خود از همان aptitūdinem است — پس attitude و aptitude دوگانه (doublet) اند و همگونیِ -pt- > -tt- در ایتالیایی رخ داده است؛ adapt از فرانسوی adapter < adaptāre؛ adept از adeptus که در لاتینیِ کیمیاگرانِ سدهٔ هفدهم به معنی «آنکه به مقصود رسیده» به کار رفت؛ inept از ineptus؛ apex یکراست از لاتینی؛ و couple (اواخر سدهٔ سیزدهم) از فرانسوی کهن cople < cōpula. ادعای نورایی درست است.\"\n},\n\"2\": {\n\"1\": \"فارسی میانه ʾpʾhtl /abāxtar/ همان apāxtara- اوستایی است با نرم‌شدنِ قاعده‌مندِ *p میان‌واکه‌ای به β/b. در پهلوی این در حقیقت دو مدخل است: abāxtar «سیّاره» — چون سیّارگان به سبب حرکت رجعیِ خود «واپس‌رونده» و در جهان‌شناسی زردشتی دیوآفریده‌اند — و abāxtar «شمال». پس معنایی که نورایی می‌دهد نیمی درست است: معنای دوم «سیّاره» است نه «ستارهٔ شمالی». گامِ abāxtar > axtar «ستاره، برج» که نورایی می‌کشد فرضیه‌ای مشخص و دفاع‌کردنی است نه دگرگونیِ آواییِ بدیهی: آیلرس (در ایرانیکا) «اختر» را واپس‌ساختی کهن از «اباختر» می‌داند که در آن اب- به‌غلط پیشوند سلبی پنداشته شده، یعنی «ناستارگان». مکنزی و نیبرگ «اختر» را مدخلی مستقل و بی‌ریشه‌شناسی می‌آورند و نه آن را تأیید می‌کنند و نه رد؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"2\": \"«باختر» فارسی نو همان abāxtar فارسی میانه است با تخفیفِ معمولِ الفِ آغازینِ بی‌تکیه (اب- > ب-)، درست مانند اوام > وام. دشواری در تاریخِ معنایی است: در اوستا و پهلوی معنی «شمال» است و فردوسی و تاریخ سیستان هنوز آن را چنین به کار می‌برند («هر چه حد شمال است باختر گویند»)، اما در فارسی نو به‌طور کلی و در فارسی معیارِ امروز منحصراً «مغرب» است در برابر «خاور»؛ چند شاعر متقدم حتی این جفت را وارونه به کار برده‌اند. معین همین را تصریح می‌کند و مکنزی و نیبرگ نیز صورت فارسی نو را «غرب» معنی می‌کنند. پس معنایی که نورایی می‌دهد کهن‌ترین معناست نه معنای رایج. «اختر» به معنی «ستاره، طالع، بخت» همان axtar پهلوی است و معنای «بخت» گسترشی احکام‌نجومی است که در ترکیبِ پهلویِ axtar-mār و در بیت فردوسی («نبینم همی اختر خویش بد») و در «اخترشناس» پیداست.\",\n\"3\": \"نام شهر و ساتراپی به‌راستی کهن است — پارسی باستان Bāxtriš (بیستون ۱٫۱۶)، اوستایی Bāxδī-، یونانی Βακτρία، فارسی میانه Baxl [bʾhl]، فارسی نو «بلخ» — اما هیچ پیوندی با «اپاختر» به معنی شمال ندارد. ریشه‌شناسیِ خودِ این نام روشن نیست و ساختی شفافِ ایرانی نیست؛ شباهت -xtr- در Bāxtriš با -xtar در abāxtar تصادفی است، چون abāxtar از *apa- به‌علاوهٔ پسوند تفضیلیِ -tara- ساخته شده و در Bāxtriš نه *apa- هست و نه -tara-. تحولِ *Bāxδī > Baxl (با بدل شدن δ/r به l) نیز یکسره از abāxtar > bāxtar جداست. افزون بر این «bâxr» صورتی گواهی‌شده نیست و به‌احتمال قریب‌به‌یقین لغزشی به جای Baxl است. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n\"4\": \"زنجیرهٔ «بلخ < Baxl < Bāxδī-/Bāxtriš» درست است، اما نیمهٔ دومِ معنایی که نورایی می‌دهد — و بار همهٔ نمودار بر آن است — نادرست است: لعلِ سرخِ گلگونِ تجارت جواهرِ سده‌های میانه سنگِ «بدخشان» است، ناحیه‌ای در کرانهٔ بالای جیحون در شمال شرقی افغانستان، نه سنگِ بلخ. نام گوهر «بلخش/بلخشان» گونه‌ای از «بدخشان» است، و خودِ معین در حاشیهٔ «بدخش» به نقل از بارتولد و مارکوارت (ایرانشهر ۲۷۹) همین را می‌گوید و می‌افزاید که balaxš نخست نام ناحیه بوده و سپس نام سنگی که از آنجا می‌آمده. شباهت «بلخ» و «بلخش» تصادفی است و همان است که خلطِ سده‌های میانه را دامن زده؛ پس پیکانِ «بلخ ← بلخشِ عربی» رد می‌شود.\",\n\"5\": \"عربی «بَلَخْش» به معنی لعلِ سرخِ گلگون واژه‌ای واقعی است و همان صورتی است که واژه‌های اروپایی از آن گرفته شده‌اند، پس جای این گره میان گرهٔ فارسی و گرهٔ فرانسوی کهن درست است. آنچه نادرست است پدرِ آن است: «بلخش» عربی وام‌واژه‌ای است از «بلخش» فارسی، گونهٔ کوتاه‌شده و ناهمگون‌شدهٔ «بدخشان»، نه از «بلخ». جغرافی‌نویسان عرب هر دو صورت «بلخشان» و «بدخشان» را برای یک جا به کار برده‌اند (اَدّی شیر به نقل از شفاء الغلیل: «والعجم يقولون له بدخشان»)، و نام‌گذاریِ سنگ به نام خاستگاهش الگوی معمول نام‌های گوهر در سده‌های میانه است. چون این واژه ساختی از ریشهٔ سامی نیست، برچسب «عربی» را باید «انتقالِ عربیِ یک نام‌جای فارسی» خواند؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"6\": \"فرانسوی کهن balais (و ترکیب rubis balais) در سدهٔ سیزدهم، همان «بلخش» عربی است که با آواشناسی فرانسوی سازگار شده: خوشهٔ -ḵš ساده شده و واژه با پسوند زایای صفتیِ -ais بازساخته شده است، چنان‌که در لاتینیِ سده‌های میانه balascius، ایتالیایی balascio، اسپانیایی balax و کاتالانی balaix نیز می‌بینیم. راه ورود، تجارت گوهرِ شام بوده است؛ مارکوپولو خود کشور را Balasian و سنگ‌ها را balasci می‌نامد. در فرانسه این واژه صفتی است برای rubis، درست مانند «balas ruby» انگلیسی. ادعای نورایی درست است.\",\n\"7\": \"انگلیسی میانه balais/bales وام‌واژه‌ای از فرانسوی کهن balais است (با پشتیبانیِ اسپانیاییِ کهن balax و لاتینیِ میانهٔ balascus) که به صورت امروزیِ balas رسیده و اکنون تقریباً همیشه در ترکیب وصفیِ «balas ruby» به کار می‌رود. مصداق آن اسپینلِ سرخِ گلگون تا نارنجی است که تنها پس از سدهٔ هجدهم از یاقوتِ راستین بازشناخته شد — و به همین سبب متون کهن‌تر انگلیسی آن را گونه‌ای یاقوت می‌شمرند، درست همان معنایی که نورایی می‌دهد. ادعای نورایی درست است.\",\n\"8\": \"سغدی ʾnγr /anɣar/ «ستاره» درست نقل شده است (قریب، شمارهٔ ۱۰۰۸، سغدی بودایی) و ترکیبات آن معنا را تأیید می‌کند: ʾnγrksʾy «اخترشناس» و ʾnγrwzn «منطقةالبروج» که خودِ قریب آن را با axtar-wazan پارتی برابر می‌نهد. همین برابری نکتهٔ اصلی است: anɣar سغدی متناظرِ axtar فارسی میانه و پارتی است، پس جای آن کنار «اختر» گرهٔ ۱ است نه یکراست زیر apāṅk- اوستایی — و خودِ یادداشت نورایی («شاید هم‌ریشه باشد نه مشتق») به همین اذعان دارد. قریب نیز تنها بازسازیِ مردّدِ *ana-har را با علامت پرسش پیشنهاد می‌کند؛ از *apāxtara- هرگز ʾnγr سغدی به دست نمی‌آید، چون نه اثری از *p هست و نه از پسوند -tar-. پس واژه و معنا درست است اما پیوندِ کشیده‌شده در بهترین حالت هم‌ریشگی است نه اشتقاق.\"\n}\n}\n}\nEOF\nfor p in 57 58; do python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py $p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p$p.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-$p.json >/dev/null && echo \"JSON_OK $p\"; done; git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-57.json data/verification/page-58.json",
 "description": "Apply Persian to pages 57 and 58"
}
```


### [2026-09-04T23:14:50.604Z] TOOL RESULT

```
ok 57
JSON_OK 57
ok 58
JSON_OK 58
 data/verification/page-57.json | 13 +++++++++++++
 data/verification/page-58.json | 19 ++++++++++++++++++-
 2 files changed, 31 insertions(+), 1 deletion(-)
```


## [2026-09-04T23:14:55.782Z] TOOL CALL #15: Bash

```json
{
 "command": "git -C /home/sfmqrb/git/rishe diff -- data/verification/page-58.json | grep -E '^[-+]' | grep -v '^[-+][-+]' | cut -c1-80",
 "description": "Inspect page 58 diff lines"
}
```


### [2026-09-04T23:14:57.661Z] TOOL RESULT

```
+      "note_fa": "ریشهٔ «Ap 2» نورایی همان *h₁ep- هندوا
+          "derivation_fa": "فعل اوستایی ap- «رسیدن، دست ی�
+          "derivation_fa": "پهلوی کتابی ʾpʾm /abām/ «وام، د�
+          "derivation_fa": "گذر از فارسی میانه به فارسی �
+          "derivation_fa": "پهلوی کتابی ʾyʾp-tn' /ayāftan/ با س
+          "derivation_fa": "«یافتن/یاب-» فارسی نو همان ay�
+          "derivation_fa": "لاتینی این ریشه را به دو صور�
+          "derivation_fa": "هر هشت واژه از مادهٔ لاتینیِ
+      "note_fa": "جعبهٔ ریشه اصیل است اما معنایی که 
+          "derivation_fa": "فارسی میانه ʾpʾhtl /abāxtar/ همان 
+          "derivation_fa": "«باختر» فارسی نو همان abāxtar ف
+          "derivation_fa": "نام شهر و ساتراپی به‌راستی �
+          "derivation_fa": "زنجیرهٔ «بلخ < Baxl < Bāxδī-/Bāxtri�
+          "derivation_fa": "عربی «بَلَخْش» به معنی لعلِ 
+          "derivation_fa": "فرانسوی کهن balais (و ترکیب rubis b
+          "derivation_fa": "انگلیسی میانه balais/bales وام‌و�
+          "derivation_fa": "سغدی ʾnγr /anɣar/ «ستاره» درست ن
-}
+}
```


## [2026-09-04T23:15:03.241Z] TOOL CALL #16: Bash

```json
{
 "command": "for p in 56 57 58 59 60 101 126 311 345; do n=$(git show HEAD:data/verification/page-$p.json 2>/dev/null | tail -c1 | xxd -p); echo \"$p last=$n\"; done",
 "description": "Check trailing newline in HEAD versions"
}
```


### [2026-09-04T23:15:05.278Z] TOOL RESULT

```
56 last=0a
57 last=0a
58 last=7d
59 last=0a
60 last=0a
101 last=0a
126 last=7d
311 last=7d
345 last=0a
```


## [2026-09-04T23:15:13.310Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/page-58.json'\ns=open(p).read()\nif s.endswith('\\n'): open(p,'w').write(s[:-1])\nEOF\npython3 - <<'EOF'\nimport re\nf='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py'\ns=open(f).read()\ns=s.replace(\"d=json.load(open(path),object_pairs_hook=collections.OrderedDict)\",\n \"raw=open(path).read()\\ntrail=raw.endswith('\\\\n')\\nd=json.loads(raw,object_pairs_hook=collections.OrderedDict)\")\ns=s.replace(\"json.dump(d,open(path,'w'),ensure_ascii=False,indent=2)\\nopen(path,'a').write('\\\\n')\",\n \"open(path,'w').write(json.dumps(d,ensure_ascii=False,indent=2)+('\\\\n' if trail else ''))\")\nopen(f,'w').write(s)\nEOF\ngit -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-58.json; tail -c1 /home/sfmqrb/git/rishe/data/verification/page-58.json | xxd -p",
 "description": "Fix trailing newline and update script"
}
```


### [2026-09-04T23:15:15.228Z] TOOL RESULT

```
 data/verification/page-58.json | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)
7d
```


## [2026-09-04T23:15:16.818Z] AGENT

Now pages 59 and 60.


## [2026-09-04T23:15:18.134Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 59 2>&1 | head -200",
 "description": "Dump page 59"
}
```


### [2026-09-04T23:15:20.146Z] TOOL RESULT

```
##########################################################################################
PAGE 59 book 29
================================================================================
ENTRY 0 | root: Apo, Apâ, Apu, Pu 3, Pô 1 | verdict: plausible | modern: PIE *apo / *h₂epo (also *ap-u, *pu, *po) 'off, away'
NOTE: Pokorny IEW p.53 heads the entry exactly 'apo (po, ap-u, pu) ‚ab, weg‘' and runs it to p.55, so four of Nourai's five variants (Apo, Apu, Pu 3, Pô 1), the language label and the gloss 'off' are literally Pokorny's; Walde-Pokorny I 47ff. and Watkins/AHD 'apo-. Also ap-. Off, away' agree. The one addition is 'Apâ' with long ā, which is not in Pokorny, WP, Watkins or Mann, and it is the peg on which Nourai hangs the whole ā- branch (nodes #6-#9). Old Iranian/Indo-Iranian ā 'to, toward' (Skt. ā́, Av./OP ā) is a separate particle (PIE *ē/*ō, Wiktionary *h₂ed), not an ablaut grade of *apo-; Horn (Grundriss no.1) and Cheung both handle it as an independent preverb. Hence the root box is right but over-extended, and everything under 'Apâ' has to be judged separately. A second cross-cutting problem: Nourai's BQT:1086 (cited on nodes #1, #6, #7) falls in the س- section of Borhān-e Qāţeʿ vol. 2 and has nothing to do with apa/ā, and KLN:168 on node #8 is Klein's 'behemoth–beige' page — almost certainly a slip for KNT:168, which does carry apadāna-.
ROOTREF: POK:53=supports
------------------------------------------------------------
# 1 Avestan | ap 2, apa; apama, apatama | verdict: confirmed | 
DER: Avestan apa is the inherited continuant of PIE *apo 'off, away' with regular Iranian retention of the medial -p- (unlike Indic, which also keeps it: Skt. ápa). Bartholomae AiW col. 71-72 lists 'apa 1) Adv. ‚weg, getrennt von—‘ (nur Komp.) 2) Praev. (mit karət-, gaud-, gam-, bar-, yam-, štar- usw.)', i.e. it survives mainly as a preverb, which is exactly the use Nourai's daughter nodes need. The superlative is formed with PIE *-m⌥o-: *apo-mo- > Av. apəma- 'the last (in time)', and with the double superlative *-t̥mo- (Skt. -tama-) *apa-tama- > MIr. abdom. Nourai's added gloss 'to' for apa is wrong (apa is ablatival, 'away from'), and 'apatama' is a reconstruction, not an attested Avestan form.
REF: POK:54=supports: POK_01.txt leaf 62 (= p.54): 'Ai. ápara- ‚hinterer; späterer, folgender; anderer‘ … av. ap… ; BQT:1086=not_found: BQT_v2_pages.txt leaf 543 (printed p. ≈1086, offset independently pinned on this repo's pa…
CON: BRT=supports: BRT.txt: 'apa 1) Adv. ‚weg, getrennt von—‘ … 2) Praev.'; and 'j., g. apama-, g. apəma- Adj… ; IEC=supports: IEC.txt: 'apo (apo, apo, po) ‚away; from, after‘, WP I, 47 … Av. apa … Lat. ab …' and 'apo… ; SNS=supports: SNS.txt line 3135: 'abdum/āfdum … (Bthl. 80-81) *apatəma, apama … awadum'. Nourai's pair '… ; WLD=supports: WLD_Bd1_pages.txt leaf 56 running head 'ap-, ap- — apo, po 47': the *apo entry that Pokorn…
------------------------------------------------------------
# 2 Pahlavi | apě, ape | verdict: confirmed | 
DER: Middle Persian abē- (Book Pahlavi ʾPʿ(y)-, Manichaean ʾby-) 'without, -less' goes back to an Old Iranian instrumental/locative *apa-i ‘away from’ built on the preposition apa; Hübschmann sets it up as OP *apaiy from apa + i (like naiy 'not' = na + i), and notes that the form arose in composition, because a free *apaiy would have given NP āb. It is productive only as first member of compounds (abē-bīm 'fearless', abē-gumān 'certain', abē-niyāz 'free from want'). This is the standard modern account and matches Nourai's arrow Av. apa → Phlv. apē exactly.
REF: AEF:309=not_checked: Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi is not online (refs_online: 'catalog' only). It is…
CON: PHD=supports: PHD_mackenzie.txt: 'abē- [ʾP(y)- | M ʾby-, N bē] without, -less. ~-bar [-bl] fruitless. ~-… ; NYB=supports: NYB_vol2_glossary.txt line 571: 'apē- [ʾpy-, ʾpyd] v.s.v. apa-', with apē-bīm 'fearless', … ; HRN=supports: HRN.txt: '247. bē, ebē ‚ohne‘. phlv. ape- (päz. awe-), z.B. ape-bīm, ape-gumān etc. … Wohl… ; HUB=supports: HUB.txt line 1096: 'Np. bē = pāz. awē, phl. apē setze ich = ap. *apaiy aus apa + id, wie n…
------------------------------------------------------------
# 3 Persian | bî «بی-»; bî-dastar «بیدستر» | verdict: disputed | 
DER: New Persian بی bī- 'without' is the regular continuation of MP abē-: the initial a- of the unstressed prefix was lost in NP (MP abē-bīm > NP bī-bīm), the older stage surviving as ابی abē/ebē in early NP verse, which Nourai correctly prints in the box (ابی-) and Moʿin glosses 'بی: [= ابی] (پش.) علامت نفی و سلب'. That half is confirmed and is the standard view (Horn 247, Hübschmann 247, MacKenzie s.v. abē-, Wiktionary بی < ابی < MP apē < PIE *h₂epo); the compounds in the extras (بی‌نیاز، بی‌بهره، بی‌شمار) are all straightforward bī- privatives. The second word is the problem. بیدستر bīdastar 'beaver' is analysed by Moʿin (and before him by Borhān-e Qāţeʿ) as بی 'without' + دستر glossed 'داس کوچک، اره' — 'without a sickle/saw', i.e. an animal that fells trees with no tool. That is a transparent folk etymology of the Borhān type: دستر 'small sickle' is not otherwise attested, and the word has the variants ویدستر vidastar and بادستر bādastar (the latter in Moʿin's own entry), whose v-/bā- cannot come from the privative bī-. Wiktionary (tentatively) takes the first element to be *widʰu- 'wood, tree', giving a 'wood-eater/wood-cutter' compound; Horn, Hübschmann and Bartholomae treat the I…
REF: AEF:309=not_checked: Not online; its original, Horn no.247, supports the bī < apē half (quoted at node #2). ; MON:131=supports: Moʿin does say what Nourai says, for both words. MON_part1.txt: 'بی: [= ابی] (پش.) علامت ن…
CON: PHD=supports: 'abē- [ʾP(y)- | M ʾby-, N bē] without, -less' — MacKenzie himself gives the New Persian ou… ; HRN=partial: Horn 247 gives bē/ebē 'ohne' < phlv. ape-, supporting bī; but Horn's beaver word is no.181… ; MON=supports: Also 'جند بیدستر [= جند بادستر] … خصیة الکلب البحر، خایهٔ سگ آبی' (castoreum), which shows… ; BQT=partial: BQT_v2_pages.txt: 'جند بیدستر باشد. گویند خایهٔ سگ آبی' — Borhān knows the word but here g…
------------------------------------------------------------
# 4 Pahlavi | afdom, awdum | verdict: confirmed | 
DER: Middle Persian abdom / afdom (Book Pahlavi ʾp̄dwm, Manichaean ʾbdwm, Pāzand awadum) 'last, finally' continues Old Iranian *apa-tama-, the *-tama- superlative of apa 'away, behind' — the same formation as Avestan apəma- but with the longer suffix. Intervocalic *-t- after the labial gave the Book Pahlavi spelling with p/f, and the word was borrowed into Biblical Aramaic as ʾappetōm (Ezra 4:13). Nourai's two spellings afdom and awdum are exactly the Book Pahlavi and Pāzand readings the handbooks print.
REF: SNS:26=supports: SNS_pages.txt leaf 29 (≈ printed p.26 — offset 3 for the front matter), headword 'abdum/āf…
CON: PHD=supports: PHD_mackenzie.txt: 'abdom [ʾp̄dwm | M ʾbdwm] last, final(ly). ~ih: finality, end.'; the En… ; NYB=supports: NYB_vol2_glossary.txt line 788: 'avdom [ʾpdwm] last … adv. in the end, finally, ultimately… ; HRN=supports: HRN.txt: '38. āfdum ‚letzter‘ … aw. *apətama ‚letzter‘; phlv. afdūm, päz. awdum ‚letzter‘.…
------------------------------------------------------------
# 5 Persian | âfdom «آفدُم» | verdict: confirmed | 
DER: NP آفدم āfdom 'last, at last' is MP abdom taken over into early New Persian; it is a rare, early word (Mojmal al-tawārīkh, Rūdakī, Abū Šukūr, Asadī), usually met in the frozen adverbial بافدم bāfdom = be + āfdom 'in the end', which is the form Nourai's extras and Rūdakī quotation give. Hübschmann's caveat is worth recording: phonologically one expects short a-, afdum, and Nöldeke suggested (ap. Hübschmann no.38) that the word was already obsolete in the earliest NP poets' day and was therefore mispronounced with ā-. The word died out and has no modern currency.
REF: MON:72,462=supports: Moʿin s.v. آفدم: MON_part1.txt line 3841 'آفدم: … (ص.) آخرین، پسین، نهائی'; vajehyab's Moʿ… ; FRS:184=supports: Asadī's Loghat-e Fors, FRS.txt line 13123ff.: 'عاقبت باشد [رودکی گوید:] مکن خویشتن از ره ر…
CON: HRN=supports: Horn cites for bāfdum exactly the same three verses (SF, FR/FJ Abū Šukūr and Asadī) and gl… ; HUB=partial: HUB.txt line 150: 'Man müsste lautgesetzlich afdum erwarten. „Vielleicht war das Wort scho… ; MON=supports: 'آفدم … (ص.) آخرین، پسین، نهائی' — same sense as the chart's 'last, at last'.
------------------------------------------------------------
# 6 Avestan | â 1; â-vare; â-gam; â-râd, â-râiti 1; apa-spar; â-kand | verdict: disputed | 
DER: The words themselves are real: Av./OP ā is a preverb/preposition 'to, toward, hither' that combines with bar- (ā-bar- 'bring'), gam- (ā-gam- 'come'), rād-/rāta- (ā-rā- 'set in order'), kan- (ā-kan- 'fill up'). But its ancestry is not *apo-. Skt. ā́, Av./OP ā and Gk. ὦ go back to an independent particle (PIE *ē/*ō; Wiktionary reconstructs *h₂ed), and every specialist treatment keeps the two apart: Horn's very first entry lists NP ā- under 'ap. aw. phlv. ā; ai. ā́' with no reference to apa, Cheung files āfrīnāmi under '*fraiH (+ *ā-)', and Pokorny's own apo- entry (pp.53-55) contains no ā-. Nourai's Avestan box therefore hangs a different preverb on the *apo- root by way of the invented root variant 'Apâ'. The one genuinely apa- item in the box, apa-spar 'walk away from, entrust', is also mis-prefixed: the ancestor of MP abespurdan / NP sepārdan is *upa-spar- (Cheung) or *abi-spar- (MacKenzie's Manichaean ʾbyspwrd), not *apa-spar-. Hence: right words, wrong parent.
REF: KNT:168=partial: KNT.txt leaf 190 (= printed p.168) is the apa- page: 'apa- prefix (§206b) ‚away‘: Av. Skt.… ; BQT:1086=not_found: As at node #1: BQT vol. 2 p.≈1086 (leaf 543) is the سبز- run of headwords; no آ-prefix or … ; FFD:24=partial: FFD_pages.txt pdf p.29 = printed p.24, s.v. آراستن: 'آراست < فارسی میانه ārāst < ایرانی با…
CON: BRT=partial: Bartholomae's apa- run (apa-gaēθa-, apa-gaya-, apa-ɣžāra-, apa-xšaθra-, apa-stūtay-, apəma… ; CHEUNG=contradicts: '*spar … (+ *upa-) BMP ʾpspʾl- /abespar-/ ‚to hand over, entrust‘ … NWIR: NP sipār-/sipurd… ; HRN=contradicts: '1. ā. 1) Praefix, z. B. in āmeden, ārāyiš. ap. aw. phlv. ā; ai. ā́. 2) Praeposition, z. B… ; PHD=contradicts: 'abespurdan, abespār- [ʾfspwltnʹ, ʾpspʾl- | M ʾbyspwrd, ʾbyspr-, N sipurdan, sipār-] commi…
------------------------------------------------------------
# 7 Persian | â-, a- «آ- ، ا-»; -â- «-ا-» | verdict: confirmed | 
DER: The edge itself is right: NP آ-/ا- is the direct continuation of the Old Iranian preverb ā, preserved fossilised in verbs whose Middle Persian ancestors already carried it — آوردن (< *ā-bar-), آمدن (< *ā-gam-), آراستن (< *ā-rād-ta-), آکندن (< *ā-kan-) — all four of which stand in Nourai's extras. The separate '-ā-' is the same particle in its adverbial/prepositional use, used to link a repeated noun: Horn's own examples her ā her and gird ā gird are precisely Nourai's برابر، دمادم، سراسر، گرداگرد type. The only defect is inherited from the parent box: the preverb goes back to PIE *ē/*ō (*h₂ed), not to *apo-; and اسپاردن in the extras belongs to *upa-spar-, not to ā-.
REF: BQT:1086=not_found: See node #1: BQT vol. 2 leaf 543 (≈ p.1086) is the سبز- section; nothing on the prefix آ-. ; HRN:1=supports: HRN.txt leaf 22 = printed p.1, entry no.1: 'ā. 1) Praefix, z. B. in āmeden, ārāyiš. ap. aw… ; FFD:24=supports: FFD printed p.24: 'ā پیشوند فعلی است', with آراستن < MP ārāst < OIr *ā-rād-ta and آرای < M…
CON: HUB=silent: Hübschmann adds no note to Horn no.1; the entry stands unchallenged. ; PHD=supports: MacKenzie's ā- compounds (āwar-, āmad-, ārāy-, āgand-) are the Middle Persian stage betwee… ; CHEUNG=supports: Cheung consistently marks these NP verbs as root + preverb *ā-, e.g. '(+ *ā-) ‚to bring ba…
------------------------------------------------------------
# 8 Avestan | apa-dâna; â-frî-nami; â-fritan; â-part | verdict: disputed | 
DER: Three separate problems. (a) apa-dāna- 'off place, secret room of a palace' is a genuine word with exactly Nourai's analysis — but it is Old Persian, not Avestan: Kent p.168 'apadāna- sb. ‚palace‘: from apa- + dāna- to root *dā-, cf. Skt. apadhā- ‚concealment‘, Gk. ἀποθήκη ‚storehouse‘', attested in Artaxerxes II's Susa and Hamadan inscriptions (D²Sa, A²Ha imam apadāna); Bartholomae's AiW apa- run has no such Avestan compound, and Nourai himself puts it (rightly) in the Old Persian box #12 as well. (b) ā-frīnāmi 'I praise/bless' is genuine Young Avestan (Y 11.15, Y 52.1, Yt 13.51 āfrīnənti) and ā-pərəta- 'battle' is a real ā + parət- 'to fight' formation — but both contain the preverb ā-, from PIE *ē/*ō, not *apo-. (c) 'ā-fritan to create' is not Avestan at all: it is the Middle Persian infinitive āfrītan (BMP ʾplyn-/ʾplyt-), as Horn's no.39 explicitly labels it ('phlv. āfrītan ‚schaffen‘'). So the box mixes an Old Persian noun, two Avestan ā- formations and one Middle Persian verb, and none of the ā- items descends from the root of the chart.
REF: KLN:168=not_found: Klein 1966 p.168 (KLN_1966.txt leaf 96) runs 'behemoth … behen … behest … behind … behold … ; POK:844=supports: POK_03.txt leaf 78 (= printed p.844): 'prāi-, prəi-, prī- (prī-) ‚gern haben, schonen, fri…
CON: KNT=partial: 'apadāna- sb. ‚palace‘: from apa- + dāna- (§147.I) to root *dā- … apadānam asm. D²Sa1; A²H… ; BRT=contradicts: Bartholomae's Avestan apa- compounds are apa-gaēθa-, apa-gaya-, apa-ɣžāra-, apa-kava-, apa… ; CHEUNG=supports: '*fraiH ‚to rejoice, ? to atone, [med.] please‘. AVESTAN: friī- ‚to rejoice, please‘ || (+… ; HRN=partial: '39. āfrīden ‚schaffen‘ … aw. āfrīnāmi ‚ich preise‘ etc., āfrīna- ‚Segen‘; phlv. āfrītan ‚…
------------------------------------------------------------
# 9 Persian | âpâdânâ «آپادانا»; âfarîn «آفرین»; âvard «آورد» | verdict: plausible | 
DER: آفرین and آورد are inherited and confirmed. āfarīn 'praise, bravo' is the present stem of آفریدن < MP āfrīn-/āfrītan 'to bless, create' < Av. ā-frīnāmi, PIE *preiH-; the antonym نفرین nifrīn < MP nifrīn 'curse' (*ni-frī-) and the agent آفریدگار in Nourai's extras belong to the same family. āvard 'combat' is the Shahnameh word (آوردگاه 'battlefield', آوردیدن), from ā- + parət- 'to fight', the exact counterpart of نبرد neberd < *ni-parət- (Horn no.1025); it must be kept apart from the homograph آورد 'he brought' (< ā-bar-). آپادانا is different in kind: it is not an inherited Persian word but a 20th-century learned re-borrowing of Old Persian apadāna from the Achaemenid inscriptions and archaeological literature (the Apadana of Persepolis/Susa); and its source is the Old Persian box #12, not an Avestan one. Hence 'plausible': two words confirmed, one with a mis-drawn parent and a learned rather than inherited transmission.
REF: KNT:168=partial: Kent p.168 (KNT.txt leaf 190) gives 'apadāna- sb. ‚palace‘: from apa- + dāna- … For develo…
CON: HRN=supports: 'āfrīden ‚schaffen‘, Praes. āfrīn-em, āfrīnegār; āfrīn 1) ‚schaffend‘ 2) ‚Lob‘, vergl. nef… ; CHEUNG=supports: '*NWIR: (+ *ā-) NP āfaridan/āfarīn- ‚to create‘ || (+ *ni-) NP nifrīn … ‚curse‘'. ; PHD=supports: MacKenzie's āfrīn 'blessing, praise' and āfrīdan 'to create, bless' are the Middle Persian… ; MON=supports: Moʿin gives آفرین 'ستایش، مدح؛ تحسین' with the Pahlavi tag, matching the chart's 'praise'.
------------------------------------------------------------
# 10 Arabic | ifrît | verdict: plausible | 
DER: Arabic عِفْريت ʿifrīt (vulgar ʿafrīt), a powerful demon; Qurʾanic (Q 27:39 ʿifrītun min al-jinn), whence English afreet. Asbaghi and Wiktionary both make it a Middle Iranian loan: from the past participle āfrīd 'created' (MP āfrītan/āfrīd-, the very verb of Nourai's parent box), originally elliptical for *dēw āfrīd 'a demon's creature' — which is exactly the chart's gloss 'demon creature'. The vocalisation ʿifrīt with initial ʿayn and the fiʿlīt shape are the usual Arabic adaptation of a foreign form to a native pattern. It is only 'plausible' because a purely internal Arabic derivation is also current: from the root ع-ف-ر 'dust, ashes' (cf. ʿafara 'to roll in the dust'), formed like عَكْرُوت ʿakrūt 'scoundrel'; Klein s.v. 'afreet' gives no Iranian source at all, and Jeffery's Foreign Vocabulary of the Qurʾān does not treat the word, i.e. he did not regard it as a loan.
REF: AHD:23=not_checked: Nourai's AHD page numbers below 1500 refer to the main body of the 1975/76 American Herita… ; PLA:203=supports: PLA_pages.txt leaf 218 = printed p.203 (leaf − 15), running head 'Saraba … 203': 'عفريت - …
CON: KLN=partial: 'afreet, n., an evil demon or jinni. — Transliteration of Arab. ʿifrīt (in vulgar pronunci… ; FVQ=silent: grep of FVQ.txt / FVQ_pages.txt for 'ifrit', 'ʿifrīt', 'عفريت' returns nothing: Jeffery ha… ; AFM=silent: grep of AFM.txt / AFM_pages.txt for عفريت returns nothing — Addi Shir does not list it amo… ; LKT=silent: grep of LKT.txt for 'ifrit' returns nothing; Lokotsch has no entry for the word.
------------------------------------------------------------
# 11 Persian | efrît «عفریت» | verdict: confirmed | 
DER: Modern Persian عفریت ʿefrīt 'demon, fiend' (with the feminine عفریته ʿefrīte in the extras) is a straightforward Arabic loan back into Persian, taken over with its Arabic عاین spelling and its Arabic feminine in -a; Moʿin tags it '[ع.]' (Arabic). If Asbaghi and Wiktionary are right about node #10, this is a round trip: MP āfrīd → Arabic ʿifrīt → NP ʿefrīt, and the modern Persian word is thus unrelated in form to its own ancestor آفریدن, which is presumably why Nourai draws it as a separate Arabic-mediated branch. The borrowing is medieval and spread through Qurʾanic and 1001-Nights usage.
REF: MON=supports: MON_part1.txt line 96994: 'عفریت: … [ع.] (ا.) دیو، اهریمن، غول' — Moʿin marks it explicitl…
CON: PLA=supports: Asbaghi's whole entry is about the Persian→Arabic direction, which presupposes the Arabic … ; KLN=supports: Klein confirms the Arabic form and its 'evil demon or jinni' sense, the sense in which Per… ; MON=supports: '[ع.]' origin tag = عربی, Arabic.
------------------------------------------------------------
# 12 Old Persian | ap 2, apa; apa-dâna; pa 2, pô | verdict: plausible | 
DER: OP apa- and apadāna- are exactly right. Kent p.168: 'apa- prefix ‚away‘: Av. Skt. apa, Gk. ἀπό, Lt. ab, Gt. af, Gm. ab, NEng. of, off, pIE *apo. Used with vb. gaud- and in sbb. apadāna-, apa-niyāka-; with suffix in apatara-, apara-'; and 'apadāna- ‚palace‘: from apa- + dāna- to root *dā-, cf. Skt. apadhā- ‚concealment‘, Gk. ἀποθήκη ‚storehouse‘' — which is precisely Nourai's gloss 'off (secret) place' and his cross-reference to root Dhē 2 (*dheh₁-). Attested in A²Sa/A²Ha/D²Sa (imam apadāna(m)). The third item is the weak one: there is no Old Persian preposition pa or pō. Pokorny's 'po:' section (p.54) illustrates it from Avestan pa-zdayeiti, Latin pō-situs/pōnō, Albanian pa, Old High German fona and Slavic/Baltic po — not from Old Persian, and Kent's lexicon has no such entry.
REF: POK:53-55=partial: POK_01.txt leaves 61-63 = pp.53-55 cover apo / po / ap-u / pu, including 'av. ap. apa ‚von… ; KNT:168=supports: KNT.txt leaf 190 (printed p.168) carries 'apa- prefix (§206b) ‚away‘ … pIE *apo' and 'apad…
CON: BRT=supports: Bartholomae marks the Old Persian forms with 'p.' in the same apa- article, e.g. 'p. apata… ; IEC=supports: 'apo (apo, apo, po) ‚away; from, after‘ … OCS po … Li. po' — Mann too attaches po to Slavi… ; AHD=partial: '7. Possible root *po(s), on, in: a. Russian po … b. Latin post … c. Latin pōnere' — Watki…
------------------------------------------------------------
# 13 Old Persian | apa-had; apa-ra; apa-taram; pan-s-dau; apa-nyâka | verdict: disputed | 
DER: Three of the five are solid Old Persian: apara- 'later, after' (Kent p.168, apa- + comparative -ra-, asn. adverb aparam DB 4.37 etc.), apataram 'farther off, elsewhere' (nsn. of apatara- = apa- + -tara-, DNa 18, DSe 16f, XPb 25, XPh 16, cf. Gk. ἀπωτέρω), and apaniyāka- 'great-great-grandfather' (apa- + niyāka- 'grandfather', cf. Lat. abavus; A²Sa 3), where Nourai's gloss 'ancestors' is loose but the formation is Kent's. The other two fail. 'apa-had ‚put away‘' is unattested: Old Persian uses apa- with gaud- (apagaudaya- 'conceal', DB 4.54-57), and the root *had- 'sit' appears only in ni-šad-/niyašādayam (Kent, Cheung s.v. *had) — neither Kent nor Bartholomae nor Cheung has an *apa-had-. 'pan-s-dau ‚after that‘' is not Old Persian at all but OLD PRUSSIAN: it comes straight out of the page Nourai cites, Pokorny p.54, 'Eine ähnliche Form sucht Trautmann Apr. 389 in apr. pan-s-dau ‚danach‘' — where apr. = altpreußisch. Nourai evidently read the abbreviation as 'Old Persian'. The book page (pdf 59) does print it inside the Old Persian box, so this is the author's error, not a scan artefact.
REF: POK:53,55=contradicts: POK_01.txt leaf 62 (= p.54, within the cited range): 'Eine ähnliche Form sucht Trautmann A… ; KNT:168=partial: Kent p.168 (leaf 190) has 'apataram adv. ‚farther off, far off‘ … DNa 18; DSe 16f; XPb 25;…
CON: KNT=partial: For the apa- verb Kent gives only apa-gaud-: 'inj. 2sg. … apa-gaudaya (DB 4.54)', 'mā … ap… ; CHEUNG=contradicts: Cheung lists the preverbs attested with *had as *abi- and *ni- only ('OLD PERSIAN: (+ *ni-… ; IEC=supports: 'apo-teros ‚further, following‘. WP I, 47 … Skt. OPer. apataram; Gk. apóteros; Go. aftaro'… ; BRT=supports: 'p. apataram Adv. 1) ‚abseits, anderswo‘: tyāmaiy apataram kartam H 2.3; 2) mit hacā ‚auss…
------------------------------------------------------------
# 14 Old Persian | apa-ardha | verdict: plausible | 
DER: The compound is real but is a reconstruction, and 'Old Iranian' rather than specifically Old Persian is the right label: Nyberg sets up MP apārōn < OIr *apārda-van-, formed with the suffix -van- from *apārda- < *apa-arda- 'whose side is turned away' (apa- 'away' + arda- 'side, half', the same *ardha- as in Skt. árdha- 'half, side'). The mirror-image compound *frārda-van- > MP frārōn 'righteous, upright' (< *fra-arda- 'whose side is turned forward') guarantees the analysis. No such word is attested in the Achaemenid inscriptions, so Kent has nothing; Kent's OP arda- is a different word, 'light' (ardata- 'silver', ardastāna-).
REF: POK:53-55=partial: Pokorny pp.53-55 give the apo- root and its derivatives apo-tero-, ap-ero-, ap-io-, ap-ōko…
CON: NYB=supports: '< OIr apārda-van-, derived, by means of the suff. -van-, from *apārda- < *apa-arda- ‚whos… ; KNT=silent: 'ardastāna- sb. ‚window-frame‘: arda- ‚light‘ as in OP ardata- ‚silver‘' — Kent's OP arda-… ; BRT=silent: No Avestan apa-arəδa- among Bartholomae's apa- compounds; the form is a Middle-Iranian-bas…
------------------------------------------------------------
# 15 Pahlavi | apârôn | verdict: confirmed | 
DER: Middle Persian abārōn (Book Pahlavi ʾpʾlʹlwnʹ/ʾpʾlwnʹ) 'contrary, wrong, perverse, sinful', adverbially 'backward' (= abāz), Pāzand āwārūn, is the regular outcome of *apārda-van-: the cluster *-rd- gives Middle Persian -r-/-l- in the Book Pahlavi orthography, and the suffix *-āna-/-ōn is the same as in its antonym frārōn 'righteous'. The word is a technical term of Zoroastrian moral vocabulary, abārōnīh meaning 'sin' and being the standing opposite of frārōnīh.
REF: NYB:23=supports: NYB_vol2_glossary.txt line 521, form-feed leaf 32 ≈ printed p.24 (Part II offset leaf = pr…
CON: PHD=supports: PHD_mackenzie.txt: 'abaron [ʾpʾlwnʹ | N warun] contrary, wrong, sinful. ~ih: sin.' MacKenz… ; NYB=supports: 'frārōn [plʾlwnʹ] righteous, upright, honest … OIr *frārda-van- < *fra-arda-, cf apārōn' —…
------------------------------------------------------------
# 16 Persian | vârŭn «وارون» | verdict: confirmed | 
DER: NP وارون vārūn 'upside down, inverted, perverse' (with the extended وارونه vārūne of the extras) is inherited directly from MP abārōn: initial ab-/aw- regularly yields NP wā-/vā- (cf. MP abāz > NP باز/واز), so *abārōn > wārūn. Classical Persian keeps the moral sense of the Pahlavi word ('wicked, ill-omened, بخت وارون ‚ill fortune‘'), while modern Persian has generalised the physical sense 'inverted'. The word was borrowed onward into Ottoman Turkish as varun.
REF: MON:4941=supports: Moʿin s.v. وارون, MON_part2.txt line 83342: 'وارون: [= وارونه] (ص.) باژگونه، واژگون، سرنگو…
CON: PHD=supports: 'abaron [ʾpʾlwnʹ | N warun] contrary, wrong, sinful' — MacKenzie's own bracket gives NP wa… ; NYB=supports: '… NP vārūn ‚inverted, turned upside down‘' in the apārōn entry; also the index entry 'vār… ; MON=supports: Moʿin also has the doublet 'وارون … [= وارون] (ص.) بازگونه، واژگون، سرنگون'.
------------------------------------------------------------
# 17 Latin | ab | verdict: confirmed | 
DER: Latin ab 'from, away from' (governing the ablative) is the direct Italic reflex of PIE *apo: intervocalic/pre-voiced *-p- was voiced to -b-, the older *ap surviving in aperiō < *ap-weriō and in the by-forms abs (before c, t: abstineō, abscondō), as- (before p: asportō), and ā- (before m, u, b: āmoveō, āvellō, ābitō). Cognate with Gk. ἀπό, Skt. ápa, Goth. af, OE of/off. Nourai's gloss 'away' and the language label are correct.
REF: AHD=supports: AHD_watkins1985.txt s.v. apo-: 'apo-. Also ap-. Off, away. 1. Germanic *af … 2. Latin ab, …
CON: POK=supports: 'lat. ab m. Abl. ‚von‘ (vor tönenden Kons. aus ap, das noch in aperiō aus *ap-weriō …); ab… ; LAT=supports: 'ab, abs, a: preverbe et preposition … Ab signifie „en s’éloignant, en partant de, depuis,… ; IEC=supports: 'apo … Lat. ab (perhaps also as a fused px. in Lat. p-arco, p-aveo, paro, pudeo, pando, et…
------------------------------------------------------------
# 18 English | abnormal | verdict: confirmed | 
DER: English abnormal (17th c.) is a Latinate formation whose first element is the Latin preposition/prefix ab- of node #17: Klein describes it as a blend of Latin abnormis 'deviating from a rule' (ab + norma 'carpenter's square, rule') with Medieval Latin anormalis, itself a blend of Latin anomalus (< Gk. ἀνώμαλος) and normalis — which is why the earlier English form was anormal and why the -b- was restored on the model of Latin ab-. Only the prefix comes from *apo-; the stem is from PIE *ǵneh₃- 'to know' via Latin norma (Watkins indexes ABNORMAL under gnō-, and ABLAUT, AFTER, EBB, OF, OFF, AWKWARD under apo-). The empty ref field is correct — Nourai cites nothing for this box.
REF: None=not_checked: The chart gives no reference for this box; nothing to check.
CON: KLN=supports: KLN_1971.txt: 'abnormal, adj. — A blend of L. abnormis and ML. anormalis, this latter itse… ; AHD=partial: The index has 'AB-¹ apo-' and 'ABNORMAL gnē-': the prefix is from apo-, the stem from the … ; SKT=silent: Skeat has no abnormal entry; his relevant material is s.v. OF, where English of/off is put…
```


## [2026-09-04T23:18:15.408Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p59.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"پوکورنی مدخل صفحهٔ ۵۳ را دقیقاً با عنوان «apo (po, ap-u, pu) ‚ab, weg‘» می‌آغازد و تا صفحهٔ ۵۵ می‌کشد، پس چهار صورت از پنج صورتی که نورایی آورده (Apo, Apu, Pu 3, Pô 1)، همچنین برچسب زبانی و معنای «دور، از» عیناً از پوکورنی است و والده-پوکورنی و واتکینز نیز همین را می‌گویند. تنها افزودهٔ نورایی «Apâ» با الفِ کشیده است که نه در پوکورنی هست، نه در والده-پوکورنی، نه در واتکینز و نه در مان — و همین صورتِ ساختگی است که تمام شاخهٔ آ- (گره‌های ۶ تا ۹) بر آن آویخته شده. حال آنکه ā «به، به سوی» در ایرانی باستان و سنسکریت حرف اضافه/پیشوندی مستقل است (از *ē/*ō هندواروپایی) نه گونهٔ ابلاوتیِ *apo-؛ هرن در نخستین مدخل گرندریس و چونگ هر دو آن را پیشوندی جداگانه می‌شمارند. پس جعبهٔ ریشه درست اما بیش از اندازه گسترده است و هرچه زیر «Apâ» آمده باید جداگانه سنجیده شود. اشکال سراسری دیگر در ارجاعات است: BQT:1086 که در گره‌های ۱ و ۶ و ۷ آمده به بخش «س» جلد دوم برهان قاطع می‌افتد و ربطی به apa/ā ندارد، و KLN:168 در گرهٔ ۸ صفحهٔ «behemoth–beige» کلاین است و تقریباً به یقین لغزشی به جای KNT:168 است که apadāna- در آن آمده.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"اوستایی apa دنبالهٔ موروثیِ *apo هندواروپایی «دور، از» است و -p- میانی در ایرانی (مانند هندی: سنسکریت ápa) برجای مانده است. بارتولومه (ستون ۷۱–۷۲) آن را هم قید «دور، جدا از» و هم پیشوند فعلی می‌شمارد و در عمل بیشتر به عنوان پیشوند به کار می‌رود — همان کاربردی که گره‌های فرزندِ این نمودار بدان نیاز دارند. صفت عالیِ آن با پسوند *-mo- ساخته می‌شود: *apo-mo- > apəma- «واپسین»، و با پسوند عالیِ مضاعفِ *-tama- صورتِ *apa-tama- که در ایرانی میانه abdom را می‌دهد. دو تصحیح: معنای «به» که نورایی برای apa افزوده نادرست است (apa معنای ازی/جدایی دارد)، و «apatama» صورتی بازسازی‌شده است نه گواهی‌شده در اوستا.\",\n\"2\": \"فارسی میانه abē- «بی، بدون» (پهلوی کتابی ʾPʿ(y)-، مانوی ʾby-) به صورت ابزاری/دریِ ایرانی باستان *apa-i از همان حرف اضافهٔ apa بازمی‌گردد؛ هوبشمان آن را *apaiy می‌داند، ساخته از apa + i، درست مانند naiy «نه» از na + i، و یادآور می‌شود که این صورت در ترکیب پدید آمده است، زیرا *apaiyِ آزاد در فارسی نو می‌بایست «آب» می‌شد. این واژه تنها به عنوان جزء نخستِ ترکیب زایاست: ابی‌بیم، ابی‌گمان، ابی‌نیاز. همین تحلیل، رأی معیار امروزی است و با پیکانِ «اوستایی apa ← پهلوی apē»ی نورایی کاملاً می‌خواند.\",\n\"3\": \"نیمهٔ نخستِ این گره درست است: «بی-» فارسی نو دنبالهٔ قاعده‌مندِ abē- فارسی میانه است که در آن الفِ آغازینِ پیشوندِ بی‌تکیه افتاده (ابی‌بیم > بی‌بیم)، و صورت کهن‌تر «ابی» در شعر فارسی متقدم بازمانده است — چنان‌که خودِ نورایی در جعبه آورده و معین نیز «بی: [= ابی] (پش.) علامت نفی و سلب» می‌نویسد؛ هرن، هوبشمان و مکنزی همه همین را می‌گویند. اما واژهٔ دوم مشکل‌ساز است: «بیدستر» را معین به پیروی از برهان قاطع «بی» + «دستر» (که آن را «داس کوچک، اره» معنی کرده‌اند) تحلیل کرده، یعنی جانوری که بی‌ابزار درخت می‌اندازد — و این نمونهٔ آشکارِ ریشه‌شناسی عامیانه از گونهٔ برهان است، چون «دستر» به معنی داسِ کوچک جای دیگری گواه ندارد و گونه‌های «ویدستر» و «بادستر» را نمی‌توان از پیشوند سلبیِ «بی» بیرون آورد. ویکی‌واژه با احتیاط جزء نخست را *widʰu- «چوب، درخت» می‌داند؛ از این رو این نیمهٔ گره را پژوهش امروزی رد می‌کند.\",\n\"4\": \"فارسی میانه abdom/afdom (پهلوی کتابی ʾp̄dwm، مانوی ʾbdwm، پازند awadum) «واپسین، سرانجام» دنبالهٔ ایرانی باستان *apa-tama- است، یعنی صفت عالیِ apa «دور، پس» با پسوند *-tama- — همان ساختی که در apəma- اوستایی با پسوند کوتاه‌تر دیده می‌شود. *t- پس از لبی، املای پهلویِ p/f را پدید آورده و همین واژه در آرامیِ کتاب مقدس به صورت ʾappetōm (عزرا ۴:۱۳) وام گرفته شده است. دو ضبطی که نورایی می‌آورد دقیقاً همان خوانش پهلوی کتابی و پازند است که در دستنامه‌ها آمده؛ ادعای او درست است.\",\n\"5\": \"«آفدم» فارسی نو همان abdom فارسی میانه است که به فارسی دریِ متقدم راه یافته؛ واژه‌ای کمیاب و کهن است (مجمل‌التواریخ، رودکی، ابوشکور، اسدی) و بیشتر در ترکیب متحجرِ قیدیِ «بافدم» یعنی «سرانجام» دیده می‌شود، همان که نورایی در شاهدها آورده است. تذکر هوبشمان درخور ثبت است: از نظر آوایی انتظار «افدم» با الفِ کوتاه می‌رفت، و نولدکه حدس زده که واژه در روزگار نخستین شاعران فارسی از رواج افتاده بوده و از این رو با الفِ کشیده تلفظ شده است. واژه بعدها یکسره متروک شد. ادعای نورایی درست است.\",\n\"6\": \"خود واژه‌ها اصیل‌اند: ā در اوستایی و پارسی باستان پیشوند و حرف اضافه‌ای است به معنی «به، به سوی، این‌سو» که با bar- (آوردن)، gam- (آمدن)، rād- (آراستن) و kan- (آکندن) ترکیب می‌شود. اما تبار آن *apo- نیست: سنسکریت ā́، اوستایی و پارسی باستان ā و یونانی ὦ به ادات مستقلی بازمی‌گردند (*ē/*ō؛ ویکی‌واژه *h₂ed) و همهٔ پژوهش‌های تخصصی این دو را از هم جدا نگاه می‌دارند — هرن در نخستین مدخلِ گرندریس، چونگ زیر *fraiH (+ *ā-)، و خودِ پوکورنی که در مدخل apo- هیچ ā- ندارد. پس نورایی با ساختنِ گونهٔ «Apâ» پیشوندی دیگر را به این ریشه بسته است. تنها عضوِ راستینِ apa- در این جعبه، یعنی apa-spar، نیز پیشوندش نادرست است: نیای «سپردن» فارسی *upa-spar- (چونگ) یا *abi-spar- (مکنزی) است نه *apa-spar-. خلاصه: واژه‌ها درست، پدرِ آنها نادرست.\",\n\"7\": \"خودِ این پیوند درست است: «آ-/ا-» فارسی نو دنبالهٔ مستقیمِ پیشوندِ ایرانی باستانِ ā است که در فعل‌هایی متحجر مانده که نیای فارسی‌میانه‌شان نیز آن را داشته‌اند — آوردن (< *ā-bar-)، آمدن (< *ā-gam-)، آراستن (< *ā-rād-ta-) و آکندن (< *ā-kan-) که هر چهار در شاهدهای نورایی آمده‌اند. «-ا-»ی جداگانه نیز همان ادات است در کاربرد قیدی/اضافی که دو اسمِ تکراری را به هم می‌پیوندد؛ نمونه‌های خودِ هرن (her ā her، gird ā gird) همان گونهٔ برابر، دمادم، سراسر و گرداگرد است. تنها عیب، ارثی است از جعبهٔ مادر: این پیشوند به *ē/*ō بازمی‌گردد نه به *apo-؛ و «اسپاردن» که در شاهدها آمده به *upa-spar- تعلق دارد نه به ā-.\",\n\"8\": \"این جعبه سه اشکال جداگانه دارد. نخست apa-dāna- «جای دور، تالار نهانِ کاخ» واژه‌ای اصیل با همان تحلیلی است که نورایی می‌دهد، اما پارسی باستان است نه اوستایی: کنت (ص ۱۶۸) آن را apa- + dāna- از ریشهٔ *dā- می‌داند و در کتیبه‌های اردشیر دوم در شوش و همدان گواه دارد، حال آنکه در فهرست ترکیب‌های apa-ی بارتولومه چنین واژه‌ای نیست. دوم، ā-frīnāmi «می‌ستایم» اوستایی متأخرِ راستین است و ā-pərəta- «نبرد» نیز ساختی حقیقی از ā + parət- است، اما هر دو پیشوند ā- دارند که از *ē/*ō است نه از *apo-. سوم، «ā-fritan» اصلاً اوستایی نیست بلکه مصدر فارسی میانهٔ āfrītan است، چنان‌که هرن در شمارهٔ ۳۹ صریحاً برچسب «phlv.» می‌زند. پس این جعبه یک اسم پارسی باستان، دو ساخت اوستایی با پیشوند ā- و یک فعل فارسی میانه را درهم آمیخته و هیچ‌یک از اعضای ā-دار از ریشهٔ این نمودار نمی‌آید.\",\n\"9\": \"«آفرین» و «آورد» موروثی و بی‌اشکال‌اند: آفرین ستاک حالِ آفریدن است، از فارسی میانه āfrīn-/āfrītan «ستودن، آفریدن»، از اوستایی ā-frīnāmi و ریشهٔ *preiH-، و «نفرین» (< *ni-frī-) و «آفریدگار» به همین خانواده تعلق دارند. «آورد» به معنی نبرد واژهٔ شاهنامه است (آوردگاه، آوردیدن) از ā- + parət-، درست قرینهٔ «نبرد» < *ni-parət- (هرن، شمارهٔ ۱۰۲۵)، و باید از هم‌نگاشتِ «آورد» (سوم‌شخصِ آوردن) جدا شود. اما «آپادانا» از گونهٔ دیگری است: واژه‌ای موروثی نیست، بلکه وام‌گیریِ کتابیِ سدهٔ بیستم از پارسی باستانِ apadāna از راه کتیبه‌ها و ادبیات باستان‌شناسی است (آپادانای تخت‌جمشید و شوش) و پدرش جعبهٔ پارسی باستانِ شمارهٔ ۱۲ است نه جعبه‌ای اوستایی. از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"10\": \"عربی «عِفریت» (در عامیانه عَفریت) دیوی نیرومند است و قرآنی است (نمل ۳۹: «قال عِفریتٌ من الجنّ»)، و افریتِ انگلیسی از همین آمده است. اصباغی و ویکی‌واژه آن را وام‌واژه‌ای ایرانی میانه می‌دانند: از اسم مفعولِ āfrīd «آفریده» (همان فعلی که در جعبهٔ مادر است)، در اصل به‌اختصار از *dēw āfrīd «آفریدهٔ دیو» — دقیقاً همان معنایی که نورایی می‌دهد. آوایش عِفریت با عینِ آغازین و بر وزن فِعلیت، همان سازگارسازیِ معمولِ صورت بیگانه با قالب‌های عربی است. حکم «با احتیاط پذیرفتنی» است، زیرا اشتقاقی یکسره درون‌عربی نیز رواج دارد: از ریشهٔ ع-ف-ر «خاک و خاکستر»، بر قیاس عَکروت؛ کلاین هیچ خاستگاه ایرانی نمی‌آورد و جفری نیز در «واژگان دخیل در قرآن» آن را وام نشمرده و اصلاً نیاورده است.\",\n\"11\": \"«عفریت» فارسی امروز وام‌واژه‌ای است سرراست از عربی، با همان املای عین‌دار و همان مؤنثِ عربیِ «عفریته» که در شاهدها آمده؛ معین نیز آن را با نشانِ «[ع.]» عربی می‌داند. اگر تحلیل اصباغی و ویکی‌واژه در گرهٔ ۱۰ درست باشد، این یک رفت‌وبرگشت است: āfrīd فارسی میانه ← عفریتِ عربی ← عفریتِ فارسی، و واژهٔ فارسیِ امروز از نظر صورت هیچ شباهتی به نیای خود «آفریدن» ندارد — و ظاهراً به همین سبب است که نورایی آن را شاخه‌ای جداگانه با میانجیِ عربی کشیده است. وام‌گیری از سده‌های میانه است و از راه کاربرد قرآنی و هزارویک‌شب گسترش یافته است.\",\n\"12\": \"apa- و apadāna- پارسی باستان دقیقاً درست‌اند: کنت (ص ۱۶۸) apa- را پیشوندِ «دور» با برابرهای اوستایی، سنسکریت ápa، یونانی ἀπό، لاتینی ab و گوتی af می‌آورد و apadāna- را «کاخ» از apa- + dāna- از ریشهٔ *dā- می‌داند و با سنسکریت apadhā- «نهان‌گاه» و یونانی ἀποθήκη می‌سنجد — یعنی همان «جای دور/نهان»ی که نورایی می‌گوید و همان ارجاعی که به ریشهٔ Dhē 2 می‌دهد. اما جزء سوم سست است: حرف اضافه‌ای به صورت pa یا pō در پارسی باستان وجود ندارد. بندِ «po» در پوکورنی (ص ۵۴) با شاهدهای اوستایی pa-zdayeiti، لاتینی pōnō، آلبانیایی pa، آلمانی علیای باستان fona و صورت‌های اسلاوی و بالتی روشن شده است، نه با پارسی باستان، و واژه‌نامهٔ کنت چنین مدخلی ندارد؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"13\": \"سه واژه از پنج واژهٔ این جعبه پارسی باستانِ استوارند: apara- «پسین، بعد»، apataram «دورتر، جای دیگر» (برابر یونانی ἀπωτέρω) و apaniyāka- «جد اعلی» از apa- + niyāka- «نیا» که با لاتینی abavus سنجیدنی است. اما دو تای دیگر نادرست‌اند. «apa-had» گواه ندارد: پارسی باستان apa- را با gaud- به کار می‌برد (apagaudaya- «پنهان کرد») و ریشهٔ *had- «نشستن» تنها با ni- می‌آید؛ نه کنت، نه بارتولومه و نه چونگ چنین ترکیبی ندارند. و «pan-s-dau» اصلاً پارسی باستان نیست بلکه پروسیِ کهن است: عیناً از همان صفحه‌ای که نورایی ارجاع می‌دهد (پوکورنی ص ۵۴) برداشته شده، آنجا که می‌نویسد تراوتمان صورتی مشابه در «apr. pan-s-dau ‚danach‘» می‌جوید — و apr. یعنی altpreußisch (پروسی کهن)؛ نورایی این اختصار را «پارسی باستان» خوانده است. تصویر صفحه نشان می‌دهد که این خطا در خودِ کتاب چاپ شده است، پس لغزش مؤلف است نه خطای اسکن.\",\n\"14\": \"این ترکیب واقعی است اما بازسازی‌شده، و برچسب درستِ آن «ایرانی باستان» است نه به‌خصوص «پارسی باستان»: نیبرگ apārōn فارسی میانه را از *apārda-van- می‌گیرد که با پسوند -van- از *apārda- < *apa-arda- «آنکه سویش برگردانده است» ساخته شده (apa- «دور» + arda- «سو، نیمه»، همان *ardha- که در سنسکریت árdha- است). ترکیبِ آینه‌وارِ *frārda-van- > frārōn «راست‌کردار» درستیِ این تحلیل را تضمین می‌کند. در کتیبه‌های هخامنشی چنین واژه‌ای گواه ندارد و کنت آن را نیاورده است؛ arda-ی پارسی باستانِ کنت واژهٔ دیگری است به معنی «روشنی» (ardata- «سیم»). از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"15\": \"فارسی میانه abārōn (پهلوی کتابی ʾpʾlwnʹ) «وارونه، نادرست، گناه‌آلود» و در کاربرد قیدی «واپس»، پازند āwārūn، برون‌دادِ قاعده‌مندِ *apārda-van- است: خوشهٔ *-rd- در فارسی میانه به -r-/-l- بدل می‌شود و پسوند -ōn همان است که در متضادِ آن frārōn «راست‌کردار» دیده می‌شود. این واژه اصطلاحی است در واژگان اخلاقی زردشتی و abārōnīh «گناه» همواره در برابر frārōnīh می‌ایستد. ادعای نورایی درست است.\",\n\"16\": \"«وارون» فارسی نو یکراست از abārōn فارسی میانه به ارث رسیده است: اب-/او- آغازین در فارسی نو قاعده‌مندانه به وا-/vā- بدل می‌شود (مانند abāz > باز/واز)، پس *abārōn > wārūn. فارسی کلاسیک معنای اخلاقیِ واژهٔ پهلوی را نگاه داشته است («بخت وارون»)، حال آنکه فارسی امروز معنای فیزیکیِ «واژگونه» را تعمیم داده است؛ گونهٔ گسترده‌ترِ «وارونه» نیز در شاهدها آمده. واژه به ترکی عثمانی نیز وام داده شده است. ادعای نورایی درست است.\",\n\"17\": \"لاتینی ab «از، دور از» (با حالت ازی) بازتاب مستقیمِ ایتالیکِ *apo است: *-p- پیش از واکِ واک‌دار به -b- واک‌دار شده و صورت کهن‌ترِ *ap در aperiō < *ap-weriō و در گونه‌های abs (پیش از c و t)، as- (پیش از p) و ā- (پیش از m، u، b) بازمانده است. هم‌ریشهٔ آن یونانی ἀπό، سنسکریت ápa، گوتی af و انگلیسی باستان of/off است. معنایی که نورایی می‌دهد و برچسب زبانی هر دو درست است.\",\n\"18\": \"abnormal انگلیسی (سدهٔ هفدهم) ساختی لاتینی‌تبار است که تنها جزء نخستش، یعنی پیشوندِ ab-، به گرهٔ ۱۷ تعلق دارد: کلاین آن را آمیزه‌ای از لاتینی abnormis «منحرف از قاعده» (ab + norma) با لاتینیِ سده‌های میانه anormalis می‌داند، و anormalis خود آمیزهٔ anomalus (< یونانی ἀνώμαλος) و normalis است — و همین توضیح می‌دهد که چرا صورت کهن‌ترِ انگلیسی anormal بوده و چرا -b- بعدها به قیاسِ ab- لاتینی بازگردانده شده است. ستاک واژه از ریشهٔ *ǵneh₃- «دانستن» از راه norma می‌آید، چنان‌که واتکینز ABNORMAL را ذیل gnō- فهرست می‌کند. خالی بودن خانهٔ ارجاع نیز درست است، چون نورایی برای این جعبه منبعی نیاورده است.\"\n}\n}\n}\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py 59 p59.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-59.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-59.json",
 "description": "Apply Persian to page 59"
}
```


### [2026-09-04T23:18:19.009Z] TOOL RESULT

```
ok 59
JSON_OK
 data/verification/page-59.json | 19 +++++++++++++++++++
 1 file changed, 19 insertions(+)
```


## [2026-09-04T23:18:21.893Z] TOOL CALL #20: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 60 2>&1 | head -220",
 "description": "Dump page 60"
}
```


### [2026-09-04T23:18:23.835Z] TOOL RESULT

```
##########################################################################################
PAGE 60 book 30
================================================================================
ENTRY 0 | root: Apo, Apâ, Apu, Pu 3, Pô 1 | verdict: confirmed | modern: PIE *h₂epo (*apo, with ablaut/enclitic variants *apā, *ap-u, *pu, *po) 'off, away, from'
NOTE: Pokorny IEW 53-55 heads the entry 'apo- (pō̆, ap-u, pu) "ab, weg"', i.e. exactly the five shapes Nourai lists (his 'Apâ' = the long-vowel variant apā, 'Pô 1' = Pokorny's po, 'Pu 3' = Pokorny's pu). Language label (Indo-European) and gloss ('off') are right; the current reconstruction writes it *h₂epó, though Hittite āppa is used to argue for laryngeal-less *apo. The whole Latin/Greek/Iranian half of the chart hangs on Pokorny's own remark under *pos that it is 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.', so the root→#3 arrow is Pokorny's, not Nourai's invention. The single weak link on this chart is the item 'eben : later time, evening' in node #1 (and 'evening' in node #2): neither Pokorny nor Watkins/AHD puts the Germanic word for 'evening' under *apo, and Klein assigns it to *epi/*opi.
ROOTREF: POK:53=supports
------------------------------------------------------------
# 1 Germanic | af; apo-tero; eben; afug | verdict: disputed | 
DER: Three of the four items are straight reflexes of *apo. (a) 'af' = Proto-Germanic *ab/*af, unstressed preposition/prefix from PIE *h₂epo with regular loss of the final vowel: Gothic af, Old Norse af, Old English of/æf, Old Saxon af, OHG aba/ab- (POK 53; AHD apo- 1a). (b) 'apo-tero' is in fact the PIE comparative *ap(o)-tero- 'further off' (Skt. apataram, OP apataram, Gk. apōtérō), which in Germanic gives *aftar-/*after- > OE æfter, ON eptir, Goth. aftra (AHD apo- 4). Labelling the comparative itself 'Germanic' is a small imprecision, since the formation is PIE, not Germanic. (c) 'afug' = Proto-Germanic *afug-/*abuh- < *apu-ko- 'turned away', whence ON ǫfugr/afugr 'turned backwards', OS avuh, OHG abuh, OE *afoc (POK 54; AHD apo- 6). (d) 'eben : later time, evening' is the problem: this is Proto-Germanic *ēbanþ-/*ēbando- 'evening' (OE ǣfen, OS āƀand, OHG āband, ON aptann). Klein derives it not from *apo but from *epi/*opi — 'cogn. with Gk. ὄπι- in ὄπισθε(ν) "after, behind", ὀψέ "late in the day" ... hence evening lit. means "the hinder (= latter) part of the day"' — and Etymonline calls Proto-Germanic *æbando- 'of uncertain origin'. Neither Pokorny's apo- entry nor Watkins/AHD lists t…
REF: AHD=partial: AHD_watkins1985.txt s.v. 'apo-. Also ap-. Off, away.': '1. Germanic *af in: a. Old English…
CON: POK=partial: 'got. af ... ags. æf, of ... ahd. aba, ab-'; 'Ableitungen: apo-tero-'; 'ags. *afoc in engl… ; WLD=partial: 'got. af Praef. und Praep. m. Dat. "von, von—weg, von—her", anord. af Adv. und Praep. m. D… ; KLN=contradicts: 'even, n., evening (poet.) — ME. eve, even, fr. OE. æfen, rel. to OS. āƀand, ON. aptann, D… ; WEB=supports: 'awk, a. [ME. awke, auke, from Ice. ǫfugr, ǫfugr, contrary; root af, off, away] 1. contrar… ; IEC=supports: 'apo (apo, apo, po) "away; from, after". WP I, 47 ... Go. af; OHG aba "away; from", abo "b…
------------------------------------------------------------
# 2 English | of, off; after; evening; awkward | verdict: disputed | 
DER: of/off: one Old English word of/æf split in Middle English into the unstressed preposition 'of' and the stressed adverb 'off' (spelling differentiated only from the 16th c.); < PGmc *af < *h₂epo. after: OE æfter (adv./prep.) < PGmc *aftar- < the PIE comparative *ap(o)-tero-, i.e. 'further away/behind'. awkward: mid-14c. awkeward 'in the wrong direction', from ME awk 'back-handed, turned the wrong way' (a Norse loan, ON ǫfugr < PGmc *afug- < *apu-ko-) plus the adverbial suffix -ward; sense 'clumsy' from the 1520s, 'embarrassed' from c.1713. evening: OE ǣfnung, a verbal noun to ǣfnian 'to grow toward evening', from ǣfen 'evening' < PGmc *ēbando- — this last word is exactly the disputed item: Etymonline says the Proto-Germanic form 'is of uncertain origin' and stops there, Klein takes it to *epi/*opi 'after, behind', and no modern IE dictionary files it under *apo. The other three items are secure.
REF: none=not_checked: the English box carries no citation of its own in the book; it inherits the AHD reference …
CON: KLN=contradicts: 'evening, n. — ME., fr. OE. æfnung, "evening", prop. verbal n. fr. æfnian, "to become even… ; WEB=supports: 'awkward, a. [ME. awkwarde, from awk-, off, and -ward; AS. -weard ...]' — English awkward … ; AHD=partial: index line 'AWKWARD apo-'; the apo- entry yields OF, OFF, AFTER, AWKWARD, EFTSOONS. 'EVENI…
------------------------------------------------------------
# 3 Indo-European | P-os, Pos : after, behind | verdict: confirmed | 
DER: Pokorny's headword *pos 'by, about, around, beside', which he himself analyses as 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.' — i.e. an oblique case-form of the very root in the top box, which is exactly the arrow Nourai draws. Nourai's double writing 'P-os, Pos' renders that analysis (p + os). Reflexes: Arcado-Cypriot and Phrygian-Greek πος/πο-, Doric ποτί, Lithuanian pas 'at, by', OCS po 'after', and the -ti- and -kʷo- extensions that give Latin post and Indo-Iranian pasča-. Kent (Old Persian, Lexicon s.v. pasā) prefers a different parsing of the same material — 'pIE *po as in Lat. po-liō, positus, Gk. ἀπό, + *sekʷé, inst. to root noun from *sekʷ- "follow"' — but both analyses start from *(a)po, so the arrow stands either way.
REF: POK:841=supports: POK_full.txt line 68658: 'Root / lemma: pos — Meaning: by, about, around, beside — Note: p… ; AHD:1506=supports: AHD_watkins1985.txt s.v. apo-, item 7: '7. Possible root *po(s), on, in: a. Russian po ...…
CON: WLD=supports: Walde-Pokorny II 78 f. is the reference Pokorny himself cites for *pos: 'Zu lit. pas auch … ; IEC=partial: Mann has no separate *pos headword here; he files the Iranian/Slavic 'behind, after' mater… ; KNT=partial: 'pIE *po as in Lt. po-liō, positus, Gk. ἀπό, + *sekʷé, inst. to root noun from *sekʷ- "fol…
------------------------------------------------------------
# 4 Avestan / Old Persian | pasča, pasca, pasâ : after, behind; paskât : from behind here | verdict: confirmed | 
DER: Avestan pasča (Nourai's 'pasca' is simply the undiacriticked spelling of the same word) 'behind, after', both local and temporal, is *pos + the adverbial -kʷo- suffix, matching Vedic paścā́ 'behind, westward, later'; Avestan paskāt (Vedic paścā́t) is the ablative of the same stem, 'from behind, coming up behind, thereafter' — Nourai's odd gloss 'from behind here' renders Bartholomae's 'von hinten her, hinterdrein'. Old Persian has pasā (never *pasča): the -č- was lost in the south-west Iranian dialect, so OP pasā stands beside Median/Avestan pasča, and OP builds the phrasal adverb pasāva 'after that, afterwards', which is the commonest adverb in the Bīsotūn inscription. Attested in the Yašts and Vidēvdād for Avestan (Yt.10.86, Yt.13.39, V.5.40) and DB 1.27 etc. for Old Persian.
REF: POK:842=supports: POK_full.txt, root 'pos', Page(s) 841-842, derivative 2: '2. -kʷo-: Old Indic paścā (Instr…
CON: BRT=supports: 'j. paskāt Adv. 1) räumlich "von hinten her, hinterher, hinterdrein" ... 2) zeitlich "dara… ; KNT=supports: 'pasā prep. "after", temporal with acc. and local with gen.: Av. pasča, NPers. pas, Skt. p… ; WLD=supports: '2. mit -qo- ai. paścā (Instr.) Adv. "hinten, westlich, später" = av. [pasča]'.
------------------------------------------------------------
# 5 Persian | pas «پس ۱» : after | verdict: confirmed | 
DER: Old Persian pasā 'after, behind' > Middle Persian pas [ps] 'then, afterwards, behind' (MacKenzie, CPD p.65; Nyberg, Manual II s.v. pas, with the by-form pasēh) > New Persian پس pas. The chart's extras are the regular family: پسین pasīn 'last, final' continues MP pasēn [psyn'] (Mo'in's own footnote in Borhān-e Qāṭeʿ derives it 'مرکب از: پس + ین ... و پهلوی pasēn'); واپسین wāpasīn is پسین with the prefix wā- 'back'; پسوند pasvand '(grammatical) suffix' and پس‌انداز pas-andāz 'savings' are modern compounds of the same adverb. Note that Persian pas is a south-west Iranian continuation of OP pasā, not of Avestan pasča: Hübschmann stresses that OP already had pasā 'without *pasča or the like beside it'.
REF: HRN:70=supports: HRN.txt 0-based leaf 91 = printed p.70, numbered entry 315: '315. pes "hinter, nachher", p… ; BQT:403=supports: BQT_v1_pages.txt \f-leaves 627-630 = printed pp. ~402-405 (fixed by the continuation notes… ; IEC:29=partial: IEC.txt leaf 31 = printed pp.29-30 (running head 'aperos — aps'): 'apetios (apətios, apoti…
CON: PHD=supports: 'pas [AHL, BATL, ps | = M, N ~] then, afterwards, behind'; and p.65 'pasēn [psyn' | N pasi… ; NYB=supports: 'pas [PHL; BʿTL], with -c: pas-ic, adv. 1. behind: bē raft hēnd ... Vahuman pēš, Zartuxšt … ; HUB=partial: 'Hinter s ist ein Laut abgefallen in pas "hinter" = ap. pasā, vgl. zd. pasča, paskāt'; and… ; MON=silent: the searchable OCR of the Moʿin lexicon volumes does not yield a clean headword hit for پس…
------------------------------------------------------------
# 6 Sogdian | `pyš, pš : then, afterwards | verdict: confirmed | 
DER: Sogdian ʾpyš (Buddhist Sogdian, read opēš/opiš, with the by-forms ʾps-, pš-, pšy) and the prefixal/adverbial psʾ (pš-) 'then, after' both continue Old Iranian pasča directly: prothetic ʾ- (a-) before the cluster, -sč- > -š-, and the vowel raised to -ē-/-i- in the eastern Iranian development. Gharib's dictionary tags both entries '©Av. pasča'. Compounds on the same base are ʾpyšy 'after, behind', ʾpyšsʾr 'backwards', ʾpyštrw / pštrw 'later, then, afterwards'. Nourai's backtick renders the initial aleph.
REF: SOD:55,300=supports: Both page numbers are exact. SOD_pages.txt 0-based leaf 120 = printed p.55 (leaf 119 carri…
CON: SOD=supports: besides the two cited entries, 1408 'ʾpyšy — opišc? after, behind', 1409 'ʾpyšsʾr — opišc-… ; BRT=supports: supplies the Avestan etymon that Gharib's Sogdian entries point to; Bartholomae's Pahlavi … ; POK=supports: Pokorny's Iranian material is the same Avestan pasča/paskāt from which the Sogdian forms a…
------------------------------------------------------------
# 7 Latin | post : after; pônere : to place | verdict: confirmed | 
DER: post: from *pos-ti (the -ti extension of *pos, formed on the model of *anti > ante), Old Latin poste, whence by loss of final -e the classical post; cognates Oscan púst/post, Umbrian post/pus, and the derivatives posterus, postumus, posticus, and pōne < *posti-ne. pōnere: Ernout-Meillet's 'pōnō est issu de po-sinō > pozno > pōnō', i.e. the preverb po- (the zero-grade *po of *apo, as in po-liō, po-lūbrum, av. pa-zdayeiti) compounded with sinō 'let, place'; the old perfect posīuī/poslui and the participle positum still show the -s-. Its original sense was 'to set aside', generalised to 'to put, place'. Both words are put under this root by Watkins (AHD apo- 7b, 7c).
REF: AHD=supports: AHD_watkins1985.txt s.v. apo-, item 7: '... b. Latin post, behind, back, afterward: POST-,…
CON: LAT=supports: '*postī, poste, post ... post est issu de *pos-ti (cf. ante de *anti); l'i en finale absol… ; POK=supports: 'derivatives: 1. with -ti ... Latin post, Old Latin poste "after, behind", örtlich and zei… ; WLD=supports: 'lat. post, alat. poste "nach, hinter", örtlich und zeitlich ... davon lat. posterus, osk.…
------------------------------------------------------------
# 8 English | postpone; oppose, propose, compose, impose, posture | verdict: confirmed | 
DER: postpone (15th c.) is a direct Latinism, postpōnere 'to place after' = post + pōnere, so it draws on both words in the parent box. The rest are the pōnere family, all reaching English through French or directly from Latin: oppose < Old French oposer (a French re-formation of Latin oppōnere on poser), propose < OF proposer (Lat. prōpōnere), compose < OF composer (Lat. compōnere), impose < OF imposer (Lat. impōnere); the -pose verbs owe their -pos- to Late Latin pausāre crossed with the pōnere compounds, which is why the nouns keep the Latin stem (opposition, composition). posture < French posture < Italian postura < Latin positūra 'position', from positus, the participle of pōnere.
REF: none=not_checked: the English box carries no citation of its own; it inherits the AHD reference of its paren…
CON: AHD=supports: the derivative list 'APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITI… ; LAT=supports: 'Positio n'apparaît du reste qu'à l'époque impériale ... positūra (Lucr.) traduit θέσις' —… ; KLN=supports: Klein routes all the -pose verbs through Old French -poser and back to Latin pōnere/positu…
================================================================================
ENTRY 3 | root: A`.q.b | verdict: disputed | modern: Common (Proto-)Semitic root *ʿ-q-b 'heel; to follow at the heel', not specifically Syriac
NOTE: The root itself is real and its gloss is right, but the language label is wrong in a way that inverts the chart. ʿ-q-b is inherited in every branch of Semitic: Akkadian eqbu/iqbu 'heel', Ugaritic and Hebrew ʿāqēb, Aramaic/Syriac ʿeqbā and the verb ʿqab 'to track, investigate', Arabic ʿaqib 'heel' and ʿaqaba 'to follow'. Nourai's own reference says so: Klein (p.823) derives Hebrew Yaʿăqōbh from Hebrew ʿāqēbh and lists 'Aram. ʿiqbā, Akkad. iqbu ... Arab. ʿāqib, ʿaqaba' as words it 'is rel. to' — cognates, not ancestors. Hebrew Yaʿăqōb is moreover attested in Bronze-Age Amorite/Egyptian form (yaʿqub-ʾil) a millennium before Syriac existed, so Hebrew cannot descend from Syriac. The one place where a Syriac source is genuinely defensible is the sub-claim Jeffery makes on the page Nourai cites: Arabic Yaʿqūb, the Qurʾānic name, probably reached Arabic from Syriac Yaʿqūḇ. A correct root box would read 'Semitic ʿ-q-b', with the Syriac→Arabic arrow restricted to the personal name.
ROOTREF: KLN:823=partial
------------------------------------------------------------
# 1 Arabic | a`.q.b : to follow; a`qeb : heel; Ya`qŭb : A prophet's name (follower, successor) | verdict: plausible | 
DER: The three items need to be separated. (a) The verb ʿaqaba (ʿ-q-b, form I) 'to follow, come after, succeed', with form II ʿaqqaba 'to pursue, to comment' and the verbal noun taʿqīb, and (b) the noun ʿaqib/ʿaqb 'heel; end; offspring' are inherited Arabic, the regular reflexes of the common-Semitic root; they are cognate with Syriac ʿqab/ʿeqbā, not borrowed from it, and Nourai's own reference (Klein) treats them as cognates. (c) The proper name يعقوب Yaʿqūb is a different matter: it is a foreign name in Arabic, and Jeffery, on the very page cited, concludes that it most likely came in from Syriac ܝܥܩܘܒ Yaʿqūḇ through Christian channels rather than directly from Hebrew — so for this word the Syriac→Arabic arrow is exactly right. The Arabic form Yaʿqūb with -ū- reflects the Syriac vocalisation, and it was already known to the pre-Islamic Arabs; Arab lexicographers themselves classed it as a loan (al-Jawālīqī, al-Khafājī, as-Suyūṭī).
REF: KLN:823=partial: KLN_1966 leaf 444-445 (p.823), s.v. Jacob: Arabic ʿāqib 'heel', ʿiqbah 'mark, trace, sign'… ; FVQ:291=supports: FVQ_pages.txt 0-based leaf 308, running head 'FOREIGN VOCABULARY OF THE QURʾĀN 291', entry…
CON: KLN=partial: gives the Arabic forms as cognates of Hebrew, not derivatives of Syriac (quoted above). ; FVQ=supports: 'probably from the Syr. ܝܥܩܘܒ' for the name Yaʿqūb. ; RCH=supports: 'A [ʿaqib] ʿaqib, Behind, after' — the Arabic noun in its adverbial use, the form Persian … ; AFA=silent: grep for ʿaqib / Jakob turns up nothing: Fraenkel does not treat ʿ-q-b as an Aramaic loanw… ; TAD=silent: no entry for عقب or يعقوب in the OCR text.
------------------------------------------------------------
# 2 Persian | aqab «عقب» : back, behind; Ya`qŭb «یعقوب» : Jacob | verdict: confirmed | 
DER: Both are ordinary Arabic loans into New Persian, taken over from the post-conquest religious and administrative vocabulary. عقب aqab (Arabic ʿaqb/ʿaqib 'heel, hind part') is used in Persian as a noun 'back part' and a preposition/adverb 'behind, after' (عقبِ خانه, عقب رفتن), displacing native پس in much modern usage. یعقوب Yaʿqūb is the Qurʾānic form of the patriarch's name, hence also a common Persian personal name. The chart's extras are the other Arabic derivatives of the same root that Persian took over ready-made: تعقیب taʿqīb (form II verbal noun) 'pursuit, following up', عقبیٰ ʿuqbā 'the hereafter', عقوبت ʿuqūbat 'punishment' (what follows a deed), عاقبت ʿāqibat 'outcome, end'. Because they are Arabic stem-formations, not Persian coinages, they entered as whole words.
REF: FVA:276=not_checked: S. M. Nahvi, Farhang-e Vāzheh-hā-ye ʿArabi dar Fārsi — refs_online.json records 'Searched …
CON: MON=supports: the OCR shows عقب used throughout as an ordinary Persian word ('عقب: پس، پیش', 'عقب‌نشینی … ; BQT=silent: عقب occurs only inside definitions, never as a headword — expected, since Borhān is a dict… ; RCH=supports: 'A [ʿaqib], Behind, after' — listed with the 'A' (Arabic) tag in a Persian dictionary, i.e… ; FVQ=supports: establishes Yaʿqūb as the Qurʾānic Arabic form, which is the shape Persian یعقوب reflects.
------------------------------------------------------------
# 3 Hebrew | âqebh : heel; Ya`aqôbh : one that takes by the heel, follower, name of a prophet | verdict: disputed | 
DER: The forms and glosses are correct: עָקֵב ʿāqēb 'heel, footprint', verb עָקַב ʿāqab 'to follow at the heel, supplant, overreach', and יַעֲקֹב Yaʿăqōb, formally a prefix-conjugation (imperfect) of that verb, explained in Genesis 25:26 by Esau's heel and in 27:36 by the pun on ʿāqab 'he supplanted'. What is wrong is the arrow: Hebrew did not get this from Syriac. Syriac is a first-millennium-CE dialect of Eastern Aramaic, while Hebrew ʿāqēb and the name Yaʿăqōb are attested in the Iron Age and the name-type Yaʿqub-ʾil already in second-millennium Amorite and Egyptian sources; Hebrew and Syriac are sister reflexes of a common Semitic *ʿaqib-. Klein, the reference Nourai cites, builds the entry the other way round (Hebrew ʿāqēbh → ʿaqabh → Yaʿăqōbh, with Aramaic/Akkadian/Arabic as relatives). Everything below this node — Greek Ἰακώβ/Ἰάκωβος, Latin Jacobus, French Jacques — does come from the Hebrew name, so only the incoming arrow is at fault.
REF: KLN:823=supports: KLN_1966 leaf 444-445 = p.823 s.v. Jacob: 'fr. Heb. Yaʿăqōbh, lit. "one that takes by the … ; FSD:1307=supports: FSD_vol2.txt 0-based leaf 601 (page numeral 1308 on the leaf; the entry straddles 1307-130…
CON: KLN=partial: supports the Hebrew forms, contradicts the Syriac parentage (cognates, not ancestors). ; FSD=supports: 'Ja'cob ... [Heb., supplanter]', with the Latin/French/Italian/Spanish forms Jacobus, Jaco… ; AFA=silent: no treatment of ʿ-q-b; the root is not an Aramaic import anywhere. ; WEB=supports: 'LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqōb, Jacob, lit., seizing by the heel, a supplant…
------------------------------------------------------------
# 4 Greek | Jacobos | verdict: confirmed | 
DER: Greek Ἰακώβ (indeclinable) is the Septuagint's transcription of Hebrew יַעֲקֹב, with η/ω rendering the Hebrew vowels and the final -b as β; alongside it the Hellenised, fully declinable Ἰάκωβος (Nourai's 'Jacobos') was formed with the Greek masculine ending -ος and is the form used in the New Testament for James son of Zebedee and James son of Alphaeus. The doublet matters for what follows: Ἰακώβ stayed the patriarch's name, Ἰάκωβος became the apostles' name and so the ancestor of the European personal names.
REF: FSD:1307=supports: FSD_vol2.txt leaf 601 (pp.1307-1308) s.v. jack: '< LL. Jacobus, < Gr. Iakōbos, < Heb. Yaʿa…
CON: KLN=supports: 'Late L. Jacōbus, fr. Gk. Ἰακώβος, fr. Heb. Yaʿăqōbh'. ; WEB=supports: 'OFr. Jaque, Jaques; LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqōb'. ; FSD=supports: as quoted.
------------------------------------------------------------
# 5 Late Latin | Jacobŭs | verdict: confirmed | 
DER: Late Latin Iacōbus, the Vulgate/ecclesiastical Latinisation of Greek Ἰάκωβος with the second-declension ending -us (beside indeclinable Iacob for the patriarch). Within Latin it developed a popular variant Iacōmus (b > m before the labial, or by dissimilation in Vulgar Latin), and the two forms then went separate ways in Romance: Iacōbus > Spanish Jacobo/Iago (whence Sant-Iago, Diego), Old French Jaques; Iacōmus > Old French James, Italian Giacomo, Spanish Jaime, and English James. The chart's later Latin -ŭs marking simply notes the short vowel of the ending.
REF: FSD:1307=supports: FSD_vol2.txt leaf 601 (pp.1307-1308) s.v. jack: '< OF. Jacques, Jacob (= OF. Jakemes, Jame…
CON: KLN=supports: 'Jacobite ... Formed with subst. suff. -ite fr. Late L. Jacōbus, "Jacob, James"'; 'James, … ; WEB=supports: 'LL. Jacobus' in the chain OFr. Jaque(s) < LL. Jacobus < Gr. Iakobos. ; LAT=silent: a Christian-era proper name; Ernout-Meillet's dictionary of the Latin lexicon has no entry…
------------------------------------------------------------
# 6 French | Jaques | verdict: confirmed | 
DER: Old French Jaques (modern Jacques), from Late Latin Iacōbus — more precisely from a hypocoristic/diminutive of it — with the regular Gallo-Romance loss of the intervocalic -b- and of the final syllable; the spelling Jaques is the medieval one, Jacques the modern. Because Jacques was the stock name for a French peasant in the 14th century it also gave the common nouns jaque 'sleeveless coat' (> jaquette > English jacket) and jacquerie 'peasants' revolt'. From the same name France produced the feminine diminutive Jacqueline, the direct source of nodes #7 and #8.
REF: none=not_checked: the French box carries no citation of its own; the chain is covered by the KLN:823 and FSD…
CON: KLN=supports: 'OF. Jaques (F. Jacques), fr. Late L. Jacōbus, for earlier Jacobus'; and 'OF. jaque, "slee… ; FSD=supports: '< OF. Jacques, Jacob ... < LL. Jacobus'. ; DEV=silent: no entry for Jacques — expected: Devic covers Arabic/Persian/Turkish borrowings, and a bib… ; PHN=silent: no occurrence of Jacques.
------------------------------------------------------------
# 7 Persian | žâk «ژاک» | verdict: confirmed | 
DER: A modern Persian transcription of the French given name Jacques [ʒak], taken over with the twentieth-century wave of French cultural borrowings: French /ʒ/ is written ژ ž (the same letter used in ژورنال, ژنرال, ژاکت), /a/ as ا, /k/ as ک. The chart's extra ژاکلین Žāklin is French Jacqueline, the feminine diminutive of the same name, and it is the far commoner of the two in Persian. These are name transcriptions, not inherited words, so there is no sound change to describe beyond the phonemic substitution.
REF: MON=not_checked: Nourai gives no page. Proper names in Farhang-e Fārsi are in volumes 5-6 (aʿlām), which ar…
CON: MON=partial: 'ژاکت: ... (اِ.) جامهٔ مردانه که تا زانو ...' — Moʿin has the related French borrowing ژاک… ; LKT=silent: the one occurrence of 'Jacques' in the text is a bibliographic name; Lokotsch treats Orien… ; BQT=silent: a 17th-century dictionary of Persian; a 20th-century French name transcription cannot appe…
------------------------------------------------------------
# 8 English | Jacqueline | verdict: confirmed | 
DER: English Jacqueline is French Jacqueline, the feminine of Jacquelin, itself a double diminutive of Jacques (Jacques + -el + -in); it entered English in the Middle Ages (Jacquetta/Jaquelin) and was re-borrowed in its French spelling and pronunciation in the twentieth century. So the parent box (French Jaques) is the right one, and the ultimate source is Late Latin Iacōbus < Greek Ἰάκωβος < Hebrew Yaʿăqōb.
REF: AHD:699=not_checked: AHD:699 is a page in the main body of the 1975/76 American Heritage Dictionary, not in the…
CON: KLN=partial: Klein has no separate Jacqueline entry but establishes the French base: 'OF. Jaques (F. Ja… ; WEB=silent: grep for 'Jacqueline' in Webster's New Twentieth Century vol. 1 returns nothing (the name … ; FSD=supports: gives OF. Jacques as the French base from which the diminutives are formed.
------------------------------------------------------------
# 9 English | Jacob, Jack, Jim, James | verdict: disputed | 
DER: Jacob and James are secure. Jacob is the learned/biblical form, taken straight from Late Latin Iacōbus (Wycliffe onwards); James is the Middle English vernacular reflex of Late Latin Iacōmus (the b>m variant of Iacōbus) through Old French James, attested from the late 12th century. Jim is a 19th-century pet form of James (with Jimmy, Jem). Jack is the disputed item. Klein — the reference cited — makes it 'Familiar form of John, but derived fr. OF. Jaques (F. Jacques), fr. Late L. Jacōbus', and Funk & Wagnalls and Webster's say the same. Modern scholarship rejects that: the OED and Wiktionary derive Jack from Middle English Jakke/Jankin/Jankyn, via Anglo-Norman Jakke from Middle Dutch Janke, a diminutive of Jan 'John' — the vowel and the -kin suffix point to John, and the sense-history (Jack as a generic name for a common fellow) matches the John words. Jack is only secondarily used as an anglicisation of French Jacques. So the Jacobus→Jack edge as drawn is at best a minority view, and with it the descent of node #10.
REF: KLN:823=partial: KLN_1966 leaf 444 (p.823): 'Jack, masc. PN. — Familiar form of John, but derived fr. OF. J…
CON: KLN=supports: quoted above; Klein routes Jack through OF Jaques. ; FSD=supports: '[< OF. Jacques, Jacob (= OF. Jakemes, James, > E. James), < LL. Jacobus, < Gr. Iakōbos, <… ; WEB=supports: 'jack, n. [ME. Jacke, Jake; OFr. Jaque, Jaques; LL. Jacobus; Gr. Iakobos, from Heb. yaʿaqō… ; SKT=silent: the OCR of this scan is too degraded to locate the headwords Jack/James (grep for 'awkward…
------------------------------------------------------------
# 10 Persian | jak «جَک» : jack (for lifting) | verdict: confirmed | 
DER: Persian جک jak is a twentieth-century borrowing of English 'jack' in the mechanical sense — a screw or hydraulic lifting device, above all the car jack (جک ماشین) — with ج for English /dʒ/ and the short a written only by the fatḥa Nourai marks. The English word itself is the personal name Jack transferred to a labour-saving contrivance ('a boy who made himself generally useful'), so the semantic step 'servant/fellow' → 'device that does the lifting for you' happened in English, not in Persian; Persian took over only the finished technical term. The chain above it (Jack ← Jacques ← Jacobus) is the disputed part, not this last link.
REF: MON:1233=not_checked: the page itself could not be opened: Moʿin's Farhang-e Fārsi has no page-mapped digital co…
CON: MON=supports: 'ریشه‌شناسی: انگلیسی — اسم: دستگاهی به شکل اهرم که برای بالا بردن و نگاه داشتن اشیاء سنگین… ; WEB=supports: '8. any of various machines used to lift, hoist, or move something heavy a short distance;… ; BQT=silent: no entry: a modern European technical loan cannot be in a 1062/1652 dictionary.
```


## [2026-09-04T23:21:24.192Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p60.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"پوکورنی (ص ۵۳–۵۵) مدخل را با عنوان «apo- (pō̆, ap-u, pu) ‚ab, weg‘» می‌آورد، یعنی دقیقاً همان پنج صورتی که نورایی برشمرده است («Apâ» همان گونهٔ واکه‌کشیدهٔ apā، «Pô 1» همان po و «Pu 3» همان pu). برچسب زبانی و معنای «دور، از» درست است؛ بازسازیِ امروزی آن را *h₂epó می‌نویسد، هرچند āppa در هیتی را دستاویزِ بازسازیِ بی‌حنجرهٔ *apo کرده‌اند. سراسر نیمهٔ لاتینی-یونانی-ایرانیِ این نمودار بر همان یادداشت خودِ پوکورنی زیر *pos استوار است که آن را «احتمالاً *p + os، صورت اضافی-ازیِ *apo» می‌داند، پس پیکانِ ریشه به گرهٔ ۳ از آنِ پوکورنی است نه ابتکار نورایی. تنها حلقهٔ سستِ این صفحه واژهٔ «eben: شامگاه» در گرهٔ ۱ (و «evening» در گرهٔ ۲) است: نه پوکورنی و نه واتکینز واژهٔ ژرمنیِ «شامگاه» را زیر *apo نمی‌نهند و کلاین آن را به *epi/*opi می‌بندد.\",\n\"3\": \"خودِ ریشه اصیل است و معنایش درست، اما برچسب زبانی به‌گونه‌ای نادرست است که کل نمودار را وارونه می‌کند. ع-ق-ب ریشه‌ای است که در همهٔ شاخه‌های سامی به ارث رسیده است: اکدی eqbu «پاشنه»، اوگاریتی و عبری ʿāqēb، آرامی و سریانی ʿeqbā و فعل ʿqab، و عربی «عقِب» و «عَقَبَ». خودِ منبعی که نورایی ارجاع می‌دهد همین را می‌گوید: کلاین (ص ۸۲۳) Yaʿăqōbh عبری را از ʿāqēbh عبری می‌گیرد و صورت‌های آرامی و اکدی و عربی را «هم‌ریشه» می‌شمارد نه نیا. افزون بر این، نامِ عبریِ یعقوب هزار سال پیش از پیدایش سریانی، در صورت آموری/مصریِ عصر برنز (yaʿqub-ʾil) گواه دارد، پس عبری نمی‌تواند از سریانی آمده باشد. تنها جایی که منبع سریانی به‌راستی دفاع‌کردنی است همان نکته‌ای است که جفری در صفحهٔ مورد استناد می‌گوید: «یعقوب» عربیِ قرآنی احتمالاً از راه سریانی به عربی رسیده است. جعبهٔ ریشه اگر «سامی: ع-ق-ب» می‌بود درست بود و پیکان سریانی ← عربی باید تنها به همان نامِ خاص محدود می‌شد.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"سه جزء از چهار جزءِ این جعبه بازتاب راستینِ *apo اند. نخست «af» یعنی ژرمنی آغازین *ab/*af، حرف اضافه و پیشوندِ بی‌تکیه، از *h₂epo با افتادن قاعده‌مندِ واکهٔ پایانی (گوتی af، نورس کهن af، انگلیسی باستان of/æf، آلمانی علیای باستان aba). دوم «apo-tero» که در حقیقت صفت تفضیلیِ هندواروپاییِ *ap(o)-tero- «دورتر» است (سنسکریت apataram، پارسی باستان apataram، یونانی ἀπωτέρω) و در ژرمنی *aftar- > æfter انگلیسی باستان را می‌دهد — برچسب «ژرمنی» برای خودِ این ساخت اندکی بی‌دقت است، چون ساختی هندواروپایی است. سوم «afug» یعنی ژرمنی آغازین *afug- < *apu-ko- «برگردانده» که نورس کهن ǫfugr از آن است. اما «eben» با معنی «شامگاه» مشکل‌ساز است: این *ēbanþ- ژرمنی آغازین است و کلاین آن را نه از *apo بلکه از *epi/*opi می‌گیرد («شامگاه» یعنی «بخش پسینِ روز»)، و اتیمآنلاین آن را «با خاستگاه نامعلوم» می‌خواند؛ نه پوکورنی و نه واتکینز آن را ذیل *apo نیاورده‌اند، پس این جزء را پژوهش امروزی رد می‌کند.\",\n\"2\": \"of و off در اصل یک واژهٔ انگلیسی باستان (of/æf) بوده‌اند که در انگلیسی میانه به حرف اضافهٔ بی‌تکیهٔ of و قیدِ تکیه‌دارِ off دوپاره شده و املایشان تنها از سدهٔ شانزدهم جدا شده است؛ هر دو از *af ژرمنی < *h₂epo. after از æfter انگلیسی باستان و آن از تفضیلیِ *ap(o)-tero- است. awkward (میانهٔ سدهٔ چهاردهم، نخست «در جهت وارونه») از awk انگلیسی میانه ساخته شده که خود وامی از نورس کهن ǫfugr < *afug- است، به‌علاوهٔ پسوند قیدی -ward؛ معنی «ناشیانه» از دههٔ ۱۵۲۰ است. اما evening همان جزءِ مورد اختلاف است: از ǣfnung انگلیسی باستان، اسم مصدرِ ǣfnian، از ǣfen < *ēbando- ژرمنی — واژه‌ای که اتیمآنلاین خاستگاهش را نامعلوم می‌داند، کلاین به *epi/*opi می‌بندد و هیچ فرهنگ هندواروپاییِ امروزی زیر *apo نمی‌آورد. سه واژهٔ دیگر استوارند و تنها همین یکی مردود است.\",\n\"3\": \"مدخلِ *pos پوکورنی «نزد، پیرامون، کنار»، که خودِ او آن را «احتمالاً *p + os، صورت اضافی-ازیِ *apo (ص ۵۳ به بعد)» تحلیل می‌کند — یعنی دقیقاً همان پیکانی که نورایی می‌کشد؛ نگارش دوگانهٔ «P-os, Pos» نیز همین تحلیل (p + os) را نشان می‌دهد. بازتاب‌های آن یونانیِ آرکادی-قبرسی πος، دوری ποτί، لیتوانیایی pas، اسلاوی کهن po و گسترش‌های -ti- و -kʷo- است که لاتینی post و هندوایرانی pasča- را می‌دهد. کنت همین ماده را جور دیگری تجزیه می‌کند (*po + *sekʷé از ریشهٔ «پی‌گرفتن»)، اما هر دو تحلیل از *(a)po آغاز می‌شوند، پس پیکان به هر روی برجاست و ادعای نورایی درست است.\",\n\"4\": \"اوستایی pasča «پس، پشت» (چه مکانی و چه زمانی) همان *pos است با پسوند قیدیِ -kʷo-، برابر ودایی paścā́؛ و paskāt اوستایی (ودایی paścā́t) حالت ازیِ همان ستاک است، «از پشت سر، از پی» — معنای عجیبِ «from behind here» در کتاب برگردانِ عبارتِ بارتولومه «von hinten her» است. پارسی باستان همیشه pasā دارد و هرگز *pasča، زیرا -č- در گویش جنوب‌غربی افتاده است؛ از همین pasā قیدِ ترکیبیِ pasāva «پس از آن» ساخته شده که رایج‌ترین قید کتیبهٔ بیستون است. صورت «pasca»ی نورایی تنها نگارشِ بی‌نشانِ همان pasča است. گواه‌ها در یشت‌ها و وندیداد و در بیستون فراوان است و ادعای نورایی درست است.\",\n\"5\": \"پارسی باستان pasā در فارسی میانه pas [ps] «سپس، پشت» شده (مکنزی ص ۶۵؛ نیبرگ با گونهٔ pasēh) و از آنجا «پس» فارسی نو آمده است. شاهدهای نمودار همه از همین خانواده‌اند: «پسین» دنبالهٔ pasēn پهلوی است (معین در حاشیهٔ برهان: «مرکب از پس + ین ... و پهلوی pasēn»)، «واپسین» همان پسین است با پیشوند وا-، و «پسوند» و «پس‌انداز» ساخت‌های نو از همین قیدند. نکتهٔ مهم آنکه «پس» فارسی دنبالهٔ جنوب‌غربیِ pasā پارسی باستان است نه pasča اوستایی؛ هوبشمان تأکید می‌کند که پارسی باستان همان pasā را داشته «بی‌آنکه *pasča یا مانند آن در کنارش باشد». ادعای نورایی درست است.\",\n\"6\": \"سغدی ʾpyš (سغدی بودایی، خواندهٔ opēš/opiš) و گونه‌های ʾps-، pš- و pšy «سپس، پس از آن» همگی یکراست دنبالهٔ pasča ایرانی باستان‌اند: الفِ پیشین (a-) پیش از خوشه افزوده شده، خوشهٔ -sč- به -š- ساده شده و واکه در تحول ایرانیِ شرقی به -ē-/-i- برکشیده شده است. قریب هر دو مدخل را با نشانِ «©Av. pasča» ثبت کرده و ترکیب‌هایی چون ʾpyšsʾr «به عقب» و ʾpyštrw «سپس» را نیز می‌آورد. نشانِ واژگونی که نورایی پیش از واژه گذاشته همان الفِ آغازین را نشان می‌دهد؛ ادعای او درست است.\",\n\"7\": \"post لاتینی از *pos-ti است، یعنی *pos با گسترشِ -ti به قیاسِ *anti > ante؛ صورت لاتینیِ کهن poste بوده که با افتادن -e پایانی post شده، و مشتقات آن posterus، postumus و pōne < *posti-ne است. اما pōnere تحلیل دیگری دارد: ارنو-مه‌یه می‌نویسند «pōnō از po-sinō > pozno > pōnō برآمده»، یعنی پیشوندِ po- (همان درجهٔ صفرِ *apo، مانند po-liō و اوستایی pa-zdayeiti) به‌علاوهٔ sinō «نهادن»؛ ماضیِ کهنِ posīuī و اسم مفعول positum هنوز آن -s- را نشان می‌دهند. معنای نخستینِ آن «به کناری نهادن» بوده که سپس به «نهادن» عام شده است. واتکینز هر دو واژه را زیر همین ریشه می‌آورد؛ ادعای نورایی درست است.\",\n\"8\": \"postpone (سدهٔ پانزدهم) وام‌واژه‌ای یکراست لاتینی است، از postpōnere «پس نهادن» = post + pōnere، پس هر دو واژهٔ جعبهٔ مادر را در خود دارد. بقیه همه از خانوادهٔ pōnere اند و بیشتر از راه فرانسه به انگلیسی رسیده‌اند: oppose از فرانسوی کهن oposer (بازساختِ فرانسویِ oppōnere بر پایهٔ poser)، propose از proposer، compose از composer و impose از imposer؛ همین -pos- فرانسوی از آمیختنِ pausāre لاتینیِ متأخر با ترکیب‌های pōnere پدید آمده و به همین سبب است که اسم‌ها ستاک لاتینی را نگاه داشته‌اند (opposition، composition). posture از فرانسوی، از ایتالیایی postura، از لاتینی positūra «وضع» از positus می‌آید. ادعای نورایی درست است.\"\n},\n\"3\": {\n\"1\": \"سه جزء این جعبه را باید از هم جدا کرد. فعل «عَقَبَ» (باب اول) «از پی آمدن، جانشین شدن» با باب دومِ «عَقَّبَ» و مصدرِ «تعقیب»، و نیز اسمِ «عَقِب/عَقْب» «پاشنه؛ پایان؛ فرزندان»، هر دو عربیِ موروثی‌اند و بازتاب قاعده‌مندِ ریشهٔ مشترکِ سامی؛ اینها هم‌ریشهٔ ʿqab سریانی‌اند نه وام‌گرفته از آن، و خودِ کلاین که نورایی بدو ارجاع می‌دهد آنها را هم‌ریشه می‌شمارد. اما نام خاصِ «یعقوب» داستان دیگری دارد: در عربی نامی بیگانه است و جفری در همان صفحهٔ مورد استناد نتیجه می‌گیرد که به احتمال زیاد از راه مسیحیان و از سریانیِ Yaʿqūḇ وارد شده نه یکراست از عبری — پس برای این یک واژه پیکانِ سریانی ← عربی دقیقاً درست است. صورت «یعقوب» با واوِ کشیده همان آوایش سریانی را بازمی‌تاباند و لغت‌شناسان عرب (جوالیقی، خفاجی، سیوطی) خود آن را دخیل شمرده‌اند؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"2\": \"هر دو واژه وام‌واژه‌های معمولِ عربی در فارسی‌اند که با واژگان دینی و دیوانیِ پس از اسلام وارد شده‌اند. «عقب» (عربی عَقِب «پاشنه، بخش پسین») در فارسی هم اسم است و هم حرف اضافه و قید («عقبِ خانه»، «عقب رفتن») و در کاربرد امروزی تا حد زیادی جای «پس» بومی را گرفته است. «یعقوب» صورت قرآنیِ نام آن پیامبر است و از این رو نامی رایج در فارسی نیز هست. شاهدهای نمودار همه مشتقات عربیِ همین ریشه‌اند که فارسی آنها را آماده گرفته است: تعقیب، عقبیٰ، عقوبت و عاقبت؛ چون ساخت‌هایی صرفی در خودِ عربی‌اند نه ساخت‌های فارسی، به صورت واژه‌های تمام‌شده وام گرفته شده‌اند. ادعای نورایی درست است.\",\n\"3\": \"صورت‌ها و معناها درست‌اند: عبری עָקֵב ʿāqēb «پاشنه، جای پا»، فعل עָקַב ʿāqab «از پی رفتن، جای کسی را گرفتن» و יַעֲקֹב Yaʿăqōb که از نظر صرفی صیغهٔ مضارعِ همین فعل است و در سفر پیدایش (۲۵:۲۶ و ۲۷:۳۶) با اشاره به پاشنهٔ عیسو و با جناسِ ʿāqab توضیح داده شده است. آنچه نادرست است خودِ پیکان است: عبری این واژه‌ها را از سریانی نگرفته است. سریانی گویشی از آرامیِ شرقی در هزارهٔ نخست میلادی است، حال آنکه ʿāqēb و نام یعقوب در عصر آهن و حتی صورتِ نام‌گونهٔ yaʿqub-ʾil در منابع آموری و مصریِ هزارهٔ دوم پیش از میلاد گواه دارند؛ عبری و سریانی هر دو بازتاب خواهروارِ سامیِ *ʿaqib- اند. کلاین نیز مدخل را وارونهٔ نمودار می‌چیند. هرچه زیر این گره است — یونانی Ἰακώβ، لاتینی Jacobus، فرانسوی Jacques — به‌راستی از نام عبری می‌آید، پس تنها همین پیکانِ ورودی نادرست است.\",\n\"4\": \"یونانی Ἰακώβ (صرف‌ناپذیر) آوانگاریِ سبعینیه از عبری יַעֲקֹב است که در آن واکه‌های عبری با η و ω و بای پایانی با β نشان داده شده‌اند؛ در کنار آن صورتِ یونانی‌شده و صرف‌پذیرِ Ἰάκωβος با پایانهٔ مذکرِ -ος ساخته شد که در عهد جدید نام یعقوبِ پسر زبدی و یعقوبِ پسر حلفی است. همین دوگانگی برای ادامهٔ نمودار مهم است: Ἰακώβ نام آن پیامبر ماند و Ἰάκωβος نام حواریان شد و از همین رو نیای نام‌های اروپایی است. ادعای نورایی درست است.\",\n\"5\": \"لاتینیِ متأخر Iacōbus، لاتینی‌سازیِ کلیسایی و ولگاتیِ Ἰάκωβος یونانی با پایانهٔ صرفِ دومِ -us است (در کنار Iacobِ صرف‌ناپذیر برای آن پیامبر). در درون لاتینی گونهٔ مردمیِ Iacōmus پدید آمد (b > m در مجاورت لبی، یا از راه ناهمگونی در لاتینی عامیانه) و این دو صورت در زبان‌های رومی راه‌های جداگانه رفتند: Iacōbus به اسپانیایی Jacobo/Iago (و از آنجا Santiago و Diego) و فرانسوی کهن Jaques، و Iacōmus به فرانسوی کهن James، ایتالیایی Giacomo، اسپانیایی Jaime و انگلیسی James. علامت کوتاهِ -ŭs در نمودار نیز تنها کوتاهیِ واکهٔ پایانه را نشان می‌دهد؛ ادعای نورایی درست است.\",\n\"6\": \"فرانسوی کهن Jaques (امروزی Jacques) از لاتینیِ متأخر Iacōbus می‌آید، دقیق‌تر از صورتی تصغیری/تحبیبیِ آن، با افتادن قاعده‌مندِ -b- میان‌واکه‌ای و هجای پایانی در گالو-رومی؛ املای Jaques صورت سده‌های میانه است و Jacques صورت نو. چون Jacques در سدهٔ چهاردهم نامِ نوعیِ دهقان فرانسوی بود، اسم‌های عامِ jaque «قبای بی‌آستین» (> jaquette > jacket انگلیسی) و jacquerie «شورش دهقانان» نیز از آن ساخته شد. از همین نام مؤنثِ تصغیریِ Jacqueline پدید آمد که سرچشمهٔ گره‌های ۷ و ۸ است. ادعای نورایی درست است.\",\n\"7\": \"«ژاک» آوانگاریِ فارسیِ نامِ فرانسویِ Jacques است که با موج وام‌گیری‌های فرهنگیِ فرانسه در سدهٔ چهاردهم خورشیدی وارد شده است: /ʒ/ فرانسوی با «ژ» نوشته می‌شود (همان حرفی که در ژورنال و ژنرال و ژاکت به کار می‌رود)، /a/ با الف و /k/ با کاف. «ژاکلین» در شاهدها همان Jacqueline، مؤنثِ تصغیریِ همین نام، و در فارسی بسی رایج‌تر از «ژاک» است. اینها آوانگاریِ نام‌اند نه واژه‌های موروثی، پس جز جانشینیِ واج‌ها دگرگونی آوایی‌ای در کار نیست؛ ادعای نورایی درست است.\",\n\"8\": \"Jacqueline انگلیسی همان Jacqueline فرانسوی است، مؤنثِ Jacquelin که خود تصغیرِ مضاعفِ Jacques است (Jacques + -el + -in)؛ در سده‌های میانه به صورت Jacquetta/Jaquelin به انگلیسی راه یافت و در سدهٔ بیستم بار دیگر با املا و تلفظ فرانسوی وام گرفته شد. پس جعبهٔ مادر (فرانسوی Jaques) درست است و سرچشمهٔ نهایی لاتینیِ متأخر Iacōbus < یونانی Ἰάκωβος < عبری Yaʿăqōb است. ادعای نورایی درست است.\",\n\"9\": \"Jacob و James استوارند: Jacob صورت کتابی و کتاب‌مقدسی است که یکراست از Iacōbus لاتینیِ متأخر گرفته شده، و James بازتاب مردمیِ Iacōmus (گونهٔ b>m همان نام) از راه فرانسوی کهن James است که از اواخر سدهٔ دوازدهم گواه دارد؛ Jim نیز صورت تحبیبیِ James در سدهٔ نوزدهم است. اما Jack جزء مورد اختلاف است: کلاین — همان منبعی که نورایی ارجاع می‌دهد — آن را «صورت خودمانیِ John، اما گرفته از فرانسوی کهن Jaques» می‌داند و وبستر و فانک و واگنالز نیز همین را می‌گویند. پژوهش امروزی این را رد می‌کند: فرهنگ آکسفورد و ویکی‌واژه Jack را از انگلیسی میانه Jakke/Jankin و آن را از راه انگلوـنورمن از هلندی میانه Janke، تصغیرِ Jan «یوحنا»، می‌گیرند؛ واکه و پسوند -kin و نیز تاریخِ معنایی (Jack به معنی «مردِ عادی») همه به John اشاره دارند. پس این پیکان در بهترین حالت رأی اقلیت است و گرهٔ ۱۰ نیز بر آن استوار شده است.\",\n\"10\": \"«جَک» در فارسی وام‌واژه‌ای از انگلیسیِ jack در معنای فنیِ آن است که در سدهٔ چهاردهم خورشیدی وارد شده — ابزار بالابرِ پیچی یا هیدرولیک، به‌ویژه «جک ماشین» — با «ج» برای /dʒ/ انگلیسی و فتحه‌ای که نورایی نشان داده است. خودِ واژهٔ انگلیسی همان نام خاصِ Jack است که به ابزارِ کارگشا منتقل شده («پسری که به هر کاری می‌آمد»)، پس تحول معناییِ «نوکر/مردِ عادی» به «دستگاهی که بار را برایت بلند می‌کند» در انگلیسی رخ داده و فارسی تنها اصطلاح فنیِ آماده را گرفته است. آنچه محل اختلاف است زنجیرهٔ بالای این گره است (Jack ← Jacques ← Jacobus) نه این حلقهٔ آخر؛ در خودِ این حلقه ادعای نورایی درست است.\"\n}\n}\n}\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa.py 60 p60.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-60.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-60.json",
 "description": "Apply Persian to page 60"
}
```


### [2026-09-04T23:21:27.465Z] TOOL RESULT

```
ok 60
JSON_OK
 data/verification/page-60.json | 655 ++++++++++++++++++++++++++++++++++-------
 1 file changed, 556 insertions(+), 99 deletions(-)
```


## [2026-09-04T23:21:30.874Z] TOOL CALL #22: Bash

```json
{
 "command": "git -C /home/sfmqrb/git/rishe diff -- data/verification/page-60.json | head -40",
 "description": "Inspect page 60 diff"
}
```


### [2026-09-04T23:21:32.745Z] TOOL RESULT

```
diff --git a/data/verification/page-60.json b/data/verification/page-60.json
index b11f9e2..dfae664 100644
--- a/data/verification/page-60.json
+++ b/data/verification/page-60.json
@@ -10,12 +10,17 @@
       "verdict": "confirmed",
       "modern_form": "PIE *h₂epo (*apo, with ablaut/enclitic variants *apā, *ap-u, *pu, *po) 'off, away, from'",
       "note": "Pokorny IEW 53-55 heads the entry 'apo- (pō̆, ap-u, pu) \"ab, weg\"', i.e. exactly the five shapes Nourai lists (his 'Apâ' = the long-vowel variant apā, 'Pô 1' = Pokorny's po, 'Pu 3' = Pokorny's pu). Language label (Indo-European) and gloss ('off') are right; the current reconstruction writes it *h₂epó, though Hittite āppa is used to argue for laryngeal-less *apo. The whole Latin/Greek/Iranian half of the chart hangs on Pokorny's own remark under *pos that it is 'probably *p + os, Gen.-Abl. to *apo above S. 53 f.', so the root→#3 arrow is Pokorny's, not Nourai's invention. The single weak link on this chart is the item 'eben : later time, evening' in node #1 (and 'evening' in node #2): neither Pokorny nor Watkins/AHD puts the Germanic word for 'evening' under *apo, and Klein assigns it to *epi/*opi.",
+      "note_fa": "پوکورنی (ص ۵۳–۵۵) مدخل را با عنوان «apo- (pō̆, ap-u, pu) ‚ab, weg‘» می‌آورد، یعنی دقیقاً همان پنج صورتی که نورایی برشمرده است («Apâ» همان گونهٔ واکه‌کشیدهٔ apā، «Pô 1» همان po و «Pu 3» همان pu). برچسب زبانی و معنای «دور، از» درست است؛ بازسازیِ امروزی آن را *h₂epó می‌نویسد، هرچند āppa در هیتی را دستاویزِ بازسازیِ بی‌حنجرهٔ *apo کرده‌اند. سراسر نیمهٔ لاتینی-یونانی-ایرانیِ این نمودار بر همان یادداشت خودِ پوکورنی زیر *pos استوار است که آن را «احتمالاً *p + os، صورت اضافی-ازیِ *apo» می‌داند، پس پیکانِ ریشه به گرهٔ ۳ از آنِ پوکورنی است نه ابتکار نورایی. تنها حلقهٔ سستِ این صفحه واژهٔ «eben: شامگاه» در گرهٔ ۱ (و «evening» در گرهٔ ۲) است: نه پوکورنی و نه واتکینز واژهٔ ژرمنیِ «شامگاه» را زیر *apo نمی‌نهند و کلاین آن را به *epi/*opi می‌بندد.",
       "sources": [
         "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82epo",
         "https://www.ahdictionary.com/word/indoeurop.html"
       ],
       "ref_check": [
-        {"ref": "POK:53", "status": "supports", "note": "POK_01.txt 0-based leaf 61 = printed p.53 (leaf 62 carries the running number '54'): the entry 'apo-, (pō̆, ap-u, pu) \"ab, weg\"' runs pp. 53-55 and contains 'got. af Präf. und Präp. m. Dat. \"von, von—weg\" ... ags. æf, of, as. af, ahd. aba', 'Ableitungen: apo-tero-, ap-ero-, ap-io-, ap-öko-', 'ags. *afoc in engl. awkward, aus *apu-ko-s', and closes 'S. noch idg. *po-ti und *po-s' — exactly the material Nourai's chart draws."}
+        {
+          "ref": "POK:53",
+          "status": "supports",
+          "note": "POK_01.txt 0-based leaf 61 = printed p.53 (leaf 62 carries the running number '54'): the entry 'apo-, (pō̆, ap-u, pu) \"ab, weg\"' runs pp. 53-55 and contains 'got. af Präf. und Präp. m. Dat. \"von, von—weg\" ... ags. æf, of, as. af, ahd. aba', 'Ableitungen: apo-tero-, ap-ero-, ap-io-, ap-öko-', 'ags. *afoc in engl. awkward, aus *apu-ko-s', and closes 'S. noch idg. *po-ti und *po-s' — exactly the material Nourai's chart draws."
+        }
       ],
       "nodes": [
         {
@@ -24,20 +29,50 @@
           "words": "af; apo-tero; eben; afug",
           "verdict": "disputed",
           "derivation": "Three of the four items are straight reflexes of *apo. (a) 'af' = Proto-Germanic *ab/*af, unstressed preposition/prefix from PIE *h₂epo with regular loss of the final vowel: Gothic af, Old Norse af, Old English of/æf, Old Saxon af, OHG aba/ab- (POK 53; AHD apo- 1a). (b) 'apo-tero' is in fact the PIE comparative *ap(o)-tero- 'further off' (Skt. apataram, OP apataram, Gk. apōtérō), which in Germanic gives *aftar-/*after- > OE æfter, ON eptir, Goth. aftra (AHD apo- 4). Labelling the comparative itself 'Germanic' is a small imprecision, since the formation is PIE, not Germanic. (c) 'afug' = Proto-Germanic *afug-/*abuh- < *apu-ko- 'turned away', whence ON ǫfugr/afugr 'turned backwards', OS avuh, OHG abuh, OE *afoc (POK 54; AHD apo- 6). (d) 'eben : later time, evening' is the problem: this is Proto-Germanic *ēbanþ-/*ēbando- 'evening' (OE ǣfen, OS āƀand, OHG āband, ON aptann). Klein derives it not from *apo but from *epi/*opi — 'cogn. with Gk. ὄπι- in ὄπισθε(ν) \"after, behind\", ὀψέ \"late in the day\" ... hence evening lit. means \"the hinder (= latter) part of the day\"' — and Etymonline calls Proto-Germanic *æbando- 'of uncertain origin'. Neither Pokorny's apo- entry nor Watkins/AHD lists the word. Hence 'disputed' for this one item only.",
+          "derivation_fa": "سه جزء از چهار جزءِ این جعبه بازتاب راستینِ *apo اند. نخست «af» یعنی ژرمنی آغازین *ab/*af، حرف اضافه و پیشوندِ بی‌تکیه، از *h₂epo با افتادن قاعده‌مندِ واکهٔ پایانی (گوتی af، نورس کهن af، انگلیسی باستان of/æf، آلمانی علیای باستان aba). دوم «apo-tero» که در حقیقت صفت تفضیلیِ هندواروپاییِ *ap(o)-tero- «دورتر» است (سنسکریت apataram، پارسی باستان apataram، یونانی ἀπωτέρω) و در ژرمنی *aftar- > æfter انگلیسی باستان را می‌دهد — برچسب «ژرمنی» برای خودِ این ساخت اندکی بی‌دقت است، چون ساختی هندواروپایی است. سوم «afug» یعنی ژرمنی آغازین *afug- < *apu-ko- «برگردانده» که نورس کهن ǫfugr از آن است. اما «eben» با معنی «شامگاه» مشکل‌ساز است: این *ēbanþ- ژرمنی آغازین است و کلاین آن را نه از *apo بلکه از *epi/*opi می‌گیرد («شامگاه» یعنی «بخش پسینِ روز»)، و اتیمآنلاین آن را «با خاستگاه نامعلوم» می‌خواند؛ نه پوکورنی و نه واتکینز آن را ذیل *apo نیاورده‌اند، پس این جزء را پژوهش امروزی رد می‌کند.",
           "sources": [
             "https://www.ahdictionary.com/word/indoeurop.html",
             "https://www.etymonline.com/word/awkward",
             "https://www.etymonline.com/word/evening"
           ],
           "ref_check": [
-            {"ref": "AHD", "status": "partial", "note": "AHD_watkins1985.txt s.v. 'apo-. Also ap-. Off, away.': '1. Germanic *af in: a. Old English of, æf (> Middle English of, of-), off: OF, OFF ... 4. Suffixed (comparative) form *ap(o)-tero- in Germanic *aftar- in Old English æfter, after, behind: AFTER ... 6. Suffixed form *apu-ko- in Germanic *afug- in Old Norse ǫfugr, turned backward: AWKWARD.' — supports af, apo-tero and afug verbatim, but the entry has no 'evening' item (the AHD index line reads 'EVEN oi-no-', 'EVENTIDE da-'); the current online AHD apo- entry likewise lists only off, ebb, awkward, puny, compote."}
+            {
+              "ref": "AHD",
+              "status": "partial",
+              "note": "AHD_watkins1985.txt s.v. 'apo-. Also ap-. Off, away.': '1. Germanic *af in: a. Old English of, æf (> Middle English of, of-), off: OF, OFF ... 4. Suffixed (comparative) form *ap(o)-tero- in Germanic *aftar- in Old English æfter, after, behind: AFTER ... 6. Suffixed form *apu-ko- in Germanic *afug- in Old Norse ǫfugr, turned backward: AWKWARD.' — supports af, apo-tero and afug verbatim, but the entry has no 'evening' item (the AHD index line reads 'EVEN oi-no-', 'EVENTIDE da-'); the current online AHD apo- entry likewise lists only off, ebb, awkward, puny, compote."
+            }
```


## [2026-09-04T23:21:50.336Z] TOOL CALL #23: Bash

```json
{
 "command": "git checkout data/verification/page-60.json && python3 - <<'EOF'\nimport json,collections\nfor p in [60,101,126,311,345]:\n    path=f'data/verification/page-{p}.json'\n    raw=open(path).read()\n    d=json.loads(raw,object_pairs_hook=collections.OrderedDict)\n    s=json.dumps(d,ensure_ascii=False,indent=2)+('\\n' if raw.endswith('\\n') else '')\n    print(p,'roundtrip',s==raw)\nEOF\ngrep -n '\"derivation\"' data/verification/page-60.json | head -3 | cut -c1-60\ngrep -n '\"note\"' data/verification/page-60.json | head -3 | cut -c1-60",
 "description": "Restore page 60, test roundtrips"
}
```


### [2026-09-04T23:21:52.625Z] TOOL RESULT

```
Updated 1 path from the index
60 roundtrip False
101 roundtrip True
126 roundtrip False
311 roundtrip True
345 roundtrip True
26:          "derivation": "Three of the four items are stra
48:          "derivation": "of/off: one Old English word of/
68:          "derivation": "Pokorny's headword *pos 'by, abo
12:      "note": "Pokorny IEW 53-55 heads the entry 'apo- (p
18:        {"ref": "POK:53", "status": "supports", "note": "
33:            {"ref": "AHD", "status": "partial", "note": "
```


## [2026-09-04T23:22:04.299Z] TOOL CALL #24: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa_text.py <<'PYEOF'\nimport json,re,sys\npage=sys.argv[1]; patch=json.load(open(sys.argv[2]))\npath=f'/home/sfmqrb/git/rishe/data/verification/page-{page}.json'\nlines=open(path).read().split('\\n')\nout=[]; cur_e=None; cur_n=None; done=set()\nfor ln in lines:\n    out.append(ln)\n    m=re.match(r'^      \"entry\": (\\d+),\\s*$',ln)\n    if m: cur_e=m.group(1); cur_n=None; continue\n    m=re.match(r'^          \"id\": (\\d+),\\s*$',ln)\n    if m: cur_n=m.group(1); continue\n    m=re.match(r'^      \"note\": (.*)$',ln)\n    if m and cur_e is not None and cur_n is None:\n        val=json.dumps(patch['entry'][cur_e],ensure_ascii=False)\n        out.append(f'      \"note_fa\": {val},')\n        done.add(('e',cur_e)); continue\n    m=re.match(r'^          \"derivation\": (.*)$',ln)\n    if m and cur_n is not None:\n        val=json.dumps(patch['nodes'][cur_e][cur_n],ensure_ascii=False)\n        out.append(f'          \"derivation_fa\": {val},')\n        done.add(('n',cur_e,cur_n)); continue\nnew='\\n'.join(out)\nd=json.loads(new)\nmiss=[]\nfor en in d['entries']:\n    if 'note_fa' not in en: miss.append(('entry',en['entry']))\n    for n in en['nodes']:\n        if 'derivation_fa' not in n: miss.append((en['entry'],n['id']))\nif miss:\n    print('MISSING',miss); sys.exit(1)\nopen(path,'w').write(new)\nprint('ok',page,len(done))\nPYEOF\necho done",
 "description": "Write text-based apply script"
}
```


### [2026-09-04T23:22:04.343Z] TOOL RESULT

```
done
```


## [2026-09-04T23:22:10.712Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 apply_fa_text.py 60 p60.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-60.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-60.json",
 "description": "Apply page 60 textually"
}
```


### [2026-09-04T23:22:12.796Z] TOOL RESULT

```
ok 60 20
JSON_OK
 data/verification/page-60.json | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)
```


## [2026-09-04T23:22:14.503Z] AGENT

Now page 101.


## [2026-09-04T23:22:15.574Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 101 2>&1 | head -240",
 "description": "Dump page 101"
}
```


### [2026-09-04T23:22:17.833Z] TOOL RESULT

```
##########################################################################################
PAGE 101 book 71
================================================================================
ENTRY 0 | root: B.r.k | verdict: confirmed | modern: Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)
NOTE: The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.
ROOTREF: FVQ:75=supports
------------------------------------------------------------
# 1 Arabic | b.r.k; barakat | verdict: confirmed | 
DER: Arabic root b-r-k: baraka 'to kneel (of a camel)' (verbal noun burūk), Form III bāraka 'to bless', Form II barraka, Form VI tabāraka 'be blessed'; the noun baraka(t) 'blessing, divine favour' is the maṣdar-type noun of the root, with tāʾ marbūṭa -at (hence the transliteration barakat). Cognate with Hebrew bērēkh 'to bless' / bərākhā 'blessing'. Wiktionary lists 11 Arabic derivatives of the root.
REF: KLN:164=supports: KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, fro… ; FVQ:75=supports: Same page as the root: 'Ar. bāraka as above' derived from the N. Semitic sense 'to bless' …
CON: LKT=supports: LKT.txt \f-leaf 46 = printed p. 20, no. 222: 'Ar. baraka: "Segen (nämlich Gottes)", ebenso… ; TAD=silent: Al-Unaysi's dictionary of loanwords in Arabic has no b-r-k headword; the only occurrence o… ; AFM=silent: Addi Shir's list of Persian words arabicised contains no b-r-k entry, i.e. he does not reg…
------------------------------------------------------------
# 2 Persian | barekat | verdict: confirmed | 
DER: New Persian barakat برکت is a direct loan of Arabic baraka(t) with the Arabic construct/pausal -at preserved as -at (a regular treatment of Arabic feminine nouns in Persian, cf. رحمت, نعمت); Wiktionary derives Urdu barkat from Classical Persian barakat < Arabic. The extra forms are all Arabic derivatives of the same root borrowed into Persian: tabrīk تبریک (Form II maṣdar 'congratulation'), tabarruk تبرّک (Form V maṣdar 'seeking blessing; blessed object'), mubārak مبارک (Form III passive participle 'blessed').
REF: FVA:45=not_checked: FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json).
CON: MON=supports: 'برکت: [ع. برکة] (مص ل.) گوالیدن. فزونی، بسیاری. خجستگی، یمن. نیکبختی، سعادت؛ ج. برکات.' —… ; HRN=silent: Horn's Grundriss has no barakat article: he deliberately excludes Arabic loanwords from Pe… ; BQT=silent: No headword برکت recoverable from the Borhan-e Qate' vol. 1 page OCR. ; ARY=silent: Aryanpur's dictionary of Indo-European roots of Persian has no entry — consistent with an …
------------------------------------------------------------
# 3 Akkadian | karâbu | verdict: plausible | 
DER: Akkadian karābu 'to pray, bless, greet, praise' (participle kāribu 'one who blesses/intercedes', diminutive kurību, a protective genius) is a real word of root k-r-b. Its connection to b-r-k is the metathesis hypothesis (Dhorme; Klein 164; AHD Semitic roots: 'krb, to praise, common Semitic root, with West Semitic metathesized variant brk'). So Nourai's cited sources (KLN, AHD) do assert this, and AHD still does; but the Semantics of Ancient Hebrew Database (Mitchell) rejects it because metathesis of the first and third radicals is extremely rare, and Wiktionary's Proto-Semitic *birk- page lists no Akkadian karābu. Verdict: accepted by some, rejected by others.
REF: KLN:164=supports: KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, fro… ; AHD:579=partial: AHD:579 is the 1976 dictionary page (griffin); the current AHD griffin entry (archived, ht…
CON: AKD=partial: AKD.txt \f-leaf 75 (Zimmern p. ~66, §17 'Religion, Kultus und Mythus'; grep -n 'segnen' AK… ; AKD=supports: AKD.txt \f-leaf 78 (Zimmern p. ~69; grep -n 'Mribu  wörtl' AKD.txt): 'akk. kāribu wörtl. s… ; MON=partial: 'کروبی: [ع. آشوری، پاسبان] (اِ.) در تورات کروب (ج. کروبیم) به فرشتگانی اطلاق شده که …' — M… ; TAD=partial: TAD_pages.txt \f-leaf 66 (al-Unaysi printed p. ~61), s.v. كروبيم وكروبين وشاروبين: 'كروبيم…
------------------------------------------------------------
# 4 Hebrew | berâkah; kerŭbh | verdict: plausible | 
DER: bərākhā בְּרָכָה 'blessing' (root b-r-k, verb bērēkh 'to bless', berekh 'knee') is a straightforward member of the root and is confirmed (cognate with Arabic baraka). kərūḇ כְּרוּב 'cherub' (pl. kərūḇīm; Gen. 3:24, Ex. 25:18) is by the mainstream view a loan from Akkadian kāribu/kurību 'intercessor; protective winged genius' (root k-r-b, karābu 'to bless') — so it belongs with Akkadian karābu (node 3), and the chart's placing of it under b-r-k stands or falls with the krb/brk metathesis hypothesis: endorsed by Klein and AHD, rejected by SAHD/Mitchell. Robert Alter's alternative ('hybrid' or, by consonant inversion, rkb 'mount/steed') is also on the table. Worst verdict for the node: plausible.
REF: KLN:274=supports: KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, pr… ; KLN:164=supports: KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, fro…
CON: AKD=partial: AKD.txt \f-leaf 78 (Zimmern p. ~69; grep -n 'Mribu  wörtl' AKD.txt): 'akk. kāribu wörtl. s… ; SKT=silent: SKT.txt \f-leaf 99 = Skeat p. 79, s.v. Cherub: 'Cherub. (Heb.) The true pl. is cherub-im, … ; FSD=silent: FSD_vol1.txt \f-leaf 516, s.v. cherub: '3. One of an order of angelic beings ranking secon… ; TAD=partial: TAD_pages.txt \f-leaf 66 (al-Unaysi printed p. ~61), s.v. كروبيم وكروبين وشاروبين: 'كروبيم…
------------------------------------------------------------
# 5 Arabic | karŭbiyy | verdict: confirmed | 
DER: Arabic karūbī كَرُوبِيّ 'cherub, archangel' (pl. karūbiyyūn, as in al-malāʾika al-karūbiyyūn) is, per Wiktionary, borrowed from Hebrew kərūḇ (in practice through Jewish Aramaic/Syriac kərūḇā, the vehicle of most biblical vocabulary into Arabic) with the Arabic nisba suffix -iyy added to form an adjective/noun of relation; the word appears in early Islamic tradition (hadith and tafsīr) for the highest angels. Not from the Akkadian directly.
REF: MON:2958=supports: vajehyab.com (Mo'in) s.v. کروبی: '(کَ یّ) [ع.] (اِ.) فرشتة مقرب درگاه. ج. کروبیون' — tagge…
CON: TAD=supports: TAD_pages.txt \f-leaf 66 (al-Unaysi printed p. ~61), s.v. كروبيم وكروبين وشاروبين: 'كروبيم… ; FVQ=silent: Jeffery has no entry: karūbī is not a Qur'anic word, so the Foreign Vocabulary of the Qur'… ; AFM=silent: Addi Shir does not list karūbī, i.e. he does not treat it as a Persian loan into Arabic.
------------------------------------------------------------
# 6 Persian | karrŭbî | verdict: confirmed | 
DER: Persian karrūbī کرّوبی is Arabic karūbī taken over unchanged (Persian writers often geminate the r, karrūbī, as Nourai's spelling shows); the plurals karrūbiyān کروبیان (Persian -ān) and karrūbiyūn کروبیون (Arabic sound plural) are both used. Attested in classical poetry, e.g. Sa'di's Bustan (13th c.), as quoted in the chart. Gloss 'angel' is loose: the word means specifically 'cherub, one of the highest angels'. Nourai's source MON (Mo'in) is the standard Persian dictionary for this and Wiktionary's Arabic entry confirms the Arabic base; no independent Persian etymological page was found, but the Arabic loan is uncontroversial.
REF: MON:2958=supports: vajehyab.com (Mo'in) s.v. کروبی [ع.] 'فرشتة مقرب درگاه، ج. کروبیون'; also کروبیان 'فرشتگان…
CON: TAD=partial: TAD_pages.txt \f-leaf 66 (al-Unaysi printed p. ~61), s.v. كروبيم وكروبين وشاروبين: 'كروبيم… ; BQT=silent: No کروبی headword recoverable from the Borhan-e Qate' vols. 3-4 page OCR. ; ARY=silent: Aryanpur has no entry — as expected for a Semitic loan in a dictionary of Indo-European ro…
------------------------------------------------------------
# 7 English | cherub | verdict: confirmed | 
DER: Hebrew kərūḇ was transliterated in the Septuagint (3rd–2nd c. BCE) as Greek χερούβ (pl. χερουβίμ), taken into Late Latin as cherub (pl. cherubim, Vulgate), and borrowed into Middle English in the late 14th c. as cherub 'an order of angels'; the sense 'winged child, putto' (the '(of love)' in Nourai's gloss) is Renaissance art usage, in English from c. 1705. The chart correctly draws it from Hebrew, not through Arabic. AHD's entry: 'from Late Latin, from Hebrew kərûb; see krb'.
REF: AHD:231=supports: AHD online s.v. cherub (archived, https://ahdictionary.com/word/search.html?q=cherub): '[M…
CON: SKT=supports: SKT.txt \f-leaf 99 = Skeat p. 79, s.v. Cherub: 'Cherub. (Heb.) The true pl. is cherub-im, … ; FSD=supports: FSD_vol1.txt \f-leaf 516, s.v. cherub: '3. One of an order of angelic beings ranking secon… ; WEB=supports: WEB_vol1.txt \f-leaf 340, s.v. cherub: '[ME. cherub; ... L. cherub; ... [Heb.] kerūb, a ch…
------------------------------------------------------------
# 8 Greek | gruphos, grups | verdict: plausible | 
DER: Greek γρύψ grȳps, gen. γρυπός grȳpós 'griffin' (Herodotus, Aeschylus) — the second form Nourai gives, 'gruphos', is not a Greek nominative but reflects the genitive grypos / Latin gryphus. Its origin is unsettled: one view links it to γρυπός 'hook-nosed, curved' (PIE *ger- 'to bend'); Klein (KLN:680, Nourai's source) and Beekes allow a Pre-Greek/Anatolian loan ultimately from Semitic (Akkadian karūbu/kāribu, Hebrew kərūḇ) 'through the medium of the Hittites', making it a doublet of χερούβ. Wiktionary reports both; AHD's own griffin entry gives no Semitic source, and SAHD notes Brown's kərūḇ–γρύψ link 'finds minimal scholarly acceptance'. So the edge Hebrew kerubh → Greek gryps is a respectable but minority hypothesis.
REF: KLN:680=supports: KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr… ; AHD:579=partial: AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): '…
CON: SKT=contradicts: SKT.txt \f-leaf 208 = Skeat p. 188, s.v. Griffin, Griffon: '(F.—L.—Gk.) Better griffon. M.… ; FSD=contradicts: FSD_vol2.txt \f-leaf 365, s.v. griffin: '[< F. griffon, < LL. gryphon-, < gryphus, < L. gr… ; WEB=contradicts: WEB_vol1.txt \f-leaf 841, s.v. griffin/griffon: '[... L. gryps; ... Gr. grypos, ... hooked… ; AKD=partial: AKD.txt \f-leaf 78 (Zimmern p. ~69; grep -n 'Mribu  wörtl' AKD.txt): 'akk. kāribu wörtl. s…
------------------------------------------------------------
# 9 Latin | gryphus | verdict: confirmed | 
DER: Latin grȳps, grȳpis (Vergil, Pliny) was borrowed from Greek γρύψ; Late Latin created the thematic variants grȳpus and grȳphus (the -ph- is a hypercorrect spelling, etymonline: 'misspelling of grypus'), and it is the Late Latin gryphus/grifus that the Romance forms continue.
REF: AHD:579=supports: AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): '…
CON: LAT=supports: LAT.txt \f-leaf 524 (Ernout-Meillet p. ~506), s.v. gryphus: 'gryphus, -ī m. (grifus, etc.)… ; SKT=supports: SKT.txt \f-leaf 208 = Skeat p. 188, s.v. Griffin, Griffon: '(F.—L.—Gk.) Better griffon. M.… ; LEW=silent: Walde's Lateinisches etymologisches Wörterbuch (1910) has no gryphus article — it omits tr…
------------------------------------------------------------
# 10 Old French | grifion | verdict: plausible | 
DER: Old French grifon / griffon (12th c.; Anglo-Norman grifun, griffoun) is Late Latin gryphus with the augmentative/derivational suffix -on (< Latin -ōnem), i.e. from a Late Latin *grifonem; AHD: 'Old French griffon, from grif, from Latin grypus, gryphus'. The edge Latin → Old French → English is certain. The spelling 'grifion' printed here is not a standard attested Old French form (expected grifon/griffon); it may be Nourai's or the scan's slip for grifon, but since Klein's page could not be checked it is left as plausible rather than transcription_suspect.
REF: KLN:680=supports: KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr…
CON: SKT=partial: SKT.txt \f-leaf 208 = Skeat p. 188, s.v. Griffin, Griffon: '(F.—L.—Gk.) Better griffon. M.… ; FSD=partial: FSD_vol2.txt \f-leaf 365, s.v. griffin: '[< F. griffon, < LL. gryphon-, < gryphus, < L. gr… ; WEB=partial: WEB_vol1.txt \f-leaf 841, s.v. griffin/griffon: '[... L. gryps; ... Gr. grypos, ... hooked…
------------------------------------------------------------
# 11 English | griffin | verdict: confirmed | 
DER: Middle English griffoun, griffon (c. 1200 as a surname, 14th c. as the beast) from Old French grifon; the modern spelling griffin/gryphon settled in the 16th–17th c. (gryphon re-Latinised after Latin gryphus). Sense: the eagle-headed, lion-bodied guardian of Scythian gold in Greek legend.
REF: AHD:579=supports: AHD online s.v. griffin (archived, https://ahdictionary.com/word/search.html?q=griffin): '…
CON: SKT=supports: SKT.txt \f-leaf 208 = Skeat p. 188, s.v. Griffin, Griffon: '(F.—L.—Gk.) Better griffon. M.… ; FSD=supports: FSD_vol2.txt \f-leaf 365, s.v. griffin: '[< F. griffon, < LL. gryphon-, < gryphus, < L. gr… ; WEB=supports: WEB_vol1.txt \f-leaf 841, s.v. griffin/griffon: '[... L. gryps; ... Gr. grypos, ... hooked…
================================================================================
ENTRY 1 | root: B.r.q | verdict: confirmed | modern: Proto-Semitic *baraḳ- 'lightning', root b-r-q 'to flash, shine' (AHD Semitic roots brq)
NOTE: Root, label and gloss are correct: Wiktionary reconstructs Proto-Semitic *baraḳ- 'lightning' (Akk. birqum, Heb. bārāq, Aram. barqā, Ar. barq, Ge'ez bärḳ), from Proto-Afroasiatic *bǐrk'-/*bǎrk'- 'to flash'; AHD Semitic appendix brq 'to flash (especially of lightning)' with emerald as its English derivative. The emerald branch (Semitic barraqtu/bāreqet → Greek smaragdos → Latin → Romance/English; Greek → Iranian/Arabic zumurrud) is standard (AHD, etymonline, Beekes, Noonan 2012). Two problems in this chart: the Greek form is misprinted/misread ('smaraldos' for smaragdos), and the Arabic → Persian direction for zumurrud is reversed relative to Wiktionary/MacKenzie (Middle Persian uzumburd is pre-Islamic).
ROOTREF: KLN:514=supports
------------------------------------------------------------
# 1 Arabic | b.r.q | verdict: confirmed | 
DER: Arabic root b-r-q: baraqa 'to flash (of lightning), shine, glitter', noun barq 'lightning' (Qur'an 2:19–20 yakādu l-barqu yakhṭafu abṣārahum); Wiktionary: from Proto-Semitic *baraḳ-, noting the Arabic noun may be a deverbal formation rather than a direct inheritance. Derivatives barrāq 'glittering' (intensive faʿʿāl), bāriqa 'flash' (active participle).
REF: KLN:514=supports: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: AKD=partial: AKD.txt \f-leaf 69 (Zimmern p. 59-60; grep -n 'barraqtu' AKD.txt): '[akk. barraqtu ein Ede… ; TAD=silent: Al-Unaysi's dictionary of foreign words in Arabic has no b-r-q headword (it is native Arab… ; FVQ=silent: Jeffery has no entry for barq: he treats it as native Arabic, not a Qur'anic foreign word.
------------------------------------------------------------
# 2 Persian | barq | verdict: confirmed | 
DER: Persian barq برق is borrowed from Arabic barq 'lightning' (Wiktionary: 'Persian borrowed the term directly from Arabic'); attested in Ferdowsi's Shahnameh (c. 1000 CE) in the sense 'lightning', as the chart's quotation shows. The sense 'electricity' is a 19th–20th-c. semantic extension in Persian (cf. barqī 'electric', barq-kār 'electrician'), paralleled by Arabic barq 'telegraph'. The extras barrāq برّاق 'glittering' and bāriqa بارقه 'flash, gleam' are further Arabic derivatives of the root borrowed into Persian.
REF: FVA:45=not_checked: FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json). ; SOR:35=not_checked: SOR (K. Akhavan Zanjani) unidentified/not online (refs_online.json).
CON: MON=supports: 'برق: [ع.] (اِ.) درخش، درخشندگی، درخشش. جلای فلز. (فز.) جرقه‌ای که در اثر نزدیک شدن الکتری… ; HRN=silent: Horn's Grundriss has no barq: Arabic loans are outside his scope, so its absence corrobora… ; HUB=silent: Hübschmann's Persische Studien has no entry for barq. ; ARY=silent: Aryanpur's Indo-European root dictionary gives برق no headword — consistent with a Semitic…
------------------------------------------------------------
# 3 Akkadian | baraqtu | verdict: plausible | 
DER: The Akkadian word for 'lightning' is birqu (Proto-Semitic *baraḳ-, Wiktionary lists Akkadian birqum); the form Nourai prints, baraqtu, corresponds to Neo-Babylonian barraqtu 'emerald, a flashing green stone' (AHD: 'akin to Akkadian barraqtu and Hebrew bāreqet, a kind of gemstone (probably emerald)'), a -t- derivative of barāqu 'to flash'. So the word is real and belongs to this root (KLN:514 s.v. emerald cites it), but the gloss 'lightning' is a conflation: barraqtu is the gem-name, and it is precisely the form from which Greek smaragdos is derived, so it ought to sit as the parent of the Greek node rather than as a sister.
REF: KLN:514=partial: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: AKD=partial: AKD.txt \f-leaf 69 (Zimmern p. 59-60; grep -n 'barraqtu' AKD.txt): '[akk. barraqtu ein Ede… ; LKT=silent: Lokotsch has no Akkadian gem-name entry; he starts the emerald family at Persian zumurrud … ; AFA=silent: Fraenkel does not treat the Akkadian gem-name.
------------------------------------------------------------
# 4 Greek | smaraldos | verdict: transcription_suspect | error_in=book book_prints=smaraldos : a shiny stone, emerald correct_form=smaragdos
DER: The Greek word is σμάραγδος smáragdos (also μάραγδος máragdos), 'emerald, green gem' (Herodotus, Theophrastus; Marcus Aurelius); 'smaraldos' with -ld- is not a Greek form and is almost certainly a misreading of the -gd- cluster (gd → ld) in the scan, since Klein (KLN:514) prints smaragdos. Etymology as drawn is confirmed: Wiktionary, AHD, etymonline and Beekes derive smaragdos from a Semitic source, Akkadian barraqtu / Hebrew bāreqet (Ex. 28:17) 'flashing gem', root b-r-q; the initial s- and the -agd- are the Greek adaptation of the Semitic b-r-q-t cluster (Noonan 2012 on Northwest Semitic loanwords). Old Armenian zmruxt also stems from it. Checked against the scan (data/verification/sources/refs/ocr/BOOK/101.png): the Greek box is printed 'smaraldos' with a plain l (no descender), while the Latin box two rows below correctly prints 'smaragdus', so this is Nourai's own misprint for smaragdos, faithfully transcribed.
REF: KLN:514=supports: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: AKD=partial: AKD.txt \f-leaf 69 (Zimmern p. 59-60; grep -n 'barraqtu' AKD.txt): '[akk. barraqtu ein Ede… ; SKT=supports: SKT.txt \f-leaf 156 = Skeat p. 136, s.v. Emerald: '(F.—L.—Gk.) M.E. emeraude — O.F. esmera… ; WEB=supports: WEB_vol1.txt \f-leaf 625, s.v. emerald: '[ME. emeraude; OFr. esmeraude, esmeralde; L. smar… ; LKT=contradicts: LKT.txt \f-leaf 206 (printed p. ~174/180), no. 2233: 'Pers. zumurrud: "Smaragd" [vielleich…
------------------------------------------------------------
# 5 Arabic |  | verdict: plausible | 
DER: Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ < Greek), i.e. Persian is the intermediary into Arabic rather than the reverse; another route often cited is Syriac zmaragdā. Arabic zabarjad 'peridot' is a doublet. The chart's Greek → Arabic → Persian ordering reverses the direction Wiktionary/MacKenzie give, so the Arabic node's parent is right in substance (Greek origin) but its child edge is not.
REF: MON:1746=supports: vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ…
CON: PLA=contradicts: PLA_pages.txt \f-leaf 162 = Asbaghi printed p. 147 (running head 'zambaq 147 zanādiqa'), s… ; LKT=contradicts: LKT.txt \f-leaf 206 (printed p. ~174/180), no. 2233: 'Pers. zumurrud: "Smaragd" [vielleich… ; TAD=partial: 'زبرجد — في الفارسية «زبرجد» وهو حجر ثمين يشبه الزمرد' — al-Unaysi has no زمرد headword, b… ; AFM=silent: No recoverable headword in the Addi Shir page OCR (the ز section OCRs poorly).
------------------------------------------------------------
# 6 Persian | zomorrod | verdict: disputed | 
DER: Persian zumurrud/zomorrod زمرّد 'emerald' is, per Wiktionary, inherited from Middle Persian uzumburd (Book Pahlavi ʾwzmbwlt), itself borrowed from Greek σμάραγδος in the Sasanian period; the prothetic u-/i- (cf. Early New Persian uzmurud, Russian izumrud, Turkish zümrüt) reflects the un-Persian initial cluster sm- (s- > z- by voicing before m, -gd- > -rd/-rrd). Arabic zumurrud is then a loan FROM Persian (Wiktionary), not its source; etymonline likewise gives Persian zumurrud as the source of Turkish and Russian without an Arabic step. Modern sources therefore reverse the chart's Arabic → Persian edge; the ultimate origin (Semitic b-r-q via Greek), which KLN:514 also gives, is not in doubt.
REF: MON:1746=supports: vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ… ; KLN:514=partial: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: PLA=contradicts: PLA_pages.txt \f-leaf 162 = Asbaghi printed p. 147 (running head 'zambaq 147 zanādiqa'), s… ; LKT=contradicts: LKT.txt \f-leaf 206 (printed p. ~174/180), no. 2233: 'Pers. zumurrud: "Smaragd" [vielleich… ; HRN=silent: Horn has no zumurrud article; his only 'Smaragd' is the unrelated Np. mīnā (no. 1011), so … ; ARY=silent: Aryanpur gives no Indo-European root for زمرد — consistent with a Wanderwort, not with an …
------------------------------------------------------------
# 7 Latin | smaragdus | verdict: confirmed | 
DER: Latin smaragdus (m./f.), Pliny, Vulgate — a direct borrowing of Greek σμάραγδος with Greek -os rendered by the Latin 2nd-declension -us. In Vulgar/Medieval Latin it became smaralda, smaraldus, esmaraldus (with -gd- > -ld- by dissimilation and a prothetic e- before the s+consonant cluster), the source of all Romance forms.
REF: KLN:514=supports: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: LAT=supports: LAT.txt \f-leaf 1130 (Ernout-Meillet, s.v. smaragdus): 'smaragdus (zma-), -ī m.: émeraude.… ; SKT=supports: SKT.txt \f-leaf 156 = Skeat p. 136, s.v. Emerald: '(F.—L.—Gk.) M.E. emeraude — O.F. esmera… ; LEW=silent: Walde (1910) has no smaragdus article; like gryphus it is left out as a transparent Greek …
------------------------------------------------------------
# 8 English | smaragdite | verdict: confirmed | 
DER: smaragdite 'a green foliated amphibole found in eclogite/gabbro' is a learned mineralogical coinage (French smaragdite, H.-B. de Saussure, 1796) from Latin smaragdus + the mineral suffix -ite (< Greek -ītēs), named for its emerald-green colour; English from French in the early 19th c. The Latin → English edge is via scientific French, with no Old French step.
REF: AHD:427=partial: AHD:427 is the 1976 page of 'emerald'; the current AHD emerald entry (archived, https://ah…
CON: FSD=supports: vol. 4: 'smaragdine … Of the color of the smaragd; emerald-colored, green. [< L. smaragdin… ; SKT=silent: Skeat's concise dictionary has smaragdus but no mineralogical smaragdite. ; WEB=silent: S is not in the available Webster volume, so Webster could not be consulted for this headw…
------------------------------------------------------------
# 9 Old French | esmeralde | verdict: confirmed | 
DER: Old French esmeraude (12th c.), with the variants esmeralde, esmeragde, smaralde listed by Wiktionary, from Vulgar Latin *smaralda/*smaraldus (< Latin smaragdus): prothetic e- before s+C, -gd- > -ld- > -ud- (vocalisation of l before a consonant gives the standard esmeraude), so esmeralde is the conservative form; Modern French émeraude.
REF: KLN:514=supports: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera…
CON: WEB=supports: WEB_vol1.txt \f-leaf 625, s.v. emerald: '[ME. emeraude; OFr. esmeraude, esmeralde; L. smar… ; SKT=supports: SKT.txt \f-leaf 156 = Skeat p. 136, s.v. Emerald: '(F.—L.—Gk.) M.E. emeraude — O.F. esmera… ; LKT=silent: Lokotsch follows only the Persian → Turkish → Slavic line and says nothing about the Roman…
------------------------------------------------------------
# 10 English | emerald | verdict: confirmed | 
DER: Middle English emeraude (c. 1300) from Old French esmeraude; the modern spelling emerald with -ld restored (after Medieval Latin esmaraldus / Old French esmeralde) appears from the 15th–16th c. AHD: 'Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos'.
REF: AHD:427=supports: AHD online s.v. emerald (archived, https://ahdictionary.com/word/search.html?q=emerald): '…
CON: SKT=supports: SKT.txt \f-leaf 156 = Skeat p. 136, s.v. Emerald: '(F.—L.—Gk.) M.E. emeraude — O.F. esmera… ; WEB=supports: WEB_vol1.txt \f-leaf 625, s.v. emerald: '[ME. emeraude; OFr. esmeraude, esmeralde; L. smar… ; LKT=silent: Lokotsch does not treat English emerald (it reaches English through Romance, not through h…
------------------------------------------------------------
# 11 Sanskrit | marakata | verdict: plausible | 
DER: Sanskrit marakata (n.) 'emerald' (Pali marakata, Prakrit maragaya; hence Tamil marakatam, Thai morakot, Tibetan mar gad) is a genuine word and, as the chart implies, ultimately of Semitic origin; Wiktionary labels it 'from Semitic', linking it with Greek σμάραγδος. But the immediate source is debated: Noonan and the classicists (Chantraine, Beekes, Mayrhofer) treat marakata as a late loan from Greek smaragdos (loss of initial s-, -gd- > -k-t-), i.e. Greek rather than the Semitic root directly; older scholarship (still echoed in some sources) even took Sanskrit as the source of the Semitic words, which is now rejected. So 'from the Semitic root' is right in ultimate origin but the direct edge Semitic → Sanskrit is uncertain.
REF: KLN:514=supports: KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmera… ; SKT:163=partial: SKT.txt leaf 156 (Skeat 1911 p. ~136; Nourai's 163 is another printing), s.v. Emerald: '(F…
CON: AKD=partial: AKD.txt \f-leaf 69 (Zimmern p. 59-60; grep -n 'barraqtu' AKD.txt): '[akk. barraqtu ein Ede… ; LKT=partial: LKT.txt \f-leaf 206 (printed p. ~174/180), no. 2233: 'Pers. zumurrud: "Smaragd" [vielleich… ; HJB=silent: Hobson-Jobson has no marakata article; 'emerald' occurs only inside quotations (e.g. Garci… ; SYN=silent: Buck's Selected Synonyms has no gem-name chapter covering 'emerald'. ; IEC=silent: Mann's Indo-European Comparative Dictionary has no entry — as expected, since neither he n…
```


## [2026-09-04T23:25:06.886Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p101.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشه اصیل است و برچسب «سامی» درست: ویکی‌واژه سامیِ آغازین *birk- «زانو» را بازسازی می‌کند (اکدی birkum، عبری berekh، سریانی burkā، گعزی bərk) با گونهٔ مقلوبِ *rukbat- که «رکبة» عربی از آن است. داستان «زانو زدنِ شتر ← برکت دادن» همان تبیین سنتیِ گزنیوس است و با «بَرَکَ/بارَکَ» عربی می‌خواند. اما پیوستِ سامیِ فرهنگ American Heritage — که خودِ نورایی بدان استناد می‌کند — b-r-k «برکت دادن» را «احتمالاً گونهٔ مقلوبِ k-r-b» می‌داند (اکدی karābu «ستودن، برکت دادن»)، و همین فرضِ قلب است که شاخهٔ اکدی-عبریِ «کروب» بر آن استوار شده؛ کلاین آن را می‌پذیرد اما فرهنگ‌نویسیِ امروزیِ عبری (پایگاه SAHD به نقل از میچل) ردش می‌کند، چون قلبِ همخوان نخست و سوم بسیار نادر است. شاخهٔ «گریفین» نیز حدسی است (از کلاین) و خودِ AHD در مدخل griffin آن را نپذیرفته است.\",\n\"1\": \"ریشه و برچسب و معنا هر سه درست است: ویکی‌واژه سامیِ آغازین *baraḳ- «آذرخش» را بازسازی می‌کند (اکدی birqum، عبری bārāq، آرامی barqā، عربی برق، گعزی bärḳ) از آفروآسیاییِ آغازینِ *bǐrk'- «درخشیدن»، و پیوست سامیِ AHD نیز b-r-q را «درخشیدن، به‌ویژه آذرخش» می‌آورد و emerald را برون‌دادِ انگلیسیِ آن می‌شمارد. شاخهٔ زمرد (سامی barraqtu/bāreqet ← یونانی smaragdos ← لاتینی ← زبان‌های رومی و انگلیسی؛ و از یونانی به ایرانی و عربی به صورت زمرّد) همان مسیر پذیرفتهٔ AHD و بیکس و نونان است. دو اشکال در این نمودار هست: صورت یونانی به غلط «smaraldos» چاپ شده به جای smaragdos، و جهتِ «عربی ← فارسی» برای «زمرّد» وارونه است، چون فارسیِ میانه uzumburd پیش از اسلام گواه دارد.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"ریشهٔ عربیِ ب-ر-ک: «بَرَکَ» یعنی «زانو زدنِ شتر» (مصدر بُروک)، بابِ سومِ «بارَکَ» «برکت دادن»، بابِ دومِ «برَّکَ» و بابِ ششمِ «تبارَکَ»؛ و اسمِ «بَرَکَة» «برکت، عنایت الهی» که مصدرگونه‌ای از همین ریشه با تاء مربوطه است — و همین -ة است که در آوانگاریِ «barakat» به صورت -ت آمده است. هم‌ریشهٔ عبریِ آن bērēkh «برکت دادن» و bərākhā «برکت» است. کلاین و جفری هر دو همین را می‌گویند و ادعای نورایی در این گره درست است.\",\n\"2\": \"«برکت» فارسی وام‌واژه‌ای سرراست از «بَرَکَة» عربی است که در آن تاء مربوطهٔ عربی به صورت -ت فارسی مانده است، همان رفتاری که با «رحمت» و «نعمت» شده است؛ اردو نیز barkat را از فارسی کلاسیک گرفته است. دیگر صورت‌های جعبه نیز همه مشتقات عربیِ همین ریشه‌اند که آماده به فارسی وام داده شده‌اند: «تبریک» (مصدر باب دوم)، «تبرّک» (مصدر باب پنجم) و «مبارک» (اسم مفعول باب سوم). معین نیز «برکت» را با نشانِ «[ع. برکة]» می‌آورد؛ ادعای نورایی درست است.\",\n\"3\": \"اکدی karābu «دعا کردن، برکت دادن، ستودن» (اسم فاعلِ kāribu «شفیع، برکت‌دهنده» و مصغّرِ kurību که نامِ فرشتهٔ نگهبان است) واژه‌ای راستین از ریشهٔ ک-ر-ب است. پیوند آن با ب-ر-ک بر فرضِ قلب استوار است (دورم؛ کلاین ص ۱۶۴؛ پیوست سامیِ AHD: «k-r-b ... با گونهٔ مقلوبِ سامیِ غربیِ b-r-k»)، پس منابعی که نورایی نام می‌برد به‌راستی همین را می‌گویند و AHD هنوز بر آن است؛ اما پایگاه معناشناسیِ عبری باستان (میچل) آن را رد می‌کند، چون قلبِ همخوان نخست و سوم بسیار کمیاب است، و صفحهٔ *birk- در ویکی‌واژه هیچ اکدی karābu نیاورده است. پس حکم «با احتیاط پذیرفتنی» است: گروهی می‌پذیرند و گروهی رد می‌کنند.\",\n\"4\": \"بخش نخست جعبه بی‌اشکال است: bərākhā «برکت» با فعل bērēkh و اسمِ berekh «زانو» عضو آشکار همین ریشه و هم‌ریشهٔ «بَرَکَة» عربی است. اما kərūḇ «کروب» (جمع kərūḇīm؛ پیدایش ۳:۲۴، خروج ۲۵:۱۸) بنا بر رأی رایج وام‌واژه‌ای است از اکدی kāribu/kurību «شفیع؛ فرشتهٔ بالدارِ نگهبان» از ریشهٔ ک-ر-ب، پس جای آن کنار گرهٔ ۳ است و نهادنش زیر ب-ر-ک یکسره به همان فرضِ قلبِ k-r-b/b-r-k وابسته است که کلاین و AHD می‌پذیرند و SAHD رد می‌کند. رأی جایگزینِ رابرت آلتر (واژه‌ای دورگه، یا با وارونگیِ همخوان‌ها از r-k-b «مرکب») نیز مطرح است. از این رو بدترین حکمِ ممکن برای این گره «با احتیاط پذیرفتنی» است.\",\n\"5\": \"عربی «کَروبیّ» به معنی «کروبی، فرشتهٔ مقرّب» (جمع: الملائکة الکروبیّون) بنا بر ویکی‌واژه از عبری kərūḇ گرفته شده است، در عمل از راه آرامیِ یهودی/سریانیِ kərūḇā که ناقلِ بیشترِ واژگان کتاب مقدس به عربی است، با افزودنِ یاء نسبتِ عربی که آن را صفت/اسم نسبی می‌کند. این واژه در سنت اسلامیِ آغازین (حدیث و تفسیر) برای برترین فرشتگان به کار رفته است و مستقیماً از اکدی نیامده است؛ ادعای نورایی درست است.\",\n\"6\": \"«کرّوبی» فارسی همان «کروبیّ» عربی است که بی‌دگرگونی گرفته شده و نویسندگان فارسی غالباً راء آن را مشدد می‌نویسند، چنان‌که ضبط نورایی نشان می‌دهد؛ جمعِ آن هم به فارسی «کروبیان» می‌آید و هم به عربی «کروبیون». در شعر کلاسیک، از جمله در بوستان سعدی که در نمودار شاهد آورده شده، گواه دارد. معنایی که نورایی می‌دهد («فرشته») مسامحه‌آمیز است: واژه به‌خصوص «کروب، از فرشتگان مقرّب» است. وام‌گیریِ آن از عربی جای بحث ندارد و معین نیز آن را با نشانِ «[ع.]» می‌آورد.\",\n\"7\": \"عبری kərūḇ در ترجمهٔ سبعینیه (سده‌های سوم تا دوم پیش از میلاد) به صورت χερούβ (جمع χερουβίμ) آوانگاری شد، از آنجا به لاتینیِ متأخر و ولگات به صورت cherub/cherubim رسید و در اواخر سدهٔ چهاردهم به انگلیسی میانه راه یافت. معنای «کودکِ بالدار» که نورایی با «(of love)» بدان اشاره می‌کند کاربردی هنری از دورهٔ رنسانس است و در انگلیسی از حدود ۱۷۰۵ دیده می‌شود. نمودار به‌درستی آن را از عبری می‌گیرد نه از راه عربی؛ ادعای نورایی درست است.\",\n\"8\": \"یونانی γρύψ (اضافیِ γρυπός) «گریفین» نزد هرودوت و آیسخولوس آمده است؛ صورت دومی که نورایی می‌آورد، «gruphos»، صورت فاعلیِ یونانی نیست بلکه بازتاب اضافیِ grypos یا لاتینیِ gryphus است. خاستگاه آن قطعی نیست: رأیی آن را به γρυπός «کج‌بینی، خمیده» می‌بندد (از ریشهٔ *ger- «خمیدن»)، و کلاین (همان منبعی که نورایی ارجاع می‌دهد) و بیکس وام‌واژه‌ای پیش‌یونانی/آناتولیایی با خاستگاه نهاییِ سامی (اکدی karūbu، عبری kərūḇ) «از راه هیتی‌ها» را روا می‌دانند، که در این صورت دوگانهٔ χερούβ خواهد بود. اما خودِ AHD در مدخل griffin هیچ خاستگاه سامی نمی‌آورد و SAHD می‌نویسد که پیوندِ kərūḇ و γρύψ «پذیرش علمیِ بسیار اندکی یافته است». پس این پیکان فرضیه‌ای آبرومند اما اقلیتی است.\",\n\"9\": \"لاتینی grȳps, grȳpis (ویرژیل، پلینیوس) وام‌واژه‌ای مستقیم از یونانی γρύψ است؛ در لاتینیِ متأخر گونه‌های ستاک‌دارِ grȳpus و grȳphus ساخته شد که -ph- در آن املایی فاضل‌نمایانه و در واقع نادرست است، و همین صورتِ متأخرِ gryphus/grifus است که زبان‌های رومی آن را ادامه داده‌اند. ارنو-مه‌یه و اسکیت نیز همین را می‌گویند؛ ادعای نورایی درست است.\",\n\"10\": \"فرانسوی کهن grifon/griffon (سدهٔ دوازدهم؛ انگلوـنورمن grifun) همان gryphus لاتینیِ متأخر است با پسوند بزرگ‌داشتیِ -on (< لاتینی -ōnem)، یعنی از *grifonem؛ حلقهٔ لاتینی ← فرانسوی کهن ← انگلیسی قطعی است. اما ضبطِ «grifion» که در کتاب چاپ شده صورت گواهی‌شدهٔ فرانسوی کهن نیست (انتظار grifon/griffon می‌رود) و می‌تواند لغزش نورایی یا خطای خوانشِ اسکن باشد؛ چون صفحهٔ کلاین بازبینی نشده، حکم به جای «مشکوک به خطای خوانش» در حد «با احتیاط پذیرفتنی» نگاه داشته شده است.\",\n\"11\": \"انگلیسی میانه griffoun/griffon (حدود ۱۲۰۰ به عنوان نام خانوادگی و در سدهٔ چهاردهم برای آن جانور) از فرانسوی کهن grifon گرفته شده و املای امروزیِ griffin و gryphon در سده‌های شانزدهم و هفدهم تثبیت شده است (gryphon دوباره به قیاس gryphus لاتینی نوشته شده). مصداق آن همان موجودِ عقاب‌سر و شیرتنی است که در افسانه‌های یونانی نگهبان زرِ سکاهاست. اسکیت، وبستر و AHD همه همین زنجیره را می‌آورند؛ ادعای نورایی درست است.\"\n},\n\"1\": {\n\"1\": \"ریشهٔ عربیِ ب-ر-ق: «بَرَقَ» «درخشیدن، برق زدن» و اسمِ «برق» «آذرخش» که در قرآن نیز آمده است (بقره ۱۹–۲۰: «یکادُ البرقُ یخطفُ أبصارَهم»)؛ ویکی‌واژه آن را از سامیِ آغازینِ *baraḳ- می‌گیرد و می‌افزاید که اسمِ عربی شاید از فعل ساخته شده باشد نه میراثِ مستقیم. مشتقاتِ «برّاق» (بر وزن فعّال، برای مبالغه) و «بارقة» (اسم فاعل) نیز از همین ریشه‌اند. ادعای نورایی در این گره درست است.\",\n\"2\": \"«برق» فارسی وام‌واژه‌ای مستقیم از «برق» عربی به معنی «آذرخش» است و در شاهنامهٔ فردوسی (حدود سال ۴۰۰ هجری) در همین معنا گواه دارد، چنان‌که شاهدِ نمودار نشان می‌دهد. معنای «الکتریسیته» گسترشِ معناییِ سدهٔ سیزدهم و چهاردهم خورشیدی در فارسی است (برقی، برق‌کار)، همچنان‌که «برق» در عربی معنیِ «تلگراف» یافت. «برّاق» و «بارقه» در شاهدها نیز مشتقات عربیِ همین ریشه‌اند که به فارسی وام داده شده‌اند؛ ادعای نورایی درست است.\",\n\"3\": \"واژهٔ اکدی برای «آذرخش» birqu است (ویکی‌واژه birqum را ذیل *baraḳ- می‌آورد)، حال آنکه صورتی که نورایی چاپ کرده، baraqtu، در واقع همان barraqtuی بابلیِ نو است به معنی «زمرد، سنگِ سبزِ درخشان» — مشتقی با -t- از فعل barāqu «درخشیدن». پس واژه راستین است و به همین ریشه تعلق دارد (کلاین ص ۵۱۴ ذیل emerald آن را می‌آورد)، اما معنایی که نورایی می‌دهد («آذرخش») دو مفهوم را درهم آمیخته است: barraqtu نامِ گوهر است و درست همان صورتی است که σμάραγδος یونانی از آن گرفته شده، پس می‌بایست پدرِ گرهٔ یونانی می‌بود نه خواهرِ آن؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"4\": \"واژهٔ یونانی σμάραγδος (و گونهٔ μάραγδος) «زمرد» است (هرودوت، تئوفراستوس) و صورتِ «smaraldos» با -ld- در یونانی وجود ندارد. ریشه‌یابیِ ترسیم‌شده درست است: ویکی‌واژه، AHD، اتیمآنلاین و بیکس همگی σμάραγδος را از خاستگاهی سامی می‌گیرند، یعنی اکدی barraqtu / عبری bāreqet «گوهرِ درخشان» از ریشهٔ ب-ر-ق، و س آغازین و خوشهٔ -agd- سازگارسازیِ یونانیِ خوشهٔ سامیِ b-r-q-t است. اما بررسی تصویر صفحه نشان می‌دهد که خودِ کتاب «smaraldos» با لامِ آشکار چاپ کرده، حال آنکه دو ردیف پایین‌تر جعبهٔ لاتینی به‌درستی «smaragdus» دارد؛ پس این خطای چاپیِ خودِ نورایی است و استخراجِ داده وفادارانه بوده است. صورت درست smaragdos است.\",\n\"5\": \"این جعبهٔ گذرا برای عربی است: «زُمُرُّد» عربی به‌راستی به σμάραγδος یونانی بازمی‌گردد، اما نه بی‌واسطه — ویکی‌واژه آن را از «زمرّد» فارسی می‌گیرد که خود از فارسی میانهٔ ʾwzmbwlt /uzumburd/ و آن از یونانی است؛ یعنی فارسی واسطهٔ ورود به عربی است نه برعکس. مسیر دیگری که گاه یاد می‌شود سریانیِ zmaragdā است، و «زبرجد» عربی دوگانهٔ همین واژه است. پس پدرِ این گره (خاستگاه یونانی) درست است اما پیکانِ فرزندِ آن (عربی ← فارسی) نادرست است؛ اصباغی و لوکوچ نیز جهت را وارونهٔ نمودار می‌دانند.\",\n\"6\": \"«زمرّد» فارسی بنا بر ویکی‌واژه میراثِ فارسی میانهٔ uzumburd (پهلوی کتابی ʾwzmbwlt) است که در دورهٔ ساسانی از یونانیِ σμάραγδος وام گرفته شده بود؛ الفِ پیشین در uzmurud (و در izumrud روسی و zümrüt ترکی) واکنش به خوشهٔ آغازینِ sm- است که در فارسی روا نیست، و s- پیش از m واک گرفته و z شده و خوشهٔ -gd- به -rd/-rrd بدل شده است. «زمرّد» عربی خود وامی از فارسی است نه سرچشمهٔ آن؛ اتیمآنلاین نیز فارسی را منبع صورت‌های ترکی و روسی می‌داند بی‌آنکه واسطه‌ای عربی بیاورد. پس منابع امروزی پیکانِ «عربی ← فارسی» این نمودار را وارونه می‌کنند و آن را رد می‌شمارند؛ خاستگاه نهایی (سامیِ ب-ر-ق از راه یونانی) البته محل تردید نیست.\",\n\"7\": \"لاتینی smaragdus (نزد پلینیوس و در ولگات) وامی مستقیم از یونانی σμάراγδος است که -os یونانی در آن به -us صرفِ دومِ لاتینی بدل شده است. در لاتینیِ عامیانه و لاتینیِ سده‌های میانه به smaralda/smaraldus و esmaraldus بدل شد، با ناهمگونیِ -gd- > -ld- و افزودن الفِ پیشین پیش از خوشهٔ s+همخوان، و همین صورت‌ها سرچشمهٔ همهٔ برون‌دادهای رومی‌اند. ادعای نورایی درست است.\",\n\"8\": \"smaragdite نامِ کانی‌شناختیِ آمفیبولی سبز و ورقه‌ورقه است که در ۱۷۹۶ سوسور در فرانسه ساخت (smaragdite)، از لاتینی smaragdus به‌علاوهٔ پسوند کانی‌شناسیِ -ite (< یونانی -ītēs)، به مناسبت رنگ زمردیِ آن؛ انگلیسی آن را در آغاز سدهٔ نوزدهم از فرانسه گرفت. پس پیوندِ لاتینی به انگلیسی از راه فرانسویِ علمی است و حلقهٔ فرانسویِ کهن در کار نیست. ادعای نورایی درست است.\",\n\"9\": \"فرانسوی کهن esmeraude (سدهٔ دوازدهم) با گونه‌های esmeralde و esmeragde، از لاتینیِ عامیانهٔ *smaralda (< smaragdus): الفِ پیشین پیش از خوشهٔ s+همخوان افزوده شده، -gd- به -ld- بدل شده و سپس l پیش از همخوان واکه‌گون شده و -ud- داده که صورت معیارِ esmeraude را می‌سازد؛ پس esmeralde صورتِ محافظه‌کارتر است. فرانسوی امروز émeraude دارد. ادعای نورایی درست است.\",\n\"10\": \"انگلیسی میانه emeraude (حدود ۱۳۰۰) از فرانسوی کهن esmeraude گرفته شده و املای امروزیِ emerald با بازگشتِ -ld (به قیاس لاتینیِ میانهٔ esmeraldus و فرانسوی کهن esmeralde) از سده‌های پانزدهم و شانزدهم دیده می‌شود. AHD زنجیره را چنین می‌آورد: انگلیسی میانه از فرانسوی کهن، از لاتینیِ میانه esmeralda، از لاتینی smaragdus، از یونانی smaragdos. ادعای نورایی درست است.\",\n\"11\": \"سنسکریت marakata «زمرد» (پالی marakata، پراکریت maragaya؛ و از آنجا تامیلی marakatam، تایلندی morakot و تبتی mar gad) واژه‌ای راستین است و چنان‌که نمودار می‌رساند خاستگاه نهاییِ آن سامی است؛ ویکی‌واژه نیز برچسب «از سامی» می‌زند. اما سرچشمهٔ بی‌واسطه محل بحث است: نونان و کلاسیک‌شناسان (شانترن، بیکس، مایرهوفر) marakata را وامی متأخر از σμάραγδος یونانی می‌دانند (با افتادن s- آغازین و بدل شدن -gd- به -k-t-)، نه وامی مستقیم از ریشهٔ سامی؛ و رأیِ کهنِ برخی که سنسکریت را سرچشمهٔ واژه‌های سامی می‌گرفت اکنون مردود است. پس «از ریشهٔ سامی» در خاستگاه نهایی درست است اما پیکانِ مستقیمِ سامی ← سنسکریت قطعی نیست.\"\n}\n}\n}\nEOF\npython3 apply_fa.py 101 p101.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-101.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-101.json",
 "description": "Apply Persian to page 101"
}
```


### [2026-09-04T23:25:09.316Z] TOOL RESULT

```
ok 101
JSON_OK
 data/verification/page-101.json | 24 ++++++++++++++++++++++++
 1 file changed, 24 insertions(+)
```


## [2026-09-04T23:25:13.249Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 126 2>&1 | head -200",
 "description": "Dump page 126"
}
```


### [2026-09-04T23:25:15.500Z] TOOL RESULT

```
##########################################################################################
PAGE 126 book 96
================================================================================
ENTRY 0 | root: Dheigh, Dhigha | verdict: confirmed | modern: PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'
NOTE: Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.
ROOTREF: POK:244=supports ; KNT:191=supports ; CEL3:203=not_checked
------------------------------------------------------------
# 1 Old Persian | didâ, děğa-vâra | verdict: disputed | 
DER: OP didā- f. 'wall, fortress' is genuinely attested: DSf (Darius' Susa foundation charter) line 54 'tyaiy didām apiθa' — 'the men who adorned the wall were Medes and Egyptians' (Kent's Lexicon p. 191, which is Nourai's KNT:191). It is the regular SW-Iranian reflex of PIr *daizah < PIE *dʰóyǵʰos: Proto-Iranian *ǰ (< PIE *ǵʰ) gives Old Persian d where Avestan/Median give z (cf. Av. daēza-), and the reduplicated-looking di-dā- shows the OP treatment (Asatrian 2017, 'SWIran. *didā- fortress, walled residence'). The second word is not an attested OP word but Horn's/Hübschmann's reconstruction of the ancestor of dīvār, i.e. *daiza-vāra- 'wall-enclosure' (HRN:133); the JSON form 'děğa-vâra' with ě and ğ is almost certainly a scan misreading of the book's 'dēza-vâra' or 'daiza-vâra' (Nourai writes ž, not ğ, for the sound elsewhere on this page: dež). Modern reconstruction (Wiktionary, after Asatrian and Rastorgueva-Edelman) is OP didā- + *-wāra-, giving MP dēwār. Checked against the scan (data/verification/sources/refs/ocr/BOOK/126.png): the book prints 'didâ, děğa-vâra' with both breves exactly as the dataset has it, so the guess of a scan misreading of 'dēza-/daiza-vâra' above is wrong — …
REF: HRN:133=supports: HRN.txt leaf 154 (Horn p. 133), No. 599: 'dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. t… ; KNT:191=supports: KNT.txt leaf 214 (Kent p. 191): 'didā- sb. wall, stronghold, fortress: NPers. diz, pIE *dh… ; IEC:191=partial: IEC.txt leaf 112 (Mann cols ~193-194), s.v. dheigh-: 'shape, earth up; form, wall ... Cf. …
CON: BRT=supports: BRT.txt col. 747: 'p. dida- f. "befestigter Ort, Festung; Burg" ... Bh. 2.8 ... — Zum V. d… ; TLM=supports: TLM.txt: 'dida, f. stronghold. Nom. sg. dida. Acc. sg. didam. New Pers. diz; cf. YAv. diz,… ; NYB=partial: NYB_vol2_glossary.txt leaf 75: 'divar [dywʾl] a wall 39*. — NP divar. V. Hübschmann, PSt 6… ; LAT=supports: Ernout-Meillet cite 'le vieux perse didā "mur, enceinte"' as a direct nominal derivative o… ; ARY=partial: ARY_pages.txt pdf p.296 (printed 297; also read from the page image, saved as ocr/ARY/0297…
------------------------------------------------------------
# 2 Persian | dîvâr | verdict: confirmed | 
DER: OP didā- 'wall' + *-wāra- (PIr *wāra- 'cover, enclosure' < PIE *wer- 'cover, guard' — Nourai's cross-reference ☞Wer 3 is right) > Middle Persian dywʾl /dēwār/ 'wall' (MacKenzie 1971) > New Persian dīvār/divār 'wall', with regular MP ē > NP ī and intervocalic w > v. The compound is an old SW-Iranian formation, since it shows the OP -d- reflex, not the Median/Avestan -z-. Borrowed onward into Turkish duvar, Hindi/Urdu dīvār.
REF: BQT:918=partial: RE-CHECKED. BQT_v2_pages.txt leaf 378 = printed p. 918 (leaf 379 carries the header 'دیو د…
CON: PHD=supports: PHD.txt: 'dēwār [dywʾl | M dywʾr, N ~] wall.' MacKenzie has the Middle Persian ancestor dē… ; NYB=supports: NYB_vol2_glossary.txt leaf 75: 'divar [dywʾl] a wall 39*. — NP divar. V. Hübschmann, PSt 6… ; ARY=supports: ARY_pages.txt pdf p.296 / ocr/ARY/0297.vision.txt: 'دیوار DIVĀR = WALL; INDO-EUROPEAN *DHE… ; MON=partial: 'دیوار [ په . ] (اِ.) ۱- جداری از سنگ، چوب، آجر و غیره که اطراف خانه، زمین و باغ و غیره به…
------------------------------------------------------------
# 3 Sogdian | dyz` | verdict: plausible | 
DER: Sogdian δyz / δyzʾ (Gharib's Sogdian Dictionary; Nourai's SOD:151) 'fortress, castle' is real and is listed by Wiktionary among the reflexes of PIE *dʰóyǵʰos beside Av. daēza-, OP didā- and Persian dez/dež. But it is a North-Eastern Iranian cognate, PIr *daizah with the regular Sogdian outcomes *d- > δ- and *ǰ > z; it does not descend from Old Persian didā- (which has -d-), as the chart's arrow implies. The word is correct, the edge should run from the Proto-Iranian/Avestan-type *daiza- rather than from OP.
REF: SOD:151=supports: SOD_pages.txt leaf 216 (Gharib p. 151), entry 3825: 'δyz' M — δiza (dyz') < OP didā, f. n.…
CON: SOD=supports: SOD_pages.txt leaf 351: '7102 prδys- M parδes < *pari-daisa- (to)build'; '7103 prδyz M par… ; NYB=supports: NYB_vol2_glossary.txt: 'dištan to build ... MPrth dyštn, pres. certainly dys- ... Sogd δys…
------------------------------------------------------------
# 4 Avestan | daeza | verdict: confirmed | 
DER: Avestan daēza- 'wall' (Bartholomae AiW; Wiktionary 𐬛𐬀𐬉𐬰𐬀) < PIr *daizah < PIIr *dʰaiȷ́ʰas < PIE *dʰóyǵʰos 'that which is kneaded/moulded' (o-grade of *dʰeyǵʰ-). Exact cognates: Skt. dehī- 'wall, rampart', Gk. teîkhos/toîkhos 'wall', Gmc *daigaz 'dough'. The semantic shift is 'kneaded clay' > 'mud-brick wall'. Pokorny 244 lists it under dhoiĝho-s, so Nourai's POK:244 citation is the standard one.
REF: POK:244=supports: POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern o…
CON: BRT=supports: BRT.txt col. 674-675: 'daez- V. "häufen, schichten" (Erde, Steine) ... mit pairi "rings-, … ; WLD=supports: WLD_Bd1_1930_dli_70244_djvu.txt, Bd. I pp. 833-834 s.v. dheigh-: 'dheigh- "Lehm kneten und… ; IEC=supports: IEC.txt: 'dhoiĝhos ... "shape, mould; shaper". Cf. dheiĝh-. WP I, 833 Skt. dehah ...; dehi… ; SYN=supports: SYN.txt: 'Av. uzdaézi- "wall" ... fr. IE *dheigh- in Skt. dih- "smear", Lat. fingere "mold…
------------------------------------------------------------
# 5 Persian | dež; dež-pol | verdict: confirmed | 
DER: Persian dez/dež 'fort, citadel' continues Middle Persian diz 'fortress' (MacKenzie 1971), itself PIr *daizah < PIE *dʰóyǵʰos — the same word as Av. daēza- and OP didā-. The -z-/-ž- forms are Median/Parthian (North-Western) reflexes of PIr *ǰ, not the Persis form (OP didā- with -d-), so MP diz is an old NW loan into Persian; Wiktionary labels dež 'Iranian (Parthian?)'. dežbān 'castellan', deždār 'fort-keeper' are transparent compounds. Dež-pol/Dezful: Wikipedia and Iranica give the town name as Dež-pul 'fortress-bridge', for the fort guarding Shapur II's Sasanian bridge over the Āb-e Dez; the Arabicised form Dezfūl replaces the un-Arabic ž and p (Nourai's gloss 'strong bridge' is loose — literally 'fort-bridge'). Nourai's arrow from Avestan is the usual shorthand for 'Old Iranian'; the Persian word is a cognate of the Avestan one, not its descendant.
REF: BQT:851=supports: RE-CHECKED. BQT_v2_pages.txt leaf 311 = printed p. 851 (leaf 310 = p. 850 ends 'بقیه در صف… ; MON5:528=not_checked: Mo'in vol. 5 (aʿlām / proper names) is neither on disk nor online (vajehyab/abadis carry o…
CON: HRN=supports: HRN.txt leaf 146: '563. diz, dez "Burg", vergl. dizbān, dizdār (syr. LW.). ap. didā "Festu… ; PHD=supports: PHD.txt: 'diz [KLYTA < A qrytʾ; dc | M dyz, N ~] fortress.' The Middle Persian link diz > … ; NYB=partial: NYB_vol2_glossary.txt leaf 75: 'diz [dcʾ] castle ... MPrthPrs dyz; NP diz. — NW form, as a… ; ARY=supports: ARY_pages.txt pdf p.277 (printed 278): entry دژ with AVESTAN UZDAEZA, -DAEZA; OLD PERSIAN … ; MON=partial: 'دژ (دِ) = (اِ.) دز: حصار، قلعه.' The meaning 'fort, citadel' is confirmed and دژ is equat…
------------------------------------------------------------
# 6 Avestan | pairi-daeza | verdict: confirmed | 
DER: Avestan pairi.daēza- 'enclosure walled all round' = pairi 'around' (PIE *péri; Nourai's ☞Per 1 is right) + daēza- 'wall'; attested in the Vidēvdād (3.18 pairi.daēzą pairi.daēzaiiąn 'they shall build an enclosure around'). PIr *pari-daizah; parallel formations Bactrian prdyjg, Khwarezmian prdyz, Sogdian prδyz, Armenian (loan) partēz, Old Persian paradayadām (A2Sd, late spelling for *paridaida-). Meaning shift 'walled enclosure' > 'walled garden, royal park'.
REF: POK:244=supports: POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern o…
CON: BRT=supports: BRT.txt col. 866: 'j. pairi.daeza- m., Plur. "eine rings-, rundum gehende, sich zusammensc… ; KLN=supports: KLN_1966.txt leaf 600 (printed p. 1124-1125) s.v. paradise: 'ME. paradis, fr. OF. paradis,… ; HUB=supports: HUB.txt leaf 133: 'pālīz "Garten" = hebr. pardēs (Hohelied), arm. partēz, zd. pairidaeza-,… ; LAT=supports: LAT.txt leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo: 'La racine i.-e. dheig'h- ..…
------------------------------------------------------------
# 7 Persian | pâlîz, jâlîz | verdict: plausible | 
DER: pālīz 'orchard, melon/vegetable field' is genuine and belongs here: PIr *paridaizah > Old Median *pariδaiza- / Sogdian prδyz (parδēz 'fruit garden') > Middle Persian *pālēz (with -rδ- > -l-, a NW/Median treatment) > NP pālēz > pālīz, Tajik poliz; Wiktionary calls it a borrowing from Sogdian, older handbooks (Horn, Hübschmann) a Median form — either way not a Persis (OP -d-) form, and a doublet of pardīs and ferdows. jālīz is the doubtful item: Persian dictionaries (Dehkhoda, Moin — Nourai's MON:680) treat it as a variant of pālīz, but English Wiktionary derives it separately from a Middle Iranian *gardīz (i.e. from *gard- 'enclosure', cf. gird), so the j- is not a simple alternation of p-. I found no scholarly citation for either view of jālīz; treat the pālīz link as confirmed and jālīz as uncertain.
REF: BQT:359=partial: RE-CHECKED. BQT_v1_pages.txt leaf 581 = printed p. 359 (the next leaf opens 'بقیه از صفحهٔ… ; MON:680=partial: vajehyab.com (Mo'in) s.v. پالیز: '(اِ.) ۱- باغ، بوستان. ۲- کشتزار. ۳- زمینی که در آن خربزه…
CON: HRN=supports: HRN.txt leaf 84: '279. pālēz "Garten" (Šāhn. I, 73 Vers 207), pālēzbān, arab. LW. fālīz. a… ; HUB=supports: HUB.txt leaf 133: 'pālīz "Garten" = hebr. pardēs, arm. partēz, zd. pairidaeza-, gr. παραδε… ; BRT=supports: BRT.txt: after the Avestan entry Bartholomae writes 'np. pāliz "Garten" [vgl. gr. LW. παρα… ; PLA=supports: incoming/PLA/PLA_pages.txt leaf 221: 'aw. pairidaeza ... mp. pāliz' — Asbaghi treats pālīz… ; ARY=supports: incoming/ARY/ARY_pages.txt pdf pp. 153-154 (printed pp. 154-155), entry پالیز، فالیز، جالی…
------------------------------------------------------------
# 8 Persian | pardîs, ferdows | verdict: plausible | 
DER: pardīs 'paradise': Wiktionary derives it from 'some reflex of PIr *paridayjah', via a Middle Persian *pardēz (with -ai- > -ē- > NP -ī- and final -z > -s); it is essentially a bookish/late doublet of pālīz and the same word that Greek borrowed. ferdows 'paradise, heaven' is real but the route is a round trip, not the direct Avestan > Persian line drawn: Old Iranian *paridaiza- > Greek parádeisos / Aramaic-Syriac pardaysā (and Hebrew pardēs) > Arabic firdaws (Qurʾān 18:107, 23:11; Arabic f- for p-; Eilers 1962 explains the -aw- as a back-formation from the plural farādīs, which reflects the Greek/Aramaic form) > Persian ferdows borrowed back from Arabic in the Islamic period. Nourai's BQT:1455 (Borhān-e Qāteʿ) glosses are right; only the arrow is simplified.
REF: BQT:1455=supports: RE-CHECKED with tools/ref_page.py BQT:1455 (vol. 3 scan, pdf p. 248; image cached at data/…
CON: FVQ=partial: FVQ_pages.txt leaves 240-241 (Jeffery pp. 223-224) s.v. firdaus: 'Obviously firdaus repres… ; PLA=supports: incoming/PLA/PLA_pages.txt leaf 221 (Asbaghi p. 207) s.v. firdus: 'firdus: "Paradies" aw. … ; ARY=supports: incoming/ARY/ARY_pages.txt pdf pp. 153-154 (printed pp. 154-155), entry پالیز، فالیز، جالی… ; KLN=supports: KLN_1966.txt leaf 600 (printed p. 1124-1125) s.v. paradise: 'ME. paradis, fr. OF. paradis,… ; MON=partial: 'پردیس (پَ) (اِ.) فردوس، بستان.'; 'فردوس (فِ دُ) ۱- باغ، بوستان. ۲- بهشت.' Mo'in equates t… ; IRN=supports: incoming/IRN/IRN_pages.txt (pdf pp. 101-105): 'پادشاهان هخامنشی ... در پیرامون کاخهای خود …
------------------------------------------------------------
# 9 Greek | paradeisos | verdict: confirmed | 
DER: Greek parádeisos 'enclosed park, garden of the Persian nobility' is borrowed from Old Iranian *paridaiza- — specifically the Median form with -z- (Greek -s-), not the Persis form *paridaida- (OP paradayadām, Elamite bar-te-taš); Greek -ei- renders Iranian -ai-/-ē-, -os is the Greek ending. First in Xenophon (5th-4th c. BCE; Anabasis 1.2.7, Oeconomicus 4.13) for the Achaemenid kings' walled hunting parks; the Septuagint (3rd c. BCE) chose it for the Garden of Eden (Gen. 2-3), and Luke 23:43 for the abode of the blessed. Parallel Semitic loans: Akkadian pardēsu, Hebrew pardēs (Neh. 2:8, Eccl. 2:5, Song 4:13), Aramaic pardaysā. AHD's root entry lists 'paradise' under Avestan daēza-, matching Nourai's AHD:950.
REF: AHD:950=supports: AHD online (archived) s.v. paradise: '[Middle English paradis, from Old French, from Late …
CON: KLN=supports: KLN_1966.txt leaf 600 (printed p. 1124-1125) s.v. paradise: 'ME. paradis, fr. OF. paradis,… ; SKT=supports: SKT.txt: 'Paradise. (F. — L. — Gk. — Pers.) F. paradis. — L. paradisus. — Gk. παραδεισος, … ; BRT=supports: BRT.txt: 'np. pāliz "Garten" [vgl. gr. LW. παραδεισος]' — Bartholomae marks παραδεισος exp… ; FVQ=supports: FVQ_pages.txt leaf 241: 'The original word is Iranian, the Av. pairidaeza ... Xenophon int… ; SOD=supports: SOD_pages.txt: Sogdian 'parδez (prδyz) © Av. pari-daeza, garden, orchard' shows the same I…
------------------------------------------------------------
# 10 English | paradise | verdict: confirmed | 
DER: Greek parádeisos > Late Latin paradīsus 'park; garden of Eden; abode of the blessed' > Old French paradis (11th c.) > late Old English/Middle English paradis (c. 1200 for the Christian heaven; c. 1300 'place of bliss'). Uncontroversial chain (Etymonline, AHD).
REF: none=not_checked: Nourai cites no reference for this node. The AHD paradise entry checked at node #9 (archiv…
CON: KLN=supports: KLN_1966.txt: 'paradise, n. — ME. paradis, fr. OF. (= F.) paradis, fr. Late L. paradisus, … ; SKT=supports: SKT.txt: 'Paradise. (F. — L. — Gk. — Pers.) F. paradis. — L. paradisus. — Gk. παραδεισος .… ; PLA=supports: incoming/PLA/PLA_pages.txt leaf 221: 'aw. pairidaeza >> griech. paradeisos, frz. paradis, …
------------------------------------------------------------
# 11 Old Persian | daika | verdict: disputed | 
DER: No Old Persian word daika 'clay pot' is attested; 'daika-' is Hübschmann's reconstructed ancestor of Persian dīg (Persische Studien p. 65, Nourai's HUB:65), which he and Klein (KLN:469) linked to *dʰeyǵʰ- 'knead clay' as 'earthenware vessel'. Modern Iranian etymology rejects this: Rastorgueva & Edelman (ESIJa 2003) and Cheung (2007), followed by Wiktionary, derive MP dēg from PIr *dai(a)-ka- 'that which is heated/fires', from *daiH- 'to shine, radiate, light a fire' (PIE *deyh₂-; cf. Skt. dīp- 'blaze'), with possible contamination from *daǰ- 'to burn' — i.e. a 'fire-vessel', not a 'moulded clay vessel'. The *dʰeyǵʰ- derivation survives only as a mentioned alternative. The 'Old Persian' label is also wrong: the form is a reconstruction and, in Persis, PIE *ǵʰ would give -d-, not the -g- of dīg.
REF: HUB:65=partial: HUB.txt leaf 75 (Hübschmann p. 65), No. 594: 'Wenn dēz, dēza Kochtopf zu got. deigan knete… ; KLN:469=supports: KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī,…
CON: HRN=partial: HRN.txt leaf 153: '594. dēg "Topf", vergl. dez, deze. phlv. dēg "Topf"; lat. figulus "Töpf… ; PHD=silent: PHD.txt: 'dēg [dykʾ | N ~] cauldron.' MacKenzie records the Pahlavi word and its New Persi… ; BRT=silent: Bartholomae's articles on daēz-/daēza-/didā- list np. dez 'Burg' and pāliz among the Irani… ; ARY=silent: Aryanpur's two entries under *DHEIGH- (دژ, دیوار) list Avestan DAĒZAYEITI/UZDAEZA, OP DIDA…
------------------------------------------------------------
# 12 Persian | dîg | verdict: disputed | 
DER: The inner-Persian chain is sound: Middle Persian dyk' /dēg/ 'cauldron' (MacKenzie 1971) > New Persian dīg 'cooking pot, cauldron' (MP ē > NP ī); Semnani dik, Pashto dēg and Hindi/Urdu deg are cognates/loans. What is disputed is the root: as under node 11, the preferred modern source is PIr *daiH- 'shine, burn' (*dai(a)-ka-), not *dʰeyǵʰ-, so the edge to this chart's root is rejected. dīzī 'small clay stew-pot (and the dish cooked in it)' is usually attached to dīg in Persian lexica (BQT:912/914, Moin), but Wiktionary gives it no etymology and I found no independent scholarly derivation; its -z- would in any case not be a regular Persian development of -g-.
REF: BQT:912,914=supports: RE-CHECKED. BQT_v2_pages.txt leaf 374 = printed p. 914 (leaf 372 = p. 912, the دیز/دیزه an… ; KLN:469=supports: KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī,…
CON: HRN=partial: HRN.txt leaf 153: '594. dēg "Topf" ... phlv. dēg "Topf" ... Zu ai. √dih-, degdhi "bestreic… ; PHD=supports: PHD.txt: 'dēg [dykʾ | N ~] cauldron' — the Pahlavi ancestor of NP dīg is attested (as Hübs… ; MON=supports: 'دیگ [ په . ] (اِ.) ظرفی که در آن غذا پزند.' Mo'in tags dīg as Pahlavi ([په.]), i.e. inher… ; AFM=partial: AFM_pages.txt: '+ (الديك) ... معنى ديك ... وهو القدر' — Addi Shir lists Arabic dīk/dīg 'co… ; ARY=silent: Aryanpur's entries under *DHEIGH- do not contain دیگ; the modern Persian etymological dict…
------------------------------------------------------------
# 13 Germanic | daigaz; dîg | verdict: confirmed | 
DER: Proto-Germanic *daigaz 'dough, that which is kneaded' < PIE *dʰóyǵʰos (Kroonen 2013: 87), with PIE *dʰ > Gmc d, *ǵʰ > g, *oy > ai (Grimm's law); Gothic daigs, Old Norse deig, Old English dāg, German Teig. Nourai's second form 'dîg' is AHD's 'Germanic *dīg-' (source of lady) — a zero-grade *dʰiǵʰ- variant; the modern reconstruction for 'kneader of bread, dairymaid' is *daigijǭ/*daigjōn- (Old English dǣge, Old Norse deigja 'maid', Swedish deja 'dairymaid'). The gloss 'one who kneads dough, lady of the house' is AHD's, hence the 'AHD' ref.
REF: AHD=supports: AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old En…
CON: POK=supports: POK_01.txt leaves 255-256: 'got. daigs m. "Teig" (*dhoighos), anord. deig, ags. dāg, ahd. … ; WLD=supports: WLD_Bd1_1930_dli_70244_djvu.txt, Bd. I pp. 833-834 s.v. dheigh-: 'dheigh- "Lehm kneten und… ; SYN=supports: SYN.txt: '4. Goth. daigs, OE dag, etc., gen. Gmc. : Goth. digan "mold, form", Lat. fingere… ; KLN=supports: KLN_1966.txt leaf 261 (printed p. 477) s.v. dough: 'rel. to ON. deig ... Goth. daigs, "dou…
------------------------------------------------------------
# 14 English | dough; lady, dairy | verdict: confirmed | 
DER: dough: OE dāg > ME dogh/dow > dough (PGmc *daigaz). lady: OE hlǣfdīġe 'mistress of a household', literally 'loaf-kneader' = hlāf 'bread, loaf' + -dīġe 'kneader' (< *daigijǭ/*dīg-); the medial -f- was lost by the 14th c. (hlǣfdīġe > lavedi > ladi > lady). dairy: ME daierie (c. 1300) = dey/daie 'dairymaid' (OE dǣġe 'kneader of bread, female servant' < *daigijǭ) + the Anglo-Norman suffix -erie; the sense narrowed from 'servant's/housekeeper's room' to 'place where milk, butter and cheese are made' (1670s). All three are AHD/Etymonline standard.
REF: none=not_checked: Nourai cites no reference for this node. Covered by the AHD dheigh- entry checked at node …
CON: KLN=supports: KLN_1966.txt leaf 261 (printed p. 477) s.v. dough: 'rel. to ON. deig ... Goth. daigs, "dou… ; SKT=supports: SKT.txt: 'Dike ... A.S. dīc. + Du. dijk, Icel. díki, Dan. dige, Swed. dike, G. teich "pond…
------------------------------------------------------------
# 15 Latin | figŭra | verdict: confirmed | 
DER: Latin figūra 'shape, form, figure' is a -ūra derivative of fingō 'to shape, mould (clay), devise, feign' < Proto-Italic *fingō < *θingō, PIE *dʰi-n-ǵʰ- (nasal-infix present of *dʰeyǵʰ-): PIE *dʰ- > Latin f-, *ǵʰ > h > g before n (de Vaan 2008: 221-222). AHD glosses figūra literally as 'result of kneading', which is where Nourai's gloss comes from. (The macron/breve on 'figŭra' in the JSON should be figūra; the -u- is long.)
REF: AHD=supports: AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old En…
CON: LAT=supports: LAT.txt leaf 437-438 (Ernout-Meillet pp. 419-420) s.v. fingo: 'La racine i.-e. dheig'h- ..… ; LEW=supports: LEW_1910.txt leaf 58: 'pairidaēza- I 501, II 251; pairidaēzayeiti ...' — the Latin etymolo… ; WLD=supports: WLD_Bd1_1930_dli_70244_djvu.txt, Bd. I pp. 833-834 s.v. dheigh-: 'dheigh- "Lehm kneten und… ; POK=supports: POK_01.txt leaves 255-256: 'lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...' — P…
------------------------------------------------------------
# 16 English | figure, fiction | verdict: confirmed | 
DER: figure: Latin figūra > Old French figure > English figure (c. 1200, first as 'numeral'). fiction: Latin fictiō (gen. fictiōnis) 'a fashioning, feigning', from fictus, past participle of fingō (same root) > Old French ficcion > English fiction (early 15th c.; 'imaginative prose' 1590s). Both are standard AHD/Etymonline derivations from *dheigh-; fiction descends from fingere rather than from figūra itself, as AHD's grouping shows.
REF: none=not_checked: Nourai cites no reference for this node. Covered by the AHD dheigh- entry checked at node …
CON: KLN=supports: KLN_1966.txt: 'fiction, n. — F., fr. L. fictiōnem, acc. of fictiō, "a forming, shaping", f… ; SKT=supports: SKT.txt: '... All from √DHIGH, to knead, form, mould; as in Dough, Figure.' Skeat files En… ; LAT=supports: Ernout-Meillet: 'fictiō ... t. de droit fictio legis. Le nom n'apparaît pas avant l'époque…
```


## [2026-09-04T23:27:40.088Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p126.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشه همان *dʰeyǵʰ- هندواروپایی آغازین است به معنی «سرشتن گِل، ورز دادن و از آن دیوار ساختن»، و صورت اسمیِ درجهٔ o یعنی *dʰóyǵʰos «آنچه سرشته شده» که هم «دیوار» و هم «خمیر» از آن آمده است؛ پوکورنی (ص ۲۴۴) عیناً همین را می‌گوید و AHD نیز dheigh- «شکل دادن، ساختن» را با ارجاع به پوکورنی می‌آورد. نگارش دومِ نورایی، «Dhigha»، صورت درجه‌صفرِ همان ریشه است (پوکورنی: dhiĝh-lo-s). پس جعبهٔ ریشه و معنای آن درست است. اما دو شاخهٔ نمودار سست است: شاخهٔ «daika > دیگ» را ریشه‌شناسیِ ایرانیِ امروزی رد می‌کند (گره‌های ۱۱ و ۱۲) و آن را از *daiH- «تابیدن، سوختن» می‌گیرد؛ و گره‌های سغدی و «دژ» و «فردوس» هم‌ریشه یا وام‌واژهٔ رفت‌وبرگشتی‌اند نه فرزندِ مستقیمِ پدری که نمودار برایشان کشیده است.\",\n\"nodes_placeholder\": \"\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"didā- پارسی باستان «دیوار، دژ» واژه‌ای گواهی‌شده است: در منشور بنیادگذاریِ کاخ شوش (DSf، سطر ۵۴) عبارت «tyaiy didām apiθa» آمده و کنت آن را در واژه‌نامهٔ خود (ص ۱۹۱) ثبت کرده است. این صورت بازتاب قاعده‌مندِ جنوب‌غربیِ ایرانی باستانِ *daizah < *dʰóyǵʰos است: *ǰ ایرانیِ آغازین (< *ǵʰ هندواروپایی) در پارسی باستان d می‌شود، حال آنکه در اوستایی و مادی z می‌دهد (اوستایی daēza-). اما واژهٔ دوم گواهی‌شده نیست: *daiza-vāra- بازسازیِ هرن و هوبشمان برای نیای «دیوار» است. بررسی تصویر صفحه نشان می‌دهد که کتاب خود «didâ, děğa-vâra» را با همان دو نشانهٔ کوتاه چاپ کرده است، پس خطای خوانشِ اسکن در کار نیست و صورت عجیب از آنِ خودِ کتاب (و برگرفته از *deghavāra-ی هرن) است. بازسازیِ امروزی didā- + *-wāra- است که فارسی میانه dēwār را می‌دهد.\",\n\"2\": \"«دیوار» ترکیبی است از didā- پارسی باستان «دیوار» و *-wāra- (ایرانی *wāra- «پوشش، حصار» از *wer- «پوشاندن») — ارجاعِ نورایی به ریشهٔ Wer 3 درست است — که در فارسی میانه dywʾl /dēwār/ شده و از آنجا «دیوار» فارسی نو آمده است، با تبدیل قاعده‌مندِ ē فارسی میانه به ī و w میان‌واکه‌ای به v. این ترکیب ساختی کهن و جنوب‌غربی است، زیرا بازتابِ d پارسی باستان را دارد نه z مادی/اوستایی را. مکنزی، نیبرگ و آریان‌پور همین را می‌گویند و واژه سپس به ترکی (duvar) و اردو (دیوار) نیز وام داده شده است؛ ادعای نورایی درست است.\",\n\"3\": \"سغدی δyz/δyzʾ «دژ، قلعه» (قریب، ص ۱۵۱) واژه‌ای راستین است و ویکی‌واژه آن را در کنار daēza- اوستایی و didā- پارسی باستان و «دژ» فارسی از بازتاب‌های *dʰóyǵʰos می‌شمارد. اما این صورت هم‌ریشه‌ای ایرانیِ شمال‌شرقی است، از *daizah با تحول‌های قاعده‌مندِ سغدیِ *d- > δ- و *ǰ > z؛ از didā- پارسی باستان (که d- دارد) نمی‌آید، چنان‌که پیکان نمودار می‌رساند. پس واژه درست است اما پیوند باید از *daiza-ی ایرانیِ آغازین/اوستایی‌گونه کشیده می‌شد نه از پارسی باستان؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"4\": \"اوستایی daēza- «دیوار» از ایرانی آغازینِ *daizah و آن از هندوایرانیِ *dʰaiȷ́ʰas و در نهایت از *dʰóyǵʰos هندواروپایی (درجهٔ o از *dʰeyǵʰ-) است، یعنی «آنچه سرشته و قالب زده شده». هم‌ریشه‌های دقیقِ آن سنسکریت dehī- «باره، خاکریز»، یونانی teîkhos «دیوار» و ژرمنیِ آغازین *daigaz «خمیر» است. تحول معنایی از «گِلِ ورزیده» به «دیوارِ خشتی» رفته است. پوکورنی آن را زیر dhoiĝho-s در همان صفحهٔ ۲۴۴ آورده، پس ارجاع نورایی معیار است و ادعای او درست است.\",\n\"5\": \"«دژ/دز» فارسی دنبالهٔ diz فارسی میانه «قلعه» است و آن از *daizah ایرانیِ آغازین — همان واژه‌ای که daēza- اوستایی و didā- پارسی باستان است. اما صورت‌های z-/ž-دار بازتاب مادی و پارتی (شمال‌غربی) از *ǰ ایرانی‌اند نه بازتاب پارسیِ اصیل (که didā- با d است)، پس diz فارسی میانه وامی کهن از شمال‌غرب است و ویکی‌واژه نیز «دژ» را «ایرانی (پارتی؟)» برچسب می‌زند. «دژبان» و «دژدار» ترکیب‌های شفاف‌اند و «دزفول» همان «دژ-پل» است، به مناسبت دژی که نگهبانِ پل ساسانیِ شاپور دوم بر آب دز بود؛ صورت معرّبِ «دزفول» ژ و پِ ناعربی را جایگزین کرده است. پس معنایی که نورایی می‌دهد («پلِ استوار») مسامحه است و پیکانِ او از اوستایی، اختصارِ معمولِ «ایرانی باستان» است، وگرنه واژهٔ فارسی هم‌ریشهٔ صورت اوستایی است نه فرزند آن.\",\n\"6\": \"اوستایی pairi.daēza- «حصارِ گرداگرد» از pairi «پیرامون» (هندواروپایی *péri؛ ارجاع نورایی به ریشهٔ Per 1 درست است) و daēza- «دیوار» ساخته شده و در وندیداد (۳٫۱۸) گواه دارد. صورت ایرانیِ آغازینِ آن *pari-daizah است و ساخت‌های موازی‌اش بلخی prdyjg، خوارزمی prdyz، سغدی prδyz، وام‌واژهٔ ارمنی partēz و پارسی باستان paradayadām است. تحول معنایی از «حصارِ دیواردار» به «باغِ دیواربسته و شکارگاه شاهی» رفته است؛ بارتولومه، هوبشمان و کلاین همه همین را می‌گویند و ادعای نورایی درست است.\",\n\"7\": \"«پالیز» واژه‌ای اصیل است و جای آن در این نمودار درست: از *paridaizah ایرانیِ آغازین، از راه صورت مادیِ *pariδaiza- یا سغدیِ parδēz، به فارسی میانهٔ *pālēz رسیده (با تبدیل -rδ- به -l- که رفتاری مادی/شمال‌غربی است) و از آنجا «پالیز» فارسی نو و «полиз» تاجیکی. ویکی‌واژه آن را وامی از سغدی می‌داند و دستنامه‌های کهن‌تر (هرن، هوبشمان) صورتی مادی؛ به هر روی صورتِ پارسیِ اصیل (با d) نیست و دوگانهٔ «پردیس» و «فردوس» است. اما «جالیز» مشکوک است: فرهنگ‌های فارسی (دهخدا، معین) آن را گونهٔ «پالیز» می‌دانند، حال آنکه ویکی‌واژه آن را جداگانه از ایرانیِ میانهٔ *gardīz می‌گیرد، یعنی ج- ابدالِ سادهٔ پ- نیست؛ برای هیچ‌یک از دو رأی استنادی علمی نیافتم. پس پیوندِ «پالیز» پذیرفتنی و «جالیز» نامعلوم است.\",\n\"8\": \"«پردیس» بنا بر ویکی‌واژه از یکی از بازتاب‌های *paridayjah ایرانی آغازین و از راه فارسی میانهٔ *pardēz آمده است (با ai > ē > ī و z پایانی > س)؛ در عمل دوگانه‌ای کتابی و متأخر از «پالیز» و همان واژه‌ای است که یونانی وام گرفت. اما «فردوس» واژه‌ای است با سفرِ رفت‌وبرگشتی، نه آنچه نمودار به صورت خطِ مستقیمِ اوستایی ← فارسی کشیده است: ایرانی باستان *paridaiza- به یونانی parádeisos و آرامی/سریانی pardaysā رفت، از آنجا به عربیِ «فردوس» (قرآن، کهف ۱۰۷ و مؤمنون ۱۱؛ ف عربی به جای پ، و ‑َو- را آیلرس واپس‌ساختی از جمعِ «فرادیس» می‌داند) و سپس در دورهٔ اسلامی از عربی به فارسی بازگشت. معناهایی که نورایی از برهان قاطع نقل می‌کند درست است؛ تنها پیکان ساده‌سازی شده است.\",\n\"9\": \"یونانی parádeisos «باغِ محصورِ بزرگان پارسی» وامی از ایرانی باستانِ *paridaiza- است، آن هم به‌خصوص از صورت مادی با z (که در یونانی س می‌شود) نه از صورت پارسیِ *paridaida- (پارسی باستان paradayadām، ایلامی bar-te-taš)؛ -ei- یونانی همان -ai-/-ē- ایرانی را می‌نمایاند و -os پایانهٔ فاعلیِ یونانی است. نخستین گواه‌ها نزد گزنفون (سدهٔ پنجم–چهارم پیش از میلاد؛ آناباسیس ۱٫۲٫۷) برای شکارگاه‌های دیواربستهٔ شاهان هخامنشی است؛ سپس ترجمهٔ سبعینیه (سدهٔ سوم پیش از میلاد) آن را برای باغ عدن برگزید و لوقا ۲۳:۴۳ برای جایگاه نیکان. وام‌های سامیِ موازیِ آن اکدی pardēsu، عبری pardēs و آرامی pardaysā است. ادعای نورایی درست است.\",\n\"10\": \"یونانی parádeisos به لاتینیِ متأخر paradīsus رفت («باغ؛ بهشت عدن؛ جایگاه نیکان»)، از آنجا به فرانسوی کهن paradis (سدهٔ یازدهم) و سپس به اواخر انگلیسی باستان و انگلیسی میانه paradis (حدود ۱۲۰۰ برای بهشت مسیحی و حدود ۱۳۰۰ برای «جای خوشی»). این زنجیره در هیچ منبعی محل اختلاف نیست (اتیمآنلاین، AHD، کلاین، اسکیت) و ادعای نورایی درست است.\",\n\"11\": \"واژه‌ای پارسی باستان به صورت daika «دیگ گِلی» گواه ندارد؛ *daika- بازسازیِ هوبشمان (مطالعات فارسی، ص ۶۵) برای نیای «دیگ» فارسی است که او و کلاین آن را به *dʰeyǵʰ- «سرشتن گِل» بستند، یعنی «ظرف سفالین». ریشه‌شناسیِ ایرانیِ امروزی این را رد می‌کند: راستارگویوا و ادلمان و نیز چونگ — و به پیروی آنان ویکی‌واژه — dēg فارسی میانه را از *dai(a)-ka- از ریشهٔ *daiH- «تابیدن، آتش افروختن» (هندواروپایی *deyh₂-؛ سنسکریت dīp-) می‌گیرند، شاید با آمیختگی با *daǰ- «سوختن»، یعنی «ظرفِ آتش» نه «ظرفِ گِلِ قالب‌زده». اشتقاق از *dʰeyǵʰ- تنها به عنوان رأیی جایگزین یاد می‌شود. برچسب «پارسی باستان» نیز نادرست است، چون صورت بازسازی‌شده است و در پارسی *ǵʰ می‌بایست d بدهد نه g.\",\n\"12\": \"زنجیرهٔ درون‌فارسی بی‌اشکال است: فارسی میانه dyk' /dēg/ «دیگ» (مکنزی) به «دیگ» فارسی نو رسیده (ē > ī) و سمنانی dik، پشتو dēg و اردو deg هم‌ریشه یا وام‌اند. آنچه محل اختلاف است ریشهٔ نهایی است: چنان‌که در گرهٔ ۱۱ گفته شد، سرچشمهٔ ترجیحیِ امروزی *daiH- «تابیدن، سوختن» است نه *dʰeyǵʰ-، پس پیوند این گره با ریشهٔ این نمودار رد می‌شود. «دیزی» را فرهنگ‌های فارسی (برهان، معین) معمولاً به «دیگ» می‌بندند، اما ویکی‌واژه برایش ریشه‌شناسی نمی‌آورد و من نیز استنادی علمی نیافتم؛ به هر روی -ز- آن نمی‌تواند تحولِ قاعده‌مندِ -گ- در فارسی باشد.\",\n\"13\": \"ژرمنیِ آغازین *daigaz «خمیر، آنچه ورز داده شده» از *dʰóyǵʰos است (کرونن ۲۰۱۳، ص ۸۷): *dʰ هندواروپایی در ژرمنی d، *ǵʰ به g و *oy به ai بدل شده است (قانون گریم)؛ از این ستاک گوتی daigs، نورس کهن deig، انگلیسی باستان dāg و آلمانی Teig آمده است. صورت دومی که نورایی می‌آورد، «dîg»، همان *dīg- ژرمنیِ AHD است (سرچشمهٔ lady) که گونهٔ درجه‌صفرِ *dʰiǵʰ- است؛ بازسازیِ امروزی برای معنای «نان‌ورزنده، کدبانو» *daigijǭ است (انگلیسی باستان dǣge، نورس کهن deigja، سوئدی deja). معنایی که در جعبه آمده از AHD گرفته شده و ادعای نورایی درست است.\",\n\"14\": \"dough از dāg انگلیسی باستان (< *daigaz) از راه انگلیسی میانهٔ dogh آمده است. lady از hlǣfdīġe انگلیسی باستان «بانوی خانه» است که تحت‌اللفظ یعنی «ورزندهٔ نان»: hlāf «نان» + -dīġe «ورزنده» (< *daigijǭ)؛ ف میانی تا سدهٔ چهاردهم افتاده و زنجیرهٔ hlǣfdīġe > lavedi > ladi > lady پدید آمده است. dairy از انگلیسی میانهٔ daierie (حدود ۱۳۰۰) است، از dey/daie «شیردوش، خدمتکار» (انگلیسی باستان dǣġe «ورزندهٔ نان») به‌علاوهٔ پسوند انگلوـنورمنِ -erie، و معنایش از «اتاق خدمتکار» به «جای فرآوردن شیر و کره و پنیر» (دههٔ ۱۶۷۰) محدود شده است. هر سه با AHD و اتیمآنلاین می‌خواند؛ ادعای نورایی درست است.\",\n\"15\": \"لاتینی figūra «شکل، صورت» مشتقی با پسوند -ūra از فعل fingō «قالب زدن، سرشتن، ساختن» است، از ایتالیکیِ آغازین *fingō و در نهایت از *dʰi-n-ǵʰ-، یعنی صورت حالِ ریشه با میان‌وندِ خیشومی: *dʰ- هندواروپایی در لاتینی f- می‌شود و *ǵʰ پیش از n به g بدل می‌گردد (دِ ڤان ۲۰۰۸، ص ۲۲۱–۲۲۲). AHD معنای تحت‌اللفظیِ figūra را «حاصلِ ورز دادن» می‌آورد و معنایی که نورایی داده از همان‌جاست. ادعای او درست است؛ تنها در ضبط، «figŭra» باید figūra باشد چون واکهٔ آن کشیده است.\",\n\"16\": \"figure از لاتینی figūra از راه فرانسوی کهن figure به انگلیسی رسیده است (حدود ۱۲۰۰، نخست به معنی «رقم»). fiction از لاتینی fictiō «شکل دادن، برساختن» است، از fictus اسم مفعولِ fingō، از راه فرانسوی کهن ficcion (اوایل سدهٔ پانزدهم؛ معنای «داستان تخیلی» از دههٔ ۱۵۹۰). هر دو اشتقاق معیارِ AHD و اتیمآنلاین‌اند، با این تفاوت که fiction از خودِ fingere می‌آید نه از figūra، چنان‌که دسته‌بندیِ AHD نشان می‌دهد. ادعای نورایی درست است.\"\n}\n}\n}\nEOF\npython3 - <<'PY'\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p126.json'))\nd['entry'].pop('nodes_placeholder',None)\njson.dump(d,open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p126.json','w'),ensure_ascii=False)\nprint(list(d['entry']),len(d['nodes']['0']))\nPY\npython3 apply_fa_text.py 126 p126.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-126.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-126.json",
 "description": "Apply Persian to page 126"
}
```


### [2026-09-04T23:27:42.098Z] TOOL RESULT

```
Exit code 1
['0'] 16
MISSING [('entry', 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16)]
```


## [2026-09-04T23:27:45.488Z] TOOL CALL #30: Bash

```json
{
 "command": "head -c 1200 /home/sfmqrb/git/rishe/data/verification/page-126.json; echo; echo ===; grep -n '\"id\"' /home/sfmqrb/git/rishe/data/verification/page-126.json | head -3",
 "description": "Inspect page 126 structure"
}
```


### [2026-09-04T23:27:45.530Z] TOOL RESULT

```
Exit code 1
{
 "pdf_page": 126,
 "book_page": 96,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "Dheigh, Dhigha",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'",
   "note": "Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos",
    "https:
(eval):1: == not found
```


## [2026-09-04T23:27:58.037Z] TOOL CALL #31: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_fa_text.py <<'PYEOF'\nimport json,re,sys\npage=sys.argv[1]; patch=json.load(open(sys.argv[2]))\npath=f'/home/sfmqrb/git/rishe/data/verification/page-{page}.json'\nlines=open(path).read().split('\\n')\nout=[]; cur_e=None; cur_n=None; e_ind=None; n_ind=None\nfor ln in lines:\n    out.append(ln)\n    m=re.match(r'^(\\s*)\"entry\": (\\d+),\\s*$',ln)\n    if m: e_ind,cur_e=m.group(1),m.group(2); cur_n=None; n_ind=None; continue\n    m=re.match(r'^(\\s*)\"id\": (\\d+),\\s*$',ln)\n    if m: n_ind,cur_n=m.group(1),m.group(2); continue\n    m=re.match(r'^(\\s*)\"note\": ',ln)\n    if m and cur_e is not None and cur_n is None and m.group(1)==e_ind:\n        out.append(f'{e_ind}\"note_fa\": {json.dumps(patch[\"entry\"][cur_e],ensure_ascii=False)},'); continue\n    m=re.match(r'^(\\s*)\"derivation\": ',ln)\n    if m and cur_n is not None and m.group(1)==n_ind:\n        out.append(f'{n_ind}\"derivation_fa\": {json.dumps(patch[\"nodes\"][cur_e][cur_n],ensure_ascii=False)},'); continue\nnew='\\n'.join(out)\nd=json.loads(new)\nmiss=[]\nfor en in d['entries']:\n    if 'note_fa' not in en: miss.append(('entry',en['entry']))\n    for n in en['nodes']:\n        if 'derivation_fa' not in n: miss.append((en['entry'],n['id']))\nif miss: print('MISSING',miss); sys.exit(1)\nopen(path,'w').write(new)\nprint('ok',page)\nPYEOF\ncd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 apply_fa_text.py 126 p126.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-126.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-126.json",
 "description": "Apply page 126 with generalized script"
}
```


### [2026-09-04T23:28:00.210Z] TOOL RESULT

```
ok 126
JSON_OK
 data/verification/page-126.json | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)
```


## [2026-09-04T23:28:02.030Z] AGENT

Now pages 311 and 345.


## [2026-09-04T23:28:03.129Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 311 2>&1 | head -220",
 "description": "Dump page 311"
}
```


### [2026-09-04T23:28:05.566Z] TOOL RESULT

```
##########################################################################################
PAGE 311 book 281
================================================================================
ENTRY 0 | root: Leudh, Rei | verdict: confirmed | modern: PIE *h₁lewdʰ- 'to grow, rise; (hence) offspring, people' (Pokorny 684-685 leudh-; LIV 248 *h₁leudʰ-; AHD leudh-)
NOTE: Pokorny 684-685 leudh- 'emporwachsen, hochkommen' with the derivatives leudho-/leudhi- 'Nachwuchs, Volk' and leudhero- 'zum Volk gehörig, frei' (Av. raoδaiti 'grows', raoδa- 'Wuchs, Ansehen', Lat. līber, OHG liut, OCS ljudьje) is exactly Nourai's root; Cheung 2007:193 gives the Iranian reflex *Hraud 'to grow (bigger)' and LIV *h₁leudʰ-. The Iranian r- is the regular Proto-Iranian merger of PIE *l with *r, not a separate root: the label 'Rei' has no counterpart in Pokorny/AHD and is unexplained (possibly Nourai's cross-reference label). Two branches of the chart are not from this root at all: the Arabic loans rawḍa (#4) and ḥūr (#15) are native Semitic, Arabic rawnaq (#7) is native Arabic, and rōstāg/Rostam (#9, #11) are today derived from the 'river' word (*srew-), not from 'grow'. The chart's own NOTE on #4 (AFM derives rawḍa from rīxtan, VDQ from rōt) records alternative Persian etymologies that modern lexicography rejects as well.
ROOTREF: POK:684=supports ; KLN:885=supports ; SYN:874=partial ; VDQ:39=partial
------------------------------------------------------------
# 1 Avestan | raod 1, raoda, raodha | verdict: confirmed | 
DER: Young Avestan verb raoδ- (raoδaiti 'grows', Vd 5.19; raoδahe Y 10.4; past participle urusta-/rusta- 'grown') and the nouns raoδa- m. 'growth, stature, appearance' (Pokorny: 'Wuchs, Ansehen') and raoδah- n. 'growth' are the direct Iranian reflexes of PIE *h₁lewdʰ-: PIE *l > Proto-Iranian *r, *ew > ao, *dʰ > δ. The sense 'face' is a secondary development of 'appearance, outward form' (Wiktionary روی: Proto-Iranian *rauda- 'appearance' < 'growth'). Nourai's cited KLN/SYN are consistent with Pokorny 684, which is the standard treatment.
REF: KLN:885=supports: KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. b… ; SYN:874=partial: SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '...…
CON: BRT=supports: AiW col. 1493 f.: 'j. ²raod- V. „wachsen“. Praes. 2 raoða-, 27 uruðya-; Perf. urūrud-. — P… ; CHEUNG=supports: '*AVESTAN: YAv. raoð- (ruð-) “to grow” … IND. 2sg. med. YAv. raoðahe (Y 10.4), 3pl. raoðan… ; WLD=supports: 'av. raodaiti „wächst“ … av. raoda- m. „Wuchs, Ansehen“, npers. roi „Gesicht“' — Walde-Pok… ; NYB=supports: 'rustan [lwstn'] rod- [lwd-] to grow … — Av. (1492 sq.) ²raod-' — Nyberg cites AiW cols. 1…
------------------------------------------------------------
# 2 Persian | rŭy-îdan; rŭy 1 | verdict: confirmed | 
DER: Av./Old Iranian raoδ- → Middle Persian present stem rōy- (Manichaean rwy-, Pahlavi lwd- /rōy-/, 3sg rōyēd) with past participle rust (rwst/lwst), Parthian rwd-/rwst → New Persian rustan/rōy- and the regularized infinitive rōyīdan 'to grow' (Cheung 2007:193; Wiktionary: Proto-Iranian *Hráwdah). Old Iranian intervocalic -d- > MP -y- (raoδa- > rōy) explains the y of rōy-/rūyīdan, while the participle keeps -st- (rust-, rustan). The noun rūy 'face' is MP rōy 'face' < Proto-Iranian *rauda- 'growth, appearance' (Edelman ESIJ 6:402; Cheung 193), the same word: 'growth, stature' → 'appearance' → 'face'.
REF: BQT:944=partial: The روییدن/روی entries (BQT_v2_pages.txt leaves ~400-403, printed pp. ~944-946) are not le…
CON: HRN=supports: HRN.txt leaf 157 (p.136): '614. rusten „wachsen“, Praes. roy-em, royiden, royaniden, rosta… ; HUB=supports: HUB.txt leaf 209 (p.199) among the examples of Av. ð > NP y: 'roi (ro) „Gesicht“ = zd. rao… ; PHD=supports: 'rustan, roy- [lwstn', lwd- | M rwst, rwy-, N ~] grow. ~išn: growth' and '¹roy [lwd | M rw… ; MON=supports: MON_part1.txt: 'روییدن rūyīdan [= رستن] (مص‌ل.) نمو کردن نباتات، بالیدن، رشد کردن' — Mo'in… ; IEC=partial: 'rūs- (3) “space, place”. Cf. reuos (2). WP II, 356. (Iranian ambig.) Per. rū, rūy, s. “fa…
------------------------------------------------------------
# 3 Persian | raz | verdict: disputed | 
DER: Persian raz 'vine, vineyard' (with the compounds razbān 'vine-keeper', razbun 'vine-stock') is a real word continuing Middle Persian raz (Pahlavi lc /raz/), but no modern source derives it from the root 'to grow': there is no Old Iranian *raza- 'growth', and rūy-/rust- could not yield a form with -z-. Wiktionary and the Greek/Latin etymological literature group Persian raz with Ancient Greek ῥάξ (gen. ῥαγός) 'grape', Latin racēmus 'bunch of grapes', Albanian rrush 'grape' as a Mediterranean/Near-Eastern culture Wanderwort of unknown (substrate) origin; the connection with 'grow' in Borhān-e Qāṭeʿ (BQT) and FSF is folk etymology.
REF: BQT:944=partial: BQT_v2_pages.txt leaf 404 (printed p. ~947; Nourai 944): 'رز = بفتح اول و سکون ثانی، درخت … ; FSF:199=partial: FSF_pages.txt leaf 265 (page numeral illegible; Nourai p. 199), s.v. 'رز (با زبر اول): ۱- …
CON: PHD=partial: 'raz [/c, lz | N ~] vine; vineyard' — MacKenzie has the Middle Persian word (so the Persia… ; IEC=contradicts: IEC.txt ff-block 372 (printed 659-660): 'laĝ- “wind, creep; twist, winding object, creeper… ; PLA=partial: 'razzāgī „Weintrauben; Wein“ ← pers. raz „a vineyard“, mp. raz „vine, vineyard“' (fn. 3 Ma… ; NYB=silent: Nyberg's glossary has only 'rāz [lʾc] a secret — Av. (1514) razah-'; there is no raz 'vine… ; HRN=silent: Horn's r- section (razm 612, rusten 614, roi 636, rēxtan 638 …) has no entry for raz 'vine…
------------------------------------------------------------
# 4 Arabic | rauza | verdict: disputed | 
DER: Arabic rawḍa (رَوْضَة) 'garden, meadow' (Qurʾān 30:15 fī rawḍatin), pl. riyāḍ, is a native formation from the Semitic root r-w-ḍ (rāḍa 'to train, tame', rawḍa 'meadow where water collects'); it has the emphatic ḍ, which never arises in Arabic renderings of Persian z (Persian raz would give *rawz/rāz, not rawḍ-). Wiktionary and Wehr treat it as Arabic with no Persian source; Persian rowze is listed only as a descendant. Nourai's PLA:138 derivation from raz, and the alternatives his NOTE records (AFM/Addai Sher from rīxtan 'to pour'; VDQ/Jeffery from Pahlavi rōt 'river'), are all unsupported by modern lexicography; the whole sub-branch #3 → #4 → #5 does not belong to *leudh-. Correction after checking Asbaghi on disk: PLA:138 does say what Nourai claims ('rauda „Garten“ aus pers. raz ← Verb rostan, mp. rod < aw. raod / ap. raza „Weinstock“'), and Jeffery (FVQ 145-146, after Vollers) likewise calls the word Iranian but derives it from Pahlavi rod 'river'; the verdict stays disputed because standard Arabic lexicography keeps rawda inside the root r-w-d and the two Iranian proposals contradict each other.
REF: PLA:138=supports: Asbaghi is now on disk. PLA_pages.txt leaf 153 = printed p.138: 'rauda: „Garten“ aus pers.… ; AFM:75=contradicts: AFM_pages.txt leaf 76 (Addi Shir p. ~75): '(الروضة) من الرمل والعشب مستنقع الماء ... وهي م… ; VDQ:226=partial: The chart's own NOTE cites VDQ:226 for a derivation from Pahlavi 'rot: river'. Checked via…
CON: FVQ=partial: FVQ_pages leaf 162 f. (pp.145-146): 'There can be little doubt that the word was borrowed … ; LKT=contradicts: LKT.txt leaf 164 (p.138): '1709. Ar. rauda: „Garten“, plr. rijad, im Magrib singularisch g… ; AFA=silent: Fraenkel's discussion of Arabic garden words treats جنة (from Aramaic) and حدیقة ('Zaun' >… ; KLN=silent: Klein's dictionary has no rawda/rauda entry (the word gave no English derivative), so it c…
------------------------------------------------------------
# 5 Persian | rowzeh | verdict: confirmed | 
DER: The edge as drawn is correct: Persian rowze «روضه» 'garden; shrine garden' is borrowed from Arabic rawḍa (Arabic ḍ rendered as Persian z, tāʾ marbūṭa as -e/-eh; Saʿdī's رَوْضَهٔ رِضْوان 'garden of Paradise' shows the classical sense), and riyāḍ «ریاض» is the Arabic broken plural. The later Shiʿi sense 'Karbalā elegy' comes from Kāshefī's Rowżat al-shohadāʾ (15th c.). Only the ancestry above #4 is wrong: the word is Semitic, not Indo-European.
REF: MON=supports: vajehyab.com (Mo'in) s.v. روضه: '(رَ ض) [ع. روضة] (اِ.) ۱- باغ، گلزار. ج. ریاض، روضات. ۲- …
CON: MON=supports: MON_part1.txt: 'روضه rowza(t) [ع. روضة] (اِ.) باغ، گلزار؛ ج. ریاض، روضات … خطبه‌ای که در م… ; BQT=partial: Borhān-e Qāṭeʿ has no independent روضه headword, only Persian compounds built on the Arabi… ; FVQ=partial: Jeffery's entry documents the Arabic word (Qur'ān xxx.14, xlii.21; 'A rich, well watered m…
------------------------------------------------------------
# 6 Persian | rŭnîk | verdict: plausible | 
DER: rū-nīk «رونیک», glossed 'beautiful' and equated by the chart with nīk-rūy «نیکروی» 'fair-faced', is a transparent compound of rūy 'face' (#2, < MP rōy < Proto-Iranian *rauda- 'appearance') + nīk 'good' (Nourai's cross-reference Nei 1). Nourai gives no reference for it; I found it only in modern online Persian dictionaries (vajehyab: 'نیک رو، خوش رو، زیبارو') and as the modern given name Rūnīkā, while nīk-rūy itself is in Dehkhoda. The word is morphologically sound and its first element does belong to this root, but I could not verify a classical attestation of rūnīk, and the claim that it is the source of Arabic rawnaq (#7) is rejected below.
REF: none=not_checked: Nourai cites no reference for this node. Addi Shir's rawnaq entry checked at node #7 presu…
CON: BQT=silent: No رونیک headword anywhere in the OCR of Borhān-e Qāṭeʿ vols. 1-2 (BQT_v1_pages.txt / BQT_… ; MON=silent: Mo'in's lexicon text has رونق, روند, رونما but no رونیک; the compound is not lexicalised i… ; PHD=silent: MacKenzie has no Middle Persian *roy-nēk compound, so there is no pre-Islamic form for Ara…
------------------------------------------------------------
# 7 Arabic | raonaq | verdict: disputed | 
DER: Arabic rawnaq (رَوْنَق) 'beauty, splendour, lustre, radiance' is treated by Wiktionary (citing Wehr and al-Maʿānī) as a native Arabic noun of the root r-n-q (cf. rāniq 'clear, limpid (water)', ranaqa/tarawnaqa 'to be clear, glisten'), of the fawʿal pattern; Persian rownaq is listed as borrowed from it. The Persian source rū-nīk proposed by Nourai (after AFM:74 = Addai Sher, al-Alfāẓ al-fārisiyya al-muʿarraba, 1908, many of whose derivations are no longer accepted) would require the unexplained loss of -y- and an irregular k > q; no modern dictionary follows it.
REF: AFM:74=supports: AFM_pages.txt leaf 75 (Addi Shir p. ~74): '(الرونق) حسن كل شيء، معرب رو أي وجه ومن نيك أي …
CON: PLA=silent: Asbaghi's alphabetical inventory of Persian loanwords in Arabic runs razzāgī, razdaq, rizq… ; LKT=silent: Lokotsch's Arabic word-index runs 'ratam 1707, ratl 1708, rauda 1709, razza 1713 …' with n… ; KLN=silent: Not in Klein (no English derivative), so no independent Semitic-vs-Iranian judgement there…
------------------------------------------------------------
# 8 Persian | rownaq | verdict: confirmed | 
DER: The edge is correct: Classical Persian rownaq «رونق» 'splendour; flourishing, boom, heyday' is a straightforward loan of Arabic rawnaq (Wiktionary: 'Borrowed from Arabic رَوْنَق'), the Arabic diphthong aw being kept as Persian ow; the meaning 'growth, success' is a Persian semantic extension, and the word spread on from Persian to Urdu/Hindi raunaq, Chagatai and Kurdish. The ancestry drawn above #7 (Persian rūnīk) is not accepted: the word is Arabic in origin.
REF: MON:1694=supports: vajehyab.com (Mo'in) s.v. رونق: '(رُ نَ) [ع.] (اِمص.) ۱- فروغ، روشنایی. ۲- زیبایی، جمال. ۳…
CON: MON=supports: MON_part1.txt: 'رونق rownaq [ع.] (امص.) فروغ، روشنایی؛ زیبایی، جمال؛ رواج' — tagged [ع.] A… ; BQT=partial: Borhān uses رونق only inside glosses and in a quoted verse ('… و رونق باشد، شهید (بلخی) گف… ; PLA=silent: Asbaghi lists no rawnaq, so the Persian word cannot be a returning Persian loan on his evi…
------------------------------------------------------------
# 9 Pahlavi | rôstâk | verdict: disputed | 
DER: Middle Persian rōstāg (Pahlavi lwstʾk') 'district, province, rural district' (MacKenzie, Concise Pahlavi Dictionary) is a real word and the source of Arabic rustāq, Syriac rustāqā and Old Armenian ṙotastak (from a Parthian *rōdastāg). Its etymology, however, is a compound *raudas-tāka-/*rautas-tāka- 'river-course, river-district' of Old Iranian rautah-/raudah- 'river' (OP rautah-, MP rōd, NP rūd < Proto-Iranian *hrautah- < PIE *srew- 'to flow') + -tāka- 'course, run' (root tak-/tač- 'to run, flow'; cf. Bactrian tago 'river valley'): rōd + tāg > rōstāg with regular devoicing of the cluster. The Parthian form rōdastāg with -d- shows the 'river' word plainly. Nothing connects it to 'grow' (*leudh-); Wiktionary leaves the deeper etymology open but gives no 'grow' derivation.
REF: MON:1689=partial: vajehyab.com (Mo'in) s.v. روستا: '(اِ.) ده، قریه' — the online Mo'in text gives the meanin…
CON: PHD=contradicts: 'rostag [lw(t)stʾk' | (P rwdystʾg), N rūstā] river-bed; district, province'; English index… ; NYB=contradicts: 'rotastāk [lwtstʾk], rostak [lwstʾk] district, province … MPrth rwdystʾg; Paz. rostā …; NP… ; HRN=supports: Horn lists 'rostā (arab. syr. LW. rustāq)' and 'phlv. rostāk [rodastak, Salemann, Eine Pär… ; PLA=partial: 'ruzdāg „Marktflecken“ ← pers. rūstā, mp. rostāk, rotstāk; ar. Lw. ruzdāg u. rustāg' — Asb… ; BRT=partial: AiW keeps four homonymous roots apart: '²raod- V. „wachsen“' (col. 1493) and '⁴raod- V. „f…
------------------------------------------------------------
# 10 Persian | rŭstâ | verdict: confirmed | 
DER: The edge is correct: MP rōstāg 'district' → Classical Persian rōstā(y) «روستا / روستای» 'countryside, village' with regular loss of the final -g of the MP -āg suffix (as in dānāg > dānā); the Arabic loan rustāq (with -q) and the by-form rostāq preserve the older shape. The semantic narrowing 'rural district' → 'village' is a Persian development. As noted at #9, the root is 'river' (*srew-), not 'grow'. Nourai's IEC:1103 turns out to be a correct page reference: Mann does list 'Per. rūsta, s. “village”' there, but under rūs- 'space, place' beside Latin rūs — a third etymology, neither 'grow' nor 'river'.
REF: IEC:1103=partial: Re-checked with the printed page numerals rather than the leaf formula: IEC p.1103 (the nu… ; MON:1689=supports: Re-checked in Mo'in's own text (the 2-vol. Adena abridgement, MON_part1.txt, is on disk; p…
CON: PHD=supports: 'rostag … N rūstā' — MacKenzie gives the New Persian outcome of the Middle Persian word di… ; NYB=supports: 'Paz. rostā, pl. rostāihā; NP rostā(i) “any inhabited place; a market-town, a village”' — … ; HRN=supports: 'rostā (arab. syr. LW. rustāq)' beside 'phlv. rostāk' — same edge, and the Arabic/Syriac l… ; PLA=supports: 'ruzdāg … ← pers. rūstā … mp. rostāk, rotstāk' and 'rustāq „Marktflecken“ = ruzdāq, mand. … ; BQT=silent: No روستا headword in the OCR of Borhān vols. 1-2 (only روستایی/روستائان inside Mo'in's foo…
------------------------------------------------------------
# 11 Avestan | raodha-taxma | verdict: disputed | 
DER: No such word occurs in the Avesta; Rostam is absent from the Avestan texts, and *Raoδas-taxma- is a scholarly reconstruction (Justi, Iranisches Namenbuch) behind Middle Persian Rōdstahm (lwtsthm), Sogdian Rwstmy and New Persian Rostam. The language label should therefore be 'Old Iranian (reconstructed)'. The standard modern analysis (Wiktionary, Iranica, Mayrhofer/Schmitt) reads the compound as *Rautas-/Raudas-taxma- 'strong as a river' or 'whose running is like a river's', i.e. first element Av. raoδah-/OP rautah- 'river' (< *srew- 'flow', the same word as in rōstāg #9) + taxma- 'strong, brave' (Nourai's cross-reference Tenk); the older reading 'grown strong' with raoδah- 'growth' is a minority interpretation not followed by current reference works.
REF: KLN:885=partial: KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. b… ; SYN:874=partial: SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '...…
CON: BRT=contradicts: AiW col. 626: 'j., g. (, p.) taxma- Adj. „fortis, tapfer, tüchtig, energisch, heldenhaft“'… ; NYB=contradicts: 'Rotastahm [lwtsthm] n. pr. — NP Rustam; Old Sogd rwstmy' — the attested Middle Persian na… ; PLA=contradicts: 'rustam „Reichsfeldherr“ ← mp. rotastahm, mand. rustam' — Asbaghi too reads the first elem… ; IEC=silent: Mann's comparative dictionary has no entry for the name or for an IE *leudh-o-teg-mo- comp…
------------------------------------------------------------
# 12 Persian | Rostam | verdict: plausible | 
DER: The name does continue the reconstructed compound behind #11: Old Iranian *Raudas-/Rautas-taxma- → Middle Persian Rōdstahm (lwtsthm; Pahlavi stahm 'force, power' < taxma-) → New Persian Rostam «رستم» (Rustam), with -dst- > -st- and shortening of ō before the cluster; Sogdian Rwstmy shows the same contraction already in Middle Iranian. So the edge is right, but the first element is 'river', not 'growth' (see #11); Ferdowsī's rastam 'I escaped' (Shāhnāma, Rostam's caesarean birth) is a poetic folk etymology.
REF: BQT=supports: BQT_v2_pages.txt leaf 408 (printed p. ~951), Mo'in's footnote s.v. رستم: 'رستم = رستهم: رو…
CON: NYB=supports: 'Rotastahm [lwtsthm] n. pr. 116². — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.-… ; PLA=supports: 'rustam „Reichsfeldherr“ … mp. rotastahm, mand. rustam' — same MP antecedent, and an Arama… ; PHD=silent: MacKenzie's Concise Pahlavi Dictionary excludes proper names, so it has no Rostahm entry. ; MON=partial: 'رستم: مرد شجاع، دلیر، پهلوان' — the appellative use is recorded, but this abridgement car…
------------------------------------------------------------
# 13 Avestan | hava-rd | verdict: transcription_suspect | error_in=book book_prints=hava-rd : well grown, well built, beautiful ☞ Su 1 correct_form=hu-raoda (Av. huraoδa-)
DER: 'hava-rd' is not a possible Avestan form; the book almost certainly printed hu-raodha (Av. huraoδa-), and the scan lost/garbled letters. Av. huraoδa- 'well-grown, well-shaped, handsome' is a real Young Avestan adjective (Vidēvdād 3.24 'iδa carāiti huraoδa'; epithet of Sraoša in Yasna 57), built from hu- 'good, well' (PIE *h₁su-; Nourai's cross-reference Su 1) + raoδa- 'growth, stature' (#1). Its meaning and root membership are exactly as glossed; only the transliteration is corrupt. Checked against the scan (data/verification/sources/refs/ocr/BOOK/311.png): the box is printed 'hava-rd', cleanly and with nothing lost, while the Pahlavi box on the same row prints 'hu-rust' correctly — so 'hava-rd' is Nourai's own garbling of Av. huraoδa- and the extraction is faithful, not the source of the corruption.
REF: VDQ:39=supports: Checked through the English original (VDQ = Badreh'i's Persian translation of FVQ; noorlib… ; MAG:186=not_checked: MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.
CON: BRT=supports: AiW cites the adjective repeatedly: 'j. čarāiti- f. „junge Frau“ … čarāitiš (NS.) huraoðay… ; FVQ=supports: 'Now hurust is a good Iranian word, the equivalent of Av. huraoða-, and though these Pahla… ; PLA=supports: 'hūrī „Huri, Paradiesjungfrau, Schönheit“ ← mp. hūrast „gut gewachsen“ ← aw. huraoða' — ag… ; CHEUNG=partial: Cheung's dictionary covers verbs, so huraoða- is not a headword; but the root *Hraud 'to g…
------------------------------------------------------------
# 14 Pahlavi | hu-rust | verdict: confirmed | 
DER: Middle Persian hurust 'well-grown, well-built, fine' = hu- 'well' + rust, the past participle of rōy-/rustan 'to grow' (Cheung 2007:193: BMP lwst /rust/, MMP rwst; the Iranian participle *Hrusta- is the analogical replacement of expected *Hruzda- < *Hrudʰ-ta-). It is thus the Middle Persian counterpart of Av. huraoδa- (#13), formed on the participle rather than on the noun raoδa-, but from the same root and with the same meaning. Jeffery cites this word as MP hū̆rust 'well grown'.
REF: MAG:186=not_checked: MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online. ; VDQ:39=supports: Checked through the English original FVQ pp.119-120: 'It is much more likely that the word…
CON: PHD=supports: 'hu-|-ramag [hwlmk'] having good flocks. ~-rust [-lwst'] well-grown' (p.48); English index… ; FVQ=supports: 'It is much more likely that the word comes from the Phlv. hurust, meaning beautiful, and … ; PLA=supports: 'mp. hūrast „gut gewachsen“' — same Middle Persian word and meaning (Asbaghi's transcripti… ; HRN=partial: 'phlv. rod, hu-rod(i)šn (AV.)' — Horn cites the Ardā Wīrāz word in the abstract form hu-ro… ; NYB=silent: Nyberg's glossary (to the texts he edits) does not contain hurust; it has rustan/rod- 'to …
------------------------------------------------------------
# 15 Arabic | hŭr | verdict: disputed | 
DER: Arabic ḥūr (حُور), the plural of aḥwar (m.) / ḥawrāʾ (f.) 'having eyes with a strong contrast of white and black', in the Qurʾānic phrase ḥūrun ʿīnun (44:54, 52:20, 56:22) 'fair, large-eyed maidens', is a regular Arabic plural of the root ḥ-w-r 'to be white; whiteness of the eye' (Wiktionary, Wehr; cognate with Syriac ḥewwār 'white', Hebrew ḥiwwēr 'pale'). Standard lexica derive it inside Semitic. The Iranian etymology Nourai follows (VDQ:39 = the Persian translation of Jeffery, The Foreign Vocabulary of the Qurʾān, who after Tisdall suggested Pahlavi hurust 'well grown') is a minority hypothesis that would require an unexplained h > ḥ, loss of -st and reinterpretation as a plural; Wiktionary and Etymonline (houri: 'from Arabic haura, to be beautifully dark-eyed') do not accept it.
REF: VDQ:39=partial: Checked through the English original FVQ pp.117-120. Jeffery does propose hurust ('It is m… ; MAG:186=not_checked: MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.
CON: KLN=contradicts: 'houri, n., a nymph of the Moslem Paradise … F., fr. Pers. hūrī, fr. Arab. hūr, pl. of aḥw… ; LKT=contradicts: '848. Ar. ḥaurāʾ: Fem. zu aḥwar „schwarzäugig“ besonders von einer Gazelle, einem Jüngling… ; FVQ=partial: Jeffery documents the pre-Islamic Arabic use ('ʿAbīd b. al-Abraṣ, vii, 24 “And maidens lik… ; PLA=partial: Asbaghi records the derivation Nourai draws ('hūrī … ← mp. hūrast „gut gewachsen“ ← aw. hu…
------------------------------------------------------------
# 16 Persian | hŭr 1 | verdict: confirmed | 
DER: The edge is correct: Classical Persian ḥūr «حور» 'houri, heavenly maiden' and the derivatives ḥūrī «حوری» (with the Persian relational/singulative -ī), ḥūr al-ʿayn «حورالعین» (the Qurʾānic phrase taken over as a unit) and ḥūr-vash «حوروش» 'houri-like' are borrowed from Arabic ḥūr; Persian ḥūrī is in turn the source of French/English houri (1650s/1737). Only the ancestry above #15 is wrong: the word is Semitic, not from hurust.
REF: MON:1378=supports: vajehyab.com (Mo'in) s.v. حور: '[ع.] (اِ.) ۱- زن سیاه چشم. ۲- زن زیباروی'; حوری '[ع - فا.]…
CON: MON=supports: MON_part1.txt: 'احور aḥwar [ع.] (ص.) سیاه‌چشم، دارای چشمی مانند چشم آهو … مؤنث حوراء (ف. ح… ; KLN=supports: 'F., fr. Pers. hūrī, fr. Arab. hūr … The -ī in Pers. hūrī is a formative element serving t… ; LKT=supports: '… hieraus zur Bezeichnung einer reizenden Frau sp. hurí, frz. houri, ndl. engl. houri, dt…
------------------------------------------------------------
# 17 Sogdian | rwd | verdict: confirmed | 
DER: Buddhist Sogdian rwδ- (rwtt, rwt 'grows'; inf. rwδʾy), Manichaean Sogdian preterite stem rws-, and the compound pati-: ptrwδ-/ptryst- 'to grow up', are listed by Cheung 2007:193 under Proto-Iranian *Hraud 'to grow (bigger)' beside Av. raoδ-, MP rōy-/rust, Parthian rwd-, Khotanese rrud-. Sogdian δ is the regular lenition of Old Iranian *d; Nourai's 'rwd' is the same word in a δ-less transliteration. (Homographic Sogdian rwδ 'copper' < *Hrawdʰas 'red' is a different word.)
REF: SOD:344=supports: SOD_pages.txt leaf 411 (Gharib p. 344), entry 8562: 'rwδ- B, M, S — rōδ < Av. raod-; *frau…
CON: CHEUNG=supports: '*SOGDIAN: BSogd. rwð-, MSogd. rwst (pret. stem) “to grow” || (+ *pati-) SSogd. ptrwð-, CS… ; BRT=partial: AiW's '²raod- V. „wachsen“' is the Avestan member of the same equation; Bartholomae of cou… ; PHD=partial: 'rustan, roy- [lwstn', lwd-] grow' — the Middle Persian cognate with the same ð > y develo…
------------------------------------------------------------
# 18 Indo-European | leudho; leudheros | verdict: confirmed | 
DER: Pokorny 684-685 lists exactly these derivatives: leudho-/leudhi- 'Nachwuchs, Volk' (OHG liut, OE lēod, German Leute, OCS ljudьje, Lith. liaudis 'people') and leudhero- 'zum Volk gehörig, frei' (Greek ἐλεύθερος, Latin līber); modern notation *h₁léwdʰ-o-, *h₁léwdʰ-ero-. The semantic path is 'growth' → 'offspring' → 'the people (born into the community)' → 'belonging to the people, free-born (as opposed to slave)'.
REF: KLN:885=supports: KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. b…
CON: WLD=supports: p.416: '(Nachwuchs → Menge, Volk:) ahd. liut, ags. lead „Volk“, mhd. liute „Leute“'; p.417… ; IEC=supports: 'leudheros (leudhər-) “active, free; action, freedom, abandon” … WP II, 417 … Myc. and Gk.… ; AHD=partial: Watkins lists only the suffixed form '*leudh-ero- in Latin liber, free (the precise semant…
------------------------------------------------------------
# 19 Latin | liber | verdict: confirmed | 
DER: PIE *h₁léwdʰ-ero-s → Proto-Italic *louðeros → Old Latin loebesum/loebertatem (Festus; oe < *ou, intervocalic *dʰ > Italic *ð > Latin b) → Classical Latin līber 'free' (with the regular monophthongization oe > ī); de Vaan 2008:338. The same stem gives lībertās 'freedom', līberāre 'to free' and Līber (the god).
REF: none=not_checked: Nourai cites no reference for this node. Klein s.v. liberal (checked at #18): 'fr. liber, …
CON: LAT=partial: Ernout-Meillet: 'Pel. loufir “liber” et fal. loferta montrent que l'ī de liber reposerait … ; WLD=supports: 'lat. Liber, ital. Gott des Wachstums, der Zeugung, Anpflanzung (aus *loudhero-, *loufero-… ; SKT=contradicts: SKT.txt leaf 270 (p.250): 'Liberal. (F.-L.) M.E. liberal … L. līberālis, befitting a free … ; AHD=supports: 'Suffixed form *leudh-ero- in Latin liber, free (the precise semantic development is obscu…
------------------------------------------------------------
# 20 English | liberty, deliver, Latvia | verdict: disputed | 
DER: liberty: Latin lībertās (acc. lībertātem) → Old French liberte → Middle English liberte (late 14th c.) — confirmed. deliver: Latin līberāre 'to free' → Late Latin dēlīberāre 'to set free' → Old French delivrer → Middle English deliveren (c. 1200), later 'hand over' — confirmed (Etymonline, AHD leudh-). Latvia, however, has no connection to *leudh-: it is a 19th-century Latvian formation Latv-ija from the ethnonym latvis 'Lett', whose origin is unknown (Etymonline: 'of unknown origin'; Wiktionary: possibly from a river name Latava); neither Etymonline nor Wiktionary nor AHD links it to Latin līber or PIE *leudh-. Node verdict is 'disputed' because of Latvia only.
REF: none=not_checked: Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 231, s.v. deliver): 'OF.…
CON: SKT=partial: 'deliver. (F.-L.) OF. delivrer, set free. — Low L. dēlīberāre, to set free. L. dē, from; l… ; AHD=partial: The Watkins index gives 'DELIVER leudh-2', 'LIBERTY leudh-2', 'LIBERAL leudh-2', 'LIBERTIN… ; KLN=partial: 'Latvia, n. — Lit. “the country of the Letts”. See Lett and cp. lat.'; 'Lett, n., an inhab…
```


## [2026-09-04T23:30:53.268Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p311.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"ریشه همان *h₁lewdʰ- هندواروپایی آغازین است به معنی «بالیدن، برآمدن» و از آنجا «زاده، مردم»؛ پوکورنی (ص ۶۸۴–۶۸۵) آن را با مشتقاتِ leudho-/leudhi- «نسل، مردم» و leudhero- «آزاد» می‌آورد (اوستایی raoδaiti، لاتینی līber، آلمانی علیای باستان liut) و چونگ (۲۰۰۷، ص ۱۹۳) بازتاب ایرانیِ آن را *Hraud «بالیدن» می‌داند. ر آغازینِ ایرانی نتیجهٔ آمیختنِ قاعده‌مندِ *l هندواروپایی با *r در ایرانیِ آغازین است، نه ریشه‌ای جداگانه؛ برچسب دومِ نورایی، «Rei»، در پوکورنی و AHD همتایی ندارد و توضیح‌ناپذیر است. چند شاخه اصلاً به این ریشه تعلق ندارند: «روضه» (گرهٔ ۴) و «حور» (گرهٔ ۱۵) واژه‌های سامیِ اصیل‌اند، «رونق» (گرهٔ ۷) عربیِ اصیل است، و «روستاگ» و «رستم» (گره‌های ۹ و ۱۱) امروزه از واژهٔ «رود» (*srew-) گرفته می‌شوند نه از «بالیدن». یادداشت خودِ نمودار زیر گرهٔ ۴ نیز دو ریشه‌شناسی فارسیِ جایگزین را نقل می‌کند که فرهنگ‌نویسی امروزی هر دو را رد می‌کند.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"فعل اوستاییِ متأخر raoδ- (raoδaiti «می‌بالد»، وندیداد ۵٫۱۹؛ اسم مفعولِ rusta- «روییده») و اسم‌های raoδa- «بالش، بالا، هیئت» و raoδah- «رویش» بازتاب مستقیم ایرانیِ *h₁lewdʰ- اند: *l هندواروپایی در ایرانیِ آغازین r، خوشهٔ *ew به ao و *dʰ به δ بدل شده است. معنی «چهره» گسترشی ثانوی از «هیئت و نمود» است، همان راهی که «روی» فارسی پیموده (ایرانی آغازین *rauda- «نمود» < «رویش»). بارتولومه، چونگ و والده-پوکورنی همه همین را می‌گویند و ادعای نورایی درست است.\",\n\"2\": \"raoδ- اوستایی/ایرانی باستان در فارسی میانه ستاک حالِ rōy- (مانوی rwy-، پهلوی lwd-) و اسم مفعولِ rust را داده و از آنجا «رستن/روی-» فارسی نو و مصدرِ قاعده‌مندشدهٔ «روییدن» آمده است (چونگ ۲۰۰۷، ص ۱۹۳). d ایرانی باستان در میان دو واکه در فارسی میانه به y نرم شده (raoδa- > rōy) و همین y در «روییدن» دیده می‌شود، حال آنکه اسم مفعول خوشهٔ -st- را نگاه داشته است (رست، رستن). «روی» به معنی «چهره» نیز همان واژه است: از فارسی میانهٔ rōy < ایرانی آغازینِ *rauda- «رویش، نمود»، با سیر معناییِ «بالش و قامت» ← «نمود» ← «چهره». هرن، هوبشمان، مکنزی و معین همه تأیید می‌کنند و ادعای نورایی درست است.\",\n\"3\": \"«رز» به معنی «تاک، تاکستان» (با ترکیب‌های رزبان و رزبن) واژه‌ای راستین است و دنبالهٔ raz فارسی میانه (پهلوی lc)، اما هیچ منبع امروزی آن را از ریشهٔ «بالیدن» نمی‌گیرد: نه *raza- «رویش» در ایرانی باستان هست و نه «روی-/رست-» می‌تواند صورتی با -ز- بدهد. ویکی‌واژه و ادبیات ریشه‌شناسیِ یونانی و لاتینی «رز» فارسی را با یونانی ῥάξ «انگور»، لاتینی racēmus «خوشهٔ انگور» و آلبانیایی rrush در یک گروه می‌نهند، به عنوان واژه‌ای فرهنگی و سرگردان (Wanderwort) از خاستگاهی ناشناخته و احتمالاً زیرلایه‌ای. پیوند آن با «رستن» در برهان قاطع نمونهٔ ریشه‌شناسی عامیانه است؛ پس این گره را پژوهش امروزی رد می‌کند.\",\n\"4\": \"عربی «رَوْضَة» «باغ، مرغزار» (قرآن، روم ۱۵) با جمعِ «ریاض» ساختی اصیل از ریشهٔ سامیِ ر-و-ض است (راضَ «رام کردن»، روضة «مرغزاری که آب در آن جمع می‌شود») و ضادِ مطبق دارد، حال آنکه ز فارسی هرگز در عربی ض نمی‌شود («رز» فارسی می‌بایست *رَوز یا راز بدهد). ویکی‌واژه و وهر آن را عربیِ اصیل می‌دانند و «روضهٔ» فارسی را تنها فرزندِ آن می‌شمارند. با این حال بررسیِ منابع نشان داد که اصباغی (ص ۱۳۸) به‌راستی همان چیزی را می‌گوید که نورایی نقل کرده (روضه از «رز» فارسی)، و جفری نیز به پیروی از فولرس واژه را ایرانی می‌داند اما آن را از rōd پهلوی «رود» می‌گیرد؛ اَدّی شیر نیز آن را از «ریختن» گرفته است. چون فرهنگ‌نویسیِ معیارِ عربی «روضة» را درون ریشهٔ ر-و-ض نگاه می‌دارد و دو پیشنهاد ایرانی یکدیگر را نقض می‌کنند، حکم «مورد اختلاف» است و سراسر زیرشاخهٔ ۳ ← ۴ ← ۵ به این ریشه تعلق ندارد.\",\n\"5\": \"خودِ این حلقه درست است: «روضه» فارسی وام‌واژه‌ای از «روضة» عربی است (ض عربی در فارسی ز خوانده می‌شود و تاء مربوطه به -ه بدل می‌گردد)، و «ریاض» جمع مکسّرِ عربیِ آن است؛ کاربرد کلاسیکِ آن را در «روضهٔ رضوان» سعدی می‌توان دید. معنای متأخر و شیعیِ «روضه» یعنی «ذکر مصیبت کربلا» از «روضة الشهداء»ی کاشفی (سدهٔ نهم هجری) برخاسته است. تنها تبارِ بالای گرهٔ ۴ نادرست است: واژه سامی است نه هندواروپایی.\",\n\"6\": \"«رونیک» ترکیبی شفاف است از «روی» (گرهٔ ۲، از فارسی میانهٔ rōy < ایرانی آغازینِ *rauda- «نمود») و «نیک»، و در نمودار با «نیکروی» برابر نهاده شده است. نورایی برای آن هیچ منبعی نمی‌آورد؛ من نیز آن را تنها در فرهنگ‌های برخطِ امروزی («نیک‌رو، خوش‌رو، زیبارو») و در نام امروزیِ «رونیکا» یافتم، حال آنکه «نیکروی» در دهخدا هست. ساخت واژه بی‌اشکال است و جزء نخستش به‌راستی به این ریشه تعلق دارد، اما گواهی کلاسیک برای «رونیک» نیافتم و ادعای اینکه «رونق» عربی از آن آمده (گرهٔ ۷) پذیرفته نیست؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"7\": \"عربی «رَوْنَق» «زیبایی، جلا، فروغ» را ویکی‌واژه به پیروی از وهر و المعانی اسمی اصیل از ریشهٔ ر-ن-ق می‌داند (رانِق «آب زلال»، رَنَقَ/تَرَوْنَقَ «صاف و درخشان بودن») بر وزن فَوْعَل، و «رونق» فارسی را وام‌گرفته از آن می‌شمارد. سرچشمهٔ فارسیِ «رونیک» که نورایی به پیروی از اَدّی شیر (الالفاظ الفارسیة المعرَّبة، ۱۹۰۸) می‌آورد، افتادنِ توضیح‌ناپذیرِ ی و نیز ابدالِ بی‌قاعدهٔ ک به ق را لازم می‌آورد و هیچ فرهنگ امروزی آن را نپذیرفته است؛ بسیاری از اشتقاق‌های اَدّی شیر امروز مردودند. پس پژوهش امروزی این گره را رد می‌کند.\",\n\"8\": \"این حلقه درست است: «رونق» فارسی کلاسیک به معنی «فروغ، رواج و رونق کار» وامی سرراست از «رَوْنَق» عربی است و مصوت مرکبِ عربیِ aw در فارسی ow مانده است؛ معنای «رواج و کامیابی» گسترشی درون‌فارسی است و همین واژه سپس به اردو، جغتایی و کردی نیز رفته است. معین آن را با نشانِ «[ع.]» می‌آورد. تنها تبارِ بالای گرهٔ ۷ (فارسیِ «رونیک») پذیرفته نیست: واژه در اصل عربی است.\",\n\"9\": \"فارسی میانه rōstāg (پهلوی lwstʾk') «بخش، ناحیهٔ روستایی» واژه‌ای راستین و سرچشمهٔ «رُستاق» عربی، rustāqā سریانی و ṙotastak ارمنی است. اما ریشه‌شناسیِ آن ترکیبِ *rautas-tāka- «مسیر رود، ناحیهٔ رودخانه‌ای» است: از rautah-/raudah- ایرانی باستان «رود» (پارسی باستان rautah-، فارسی میانه rōd، فارسی «رود» < *hrautah- < هندواروپایی *srew- «روان بودن») به‌علاوهٔ -tāka- «دویدن، جریان» از ریشهٔ tak-/tač-؛ خوشه در فارسی میانه بی‌واک شده و rōstāg داده است، و صورت پارتیِ rōdastāg با d واژهٔ «رود» را آشکارا نشان می‌دهد. هیچ چیز آن را به «بالیدن» نمی‌پیوندد؛ مکنزی و نیبرگ صریحاً معنی «بستر رود» را نیز ثبت کرده‌اند. پس این گره رد می‌شود.\",\n\"10\": \"این حلقه درست است: rōstāg فارسی میانه در فارسی دری «روستا/روستای» شده است، با افتادن قاعده‌مندِ گاف در پسوند -āg (مانند dānāg > دانا)؛ وام‌واژهٔ عربیِ «رستاق» و گونهٔ «رستاق» فارسی صورت کهن‌تر را نگاه داشته‌اند. محدود شدن معنا از «ناحیهٔ روستایی» به «ده» تحولی درون‌فارسی است. چنان‌که در گرهٔ ۹ گفته شد، ریشه «رود» است نه «رستن». ارجاع نورایی به مان (ص ۱۱۰۳) از قضا صفحهٔ درستی است، اما مان «روستا» را زیر rūs- «فضا، جای» در کنار rūs لاتینی می‌آورد، یعنی ریشه‌شناسیِ سومی که نه «بالیدن» است و نه «رود».\",\n\"11\": \"چنین واژه‌ای در اوستا نیست و نام رستم در متون اوستایی نیامده است؛ *Raoδas-taxma- بازسازیِ پژوهشگران (یوستی، نامنامهٔ ایرانی) در پسِ Rōdstahm فارسی میانه، Rwstmy سغدی و «رستم» فارسی است، پس برچسب درست «ایرانی باستانِ بازسازی‌شده» می‌بود. تحلیل معیارِ امروزی (ویکی‌واژه، ایرانیکا، مایرهوفر و اشمیت) این ترکیب را *Rautas-taxma- «نیرومند چون رود» می‌خواند، یعنی جزء نخست همان raoδah-/rautah- «رود» (< *srew-، همان واژه‌ای که در «روستاگ» هست) و جزء دوم taxma- «دلیر، نیرومند» (ارجاع نورایی به ریشهٔ Tenk درست است). خوانش کهن‌ترِ «بالیده و نیرومند» با raoδah- «رویش» رأیی اقلیتی است که مراجع امروزی نمی‌پذیرند.\",\n\"12\": \"نام «رستم» به‌راستی دنبالهٔ همان ترکیب بازسازی‌شدهٔ گرهٔ ۱۱ است: ایرانی باستان *Rautas-taxma- > فارسی میانه Rōdstahm (پهلوی stahm «زور، نیرو» < taxma-) > «رستم» فارسی نو، با ساده شدن خوشهٔ -dst- به -st- و کوتاه شدن ō پیش از خوشه؛ صورت سغدیِ Rwstmy نشان می‌دهد که این فشردگی در دورهٔ ایرانی میانه رخ داده بود. پس خودِ این حلقه درست است، اما جزء نخست «رود» است نه «رویش» (گرهٔ ۱۱). «رستم» فردوسی که آن را از «رَستم» (رها شدم، به مناسبت زادنِ رستم به شیوهٔ رستمزاد) می‌گیرد ریشه‌شناسیِ عامیانه و شاعرانه است؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"13\": \"«hava-rd» صورتی ناممکن در اوستایی است؛ آنچه باید می‌بود hu-raoδa- است، یعنی صفت اوستاییِ متأخرِ huraoδa- «خوش‌بالا، خوش‌اندام، زیبا» (وندیداد ۳٫۲۴؛ صفت سروش در یسنا ۵۷) از hu- «خوب، نیک» (هندواروپایی *h₁su-؛ ارجاع نورایی به ریشهٔ Su 1 درست است) و raoδa- «بالش، قامت» (گرهٔ ۱). معنا و تعلق آن به این ریشه دقیقاً همان است که در جعبه آمده و تنها آوانگاری مخدوش است. اما بررسی تصویر صفحه نشان می‌دهد که کتاب خود «hava-rd» را روشن و بی‌افتادگی چاپ کرده، حال آنکه در همان ردیف جعبهٔ پهلوی «hu-rust» را درست آورده است؛ پس این خطای خودِ نورایی است نه خطای خوانشِ اسکن، و استخراج داده وفادار بوده است.\",\n\"14\": \"فارسی میانه hurust «خوش‌بالا، خوش‌ساخت» ترکیبی است از hu- «نیک» و rust، اسم مفعولِ rōy-/rustan «روییدن» (چونگ ۲۰۰۷، ص ۱۹۳؛ صورت *Hrusta- جانشین قیاسیِ *Hruzda-ی مورد انتظار است). پس این واژه همتای فارسیِ میانهٔ huraoδa- اوستایی (گرهٔ ۱۳) است، با این تفاوت که بر اسم مفعول ساخته شده نه بر اسمِ raoδa-، اما از همان ریشه و با همان معنا. مکنزی آن را ثبت کرده و جفری نیز hurust پهلوی «خوش‌بالا» را می‌آورد؛ ادعای نورایی در این گره درست است.\",\n\"15\": \"عربی «حُور» جمعِ «أحور» (مذکر) و «حَوْراء» (مؤنث) است به معنی «کسی که سیاهی و سپیدیِ چشمش شدت تضاد دارد»، و در ترکیب قرآنیِ «حورٌ عینٌ» (دخان ۵۴، طور ۲۰، واقعه ۲۲) آمده است؛ این جمعی قاعده‌مند از ریشهٔ سامیِ ح-و-ر «سپید بودن» است و هم‌ریشهٔ سریانی ḥewwār «سپید» و عبری ḥiwwēr «رنگ‌پریده» است. فرهنگ‌های معیار آن را درون سامی نگاه می‌دارند. ریشه‌شناسیِ ایرانی که نورایی به پیروی از جفری (و پیش از او تیزدال) می‌آورد — یعنی گرفتن آن از hurust پهلوی — فرضی اقلیتی است که ابدالِ توضیح‌ناپذیرِ ه به ح، افتادن -ست و بازتفسیرِ واژه به عنوان جمع را لازم می‌آورد؛ ویکی‌واژه و اتیمآنلاین آن را نمی‌پذیرند و لوکوچ نیز صریحاً مخالف است. پس پژوهش امروزی این گره را رد می‌کند.\",\n\"16\": \"این حلقه درست است: «حور» فارسی و مشتقاتش «حوری» (با یاء نسبت/وحدتِ فارسی)، «حورالعین» (که ترکیب قرآنی را یکجا گرفته) و «حوروش» همه از «حور» عربی وام گرفته شده‌اند، و «حوری» فارسی خود سرچشمهٔ houri فرانسوی و انگلیسی (سده‌های هفدهم و هجدهم) است — چنان‌که کلاین تصریح می‌کند که یاء در hūrī فارسی است. تنها تبارِ بالای گرهٔ ۱۵ نادرست است: واژه سامی است نه برگرفته از hurust.\",\n\"17\": \"سغدیِ بودایی rwδ- («می‌روید»؛ مصدر rwδʾy)، ستاک گذشتهٔ مانویِ rws- و ترکیبِ ptrwδ-/ptryst- «برآمدن و بالیدن» را چونگ (۲۰۰۷، ص ۱۹۳) زیر ایرانی آغازینِ *Hraud «بالیدن» می‌آورد، در کنار raoδ- اوستایی، rōy-/rust فارسی میانه، rwd- پارتی و rrud- ختنی. δ سغدی نرم‌شدگیِ قاعده‌مندِ *d ایرانی باستان است و ضبطِ «rwd»ی نورایی همان واژه است بدون نشانِ δ. (هم‌نگاشتِ سغدیِ rwδ «مس» < *Hrawdʰas «سرخ» واژهٔ دیگری است.) قریب و چونگ هر دو تأیید می‌کنند و ادعای نورایی درست است.\",\n\"18\": \"پوکورنی (ص ۶۸۴–۶۸۵) دقیقاً همین دو مشتق را می‌آورد: leudho-/leudhi- «نسل، مردم» (آلمانی علیای باستان liut، انگلیسی باستان lēod، آلمانی Leute، اسلاوی کهن ljudьje، لیتوانیایی liaudis) و leudhero- «متعلق به مردم، آزاد» (یونانی ἐλεύθερος، لاتینی līber)؛ در نگارش امروزی *h₁léwdʰ-o- و *h₁léwdʰ-ero-. سیر معنایی روشن است: «رویش» ← «زاد و نسل» ← «مردمِ زادهٔ آن جامعه» ← «متعلق به مردم، آزادزاده در برابر برده». ادعای نورایی درست است.\",\n\"19\": \"هندواروپایی *h₁léwdʰ-ero-s در ایتالیکیِ آغازین *louðeros شده، در لاتینیِ کهن به صورت loebesum/loebertatem گواه دارد (oe از *ou، و *dʰ میان‌واکه‌ای از راه *ð ایتالیکی در لاتینی b) و سپس با یک‌آوایی شدنِ قاعده‌مندِ oe به ī صورت کلاسیکِ līber «آزاد» را داده است (دِ ڤان ۲۰۰۸، ص ۳۳۸). از همین ستاک lībertās «آزادی»، līberāre «آزاد کردن» و نام خدای Līber ساخته شده است. ادعای نورایی درست است.\",\n\"20\": \"دو واژه از سه واژهٔ این جعبه بی‌اشکال‌اند: liberty از لاتینی lībertātem از راه فرانسوی کهن liberte به انگلیسی میانه (اواخر سدهٔ چهاردهم) رسیده، و deliver از līberāre و لاتینیِ متأخر dēlīberāre «رها کردن» از راه فرانسوی کهن delivrer (حدود ۱۲۰۰، و بعدها به معنی «تحویل دادن»). اما Latvia هیچ پیوندی با این ریشه ندارد: ساختی لتونیایی از سدهٔ نوزدهم است (Latv-ija) بر پایهٔ نام قومیِ latvis که خاستگاهش ناشناخته است (اتیمآنلاین: «از خاستگاه نامعلوم»؛ ویکی‌واژه: شاید از نام رودِ Latava)؛ نه اتیمآنلاین، نه ویکی‌واژه و نه AHD آن را به līber لاتینی یا *leudh- نمی‌بندند. حکم این گره تنها به سبب همین یک واژه «مورد اختلاف» است.\"\n}\n}\n}\nEOF\npython3 apply_fa.py 311 p311.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-311.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-311.json && tail -c1 /home/sfmqrb/git/rishe/data/verification/page-311.json | xxd -p",
 "description": "Apply Persian to page 311"
}
```


### [2026-09-04T23:30:56.308Z] TOOL RESULT

```
ok 311
JSON_OK
 data/verification/page-311.json | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
7d
```


## [2026-09-04T23:31:00.200Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/dump.py 345 2>&1 | head -220",
 "description": "Dump page 345"
}
```


### [2026-09-04T23:31:02.088Z] TOOL RESULT

```
##########################################################################################
PAGE 345 book 315
================================================================================
ENTRY 0 | root: Murvârît | verdict: confirmed | modern: Middle Persian murwārīd (Book Pahlavi mwlwʾlyt', Manichaean mwrwʾryd) 'pearl' < Old Persian *margārīta- < Proto-Iranian *mŕ̥ga-ahri-ita- 'born of the (sea-)bird's shell, oyster'
NOTE: Pahlavi murwārīd 'pearl' is real (MacKenzie 1971/1986; Nourai's -t reflects the Pahlavi spelling -yt'); gloss 'small pearl' is slightly narrow — MacKenzie simply 'pearl'. Modern scholarship (Wiktionary, Beekes s.v. μαργαρίτης, Encyclopaedia Iranica 'Greek loanwords in Middle Iranian') agrees the Iranian word is the SOURCE and Greek margaritēs the loan, so the chart's direction is right and the Borhan-e Qate' note (Persian from Greek) is rejected. One caveat: Greek margaritēs is already in Theophrastus (4th c. BCE), so the actual donor was Old Iranian *margārīta-, not Middle Persian proper; and the Aramaic/Arabic marjān branch runs through Greek (Syriac margānīṯā < Greek), not straight from Pahlavi. English margarine, Margarita and Rita do not pass through Old French.
ROOTREF: PLA:247=supports ; FVQ:261=supports
------------------------------------------------------------
# 1 Persian | morvârîd | verdict: confirmed | 
DER: New Persian morvārīd مروارید continues Middle Persian murwārīd (mwlwʾlyt' / mwrwʾryd) unchanged apart from vowel adjustment; Parthian morγārīd, Sogdian mrγʾrt, Khotanese mrāhe are cognates, all from Old Iranian *margārīta-, which Beekes analyses as *mŕ̥ga-ahri-ita- 'oyster', literally 'born from the shell of a (sea-)bird' (*mr̥ga- 'bird', cf. Av. mərəγa-). Attested throughout classical poetry (Hafez, 14th c., in the chart). The NOTE that Borhan-e Qate' derives it from Greek is the reverse of the modern consensus: the Greek word is the borrowing (Wiktionary; Encyclopaedia Iranica 'Greece xiii': 'most probably not borrowed from Greek margarítēs, but the borrowing may rather have functioned the other way around').
REF: BQT:1997=partial: BQT_v4_pages.txt pdf page 80 = printed p. 1997, Mo'in's footnote 5 to مروارید: «مروارید ..… ; FVQ:261=supports: FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only … ; KGW:112=not_checked: KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books prev…
CON: HUB=supports: HUB.txt leaf 258 (Persische Studien p. 248, §140 'Für ap. g erscheint v in:'): "marvarīd '… ; PHD=supports: PHD.txt leaf 80 (printed p. 59), s.v. morwārīd: "morwārīd [mwlw'lyt' | M mwrwryd, N ~] pea… ; MON=partial: Mo'in has the headword «مروارید» with a long mineralogical description ('جسم جامد و کروی ش… ; HRN=silent: Horn's Grundriss has no numbered entry for marvārīd; the only m-r-w hit is no. ~1024 on mu…
------------------------------------------------------------
# 2 Aramaic |  | verdict: plausible | 
DER: Pass-through node: the Aramaic word is Jewish Aramaic מַרְגָּנִיתָא / Syriac ܡܪܓܢܝܬܐ margānīṯā 'pearl' (with -n- for the Greek/Iranian -r-; dissimilation r…r > r…n). Wiktionary derives it from Greek μαργαρίτης, which in turn is the Iranian loan, so the ultimate source is the Iranian word as the chart says, but the immediate parent should be Greek rather than Pahlavi (a direct Iranian → Aramaic borrowing in the Achaemenid/Parthian period is not excluded but is not what the sources give).
REF: FVQ:261=supports: FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only …
CON: PLA=supports: PLA_pages.txt leaf 262 = Asbaghi, Persische Lehnwörter im Arabischen p. 247, s.v. marǧān: … ; BQT=supports: BQT_v4_pages.txt pdf page 64 = printed p. 1981, Mo'in's footnote 10 to مرجان: «مرجان کلمهٔ… ; AFM=partial: AFM_pages.txt leaf 145 (≈ Addi Shir p. 144, s.v. مرجان; the file has no printed-page tags)… ; AFA=silent: Fraenkel's Aramaic and Arabic are in unOCR'd script and no German gloss for 'Perle'/'Koral…
------------------------------------------------------------
# 3 Arabic | mardjân | verdict: confirmed | 
DER: Arabic marjān مَرْجَان 'small pearls; coral' (collective; unit noun marjāna) is borrowed from Classical Syriac margān 'pearl-like' / margānīṯā 'pearl' (Wiktionary), with Syriac g > Arabic j regularly. It is Qur'anic (55:22, 55:58 lu'lu' wa-l-marjān), where commentators already waver between 'small pearls' and 'coral' — the source of the double gloss. So the edge Aramaic → Arabic is confirmed.
REF: FVQ:261=supports: FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only … ; PLA:247=supports: PLA_pages.txt leaf 262 = Asbaghi, Persische Lehnwörter im Arabischen p. 247, s.v. marǧān: …
CON: LKT=partial: LKT.txt leaf 140 (Lokotsch p. 114), No. 1416: "[Ar. margān.] 'Koralle' [aus gr. μαργαρίτης… ; AFM=supports: AFM_pages.txt leaf 145 (≈ Addi Shir p. 144, s.v. مرجان; the file has no printed-page tags)… ; MON=supports: MON_part2.txt line 52627 s.v. مرجان: «مرجان: [ع. مح. مروارید، بسد]» — Mo'in tags the word … ; KLN=partial: Klein: "Morgana itself derives fr. Arab. marjān, 'pearl', used also as a female name … See…
------------------------------------------------------------
# 4 Persian | marjân | verdict: confirmed | 
DER: Persian marjān مرجان 'coral' (also the female name Marjan) is borrowed from Arabic marjān, keeping only the 'coral' sense (Wiktionary: Persian and Ottoman Turkish 'adopted the Arabic term to mean coral specifically'); attested in Hafez alongside lu'lu' 'pearl' as in the chart's line. This is an Iranian → Greek → Aramaic → Arabic → Persian round trip, so morvārīd and marjān are doublets in Persian.
REF: BQT:1981=supports: BQT_v4_pages.txt pdf page 64 = printed p. 1981, Mo'in's footnote 10 to مرجان: «مرجان کلمهٔ…
CON: MON=supports: MON_part2.txt line 52627 s.v. مرجان: «مرجان: [ع. مح. مروارید، بسد]» — Mo'in tags the word … ; BQT=supports: Borhān's own article: «مرجان … و درعربی جوهرست سرخ» ('in Arabic it is a red gem') and, on … ; LKT=partial: LKT.txt leaf 140 (Lokotsch p. 114), No. 1416: "[Ar. margān.] 'Koralle' [aus gr. μαργαρίτης…
------------------------------------------------------------
# 5 Greek | margarites | verdict: confirmed | 
DER: Greek μαργαρίτης (λίθος) margarítēs 'pearl' (first in Theophrastus, De lapidibus 36, 4th c. BCE; also μάργαρον) is, per Wiktionary/Beekes, a loan from Indo-Iranian, specifically the Old Iranian ancestor (*margārīta-) of Middle Persian murwārīd, with the Greek agent/material suffix -ίτης substituted for the Iranian ending; etymonline: 'from some Oriental language, most likely Iranian; cf. Middle Persian marvarit'. The edge is right in direction; only the label 'Pahlavi' for the donor is anachronistic (the loan predates Middle Persian).
REF: AHD:1527=supports: AHD_watkins1985.txt line 725: '[margarītēs. Pearl. Greek noun of Oriental origin (probably… ; KGW:111=not_checked: KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books prev… ; FVQ:261=supports: FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only …
CON: KLN=contradicts: KLN_1966.txt leaf 504, s.v. margarite: "ME., fr. OF. margarite (F. marguerite), fr. L. mar… ; SKT=supports: SKT.txt leaf 289 (Skeat p. 269), s.v. Magpie: "Mag is short for Magot, a familiar form of … ; WEB=partial: WEB_vol1.txt line 112833, s.v. margarite: "[L. margarita; Gr. margarítēs, a pearl.] 1. a p… ; POK=silent: Pokorny's IEW has no entry for margarítēs — consistent with the word being a non-IE (Orien…
------------------------------------------------------------
# 6 Latin |  | verdict: confirmed | 
DER: Pass-through node: Latin margarīta 'pearl' (Cicero, Pliny; Vulgate Matt. 13:45–46 'pretiosa margarita'), a direct loan of Greek margarítēs with the Greek masculine -ítēs re-shaped as a Latin 1st-declension feminine -īta; Late Latin also as the female name Margarita.
REF: none=not_checked: Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 504, s.v. margarite): 'M…
CON: LAT=supports: LAT.txt leaf 707 (Ernout–Meillet p. 689), s.v. margarita: "margarita, -ae (-tum n.) f.: pe… ; WEB=supports: WEB_vol1.txt line 112833, s.v. margarite: "[L. margarita; Gr. margarítēs, a pearl.] 1. a p… ; LEW=silent: The local Walde LEW scan is a 305-leaf partial whose OCR yields no dictionary entries at a…
------------------------------------------------------------
# 7 Old French |  | verdict: confirmed | 
DER: Pass-through node: Old French margarite / marguerite 'pearl' and the name Margarete/Marguerite (12th–13th c.) from Latin margarīta (regular -a > -e, Latin g kept before a); Old French is the channel for English margarite, Margaret and Margery, but not for margarine, Margarita or Rita (see node 8).
REF: none=not_checked: Nourai cites no reference for this node. Klein (KLN_1966.txt leaf 504, s.v. margarite/Marg…
CON: SKT=supports: SKT.txt leaf 289 (Skeat p. 269), s.v. Magpie: "Mag is short for Magot, a familiar form of … ; WEB=partial: Webster goes straight from Latin margarita to English margarite and does not name the Old … ; FSD=silent: Funk & Wagnalls has no margarite/marguerite entry in the OCR; the only hits are 'Margarita…
------------------------------------------------------------
# 8 English | margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita | verdict: confirmed | 
DER: All seven go back to Greek margarítēs/Latin margarīta, but by different routes: margarite — Middle English 'pearl' (obsolete) from Old French margarite; the modern mineral sense (a calcium mica, 1820s) is a learned re-use with -ite. margarine — French margarine, coined by Chevreul (1813, acide margarique 'pearly acid', for the lustre of the crystals) from Greek margarítēs, then Mège-Mouriès' butter substitute (1869), English 1873: Greek → French → English, no Old French/Latin stage. Margaret — c. 1300 from Old French Margaret (Fr. Marguerite) < Late Latin Margarita. Marjorie — variant of Margery, the medieval vernacular (Old French Margerie) form of Margaret. Margarita — the Latin/Spanish form of the name (and the cocktail, from Spanish). Maggie — English pet form of Margaret; Rita — Spanish/Italian aphetic short form of Margarita/Margherita. So the chart's single Old French pass-through is right for margarite/Margaret/Marjorie/Maggie and only schematic for margarine, Margarita and Rita.
REF: none=not_checked: Nourai cites no reference for this node. AHD_watkins1985.txt line 725 lists MARGARIC, MARG…
CON: WEB=supports: WEB_vol1.txt line 112833, s.v. margarite: "[L. margarita; Gr. margarítēs, a pearl.] 1. a p… ; SKT=partial: SKT.txt leaf 289 (Skeat p. 269), s.v. Magpie: "Mag is short for Magot, a familiar form of … ; FSD=silent: No margarite or Margaret entry surfaces in the Funk & Wagnalls OCR; only 'oleomargarine' (…
================================================================================
ENTRY 2 | root: M.v.t | verdict: confirmed | modern: Proto-Semitic *mawt- 'death', root m-w-t 'to die' (Arabic māta, yamūtu; AHD Semitic roots mwt)
NOTE: The root is real (Proto-Semitic *mawt-; Akk. mūtu, Heb. māweṯ, Aram. mawtā, Ar. mawt) and is Common Semitic rather than specifically 'Arabic', though the Arabic reflex is what feeds Persian and Europe. The chart's two European branches diverge from modern scholarship: (a) Latin mattus 'drunk, sodden' cannot come from Arabic māt — it is attested in Petronius (1st c. CE) and is derived by Pokorny 694, de Vaan and Wiktionary from *maditus (madēre 'be wet'), PIE *meh₂d-; Nourai's own NOTE records this and modern scholarship sides with Pokorny/AHD; (b) the chess word French mat / échec et mat does come from Persian šāh māt via Arabic, but not through Latin mattus as drawn (its parent should be node 2/Arabic). Also, the māt of šāh māt is by Wiktionary's account native Persian 'stunned, at a loss', reinterpreted in Arabic as māta 'he died', so the whole Persian mât node sits awkwardly under an Arabic root. Spanish matar is of disputed origin (Latin mactāre or mattus preferred; Arabic/Persian māt is a competing minority view).
ROOTREF: FVA:384=not_checked ; KLN:946=supports
------------------------------------------------------------
# 1 Arabic | maot | verdict: confirmed | 
DER: Arabic mawt مَوْت 'death' is the verbal noun (maṣdar) of the hollow verb māta / yamūtu 'to die', root m-w-t, from Proto-Semitic *mawt- (Wiktionary; cognates Akk. mūtu, Heb. māweṯ, Syr. mawtā). 'maot' is simply Nourai's rendering of mawt (aw diphthong).
REF: FVA:387=not_checked: FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json).
CON: SKT=supports: SKT.txt leaf 298 (Skeat p. 278), s.v. Mate (2), to check-mate, confound. (Pers. & Arab.): … ; LKT=supports: LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: "Ar. māt(a): 'Er ist gestorben, tot'; als Fa… ; FSD=supports: FSD_vol1.txt leaf 511 (printed p. 457), s.v. Checkmate, n.: "The final position in a game … ; FVQ=silent: No entry: mawt is native Arabic, not a Qur'ānic foreign word.
------------------------------------------------------------
# 2 Persian | mawt, mowt; mayyet; mât; kîš-mât | verdict: plausible | 
DER: mawt/mowt موت 'death' — borrowed from Arabic mawt, Iranian pronunciation mowt (Wiktionary); mamāt ممات is the Arabic maṣdar mīmī of the same verb, also borrowed: confirmed. mayyet میّت 'dead person' — Arabic mayyit, a CaCīC adjective of m-w-t (*mawīt > *mayīt > mayyit by assimilation), borrowed as a noun into Persian: confirmed. māt مات 'dead, dull; stunned, confused' — Wiktionary gives two views: Arabic māta 'he died' (the traditional one, Nourai's) or a native word connected with Sanskrit/Iranian 'measured, traversed', with the meaning 'stunned' reinforced by the chess use; unresolved. kīš-māt / šāh-māt کیش مات 'checkmate' — Wiktionary analyses šāh-māt as Persian 'the king is stunned/helpless', with Arabic speakers re-etymologising māt as 'died' before the phrase reached Europe; Barnhart and etymonline give the same alternative. So the Arabic derivation of māt/šāh-māt is the classical account but not the only modern one; node verdict follows the weakest word.
REF: FVA:387=not_checked: FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json). ; MON:3678,4421=supports: vajehyab.com (Mo'in) s.v. موت: '(مَ) [ع.] (اِ.) مرگ' (tagged Arabic; archived https://vaje…
CON: MON=supports: MON_part2.txt line 67676, s.v. موت: «موت: [ع.] (اِ.) مرگ» ('Arabic, noun, death'), with th… ; BQT=silent: BQT_v4_pages.txt pdf pages 15-16 = printed pp. 1932-1933 (the میم+الف bayān, which runs ما… ; SKT=partial: Skeat records precisely the Persian sense the chart gives māt: "Hence Turk. and Pers. mat,…
------------------------------------------------------------
# 3 Latin | mattus | verdict: disputed | 
DER: Latin mattus (also mātus) 'drunk, maudlin; sodden, dull' is attested in Petronius (Satyricon 41, 1st c. CE) — six centuries before any Arabic contact — so it cannot derive from Arabic/Persian māt. The standard etymology (Pokorny IEW 694 s.v. mad-, de Vaan, Wiktionary) is *maditus 'wetted' (past participle of madēre 'to be wet, be drunk', PIE *meh₂d-, cf. Skt. mattá- 'drunk') with syncope and assimilation -dt- > -tt-. Nourai's own NOTE ('POK:694 derives mattus from Mad: wet') records the correct view; modern scholarship is unanimous on Pokorny's side, and Nourai's FSD (Funk & Wagnalls) source is superseded. The parent edge Persian māt → Latin mattus is therefore rejected.
REF: FSD:1526=partial: FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly … ; POK:694=contradicts: POK_02.txt leaf 355 (IEW pp. 694-695), s.v. mad-: 'naß, triefen; auch von Fett triefen, vo…
CON: WLD=contradicts: WLD_Bd2_pages.txt leaf 236 (Walde–Pokorny Bd. II p. 231), s.v. mad- 'naß, triefen': "Lat. … ; LAT=contradicts: LAT.txt leaf 713 (Ernout–Meillet p. 695), s.v. matus: "matus, -a, -um: ivre. Mot vulgaire … ; AHD=silent: AHD_watkins1985.txt line 708, root mad-: "mad-. Moist, wet; also refers to various qualiti… ; LEW=silent: The local Walde LEW scan is a 305-leaf partial with unusable OCR (no dictionary entries re…
------------------------------------------------------------
# 4 French | mat | verdict: plausible | 
DER: French mat 'matte, dull, without lustre' continues Old French mat 'beaten down, withered, dejected; dull' (12th c.), which Wiktionary and TLF derive from Latin mattus 'sodden, dull' — so the edge Latin mattus → French mat is the majority view and is right as drawn; etymonline adds the alternative that the Old French adjective is a transferred use of chess mat 'checkmated' (from Arabic šāh māt), in which case this word would after all descend from node 2 (but not through Latin). Either way it does not go back to Arabic through Latin.
REF: FSD:1526=supports: FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly …
CON: WEB=contradicts: WEB_vol1.txt line 113629, s.v. mat, a.: "[... OFr. mat, defeated, from Ar. māt.] not gloss… ; LAT=partial: Ernout–Meillet, after deriving mattus from *maditus, add "Le rapprochement de l'ital. matt… ; DEV=supports: Devic: "Mat, adjectif, au sens de terne, vient du mat des échecs. « Dans les anciens auteu…
------------------------------------------------------------
# 5 English | mat 1 | verdict: confirmed | 
DER: English mat/matte 'dull, lustreless' (1640s) is borrowed from French mat; the spelling matte was not standardised until the 20th c. AHD:805 (the chart's NOTE) refers it to the IE root mad- 'wet' via Latin mattus — which, as with node 3, is the modern consensus; the French → English edge itself is uncontroversial.
REF: FSD:526=not_found: FSD_vol1.txt: printed p. 526 (leaf ~575) is in the C's ('coerce' etc.) and has no 'mat'; t… ; AHD:805=contradicts: AHD online s.v. mat 2 (archived, https://ahdictionary.com/word/search.html?q=mat): '[From …
CON: WEB=supports: WEB_vol1.txt line 113629, s.v. mat, a.: "[... OFr. mat, defeated, from Ar. māt.] not gloss… ; KLN=supports: Klein: "mat, adj., dull. — F., dull, lusterless, unpolished, fr. OF. mat, defeated, afflic… ; SKT=silent: Skeat's only 'Mat' headword is the floor-covering: "Mat. (L.) M.E. matte. A.S. — L. matta …
------------------------------------------------------------
# 6 French | mat; e'chec et mat | verdict: disputed | 
DER: Old French mat 'checkmated, defeated' (12th c.; verb mater 'to checkmate, overcome') and the phrase eschec mat > Modern French échec et mat are the chess term, from Arabic šāh māt (Persian šāh māt 'the king is stunned/helpless', re-read in Arabic as 'the king is dead'), which reached the Romance languages with chess itself through Muslim Spain and Sicily in the 10th–11th c. (Spanish jaque mate, Italian scacco matto, Medieval Latin scaccum mattum). The chart draws this French mat from Latin mattus 'drunk' — that edge is wrong: the checkmate word is an Arabic/Persian loan and should hang directly from node 2 (Persian/Arabic māt), as Nourai's own NOTE ('debatable paths') half-concedes. Its ultimate Semitic vs. Persian identity is the open question discussed at node 2.
REF: PHN:257=supports: PHN.txt leaf 288 (Pihan p. 257): 'MAT, adj. m. (p.) [māt] défait, réduit à l'extrémité. — … ; DEV:159=supports: DEV.txt leaf 192 (Devic p. 159): 'Mat. Terme du jeu des échecs. (Voy. Échec.) Mat, adjecti…
CON: LKT=supports: LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: "Ar. māt(a): 'Er ist gestorben, tot'; als Fa… ; SKT=supports: SKT.txt leaf 98 (Skeat p. 78), s.v. Check: "— O.F. eschec, 'a check at chess-play,' Cot. —… ; LAM=partial: LAM.txt leaf 161 (Lammens p. 104), s.v. Échecs: "L'expression échec et mat est une altérat…
------------------------------------------------------------
# 7 English | mate 2; checkmate | verdict: confirmed | 
DER: English mate (v.2) 'to checkmate; to overcome, confound' (c. 1300) from Old French mater 'to checkmate, defeat' (< mat); mate (n.2) 'checkmate' likewise c. 1300 from Old French mat; checkmate (mid-14th c.) from Old French eschec mat, ultimately Arabic šāh māt. The figurative 'to thwart' sense is late-14th-c. AHD Semitic roots mwt lists exactly these two English derivatives.
REF: LKT:115=supports: LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: 'Ar. māt(a): Er ist gestorben, tot; als Fach… ; KLN:946=supports: KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj.…
CON: SKT=supports: SKT.txt leaf 298 (Skeat p. 278), s.v. Mate (2), to check-mate, confound. (Pers. & Arab.): … ; FSD=supports: FSD_vol1.txt leaf 511 (printed p. 457), s.v. Checkmate, n.: "The final position in a game … ; WEB=partial: Webster defines checkmate n./interj./v.t. ('in chess, to place in check … hence, to arrest…
------------------------------------------------------------
# 8 Spanish | matar; matador | verdict: plausible | 
DER: Spanish matar 'to kill' (also Portuguese, Catalan) is of disputed origin. Wiktionary: 'most likely from Latin mactāre (through a Vulgar Latin *mattāre)', alternatively from Late Latin mattus 'drunk, stupefied' (*mattāre 'to stun'), or influenced by Arabic māta 'to die'; RAE likewise prefers Vulgar Latin *mattare < mattus. Etymonline notes the phonological difficulty of mactāre (expected *mechar) and gives Arabic māta (borrowed from Persian māt) as the alternative — the view Klein (KLN:946, Nourai's source) adopts and Corominas discusses via the chess word. So the Arabic derivation is a real scholarly option but not the preferred one. matador 'killer; the bullfighter who kills the bull' is transparently matar + agent suffix -dor (Latin -tōrem): confirmed as a derivative.
REF: KLN:946=supports: KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj.…
CON: SKT=contradicts: SKT.txt leaf 298 (Skeat p. 278), s.v. Matador: "Matador, the slayer of the bull in bull-fi… ; WEB=contradicts: WEB_vol1.txt line 113638, s.v. matador: "[Sp., a murderer, slayer, from matar, to kill, fr… ; FSD=contradicts: FSD_vol3.txt leaf ~15845 region, s.v. matador (OCR badly broken): the etymology bracket re… ; LKT=supports: Lokotsch expressly rejects the Latin route: "Dazu die Vb. it. mattare, frz. mater, prov. k…
------------------------------------------------------------
# 9 French | matador | verdict: confirmed | 
DER: French matador is borrowed from Spanish matador in the late 17th–18th c. with the bullfighting vocabulary (Wiktionary: 'Borrowed from Spanish matador'); form unchanged.
REF: MON:3678=supports: vajehyab.com (Mo'in) s.v. ماتادور: '(دُ) [فر.] (اِ.) کسی که در میدان عمومی با گاو مبارزه م…
CON: PHN=silent: Pihan's dictionary of French words from Arabic, Persian and Turkish has no MATADOR article… ; DEV=silent: Devic likewise has no matador entry; his Mat (leaf 192, p. 159) is the chess adjective onl… ; LKT=partial: Lokotsch's international list under Ar. māt(a) includes 'frz. mater' and 'sp. pg. matar tö…
------------------------------------------------------------
# 10 Persian | mâtâdor | verdict: plausible | 
DER: Persian mātādor ماتادور (the chart's spelling ماتادُر marks the short o) is a 20th-c. loan; Wiktionary labels it 'borrowed from Spanish matador', whereas Nourai (following Mo'in, MON:3678) routes it through French, which was the usual channel for European words into Persian in that period and is phonetically indistinguishable here. Both routes are compatible; the immediate donor cannot be decided from the form.
REF: MON:3678=supports: vajehyab.com (Mo'in) s.v. ماتادور [فر.] 'گاوباز' — French → Persian as drawn. Archived htt…
CON: MON=silent: The 2-vol Adena abridgement of Mo'in on disk has no ماتادور headword; the entry Nourai cit… ; BQT=silent: Borhān-e Qāṭeʿ (1652, ed. Mo'in 1963) is a dictionary of classical Persian and has no 20th… ; ARY=silent: Aryanpur's Indo-European roots dictionary has no matador entry (its MAT- index lines are a…
------------------------------------------------------------
# 11 English | matador | verdict: confirmed | 
DER: English matador (1670s) is borrowed directly from Spanish matador 'killer', agent noun of matar; also used from 1730s for the top trump cards in ombre/quadrille (Spanish card games).
REF: KLN:946=supports: KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj.…
CON: SKT=supports: SKT.txt leaf 298 (Skeat p. 278), s.v. Matador: "Matador, the slayer of the bull in bull-fi… ; WEB=supports: WEB_vol1.txt line 113638, s.v. matador: "[Sp., a murderer, slayer, from matar, to kill, fr… ; FSD=supports: FSD_vol3.txt leaf ~15845 region, s.v. matador (OCR badly broken): the etymology bracket re…
```


## [2026-09-04T23:33:36.954Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > p345.json <<'EOF'\n{\n\"entry\": {\n\"0\": \"«مروارید» فارسی میانه (پهلوی کتابی mwlwʾlyt'، مانوی mwrwʾryd) واژه‌ای راستین است (مکنزی) و ضبطِ -t نورایی همان املای پهلوی است؛ تنها معنایی که او می‌دهد («مروارید خرد») اندکی تنگ است، چون مکنزی تنها «مروارید» می‌نویسد. پژوهش امروزی (ویکی‌واژه، بیکس ذیل μαργαρίτης، دانشنامهٔ ایرانیکا) هم‌داستان است که واژهٔ ایرانی سرچشمه است و margarítēs یونانی وام‌واژه، پس جهتِ پیکانِ نمودار درست است و آنچه در برهان قاطع آمده (فارسی از یونانی) پذیرفته نیست. یک تذکر: margarítēs یونانی همان در تئوفراستوس (سدهٔ چهارم پیش از میلاد) گواه دارد، پس وام‌دهنده در واقع ایرانی باستانِ *margārīta- بوده نه فارسی میانه؛ و شاخهٔ آرامی/عربیِ «مرجان» از راه یونانی می‌گذرد نه یکراست از پهلوی. افزون بر این margarine و Margarita و Rita از فرانسویِ کهن نگذشته‌اند.\",\n\"2\": \"ریشه اصیل است — سامیِ آغازینِ *mawt- «مرگ» (اکدی mūtu، عبری māweṯ، آرامی mawtā، عربی موت) — و مشترکِ سامی است نه به‌خصوص «عربی»، هرچند بازتاب عربی است که به فارسی و اروپا خوراک داده است. اما دو شاخهٔ اروپاییِ نمودار با پژوهش امروزی نمی‌خواند: نخست، لاتینی mattus «مست، خیس و کرخت» نمی‌تواند از «مات» عربی بیاید، چون در ساتیریکونِ پترونیوس (سدهٔ نخست میلادی) گواه دارد و پوکورنی (ص ۶۹۴)، دِ ڤان و ویکی‌واژه آن را از *maditus (از madēre «خیس بودن»، هندواروپایی *meh₂d-) می‌گیرند — و خودِ یادداشت نورایی این را نقل کرده است. دوم، واژهٔ شطرنجیِ فرانسویِ mat و ترکیب échec et mat به‌راستی از «شاه مات» فارسی از راه عربی آمده، اما نه از mattus لاتینی چنان‌که نمودار می‌کشد؛ پدرِ آن باید گرهٔ ۲ باشد. افزون بر این، «مات» در «شاه مات» بنا بر ویکی‌واژه واژه‌ای فارسیِ اصیل به معنی «حیران، درمانده» است که در عربی به «مات = مرد» بازتفسیر شده، پس جای گرهٔ فارسیِ «مات» زیر ریشه‌ای عربی ناهموار است. سرچشمهٔ matar اسپانیایی نیز محل اختلاف است.\"\n},\n\"nodes\": {\n\"0\": {\n\"1\": \"«مروارید» فارسی نو دنبالهٔ بی‌واسطهٔ murwārīd فارسی میانه است و جز اندکی تعدیلِ واکه دگرگونی نیافته؛ هم‌ریشه‌های آن پارتی morγārīd، سغدی mrγʾrt و ختنی mrāhe است و همه از ایرانی باستانِ *margārīta- می‌آیند که بیکس آن را *mŕ̥ga-ahri-ita- «زادهٔ صدفِ مرغِ دریایی» تحلیل می‌کند (*mr̥ga- «مرغ»، اوستایی mərəγa-). واژه در سراسر شعر کلاسیک، از جمله در بیت حافظِ نمودار، گواه دارد. یادداشتی که برهان قاطع آن را از یونانی می‌گیرد وارونهٔ اجماع امروزی است: ایرانیکا تصریح می‌کند که «به احتمال بسیار از margarítēs یونانی وام گرفته نشده، بلکه وام‌گیری در جهت عکس بوده است». پس ادعای نورایی درست است.\",\n\"2\": \"این جعبهٔ گذرا نمایندهٔ صورت آرامی است: آرامیِ یهودی מרגניתא / سریانی margānīṯā «مروارید» که در آن -n- جانشین -r- شده است (ناهمگونیِ r…r > r…n). ویکی‌واژه آن را از یونانی μαργαρίτης می‌گیرد و یونانی خود وام‌واژه‌ای ایرانی است، پس سرچشمهٔ نهایی همان است که نمودار می‌گوید، اما پدرِ بی‌واسطهٔ آن می‌بایست یونانی می‌بود نه پهلوی. وام‌گیریِ مستقیم ایرانی ← آرامی در دورهٔ هخامنشی یا اشکانی ناممکن نیست، اما منابع چنین چیزی نمی‌گویند؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"3\": \"عربی «مَرْجان» «مروارید خرد؛ مرجان» (اسم جمع، با اسم واحدِ مرجانة) وامی از سریانیِ margān/margānīṯā است، با بدل شدن قاعده‌مندِ گافِ سریانی به جیم عربی. واژه قرآنی است (الرحمن ۲۲ و ۵۸: «اللؤلؤ والمرجان») و مفسران از همان آغاز میان «مرواریدهای خرد» و «مرجان» مردد بوده‌اند — و همین سرچشمهٔ دوگانگیِ معناست. جفری و اصباغی هر دو همین را می‌گویند، پس پیوند آرامی ← عربی درست است.\",\n\"4\": \"«مرجان» فارسی وام‌واژه‌ای از «مرجان» عربی است که تنها معنای «مرجان» را نگاه داشته است (ویکی‌واژه: فارسی و ترکی عثمانی این واژهٔ عربی را به‌خصوص در معنای مرجان گرفتند)، و در بیت حافظ در کنار «لؤلؤ» آمده است. جالب آنکه این یک رفت‌وبرگشتِ کامل است: ایرانی ← یونانی ← آرامی ← عربی ← فارسی، پس «مروارید» و «مرجان» در فارسی دو صورتِ یک واژه (دوگانه) اند. معین آن را با نشانِ «[ع.]» می‌آورد و حاشیهٔ او بر برهان نیز همین را تأیید می‌کند؛ ادعای نورایی درست است.\",\n\"5\": \"یونانی μαργαρίτης (λίθος) «مروارید» نخستین بار در «در باب سنگ‌ها»ی تئوفراستوس (سدهٔ چهارم پیش از میلاد) آمده و بنا بر ویکی‌واژه و بیکس وام‌واژه‌ای هندوایرانی است، به‌خصوص از نیای ایرانی باستانِ *margārīta- که «مروارید» فارسی میانه نیز از آن است، با جایگزینیِ پسوند یونانیِ -ίτης به جای پایانهٔ ایرانی؛ اتیمآنلاین نیز می‌نویسد «از زبانی شرقی، به احتمال بسیار ایرانی؛ سنجیده شود با marvarit فارسی میانه». پس جهت پیکان درست است و تنها برچسبِ «پهلوی» برای وام‌دهنده زمان‌پریشانه است، چون وام‌گیری پیش از دورهٔ فارسی میانه رخ داده است.\",\n\"6\": \"این جعبهٔ گذرا برای لاتینی است: margarīta «مروارید» (سیسرون، پلینیوس، و ولگاتِ متی ۱۳:۴۵–۴۶) وامی مستقیم از margarítēs یونانی است که پایانهٔ مذکرِ -ítēs یونانی در آن به -īta مؤنثِ صرفِ نخستِ لاتینی بازساخته شده است؛ در لاتینیِ متأخر همین صورت نام زنانهٔ Margarita نیز شده است. ارنو-مه‌یه و وبستر هر دو تأیید می‌کنند و ادعای نورایی درست است.\",\n\"7\": \"این جعبهٔ گذرا برای فرانسویِ کهن است: margarite/marguerite «مروارید» و نامِ Marguerite (سده‌های دوازدهم و سیزدهم) از لاتینی margarīta می‌آید، با تبدیل قاعده‌مندِ -a به -e و نگاه‌داشتِ گاف پیش از a. فرانسوی کهن مجرای ورودِ margarite و Margaret و Margery به انگلیسی است، اما margarine و Margarita و Rita از این راه نیامده‌اند (گرهٔ ۸). ادعای نورایی در این حلقه درست است.\",\n\"8\": \"هر هفت واژه سرانجام به margarítēs یونانی و margarīta لاتینی می‌رسند، اما از راه‌های گوناگون: margarite در انگلیسی میانه «مروارید» بود (از فرانسوی کهن) و معنای کانی‌شناختیِ امروزی‌اش (نوعی میکای کلسیم‌دار، دههٔ ۱۸۲۰) کاربردی علمی با پسوند -ite است؛ margarine از فرانسوی margarine است که شورول در ۱۸۱۳ از «اسید مارگاریک» (به مناسبت جلای مرواریدگونِ بلورها) ساخت و مژـموریه در ۱۸۶۹ آن را نام کرهٔ مصنوعی کرد و در ۱۸۷۳ به انگلیسی رسید — یعنی یونانی ← فرانسوی ← انگلیسی، بی هیچ مرحلهٔ فرانسویِ کهن؛ Margaret (حدود ۱۳۰۰) از فرانسوی کهن Margaret؛ Marjorie گونه‌ای از Margery، صورت مردمیِ سده‌های میانه؛ Margarita صورت لاتینی/اسپانیایی همان نام (و نام آن نوشیدنی)؛ Maggie تصغیر انگلیسیِ Margaret و Rita کوتاه‌شدهٔ اسپانیایی/ایتالیاییِ Margarita. پس جعبهٔ واحدِ فرانسویِ کهن برای margarite و Margaret و Marjorie و Maggie درست است و برای سه واژهٔ دیگر تنها شماتیک است.\"\n},\n\"2\": {\n\"1\": \"عربی «مَوْت» مصدرِ فعل اجوفِ «ماتَ/یموتُ» از ریشهٔ م-و-ت است، از سامیِ آغازینِ *mawt- (هم‌ریشه با اکدی mūtu، عبری māweṯ و سریانی mawtā). ضبطِ «maot» نورایی تنها نگارشِ همان mawt با مصوت مرکب است. اسکیت، لوکوچ و فانک و واگنالز همین را می‌آورند و ادعای نورایی درست است.\",\n\"2\": \"چهار واژهٔ این جعبه یکسان نیستند. «موت» (با تلفظ ایرانیِ mowt) و «ممات» هر دو وام‌واژه‌های عربی‌اند و بی‌اشکال؛ «میّت» نیز عربیِ mayyit است، صفتی بر وزن فَعیل از م-و-ت (*mawīt > *mayīt > mayyit با همگونی) که در فارسی به‌عنوان اسم گرفته شده است. اما «مات» به معنی «بی‌فروغ، حیران، درمانده» دو تحلیل دارد: تحلیل سنتی (که نورایی می‌آورد) آن را از «ماتَ» عربی می‌گیرد، و ویکی‌واژه در برابر آن واژه‌ای ایرانیِ اصیل را ممکن می‌داند که معنای «حیران» آن با کاربرد شطرنجی تقویت شده است. «کیش مات/شاه مات» را نیز ویکی‌واژه ترکیبی فارسی به معنی «شاه درمانده است» می‌خواند که عرب‌زبانان «مات» آن را به «مرد» بازتفسیر کرده‌اند، و بارنهارت و اتیمآنلاین نیز همین را می‌گویند. پس اشتقاق عربیِ «مات» روایت کلاسیک است اما یگانه رأی امروزی نیست و حکم گره از ضعیف‌ترین واژه پیروی می‌کند.\",\n\"3\": \"لاتینی mattus (و mātus) «مست، خیس و کرخت» در ساتیریکونِ پترونیوس (سدهٔ نخست میلادی) گواه دارد، یعنی شش سده پیش از هرگونه تماس با عربی، پس به هیچ روی نمی‌تواند از «مات» عربی یا فارسی آمده باشد. ریشه‌شناسیِ معیار (پوکورنی ص ۶۹۴ ذیل mad-، دِ ڤان، ویکی‌واژه) آن را *maditus «خیس‌شده» می‌داند، اسم مفعولِ madēre «خیس/مست بودن» از هندواروپایی *meh₂d- (سنسکریت mattá- «مست»)، با افتادن واکه و همگونیِ -dt- > -tt-. خودِ یادداشت نورایی نیز رأی پوکورنی را نقل کرده است و پژوهش امروزی یکپارچه جانب اوست؛ پس پیوندِ «ماتِ فارسی ← mattus لاتینی» رد می‌شود.\",\n\"4\": \"فرانسوی mat «بی‌جلا، کدر» دنبالهٔ mat فرانسویِ کهن (سدهٔ دوازدهم) به معنی «فروکوفته، پژمرده، افسرده» است که ویکی‌واژه و فرهنگ زبان فرانسه آن را از لاتینی mattus می‌گیرند؛ پس پیوندِ «mattus ← mat» که نمودار کشیده رأی اکثریت است و درست. با این همه اتیمآنلاین احتمال دیگری می‌افزاید: اینکه صفت فرانسویِ کهن کاربردی منتقل‌شده از mat شطرنجی («ماتِ شده») باشد که خود از «شاه مات» عربی آمده است — در آن صورت این واژه از گرهٔ ۲ می‌آید، اما باز هم نه از راه لاتینی. به هر روی از عربی از مسیر لاتینی نیامده است، از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"5\": \"انگلیسی mat/matte «کدر، بی‌جلا» (دههٔ ۱۶۴۰) وامی از mat فرانسوی است و املای matte تا سدهٔ بیستم یکدست نشد. یادداشت نمودار به AHD (ص ۸۰۵) ارجاع می‌دهد که واژه را از راه mattus لاتینی به ریشهٔ mad- «خیس» می‌برد — و همان، چنان‌که در گرهٔ ۳ گفته شد، اجماع امروزی است. خودِ حلقهٔ فرانسوی ← انگلیسی محل بحث نیست و ادعای نورایی در این گره درست است.\",\n\"6\": \"فرانسوی کهن mat «ماتِ شده، شکست‌خورده» (سدهٔ دوازدهم، با فعل mater) و ترکیب eschec mat که به échec et mat امروزی رسیده، اصطلاح شطرنج است و از «شاه مات» عربی می‌آید (فارسی «شاه مات» یعنی «شاه درمانده است» که در عربی «شاه مرد» خوانده شد)، و همراه خودِ بازیِ شطرنج در سده‌های چهارم و پنجم هجری از راه اندلس و سیسیل به زبان‌های رومی رسید (اسپانیایی jaque mate، ایتالیایی scacco matto). اما نمودار این mat فرانسوی را از mattus لاتینی «مست» می‌گیرد و همین نادرست است: واژهٔ شطرنجی وام‌واژه‌ای عربی-فارسی است و باید یکراست به گرهٔ ۲ آویخته می‌شد، چنان‌که یادداشت خودِ نورایی («مسیرهای محل بحث») نیم‌بند اذعان دارد. پیهان، دویک، لوکوچ و اسکیت همه همین را می‌گویند.\",\n\"7\": \"انگلیسی mate (فعل) «مات کردن، مقهور ساختن» (حدود ۱۳۰۰) از mater فرانسویِ کهن است و mate (اسم) «مات» نیز از mat فرانسوی کهن؛ checkmate (میانهٔ سدهٔ چهاردهم) از eschec mat فرانسویِ کهن و در نهایت از «شاه مات» عربی/فارسی می‌آید. معنای مجازیِ «بازداشتن و ناکام گذاشتن» از اواخر سدهٔ چهاردهم است. پیوستِ سامیِ AHD ذیل m-w-t دقیقاً همین دو واژهٔ انگلیسی را برمی‌شمارد؛ ادعای نورایی درست است.\",\n\"8\": \"matar اسپانیایی «کشتن» (و نیز پرتغالی و کاتالان) خاستگاهی محل اختلاف دارد. ویکی‌واژه آن را «به احتمال بسیار از لاتینی mactāre (از راه لاتینیِ عامیانهٔ *mattāre)» می‌داند و گونهٔ دیگر را mattus لاتینیِ متأخر («مست، کرخت»، پس *mattāre «کرخت کردن») یا زیر تأثیر «ماتَ» عربی؛ فرهنگستان اسپانیا نیز *mattare < mattus را ترجیح می‌دهد. اتیمآنلاین دشواریِ آواییِ mactāre را یادآور می‌شود (که می‌بایست *mechar بدهد) و «مات» عربی (وام‌گرفته از فارسی) را گزینهٔ جایگزین می‌داند — همان رأیی که کلاین، منبعِ نورایی، برگزیده و کورومیناس نیز از راه واژهٔ شطرنجی بحث کرده است. پس اشتقاق عربی گزینه‌ای علمی و واقعی است اما گزینهٔ ترجیحی نیست. «ماتادور» نیز به‌روشنی matar است به‌علاوهٔ پسوند فاعلیِ -dor (< لاتینی -tōrem) و در این حد بی‌اشکال است.\",\n\"9\": \"فرانسوی matador وام‌واژه‌ای است از اسپانیایی matador که در اواخر سدهٔ هفدهم و در سدهٔ هجدهم همراه واژگان گاوبازی وارد فرانسه شد و صورتش دگرگون نشده است. ادعای نورایی در این حلقه درست است.\",\n\"10\": \"«ماتادور» فارسی (که نورایی با ضمه «ماتادُر» می‌نویسد) وامی از سدهٔ چهاردهم خورشیدی است؛ ویکی‌واژه آن را «وام‌گرفته از اسپانیایی» می‌داند، حال آنکه نورایی به پیروی از معین آن را از راه فرانسه می‌آورد — و فرانسه در آن دوره مجرای معمولِ ورودِ واژه‌های اروپایی به فارسی بوده و از نظر آوایی این دو راه تفکیک‌پذیر نیستند. هر دو مسیر با صورت واژه سازگارند و زبانِ وام‌دهندهٔ بی‌واسطه را نمی‌توان از روی صورت تعیین کرد؛ از این رو حکم «با احتیاط پذیرفتنی» است.\",\n\"11\": \"انگلیسی matador (دههٔ ۱۶۷۰) یکراست از اسپانیایی matador «کشنده» گرفته شده است، اسم فاعلِ matar؛ از دههٔ ۱۷۳۰ نیز برای برگ‌های برندهٔ بازی‌های ورق اسپانیایی (اومبره و کوادریل) به کار رفته است. کلاین، اسکیت و وبستر همین را می‌گویند و ادعای نورایی درست است.\"\n}\n}\n}\nEOF\npython3 apply_fa.py 345 p345.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-345.json >/dev/null && echo JSON_OK && git -C /home/sfmqrb/git/rishe diff --stat -- data/verification/page-345.json",
 "description": "Apply Persian to page 345"
}
```


### [2026-09-04T23:33:39.918Z] TOOL RESULT

```
ok 345
JSON_OK
 data/verification/page-345.json | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
```


## [2026-09-04T23:33:41.888Z] AGENT

Now final verification across all nine pages.


## [2026-09-04T23:33:46.701Z] TOOL CALL #36: Bash

```json
{
 "command": "for p in 56 57 58 59 60 101 126 311 345; do python3 -m json.tool data/verification/page-$p.json >/dev/null || echo \"BAD $p\"; done; echo \"json ok\"\npython3 - <<'EOF'\nimport json\ntot=0\nfor p in [56,57,58,59,60,101,126,311,345]:\n    d=json.load(open(f'data/verification/page-{p}.json'))\n    n=fa=e=efa=0; bad=[]\n    for en in d['entries']:\n        e+=1\n        t=en.get('note_fa')\n        if t and len(t)>150: efa+=1\n        else: bad.append(('entry',en['entry']))\n        for nd in en['nodes']:\n            n+=1\n            t=nd.get('derivation_fa')\n            if t and len(t)>150: fa+=1\n            else: bad.append((en['entry'],nd['id']))\n    tot+=fa\n    print(f'page {p}: nodes {n} derivation_fa {fa} | entries {e} note_fa {efa}', 'BAD:'+str(bad) if bad else '')\nprint('total nodes with derivation_fa:',tot)\nEOF\npython3 tools/verify_check.py 56 57 58 59 60 101 126 311 345\ngit status --short data/verification/",
 "description": "Validate all pages and run verify_check"
}
```


### [2026-09-04T23:33:49.221Z] TOOL RESULT

```
json ok
page 56: nodes 22 derivation_fa 22 | entries 1 note_fa 1 
page 57: nodes 11 derivation_fa 11 | entries 2 note_fa 2 
page 58: nodes 15 derivation_fa 15 | entries 2 note_fa 2 
page 59: nodes 18 derivation_fa 18 | entries 1 note_fa 1 
page 60: nodes 18 derivation_fa 18 | entries 2 note_fa 2 
page 101: nodes 22 derivation_fa 22 | entries 2 note_fa 2 
page 126: nodes 16 derivation_fa 16 | entries 1 note_fa 1 
page 311: nodes 20 derivation_fa 20 | entries 1 note_fa 1 
page 345: nodes 19 derivation_fa 19 | entries 2 note_fa 2 
total nodes with derivation_fa: 161
nodes verified: 161/161
node verdicts: {'confirmed': 100, 'plausible': 31, 'transcription_suspect': 3, 'disputed': 27}
root verdicts: {'confirmed': 11, 'plausible': 2, 'disputed': 1}
ref checks: {'supports': 131, 'not_checked': 48, 'partial': 44, 'not_found': 9, 'contradicts': 4}
books consulted: {'supports': 317, 'partial': 110, 'silent': 110, 'contradicts': 43} | by book: {'KLN': 46, 'SKT': 38, 'PHD': 35, 'MON': 34, 'HRN': 31, 'NYB': 28, 'BRT': 28, 'WEB': 26, 'LKT': 24, 'PLA': 21, 'AHD': 20, 'BQT': 19, 'LAT': 19, 'FSD': 18, 'POK': 17, 'IEC': 17, 'CHEUNG': 16, 'ARY': 15, 'WLD': 15, 'HUB': 14, 'FVQ': 13, 'AFM': 10, 'SYN': 9, 'LEW': 8, 'TAD': 8, 'AKD': 8, 'KNT': 7, 'SOD': 6, 'DEV': 5, 'AFA': 5, 'HJB': 4, 'RCH': 3, 'PHN': 3, 'SNS': 2, 'AID': 2, 'FRS': 1, 'FSF': 1, 'ISS_alt_DKS': 1, 'TLM': 1, 'IRN': 1}
 M data/verification/page-345.json
```


## [2026-09-04T23:33:52.865Z] TOOL CALL #37: Bash

```json
{
 "command": "git log --oneline -3 && git status --short | head -20",
 "description": "Check git log and status"
}
```


### [2026-09-04T23:33:52.922Z] TOOL RESULT

```
0e8af86 Verify page 62 (Ar/Are part 2); data fix: logârîtm
ae93dac Persian explanations: backfill progress
61a3a20 Verify page 61 (A.q.r, Ar/Are)
 M data/verification/page-345.json
```


## [2026-09-04T23:34:12.128Z] AGENT

All nine files now carry Persian explanations; JSON validates and `verify_check.py` reports 0 PROBLEM lines (161/161 nodes verified).

Per page — nodes given `derivation_fa`, and every entry has `note_fa`:

- page 56: 22 nodes — all entries (1) have `note_fa`
- page 57: 11 nodes — all entries (2) have `note_fa`
- page 58: 15 nodes — all entries (2) have `note_fa`
- page 59: 18 nodes — all entries (1) have `note_fa`
- page 60: 18 nodes — all entries (2) have `note_fa`
- page 101: 22 nodes — all entries (2) have `note_fa`
- page 126: 16 nodes — all entries (1) have `note_fa`
- page 311: 20 nodes — all entries (1) have `note_fa`
- page 345: 19 nodes — all entries (2) have `note_fa`

Total: 161 nodes + 14 entries, none missing.

Notes on how it was done:
- Each Persian text was written from that node's own `derivation`, `verdict`, `ref_check` and `consulted` — naming which sources support or contradict (پوکورنی، بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، قریب، کلاین، معین/برهان قاطع، اصباغی، جفری، ویکی‌واژه) and stating the verdict in Persian terms (ادعای نورایی درست است / با احتیاط پذیرفتنی / پژوهش امروزی رد می‌کند و … می‌گوید / خطای چاپی کتاب).
- The three flagged forms are described as the sources record them: page 101 #4 «smaraldos» and page 311 #13 «hava-rd» as Nourai's own misprints (خطای چاپی کتاب، استخراج وفادار)، page 126 #1 «děğa-vâra» likewise printed that way in the book; page 56 #13 «کترنگ» as most likely a scan misreading of «چترنگ».
- Only the new keys were inserted; `derivation_fa` sits immediately after `derivation`, `note_fa` after `note`. Files 60 and 126 use non-standard indentation/compact arrays, so those were patched by line insertion rather than re-serialisation, preserving byte-for-byte formatting (including the missing trailing newline in 58/126/311). `git diff --stat` shows insertions only.
- Note: while I was working, the coordinator committed "Persian explanations: backfill progress" (ae93dac), which swept in pages 56–311; page-345.json remains uncommitted in the working tree.
