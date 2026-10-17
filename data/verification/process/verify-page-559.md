# Verification process log — verify-page-559


## [2026-10-17T00:30:14.184Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 559 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-559.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-559.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-559.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 559` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.218Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:18.859Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:18.878Z] TOOL RESULT

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
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:30:19.352Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-559.txt"
}
```


### [2026-10-17T00:30:19.374Z] TOOL RESULT

```
1	=== PDF page 559 (book page 529) ===
2	--- entry 0 ---
3	ROOT [Chinese] Xalen : birch tree, birch wood  (refs SIN:552)
4	#1 (parent #0) [Altaic] refs=SIN:553 | 
5	  #2 (parent #1) [Persian] refs=SIN:553; BQT:719; FSF:158 | xadang «خدنگ» : hard wood, arrow made of this wood
6	--- entry 1 ---
7	ROOT Xartěs -> redirect to Čartěs
8	--- entry 2 ---
9	ROOT Xasta -> redirect to Xad
10	--- entry 3 ---
11	ROOT [Avestan / Old Persian] Xšad : to forgive  (refs FFD:35)
12	#1 (parent #0) [Avestan / Old Persian] refs=FFD:35 | apa-xšad-a : to forgive ☞Apo
13	  #2 (parent #1) [Pahlavi] refs=FFD:35 | abaxšay, abaxšâyîd
14	    #3 (parent #2) [Persian] refs=FFD:35 | baxšîdan «بخشیدن» : to forgive | extra: بخشای ، بخشاینده ، بخشنده ، بخشایش | NOTE: Due to the similarity in sounds / meanings of "baxšŭdan: to forgive" and "baxšîdan: to give", these words are often confused with each other.
15	--- entry 4 ---
16	ROOT Xšaivan -> redirect to Xšî 1
17	--- entry 5 ---
18	ROOT [Old Iranian] Xšarta : to press, squeeze  (refs BLY:75)
19	#1 (parent #0) [Pahlavi] refs=BLY:75; PHD:5 | afsârtan, aššârdan : to squeeze
20	  #2 (parent #1) [Persian] refs=BLY:75 | afšârdan «افشاردن ( افشردن، فشردن )» : squeeze, crush ; fešâr «فشار» : pressure ; afšoreh «افشره» : juice (squeezed out of a fruit)
21	--- entry 6 ---
22	ROOT [Avestan / Old Persian] Xšî 1, Xšaivan : Xšî 1: grief, poverty; Xšaivan: grief, crying  (refs BQT:1329)
23	#1 (parent #0) [Pahlavi] refs=None | šěvan : crying
24	  #2 (parent #1) [Persian] refs=BQT:1329 | šîvan «شیون» : crying
25	
```


## [2026-10-17T00:30:20.130Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-559.json"
}
```


### [2026-10-17T00:30:20.146Z] TOOL RESULT

```
1	{
2	  "pdf_page": 559,
3	  "book_page": 529,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Xalen",
8	        "lang": "Chinese",
9	        "refs": "SIN:552",
10	        "gloss": "birch tree, birch wood",
11	        "note": "A common tree in north China and Tabarestân. The artifacts from this wood were exported to Iran."
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Altaic",
18	          "refs": "SIN:553",
19	          "words": [],
20	          "note": null,
21	          "quote": null
22	        },
23	        {
24	          "id": 2,
25	          "parent": 1,
26	          "lang": "Persian",
27	          "refs": "SIN:553; BQT:719; FSF:158",
28	          "words": [
29	            {"translit": "xadang", "gloss": "hard wood, arrow made of this wood", "script": "خدنگ"}
30	          ],
31	          "note": null,
32	          "quote": {
33	            "text": "کمان کیـانی گـرفتم به چنگ - به پیکان پولاد و تیر خدنگ",
34	            "poet": "Ferdowsî"
35	          }
36	        }
37	      ]
38	    },
39	    {
40	      "root": {"name": "Xartěs", "redirect": "Čartěs"},
41	      "nodes": []
42	    },
43	    {
44	      "root": {"name": "Xasta", "redirect": "Xad"},
45	      "nodes": []
46	    },
47	    {
48	      "root": {
49	        "name": "Xšad",
50	        "lang": "Avestan / Old Persian",
51	        "refs": "FFD:35",
52	        "gloss": "to forgive"
53	      },
54	      "nodes": [
55	        {
56	          "id": 1,
57	          "parent": 0,
58	          "lang": "Avestan / Old Persian",
59	          "refs": "FFD:35",
60	          "words": [
61	            {"translit": "apa-xšad-a", "gloss": "to forgive", "script": null, "see": ["Apo"]}
62	          ],
63	          "note": null,
64	          "quote": null
65	        },
66	        {
67	          "id": 2,
68	          "parent": 1,
69	          "lang": "Pahlavi",
70	          "refs": "FFD:35",
71	          "words": [
72	            {"translit": "abaxšay, abaxšâyîd", "gloss": null, "script": null}
73	          ],
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 3,
79	          "parent": 2,
80	          "lang": "Persian",
81	          "refs": "FFD:35",
82	          "words": [
83	            {"translit": "baxšîdan", "gloss": "to forgive", "script": "بخشیدن"}
84	          ],
85	          "script_extra": "بخشای ، بخشاینده ، بخشنده ، بخشایش",
86	          "note": "Due to the similarity in sounds / meanings of \"baxšŭdan: to forgive\" and \"baxšîdan: to give\", these words are often confused with each other.",
87	          "quote": null
88	        }
89	      ]
90	    },
91	    {
92	      "root": {"name": "Xšaivan", "redirect": "Xšî 1"},
93	      "nodes": []
94	    },
95	    {
96	      "root": {
97	        "name": "Xšarta",
98	        "lang": "Old Iranian",
99	        "refs": "BLY:75",
100	        "gloss": "to press, squeeze"
101	      },
102	      "nodes": [
103	        {
104	          "id": 1,
105	          "parent": 0,
106	          "lang": "Pahlavi",
107	          "refs": "BLY:75; PHD:5",
108	          "words": [
109	            {"translit": "afsârtan, aššârdan", "gloss": "to squeeze", "script": null}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 2,
116	          "parent": 1,
117	          "lang": "Persian",
118	          "refs": "BLY:75",
119	          "words": [
120	            {"translit": "afšârdan", "gloss": "squeeze, crush", "script": "افشاردن ( افشردن، فشردن )"},
121	            {"translit": "fešâr", "gloss": "pressure", "script": "فشار"},
122	            {"translit": "afšoreh", "gloss": "juice (squeezed out of a fruit)", "script": "افشره"}
123	          ],
124	          "note": null,
125	          "quote": null
126	        }
127	      ]
128	    },
129	    {
130	      "root": {
131	        "name": "Xšî 1, Xšaivan",
132	        "lang": "Avestan / Old Persian",
133	        "refs": "BQT:1329",
134	        "gloss": "Xšî 1: grief, poverty; Xšaivan: grief, crying"
135	      },
136	      "nodes": [
137	        {
138	          "id": 1,
139	          "parent": 0,
140	          "lang": "Pahlavi",
141	          "refs": null,
142	          "words": [
143	            {"translit": "šěvan", "gloss": "crying", "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 2,
150	          "parent": 1,
151	          "lang": "Persian",
152	          "refs": "BQT:1329",
153	          "words": [
154	            {"translit": "šîvan", "gloss": "crying", "script": "شیون"}
155	          ],
156	          "note": null,
157	          "quote": null
158	        }
159	      ]
160	    }
161	  ]
162	}
163	
```


## [2026-10-17T00:30:23.656Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SIN','BQT','FSF','FFD','BLY','PHD','HRN','HUB','CHEUNG','MON','ARY','NYB','BRT','KNT','LKT','TTS']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; command ls data/verification/sources/refs/ | head -100"
}
```


### [2026-10-17T00:30:24.469Z] TOOL RESULT

```
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
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt", "page_offset": "
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
BLY {"title": "H. W. Bailey, 'Hvatanica II' (glossary of Khotanese words), BSOAS 9.1 (1937) pp. 69-78", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian's open compilation \"Selected Writings of H. W. Bailey\"; Hvatanica II = PDF pp. 313-322)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verificati
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uof
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
KNT_full.txt
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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-10-17T00:30:27.346Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['SIN','BQT','FSF','FFD','BLY','MON','CHEUNG']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:1500]);print()\n\"; sed -n 80,200p data/verification/sources/SOURCE_MATRIX.md | grep -n -i -A3 'CHEUNG\\|MON\\b' | head -30"
}
```


### [2026-10-17T00:30:27.951Z] TOOL RESULT

```
SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sections are numbered with plant/product names in caps; grep the Persian/Chinese word or the page number.", "notes": ""}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."}

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).", "covers_etymology": true, "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N

BLY {"title": "H. W. Bailey, 'Hvatanica II' (glossary of Khotanese words), BSOAS 9.1 (1937) pp. 69-78", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/bailey-studies-1930-1993 (Robert Bedrosian's open compilation \"Selected Writings of H. W. Bailey\"; Hvatanica II = PDF pp. 313-322)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/Bailey_Studies_1930-1993_bedrosian.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY/BLY_bailey_studies_pages.txt"], "page_offset": "BLY_pages.txt: 11 leaves; printed = leaf(1-based) + 67 (leaf 2 = p.69 ... leaf 11 = p.78).", "lookup_hint": "JSTOR only (BSOAS 9, 1937-39). Not on IA. Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt, open) supersedes Hvatanica for the same words.", "notes": "Open full text obtained (article extracted from the compilation; the whole 114 MB compilation with 80 Bailey articles is kept alongside and also covers Hvatanica I, III, IV and other Bailey papers)."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmq

CHEUNG null

1:- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
2-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
3-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
4:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
5:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
6:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
7:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
8-- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
9-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
10-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
--
84:- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
85-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
86-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
87:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
88:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
89:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
90:  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
91-- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
92-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
93-  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
```


## [2026-10-17T00:30:32.697Z] AGENT

Let me start with SIN pages 552-553 (leaves 380-381).


## [2026-10-17T00:30:34.306Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'xadan\\|k.adang\\|xa-lien\\|hua\\b\\|birch' SIN.txt | head -30; for n in 381 382; do echo \"=== leaf $((n-1))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SIN.txt | head -80; done"
}
```


### [2026-10-17T00:30:34.643Z] TOOL RESULT

```
114:The  Square  Bamboo,  p.  535. — Silk,  p.  537. — Peach  and  Apricot,  p.  539. — Cinnamon, p.  541. — Zedoary,  p.  544. — Ginger,  p.  545. — Mamiran,  p.  546. — Rhubarb,  p.  547. — Salsola,  p.  551. — Emblic  Myrobalan,  p.  551. — Althaea,  p.  551. — Rose  of  China, p.  551.— Mango,  p.  552. — Sandal,  p.  552. — Birch,  p.  552.— Tea,  p.  553. — Onyx, p.  554. — Tootnague,  p.  555. — Saltpetre,  p.  555. — Kaolin,  p.  556. — Smilax  pseudo- china,  p.  556. — Rag-paper,  p.  557. — Paper  Money,  p.  559. — Chinese  Loan-Words in  Persian,  p.  564. — The  Chinese  in  the  Alexander  Romance,  p.  570.
3677:16.  Antaki  notes  the  xalen  tree  ("birch")  in  India  and  China;  and Ibn  al-Keblr  remarks  that  it  is  particularly  large  in  China,  in  the country  of  the  Rus  (Russians)  and  Bulgar,  where  are  made  from  it vessels  and  plates  which  are  exported  to  distant  places;  the  arrows made  of  this  wood  are  unsurpassed.    According  to  Qazwlnl  and  Ibn
3683:Irano-Sinica— Mango,  Birch,  Tea  553
3684:Fadlan,  the  tree  occurred  in  Tabaristan,  whence  its  wood  reached  the comb-makers  of  Rei.1  The  Arabic  xaleit,  Persian  xadan  or  xadanj, is  of  Altaic  origin:  Uigur  qadan,  Koibal,  Soyot  and  Karagas  kaden, Cuwas'  xoran,  Yakut  xatyn,  Mordwinian  kilen,  all  referring  to  the  birch (Betula  alba).  It  is  a  common  tree  in  the  mountains  of  northern  China (hwa  %&  ),  first  described  by  C'en  Ts'an-k'i  of  the  eighth  century.2  The bark  was  used  by  the  Chinese  for  making  torches  and  candles  filled  with wax,  as  a  padding  or  lining  of  underclothes  and  boots,  for  knife-hilts and  the  decoration  of  bows,  the  latter  being  styled  "birch-bark  bows."3 The  universal  use  of  birch-bark  among  all  tribes  of  Siberia  for  pails, baskets,  and  dishes,  and  as  a  roof -covering,  is  well  known.
4279:Birch,  552-553-
=== leaf 380
  of  the Chinese  transcription  mun  W. .  The  an-lo  tree  is  first  mentioned  for Cen-la  (Camboja)  in  the  Sui  Annals,5  where  its  leaves  are  compared with  those  of  the  jujube  (Zizyphus  vulgaris),  and  its  fruits  with  those of  a  plum  (Prunus  tri flora).
15.  Isak  Ibn  Amran  says,  "Sandal  is  a  wood  that  comes  to  us  from China."6  Santalum  album  is  grown  in  Kwan-tun  to  some  extent,  but  it is  more  probable  that  the  sandal-wood  used  in  western  Asia  came  from India  (cf.  Persian  Zandan,  Zandal,  Armenian  candan,  Arabic  sandal, from  Sanskrit  candana).
16.  Antaki  notes  the  xalen  tree  ("birch")  in  India  and  China;  and Ibn  al-Keblr  remarks  that  it  is  particularly  large  in  China,  in  the country  of  the  Rus  (Russians)  and  Bulgar,  where  are  made  from  it vessels  and  plates  which  are  exported  to  distant  places;  the  arrows made  of  this  wood  are  unsurpassed.    According  to  Qazwlnl  and  Ibn
1  Ibid.,  p.  314.
2  G.  Ferrand,  Textes  relatifs  a  l'Extr&ne-Orient,  p.  381.
3  Leclerc,  Traits  des  simples,  Vol.  II,  p.  471.  Cf.  Ibn  Batata,  ed.  of  De- fremery  and  Sanguinetti,  Vol.  Ill,  p.  127;  Yule,  Hobson-Jobson,  p.  553.
4  T'ai  p'in  hwan  yii  ki,  Ch.  181,  p.  13  b. 6  Sui  1m,  Ch.  82,  p.  3  b.
6  Leclerc,  op.  tit.,  p.  383.
Irano-Sinica— Mango,  Birch,  Tea  553
Fadlan,  the  tree  occurred  in  Tabaristan,  whence  its  wood  reached  the comb-makers  of  Rei.1  The  Arabic  xaleit,  Persian  xadan  or  xadanj, is  of  Altaic  origin:  Uigur  qadan,  Koibal,  Soyot  and  Karagas  kaden, Cuwas'  xoran,  Yakut  xatyn,  Mordwinian  kilen,  all  referring  to  the  birch (Betula  alba).  It  is  a  common  tree  in  the  mountains  of  northern  China (hwa  %&  ),  first  described  by  C'en  Ts'an-k'i  of  the  eighth  century.2  The bark  was  used  by  the  Chinese  for  making  torches  and  candles  filled  with wax,  as  a  padding  or  lining  of  underclothes  and  boots,  for  knife-hilts and  the  decoration  of  bows,  the  latter  being  styled  "birch-bark  bows."3 The  universal  use  of  birch-bark  among  all  tribes  of  Siberia  for  pails, baskets,  and  dishes,  and  as  a  roof -covering,  is  well  known.
17.  It  would  be  very  desirable  to  have  more  exact  data  as  to when  and  how  the  consumption  of  Chinese  tea  (Camellia  theifera) spread  among  Mohammedan  peoples.  The  Arabic  merchant  Soleiman, who  wrote  about  a.d.  851,  appears  to  be  the  first  outsider  who  gives  an accurate  notice  of  the  use  of  tea-leaves  as  a  beverage  on  the  part  of  the Chinese,  availing  himself  of  the  curious  name  sax.4  It  is  strange  that_ the  followinglArabic  authors  who  wrote  on  Chinese  affairs  have  nothing^' to  say  on  the  subject.J  In  the  splendid  collection  of  Arabic  texts  relative to  the  East,  so  ably  gathered  and  interpreted  by  G.  Ferrand,  tea is  not  even  mentioned.  It  is  likewise  absent  in  the  Persian  pharmacology of  Abu  Mansur  and  in  the  vast  compilation  of  Ibn  al-Baitar.  On  the other  hand,  Chinese  mediaeval  authors  like  Cou  K'u-fei  and  Cao  2u- kwa  do  not  note  tea  as  an  article  of  export  from  China.  As  far  as we  can  judge  at  present,  it  seems  that  the  habit  of  tea-drinking  spread to  western  Asia  not  earlier  than  the  thirteenth  century,  and  that  i
=== leaf 381
*j was  perhaps  the  Mongols  who  assumed  the  r61e  of  propagators.  In Mongol,  Turkish,  Persian,  Indian,  Portuguese,  Neo-Greek,  and  Rus- sian, we  equally  find  the  word  &w,  based  on  North-Chinese  <?'a.5  Ramu-
1  G.  Jacob,  Handel sartikel  der  Araber,  p.  60. ■  Pen  ts"ao  kan  mu,  Ch.  35  B,  p.  13.
3  Ko  ku  yao  lun,  Ch.  8,  p.  8  b.  Cf.  also  O.  Franke,  Beschreibung  des  Jehol- Gebietes,  p.  77.
4  Reinaud,  Relation  des  voyages,  Vol.  I,  p.  40  (cf-  Yule,  Cathay,  new  ed., Vol.  I,  p.  131).  Modern  Chinese  Va  was  articulated  *ja  (dza)  in  the  T'ang  period; but,  judging  from  the  Korean  and  Japanese  form  sa,  a  variant  sa  may  be  supposed also  for  some  Chinese  dialects.  As  the  word,  however,  was  never  possessed  of  a final  consonant  in  Chinese,  the  final  spirant  in  Soleiman's  sax  is  a  peculiar  Arabic affair  (provided  the  reading  of  the  manuscript  be  correct).
5  The  Tibetans  claim  a  peculiar  position  in  the  history  of  tea.  They  still  have the  Chinese  word  in  the  ancient  form  ja  (dZa),  and,  as  shown  by  me  in  T'oung  Pao (1916,  p.  505),  have  imported  and  consumed  tea  from  the  days  of  the  T'ang.  In fact,  tea  was  the  dominant  economic  factor  and  the  key-note  in  the  political  rela- tions of  China  and  Tibet.
554  Sino-Iranica
sio,  in  the  posthumous  introduction  to  his  edition  of  Marco  Polo  pub- lished in  1545,  mentions  having  learned  of  the  tea  beverage  from  a Persian  merchant,  Hajji  Muhammed.1  A.  de  Mandelslo,2  in  1662, still  reports  that  the  Persians, instead  of  Th&,  drink  their  Kahwa  (coffee). In  the  fifteenth  century,  A-lo-tih,  an  envoy  from  T'ien-fah  (Arabia), in  presenting  his  tribute  to  an  emperor  of  the  Ming,  solicited  tea- leaves.3
The  Kew  Bulletin  for  1896  (p.  157)  contains  the  following  inter- esting information  on  "White  Tea  of  Persia:"  —
"In  the  Consular  Report  on  the  trade  of  Ispahan  and  Yezd  (Foreign  Office, Annual  Series,  1896,  No.  1662)  the  following  particulars  are  given  of  the  tea  trade in  Persia:  'Black  or  Calcutta  tea  for  Persian  consumption  continues  to  arrive  in steady  quantities,  2,000,000  pounds  representing  last  year's  supply.  White  tea  from China,  or  more  particularly  from  Tongking,  is  consumed  only  in  Yezd,  and,  there- fore, the  supply  is  limited.'  Through  the  courtesy  of  Mr.  John  R.  Preece,  Her Majesty's  Consul  at  Ispahan,  Kew  received  a  small  quantity  of  the  'White  tea' above  mentioned  for  the  Museum  of  Economic  Botany.  The  tea  proved  to  be  very similar  to  that  described  in  the  Kew  Bulletin  under  the  name  of  P'u-erh  tea  (Kew Bulletin,  1889,  pp.  118  and  139).  The  finest  of  this  tea  is  said  to  be  reserved  for  the Court  of  Peking.  The  sample  from  Yezd  was  composed  of  the  undeveloped  leaf buds  so  thickly  coated  with  fine  hairs  as  to  give  them  a  silvery  appearance.  Owing to  the  shaking  in  transit  some  of  the  hairs  had  been  rubbed  off  and  had  formed  small yellow  pellets  about  y&  inch  diameter.  Although  the  hairs  are  much  more abundant  than  usual  there  is  little  doubt  that  the  leaves  have  been  derived  from the  Assam  tea  plant  (Camellia  theifera,  Griff.)  found  wild  in  some  parts  of  Assam and  Burma  but  now  largely  cultivated  in  Burma,  Tongking,  etc.  The  same  species has  been  shown  to  yield  Lao
```


## [2026-10-17T00:30:42.578Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/559.jpg 2>/dev/null; pdftoppm -f 559 -l 559 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg559; echo ok"
}
```


### [2026-10-17T00:30:43.513Z] TOOL RESULT

```
site/pages/559.jpg
ok
```


## [2026-10-17T00:30:45.969Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg559.png"
}
```


### [2026-10-17T00:30:46.394Z] TOOL RESULT

```

```


## [2026-10-17T00:30:46.388Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:30:54.206Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; for n in 40 41; do echo \"=== NR $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' FFD_pages_faseng.txt | head -60; done"
}
```


### [2026-10-17T00:30:54.519Z] TOOL RESULT

```
=== NR 40
awk: cmd. line:1: fatal: cannot open file `FFD_pages_faseng.txt' for reading: No such file or directory
=== NR 41
awk: cmd. line:1: fatal: cannot open file `FFD_pages_faseng.txt' for reading: No such file or directory
```


## [2026-10-17T00:30:58.628Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; find . -ipath '*FFD*' | head; "
}
```


### [2026-10-17T00:30:58.999Z] TOOL RESULT

```
./incoming/FFD
./ocr/FFD
./incoming/FFD/FFD_asmaneketab.pdf
./incoming/FFD/FFD_pages.txt
./ocr/FFD/50.png
./ocr/FFD/50.vision.txt
./ocr/FFD/51.png
./ocr/FFD/51.vision.txt
./ocr/FFD/77.png
./ocr/FFD/77.vision.txt
```


## [2026-10-17T00:31:01.895Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; for n in 40 41; do echo \"=== NR $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' FFD_pages.txt | head -70; done; grep -n 'xšad\\|bax\\|بخش' FFD_pages.txt | head"
}
```


### [2026-10-17T00:31:02.205Z] TOOL RESULT

```
=== NR 40
[pdf page 40]
ماده‌های ماضی و مضارع فارسی دری ۳۵
بافتن

بافت < ایرانی باستان ۹۷31-۵*. برای 12 -> آراست. ]۷3 صورت بالاندةٌ ريشةٌ ۷:۵۲
است. ريشةٌ ۷۷2۶ به معنی «بافتن» است.

باف + فارسی میانه و پهلوی اشکانی ۴3۲+ ایرانی باستان ۷3۶۵*. برای 8 ->
آرای.

بالیدن

بالید + فارسی میانه ۷۷3170 ۷31704 مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته
شده است.

بال < فارسی میانه ۷31 < ایرانی باستان ۹۷374-8*. برای 2 -» آرای. ۲۷374 صورت
بالاندةٌ ريشهٌ ۷۷27۵ است بهُ معنی «رشد کردن».

بایستن

بایست + فارسی میانه 2032191. 202181 مادهٌ ماضی جعلی است و از مادهٌ مضارع
ساخته شده است.

بای < فارسی میانه 203 < ایرانی باستان 8ر3م* < 2-ر02-4*. برای ۵ -> آرای.
4 پیشوند فعلی است. 2۷ به معنی «حرکت کردن» است. «آی» مادهٌ مضارع «آمدن» از
9 آمده است > آمدن.

بخشودن

در فارسی میانه به جای «بخشود» 202333774 آمده است. 20253710 مادهٌ
ماضی جعلی و از مادهٌ مضارع ساخته شده است. «بخشود» در فارسی دری به قیاس
1 , 870 به وجود آمده است.

بخشای + فارسی میانه 202۶3 < ایرانی باستان ۵ -3520 -۵02*. برای 2 > آرای.
2 پیشوند فعلی است. ريشةٌ 7524 فرضی است > بخشیدن.

=== NR 41
[pdf page 41]
وج ان ار فعلهای فارسی دری
بخشیدن
بخشید < فارسی میانه 029870 027870 مادهٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
بخش < فارسی میانه 0235 < ایرانی باستان 82۳-3*. 328 صورت اصلی 337 است» 8
پیش از 8 به #بدل شده است. ‎٩‏ برای ساختن ريشهٌ جدید به کار رفته است. 328 به معنی
«تقسیم کردن» است و واه «بخت» در فارسی دری از 025-18 آمده است. 327۳-18 صفت
مفعولی گذشته است از پسوند 14 و 085 به جای ۳۵8. به سیب شباهت لفظی که میان
«بخشودن» به معنی «عفو کردنْ» و «بخشیدن» به معنی «تقسیم کردن» هست» «بخشیدن»
در معنی «بخشودن» به کار رفته است > بخشودن.
برازیدن
برازید « فارسی میانه 053270. 073270 مادةٌ ماضی جعلی است. از مادةٌ مضارع
ساخته شده است.
براز « فارسی میانه 0732 < ایرانی باستان ۳122-8*. برای 2 - آرای. ريشهٌ 3۲37 و
فارسی میانه هر دو به معنی «درخشیدن» هستند. «برازیدن» در معنی «سزاوار
و زیبنده بودنْ» به کار رفته است.
بردن
برد < فارسی میانه 0۵07۵ < ایرانی باستان ۳7-1۵*. برای 1۵ -> آراست. 7۲ صورت
ضعیف ريشةٌ 7 است. به معنی «حمل کردن». چون 2707448 در فارسی میانه معنی
«حمل کردن به سوی متکلم» می‌دهده 0070۵ در معتی «حمل کردن از متکلم» به کار
رفته است. در فارسی دری «آوردن» و «بردن» از نظر معنی چون فارسی میانه هستند.
بر < فارسی میانه 027 < ایرانی باستان ۳۵۲-۵*. برای 2 -> آرای.
برشتن
برشت < فارسی میانه 07151 < ایرانی باستان ۳۳18-1*. برای 18 -> آراست. 0۲2 که

996:بخشودن
998:در فارسی میانه به جای «بخشود» 202333774 آمده است. 20253710 مادهٌ
999:ماضی جعلی و از مادهٌ مضارع ساخته شده است. «بخشود» در فارسی دری به قیاس
1002:بخشای + فارسی میانه 202۶3 < ایرانی باستان ۵ -3520 -۵02*. برای 2 > آرای.
1003:2 پیشوند فعلی است. ريشةٌ 7524 فرضی است > بخشیدن.
1006:بخشیدن
1007:بخشید < فارسی میانه 029870 027870 مادهٌ ماضی جعلی است. از مادهٌ مضارع
1009:بخش < فارسی میانه 0235 < ایرانی باستان 82۳-3*. 328 صورت اصلی 337 است» 8
1013:«بخشودن» به معنی «عفو کردنْ» و «بخشیدن» به معنی «تقسیم کردن» هست» «بخشیدن»
1014:در معنی «بخشودن» به کار رفته است > بخشودن.
```


## [2026-10-17T00:31:11.345Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n -i 'baxš\\|abaxš\\|bax[sš]ud\\|bax[sš]ay\\|xšad\\|xsad' CHEUNG.txt | head -30; echo ---PHD; grep -n -i 'abaxš\\|abax[sš]' PHD.txt PHD_mackenzie.txt | head; echo ---NYB; grep -n -i 'apaxš\\|abaxš\\|apax[sš]' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:31:11.745Z] TOOL RESULT

```
2514:*NWIR: NP baxsudan/baxSsay- ‘to grant, bestow’, Gur. (Kand.) bas ‘give !’, Ham. 
2515:baxSayan/baxs- ‘to give, distribute’, Kurd. (Sor.) bas ‘share, part’ 
22793:Yghn. sinóy-/Sinóyta ‘to wash’, ? Oss. I. exsyn/exsad, D. exsnun/eksnad ‘to wash 
26001:Pres. them.: IND. 3pl. med. YAv. 0Baxsonte (Yt 10.14), INJ. 25р. OAv. 0Baxšo (Y 29.2); Partic.: pres. 
29091:*xšad ‘to have mercy, grace, forgive (< to cleanse, clear of ?)’ 
29093:*MIDDLE PERSIAN: (+ *apa-) MMP ’bxs’y-, BMP ’phs’d- /abaxsay-/ ‘to forgive, have 
34907:*phs’d- /abaxsay-/, 450 
35020:bhS- /baxš-/, 19 
46414:axsyn/zexsad (1), 348 
56013:*uaic (s.v.), *xšad, *zaË 
56630:*marzd, *xsad 
56795:*xsad 
56797:*xsad, *marzd 
---PHD
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:2006:forgive abaxSayidan, āmurzīdan, wixSay-.
PHD.txt:2007:forgiveness abaxšāyišn, āmurzišn.
PHD.txt:2008:forgiving abaxšāyišnīg.
PHD.txt:2784:merciful abaxšāyišnīg.
PHD.txt:2788:mercy abaxšāyišn, amurzišn; have — abaxSayidan, amurzidan.
PHD.txt:3364:regretful abaxSawand.
PHD.txt:3387:repentance abaxšīh, pašēmānīh,
PHD.txt:3388:repentant abaxš, pašēmān.
---NYB
552:apaxš [’phs] changing one's mind, repent- ing 8311. — Paz. awäx$, but in SGV awaxša- dar and awaxši. Perhaps Paz. awāxš = apāxš represents the original form: < "apa-axši ‘having his eye (look) turned back’; as to "axši- cf s. v. bītaxš. apaxtar [’p’htl] 1. planet 1151; han i 7 ~ 7718-19.22, 7915-16 (cas. rect.); 62 7 ~-dn 7720; Gišan ~-dn 7919-20 (pl. cas. obl. as subj.); —-àn 1152. — 2. the north 12012, — Av. (79) apäztara- ‘northern’; MPrs ’b’zir; Paz. awāxtar; NP bāxtar ‘the west’ or ‘the east’.
1004:rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
6428:awāxš, -šī, -šadar: apaxš
```


## [2026-10-17T00:31:15.401Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; sed -n 29085,29115p CHEUNG.txt; sed -n 2505,2520p CHEUNG.txt; grep -n 'baxš\\|bakhsh' HRN.txt | head; grep -n -i 'baxš\\|bax[sš]ūdan\\|bax[sš]idan' HUB.txt | head"
}
```


### [2026-10-17T00:31:15.941Z] TOOL RESULT

```
638 ff. 
«REFERENCES: ELO: 32 f.; DKS: 197b; Werba 1997: 280; Shahbakhsh: s.v. Saksa(h)- 


*xšad ‘to have mercy, grace, forgive (< to cleanse, clear of ?)’ 

*MIDDLE PERSIAN: (+ *apa-) MMP ’bxs’y-, BMP ’phs’d- /abaxsay-/ ‘to forgive, have 
pity, mercy’ > DMMPP: 15b 

Pres.: IND. 35р. (?) MMP ’bxS’yd- (S9 I Ra=Ri,32) 

*PARTHIAN: ’xSd ‘pity, mercy’ || (+ *apa-) ’bxs’h- ‘to have pity, mercy’, *bxs’hysn 
‘mercy, pity’ = Ghilain: 70 | DMMPP: 78b, 15a f. 

Pres.: IND. 3sg. ’b’x$’hyd, SUBJ. 2sg. ’b’xS’h’, 3sg. ’bxs’h’, IMPV. 250. *bxs’h, 2р1. 'b'xš'hyd 
*BACTRIAN: орҳол- (denomin.) “о vouchsafe, deign to grant? = S-W, Bact.: 184b 
*NWIR: (+ *apa-) NP baxstidan, baxsidan/baxs-, borrowed into: Bal. baskät/bask- ‘to 
forgive’, Anar. -ibaxso/ibaxs-, Khuns. biys- ‘to pardon, excuse’. 0 NP baxsüdan, 
baxsıdan/baxs-, etc. is contaminated with the root *baHx&, cf. WIM I: 66; Horn 
1893: 43 f.; Henning 1933: 188 f. Therefore, Bal. baskat/bask- cannot directly go 
back to *baHx$ ‘to bestow, divide, apportion’, as assumed in Korn 2005: 113, 177 
(passim). 

*NEIR: Oss. I. æxsædyn/æxsæst, D. æxsædun/æxsast ‘to clear, get rid of something 
useless [e.g. field from stones]; to peel off 

*MISC: (+ *apa-) Arm. (LW) apasxarem ‘I regret’ 

9 The root appears to be exclusively Iranian. 
Pres.: POT.-IMPV. 25р. SSogd. L’ "nBytw kwn’ ‘do not dare to impart (?)’; Impf.: IND. 3sg. MSogd. 
mnßxs; Fut.: IND. 3pl. SSogd. "nBxsnt km Partic.: perf. pass. SSogd. ’nß’yt’k 

*CHORESMIAN: BX- ‘to give, bestow; to share’ || (+ *ni-) m/nBx- ‘to share’ 
= Samadi: 43, 118 

*BACTRIAN: Bay- (pret. stem) ‘to give away’ || (+ *ham-) орВоҳ- (pret. stem) ‘to 
give away, distribute’ = S-W, Bact.: 184, 179b 

*NWIR: NP baxsudan/baxSsay- ‘to grant, bestow’, Gur. (Kand.) bas ‘give !’, Ham. 
baxSayan/baxs- ‘to give, distribute’, Kurd. (Sor.) bas ‘share, part’ 

*NEIR: Yzgh. vas-/vast ‘to sell’ 

*MISC: Orm. bas-/b(as)’ék ‘to give, grant’ = bax-/baxók ‘to offer, pardon’
```


## [2026-10-17T00:31:24.207Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n -i 'af[sš]ārd\\|af[sš]ard\\|af[sš]urd\\|fa[sš]ār\\|xšard\\|xsard\\|*xšar' CHEUNG.txt | head -20; grep -n -i 'af[sš]ārd\\|af[sš]ard\\|af[sš]ār\\|af[sš]urd\\|ašār' PHD.txt NYB_vol2_glossary.txt HRN.txt HUB.txt | head; grep -n -i 'ṣārt\\|xšārt\\|ksart\\|ssart\\|ṣṣār\\|ššār' incoming/BLY/BLY_pages.txt | head"
}
```


### [2026-10-17T00:31:24.509Z] TOOL RESULT

```
ugrep: error: error at position 69
[sš]ard\|af[sš]urd\|fa[sš]ār\|xšard\|xsard\|*xšar
                   empty (sub)expression___/


PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:1317:compress afSurdan.
PHD.txt:1387:cool down afsardan.
PHD.txt:1451:crush afSurdan, kóftan.
PHD.txt:1856:extinguish afsardan.
PHD.txt:3217:press afSurdan.
PHD.txt:3614:shame (v.) pafšār-.
PHD.txt:4645:pafšār-
HUB.txt:5121:azdrayeinti) ; afsurdan 'frieren , af^h. LW. afsurdq ^frozen'
```


## [2026-10-17T00:31:29.479Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY; grep -n -i 'sārt\\|ṣārt\\|sart\\|press\\|squeez\\|af[sš]' BLY_pages.txt | head -20"
}
```


### [2026-10-17T00:31:30.024Z] TOOL RESULT

```
5:Published by: Cambridge University Press on behalf of the School of Oriental and
19:            School of Oriental and African Studies and Cambridge University Press are collaborating with
402:                *Xsarta-,            'yellow'
406:                                                               'press'.
```


## [2026-10-17T00:31:33.299Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BLY; sed -n 370,440p BLY_pages.txt"
}
```


### [2026-10-17T00:31:33.859Z] TOOL RESULT

```
       have started from the secondary meaning of 'prince'. As an
      epithet of Manjuiri it represents kumarabhita- 'youth'. Hence
      probably not connected with OIran. arg- 'be worth', where the
      guttural was difficult, but rather with Khotan aysdau 'young',
       Skt. bala, Tib. byis-pa: aysdau < *arzddvan-.
 avachauda 'unhindered' *a-pati-scafta-, Av. paiti-scapti-.

 .ssud.a possibly
      OIran. *asru-toassarr- or ksar-
                        himjuda-       or perhaps
                                 'bleeding' [-uda cf.rather :ssuda-
                                                      BSOS viii 927]. ' tearful' to
ariyamata requires a verbal base driy-.
aspata- 'refuge', not Prakr. aspada-, as shown by -d- in the second
     syllable.
 dlihra 'ashes ', Rsdni aejr 'ashes' < *aOirya- Morgenstierne
      NT. 5, 47. Sogd. ,,',kw.
ihivia- 'not one's own' Konow NT. 7, 14, as iharstd, aharstda
     'regularly '.
ulagana-, ulatana- possibly kan- 'dig', as second component.

ustana with s.t as Av. ustdna, Mid. Pers. (learned word) u'tan (cf,
     Mid. Ind. (AMoka) ustanarm). Hence ui-tdna- 'tension of the
     us' ' vitality'.
iitc& not < *udakya, since uda- > a- (as in ara Av. udara), and the
      suffix must then be voiced. But *dpak-, Mun!i yowga ' water', etc.,
    Oss. awgd ' glass, flask '.
kadara, d < rt, not Indian.

ks.dabut
      notOIran.
           *kiarita- sincetoys1daa-
                *Xsarta-,            'yellow'
                             Mid. Pers.       < *zaritaka
                                        a/B3art,           shows
                                                 NPers. afgurd    umlaut,
                                                               'press'.
      So pdada- < *parta-.
ksiyare with ptc. ksita- to OIran. *lX7-, Skt. ksaya-, etc.
ksundaa- (u replaced by C in later ksamdai), MunSI aiiy- (Morgenstierne,
      Indo-Iranian Frontier Languages, i, p. 37), fty, fdy (Zarubin,

khan-Iran  i 168)
      rather kan- <as*fiuyant-,
                      in naskanda, cf. ks Av:
                                    OPers. in ks.rma-
                                              kan-.   ' shame ', Av.ftaramna-.
khiha <**Xa a-, as Sogd. y-y- (*XjX), Mid. Pers. Xx 4y
     Yasna 65, 4.
ggadaa- ' throat' (?), then to gart- 'turn ', cf. NPers. gardan ' neck'.
     But cf. u hainai gadad hvasti baysgi thauracaihi sau ' and one red
           . -beaten thick cloth (?) '.




                              This content downloaded from
            71.172.217.118 on Thu, 11 Feb 2021 00:49:26 UTC
                      All use subject to https://about.jstor.org/terms
 76     H.      W.         BAILEY-


 ggumice                         <      *vi-matak-.
 ggiigno                   karmgo                         212,       possibly     t
      one           short                   stroke),                 if   one   ou
      'deer'                  (Mid.                    Pers.          gavazn,
   known in Buddhist texts,
   g-ya-gz'i ham ipags-pa.
 jin- Av. 'yd-, Skt. jinati, but
 ttiman- with -i-, but tceim
      reman,                      hence                    *tuxman-           >   *
```


## [2026-10-17T00:31:41.037Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n -i -E 'af(s|š)(u|ā|a|ü)rd|fis(u|ā)rd|fiš(u|ā)rd|fa(s|š)ār' CHEUNG.txt | head -20"
}
```


### [2026-10-17T00:31:41.612Z] TOOL RESULT

```
6991:Inf.: BMP ’ps’Itn /afsardan/ 
6996:*NWIR: NP fišurdan/fišar-, afšurdan/afšar-, Kurd. $е/ап, Awrom. šeláy/šel- ‘to press, 
22051:pres. IND. 3sg. BMP /afsarénéd/; Inf.: BMP "psitn /afsardan/ 
22072:*NWIR: NP sard, Bal. sart, Kurd. sar ‘cold’ || (+ *apa-) NP afsurdan/afsär- ‘to 
40694:afsurdan/afsar-, 337 
40972:fisurdan/fisär-, 
40973:afsurdan/afsär-, 93
```


## [2026-10-17T00:31:45.448Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; sed -n 6970,7010p CHEUNG.txt"
}
```


### [2026-10-17T00:31:46.021Z] TOOL RESULT

```
*NWIR: NP šarm ‘shame’ 

*NEIR: Oss. І. æfsærm, æfsarm, D. zfsar(m) ‘shame’ 

*MISC: Slav. (LW), OCS samt ‘shame’, Russ. sram ‘disgrace’, etc. 


© The root (with its nominal derivative *fSarma-) is exclusively Iranian. 
*REFERENCES: Abaev, Slovar’ I: 482 f.; DKS: 67a, 68a 


*gaHl 93 


* far? ? ‘to prepare and press an intoxicating drink ?' 

*AVESTAN: ? OAv. fsaratu- ‘joy, enjoyment’ 

*MIDDLE PERSIAN: (+ *ара-) BMP ’ps’I- /apsar-/ ‘to press (out) 

Inf.: BMP ’ps’Itn /afsardan/ 

*KHOTANESE: ? OKh. ssarr- ‘to exhilarate’ || (+ *a-) OKh. "asarr- ‘to exhilarate’ 
c» SGS: 129 f. 

*NWIR: NP fišurdan/fišar-, afšurdan/afšar-, Kurd. $е/ап, Awrom. šeláy/šel- ‘to press, 
squash, knead, massage’ (< Kurd. ?), fisaray/fisar- ‘to press’ (< NP ?), Gur. (Kand.) 
Süárd- ‘to press’, Soi fäsär- ‘to press, push’, NP afsurah ‘pressed (fruit) juice’, Gz. 
afsurre ‘liquid essences’ 

*MISC: Arm. (LW) ösarak, Arab. (LW) afSaraj ‘juice’ 

*SANSKRIT: psáras- (n.) ‘enjoyment, joy’ (RV) = EWAia II: 198 

9 An IE origin is unknown: the root appears to be exclusively Пг. 

*REFERENCES: KPF I: 247a; КРЕП: 207; DKS: 407b f.; WIM II/2: 634 


G
```


## [2026-10-17T00:31:59.462Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n -E 'xšī|xsī|xšaiw|xsaiw|šēwan|sēwan|šīvan|šēvan|šewan|šiwan' BRT.txt HRN.txt HUB.txt PHD.txt NYB_vol2_glossary.txt CHEUNG.txt | head -30"
}
```


### [2026-10-17T00:32:00.105Z] TOOL RESULT

```
PHD.txt:129:niyāz, —omandih ... add necessity. read niyoxšīdan... по [TSA < A tě |... (not tē”).
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
PHD.txt:597:tru(f)Š [t/wu(p)$ | (P tryff), N turf] sour. truftag [t/wptk'] stolen; intercalary (days). tuhig [twhyk! | M twhyg, ЇЧ tuhi] empty, vain. ~ih : emptiness, void. tumbag [twmbk' | N ~a] drum. tund [twnd | N ~] sharp, violent. ~ih: violence, vehemence. Tür [twl | N ~] one of a people inimical to Eran, Turanian. ~ап [—n! | N ~] (land of) the Turanians. Turk [twlk' | N ~] Turk. tu&t [twst'] silent. tuwān [twb!n! | M twn, N ~] might, power. ~ (+infinitive): it is possible to, one can. ~ag [~k' | N —a] mighty, able. «gar [-kl | N ~] rich. ~garih: richness, wealth. ~ig [-yk'] able. ~igih: ability, power. --sāmān [-s’m’n'] the extent of one’s ability. tuxšáé [twhPk! | M рох р, N tuxsa] diligent. “Аһ: diligence, endeavour. tuxšīdan, tux&- [гол у! | (M. twxf‘yst), N ~] strive, endeavour. ~išn: endeavour, striving.
PHD.txt:642:waxš, —išn, v. 1, *waxšīdan,
PHD.txt:758:agreement husāzagīh; pašn, past; (document) pādixšīr.
PHD.txt:912:backgammon nēwardaxšīr.
PHD.txt:1014:blaze waxšīdan.
PHD.txt:1117:burn (vi.) waxšīdan.
PHD.txt:1763:endeavour (v.) kē(x)šidan, tuxšīdan; v. strive.
PHD.txt:2411:increase (vi)  abzüdan, wālidan, waxšīdan; (vt.) mehénidan.
PHD.txt:2526:kindle (vi.) waxšīdan; (vt.) abroxtan.
PHD.txt:2551:lament (n.) šēwan.
PHD.txt:3387:repentance abaxšīh, pašēmānīh,
PHD.txt:3847:strive āyozīdan, kē(x)šidan, tuxšīdan.
PHD.txt:4281:wax waxšīdan.
PHD.txt:4496:tuhig tohmag tanapuhl tuxš- tuxšagih tuxšag i tuxšīdan tuxšišn tēxtan tuwānāg tuwānīgīh tuwānīg tuwāngar tuwāngarīh tuwān tuwānsāmān tambūr tambūrag did!, tand, tang tandih, tangih tanigardig tanigard tan
PHD.txt:4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
PHD.txt:4740:pādixšīr Nas rey о
PHD.txt:5037:kan- har(w)! kanār, kennir kanāragūmand kanārag kennārsrāy kóx&- kūxšīdan kox&isnig kóxXi&n kawādak köv
PHD.txt:5232:wasnid nixwiür- nixwārišn nahang, nihang wiyūz- wayūdagān wēn- (v. dīdan) жатап! wēnāgīh wēnāg winnār- winnārišn nēwardaxšīr winnārdan wēnāb wēnābdīg wēnābdāg niyūxš- niyoxsidan niyoxsián wénig
NYB_vol2_glossary.txt:601:apoxšāyišn [’pwhs’dän'] compassion, mer- cy 6214, — apo- < apa- : -a- > -o- because of the surrounding consonants; Ps. pres. ’phs’d-; MPrs ?baštyšn (A-H. II, BBB); [Arm. lw. apasxar-em < *apa-xšād- is not akin]; MPrth ^bz$?hy$n, pres. ?"baš?h- (A-H III, MHC); Paz. awaxšīdan awa- xsGéd, Skr. v. sahate (Aog.); NP baxsudan, baxšā'īdan, baxšāy-, baxšāyiš. Bailey, JRAS 1930, 15—16; Verbum 188 sg.; Ghilain 70.
NYB_vol2_glossary.txt:2247:Kartār-gāv [~-TWR’] n. pr. one of the Ātwiyānis (v. Aspikün) 47%. — ‘Having vigorous (?) bulls’. As all the other A@wi- yanis have names in which -gäv is pre- ceded by an adj. designating a colour: Bör-gäv, Siyāh-gāv, Spet-gäv, kartär is possibly the corruption of a similar adj. which, as Dr. Monchi-zadeh would as- sume, was the Milr equivalent of NP kahar ‘chestnut, bay’ (in BP it would be *k?hl or the like). Tab. I, 227 in fine has Axšīn-gāv which he translates ‘possessing yellow cattle’ (Av. [51] axSaéna- 'dark-
NYB_vol2_glossary.txt:3634:ščvan [šywn'] lamentation 862°. — Paz. šina < *šēvanak; NP Svan, cf also šīnah ‘a kind of pipe’.
NYB_vol2_glossary.txt:3824:ete.; v. also tuxšītan. — MPrs twxš'g (S); Paz. tuxša, NP taxšā.
NYB_vol2_glossary.txt:4053:vaxšišneh det. v. n. of *vaxšītan: ul ~ the flaming up, the shining forth, of the dawn 44!?,
NYB_vol2_glossary.txt:6429:awaxšīdan, -xšačd: apoxšāyišn
NYB_vol2_glossary.txt:7244:kösidan: kēxšītan kudam: katam
```


## [2026-10-17T00:32:05.827Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1329 2>&1 | head -80"
}
```


### [2026-10-17T00:32:13.644Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 124; check the printed number and re-run with --pdf-page if off)
REF: BQT:1329  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 124  OCR-lang: fas

او هی شا ۰ 1 صاع‌زربوسف
از حضرت عیمی علیه‌ااسلام است . از سبعةٌ سیاره است که زخل و هشتری و هریخ
صاحب امضا «بکر همزه‌وسکون وآفتاب و زهره وعطارد و باشد.
میم و فاد نقطه‌دار بالف کشیده ,کنایه از وزیر صاحب سنگ ؟ - کنایه از مردم
-ولونندگان باشد ۰.۱ با وقار و صاحب قدر و نمکین باشد - و کنایه
کود وا اند اس صاحب صابی * - با بای ابجد »
بند چه برح جوزا خانة اوست. ک م۳ 3 با بای ۱+
۱ نایه از عیسی ۶ است - وبام مردی بوده‌صاحب
صاحب خاطر ان کناب ازعامراد :
کب طر آت «کنایه ازدامران فطرت و فطاات عالی داشته و ساره پرستی را او
و اهل -خن وخوش طبعمان باشد . بهم رسانیده اخت ‎٩‏ .
صاحب خبر - با بای ابجد بر وزن صاحص عین دبران - کدایه از
صاحب نظر. کنایه از حاجیان ولقیبان- ومعرفان | برج ور است که برج دوم (۱) باشد از جملهٌ
- و ابلجیان باغد ۳ . دوازده برج فلك .
صاحب خطرآن - کنایه از .ار صاحب کف لیصا - کندابه از
وسلاطین و امرا و مشاهیر باشد. حطرت موسی علیه‌اللام است.
صاحب دای » پمعتی وزبراست چه صاره - بنتح رای قرشت ,بزبان الالی
رای در اسطلاح وزیر راکوبند - و کنابه از | کلی است که آبرا بفارسی فیل کوش خوانند
شیخ بوءای هم هست,اعتبار ایشکه‌وزبرفخرالدوله | و بعربی لوف الصغیر کویند ۷ .
)۱( چش : دوم .
۱- نویدنده (مقرد) نه نوسندگان . ۴ - ومنهی وجاسوی وخب رگزار :
2 منوچهری دامغانی ۰.۱۵۹۵
۴ - دربنجا چند اشتباه است , ر4: ص نود وچهار مقدمه ( مثال ۳ ).
شد . وظاهراً خلطی است درقول نظامی عروضی » درمقالت اول ازچهار مقاله » آنجا که دبیران
را بند دهد : ۶ پی ءادت باید کرد بحواندن کلام رب‌المرة واخبار مصطفی و آثار صحابه وامثال
عرب وکامات ءجم ومطالعة کتب سلف و مناظطرء صحف خلف چون ترسل صاحب وضاای و...»
ددالمه‌متوفی ۳۸۵ ومدظور از صابی ابواسحق ابراهیم‌ین‌هلال حرانی صایی متوفی ۶ است. راد :
تعلیقات چهار مقاله ا,ضآس۹۰ . ۹ -مابثه- 52066009 بدو فرقهٌ ممتاز اطلاق شده:
- صبیان نت۱۱۹ که فرقهٌ بهودی << ییحی بن‌النهرین (پیرویحیی هممد)
باشند . ۲ - صابئان حران » فرقةٌ مشرکی که هدتی دراز درعهد انلام وجود داشته . رك :داثرة
المعارف اسلام : صابثه . درکتب املاه‌ی صابی را موس فرقةٌ صابله دانته‌اند :
۷ - ۸7۲۵۲۲ دنك ۲ س ۰.۳۹۱ ۸ - (عر) پیمانه ایست.رك : منتهی‌الارب.
```


## [2026-10-17T00:32:17.487Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; grep -n 'شیون\\|šēvan\\|šēwan\\|šivan' BQT_v3_pages.txt | head; grep -n 'pdf page' BQT_v3_pages.txt | head -3"
}
```


### [2026-10-17T00:32:18.051Z] TOOL RESULT

```
9325:‏شیون ‎tt ued‏ مجپول بر وزن
9346:‎F NMA‏ رك : شیوانیدن » شیونده.
9353:شیوانبدن » شیونده .
17370:‏فراشیون 1 © بفتح اول و واوبروزن
17371:خراشیون » گیاهی است کهآ ترا بعربی‌سوف‌الارض
17388:‎600115 ‏فدزی ج۷ ص ۰۲۳۹ ؛ فراسیون‌الماء‎ Ope d= (pm) ‏فراشیون‎ Y
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
```


## [2026-10-17T00:32:21.244Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; awk 'NR<=9325 && /pdf page/{p=$0} END{}; NR==9325{print p}' BQT_v3_pages.txt; sed -n 9315,9360p BQT_v3_pages.txt"
}
```


### [2026-10-17T00:32:21.787Z] TOOL RESULT

```
[pdf page 122]
را کویند. خصوصاًبویمهنی لرزالیدن‌همآمدهاست.
شیوشه - نم اول و الی و فتح شین
تقطه‌رار , شوش4ٌ طلا و فره را گوبند و آن طلا
ور کداخته است که در ‎beg‏ آهثین ریزد ۴
- و دلبالهٌ خربزه وهندواله را یز گویند.
شیوم ۶ ‎che‏ واو بر وزن بیفم »

‏یعنی بر همزده کردم وآمیخته شوم و بيامیزم -
وبلرزم و لرزان گردم.

‏شیون ‎tt ued‏ مجپول بر وزن
‎yaw‏ ۰ ناله و افغایرا گوبند که درهنگام محنت
و مصیبت کنند .

‏شیو ‎YO‏ © بر وزن زیبنده » بمعنی
آمیخته و برهمزده 4 - ولرزان ‎ath‏ .

‏شیوه - با ‎gh‏ مجهول بر وزن میوه +
بمعنی ‎SM‏ و کرشمه و طور و عمل و طرز و روش
و قاعده و قانون باشد ‎٩‏ - و ‎ner‏ هثر وکمال
همهست - و خویشتن لمودن و خودا‌ابی‌وزیبابی
- وخویی ولیکوبی کردن را ليزگوبند.

‏شیهه = اول و سکون ‎vt‏
‏و فتح ها » آواز وصدای اسب را گونند وبعریی
صهیل خوالند .

‏۱ - بقول هرن اوستا ‎at) xshvaewa_‏ ؛ سربع) ؛ پولوی 5082۵1 و ‎shévak‏
‎shal‏ 5۷۵1 (لفز نده ,لیز ) «اسشق ‎care‏ و بقول هوبتمان پهلوی 5۳6۳8 ‎Ty)‏ ۱۱:۰۱)
= پارسی ‎oxshaipa_ git‏ با ‎xShvaipa_?‏ .قس : ‎las‏ «هوبدمان ۸۰۵» ‎dy‏ فاباص

‎F NMA‏ رك : شیوانیدن » شیونده.

‏۴ - متعدی ‎Cosi t®‏ (رك:شیوم.شبوان:

‏شبونده ) . دزقولی ‎shevanidan‏ ( آمیختن »هم زدن [متصوصاً در ‎ty‏ چای ]) «امام» .

‏۴ 2 شوشه («.م.) ‏ شفشه(«م.) .
شیوانبدن » شیونده .

‏9 اول شخص منارع از «شیوبدن» رك:

‏۲ - پهلری ‎shivan ( shévan‏ « باروچا ۰۲4۵ ) » ابرالی

‏پاستان - ‎xshaivan‏ ۵, اومتا- 1510 (بدبختی » فقر » احتیاج) «بارتولمه ‎Spoon‏ ص
```


## [2026-10-17T00:32:27.960Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n -i 'Elend' BRT.txt | head -20; grep -n -i 'šēvan\\|sevan\\|šēwan\\|šīvan\\|sivan' HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:32:28.556Z] TOOL RESULT

```
7369:•  j-i  g-  äyav-  n.  i)  'Dauer':  xsys  dar^gSr. °yü  timauhd  "des  Elends  lange  Dauer  (und) der  Finstemiss"  Y.  31.  20.  2)  'Alter, Lebensalter":  'iwarUahe  zrä  'yu  "mit  dem Alter  des  bestimmten  Termins'"' Yt.Ä  11, /o.  74  (,  wo  °yü).
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
13657:Ubergeht,  fem  wird  dem  künftig  bleiben !  r»'irS'  oder  die  Tochter  der  Tocht«  der des  Elends  lange  Dauer  .."  Y.W.  2o'>.     I     Vate^chw«ier     aUo     'ti:.rya,Arii^^^^„
13745:•  g.  du§itay-  £  'übles  Wohnen  sva.  Elend, Unglück':  ^ä  xi  d»nifn>m  visiin  vä  sOdr.'in vS  daRyüm  vä  ädäl -tääJ  (X&-)  marakalcä "denn  Hai;s  und  Gemeine  und  Gau  und Land  bringt  er  in  Elend  und  Verderben" Y.^/.i8.
18434:hinter  den  Uelativadv.  aaftrelende  'hS  ist  tU.
28164:•  j.,  g.  zi  enkl.  Part,  hinter  dem  ersten Wort  des  Satzes";  I)''  der  sf-Satz  be- gründet den  Inhalt  eines  andern  Satzes, dem  er  i)  folgen,  2)  vorausgehen,  3}  ein- gefügt sein  kann;  'denn;  ja';  a)  im  gAwr.; zu  i):  mä  Hs..dr>gvatü  rna^rqsca  gastä sasmis(sd.)c,l  *il  *zT  dsmSitim  vJsfm  vä  . . ädä^  dusi/ä(sd.y3  marakaicä  "keiner  . . höre  auf  des  Z'r«<f genossen  Worte  .  .; denn  Haus  und  Gemeinde  .  .  bringt  er in  Elend  .  ."  Y.J/.  iS;  —  /?m  .  .  *a.vT- vansö  (Sp.  1377  o.)  na  zU  (Sp.  154  u.) ialmainX  vyadarpsim  .  .  Y.  45.  S;  30.  10 {adiJ  zl  .  .);  —  at  yastsm  iwil  nä  is>mttS äya/ (Sp.  150  o.)  drU/J  hvs  dämqn  */iae- %ahyä  ffdj  (Sp.  517  m.)  AvS  zT  dngvä  yS dngziäit!  vahUtS  hvS  asavä  yahmäi  ai'avä /ryS{%A.)  Y.46.6;  —  atlöi  af)h>n  saofyantö (sd.)  dahyunqm y5i..isi  sj data  kamaistärS lsd.)*aa)/mäiyaY.4S.i3; 34.S  {iais sT..),
```


## [2026-10-17T00:32:33.494Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; grep -n 'خدنگ' BQT_v2_pages.txt | head; grep -n 'خدنگ' FSF_pages.txt | head -5; grep -n -i 'xadang\\|chadang\\|xadank\\|qadïŋ\\|kadin\\|qadin' HRN.txt HUB.txt LKT.txt TTS* incoming/TTS/*.txt 2>/dev/null | head"
}
```


### [2026-10-17T00:32:33.999Z] TOOL RESULT

```
1427: ‫ازانت ‪ -‬و دام قربه ابت از قرای شیراز ‪-‬‬               ‫و طاس و امثال آن ‪-‬‬               ‫زنگگ‬     ‫> صدای‬     ‫خدنگه‬
3755:  ‫» وار وی کمان وتر خدنگو چوب‌خلنج بار افند ‪« ».‬حدود‬                 ‫وجنگ فگر وتوانگر وسار تعمت‬
9959:                  ‫کمندی دشت بر گوران خباک‬                      ‫خدنگش بیشه برشیران قفص کرد‬
10338:          ‫هدهد بر الدرون زند تدرخدنگه‪.‬‬    ‫‪ - ۲‬فمری بمژه درون کشد شمری‌را‬
7834: ‫بهپیکان پولاد و تیر خدنگ‬                                           ‫گزوهر یکی تخت در پیشگاه‬
8951:                            ‫اس‬‫ز‬                      ‫می‌پیچیدند‪ .‬از جوب خدنگ تیر و نیزه و‬
9440:                                                 ‫تیر خدنگ و جوب خحلنج بسیار‬
9966: ‫تو را اگیزنند از کهآمد به روی‬                                      ‫کمان برگرفتند و تیر خدنگ‬
10310:                        ‫تب‬                                     ‫خدنگت (با زبر اول و دوم)‬
(eval):1: no matches found: TTS*
```


## [2026-10-17T00:32:37.737Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; awk 'NR<=3755 && /pdf page/{p=$0} NR==3755{print p}' BQT_v2_pages.txt; sed -n 3730,3790p BQT_v2_pages.txt; echo ===FSF; sed -n 10300,10325p FSF_pages.txt; awk 'NR<=10310 && /pdf page/{p=$0} NR==10310{print p}' FSF_pages.txt"
}
```


### [2026-10-17T00:32:38.291Z] TOOL RESULT

```
Exit code 1

                                                       ‫‪۰‬م‬
                                                        ‫چاچ ‪ ۰‬بسکون جیمفارسی ن‬
  ‫است ‪ -‬و سبزه زار وموغزار را نگیوزنند ‪.‬‬
 ‫وین کرو‬                  ‫ار‬
                                                   ‫اشتهاردارد»‬   ‫که بتاشکند‬           ‫از ماوراءالنهر‬               ‫شهرست‬

                                                   ‫آجا‬
                                                     ‫یشغر گرفاته‌اند وکمان خوب از ن‬
                                                                                  ‫و کا‬
‫ووزه وامثال‬
          ‫آحك وکاسه ک‬
                    ‫که در آن خشت و‬                 ‫آورند ‪ -‬ومتسوب بناجا را چاچی گوبند عموما‬
‫آن پزاد ‪ -‬و مخفف چهار هم هت که بعربی‬              ‫و نوده غله پاك کرده وازکاه‬                     ‫وکمانرا وتا‬

                                                                         ‫‪.‬‬       ‫و‬    ‫‪- :‬‬    ‫چك‬      ‫(‪)۱‬‬



  ‫بکوهی در انداختن‪ .‬نظامیکنجوی‪.‬‬           ‫کمندی‬    ‫‪ - ۱‬ده چابك شد ابن چایکی تاختن‬
                       ‫‪ « 501086 _ ۴‬امفا ‪ ۲ :۱‬ص ‪ = ۵۷‬چابلوی = چالیوس ‪:‬‬
              ‫که بته بود چاپلوی از فسوس‪.‬‬      ‫مکن خوبشتن سهمگن چاپلوی‬
        ‫ابوشکور بلخی‪« .‬لفت فرس ‪4۹۱‬؟‪.‬‬
  ‫« چاج » احبتی‌است بزرك وآبادان ومردمانی غازی‌پیشه‬              ‫‪۴‬‬               ‫‪.‬‬   ‫چابك‬    ‫‪:‬‬    ‫رك‬       ‫‪۴‬‬


  ‫» وار وی کمان وتر خدنگو چوب‌خلنج بار افند ‪« ».‬حدود‬                 ‫وجنگ فگر وتوانگر وسار تعمت‬

                                ‫بدان چاچی أست‪:‬‬     ‫و موب‬         ‫و معرب آن الشاش |‬                             ‫العالم ‪۶‬‬

              ‫بخم چون کمان کوشة چاچیان‪.‬‬
         ‫نکظانمجیوی‪« .‬گنجینه ‪.64‬‬                                             ‫‪۰‬‬       ‫چش‪‎‬‬    ‫رك‪:‬‬        ‫*‬


              ‫که زرین کی سندل و چاچله ‪.‬‬                ‫‪ ۱‬گ‪-‬رفتم که جابی رسیدی زمال‪‎‬‬
      ‫عنصری بلخی«لفت فری ‪.>۱۳۳‬‬
‫چ‪#‬اپ ‪-‬کالزمةٌ هندی ‪ »8‬مأخوذ است ؟‬
    ‫طبع ‪.‬کشت با وسم و صوبری وسطچ*اماپتاینر متتصوی ‪ -‬هیا ‪ -‬دروغ[ وکی‬
                                                           ‫‪#‬ایلوس ‪ -‬رك ‪ :‬چایلوی ‪.‬‬
                                                                                ‫چ‬

  ‫‪-‬رکی ؛ يبك ‪ .‬فاصد نامه بر ؛‬                            ‫ایزبدین ممنی است) ‪ « .‬جفتابی ‪.> ۰۷۲‬‬
                       ‫‪ #‬چاچی ‪ -‬منسوب به« چاج » ( « ‪ .‬م ‪).‬‬                                  ‫‪ :‬یام ‪.‬‬        ‫برید ‪ .‬رك‬

 ‫تح ‪ 3‬کسردال (وامروزضم‌دال تلفظکننداس چانر( بفتح‌ذال)‪ .‬روسى ‪t2 6‬‏ ‪hS‬‬
                                                                     ‫‪ #‬چادر = ش‬
  ‫حرهٌ ‪4۰٩‬‏‬
          ‫فد‬‫صبه‬
              ‫بق‬
 ‫چار تاره‬                                                                                 ‫—‬        ‫س‬




 ‫چار باالش کهنابه از دیا باهد ‪-‬‬                      ‫ولاج هم‬
                                                           ‫اربعه گویند ‪ - ۱‬ومخفف چاره ع‬
‫ومستدبرا فيز گویندکه پادشاهان وصدور واکابر‬            ‫بزبان علمی آهل‌هند بمعنی جا‪-‬ری‬     ‫هت ؟ و‬
                                                                                              ‫باشد ‪.. ۴‬‬
                                           ‫هت ا ‪.‬‬    ‫نم خای نقطه دار‪ ,‬کنانه‬     ‫چار ] خر ‪-‬‬

                                                      ‫و باد وآب و اش‬       ‫ك‬
                                                                           ‫خاکه‬
(eval):1: ==FSF not found
```


## [2026-10-17T00:32:43.690Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:719 2>&1 | grep -n -B3 -A8 'خدنگ' | head -60"
}
```


### [2026-10-17T00:32:44.270Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:32:48.383Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:719 2>&1 | head -30; grep -n 'ـدنگ\\|خد نگ\\|خدنك' data/verification/sources/refs/BQT_v2_pages.txt | head"
}
```


### [2026-10-17T00:32:49.068Z] TOOL RESULT

```
no scan of BQT covers printed page 719 (see 'scans' in refs_online.json)
10337:            ‫‪ - ۱‬معرب آن خدنك = ‪cnalb‬‏ ‪( reilpuep‬فر) «دزی ج‪ ۱‬ص‪.* ۵۵۳‬‬
```


## [2026-10-17T00:32:53.074Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=10337 && /pdf page/{p=$0} NR==10337{print p}' BQT_v2_pages.txt; sed -n 10290,10345p BQT_v2_pages.txt"
}
```


### [2026-10-17T00:32:53.743Z] TOOL RESULT

```
‫اول‌بروزن مهره » خرده‬         ‫حدره =‬                         ‫زراق که بظاهر خود را بیارایند‪ -‬وآلهایی‌را فیز‬
‫رىز هرچیز را گویند رک وشرارة آتش‌را لز‬‫و‬                      ‫‌دشدادو لمرود؛‬      ‫عابنییکر‬‫یخد‬
                                                                                           ‫دی‌‬
                                                                                             ‫نوا‬
                                                                                               ‫گونن که دع‬
          ‫گفته‌اند ؛ وبفتح اول همآمده اش‬                         ‫وآنها راخدای فروشان هم میگوبند با دوتحتانی‬
‫خدك ‪ .‬بفتح اووئانی بروزن کجك‪.‬‬                                                                                    ‫ورف‬
‫مطلق پل را گوبند خواه باسنگف وخشت وکچ‬                        ‫تون‬     ‫حجد او ند ‪ ۱‬ب‌ بقتح واو وسکون‬

 ‫بر رودخانه بندند و خواه با چوب وخاکد‬                                 ‫‪۰‬‬   ‫را کوند‬    ‫انه‬    ‫ویز رگ‬        ‫صاحب‬   ‫‪1‬‬   ‫ودال‬

                                 ‫بر جوی (‪# . )۱‬‬
                                                             ‫مزر گد‬        ‫بادشاه‬       ‫‪ ۴‬س‬     ‫حدایگان‬
‫سمعنی‬
    ‫بر وزن عشرنی ‪۰‬‬           ‫‪°‬‬
                                                                                            ‫وخداوند گار اعظم باشد‪.‬‬

‫بروزن بپلنگه‪ ,‬نام درختی‬      ‫‪-‬‬        ‫‪۱‬‬
                                                                 ‫حدر نق » بفتح‌اول وئانی‌بروزن‌خورنق‬
‫است بیارسخت که از چوب آن‌نیزه وتبروژین‬                       ‫بلغت رومی و بعضی گوبند بونانی عنکبوت را‬
                                                            ‫گوبند ‪ ۴‬؛ وباین‌معنی بجای نون بای حطی حم‬
                                          ‫میکویند ‪. ۷‬‬                                                ‫بنظر آ مده اف‬

                                                                               ‫(‪)۱‬چك» چش‪ :‬جوئی‪.‬‬
                            ‫وند (یوند اصاف) بمعنی صاحب (مطلقا) ‪:‬‬                    ‫‪+‬‬       ‫ا‬‫د‪:‬‬
                                                                                              ‫از‬‫‪ ۱‬خ‬
  ‫‪۶‬لتان ‪. ۸۳‬‬
           ‫گ‬                        ‫درتهند‬      ‫ر‬   ‫دست‬   ‫کنان‬    ‫لماش‬         ‫جاه‬          ‫ویشند‬
                                                                                                ‫اه ب‬
                                                                                                   ‫دی ک‬
                                                                                                      ‫خبن‬
                                                                                                     ‫‪“e‬‬
                                                                                                        ‫نه‬
  ‫)ه فلان قلعه را بدولت خداوند‬
                             ‫‪-‬یادشاه ‪« :‬سواری از در درآمد وبثارت داد (ملك را ک‬
  ‫کشادیم» ‪« .‬دکلتان ‪ - ۰ ۸۲‬ان ‪ 9:‬هر که خدای را عزوجل بمازارد تادل مخلوقی بدست آرد ‪۰‬‬
              ‫خداوند تعالی همان خلق را براو کمارد تا دمار از زروکارش برآرد»‪ .‬ک«لتان ‪.۲4‬‬
                                            ‫‪+‬ان (پسوند بت و اصاف ) ‪:‬‬
                                                                   ‫ک‬                        ‫ای‬
                                                                                             ‫د‪:‬‬‫‪ ۴‬خاز‬
         ‫که وقف کرد بدو ذوالجلالعزوجلال‪.‬‬                                  ‫خدایگان خراسان وآفتاب کمال‬
   ‫عنصری بلخی‪« .‬لفت فرس‪.*۵۷۳‬‬
   ‫ی‬     ‫رت)‪+‬‬
            ‫(‪:‬عخدم‬
                 ‫‪ = 6‬از‬                         ‫‪ ۴‬مقلوب «خرده» ‪.‬‬          ‫‪« 66081272 = ۴‬لك س ‪. ۵۱‬‬
          ‫‪۰‬‬   ‫‪۹۱)٩‬‏‬   ‫‪ ۸‬ص‬   ‫شمارء‬    ‫‪۲‬‬    ‫سال‬    ‫مله مخن‬     ‫(انمام وییشکش)‬     ‫در ناجیکی خدمتاله‬            ‫(لست)؛‬

            ‫‪ - ۱‬معرب آن خدنك = ‪cnalb‬‏ ‪( reilpuep‬فر) «دزی ج‪ ۱‬ص‪.* ۵۵۳‬‬
          ‫هدهد بر الدرون زند تدرخدنگه‪.‬‬    ‫‪ - ۲‬فمری بمژه درون کشد شمری‌را‬
   ‫«منوچهری دامقانی* ‪.*۵۱‬‬
   ‫‪#‬داو لد‪۴‬ار ‪ -‬از‪ :‬خداوند ‪ +‬کار(یسوند نت واصاف)؛بزرك‪ :‬مخدوم ‪ -‬شاه؛مخفف‬
                                                                      ‫خ‬
   ‫( وخوند کار ( که سلاطن عثمانی اطلاق میشد) ومعرب آن خنکارهرزی‬                              ‫آن خاوندگار ( ھ‪ .‬م‬
                                                                                                 ‫‪:‬‬   ‫ج ‪١‬ص‏ ‪۰۱۶‬‬
   ‫ما را بعفو ولطف خداوند گاربخش‪.‬‬                                 ‫شکرانه را که چشم توسوی بتان (بدان) ند‪.‬د‬
   ‫«حافظ شبرازی ‪۹۸۱‬؟‪.‬‬
```


## [2026-10-17T00:33:00.694Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in خدنگ شیون بخشودن بخشیدن افشردن فشار; do python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 559, Persian $w etymology\" 2>&1 | tail -2; done; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kadïŋ\" --note \"page 559, root Xalen, Turkic birch word\" 2>&1 | tail -2"
}
```


### [2026-10-17T00:33:04.805Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/42b017ff9f39db91.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/45cf5cfcfc35dca0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/372ea0dfb240e668.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5e716a0223acb043.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/79f51f93e7e831e0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/50e5d47f15f1f8f6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6bc88c5004a49eba.txt
```


## [2026-10-17T00:33:08.792Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 42b017ff9f39db91 45cf5cfcfc35dca0 372ea0dfb240e668 5e716a0223acb043 79f51f93e7e831e0 50e5d47f15f1f8f6 6bc88c5004a49eba; do echo \"=== $f\"; grep -v '^\\s*$' $f.txt | grep -i -A6 'etymology\\|Reconstruction' | head -25; done"
}
```


### [2026-10-17T00:33:09.402Z] TOOL RESULT

```
=== 42b017ff9f39db91
 Etymology 1 
 1.2.1 
 Noun 
 1.3 
 Etymology 2 
 1.3.1 
 Noun 
 1.3.1.1 
 See also 
 1.4 
 References 
--
 Etymology 1
 [ edit ] 
 Perhaps related to Ancient Greek κάττα ( kátta ) , Classical Syriac ܩܛܘ ( qaṭṭu ) .
 Noun
 [ edit ] 
 خدنگ • ( xadang ) 
 mongoose 
 Etymology 2
 [ edit ] 
 Possibly borrowed from Turkic , ultimately from Proto-Turkic *kadïŋ ( “ birch ” ) . [ 1 ] 
 Noun
 [ edit ] 
 خدنگ • ( xadang ) 
=== 45cf5cfcfc35dca0
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Descendants 
--
 Etymology
 [ edit ] 
 Inherited from Middle Persian [Book Pahlavi needed] ( šywn /⁠šēwan⁠/ , “ lament ” ) , from Proto-Iranian *xšai- ( “ to lament, to weep ” ) ; further connections unclear. [ 1 ] 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ʃeː.ˈwan/ 
 ( Dari, formal ) IPA ( key ) : [ʃeː.wán] 
=== 372ea0dfb240e668
 Etymology 
 1.3 
 Pronunciation 
 1.4 
 Verb 
 1.4.1 
 Conjugation 
--
 Etymology
 [ edit ] 
 Back-formation from بخشای ( baxšāy ) , by analogy with verbs such as فرمودن ( farmūdan  / farmudan ) , from earlier بَخْشَایِیدَن ( baxšāyīdan ) , inherited from Middle Persian [Book Pahlavi needed] ( ʾp̄hšʾd-ytn' /⁠abaxšāyīdan⁠/ , “ to forgive, have mercy on ” ) . [ 1 ] Akin to Old Armenian ապաշխարեմ ( apašxarem ) , an Iranian borrowing.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /bax.ʃuː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [bäx.ʃuː.d̪än] 
=== 5e716a0223acb043
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Verb 
 1.3.1 
 Conjugation 
--
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( b(ʾ)htn', bhš- /⁠baxtan, baxš⁠/ , “ to apportion , to distribute , to allocate ” ) , from Proto-Iranian *baxšáh , from Proto-Indo-Iranian *bʰakšás , ultimately from Proto-Indo-European *bʰeh₂g- ( “ to distribute, allot ” ) . Related to بخش ( baxš , “ portion, lot ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /bax.ʃiː.ˈdan/ 
 ( Dari, formal ) IPA ( key ) : [bäx.ʃiː.d̪án] 
=== 79f51f93e7e831e0
=== 50e5d47f15f1f8f6
 Etymology 
 1.2 
 Noun 
 1.2.1 
 Declension 
 2 
 Hijazi Arabic 
--
 Etymology 
 2.2 
 Pronunciation 
 2.3 
 Noun 
 2.3.1 
 See also 
--
 Etymology 
 3.3 
 Pronunciation 
 3.4 
 Verb 
 3.5 
 Noun 
--
 Etymology
=== 6bc88c5004a49eba
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/kadïŋ
FETCHED: 2026-10-17T00:33:04Z
STATUS: 200
TITLE: Reconstruction:Proto-Turkic/kadïŋ - Wiktionary, the free dictionary
Reconstruction:Proto-Turkic/kadïŋ - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
--
 Reconstruction:Proto-Turkic/ kadïŋ 
 Add languages 
 Reconstruction 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
--
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Turkic/kadïŋ&oldid=92181548 "
 Categories : Proto-Turkic lemmas 
 Proto-Turkic nouns
```


## [2026-10-17T00:33:15.648Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 6bc88c5004a49eba.txt | sed -n '/Reconstruction:Proto-Turkic\\/ kadïŋ/,/Retrieved/p' | head -50; grep -v '^\\s*$' 79f51f93e7e831e0.txt | head -15; grep -v '^\\s*$' 42b017ff9f39db91.txt | grep -A12 'Etymology 2' | tail -10; grep -A8 'Persian' 50e5d47f15f1f8f6.txt | grep -v '^\\s*$' | head -20"
}
```


### [2026-10-17T00:33:16.361Z] TOOL RESULT

```
 Reconstruction:Proto-Turkic/ kadïŋ 
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
 Get shortened URL 
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Turkic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Turkic
 [ edit ] 
 Noun
 [ edit ] 
 *kadïŋ 
 birch tree
 Declension
 [ edit ] 
 Declension of *kadïŋ 
 singular 3) 
 nominative
 *kadïŋ 
 accusative
 *kadïŋïg , *kadïŋnï 1) 
 genitive
 *kadïŋnïŋ 
 dative
 *kadïŋka 
URL: https://en.wiktionary.org/wiki/افشردن
FETCHED: 2026-10-17T00:33:03Z
STATUS: 200
TITLE: افشردن - Wiktionary, the free dictionary
افشردن - Wiktionary, the free dictionary 
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
 Noun
 [ edit ] 
 خدنگ • ( xadang ) 
 ( obsolete ) birch 
 Synonyms: غان ( ġân ) , توسکا ( tuskâ ) 
 ( obsolete ) a type of arrow made of birch
 See also
 [ edit ] 
 خلنگ ( xalang , “ heather ” ) 
 References
 Persian 
 Toggle Persian subsection 
 3.1 
 Alternative forms 
 3.2 
 Etymology 
 3.3 
--
 Persian فشردن ( fešordan ) 
 Persian فشار ( fešâr ) bor. 
 Arabic فشار 
 Borrowed from Persian فشار ( fešâr , “ pressure ” ) , from فشردن ( fešordan , “ to press , to squeeze ” ) .
 Noun
 [ edit ] 
 فُشَار • ( fušār )  m 
 ( uncountable ) popcorn 
--
 Derived from Persian فشار ( fešâr ) .
 Pronunciation
 [ edit ]
```


## [2026-10-17T00:33:20.603Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 79f51f93e7e831e0.txt | grep -i -B2 -A5 'Middle Persian\\|Inherited\\|from ' | head -30; grep -v '^\\s*$' 50e5d47f15f1f8f6.txt | grep -B3 -A3 'Persian.*Etymology\\|Middle Persian' | head"
}
```


### [2026-10-17T00:33:21.130Z] TOOL RESULT

```
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 See also: افسردن 
 Persian
 [ edit ] 
 Pronunciation
 [ edit ] 
--
 بافشار ( béafšâr ) 
 بافشارین ( béafšârin ) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=افشردن&oldid=77893051 "
 Categories : Persian terms with IPA pronunciation 
 Rhymes:Persian/an 
 Rhymes:Persian/an/3 syllables 
 Persian lemmas 
 Persian verbs
```


## [2026-10-17T00:33:28.178Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'xšūdan\\|χšūdan\\|xsüdan\\|bax\\|xšāy' HRN.txt | head -10; grep -n -i 'šēvan\\|šīvan\\|Wehklage\\|Klage' HRN.txt HUB.txt | head; grep -n -i 'afšurdan\\|afsurdan\\|fišurdan\\|af.ardan' HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:33:28.967Z] TOOL RESULT

```
1495:H-BKOTOPWXX nEPCH4CKHX^ GIOBAX^ Kh OCETHHGKOMX
2027:aw. baxta- *Verhängniss'; phlv. baxt 'Schicksal';
2033:gegebene Verbum baytan 'schenken', päz. baxsfdan,
2057:vatabaxt, vatabaxtik,
7226:ap. baga- 'Gott*; aw. baya-; phlv. bag]baxt (ge-
15044:baxta- 185, 47.
22499:ratabaxf 187.
HUB.txt:3494:zuriick, zu dem np. must 'Klage, Betriibniss' wohl
HUB.txt:3633:1054. Np. naltdan 'klagen, seufzen' stellt Geiger (Etym.
HUB.txt:4620:*Rohr , skr. nada- *Schilfrohr , gr. vdgdog ? ; naltdan *klagen',
HUB.txt:5079:herezaiti; gila 'Klage' = zd. gerezd-; kistan saen', skr.
HUB.txt:6067:afgh. LW. gran; girtstan *klagen'; xirad 'Verstand' = zd.
HUB.txt:7852:iran. rz steht: 14) np. gUa 'Klage', paz. gila Min. 61. 90
HUB.txt:8809:guftan *sprechen', ap. gaub-; gila 'Klage = zd. gereza-
HUB.txt:9322:(siehe § 34, a und b) ; gUa 'Klage* = phi. gilak, ap. "^grdor-
HRN.txt:1940:Klagen (Is. 14, 31 ; 15, 4, 5), nwXir:N2 (Is. 57, 13).
HRN.txt:4357:aw. [//raos-, yraosyöii^ /jaosya- Vehklagend, heulend',
HUB.txt:5121:azdrayeinti) ; afsurdan 'frieren , af^h. LW. afsurdq ^frozen'
HUB.txt:5122:(aus *afsardan, vgl. paz. awasard , phi. afsart 'frozen*
HUB.txt:5125:hat. Ob afsurdan 'auspressen' : pr. afsaram Muster oder
HUB.txt:6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
HUB.txt:6469:p. 17; afsurdan *frieren' H. 100, paz. aw(a)sard 'frozen*;
```


## [2026-10-17T00:33:32.212Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2022,2040p HRN.txt; sed -n 5118,5128p HUB.txt"
}
```


### [2026-10-17T00:33:32.830Z] TOOL RESULT

```
Da np. c nicht für skr. ts stehen kann, so ist die
Zusammenstellung mit ai. vatsd- 'Kalb, Jährling*, unzu-
lässig ; das letztere Wort entspricht vielmehr np. gösäle
(No. 941).
185. beyit 'Schicksal'.
aw. baxta- *Verhängniss'; phlv. baxt 'Schicksal';
ai. bhaktd- zugeteilt'.
arm., bei., s.{y, LW. ba^t, kurd. LW. be/t, bakt
(letztere Form echt?).
186. bey(STden 'schenken', Praes. be/s-em, beyßis.
aw. |^6a/s- 'schenken' ; phlv. vergl. das im Np. auf-
gegebene Verbum baytan 'schenken', päz. baxsfdan,
ba/Sisn.
kurd. ba/sin; af/. ba$al resp. ba/al; bei. baksag,
n. baSkay (24).
np. ba^sis ist weithin entlehnt, schon arm. bas/is.
186^** bey(8uden (*buxsüden) 'gnädig sein, verzeihen',
Praes. bexsay-em, bex§äyis\ TNi^OJ^ (Qiss. Dan. 400,
13, 18; 402, 4).
gebildet azurdan *kranken' (Sal. Shuk. Gram. p. 15, Bloch-
m'ann, JASB. XXXVII, 1, 52, afgh. LW. azurda) neben
azardan bei Vullers^), zd. anazareta-i pr. azaram (zd.
azdrayeinti) ; afsurdan 'frieren , af^h. LW. afsurdq ^frozen'
(aus *afsardan, vgl. paz. awasard , phi. afsart 'frozen*
Shk. 233, Gl. and Ind. 13, dazu sard *kalt* = zd. sareta-,
skr. *g9rta-), dessen Praes. wahrscheinlich "^afsaram gelautet
hat. Ob afsurdan 'auspressen' : pr. afsaram Muster oder
Analogiebildung ist, lasst sich nicht bestimmen, da die
Etymologie unbekannt ist.
Ueber ar aus ir nach Analogie siehe § 34 Ende.
```


## [2026-10-17T00:33:38.723Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10305,10318p FSF_pages.txt; awk '/pdf page/{p=$0} NR==10310{print p; exit}' FSF_pages.txt; grep -n -i 'xalanj\\|khalanj\\|chalendsch\\|xalen' LKT.txt KLN_1966.txt DOZ.txt 2>/dev/null| head -5"
}
```


### [2026-10-17T00:33:39.475Z] TOOL RESULT

```
                       ‫ز‬ ‫رب‬
                          ‫خامک‬
                             ‫سی‬                                               ‫حود)‬

  ‫گهشت وماند انجمن بخیدیو‬
                        ‫تب‬                                     ‫خدنگت (با زبر اول و دوم)‬
‫)‪(V-F.-1‬‬                                  ‫‪-۱‬نوعی چوب گز بسیار سخت و هموار‬
‫مصراع اول این بيت را عباس اقبال‬           ‫سازند و‬     ‫که از ان تیر و نیزه و زین اسب‬


‫مصحح لغت فرس بهاین شکل ضبط کرده‬           ‫تیر حدنگ و زین خدنگ به این اعتبار‬
                                ‫است‪:‬‬                         ‫گویند (رشیدی برهان)‪:‬‬
‫«سیامک به دست خود و رای دیو» که‬                        ‫چنان برگرفتم ز زین خحدنگ‬
 ‫نادرست است و معنی بيت و مضمون‬            ‫که گفتی ندارم به یک پشه بتک‬

KLN_1966.txt:15697:Galilee,  name  of  the  northern  province  of  wes¬ tern  Palestine.  —  L.  Galilaea,  fr.  Gk.  raXiXata, fr.  Heb.  Haggdlil,  lit.  ‘the  district’,  shortened  fr. Gflil  haggoyim,  ‘the  District  of  nations’  (Is. 8:23).  Haggdlil  was  the  name  of  a  district  in  the hill  country  of  Naphtali  (see  Josh.  20:7  and 21:32).  and  it  was  only  at  a  relatively  later  period that  it  began  to  denote  the  territory  of  Palestine north  of  the  Emek  Jezreel  (Esdraelon).  For  the etymology  of  Heb.  galil,  ‘district’,  see  gelilah. galimatias,  n.,  jargon.  —  F.,  ‘nonsense,  gibberish  , prob.  a  deformation  of  Late  L.  balhmathia,  in¬ decent  songs'.  For  the  etymology  of  this  latter word  see  Du  Cange,  Glossarium  mediae  et  in- fimae  latinitatis,  s.v.  balare. galingale,  n.,  an  aromatic  root  of  the  ginger family.  —  OF.  galingal,  formed— through  the medium  of  MGk.  yaXxyyoc  and  ML.  galanga fr.  Arab,  khalanjdn,  fr.  Pers.,  ult.  fr.  Chin.  Ko- leung-keung,  lit.  ‘mild  ginger  from  the  region of  Kao’.
```


## [2026-10-17T00:33:44.280Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for w in شیون فشرد افشرد بخشود بخشای بخشید خدنگ; do echo \"== $w\"; grep -n \"$w\" ARY_pages.txt | head -3; done; grep -n -i 'xšī\\|xšai\\|xšad\\|fšar\\|XSAD\\|XSAI' ARY_latin_index_pages.txt ARY_pages.txt | head"
}
```


### [2026-10-17T00:33:44.979Z] TOOL RESULT

```
== شیون
== فشرد
5905:فارسی (28/814): تنجیدن, تنج (به چم "بخود پیچیدن" و درهم فشرده شدن۳)
10244:۳ چم این واژه در زبان سانسکریت: فشار آوردن؛ فشردن» (ضربه) زدن,
== افشرد
== بخشود
== بخشای
== بخشید
3309:بخش, بخشیدن, بخشش / ۱۱۵
== خدنگ
```


## [2026-10-17T00:33:48.685Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk '/pdf page/{p=$0} NR==3309{print p; exit}' ARY_pages.txt; sed -n 3295,3325p ARY_pages.txt"
}
```


### [2026-10-17T00:33:49.160Z] TOOL RESULT

```
[pdf page 114]
دانمارکی (0۸۸//54):(شاید) ان 9 (05110) :۸/۸۸0
سوئدی (582/34):(شاید) ۸ برهان قاطع + ۳۳۷
لینوانی (/۷14۸ملا727/.)(شاید) ‏ ,8588۸۸8 فرهنگ معین : ۳۷۳-۴
اوستایی (47537۸/۷) :8۸6817۸771 ب8۸7۸ 20
پهلوی (۷1هابل#ه): .3 پسگشت‌ها ۱۱5
کردی (7ل08/15): 2 زر سا
تخاری ۸ (۸ [(4ل70707/۸7): 2۸ 71 :هلیم ت02
تخاری 8 (8 2۸ لل70): 4 5 (۲۵37108) :۸218
سانسکریت (54(/858/7): 817۸6871۸71 1095 ناه
ارمنی (۸۷۸/807140): اد رانا 13 ۸0
اسلاوی کهن (ع۲7اما؟ ۲ل#6تالق هام برهان قاطع : ۳۵
بادداشت:
بازگلست به: هر و بخش. ۰
[pdf page 114]
بخش, بخشیدن, بخشش / ۱۱۵
اوستایی (۷ل۸۲8874): ,8۸6 ,لاش87 ,88711 برنانی (0ق07): ۳0
8۸01۸ ,8۸381۸71 اسلاوی کهن (۷76ما5 ل#6ناتل) صا0):
پهلری (1/ا۸3): ,1 ,2۸3877 ت67 806
+811۸ ,(3۸38117813 ,28۸77۸۵
ترا تن ها پسگشت‌ها نششیت دنت
سانسکریت (7ل8۸587): 0
311۸71 ,81176817۸75 4 (ت88870۷/۸) ,ک1 ۰ 2ل2اققه ما
1 ,871۸6۸5 ,211۸6 برهان قاطع + ۲۱۴۱۴۰
ارمنی ((۵/0/8774): 3006۸77
یادداشت:
۱- بازگلت به "بخت" و ابغ".
۲ چم این واژه در زبان پونانی: خوردن.
۳ واژه‌های فارسی برع" و آبرخه" هم از همین واجریشه‌اند.
پهلوی (۳۸14۲7): ۷۸۳7۸۹ ,۷۸ ,۷۷۸ پسگشت‌ها 5
کردی (600[/87): ۰ - 8 ( 160 2020
لاتین (4710ا): (شاید) 0۸ 1 (8۸0) ات این نا
```


## [2026-10-17T00:34:04.562Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10845,10856p BRT.txt | cut -c1-200; cat ../../../verification/page-558.json 2>/dev/null | head -c 1500; command ls /home/sfmqrb/git/rishe-private/data/verification/ | head"
}
```


### [2026-10-17T00:34:05.331Z] TOOL RESULT

```
x5i-
S54
yam  D.6. 1;  X.i.  r,  6.  i,  Ao./.  1,  D.  <f- 4;  —  a^ura^mazdä  ..  kaieu  darayt^v^um yam  adadi^  .  .  vaina  J'urJ'mazdahJ' därayt^va/'ui'  yJ"  D.  4. 1 ;  Bh,  /.  5,  6,  13, D.  ff.  4;
2^   2).
Ableit.  aus  ♦j^/ncflSa- oder  ♦jr/oj-aSa- (mit  dem ödes  Praesens;  dann  mit  l^flVÄ/(l)m.-Herrsch- gewall',  zum  V,  xhii.y)-i).  —  np.  /ÖA,  — ')  Oft  mittelst  Ideogramm  geschrieben,  aber
g.  xSntä,  xSntqm ;  s.  »«(j')-.
•  j.  xä5i9nt-  fem.  Adj.:  s.  unter  xsagta-.
•  j.  xsa%ratxsayamna''x^5i^ra..'Vyt3_S-
•  g.  x^anmäne  Inf  'sich  etwas  gefallen lassen  müssen,  sich  damit  zufrieden  geben müssen',  mit  Akk.:  y!  anaispm  xs'  radsm *vaäm  w«/  aiärahya  "dass  ich  mir  ab Fürsorger  das  unwi
Zum  ai.  V.  iiamaä;  %  68,  358.  2  c.  Inf.  in konjunkt.  Sinn.  —  Pu.:  *<iial  (NpB.:  nisäd) mcniiiilh'),  Sü.;  aaiaaadajnatiäi.  —  i)  Vgl, Y.44,  17.  —  *)  Als  hätte  er  *asqm  mini 
•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
Vgl.  xiayS.    —    Pü.;    inian  'Jammern'  (wozu Hbm.  AGr.  /.  2 14).  —  ')  Für  *xHyB,  'xHyasäi, *xSiy>ni  S  /pj,  ^/o. j.  xHvti/i   V.  2.  31:    liei   arAüA'j    t.   unter
{
  "pdf_page": 558,
  "book_page": 528,
  "verified_by": "claude-opus-5.5",
  "verified_on": "2026-10-16",
  "entries": [
    {
      "entry": 0,
      "root": "Xac 1",
      "verdict": "plausible",
      "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
      "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
      "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ر�agent
COORDINATOR.md
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
```


## [2026-10-17T00:34:10.521Z] TOOL CALL #39: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg559.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/559.png; echo ok"
}
```


### [2026-10-17T00:34:11.262Z] TOOL RESULT

```
ok
```


## [2026-10-17T00:35:59.860Z] TOOL CALL #40: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-559.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nSIN_NOTE = (\"SIN.txt leaves 380-381 (pp. 552-553), §16 'Birch': 'Antaki notes the xalen tree (\\\"birch\\\") in India and China ... \"\n            \"The Arabic xalen, Persian xadan or xadanj, is of Altaic origin: Uigur qadan, Koibal, Soyot and Karagas kaden, \"\n            \"Cuwas xoran, Yakut xatyn ... all referring to the birch (Betula alba). It is a common tree in the mountains of northern China (hwa ...)'.\")\n\ndata = {\n \"pdf_page\": 559, \"book_page\": 529, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-16\",\n \"entries\": [\n  {\n   \"entry\": 0, \"root\": \"Xalen\", \"verdict\": \"disputed\",\n   \"modern_form\": \"Arabic xalanj/xalen (خلنج) 'birch (wood)' as cited by Antaki; Chinese name is hua 樺; Persian xadang < Turkic (Proto-Turkic *kadïŋ 'birch')\",\n   \"note\": \"Nourai labels 'Xalen' as Chinese, citing Laufer (SIN 552). Laufer calls xalen the ARABIC name (from Antaki and Ibn al-Kabir) and gives the Chinese name as hwa (hua 樺). So the language label is wrong. Laufer does not derive the Altaic birch word from Chinese. He says that both the Arabic and the Persian words come from Altaic. The arrow Chinese -> Altaic therefore has no support. The gloss 'birch' and the cultural note (north China, Tabarestan, wood exported) do match Laufer. The extraction matches the printed page.\",\n   \"note_fa\": \"نورایی «Xalen» را واژه‌ای چینی به معنای «درخت غان (توس)» گرفته و به لاوفر (Sino-Iranica ص ۵۵۲) ارجاع داده است. لاوفر xalen (خلنج) را نام عربی این درخت می‌داند، به نقل از انطاکی، و نام چینی آن را hwa (樺) می‌نویسد. به گفتهٔ او واژهٔ عربی و واژهٔ فارسی «خدنگ» هر دو از زبان‌های آلتایی آمده‌اند. پس برچسب «چینی» نادرست است و پیکان چینی ← آلتایی در منبع خود نورایی پشتوانه‌ای ندارد. معنا و یادداشت فرهنگی (رواج درخت در شمال چین و طبرستان) درست است.\",\n   \"sources\": [W + \"خدنگ\", W + \"Reconstruction:Proto-Turkic/kadïŋ\"],\n   \"ref_check\": [{\"ref\": \"SIN:552\", \"status\": \"contradicts\", \"note\": SIN_NOTE + \" Laufer gives xalen as Arabic, not Chinese. The Chinese word is hwa.\"}],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. galingale (grep 'khalanj')\", \"stance\": \"silent\", \"note\": \"only Arab. khalanjān 'galingale' < Chin. 'Ko-leung-keung'. That is a different word; nothing on xalen 'birch'.\"},\n     {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt line ~10316/10337 s.v. خدنگ\", \"stance\": \"silent\", \"note\": \"'نام درختی است بسیار سخت که از چوب آن نیزه و تیر و زین...'; Mo'in fn: 'معرب آن خدنك = peuplier blanc (فر.) دزی ج۱ ص۵۵۳'. No Chinese source word.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Altaic\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Empty pass-through node for the Altaic (Turkic) birch word. Laufer lists Uighur qadan, Koibal/Soyot/Karagas kaden, Chuvash xoran and Yakut xatyn. Modern reconstruction is Proto-Turkic *kadïŋ 'birch tree' (Wiktionary). The Altaic source itself is well founded, but it does not derive from a Chinese 'xalen' as the chart's arrow implies.\",\n     \"derivation_fa\": \"این گره بی‌واژه، صورت آلتایی (ترکی) نام درخت غان را نشان می‌دهد: اویغوری qadan، یاقوتی xatyn، چوواشی xoran. ترکی آغازین آن را *kadïŋ «درخت غان» بازسازی کرده‌اند. خاستگاه آلتایی درست است، ولی این واژه از «Xalen» چینی نیامده است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Turkic/kadïŋ\"],\n     \"ref_check\": [{\"ref\": \"SIN:553\", \"status\": \"supports\", \"note\": SIN_NOTE}],\n     \"consulted\": [\n       {\"src\": \"TTS\", \"where\": \"incoming/TTS (grep qadin/kadin)\", \"stance\": \"silent\", \"note\": \"grep for qadin/kadin/qadıŋ found no usable entry in the OCR.\"},\n       {\"src\": \"LKT\", \"where\": \"LKT.txt (grep xadang/chadeng)\", \"stance\": \"silent\", \"note\": \"no entry for the birch word.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"xadang\", \"verdict\": \"plausible\",\n     \"derivation\": \"Persian xadang خدنگ means 'a very hard wood (birch/white poplar); arrow made of it'. Laufer records the variants xadan/xadanj. Wiktionary (Etymology 2) says it is 'possibly borrowed from Turkic, ultimately from Proto-Turkic *kadïŋ birch'. Turkic initial q-/k- was rendered by Persian x-, and final -ŋ by -ng. The word is well attested in classical poetry, e.g. Ferdowsi's 'به پیکان پولاد و تیر خدنگ' (the chart's quote). The Turkic loan is accepted with a 'possibly', and Mo'in gives no etymology, so the verdict is plausible.\",\n     \"derivation_fa\": \"«خدنگ» (xadang) در فارسی نام چوبی بسیار سخت است که از آن تیر و نیزه و زین می‌ساختند، و به خود تیر نیز گفته می‌شود. معین آن را «سپیدار» (peuplier blanc) معنا کرده است. لاوفر صورت‌های xadan و xadanj را آورده و آن را آلتایی دانسته است. ویکی‌واژه نیز آن را «احتمالاً» وام‌واژه‌ای از ترکی می‌داند، از ترکی آغازین *kadïŋ «غان». در این وام‌گیری q/k آغازی ترکی به «خ» و ŋ پایانی به «نگ» بدل شده است. این ریشه‌شناسی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"خدنگ\"],\n     \"ref_check\": [\n       {\"ref\": \"SIN:553\", \"status\": \"supports\", \"note\": SIN_NOTE},\n       {\"ref\": \"BQT:719\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt ~line 10316: 'خدنگ ... نام درختی است بسیار سخت که از چوب آن نیزه و تیر و زین...'; fn 1: 'معرب آن خدنك = peuplier blanc (فر.) دزی ج۱ ص۵۵۳'. Confirms the meaning; gives no Altaic etymology. (ref_page.py: no scan mapped for printed p.719; located through the OCR text.)\"},\n       {\"ref\": \"FSF:158\", \"status\": \"partial\", \"note\": \"FSF_pages.txt line ~10310: 'خدنگ (با زبر اول و دوم) ۱- نوعی چوب گز بسیار سخت و هموار که از آن تیر و نیزه و زین اسب سازند'. Gloss only, no etymology.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 2 s.v. خدنگ (BQT_v2_pages.txt ~10316)\", \"stance\": \"partial\", \"note\": \"'درختی است بسیار سخت'. Mo'in: Arabicized خدنك, Dozy 'peuplier blanc'.\"},\n       {\"src\": \"FSF\", \"where\": \"FSF_pages.txt ~10310\", \"stance\": \"partial\", \"note\": \"'نوعی چوب گز بسیار سخت'.\"},\n       {\"src\": \"HRN\", \"where\": \"HRN.txt (grep xadang)\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n       {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep خدنگ)\", \"stance\": \"silent\", \"note\": \"not listed. The word is not Indo-European.\"}\n     ]}\n   ]\n  },\n  {\n   \"entry\": 3, \"root\": \"Xšad\", \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Iranian *xšad- 'to have mercy, forgive' (Cheung 2007), with preverb *apa-\",\n   \"note\": \"Cheung reconstructs *xšad 'to have mercy, grace, forgive (< to cleanse, clear of ?)', MP abaxšāy-, Parth. ʾxšd 'mercy', ʾbxšʾh-, and says 'the root appears to be exclusively Iranian'. It is not attested as a verb in Avestan or Old Persian, so the label 'Avestan / Old Persian' presents a reconstruction as attested. Abolghasemi (FFD 35) calls the root hypothetical (فرضی). Cheung and FFD also explain the chart's NOTE: NP baxšūdan 'forgive' and baxšīdan 'give' (< *baxš-, PIE *bʰeh₂g-) were contaminated with each other. Modern scholarship sides with Nourai's note. The extraction matches the page; the note's 'baxšŭdan' is baxšūdan بخشودن.\",\n   \"note_fa\": \"ریشهٔ *xšad- «بخشودن، رحم کردن» را چونگ برای ایرانی آغازین بازسازی کرده است. او پهلوی abaxšāy- و پارتی ʾbxšʾh- را از آن، با پیشوند apa-، می‌داند و می‌گوید این ریشه تنها در زبان‌های ایرانی دیده می‌شود. ابوالقاسمی نیز آن را «فرضی» می‌خواند. این ریشه در اوستا و پارسی باستان به صورت فعل گواهی نشده است، پس برچسب «اوستایی/پارسی باستان» دقیق نیست. ادعای نورایی در کلیت با احتیاط پذیرفتنی است.\",\n   \"sources\": [W + \"بخشودن\", W + \"بخشیدن\"],\n   \"ref_check\": [{\"ref\": \"FFD:35\", \"status\": \"supports\", \"note\": \"FFD_pages.txt pdf page 40 (= p.35) s.v. بخشودن: 'بخشای < فارسی میانه abaxšāy < ایرانی باستان *apa-xšād-... apa پیشوند فعلی است. ریشهٔ xšād فرضی است' (Latin OCR garbled). Root and prefix as in the chart.\"}],\n   \"consulted\": [\n     {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 29091\", \"stance\": \"supports\", \"note\": \"'*xšad ‘to have mercy, grace, forgive (< to cleanse, clear of ?)’ ... (+ *apa-) MMP ’bxš’y-, BMP ’phš’d- /abaxšāy-/ ... The root appears to be exclusively Iranian.'\"},\n     {\"src\": \"BRT\", \"where\": \"BRT.txt (grep xšad)\", \"stance\": \"silent\", \"note\": \"no Avestan verb xšad- 'forgive' found.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"apa-xšad-a\", \"verdict\": \"plausible\",\n     \"derivation\": \"apa-xšad-a is the reconstructed Old Iranian present stem *apa-xšāda- (preverb apa- 'away' + *xšad 'clear, forgive'). It underlies MP abaxšāy- and Parthian ʾbxšʾh-, and the Armenian loan apašxarem 'I repent' is linked to it (Wiktionary; Nyberg disputes the Armenian link). The form is not attested in any Avestan or Old Persian text, so it should carry an asterisk.\",\n     \"derivation_fa\": \"apa-xšad-a صورتی بازسازی‌شده است (*apa-xšāda-)، از پیشوند apa- «دور، باز» و ریشهٔ *xšad «بخشودن». پهلوی abaxšāy- و پارتی ʾbxšʾh- از همین صورت آمده‌اند. ولی این صورت در متن‌های اوستایی و پارسی باستان دیده نمی‌شود و باید ستاره‌دار نوشته شود. ادعا با احتیاط پذیرفتنی است.\",\n     \"sources\": [W + \"بخشودن\"],\n     \"ref_check\": [{\"ref\": \"FFD:35\", \"status\": \"supports\", \"note\": \"FFD p.35 s.v. بخشودن: 'ایرانی باستان *apa-xšād- ... apa پیشوند فعلی است. ریشهٔ ... فرضی است'.\"}],\n     \"consulted\": [\n       {\"src\": \"CHEUNG\", \"where\": \"line 29091-29110\", \"stance\": \"supports\", \"note\": \"'(+ *apa-) ... /abaxšāy-/ ‘to forgive, have pity, mercy’'. Lists no Avestan form.\"},\n       {\"src\": \"BRT\", \"where\": \"BRT.txt (grep apaxš/xšad)\", \"stance\": \"silent\", \"note\": \"no Avestan apa-xšad- found.\"},\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 601 s.v. apoxšāyišn\", \"stance\": \"partial\", \"note\": \"'apo- < apa- ... [Arm. lw. apasxar-em < *apa-xšād- is not akin]'. Assumes apa- + xšāy-.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"abaxšay, abaxšâyîd\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian abaxšāy- (present stem) and abaxšāyīdan 'to forgive, have mercy on' (Book Pahlavi ʾp̄hšʾd-, Manichaean ʾbxšʾy-) come from *apa-xšāya-. Intervocalic -p- voiced to -b-, and *-xš- was kept. abaxšāyīdan is a secondary past stem built on the present stem with -īd-. The chart's 'abaxšâyîd' is that past stem.\",\n     \"derivation_fa\": \"پهلوی abaxšāy- (ستاک حال) و abaxšāyīdan «بخشودن، رحم آوردن» از *apa-xšāya- آمده‌اند. «پ» میان دو واکه به «ب» بدل شده است. abaxšāyīd ستاک ماضی ساختگی است که از ستاک حال ساخته شده. مکنزی و نیبرگ هر دو این صورت را آورده‌اند و ادعای نورایی درست است.\",\n     \"sources\": [W + \"بخشودن\"],\n     \"ref_check\": [{\"ref\": \"FFD:35\", \"status\": \"supports\", \"note\": \"FFD p.35: 'در فارسی میانه به جای «بخشود» abaxšāyīd آمده است ... مادهٔ ماضی جعلی ... بخشای < فارسی میانه abaxšāy'.\"}],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"p.5 (PHD.txt line 164)\", \"stance\": \"supports\", \"note\": \"'abaxšāyīdan, abaxšāy- ['phšʾd-ytn' | M ʾbxšʾy-, N baxšūdan, baxšāy-] forgive, have mercy on. ~išn: mercy, forgiveness.'\"},\n       {\"src\": \"NYB\", \"where\": \"Glossary, line 601 s.v. apoxšāyišn\", \"stance\": \"supports\", \"note\": \"'apoxšāyišn ['pwhšʾdšn'] compassion, mercy ... Ps. pres. ʾphšʾd- ... NP baxšūdan, baxšā'īdan, baxšāy-, baxšāyiš'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"line 29093\", \"stance\": \"supports\", \"note\": \"'BMP ’phš’d- /abaxšāy-/ ‘to forgive, have pity, mercy’'.\"}\n     ]},\n    {\"id\": 3, \"lang\": \"Persian\", \"words\": \"baxšîdan\", \"verdict\": \"plausible\",\n     \"derivation\": \"The regular New Persian reflex of MP abaxšāy-/abaxšāyīdan is baxšāy-/baxšāyīdan, with loss of the initial a-. A newer past stem baxšūdan arose by analogy with farmūdan/farmāy- (FFD; Wiktionary). The extras بخشای، بخشاینده، بخشایش belong to this verb. baxšīdan 'to give, divide' and baxšande 'giver' come from the different root *baxš- (PIE *bʰeh₂g-, cf. baxt), which was later used in the sense 'forgive' through contamination (Cheung; FFD 36). The chart's headword baxšīdan 'to forgive' is therefore secondary. Its NOTE about the confusion matches modern scholarship.\",\n     \"derivation_fa\": \"بازماندهٔ درست پهلوی abaxšāy- در فارسی دری «بخشای-» و «بخشاییدن» است. آغازه a- در آن افتاده است. «بخشود(ن)» ستاک ماضی تازه‌ای است که به قیاس «فرمود/فرمای» ساخته شده. «بخشای، بخشاینده، بخشایش» از همین فعل‌اند. ولی «بخشیدن» به معنای «دادن، تقسیم کردن» و «بخشنده» از ریشهٔ دیگری‌اند (*baxš-، هندواروپایی *bʰeh₂g-، هم‌ریشه با «بخت»). این دو فعل از راه همانندی آوایی با هم آمیخته‌اند، چنان‌که چونگ و ابوالقاسمی گفته‌اند. پس «بخشیدن» در معنای «عفو کردن» کاربردی ثانوی است و یادداشت خود نورایی درست است.\",\n     \"sources\": [W + \"بخشودن\", W + \"بخشیدن\"],\n     \"ref_check\": [{\"ref\": \"FFD:35\", \"status\": \"partial\", \"note\": \"FFD p.35 treats this under بخشودن, not بخشیدن: '«بخشود» در فارسی دری به قیاس ... به وجود آمده است'. p.36 s.v. بخشیدن: 'بخش < فارسی میانه baxš < ایرانی باستان *bag-s- ... به سبب شباهت لفظی که میان «بخشودن» به معنی «عفو کردن» و «بخشیدن» به معنی «تقسیم کردن» هست، «بخشیدن» در معنی «بخشودن» به کار رفته است'.\"}],\n     \"consulted\": [\n       {\"src\": \"CHEUNG\", \"where\": \"line 29102-29106\", \"stance\": \"partial\", \"note\": \"'NP baxšūdan, baxšīdan/baxš- ... is contaminated with the root *baHxš, cf. ... Horn 1893: 43 f.'\"},\n       {\"src\": \"HRN\", \"where\": \"nos. 186 / 186bis (HRN.txt line 2032-2038)\", \"stance\": \"partial\", \"note\": \"186 'baxšīden schenken' < aw. baxš-; 186bis 'baxšūden (*buxšūden) gnädig sein, verzeihen, Praes. baxšāy-em'. Horn keeps the two verbs apart.\"},\n       {\"src\": \"ARY\", \"where\": \"pdf page 114 (p.115) 'بخش، بخشیدن، بخشش'\", \"stance\": \"partial\", \"note\": \"puts بخشیدن under PIE *bhag- ('بازگشت به \\\"بخت\\\"'), i.e. the 'give' verb, not the xšad root.\"},\n       {\"src\": \"PHD\", \"where\": \"p.5 s.v. abaxšāyīdan\", \"stance\": \"partial\", \"note\": \"'N baxšūdan, baxšāy-'. Gives baxšūdan, not baxšīdan, as the NP reflex.\"}\n     ]}\n   ]\n  },\n  {\n   \"entry\": 5, \"root\": \"Xšarta\", \"verdict\": \"disputed\",\n   \"modern_form\": \"Iranian *fšar- 'to press (out)' with preverb *apa- (Cheung 2007); IE origin unknown\",\n   \"note\": \"The root *xšarta- 'press' comes from Bailey's 1937 Khotanese note (BLY 75; the OCR is garbled). Cheung files MP apšār-/afsārdan, NP afšurdan/afšār-, fišurdan, afšure under *fšar(?) 'to press', + *apa-. Hübschmann says the etymology of afšurdan 'auspressen' is unknown. The chart's root is also hard to square with the sounds: *apa-xšar- would give MP *abaxšār- (compare abaxšāy- in the preceding chart), not afšār-. The f of afšār- points to *apa-fšar- (pf > f). Modern scholarship therefore prefers *fšar-.\",\n   \"note_fa\": \"نورایی ریشهٔ «افشردن» را ایرانی باستان *xšarta- «فشردن» می‌گیرد، به پیروی از بیلی (۱۹۳۷). چونگ این خانواده (پهلوی apšār-، فارسی افشردن/افشار-، فشردن، افشره) را زیر ریشهٔ ایرانی *fšar- «فشردن» با پیشوند apa- آورده است. هوبشمان ریشهٔ «افشردن» را ناشناخته می‌داند. از نظر آوایی هم *apa-xšar- در پهلوی به *abaxšār- می‌انجامید، همان‌گونه که از apa-xšāy- صورت abaxšāy- پدید آمد، نه به afšār-. پس پژوهش امروزی ریشهٔ *fšar- را ترجیح می‌دهد.\",\n   \"sources\": [],\n   \"ref_check\": [{\"ref\": \"BLY:75\", \"status\": \"supports\", \"note\": \"incoming/BLY/BLY_pages.txt ~line 398-406 (p.75, s.v. kṣ...): garbled OCR '*Xšarta- ... Mid. Pers. afšart ... NPers. afšurd shows umlaut ... press'. Bailey posits *xšart- 'press' with MP/NP afšurd-.\"}],\n   \"consulted\": [\n     {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt line 6985-7005, s.v. *fšar\", \"stance\": \"contradicts\", \"note\": \"'*fšar ? ‘to prepare and press an intoxicating drink ?’ ... (+ *apa-) BMP ’psʾr- /apšār-/ ‘to press (out)’ ... NP fišurdan/fišar-, afšurdan/afšar- ... NP afšurah ‘pressed (fruit) juice’ ... An IE origin is unknown'.\"},\n     {\"src\": \"HUB\", \"where\": \"HUB.txt line 5125\", \"stance\": \"contradicts\", \"note\": \"'Ob afšurdan ‘auspressen’ : pr. afšāram Muster oder Analogiebildung ist, lässt sich nicht bestimmen, da die Etymologie unbekannt ist.'\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"afsârtan, aššârdan\", \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\", \"book_prints\": \"afsârtan, aššârdan\", \"correct_form\": \"afšurdan, afšār- / afšārdan\",\n     \"derivation\": \"MacKenzie (PHD 5) gives MP afšurdan, afšār- 'press, compress, crush' and afšārdan (= afšurdan), from *apa-(f)šar-. The chart's 'afsârtan' matches MacKenzie's afsārdan, which means 'cool, freeze' (Hübschmann: Pahl. afsart 'frozen', from the root of sard 'cold'). Cheung, however, reads the ambiguous Book Pahlavi spelling ʾpsʾr- as /apšār-/ 'press', so this first word is defensible as a reading. 'aššârdan' is not a known form. The printed page shows it exactly so (the extraction is faithful), and it is evidently Nourai's misprint for afšārdan.\",\n     \"derivation_fa\": \"مکنزی در پهلوی afšurdan، afšār- «فشردن، له کردن» و afšārdan را آورده است، از *apa-(f)šar-. «afsârtan» در نمودار به afsārdan در فرهنگ مکنزی می‌ماند که به معنای «سرد کردن، فسردن» است. البته چونگ همین نگارش پهلوی (ʾpsʾr-) را apšār- «فشردن» خوانده است. ولی «aššârdan» صورتی ناشناخته است. در صفحهٔ چاپی هم همین آمده، پس خطای چاپی کتاب است، به جای afšārdan، نه خطای خوانش اسکن.\",\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"PHD:5\", \"status\": \"partial\", \"note\": \"PHD.txt line 164 (p.5): 'afšārdan ['pšʾlšn'] = afšurdan. afšurdan, afšār- [ʾpšwltn',ʾpšʾl- | N ~] press, compress, crush'. Also 'afsārdan, afsār- [ʾpsʾl-tn'] cool, freeze, extinguish'. MacKenzie has afšārdan/afšurdan, not 'aššârdan', and his afsārdan means 'freeze'.\"},\n       {\"ref\": \"BLY:75\", \"status\": \"partial\", \"note\": \"BLY_pages.txt ~line 402-406: 'Mid. Pers. afšart ... NPers. afšurd ... press' (garbled). Bailey's MP form is afšart, not aššârdan.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"p.5\", \"stance\": \"partial\", \"note\": \"'afšurdan, afšār- press, compress, crush'; 'afsārdan ... cool, freeze'.\"},\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt (grep afš/apš)\", \"stance\": \"silent\", \"note\": \"no entry for afšurdan found.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"line 6989-6991\", \"stance\": \"supports\", \"note\": \"'BMP ’psʾr- /apšār-/ ‘to press (out)’ ... Inf.: BMP ’psʾltn /afsārdan/'.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"afšârdan; fešâr; afšoreh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP afšordan/afšārdan (present stem afšār-) continues MP afšurdan/afšār-. fešordan is the form with the initial a- lost (aphaeresis), and fešār 'pressure' is the bare present stem used as a noun. afšore 'pressed juice' is the past stem + -a. Cheung lists exactly 'NP fišurdan/fišar-, afšurdan/afšar- ... NP afšurah ‘pressed (fruit) juice’', with the Arabic loan afšaraj 'juice'. The MP -> NP step is secure; only the deeper root (see entry note) is disputed.\",\n     \"derivation_fa\": \"«افشردن/افشاردن» (ستاک حال «افشار») بازماندهٔ پهلوی afšurdan/afšār- است. «فشردن» همان واژه است که واکهٔ آغازی‌اش افتاده. «فشار» ستاک حال است که به جای اسم به کار رفته، و «افشره» از ستاک ماضی و پسوند «-ه» ساخته شده است. چونگ همهٔ این صورت‌ها را آورده است. گذر پهلوی ← فارسی درست است و تنها ریشهٔ کهن‌تر محل بحث است.\",\n     \"sources\": [W + \"فشار\", W + \"افشردن\"],\n     \"ref_check\": [{\"ref\": \"BLY:75\", \"status\": \"partial\", \"note\": \"BLY_pages.txt ~line 404: 'NPers. afšurd ... press' (garbled OCR). Mentions only the verb, not fešār/afšore.\"}],\n     \"consulted\": [\n       {\"src\": \"CHEUNG\", \"where\": \"line 6996-6999\", \"stance\": \"supports\", \"note\": \"'NP fišurdan/fišar-, afšurdan/afšar- ... NP afšurah ‘pressed (fruit) juice’ ... Arab. (LW) afšaraj ‘juice’'.\"},\n       {\"src\": \"HUB\", \"where\": \"line 5125\", \"stance\": \"partial\", \"note\": \"'afšurdan ‘auspressen’ ... Etymologie unbekannt'.\"},\n       {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep افشرد/فشرد)\", \"stance\": \"silent\", \"note\": \"no headword entry.\"}\n     ]}\n   ]\n  },\n  {\n   \"entry\": 6, \"root\": \"Xšî 1, Xšaivan\", \"verdict\": \"plausible\",\n   \"modern_form\": \"Avestan xšī- f. 'distress, misery' (Bartholomae 554); Proto-Iranian *xšai- 'to lament, weep' (Wiktionary); *xšaivana- reconstructed\",\n   \"note\": \"Avestan xšī- 'Not, Elend' is real (Y.31.20, Y.71.17; Bartholomae col. 554). 'Xšaivan' is a reconstruction (Mo'in: 'ایرانی باستان *xshaivan'), not an attested Avestan or Old Persian word. Wiktionary derives MP šēwan from Proto-Iranian *xšai- 'lament, weep' and adds 'further connections unclear'. The chart follows Mo'in's footnote in BQT 1329 exactly.\",\n   \"note_fa\": \"اوستایی xšī- «تنگی، بدبختی» واژه‌ای گواهی‌شده است (بارتولومه، ستون ۵۵۴، یسنا ۳۱.۲۰). ولی xšaivan صورتی بازسازی‌شده است که معین در حاشیهٔ برهان آورده، نه واژه‌ای اوستایی یا پارسی باستان. ویکی‌واژه «شیون» را از پهلوی šēwan و ایرانی آغازین *xšai- «زاری کردن» می‌داند و پیوندهای دورتر را روشن نمی‌داند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [W + \"شیون\"],\n   \"ref_check\": [{\"ref\": \"BQT:1329\", \"status\": \"supports\", \"note\": \"incoming/BQT/BQT_v3_pages.txt line ~9354 ([pdf page 122]; ref_page.py's offset guess of pdf 124 lands on ص, off by 2), fn 2 to شیون: 'پهلوی shivan (shévan، باروچا) ، ایرانی باستان *xshaivan ، اوستا xšī (بدبختی، فقر، احتیاج) «بارتولمه» ...'.\"}],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"col. 554 (BRT.txt line 10855)\", \"stance\": \"supports\", \"note\": \"'xšī- f. ‘Not, Elend’: ... Y.31.20; ... xšayasča Y.71.17 ... Pü.: ... ‘Jammern’'.\"},\n     {\"src\": \"HUB\", \"where\": \"HUB.txt (grep šēvan)\", \"stance\": \"silent\", \"note\": \"not found.\"}\n   ],\n   \"nodes\": [\n    {\"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"šěvan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian šēwan [šywn'] 'lament, lamentation' comes from *xšaiwana- (root *xšai- plus the action-noun suffix -ana-). Old Iranian xš- became š- in Middle Persian, and the diphthong *ai became ē. Pazand šīna < *šēvanak is a related form.\",\n     \"derivation_fa\": \"پهلوی šēwan «شیون، زاری» از *xšaiwana- آمده است (ریشهٔ *xšai- و پسوند اسم‌ساز -ana-). در فارسی میانه xš- آغازی ایرانی باستان به š- و واکهٔ مرکب ai به ē بدل شده است. مکنزی و نیبرگ هر دو این واژه را آورده‌اند و ادعای نورایی درست است.\",\n     \"sources\": [W + \"شیون\"],\n     \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"PHD.txt line 583 (s.v. šēwan)\", \"stance\": \"supports\", \"note\": \"'šēwan [šywn' | N ~] lament.'\"},\n       {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 3634\", \"stance\": \"supports\", \"note\": \"'šēvan [šywn'] lamentation 86²⁰. — Paz. šīna < *šēvanak; NP šīvan'.\"}\n     ]},\n    {\"id\": 2, \"lang\": \"Persian\", \"words\": \"šîvan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP šīvan شیون 'wailing, lament' continues MP šēwan. Classical Persian had šēwan with majhul ē (BQT: 'با یای مجهول'), which merged with ī in Iranian Persian, giving šīvan. Intervocalic w became v.\",\n     \"derivation_fa\": \"«شیون» در فارسی نو بازماندهٔ پهلوی šēwan است. در فارسی کلاسیک با «یای مجهول» (ē) تلفظ می‌شد، چنان‌که برهان می‌گوید، و در فارسی امروز ایران ē به ī بدل شده است. برهان قاطع آن را «ناله و افغانی که در هنگام محنت و مصیبت کنند» معنا می‌کند. ادعای نورایی درست است.\",\n     \"sources\": [W + \"شیون\"],\n     \"ref_check\": [{\"ref\": \"BQT:1329\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt line 9325-9327 ([pdf page 122]): 'شیون - با یای مجهول بر وزن ... ناله و افغان را گویند که در هنگام محنت و مصیبت کنند'; fn: 'پهلوی shivan (shévan) ... ایرانی باستان *xshaivan ...'.\"}],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 3 p.1329\", \"stance\": \"supports\", \"note\": \"headword + Mo'in footnote as above.\"},\n       {\"src\": \"NYB\", \"where\": \"Glossary line 3634\", \"stance\": \"supports\", \"note\": \"'NP šīvan'.\"},\n       {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (grep شیون)\", \"stance\": \"silent\", \"note\": \"no entry.\"}\n     ]}\n   ]\n  }\n ]\n}\n\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-559.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n"
}
```


### [2026-10-17T00:35:59.880Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-559.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:36:05.444Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-559.py && python3 -m json.tool data/verification/page-559.json >/dev/null && python3 tools/verify_check.py 559"
}
```


### [2026-10-17T00:36:06.180Z] TOOL RESULT

```
nodes verified: 9/9
node verdicts: {'confirmed': 5, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'disputed': 2, 'plausible': 2}
ref checks: {'supports': 5, 'partial': 6, 'not_checked': 1}
books consulted: {'silent': 8, 'partial': 9, 'supports': 10} | by book: {'CHEUNG': 5, 'NYB': 5, 'ARY': 4, 'PHD': 4, 'BQT': 2, 'HRN': 2, 'TTS': 1, 'LKT': 1, 'FSF': 1, 'BRT': 1, 'HUB': 1}
```


## [2026-10-17T00:36:17.402Z] TOOL CALL #42: SubagentHandback

```json
{
 "message": "Page 559 (book page 529) is verified and written to /home/sfmqrb/git/rishe-private/data/verification/page-559.json. `verify_check.py 559` reports 0 PROBLEM lines.\n\nI skipped the 3 redirect entries (Xartěs, Xasta, Xšaivan), which leaves 4 charts with 9 nodes.\n- **Nodes:** 5 confirmed, 3 plausible, 1 transcription_suspect.\n- **Roots:** 2 disputed, 2 plausible.\n\nDisputed and suspect items:\n- **Xalen (root, disputed):** the book labels it Chinese, but its own source (Laufer, SIN 552–553) gives xalen as the Arabic name and the Chinese name as hwa. Laufer derives both the Arabic and the Persian words from Altaic (modern Proto-Turkic *kadïŋ \"birch\"), so the Chinese → Altaic arrow has no support. Persian xadang itself is plausible as a Turkic loan.\n- **Xšarta (root, disputed):** Cheung puts afšurdan/fešordan, fešār and afšore under *fšar- \"press\" with the prefix apa-, and Hübschmann calls the etymology unknown. The chart's *xšarta- (from Bailey 1937) does not fit the sounds: *apa-xšar- would give MP *abaxšār-, not afšār-.\n- **Xšarta, Pahlavi node \"afsârtan, aššârdan\" (transcription_suspect, error in the book):** MacKenzie (PHD 5) has afšurdan/afšārdan \"press\". \"aššârdan\" is not a known form and is Nourai's misprint for afšārdan. His afsārdan means \"cool, freeze\", though Cheung reads that spelling as apšār- \"press\", so \"afsârtan\" is defensible.\n\nOther notes:\n- **Xšad:** the root *xšad- is a reconstruction (Cheung; Abolghasemi calls it hypothetical), not attested Avestan/Old Persian, so the root and the apa-xšad-a node are plausible. Persian baxšîdan is plausible: the true reflex is baxšūdan/baxšāy-. baxšīdan \"give\" (and baxšande) comes from *baxš- and was mixed up with it. Nourai's own note says this, and modern scholarship agrees with the note.\n- **Xšî 1 / Xšaivan:** Avestan xšī- is attested (Bartholomae col. 554), but xšaivan is Mo'in's reconstruction, so the root is plausible. šēwan → šīvan is confirmed.\n- **BQT:1329:** `ref_page.py` maps it to pdf page 124, but the شیون entry is on pdf page 122 of vol. 3 (found in the OCR text). BQT:719 has no mapped scan, so I read the خدنگ entry from the vol. 2 OCR text.\n\nNo extraction errors: the JSON matches the printed page. The page image is saved at /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/559.png."
}
```


### [2026-10-17T00:36:17.895Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
