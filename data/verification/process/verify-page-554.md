# Verification process log — verify-page-554


## [2026-10-17T00:00:15.747Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 554 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-554.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-554.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-554.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 554` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.851Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:19.104Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:19.134Z] TOOL RESULT

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


## [2026-10-17T00:00:19.630Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-554.txt"
}
```


### [2026-10-17T00:00:19.684Z] TOOL RESULT

```
1	=== PDF page 554 (book page 524) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wi : part, apart  (refs POK:1175,1176)  PART 2
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:1175; KNT:204 | wi, vî 2, vi 3 : apart, away, opposite
5	  #2 (parent #1) [Avestan] refs=NYB:217; FFD:75 | vi-vačah : to speak against ☞Wekw ; vi-taxtî : melt apart ☞Dhogh ; vi-kar : to digest ☞Kwer
6	    #3 (parent #2) [Persian] refs=BQT:1813,1835; FFD:75 | govâžîdan «گواژیدن (گواژه)» : "to speak against" ; godâxtan «گداختن (گدازیدن ، گدازه)» : "to melt apart" ; govârdan «گواردن (گوارا ، گوارش)» : to digest
7	#4 (parent #0) [Avestan] refs=POK:1175 | viš 3, vît : apart, away, opposite
8	  #5 (parent #4) [Avestan] refs=POK:1176; KNT:208 | viš-patha : all around ; viš-pat : depart ; vîspa : all ; vîspa-dahyu : all provinces ☞Dhîs
9	  #6 (parent #4) [Avestan] refs=POK:1176; KNT:208; SOD:73 | vîtarem : sideways ; vîtara : further, later, tomorrow, morning ; vithra : separate ; ôithara : lonely
10	#7 (parent #0) [Old Persian] refs=KNT:208 | visa, vispa : all
11	#8 (parent #0) [Sogdian] refs=SOD:73 | `wc`q : tomorrow ; `yw-wšy : lonely
12	#9 (parent #0) [Germanic] refs=AHD; KLN:1748 | withro : apart with
13	  #10 (parent #9) [English] refs=None | with
14	#11 (parent #0) [Indo-European] refs=KLN:1743 | Wi-itos : to go apart (wide) ☞Ei
15	  #12 (parent #11) [Germanic] refs=None | wîdaz : wide
16	    #13 (parent #12) [English] refs=None | wide
17	--- entry 1 ---
18	ROOT Wid -> redirect to Weid
19	--- entry 2 ---
20	ROOT Wi-itos -> redirect to Wi
21	--- entry 3 ---
22	ROOT Win -> redirect to Woin
23	--- entry 4 ---
24	ROOT Wiros -> redirect to Wei 2
25	--- entry 5 ---
26	ROOT Wlkwo -> redirect to Wel 2
27	--- entry 6 ---
28	ROOT Wlnâ -> redirect to Wel 2
29	--- entry 7 ---
30	ROOT Wlp -> redirect to Wel 2
31	
```


## [2026-10-17T00:00:20.106Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-554.json"
}
```


### [2026-10-17T00:00:20.389Z] TOOL RESULT

```
1	{
2	  "pdf_page": 554,
3	  "book_page": 524,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wi",
8	        "lang": "Indo-European",
9	        "refs": "POK:1175,1176",
10	        "gloss": "part, apart"
11	      },
12	      "part": 2,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Old Persian",
18	          "refs": "POK:1175; KNT:204",
19	          "words": [
20	            {"translit": "wi, vî 2, vi 3", "gloss": "apart, away, opposite", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Avestan",
29	          "refs": "NYB:217; FFD:75",
30	          "words": [
31	            {"translit": "vi-vačah", "gloss": "to speak against", "script": null, "see": ["Wekw"]},
32	            {"translit": "vi-taxtî", "gloss": "melt apart", "script": null, "see": ["Dhogh"]},
33	            {"translit": "vi-kar", "gloss": "to digest", "script": null, "see": ["Kwer"]}
34	          ],
35	          "note": null,
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "Persian",
42	          "refs": "BQT:1813,1835; FFD:75",
43	          "words": [
44	            {"translit": "govâžîdan", "gloss": "\"to speak against\"", "script": "گواژیدن (گواژه)"},
45	            {"translit": "godâxtan", "gloss": "\"to melt apart\"", "script": "گداختن (گدازیدن ، گدازه)"},
46	            {"translit": "govârdan", "gloss": "to digest", "script": "گواردن (گوارا ، گوارش)"}
47	          ],
48	          "note": null,
49	          "quote": {"text": "گواژه که خنداندمت کند - سرانجام بادوست جنگ افکند", "poet": "Abûšakûr"}
50	        },
51	        {
52	          "id": 4,
53	          "parent": 0,
54	          "lang": "Avestan",
55	          "refs": "POK:1175",
56	          "words": [
57	            {"translit": "viš 3, vît", "gloss": "apart, away, opposite", "script": null}
58	          ],
59	          "note": null,
60	          "quote": null
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Avestan",
66	          "refs": "POK:1176; KNT:208",
67	          "words": [
68	            {"translit": "viš-patha", "gloss": "all around", "script": null},
69	            {"translit": "viš-pat", "gloss": "depart", "script": null},
70	            {"translit": "vîspa", "gloss": "all", "script": null},
71	            {"translit": "vîspa-dahyu", "gloss": "all provinces", "script": null, "see": ["Dhîs"]}
72	          ],
73	          "note": null,
74	          "quote": null
75	        },
76	        {
77	          "id": 6,
78	          "parent": 4,
79	          "lang": "Avestan",
80	          "refs": "POK:1176; KNT:208; SOD:73",
81	          "words": [
82	            {"translit": "vîtarem", "gloss": "sideways", "script": null},
83	            {"translit": "vîtara", "gloss": "further, later, tomorrow, morning", "script": null},
84	            {"translit": "vithra", "gloss": "separate", "script": null},
85	            {"translit": "ôithara", "gloss": "lonely", "script": null}
86	          ],
87	          "note": null,
88	          "quote": null
89	        },
90	        {
91	          "id": 7,
92	          "parent": 0,
93	          "lang": "Old Persian",
94	          "refs": "KNT:208",
95	          "words": [
96	            {"translit": "visa, vispa", "gloss": "all", "script": null}
97	          ],
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 0,
104	          "lang": "Sogdian",
105	          "refs": "SOD:73",
106	          "words": [
107	            {"translit": "`wc`q", "gloss": "tomorrow", "script": null},
108	            {"translit": "`yw-wšy", "gloss": "lonely", "script": null}
109	          ],
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 9,
115	          "parent": 0,
116	          "lang": "Germanic",
117	          "refs": "AHD; KLN:1748",
118	          "words": [
119	            {"translit": "withro", "gloss": "apart with", "script": null}
120	          ],
121	          "note": null,
122	          "quote": null
123	        },
124	        {
125	          "id": 10,
126	          "parent": 9,
127	          "lang": "English",
128	          "refs": null,
129	          "words": [
130	            {"translit": "with", "gloss": null, "script": null}
131	          ],
132	          "note": null,
133	          "quote": null
134	        },
135	        {
136	          "id": 11,
137	          "parent": 0,
138	          "lang": "Indo-European",
139	          "refs": "KLN:1743",
140	          "words": [
141	            {"translit": "Wi-itos", "gloss": "to go apart (wide)", "script": null, "see": ["Ei"]}
142	          ],
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 12,
148	          "parent": 11,
149	          "lang": "Germanic",
150	          "refs": null,
151	          "words": [
152	            {"translit": "wîdaz", "gloss": "wide", "script": null}
153	          ],
154	          "note": null,
155	          "quote": null
156	        },
157	        {
158	          "id": 13,
159	          "parent": 12,
160	          "lang": "English",
161	          "refs": null,
162	          "words": [
163	            {"translit": "wide", "gloss": null, "script": null}
164	          ],
165	          "note": null,
166	          "quote": null
167	        }
168	      ]
169	    },
170	    {"root": {"name": "Wid", "redirect": "Weid"}, "nodes": []},
171	    {"root": {"name": "Wi-itos", "redirect": "Wi"}, "nodes": []},
172	    {"root": {"name": "Win", "redirect": "Woin"}, "nodes": []},
173	    {"root": {"name": "Wiros", "redirect": "Wei 2"}, "nodes": []},
174	    {"root": {"name": "Wlkwo", "redirect": "Wel 2"}, "nodes": []},
175	    {"root": {"name": "Wlnâ", "redirect": "Wel 2"}, "nodes": []},
176	    {"root": {"name": "Wlp", "redirect": "Wel 2"}, "nodes": []}
177	  ]
178	}
179	
```


## [2026-10-17T00:00:29.554Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','NYB','FFD','BQT','SOD','AHD','KLN','WLD','BRT','PHD','HRN','HUB','CHEUNG','MON','ARY','SKT','IEC','SYN']:\n  v=d.get(k,{}); print(k, v.get('kind'), v.get('local_file'), v.get('page_offset'), (v.get('lookup_hint') or '')[:150])\n\"; command ls data/verification/sources/refs/ | head -100; sed -n 1,80p tools/verify_check.py"
}
```


### [2026-10-17T00:00:30.146Z] TOOL RESULT

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
POK archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-ch
KNT archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section ref
NYB archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP
FFD local_scan_ocr ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان ف
BQT archive_djvu+local_scan_ocr ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page s
SOD archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'] printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the S
AHD archive_djvu+website+archive_restricted /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word 
KLN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nour
WLD archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the 
BRT archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special translite
PHD archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https:/
HRN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak..
HUB archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the translite
CHEUNG None None None 
MON website+archive_djvu ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] 
ARY local_scan_ocr ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD 
SKT archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
IEC archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN archive_djvu /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the conc
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
```


## [2026-10-17T00:00:40.632Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 80,200p tools/verify_check.py; command ls data/verification/ | grep -E 'page-55[0-9]'; grep -c . data/verification/agent/charts/page-553.txt; head -20 data/verification/agent/charts/page-553.txt"
}
```


### [2026-10-17T00:00:40.971Z] TOOL RESULT

```
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
17
=== PDF page 553 (book page 523) ===
--- entry 0 ---
ROOT [Indo-European] Wi : part, apart  (refs POK:1175,1176)  PART 1
#1 (parent #0) [Avestan / Old Persian] refs=POK:1175; KNT:204 | wi, vî 2, vi 3 : apart, away, opposite
  #2 (parent #1) [Avestan] refs=HRN:205 | vî-čira, vîčâra : to judge ☞Kwer ; wi-čâr : to move, do ☞Kwer
    #3 (parent #2) [Pahlavi] refs=FFD:73 | vičir : judge ; wi-zârišn : to do, to translate
      #4 (parent #3) [Persian] refs=BQT:1809,2258; MON:4988 | vačar «وچر» : judgment ; vačargar «وچرگر» : judge ; gozârdan «گزاردن» : to translate | extra: گزارش ، گزیر ، ناگزیر
      #5 (parent #3) [Arabic] refs=KLN:1718 | vazîr
        #6 (parent #5) [Persian] refs=BQT:2279 | vazîr «وزیر» : minister
#7 (parent #0) [Avestan] refs=HRN:205 | vi-stâr : to spread out ☞Ster 1 ; vi-stâka : to stand against, rude ☞Stâ ; vi-saëd : to cut off ☞Sek ; vi-šâ, vi-sâ, vi-hây : to open ☞Sě 1
  #8 (parent #7) [Persian] refs=BQT:1800,1816,1818 | gostardan «گستردن (گسترش ، بستر)» ; gostâx «گستاخ» : "(one who) stands against" ; gosastan «گسستن (گسیختن ، گسیل)» : "cut apart" ; gošâdan «گشادن»
#9 (parent #0) [Avestan] refs=HUB:95 | vi-mad : to cure ☞Me ; vi-radh, vi-raiti : to set separate, edit ☞Ar ; vi-manah : think apart, guess ☞Men 1 ; vi-mar : to designate ☞Mer 1
  #10 (parent #9) [Persian] refs=BQT:437,834 | bîmâr «بیمار» ; vîrâstan «ویراستن (ویراستار)» : "to set apart", edit ; gomân «گمان» : "think apart", guess ; gomârdan «گماردن (گماشتن،گماشته)» : "to designate"
#11 (parent #0) [Avestan] refs=POK:1176; HRN:199,203 | vi-kâs : see apart ☞Kwek ; vi-raeč : run away ☞Leigh 2 ; vi-saiti : (two) separate tens ☞Dekm ; vi-tar : to go further, cross ☞Ter 1
  #12 (parent #11) [Persian] refs=BQT:1776,1778,1806 | govâh «گواه (گواهینامه)» ; gorixtan «گریختن (گریز)» : run away ; bîst «بیست» : two "separate" tens ; gozaštan «گذشتن (گذاشتن ، گذاردن)» | extra: گذشت ، گذر ، گذار ، گدار ، گذرنامه
#13 (parent #0) [Avestan] refs=NYB:217; FFD:75 | vi-čay, vi-kay : choose apart ☞Kwei 2 ; vi-žainti : to hit against, harm ☞Gwhen 2 ; vi-maik : mix different things ☞Meig
  #14 (parent #13) [Persian] refs=BQT:1813,1835; FFD:75 | gozîdan «گزیدن ۱ (گزینش،برگزیدن)» : "choose apart" ; gazîdan «گزیدن ۲ (گزند)» : "hit against" ; gomîxtan «گمیختن (گمیز)» : "mix different things"
```


## [2026-10-17T00:00:43.564Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-17T00:00:44.029Z] TOOL RESULT

```
{
 "pdf_page": 538,
 "book_page": 508,
 "verified_by": "claude-opus-5.5",
 "verified_on": "2026-10-16",
 "entries": [
  {
   "entry": 0,
   "root": "Wekw, Weqw",
   "verdict": "confirmed",
   "modern_form": "PIE *wekʷ- 'to speak' (Pokorny 1135-1136 u̯ekᵘ-; LIV² 673f.; Watkins wekw-; o-grade root noun *wṓkʷs 'voice')",
   "note": "Root, label and gloss are correct: Pokorny 1135 u̯ekᵘ- 'sprechen' with Skt. vakti, vāc-, vacas-, Av. vac-, vacah-, vāxš, Gk. épos, ops, Lat. vōx, vocāre (WP I 245f.). Cheung 2007 (*u̯ač) and Wiktionary agree. The Latin/English branch and the Avestan vāč-/vacah-/uxδa- branches are textbook. The weaker parts of the chart are the Iranian compounds Nourai reconstructs or invents to reach particular New Persian words: 'paurvatâ-vac' (for pažvāk), 'hu-ni-vak' (for xonyā), Avestan 'vaxš-ô-bara' (only a reconstruction *vaxša-bara- behind MP waxšwar) and 'Old Persian wâk/wânk' (not attested). The derivation of xonyā (MP huniyāg) from *hu-ni-vāka- is opposed by the Middle Persian form, which has no -w- (see node 9). forūxtan 'sell' is linked to vac- by Justi/Horn/Mo'in, but Cheung puts it under *waxš- 'grow' (see node 4). The extraction matches the printed page (checked against site/pages/538.jpg).",
   "note_fa": "ریشهٔ هندواروپایی آغازین *wekʷ- «سخن گفتن» با بالاگونهٔ o در نام‌واژهٔ *wṓkʷs «آواز، صدا» در پوکورنی (ص ۱۱۳۵-۱۱۳۶)، والده-پوکورنی (ج ۱، ص ۲۴۵)، واتکینز و چونگ آمده است. بازمانده‌های آن سنسکریت vāc- و vacas-، اوستایی vāč- (حالت فاعلی vāxš) و vacah- «سخن»، یونانی épos و لاتینی vōx و vocāre است. ریشه و زبان و معنایی که نورایی داده درست است. ولی چند ترکیب ایرانی در این نمودار ساختهٔ خود اوست و در متن‌ها نیامده، مانند paurvatâ-vac و hu-ni-vak و vaxš-ô-bara. پیوند «خنیا» با این ریشه هم با پژوهش امروزی سازگار نیست.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-"
   ],
   "ref_check": [
    {
     "ref": "POK:1135",
     "status": "supports",
     "note": "POK_full.txt l.90116ff. 'Root / lemma: ueḱ- (*hueḱᵘ-) / Meaning: to speak / Material: Old Indic vakti, vivakti says, talks, speaks ... Avestan vac- speak, uxta-. Old Indic vacas- = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word ... Latin vox, vocis voice, voco, -are call ... References: WP. I 245 f.' Page(s) 1135-1136."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 245-246 (WLD_Bd1_pages.txt l.22850ff., leaf 253)",
     "stance": "supports",
     "note": "'uekᵘ- „sprechen“. Ai. vákti, vivakti „sagt, redet, spricht“ ... av. vac- „sprechen“, uxta- ... ai. vacas- n. = av. vacah- (= gr. épos) „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“ ... lat. vox vocis „Stimme“, voco, -āre „rufen“'."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985 s.v. wekw-",
     "stance": "supports",
     "note": "AHD_watkins1985.txt: 'wekw-. To speak. 1. O-grade form *wokw- in: a. Latin vox (stem voc-), voice: VOCAL, VOICE, VOWEL ... 2. Suffixed o-grade form *wokw-a- in Latin vocare, to call: VOCABLE, VOCATION ... 3. Suffixed form *wekw-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekw- 1135.]'"
    },
    {
     "src": "IEC",
     "where": "s.v. uequó",
     "stance": "partial",
     "note": "IEC.txt l.20012 'uequó (uequmi, uiuéqumi) call, say, speak ... WP I, 245 Skt. vakti ... Av. vač-, v. talk; Per. gūyam, inf: guftan, v. say' -- Mann has the root but wrongly files Persian guftan here (that verb is from *gaub-)."
    },
    {
     "src": "SYN",
     "where": "18.11 VOICE; 18.26 WORD",
     "stance": "supports",
     "note": "SYN.txt l.31455 '1. Derivs. of IE *wekʷ- speak, say (18.21). Walde-P. 1.245f. ... Grk. óps (poet.); Lat. vōx ...; Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš); Toch. A wak, B wek'; l.31765 'Skt. vacas-, Av. vacah- ... Lat. vocabulum (more directly fr. vocāre call)'."
    },
    {
     "src": "CHEUNG",
     "where": "pp. 402-404 s.v. *u̯ač",
     "stance": "supports",
     "note": "CHEUNG.txt l.26156ff. '*uač to say, speak / AVESTAN: vaoc- (vāč-) to say || (+ *ā-) to say to || (+ *fra-) to proclaim ... PIE *uekʷ- to speak, to say > LIV: 673 f. | Pok.: 1135 ff.'"
    },
    {
     "src": "ARY",
     "where": "p. 513 (pdf 512) s.v. واژه، وات، واج",
     "stance": "supports",
     "note": "ARY_latin_index_pages.txt l.14955ff.: Avestan 'VAXSH, VAK, VACHAH', Pahlavi 'WAZ, VACHAK, WAZAG, VAJ', English VOICE, Latin VOX, VOCEM; references 'POKORNY 1135-1136'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "vak, vačah, vaxš 1",
     "verdict": "confirmed",
     "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root
```


## [2026-10-17T00:01:02.415Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'Page(s) 117[4-7]' POK_full.txt | head; grep -n 'Root / lemma: u̯i-\\|Root / lemma: ui-\\|lemma: u̯i\\b' POK_full.txt | head"
}
```


### [2026-10-17T00:01:02.724Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:01:17.013Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s)' POK_full.txt | awk -F'Page\\\\(s\\\\)' '{print $0}' | grep -E ' 11(7[3-9])' | head; grep -n 'vītarəm\\|vitaram\\|vitarám\\|vītara' POK_full.txt | head"
}
```


### [2026-10-17T00:01:17.367Z] TOOL RESULT

```
92619:Page(s): 1173-1174 
92826:Page(s): 1174-1175 
92991:Page(s): 1175-1176 
93050:Page(s): 1177-1178 
93117:Page(s): 1178-1179 
93215:Page(s): 1179-1180
```


## [2026-10-17T00:01:21.518Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92826,93050p POK_full.txt"
}
```


### [2026-10-17T00:01:21.814Z] TOOL RESULT

```
Page(s): 1174-1175 

Root / lemma: uag- : uag- {*huegh^ 

Meaning: to be bent 

Material: Latin vagor, -5/7"schweife umher, breite myself from', vagus ^ wandering '; Old 

Irish fanm. 'slope, cavity; slantwise, abschliJssig' {*uag-no)\ acymr. guoin, cymr. gwaun 

'lowland, depression, meadow', corn, goen, goon, gon, bret. geun, ye^/7 'marshland' 

{*uagna). 

References: WP. I 218, WH. I 268, II 726, Loth RC 36, 181; 

See also: compare ua-, uek-, uak-, ueng(h)-, uenk-. 

Page(s):1120 

Root / lemma: £/aAr-(: *uak-) {* huek-) 

Meaning: to be bent 

Material: Latin vacillo, -are 'wobble, sway, waver'; abrit. VN OuaKo-fjayoi 'die Bewohner 

the gekrijmmten Felder', cymr. gwaeth {*uak-to-) Kompar. 'bad' (Superl. gwaethaf), corn. 

gweth. Middle Breton goaz. 

References: WP. I 218, WH. I 268, II 723 ff.; 

See also: s. also ua-, uag- etc. 

Page(s):1135 

Root / lemma: uiiyu- {*hueighu-) 

Meaning: tree 

Note: 

Root/ lemma: uiA'^u-i* hueighu^: 'tree' derived from alb. -lllyrian vith. Gen. K/ic//7'elm tree' 

of Root/ lemma: uing-3iU6 ueig-{uig-l) : 'elm'; common alb. -g- > -d-. 



Material: Old Irish fid, Gen. fedo^\xee, wood, wood, forest', cymr. gwydd{S<^. gwydden), 
acorn, gulden, br. gwez{SQ. gwezenn) ds., also in cymr. syb-wydd^'^\v\e' ("Resinous tree ') 
= corn, sib-uit, gall. VN Uidu-casses, Old Icelandic vidr. Gen. vidarm. "wood, forest, wood, 
tree'. Old English widu, wudum. ds.. Old High German witu, 147/0 "wood'; 

perhaps as "Grenzbaum, trennender Grenzwald between Ansiedlungen' to *ueid!^- 
"separate, divide' and then formal = Old Indie vidh'u- "vereinsamf, Lithuanian vidus^ 
center, the interior'; compare above S. 707 Lithuanian medzias^iree"; 

connection with Irish ffad^wM, fladach' hunt', cymr. gwydd'wM', acorn. gu/t-f/71era', 
bret. ^c»^ez"wild' would be the meaning after through Latin s/'/vat/cus'wM : s/7va, 
Lithuanian med/n/s^wM', medz/dk/e' hunt' : med/s'tree' to prop, support, yet bliebe dabei 
die lengthened grade e/ compared with dem Grundworte Irish /^icy difficult, hard; es is hence 
fladirom f/dto separate and auf eine besides *ue/-t- in Old High German weida. Old 
English wad. Old Icelandic veidr^ hunt, fishing' (: *uei-3) liegende root form *uei-c^h)- to 
beziehen. 

References: WP. I 314, 228 ff. 
Page(s):1177 

Root / lemma: u/ng- and ue/g-{u/g-7) {*hueik-) 
Meaning: elm 

Material: With nasalization Balto Slavic group Lithuanian vinksna, Latvian v/'ksna ds. (also 
Old Prussian w/m/no'e\r(\', lies wincsnd) from *u/ng-sna {Suii. as in Lithuanian g/uosna' 
willow '); 

nasalized Old English w/ic, wTce, engl. witch. Low German W77re"elm'; 

likewise uing- as uig- can be in alb. vith. Gen. i//o'/7"elm' and in Kurdish K/z"a kind of 
elm'; the relationship of the nasalized against unnasalized form is still to be cleared, 
(common alb. Celtic -k > -th, -g > -dh > Slavic Iranian z-) 

Serb. Kez(Gen. i/eza), russ. vjaz-b, poln. M//^z"Ulmus campestris' (proto Slavic. V^zb); 
References: WP. I 314, Specht Indo Germanic Dekl. 59 f., Trautmann 360, Vasmer 1, 244, 
Petersson Heteroklisie 56 f. 
Page(s):1177 

Root / lemma: ujeth-, uith- {*haueith-^ 
Meaning: to shake 



Material: Old Indie vyathate' sways, taumelt, geht schief, kommt to Falle, shrugs, jerks, 

weicht', vithura-^ fluctuating, mangelhaft'; Gothic wiPon^ shake' \ relationship to *uei-1 

"turn' is probably, da in Kreise this root words for 'waver, hin and her bewegen' right 

frequent, often are. 

Maybe alb. vithe " buttocks, hips '. 

References: WP. I 318, Kuiper Nasalpras. 53, Wackernagel-Debrunner II 2, 487. 

Page(s):1178 

Root / lemma: uTks- {*hauiks^ 

Meaning: ' mistletoe and other glue delivering trees ' 

Note: {u7sk-l) 

See also: s. S. 1134 (ue/s-). 

Page(s):1177 

Root / lemma: uT-Rnrit-T{* hauT-RrQt-J) 
Meaning: twenty 

Note: actually Dual "two decades ' (to Indo Germanic oT-'two' and dRrpt- above S. 192) 
Material: Old Indie viifisatf-, Avestan vTsaiti, osset. insai, Armenian k'san, gr. eiKoai, Doric 
FiKQTi, hom. EsiKOGi for £(F)lKoai, alb. zet, Latin vTginti{see above S. 192), Old Irish fiche. 
Gen. fichet {*uiRmt-s, -os), acymr. i/ce//?/ (instead of *gwyca/ntirorr\ the compound *dou- 
viceint, cymr. deugaint^AQ" abstracted), corn, ugans, Tocharian A wiki, B ik9. 
References: WP. I 313, Wackernagel-Debrunner 3, 366 f., WH. II 788 f.. Frisk 453 f. 
Page(s):1177 

Root / lemma: u7-1 {*hauV) 
Meaning: separate from; both, two 
Note: (see uT-Rixit-fj 

Material: Old Indie k/- 'apart', Avestan i/7- 'apart; abseits, apart, separated from; entgegen; 
through and through ' (also vis-: v/s-pat-^go away, pass over'); Old Indie i//si/- 'after variant 
Seiten' in i//si//7a- 'verschiedenartig', iz/siz-zt/pa- 'verschiedengestaltig' , v/suva-n. 
'aequinoctium', visuvant- 'in the middle situated, after beiden Seiten gleich', visv-anc- 
'afterbeiden (all) Seiten gewandt, auseinandergehend'. Old Indie i//5i/5-o'/y5/7/r'uberallhin 
going', Avestan vispa&aMN. 'ringsum allenthalben' {*uisu- dw^, *uisuo-\ besides *uiso-\v\:) 
Lithuanian visas, Latvian viss. Old Prussian wissa-^aW; Old Church Slavic i/i.56 'all, 
whole'; with the same meaning 'all' from 'after all Seiten auseinandergegangen, 
umfanglich' and Indo Germanic A^-suffix: Old Indie visva- ' each, every, all', Avestan vfspa-. 



ap. vispa- "ds.'; Sg. also "whole' ( *uiRuo-\ out of it also Old pers. visa- with regular 
southwest - development from -si/-); 

to stem *uisu-, uisuo- presumably also gr. FiaFo(;, \qoc, " alike ' (for das on the other 
hand derivation from *uidsuos\.o *ueid- " behold ' erwogen wird); 

Latin v/t/umlau\t, error, disability, damage' as *i//-//-c»/r7"*Abweichung'; vitupero, -are 
"spoil, tadle' {vitium + parare); in addition Latin vitilTgoi. " skin rash '. 

comparative *uitero-. Old Indie i///a/'a- "further fijhrend', i///a/'5/77 "further, further', 
Avestan vTtaram^ sideways ', vTtara- "the weitere, spatere', d/^ra(\.e. vi&ra) Adv. " 
particularly, specially, especially, particular: in particular, peculiarly, separately, extra, 
notably, apart, separated', Gothic wiPraMv. and preposition m. Akk. "gegen, wider, 
compared with, vor'. Old Icelandic vidrMy. and preposition m. Dat. Akk. "gegen, wider, 
with, by' (also i//id' after Paaren as nordr: nord). Old English widMv. and preposition m. 
Gen. Dat. Akk. "gegen, compared with, wider, along, with', wider-\v\ compounds. Old High 
German widarMv. "gegen, back, against', preposition m. Dat. Akk. "gegen, compared 
with, wider'; Latin perhaps in i//?/7ici/s "Stiefvater', originally "the second ', or "the entferntere 
Vater' (but Old High German entrig, das an the einzigen Stelle, where es vorkommt (1 1 . 
Jh.), "transtiberinus' iJbersetzt, wird rather to e/70/7/" beyond' belong); Old Church Slavic 
vbtorb " alter, secundus ' (from *vbtorb). 

References: WP. I 312 f., WH. II 80, 808, Vasmer 1, 192 f., 237, Trautmann 362 f. 
Page(s): 1175-1176 

Root /lemma: u7-2, uoi- {* hau7-sl^ 

Meaning: expr. root 

Material: Gr. {*uT-ska) ia, Ionian in f. "shout, call, scream' (Fia:), (*FiaFT) iaT,1ri "exclamation 

of Freude or of Schmerzes', hom. (F)i6|JU)poi epithet the Argiver (" (3or|v ayaOoi '); 

(*Fir|Fioq) iniO(; epithet of Apollo (den man with ir| naicbv anrief), hence perhaps 

(*FiaFov£(;) laFovsc;, "Iwvsc; "lonier' as "Verehrer of Apollo'; (*Fir|FiO(;) iniO(; or ia-Rufer (? 

Schwyzer Gr. Gr. 1, 80); Old English by/"(besides weg, wei, wa) "weh, oh'; due to *uT-to- 

"jubelnd' here Lithuanian vyturys^ lark ' and probably Latin vTtulor^ jubilate, cheer, stimme 

einen Sieges- or hymn of praise, song of praise an, be cheerful'; Old Russian viskati^ 

neigh ', visngtr muttire ', russ. dial, viscatb, poln. wiskac, w/szczec'\ou6 whistle'; russ. 

v/zg' Gewinsel ', vizzatb " whimper '. 

Maybe in -A suffix in alb. fishkellej^ whistle '. 

References: WP. I 312, 527, WH. II 807, Holthausen Ae. etym. Wb. 392, Vasmer 1, 199. 



Page(s):1176 



Root / lemma: uTro-s {*haueir-) 

Meaning: man; warrior 

Material: With f. Old Indie vTra-, Avestan vTra- "man, hero ', Umbrian Akk. PI. n. u(e)iro^ 

mancipia ', Volscan Abl. Sg. couehr/u ^*coy\n6, contione ', Lithuanian vyras, Latvian mrs, 

Old Prussian w/jrs^man'; skyth. oiop ' av5pa ' (Herod. 4, 110), more properly oipo- = v/ro-, 

Old Indie v/rapsa-irom * vTra-psv-a- {: Avestan pasu vTra) 'people and cattle', compare 

Umbrian ueiro pequo6,s. 

With / Latin iz/^'man', in the old language also the unique word for " husband ', 
wherefore K/Aa^d'mannhafte virgin, Heldin', virtus^ manfulness, skillfulness, virtue, 
uprightness, integrity ', Old Irish /fe^'man', cymr. etc. gwr, PI. gwyr{{o which the Sg. gwr 
analogically is formed additionally). 

Gothic wafr. Old Icelandic verr. Old High German Old Saxon Old English wer^rc\av\\ 
Tocharian A wir^ young '; Modern High German Werwolf, probably to Latin vTs " power ' 
etc., "Vez-'auf etwas losgehen', s. d. 

References: WP. I 314 f., WH. II 796 f., Trautmann 360, W. Schuize Kl. Schr. 398, 
Untermann, IF. 62, 127. 
Page(s): 1177-1178
```


## [2026-10-17T00:01:28.539Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A8 '^wi-\\.' AHD_watkins1985.txt | head -30; grep -n '^with,\\|^wide,' KLN_1966.txt; grep -n '^WITH\\b\\|^WIDE\\b' SKT.txt"
}
```


### [2026-10-17T00:01:28.910Z] TOOL RESULT

```
1167:wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< “far apart”): WIDE. 2. Suffixed (comparative) form *wi-tero- in Germanic *withr6, against, in: a. Old English wither, against, with its derivative with, with, against: WITH, WITHERS; b. Old High German widar, against: GUERDON; WITHERSHINS. [Pok. 1. wi- 1175.]
1168-widhu-. Tree. Germanic *widu- in Old English wudu, wood: woop. [Pok. uidhu- 1177.]
1169-wikmti. Twenty. Compound of wi-, in half, hence two, and *(d)kmt-i (nominative dual), decade, reduced zero-grade form of dekm. 1. Latin viginti, twenty: VICE- NARY, VIGESIMAL. 2. Greek eikosi, twenty: ICOSAHE- DRON. 3. Sanskrit vimsatih, twenty: PACHISI. [Pok. ui-kmt-i 1177.)
1170-wi-ro-. Man. Derivative of weie-?. 1. Germanic shortened from *wiraz becoming *weraz in: a. Old English wer, man: WEREWOLF, WERGELD; b. Germanic compound
1171-wrod-
1172-*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1173-wrdd-
1174-ROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]
1175-wrod-. To root, gnaw. Germanic *wrét- in Old English wr6tan, to dig up: ROOT?. [Pok. 7. ver- 1163.]
```


## [2026-10-17T00:01:32.191Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^with\\b\\|^wide\\b' KLN_1966.txt KLN_1971.txt | head; grep -n -i '^WITH\\|^WIDE' SKT.txt | head"
}
```


### [2026-10-17T00:01:32.525Z] TOOL RESULT

```
KLN_1966.txt:1449:with  verbal  suff.  -ate  fr.  L.  acidulus,  dimin.  of acidus.  See  acidulous.
KLN_1966.txt:2441:with  subst.  suff.  -ite;  so  called  because  it  re¬ sembles  amber.
KLN_1966.txt:3974:with  OSlav.  vlekg,  vlesti,  Lith.  velkit,  vilkti,  ‘to draw,  drag’.
KLN_1966.txt:4371:with  a  leash’,  fr.  Hem,  ancient  form  of  lien, ‘band’.
KLN_1966.txt:6360:with  stiff,  -ic  fr.  L.  cannabis.  See  next  word. Cannabis,  n.,  a  genus  of  plants,  the  hemp  (hot.)  — L.  cannabis ,  ‘hemp’,  fr.  Gk.  xavvafkc;.  See  canvas, cannel,  n.,  a  gutter;  kennel.  —  ME.  cane!,  fr. ONF.  cane!,  fr.  L.  canalem ,  acc.  of  canalis, ‘pipe’.  See  canal  and  cp.  kennel,  ‘gutter’, cannel  coal,  a  bituminous  coal.  —  Corruption  of candle  coal.
KLN_1966.txt:7882:with  L.  clavis,  ‘key’,  clavtts,  ‘nail’,  claudere,  ‘to shut’.  See  close,  adj.,  and  cp.  cleisto-,  cleithral and  the  first  element  in  cleoid.  Cp.  also  clathrate.
KLN_1966.txt:9545:with  adj.  suff.  -al  fr.  ML.  cranium.  See  cranium. Derivative:  cranial-ly,  adv. cranio-,  combining  form  denoting  the  skull  ( anat .')
KLN_1966.txt:10038:with  an  element  or  a  radical  (chem.)  —  See  prec. word  and  chem.  suff.  -ide,  resp.  -id.
KLN_1966.txt:10135:with  Of.  svdsati,  svdsiti,  ‘blows,  breathes,  sighs'. L.  queri,  ‘to  complain’.  See  quarrel,  ‘dispute’, cyst-,  form  of  cysto-  before  a  vowel.
KLN_1966.txt:13191:with  Avestic  gava,  ‘both  hands’.  Both  these
595:with  other  metals.  Either  a  corTUV\\on  ot
1568:with  mm ;  Ace
8592:with  O.  H.  G./oraAarv,
11144:with   F.  marmot,  *a  tnarmoset,  or  K monkey;*  which  ts,  a^in,  quite  a  diffeid word  from  E.  tnat  •  '-jw),
12660:with  £.  ntJU.)     Formed  from  M.  £.
13091:with  suffix  -act  (^L.  -Aroa).
13511:with  suffix  'Qieus,  from  h*  papf^i form  of fa/iiic,  a  butterfly  vabo
13540:with  iu  beak :  pick  and  peck iants  ;    cf.  M.  E.  pikken,  ptk-
15850:with  suffix  -y;  a  coined  word.     See  ruin
17600:with  the  hammer.  — A.  S.  smiS-tn  •,  pp.  of lost  strong  verb  sml^n  •  (sec  above). +  Du. smui\  Ice!. /«/iV:    Don.  Swed.  .;#//(/ ;  G. schmied;  Goth,  smitha.       Cf.  Don.  smedt, Swcd.  jMid^.  to  forge;  Icel.  nff/fi,  smith's work,  from  an  Icel.  lost  strong  verb  cog- nate wilh  Swcd.  dial,  smida  (above).     Der. smithy.  A.  S.  smt^'^  Uccl.  smfti/a). Smother,  Smoulder;  see  Braell. Bmu^,  Smuggle :  sec  Smock. Smudge,  Smut ;  see  Smit«. J  Snack;  sec  Snatch,
```


## [2026-10-17T00:01:35.686Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'with,  prep\\|with, prep\\|wide,  adj\\|wide, adj' KLN_1966.txt KLN_1971.txt | head; grep -n -i 'With,\\s*prep\\|Wide,\\s*adj\\|^Wide\\b\\|^With\\b' SKT.txt | head"
}
```


### [2026-10-17T00:01:36.092Z] TOOL RESULT

```
KLN_1971.txt:267049:wide, adj. — ME. wide, fr. OE. wid, rel. to OS., 
KLN_1971.txt:267062:(adj.) See wide, adj. 
KLN_1971.txt:267066:wid, ‘wide’. See wide, adj. and -ness, 
KLN_1971.txt:267769:with, prep. — ME. with , ‘against; with’, fr. OE. 
595:with  other  metals.  Either  a  corTUV\\on  ot
1568:with  mm ;  Ace
8592:with  O.  H.  G./oraAarv,
11144:with   F.  marmot,  *a  tnarmoset,  or  K monkey;*  which  ts,  a^in,  quite  a  diffeid word  from  E.  tnat  •  '-jw),
12660:with  £.  ntJU.)     Formed  from  M.  £.
13091:with  suffix  -act  (^L.  -Aroa).
13511:with  suffix  'Qieus,  from  h*  papf^i form  of fa/iiic,  a  butterfly  vabo
13540:with  iu  beak :  pick  and  peck iants  ;    cf.  M.  E.  pikken,  ptk-
15850:with  suffix  -y;  a  coined  word.     See  ruin
17600:with  the  hammer.  — A.  S.  smiS-tn  •,  pp.  of lost  strong  verb  sml^n  •  (sec  above). +  Du. smui\  Ice!. /«/iV:    Don.  Swed.  .;#//(/ ;  G. schmied;  Goth,  smitha.       Cf.  Don.  smedt, Swcd.  jMid^.  to  forge;  Icel.  nff/fi,  smith's work,  from  an  Icel.  lost  strong  verb  cog- nate wilh  Swcd.  dial,  smida  (above).     Der. smithy.  A.  S.  smt^'^  Uccl.  smfti/a). Smother,  Smoulder;  see  Braell. Bmu^,  Smuggle :  sec  Smock. Smudge,  Smut ;  see  Smit«. J  Snack;  sec  Snatch,
```


## [2026-10-17T00:01:39.572Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 267049,267062p KLN_1971.txt; echo ----; sed -n 267769,267790p KLN_1971.txt; grep -n 'WIDE\\|WITH,' SKT.txt | head"
}
```


### [2026-10-17T00:01:40.060Z] TOOL RESULT

```
wide, adj. — ME. wide, fr. OE. wid, rel. to OS., 
OFris. wid, ON. vidr, Dan., Swed. vid, Du. wijd, 
OHG., MHG. wit, G. weit, fr. Teut. *wida-, cor- 
responding to I.-E. *wi-ito-, which is formed fr. 
I.-E. base * wi-, ‘asunder’, and the pp. stem of 
I.-E. *ei-, ‘to go’. For the first element see with, 
for the second see itinerant. 

Derivatives: wide, adv. (q.v.), wide , n., wide-ly, 
adv., wid-en , v., widen-er , n., wideness (q.v.), 
wid-ish, adj. 

wide, adv. — ME., fr. OE. wide, fr. wid, ‘wide’ 
(adj.) See wide, adj. 
----
with, prep. — ME. with , ‘against; with’, fr. OE. 
wid, ‘opposite, near; against; with’, OS. with, 
ON. vid, of s.m.; rel. to OE. wider , ‘against’, 
which, together with OS. withar, ‘against’, ON. 
vidr , ‘against, with, toward, at’, MDu., Du. 
weder, Du. weer, ‘again’, Goth, wipra, ‘against, 
opposite’, derives fr. I.-E. *wi-t(e)ro-, lit. 
‘more apart’, formed with compar. suff. -ter 
(see -flier), fr. I.-E. base *wi-, ‘against; apart, 
asunder; two’, whence also OI. vi, Avestic vi- 
‘asunder’, OI. vitardm , ‘farther, further’, 
Avestic vitar e m, ‘sideward’, OSlav. vutoru (for 
*vitoru), ‘other, second’; Gk. tSiog, ‘one’s own’, 
and tnog, ‘equal’, are not cognate. Cp, withers 
•and the first element in withershins. Cp. also 
wide. Cp. also vice, ‘moral fault’, and the first 
element in vicennial and in guerdon, vihara, 
vimana, visarga. With has superseded to OE. 
preposition mid, ‘with’, which has survived only 
as a ModE. pref. (see midwife). The orig. sense 
of with (‘against’) has survived in compounds 
(cp. e.g. withdraw, withhold, withstand).
```


## [2026-10-17T00:01:47.955Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'gudāxtan\\|gudaxtan\\|gudākhtan\\|gudāzīdan\\|gudâxtan\\|gudächtan\\|gudäxtan\\|gudākh' HRN.txt HUB.txt CHEUNG.txt | head -20; grep -n -i 'guwārdan\\|gugārdan\\|guvārdan\\|gugar\\|wigār\\|gugāridan\\|guwardan\\|guvardan' HRN.txt HUB.txt CHEUNG.txt PHD.txt NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:01:48.302Z] TOOL RESULT

```
HUB.txt:5477:§ 45. Ap. V =^ np. g: gudaxtan *schmelzen' = phi.
CHEUNG.txt:24524:*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
CHEUNG.txt:41043:gudaxtan/gudaz-, 376 
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
PHD.txt:1607:digest gugar(i)dan.
PHD.txt:5446:gon gonag dowom drustih drust gowizar gozénag gugay gugay gugayih gugayih gugan- gokanig gokan doganag gugar- gugārīdan gugārdan dēk gēūgirdūmand gogird даг, рог, gul dol gurbag
```


## [2026-10-17T00:01:54.173Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24505,24535p CHEUNG.txt; sed -n 5470,5485p HUB.txt; grep -n 'widāxtan\\|widaxtan\\|widāz\\|gudāxt\\|wiwāz\\|guwāz\\|gowāz\\|guwāž' PHD.txt NYB_vol2_glossary.txt HRN.txt CHEUNG.txt | head"
}
```


### [2026-10-17T00:01:54.676Z] TOOL RESULT

```
339b 
Pres.: IND. 3sg. MMP wadcyd; Partic.: perf. pass. BMP wt'htk /widaxtag/, BMP wt’ht /widaxt/; Caus.: 
pres. IND. 3sg. BMP wt'cyt /widazed/, BMP wt'cynyt /widazénéd/; Inf.: caus. BMP wt'htn /widaxtan/ 


*PARTHIAN: (+ *ui-) wdc- ‘to melt’, w(y)d'c- (caus.) ‘to dissolve" = Ghilain: 50, 47 
| DMMPP: 338b £. 

Pres.: IND. 3sg. wdcyd; Caus.: IND. 35р. wd’cyd, wyd’cyd; Partic.: perf. pass. "wdxtg; Inf.: "wdxtn 
*KHOTANESE: (+ *ui-) LKh. byaj- (byas-) ‘to dissolve’ = SGS: 104 

*SOGDIAN: (+ *ui-) BSogd. wyt’wxs ‘to disappear, melt away’, BSogd. wyt’yc ‘to 
melt’ 

(+ *ui-) Pres.: IND. 3sg. BSogd. wyt’wxsty, BSogd. wyt’wxst’y, CSogd. “wytwxsty; Partic.: perf. pass. 
BSogd. wytwytk ‘molten’; Caus.: pres. IND. 3sg. BSogd. wyt’yct 


*NWIR: (+ *ш-) NP gudaxtan/gudaz- ‘to smelt, melt’, ? Kurd. (Kurm.) 
bihöstin/bihös- ‘to melt’ (why -0- ?) 

9 The close match in meaning between the Ir. and Gr. forms suggests a common IE 
origin. Hence, the formally identical forms with the meaning ‘to run, walk, sim.’ 
should be excluded (*ta&!). *taHé appears to be an enlarged root of *taH. 

«PIE "enlarged" *teH5k- ‘to melt" = LIV: 617 | Pok.: 1053 


*IE COGNATES: Gr. 14c, (Dor.) тако ‘I melt [tr.]', (Hom.) ёт@кту ‘melted [intr.]’ 
*REFERENCES: Horn 1893: 199; Nyberg II: 217a; DKS: 307b; Gharib: 427b; Cabolov 2001: 175 
Gl. 214, phi. oes, bal. g^; b%nam sehe' = ap. *vainamiy
(belegt vainahy, avaina); blm 'Nase = paz. vlni Shk. 273;
blst zwanzig = phi. vtst, zd. vlsaiti; bimdr 'krank* = paz.
vimar Shk. 273, Min. Gl. 215, phi. vimar; biyaban 'Wiiste,
Ebene', g. vmbUn, phi. viyapan Gl. and Ind. 226; beva *Wittwe
= phi. vevak ZPGl. 5, 3 aus *viyavak = zd. vidava ZPGl. 5.
Dazu Bahranij Bala$, Bad yes, BarOz § 51.
§ 45. Ap. V =^ np. g: gudaxtan *schmelzen' = phi.
v(i)taxtan Gl. and Ind. 234, zd. vitaxti- ^) ; gudara 'Brett* aus
*) In Zend 8teht*ti- regelmftssig fiir urspr. ri-; im Phi. wii^^f-
fiir urspr. vi- geschrieben, im Armenisohen failt * in nioht-letzter Silbe
lautgesetzUch aus.— 156 —
^vitara-y vgl. zd. mtara- *Brett'?, nach Darmesteter =
'allee' (oben p. 91), guddstan *passiren lassen , guSastan Vor-
ubergehen', phi. v(i)tartan, v(i)tartan to pass Gl. and Ind.
234, 235, ap. viyatarayama 'wir uberschritten' ; gurextan
PHD.txt:651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
PHD.txt:1651:dissolve widaxtan.
PHD.txt:1652:dissolved, be — widāzīhistan.
PHD.txt:2774:melt widaxtan.
PHD.txt:5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
CHEUNG.txt:24508:pres. IND. 3sg. BMP wt'cyt /widazed/, BMP wt'cynyt /widazénéd/; Inf.: caus. BMP wt'htn /widaxtan/
```


## [2026-10-17T00:02:00.070Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24485,24504p CHEUNG.txt; grep -n 'gugar\\|guwār\\|guvār\\|gawār\\|gugār' CHEUNG.txt | head; grep -n '^widāxtan\\|^widaxtan\\|^vitāxtan\\|^witaxtan\\|^vitaxtan\\|^gugār\\|^gugar\\|^vivāč\\|^wiwāz' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:00.391Z] TOOL RESULT

```
shed, spill (blood)’ || (+ *nis-) Sh. naXtiy-/naXtizd, naxtüyd, Rosh. nixtéy-/nixtizd, 
nixtuyd, Bart. nixtéy-/nixtuyd ‘to go, come out, flow out’ (certainly influenced by 
*tac) 


376 *taHé 


«PIE *teH>- ‘to melt, thaw’ = LIV: 616 | Pok.: 1053 


*IE COGNATES: Arm. t‘anam ‘I dive’, OCS tajeti ‘to melt’, ? Welsh tawdd ‘melts’ 
*REFERENCES: КРЕТ. 142a; EVP: 79; KPF II: 189; Abaev, Slovar’ I: 180; MacKenzie 1966: 110; EVS: 
52a, 93b’ DKS: 2b; Abaev, Slovar’ III: 222 f.; Abaev, Slovar’ IV: 7 f.; Cabolov 1997: 74; NEVP: 84 


*taH ‘to melt’ 
*MIDDLE PERSIAN: (+ *ui-) MMP wdc- ‘to melt [intr.]’, BMP wt’c- /widaz-/ (caus.) 
‘to melt [tr.], BMP wt’cyn- /widazén-/ (sec. caus.) Чо cause to melt? = DMMPP: 

4248:vitaxtan vitdc- trans. to melt: bé witäcet 10177, — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wd’c- (MHC), Ghilain 50; MPrs. wdc- (8), Verbum 169; Paz. vadáxtan vadāž- (SGV); NP gudāx- tan gudäz- ‘to liquify’.
```


## [2026-10-17T00:02:08.095Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4246,4250p NYB_vol2_glossary.txt; grep -n -i 'digest' CHEUNG.txt NYB_vol2_glossary.txt HRN.txt | head; grep -n -i 'vitaxti\\|vītaxti\\|vitaxtay\\|vitäxti' BRT.txt | head"
}
```


### [2026-10-17T00:02:08.564Z] TOOL RESULT

```
vitávane (inscr. Prth) [wt’wny] shooting range HajA:1 = Prs tigrähy (g.v.); FrP 25 = vindak-vitav (g. v.). - < vi + *tavana- from tav-, v. s. v. tuvām; as to the ending -é v.s. v. Site.
vitāxtak [wt'htk'] molten 101?9. 1022. 108%, from
vitaxtan vitdc- trans. to melt: bé witäcet 10177, — Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- and wd’c- (MHC), Ghilain 50; MPrs. wdc- (8), Verbum 169; Paz. vadáxtan vadāž- (SGV); NP gudāx- tan gudäz- ‘to liquify’.
vitir [wtyly] thoroughfare F: 6.
vitirän pt. of vitartan, passing away: hac gētē ~ bavend 12071.
CHEUNG.txt:7015:*AVESTAN: YAv. gah- ‘to gorge’ || (+ *ni-) ‘to digest’ || (+ *nis-) ‘to devour’ 
CHEUNG.txt:7020:‘indigestible ?' (Y 28.3), which is phonologically difficult. 
CHEUNG.txt:7963:(m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to 
CHEUNG.txt:7972:*IE COGNATES: Gr. В.Вроско “I eat, digest’, Lat. voräre ‘to devour, to eat greedily’, 
CHEUNG.txt:18896:*KHOTANESE: pajs- (pas-) ‘to cook’, pach- (pas-) ‘to be cooked, digested’ || (+ 
CHEUNG.txt:18897:*pari-) LKh. parvach- (parvas-) ‘to ripen’ || (+ *ui-) gvas- ‘to be digested’ = SGS: 
CHEUNG.txt:18906:*NWIR: NP puxtan/paz- ‘to cook; to ripen; (dial.) ‘to digest, defecate’, Bal. patk/pac-
```


## [2026-10-17T00:02:11.564Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7940,7975p CHEUNG.txt; grep -n -i 'guvar\\|gugar\\|vikar\\|vikār' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:12.093Z] TOOL RESULT

```
*IE COGNATES: Hitt. /ku(ua)liya-/ ‘to flow; to run smoothly, be calmed’, OHG 
quellan, Engl. to well 


*REFERENCES: EVP: 51; IIFL II: 533a; Morgenstierne 1942: 266; Abaev, Slovar’ II: 268 f.; Abaev, 
Slovar’ III: 205 f.; EVS: 17b, 52a; Werba 1997: 282; Puhvel IV: 303 ff.; Steblin-Kamenskij 1999: 251 


* garH* *to swallow" 

*AVESTAN: YAv. garð (f. pl.) ‘throats’ (Yt 17.56), YAv. aspo.garom noro.garom 
‘who swallows horses (and) who swallows men’ (Y 9.11).. 6 YAv. "jar- ‘to swallow’ 
(Y Av. "jarois P22), as cited by Bartholomae, AIW: 512, does not exist, on which see 
Jamaspa — Humbach 1971: 45, fn. a. 

*NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ? 
Bal. ugarit/ugar- ‘to chew the cud, swallow, devour, devastate, misspend’. © The 
etymology of Bal. ugarit/ugar- is unclear: Sims-Williams apud Shahbakhsh suggests 
a connection with MP ogar- (BMP wkl /ögär-/) ‘to remove, expel’, but contamina- 
tion with Si. ugaranu ‘to chew the cud’ seems quite likely, as observed by Shah- 
bakhsh. The older Bal. form might have been *ögär- ? 

*NEIR: Pash. yaráy ‘greedy, gluttonous’, ? Pash. yur (m.) ‘goitre’ || (+ *a-) Pash. ayér 
(m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to 
swallow’ (with sec. -r-) || (+ *niZ-) Oss. I. nyqq.yryn/nyqqoyrd, D. niq(q)warun 
/niq(q)ward ‘to swallow’ (contaminated with q.yr/qur throat), Wa. noZ(y)or-/ 
noZ(y)ord-, noZ(y)or-/noZ(y)ord ‘to swallow’ 

*SANSKRIT: gar’ ‘to devour, swallow’ (RV+)  EWAia I: 469 

«PIE *g”erH;- ‘to devour, consume (wholly)? = LIV: 211 f. | Pok.: 474 ff. 

*IE COGNATES: Gr. В.Вроско “I eat, digest’, Lat. voräre ‘to devour, to eat greedily’, 
OCS po-Zréti ‘to eat (of animals), to devour’, Lith. gérti ‘to drink’, etc. 

*REFERENCES: EVP: 26, 51; IIFL II: 533a, 275a; Morgenstierne 1942: 266; Abaev, Slovar’ II: 268 f., 205
```


## [2026-10-17T00:02:16.332Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'verdau' HRN.txt HUB.txt | head; grep -n -i 'schmelz' HRN.txt | head; grep -n -i 'gavāž\\|guvāž\\|guvaz\\|guwäz\\|Spott' HRN.txt HUB.txt | head"
}
```


### [2026-10-17T00:02:16.647Z] TOOL RESULT

```
HUB.txt:5751:guva, und „guhared'^ verdaut* Min. cap. 16, 38, T^guhara"
HUB.txt:8578:= phi. gukos und guvaridan Verdauen' = phi. gukarttan
5319:tegel, ahd. tegal 'Schmelztiegel*, an. diguU 'Tiogcl*.
7744:891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
7746:aw. vUa/ti- 'Schmelzen, Thauen', vUaöina-; phlv.
HUB.txt:3685:Np. guvaza *Schelten' = skr. vivac- 'streitend, Streit'
HUB.txt:6128:surdan H. 100; afsos *Spott* — fisds H. 101; afscLndan *aus-
HUB.txt:6470:afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
HRN.txt:1287:101. efsös 'Spott, Scherz', fisös,
HRN.txt:1288:phlv. afsös 'Spott, Scherz'.
HRN.txt:5860:aw. jlstayamna- (y. 8, 3) Verachtend, vorspottend'
HRN.txt:10892:haftes Dasein wie vaj, guvaze, gnvaMden, Allerdings
```


## [2026-10-17T00:02:19.117Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7740,7752p HRN.txt; echo ---; sed -n 3680,3690p HUB.txt; echo ---; sed -n 5745,5755p HUB.txt; echo; sed -n 8574,8580p HUB.txt; echo ---; sed -n 10885,10895p HRN.txt"
}
```


### [2026-10-17T00:02:19.637Z] TOOL RESULT

```
890. f/e^^Mörtel'.
aw. vlöica- 'Mörtel'; phlv. gaö^ gaöln.
kurd. af/. LW. gac 'Mörtel'.
Die Zusammenstellung mit aw. vlcica^ ist unsicher ').
891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
(Vis und Rrimin, 69 Zeile 1(3; AM. 105 Zeile 1).
aw. vUa/ti- 'Schmelzen, Thauen', vUaöina-; phlv.
v{i)täxian (AV., Bund.), v(i)taö(i)sn,
892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
aw. Vitara- 'Brett, Planke (zur Herstellung eines
Kinderpferchs)' (vd. 14, 14), Rückert, vergl. Spiegel,
Kommentar I, 342 und Geldner KZ. 25, 568 Note 37.
893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
---
Einl. XXVL
1072. Hierzu np. bdj mussitatio magorum' u. s. w. bei
Vullers, alter i^a;? 'Gemurmel, leises Recitiren reli-
gioser Formeln', Noldeke, Tab. p. 353, phi. vac
Gl. and Ind. 228, West, PT. I, Introduction p. 73.
Np. guvaza *Schelten' = skr. vivac- 'streitend, Streit'
(larmend, schreiend, tosend, Wettstreit, Schlacht' bei
Pischel-Geldner, Ved. Stud. I, 37).
1075. Lies Gazophyl. p. 289. Die Form auch bei Vullers.
Np. valana also aus Halan- = idg. *volonos? Lat.
volnus = idg. *volenos KZ. 32, 386.
---
p. 57, Z. 4 V. u.; guzurg gross Shk. 247, Min. Gl. 95
neben paz. vazurgi *Gr5sse' Shk. 272, np. buzurg, Oflfenbar
sind die gr-Formen fiir die jiingeren, neupersischen zu
halten.
Nicht in Betracht kommen hier guvdh *Zeuge', guvcll
Zeugniss' = phi. gukasth Shk. 247, Min. Gl. 95, np. guvah,
guva, und „guhared'^ verdaut* Min. cap. 16, 38, T^guhara"
= phi. gukarak 'digesting Shk. 246, np. guvara, da gu^
schon im Pehlevi vorliegt ohne irgend eine Nebenform^)
mit V, Paz. guzurg setzt ein alteres *vuzurg — fhi*vuzurJc
(arm. vzurk) voraus, das aus *vazurk durch Assimilation

in takarapet *Mundschenk* (5. Jhd.). Also konnte rey 'Hass*
(Horn 17) doch auf ap. araika- *feindlich' zuriickgehen,
wenn dies nicht arika- (s. oben p. 6) zu lesen ist. Der
Uebergang von k zn g = v findet sich nur in guvdh Zeuge'
= phi. gukos und guvaridan Verdauen' = phi. gukarttan
(vgl. § 53).
Geschwunden ist k in padospdn Tab. 151 — 152 = arm,
---
162. lyatvdyitan 'antworten*, Pvsies, patväcet {^eiZ, patvnzed),
Men.
aw. \/^vaC' -\r paiti, paityaoyta 'antworten'; ai. V^vac-
-\-prati,
Vergl. np. vaj (oben No. 1072).
np. heväz (oder vielmehr peivaz) 'Zustimmung, Ant-
wort*, heoä^lden fristen auch nur ein solches zweifel-
haftes Dasein wie vaj, guvaze, gnvaMden, Allerdings
führen FR und FJ für die Bedeutung 'Zustimmung
folgenden Vers BehrämT's^) an (Metrum: Muteqtirib):
he ummed^ reftem bedergah-t ö
```


## [2026-10-17T00:02:25.784Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vitarəm\\|vitarem\\|vitaram\\|vltarom\\|vitardm\\|vltarem\\|vitar^m' BRT.txt | head; grep -n -i 'vlspa\\|vispa-' BRT.txt | head -5; grep -n -i 'vlspa\\.paO\\|vispapad\\|vispaö\\|vispa6\\|vis\\.pa' BRT.txt | head; grep -n -i 'vlpra\\|viOra\\|vlOra\\|vi&ra\\|vipra' BRT.txt | head"
}
```


### [2026-10-17T00:02:26.324Z] TOOL RESULT

```
2455:l'S.S  (wo  awÄ<f' als  LSf.),  Y.9-28';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  visal  güuS  buyät  Y.6'o.2i.; '  2.  S..2J.3.  52-3.  FrD.  P,  Yt.  /j.  i3;  ~  ioa fri>ä  .  .  buyata  ahmya  nmlne  Yt.  /J.  147  ; IS6f.^  Y.26.^,  62.3*;  —  fraddiäi  ahe nmanahe  ..  vlspaya  alaond  stöis  Y.52.4; 4.5',  Vr. ».  13*;  —  imim  >7oqm  .  .yänim .  .  jaioyemi  .  .  dn'atütam  aiiiAas?  tanvS ". .  Gesundheit  dieses  (meines)  Leibes"  Y. 5.19;  — yaiä  ratSm  akurö  valdil  . ,  aya qsayä(scL)Y.ji.2;  —  afäi  aAmäi  var^nai.. nidätitn  ahm  . .  iAaeiili  (sd.) . .  "und  in  diesen (ünsem)  Glauben  .  ."  Y.4ff-3;  —  aitiAa daenayä  mqs  vaca  dd^anaAe  Y.  j?.  3 1 ;  — frä  KTjri»ie(sd.)aA£(XS{.alsinstr.)da^(^a ..  aAura  ..  Vr.5.3;  —  atcäv3  mizdtm  (sd.) anhat  aAyä  magahyH  y.  S3T>  —  H  *"''^ (sd.)  maiy  aniya/ay  vasiy  astiy  kartam avJ*  ahiyäyä  dipiyä  ttaiy  nipislam  (sd.) ".  .  in  dieser  (meiner)  Inschrift  (hier)  . ." Bh,  4-  S;  —  yS  ach-a  mazdayasnalh-a  .  . ". .  wer  hier  unter  den  Af.  .  ."  V-S-z; —  aAyil  '^wil  J^rff  rtr»z3nil  .  .  pairl.ja-
3998:•  j.  aiwyaaha-  f.  'Lesen,  Studium'  uzw.  1  durch,  dass  ihm  (dem  Schüler)  kein  Be- der  heiligen  Texte:  ka  asti  ihy^a  »la/^!  scheid  wird?"  N.  ij; —  vtspagsu  "partnti saonB  {%A.)f  ..  aya  doEna  disyut  .  .  yB  .vlspaiiü  *'fi*i  ästryeiti  "jedes  Mal,  wenn %ritarymaEm  ratüm  'kam  nHit  aiwyästi  \  Einwendung  erhoben  und  kein  Bescheid Mit  gä'hs  srävaydti  "..  er  könnte  durch  gegeben  wird,  versündigt  er  sich"  N.7_J. seine  schlechte  Religion  (einen)  dazu  ver-  j  P"--  a/rälgda^Hnih.  —  ■>  s.  No.  3, 4.  —  i)  Ausg. leiten,  daas  er  wihrend  der  drei  (dafür!  l%^fZtl,^tl  ^- *)'m^^''Sr5ti~  ^'  "^ bestimmten)  Frühlinge'*  dem  Studium  (der  .""''  '',"^''  __  .  /'  ,™  '  .  ,  , ■    -       _       ,    .  ."    ,^..     •  ].  a-fra'oxiayant-  Adj.  (fem.  yan/i-)
4146:der  Gesammtheit  der  stofflich  Seienden, 'die  Welt,  Menschheil'  (s.  I  la);  yasnyasla vahmyaüa  'nuhe  astvaite  Yt-fS*.  15;  Y.  65. 1%  Yt  y.146,  V.  2.24,  P.J5  (wo  arikeY\ *Vyt  J<?;  —  apam  napiss  tä  äps  .  .  -t3uhe astvaite . .  vl6ax/aiti  Yt.  Ä  34 ;  —  syai)^  na . . yä  'ühus  astvä  vfifzyäü  V.  75.  i;  Yt.  y. 12;  —  avi  °hüm  astvantpta  a-fpm  (sd.) *e}mS  jaiihintuY.  2.22*;  —  kascit  'ufiSus astfats  "ein  jeglicher  Mensch"  F.  2()", V.Äioo;  7.50,  70.19,  'Äaa.  P.y,  .<3;  — anys  kascit  "nhSu^  ash'atö  N.  63;  — yeiftyö  .  .  vlsp^mili  -uuÄe''  astvaite  Yt  10. 5.  aa)  mit  vispa-  Adj.  'die  gesammte
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4208:•  j.  ana,  p.  anä  Praen. 'über  — hin';  i)  mit Akk.,  a)  'über—  hin':  yat  vlspanqm  yuxta- nqm  az>m  fratsmsm  "^anjaymi  (sd.)  "</ *car>tqm  yqm  daryyqm  ". .  über  die  lange Rennbahn  hin"  Yt5.so'>.  b)  'entlang, längs';  "a  til  vai'Am{&i..)  ayii  °a  bititn  °a 'iritXm  V.  5.  5.         c)  'auf',  auf  die  Frage
13891:pa  duig^oiinlk.  und   'dab:  —  Pü. :  lässt  aus,  Su.r  vipralärakak
```


## [2026-10-17T00:02:30.555Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -i '.\\{80\\}auseinander.\\{80\\}' BRT.txt | grep -i 'v[iïlí]' | head -8; grep -n -o '.\\{60\\}seitwärts.\\{80\\}' BRT.txt | head -5; grep -n -o '.\\{60\\}ringsum.\\{60\\}' BRT.txt | head -5"
}
```


### [2026-10-17T00:02:30.923Z] TOOL RESULT

```
10498:  Yt.Ä3i. (näml.  niii-rahe)  grantahe'^l.i0.i>ii,^%-,\      mit  i'f  Kaus.   'auseinander,  tiberwallen —  varäsahe  ..  grantahe  Yt. /^ig.  lassen':  Jt3  zrayo  viyzr
12070:  tarö  (,  tan),  g.  tar»  (,  p.  tare^) 1)  Adv.;  a)  'seitwärts':  *aor3ca  paräca 'rasia  "hinunter  und  fort  und  seitwärts" F. ja;  —  sfä
9203: und  Menschen  be- einem  Metallstiick  sollst  du  einen  ringsum  wegen  sich  frei  einher"  Yt  io.  112-,  — gehenden  Fu
14426: ein  stark  gehender Wind  von  Westen  her  den  Luftraum ringsum  (von  Dünsten)  freifegt"  V.  j. 42",         a)  mit  3^
15580: t. •  j.  ■•■pairi.gä.-vacah-"  Adj.   'der   seine Worte  ringsum  singt,  d.  L  ettönen,  erklingen lässt':    kaomS  /räim
30293:  gJu/  'iaukö  urvamm  Y.  j  •  j.  hu-pairi'spl-  Adj.  "ringsum  wohl  ge- JÖ'.  4,  20".  4,  S.  2. 14;  FrW.  Ö.  1;  —
```


## [2026-10-17T00:02:33.079Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12066,12072p BRT.txt | cut -c1-1500"
}
```


### [2026-10-17T00:02:33.582Z] TOOL RESULT

```
4i:är  ape  t  n  1  a  r  (fartär  F)  iavF,'.    —    >)  Hds,
ia^ärä  mai/i;   5.  aber  Pü.
•  j.  tarv-manab-  n.  sva.  iars.matay-.  °n3 F./Ä».
Pä.  (l.St.):  fakUluia,  (3.  St.):  j^aH;  offenbar Restart.  —   ■)  Zum  3  e.  tarAU-  No.  I.
•  j.  tarö  (,  tan),  g.  tar»  (,  p.  tare^) 1)  Adv.;  a)  'seitwärts':  *aor3ca  paräca 'rasia  "hinunter  und  fort  und  seitwärts" F. ja;  —  sfänö  .  .  ^'rJ'^  spasänH  ivin- ^ftU  (sd.)  V.  jj.  a8.  b)  'unvermerkt, Iränlich':  yextca  alfa  yä  iaine  ..  'rö . tlixibm  paraiti  'rs  apsm'a  ui'varqmla\ "uid  wenn  das  Mädchen  heimlich  sich  die
taro.pifrwa-  643
'/ravazaite  mihrS  . .  'rS  anzaki  savaki  YL 70,133)1331,  aa)  bildlich:  Hfli/afljtrfy^j- raihyanqm  (sd.)  *urvisyeiti  *V;?*'  dar^ya data    .  .    zara^uürake  P.  ^6.  ß)    zeit-
```


## [2026-10-17T00:02:37.531Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^vi-\\|^visa-\\|^vispa-\\|^vi- \\|^visa\\b\\|^vispa' KNT_full.txt | head; grep -n 'visa-\\|vispa-' KNT_full.txt | head -20"
}
```


### [2026-10-17T00:02:37.991Z] TOOL RESULT

```
2858:vi-mardaliy, Skt. mrdáti. 
5443:vispa-, Skt. visva-. 
7957:vispa-, from pIE *yik-yo-; ji-va- ‘living’, unless 
12767:vi-, pref. w. verbs and nouns. 
24895:vi- + kan- ‘dig apart, destroy’: viyakanam 1st 
25820:vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, 
25961:vi- + tar- ‘go across’, caus. ‘put across’: viya- 
26923:vi- + nab- caus. ‘injure, harm’: vindPayatiy 
28292:vi- + mard- ‘destroy’: vimardatiy (830, $213) 
28946:vi- prefix ‘away, apart’: Av. vi, Skt. vi; with 
5381:zana-, Skt. jána-; m OP vispa-cana-, paru- 
5441:pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; 
5443:vispa-, Skt. visva-. 
7956:yd-va-, to relative ya-; har-uva-; visa- and (Med.) 
7957:vispa-, from pIE *yik-yo-; ji-va- ‘living’, unless 
8333:paru-zana- ‘having many men’; vispa-zana- ‘hav- 
28971:visa- ‘all’, because of the АКК. translation (Wb. 
29036:visa- adj. ‘all’: OP (Med.) vispa-, Av. vispa-, 
29040:vispa-.  visahyü gsm. DSa 5; DS} 6. visam nsn. 
29047:ía-da-a-hu-i$ and (with Med. vispa-) Akk. u~- 
29048:1$-pt-da-a-'-1; visa- ‘all’ + dahyu- ‘country, prov- 
29052:vispa- adj. ‘all’: Median (49.11, $90) for OP 
29053:visa-, q.v. See also wtspazana-. vispā absn. 
29060:from the OP form *visadana-: Med. vispa- ‘all’ +
```


## [2026-10-17T00:02:41.231Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5438,5444p KNT_full.txt; sed -n 28946,28955p KNT_full.txt; sed -n 29036,29062p KNT_full.txt; awk 'BEGIN{RS=\"\\f\"} {n++} n>1 && index($0,\"visa- adj.\") {print \"leaf\",n-1; exit}' KNT_full.txt"
}
```


### [2026-10-17T00:02:41.648Z] TOOL RESULT

```
Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, 
Lt. equos. 

pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; 
OP nspa- (with Med. sp) in vispaeana-; Av. 
vispa-, Skt. visva-. 

vi- prefix ‘away, apart’: Av. vi, Skt. vi; with 
verbal roots kan-, jan-, iar-, nof-, mard-, and 
perhaps in sbb. Vidarna-, Vivdna-, Vistaspa-, and 
adj. Viyaxna-. 


við- sb. ‘house, royal house, royal clan, court’ 
(JNES 4232): Av. vis- ‘Herrenhaus’, Skt. vié- 
‘house, dwelling’, Gk. ofxos ‘house’, Lt. vicus 
‘village’ (§22, $87, $114, §142). Decl., §188.1V, 
visa- adj. ‘all’: OP (Med.) vispa-, Av. vispa-, 
Skt. víóva-, pAr. *yiSya- (800) for pIE *uiko- 
(OCS vist ‘all’) after -ya- in (Skt.) sdrva- (see OP 
haruva-; 5150). See also visadahyu-, and cf. viba-, 
vispa-.  visahyü gsm. DSa 5; DS} 6. visam nsn. 
DSj 4°; DSI 5. visam asn. DNa 49; DSf 21; DSi 
4°; XPa 16; XPb 25f; XPf 42; XPh 44. 


visadahyu- adj. ‘of or for all countries or 
provinces’ ($161.Па): borrowed in Elam. mz-25- 
ía-da-a-hu-i$ and (with Med. vispa-) Akk. u~- 
1$-pt-da-a-'-1; visa- ‘all’ + dahyu- ‘country, prov- 
ince’. visadahyum asm. (§53, 418811) XPa 12. 


vispa- adj. ‘all’: Median (49.11, $90) for OP 
visa-, q.v. See also wtspazana-. vispā absn. 
A%Sa 5°; Ada 4, Аас 4 (iispa db, $55.1); 
A?Ha 6°. 


vispazana- adj. ‘containing all (kinds of) men’ 
($101.09): borrowed in Elam. mi-iš-ša-da-na, 
from the OP form *visadana-: Med. vispa- ‘all’ + 
Med. zana- ‘man, human being’ ($9.11, §88, $90). 
uspazananim gpf. DNa 10Ї; DSe 9f; DZc 5.
```


## [2026-10-17T00:02:49.007Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==140' SOD_pages.txt | head -120"
}
```


### [2026-10-17T00:02:49.479Z] TOOL RESULT

```
  Svfc                                                                                                                         74


         o5cz OwSynt) ©<*ava-darzaya ?; Khwar.                1883 'wYr-1 S                    jji^^(^^X^ <o^o jy
           *uSaziy =^{35^?-, 'w^yz-
         Od?)strangle                                               oyar ?
                                                                    gulping
                                         fljUg
         TSP 2.284; STSC 50, 152 Add.
                                                                   MHC 26 n 36; S W, gar- "to gulp"
 1872 >wfc C                                                  1884 NvYr-2 B                       o>/\*j*q>/Sj
      ufc, ofc ©f. pp. =»Svptyy                                     oxar OwY*r-) ©impf. w7r =»Jwxr-
      sleeping                                                      OcOleave, 0<?)abandon
                                                                    TSP 2.97, 7.82 n p212; SCE; BSTBL, Dhy. 42;
      C2, 48V9                                                        >wVwr, TSP 2.465
 1873 *>wfs- C                                      ijX^ly-
                                                              1885 SvYst-     S                          &&&<&*»                J
         ufs, ofs ©Av. <hufsa- ©impf. w^fs =^*>wJ3s
           w'fs-                                                    oxast ©pt. st. =»*wyz-, >wxst-
         (ro)sleep                                                 (ro)go down
         Benv. JA 1955, 305; C2 gloss. 60 R8                       MDii; MDiii
 1874 >wft-      C                                            1886 'wYwr =» 'wyywr
         uft, o[3d ©pt. st. ^wPt-                             1887 >wYwrt =» \vfwrt-
         0<?)slccp
                                                              1888 >wyvz-     S =» »wYlyz-
         STi 12-6 apud. Sund. AoFiii 70, trans, prct.
                                                              1889 jwyz =* 'wyz-, Jwxz-
           ywfd>r-                                            1890 >wYz- B,S,C                     ^^W>
 1875 »wywk      B                                ojU^cuo          oxaz Owy'z-) ©<*ava-haiz ©impf. w*Yz
         oxak Owx-) ©a/**/iav +a£ ©ob. -yfc =»}wxt-2                 ^Jwyst-, *wxz-, Jwxst-
         pestle249                                                 0o)go down, 0<?)dcsccnd
         SCE                                                       GMS 55, 342; Gcrsh. BSOAS 14.88; VJ; TSP; SCE
                                                                                                                bjA~ I Jj>
 1876 'wy'in1 B                        ^li****^.                     182; BSTBL*, Frag. Lcn.; MDii; MDiii; STi 61.16
      uyam ? ©<*^/n; Parth. ^bg^m ^wyW                        1891 SvYz'mndty M
      torture
                                                                   oxazamandc -^wxz'mnty
         TSP 6.161 n p206; Szemerenyi. ZDMG      1951, 219         descending, fall
1877 NvyW B                  j^O' £j^ «jI=»' jjj ^U-               GMS 55, 164, 1100
     uyam, wiyam ©<*vi-£ama- =*Yw>m> wy*m                     1892 >wh M
     foreign country                                               uh, 5h ©exclamation mark
     Sogdica. 60.14; GMS 214
1878 'wY'nz S                                                      BBB b55; GMS 10                   i^j^y     t5
                                                                                                                             cl«l
                                               J^jj^k °V                                             ■-^j=iV        <;Uj i
     oxan'z ©inf. =*}wyz-, 'wxnz                              1893 -wj>k M                   UII.J
     going down, descend(//j^)                                                                                                »o aj
                                                                     o\ oh1=*wjk-k
                                                                   uzak
     MDii A-14, 29                                                 letter of alphabet
1879 »wY'r-          B =» >wyr-                                    GMS 472, 991
1880 »wYJwrt- S                                     o*j> ^j
                                                              1894 >wjy5(S)- M
     oxurt Owywrt) ©pt. st.                                        ozya5 0)<*ava-zgad        ©impf. wVYS        ^wzy5-,
     (ro)abandon                                                     w'c'y-S-
     Hen. BSOAS 11, 74n4; TSP 2.219                oijijaS
                                                                   (fc)dismount
1881 >wy>yz- S                                                     Hen. JRAS 1944, 143.18; GMS 376, 263n 1; AVS
                                                                     78
     oxez Owyyz-) ©<*av£-;taizaya- ©impf.
       w^yz; trans, v. ^'wyz-, }wxz-, w^'yz-,                 1895 HvJYnd- M                                          ox^U
       w'yyz-                                                      ozyand ©inf. -yy
     Go)bring down                                                 (fo)dismount, dismounting
     GMS 543; VJ 38e; MDii; AVS 136, 80                            BBB 508; GMS 342 n 1, 600 n 1; Sogdica. 32.28 n
1882 'wy'z-      B =* >wyz-, >wxz-
```


## [2026-10-17T00:02:53.221Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==139' SOD_pages.txt | grep -n -i -B3 -A4 'tomorrow\\|lonely\\|alone\\|morning'; grep -n -i 'tomorrow' SOD.txt | head; grep -n -i 'lonely\\|alone,\\|solitary' SOD.txt | head"
}
```


### [2026-10-17T00:02:53.675Z] TOOL RESULT

```
24-                                                                       ucak ? ©Av. vitara-, vicak <*vitrak <*vitardk
25-      synagogue
26-      Sund. AoFiii 1975, 67.54                                           =»wc*q, wt's'k
27:                                                                       morning, tomorrow
28-1851 >w}zy C                             ■'nw'z'k                      Sund.
29-                                                                         V17 AoFviii 1981, 204, 29V3 p205 n389; C2, 48
30-     awazc ©pi. -f; ob. pi. -ty
31-     crowd, assembly
19837:morning,  tomorrow 
25292:morning,  tomorrow 
25838:tomorrow 
75159:tomorrow 
77375:tomorrow 
94698:tomorrow     1862,  2673,  2755,  9943, 
23696:lonely 
83152:solitary 
91389:lonely     2427 
93817:solitary     11076
```


## [2026-10-17T00:02:56.624Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==139' SOD_pages.txt | sed -n 15,30p; grep -n -B8 -A3 '^lonely $' SOD.txt | head -30; grep -n '2427' SOD.txt | head -3"
}
```


### [2026-10-17T00:02:56.962Z] TOOL RESULT

```
1848 Vnkw        S(MD) => 'wn'kw
                                                                  1861 'wc' C                                          b*T
1849 Sv-'wt'qcyq           C                             j*3^
     aw-otakcik           ©pi. -f                                      oca ?, otsa   Owcy) ^wts'r, 'wrc ?, 'wrts^, >ws\
      fellow-countryman                                                 there
      S W, C2, 87R 13 & n p!63
                                                                       GMS 71, 358; STii 3.70, 29; Frag. Len. 13V1
1850 'w'zqty C                               (^     ^l^u^T        1862 'we'q C                                  k><£~<>
     awaz-kate
                                                                       ucak ? ©Av. vitara-, vicak <*vitrak <*vitardk
      synagogue
      Sund. AoFiii 1975, 67.54                                           =»wc*q, wt's'k
                                                                       morning, tomorrow
1851 >w}zy C                             ■'nw'z'k                      Sund.
                                                                         V17 AoFviii 1981, 204, 29V3 p205 n389; C2, 48
     awazc ©pi. -f; ob. pi. -ty
23688-
23689-2426  'ywtr   M 
23690-ew-tar   **ywtr 
23691-onciof  several) 
23692-Sogdica.  54,10;  GMS  1318 
23693-
23694-2427  'yw  wsy   M 
23695-ew-  wise  ?   ®<*wi0rai  A  v.  oiOra 
23696:lonely 
23697-
23698-Sogdica.  25.9;  GMS  299 
23699-
23694:2427  'yw  wsy   M 
74771:61R24,  27;  BSTii  892.24,  903.12,  9092427, 
91389:lonely     2427
```


## [2026-10-17T00:03:04.359Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/554.jpg 2>/dev/null; pdftoppm -f 554 -l 554 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg554 && echo ok"
}
```


### [2026-10-17T00:03:05.832Z] TOOL RESULT

```
site/pages/554.jpg
ok
```


## [2026-10-17T00:03:10.384Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg554.png"
}
```


### [2026-10-17T00:03:10.856Z] TOOL RESULT

```

```


## [2026-10-17T00:03:10.851Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:03:16.681Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg554.png data/verification/sources/refs/ocr/BOOK/554.png; for p in 1813 1835; do timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; echo =======; done",
 "timeout": 600000
}
```


### [2026-10-17T00:03:24.377Z] TOOL RESULT

```
Exit code 1
(no exact page map; using offset -1205 -> pdf page 608; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1813.png
REF: BQT:1813  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 608  OCR-lang: fas

-۱۸۱۱- کزدایکان
رساننده و کزند وآزا ر کنان هم‌آمده‌است۱ ۰ وعلاج باشد بفتح دویم هم آمده است.
گزاید ۴ « بفتح اول بر وزن سرایده گزرد *سینم‌اول وفتح ثانی۱۱وسکون
مشتق از کزیدن ۴ است یعنی گزد و کزید را و دال بی‌نقطه » بمعنی علاج وچاره باشد چه
رساند خواه به نیش وخواه بزبان: #۰ ناکزرد بمعتی لاعلاج باشد.
گزایش ۴ نم اول پروژن کشایش, گزردن ۱۴ بن‌ارل وفتم‌دال‌ایی۰۱۹
ی خور ولایق باشد * - و بقتح اولرهم بمعنی علاج کردن وچاره نمودن باشد .
این ممنی و هم بسن <وبی اک غرو کاد گزر نامه ۱۴ کناب تعبیر خواب را
ی و بکس اود پیز گنها - کوبند چه کزر بدمنی خواب هم آمده است۹۴.
و بمعنی پیچش هم هت ۷ . چه دزر به‌عنی خواب هم
گزر - بفتح اول و ثابی و سکون رای گزره - بنتح اول وئالك و ضم قالی,
قرشت » زردك راگوبند ومعرب آن‌جزراست۸ | کیاهی است که آن را سرزبره خوانند ۱۵
- وم اول وکسر نانی» مخفف کزیر است که گزشایگان نش کزی‌باشد به مقدار
چاره وعلاج باشد ‎٩‏ - و بضم اول وفتح ثالی . يك ارش و نیم آدمی که متوی الغلقه باشد.
خرجین شبانرا کوبند ؛ و بمعنی دویم که چاره | و بعضی کوبند ازيك ارش ولیم چیزی کمتراست»
۱- از :کزای (کزاییدن )+ ان ( پسوند فاعلی ):
حقاکه شکر زهر شود تلخ وگزایان گرنام خلافش بنگاری بشکر بر .
عنصری بلخی « رشیدی » .
۲ -ر4 :کزاییدن . ۴ - از «کزاییدن» . ۴ - از :کزای(کزاییدن)
دش ( ام مصدر) . 8 -_رك :کزاش. ‎٩‏ - رك4 :کزاش .
۷ - ظ.مصحف «کرایش»(ه.م.) ۸ - سانسکر بت 88187 محتملااز پارسی ناشی‌شده.
زرا دریکی از مآخذ طبی متأخرآمده . رك : -89751۳11 ‎ 0:880411081,‏ بو
( 89 - 1879 ,ع۲اط 3616۲۶ ۰ 51 ) ۰ 64 2۳004860 ,ط۲۲۶ ۷۷۵۲۵۲ شوه
و 69017 با 398017 در لهجهٌ قره قلیق ( روسیه ) نیز باغلب احتمال از همین ۱
لغت فارسی است. ر4: مقالهٌ ۳۲۷6 .87 .14 درمعرفی ,۸/168865 .77 ۳۳8۳1 9
7 21030 22720) درمحلهٌ ۸912116 0۶ [707۵ 173۳۷8۵7۵ 3
8 , 3-4 37۵۰ .۷۵۱۰10 ,51068 درپعتو 822۵72 و درکیلکی ‏ 7
7 (زرد4) .۰ ‎٩‏ -رك :کزیر . ۰ مصدرمرخم ازه کزردن» نت
(همم.) ۹۱ - صجیح بکر دوم است . ۴۳ از :گزر (<- کزبر)
ادن (پوند مصدری). ۴ رد : گزارنامه ۳ کزارش نامه .
۴ رك : ح۱۵صفحة۰۱۸۰۸ ۵ رك : سرزیره. کزر
‎۹٩‏ لغة بعتی گز(واحد مقیای) شاهی (ملکی) < کزملك (م.) . رالد :کز, شایگان.
درادن - بفتح اول وششم * کزیدن ؛ آفت رسالیدن » سیب رساندن,صدمهزدن:
کیست کش وصل تو ندارد سود کیست کش فرقت تو نکزاید .
دقیقی طوسی « فرهنگه فظام»:
- زهر ربختن .

(eval):1: ====== not found
```


## [2026-10-17T00:03:28.221Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:1813 --pdf-page 610 2>&1 | head -12; echo ====; timeout 300 python3 tools/ref_page.py BQT:1835 2>&1 | head -60",
 "timeout": 600000
}
```


### [2026-10-17T00:03:28.833Z] TOOL RESULT

```
Exit code 1
REF: BQT:1813  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 608  OCR-lang: fas

-۱۸۱۱- کزدایکان
رساننده و کزند وآزا ر کنان هم‌آمده‌است۱ ۰ وعلاج باشد بفتح دویم هم آمده است.
گزاید ۴ « بفتح اول بر وزن سرایده گزرد *سینم‌اول وفتح ثانی۱۱وسکون
مشتق از کزیدن ۴ است یعنی گزد و کزید را و دال بی‌نقطه » بمعنی علاج وچاره باشد چه
رساند خواه به نیش وخواه بزبان: #۰ ناکزرد بمعتی لاعلاج باشد.
گزایش ۴ نم اول پروژن کشایش, گزردن ۱۴ بن‌ارل وفتم‌دال‌ایی۰۱۹
ی خور ولایق باشد * - و بقتح اولرهم بمعنی علاج کردن وچاره نمودن باشد .
این ممنی و هم بسن <وبی اک غرو کاد گزر نامه ۱۴ کناب تعبیر خواب را
ی و بکس اود پیز گنها - کوبند چه کزر بدمنی خواب هم آمده است۹۴.
و بمعنی پیچش هم هت ۷ . چه دزر به‌عنی خواب هم
(eval):1: === not found
```


## [2026-10-17T00:03:31.551Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; for w in 'گواژه' 'گواژیدن' 'گداختن' 'گوارد' 'گواریدن'; do echo \"## $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print \"pdf\",NR; c++} c>=4{exit}' BQT_v3_pages.txt; done"
}
```


### [2026-10-17T00:03:32.784Z] TOOL RESULT

```
## گواژه
## گواژیدن
## گداختن
## گوارد
pdf 227
pdf 644
## گواریدن
```


## [2026-10-17T00:03:35.082Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} NR==644' BQT_v3_pages.txt | grep -n -B3 -A6 'گوارد'; grep -c . BQT_v3_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==644' BQT_v3_pages.txt | head -3"
}
```


### [2026-10-17T00:03:35.614Z] TOOL RESULT

```
75-
76-‎227+ ) iS) 88۷2 : ‏کوازء ح جواز س غباز  خبازه , در اوستا 82۷828 از‎ A
77-ER ‏(ستور) ران « فاب ۱ ص ۱۸ ح‎ WF ‏لغة بمعنی‎ IT ) ‏راندن‎ (
78:‏(پسود‎ Oa, ‏گواردی + گواریدی - نم اول وقتح دال ؛ از: کوار (هدم.) + دن‎ »
79-
80-‏مصتری )۰ پهلوی ‎Vikar cSt. gukdritan‏ ( تفییردادن ) « هوبشمان ص ۹۵ ‎٩‏ ؛
81-موافق مزاج بودن , قابل ‎doles‏ رفتن , خوب هم شدن : « چیزهاء خلم و بی‌مزه ... بدان‌پخته
82:شود و مزء و رنگه و بوی گیردکه مردمان ‎LIT‏ بتواشد خوردن ‏ ومرایغان را بگوارد .» «ناصر
83-خرو بلشی . جام‌العکنتین ص ۶۲۳۱ ۰
84-
37437
[pdf page 644]
۱۸6۷
```


## [2026-10-17T00:03:41.582Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; for w in 'کواژ' 'واژه -' 'گداخت' 'کداخت' 'کدازه' 'گدازه'; do echo \"## $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print \"pdf\",NR; c++} c>=5{exit}' BQT_v3_pages.txt; done"
}
```


### [2026-10-17T00:03:42.470Z] TOOL RESULT

```
## کواژ
pdf 510
## واژه -
## گداخت
pdf 88
pdf 568
pdf 574
## کداخت
pdf 63
pdf 100
pdf 101
pdf 122
pdf 326
## کدازه
## گدازه
```


## [2026-10-17T00:03:45.176Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; for n in 568 574; do echo \"### $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v3_pages.txt | head -4; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v3_pages.txt | grep -n -A4 'گداخت'; done; awk 'BEGIN{RS=\"\\f\"} NR==510' BQT_v3_pages.txt | grep -n -A3 'کواژ'"
}
```


### [2026-10-17T00:03:45.981Z] TOOL RESULT

```
### 568
[pdf page 568]
۱۷۷۱
‎OPIVP‏ ه با زای ‎abs‏ دار بر وزن
ایدن,زهرة کار راکویند. چیزی با مد
52:‏برآن مثال که سیم گداخته درگاه.
53-«فرخی ‎Joe‏ ص۳46٩‏ .۰
54-
55-‏۷ - باين ععنی در عربی «جدی؟ بفتح اول وسکون دوم‌ولیز
56-نم اول ‎ce‏ دوم وسوم مشدد ‎ate)‏ «متتهی‌الارت» .
### 574
[pdf page 574]
‎oo, ۱۷۷۷‏ کدیه

‏کیپای کوچك وخردرا کوبند وآن پوست‌پارهای
66:گداختی- بضماول وفتح پنجم = کدازیدن, اوستا- ‎Vitacina. lS )vitaxti‏
67-
68-‏پپلوی ‎ge bvitaxtan‏ 4۸۹۱ آب شدن وآب کردن فلز با روغن با جزآنها بوسیلحرارت-
69-آب شدن هر چیز سخت .
70-
14:کواژ * = بنتح اود و سکون ‎Fl‏
15-‏که زای فارسی‌باشد ۰ طعته وسرزش راکوبند.
16-
17-‎Od! rs‏ = بنتح اولبروژن ملازه.بسنی
--
25:‏کواژه © بفتح اول‌وزای فارسی؛ بمعنی
26-‎Aah‏ زدن و سرزش کردن باشد ‎٩‏ - و بمعنی
27-سخر و ‎BY‏ و مزاج خوش طیمی هم هت ‎٩‏ -
28-
--
68:‏9 مصحف «کواژ ‎ »‏ کواژه ‎(pm)‏ ۱ - مسحف «کرازه» ‏ کراز (هم.).
69-
70:‏۴ - ۶ و مرغانگردانیدنگرفتند و خابه وکواژء و آنچه ‎LY‏ روزمپر کان است‌ملواد
71-را از سوخته و برکان روده میکردند . » * تاریخ بیپفی مصحح فیاض ص ۷ > رشیدی صحیح
72-این کلمه را «کوازه » میداند و معرب ‎OT‏ «جوازق» موید این قول است .
73-
```


## [2026-10-17T00:03:50.134Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; awk 'BEGIN{RS=\"\\f\"} NR==510' BQT_v3_pages.txt | sed -n 1,70p"
}
```


### [2026-10-17T00:03:50.646Z] TOOL RESULT

```
[pdf page 510]
۱۷۲۱۷
٩ ‏است‎ Kz se ‏خزفپا پوست‎

lee ‏دان ۳ + با واو پروزن‎ ol
‏وامثال‎ Fy ‏کشان . شخصیرا گوبند که کوسفتد‎
‏آن را بچرالیدن برد و پمربی او را سراج‎
aan
Ss. ‏اول بروزن نماز‎ che ‏کواد‎
‏وآن‌کوزه‌ای باشد سر تنگه و کردن‎ WL,
‏وچوبدستیرا‎ - Paiste ‏کوتاه که مسافران باخود‎
. ۴ ‏نیز گویند که خر وکاو بدان رانند‎

کواژ * = بنتح اود و سکون ‎Fl‏
‏که زای فارسی‌باشد ۰ طعته وسرزش راکوبند.

‎Od! rs‏ = بنتح اولبروژن ملازه.بسنی
اول کواز است که تنکه مسافران باشد" - ‎poe‏
‏اول تخم مرغ نیم پخته را کویند و معرب آن
جوازق است ۷ - و بکسر اول چوبی که‌خروکاو
‎ole‏ رانند ۸ .

‎۰

‏کواژه © بفتح اول‌وزای فارسی؛ بمعنی
‎Aah‏ زدن و سرزش کردن باشد ‎٩‏ - و بمعنی
سخر و ‎BY‏ و مزاج خوش طیمی هم هت ‎٩‏ -

‎AS

‏و مزاح کننده را یز کوبند ‎٩‏ - و بععتی نان
وطمام یم پخته و تخم مرخ لیم برشت هم آمده
است *۱- و با انی مشدد هم‌هست ؛ وباین‌معانی

‎GEL |‏ فارسی 55 کفته‌اند .

‎ce ST‏ اولبروزن قطاس؛ بععنی
صفت ‏ وگونه - وطرز و روش و قاعده و قانون
باشد ‎ah‏

‏کواسمه ‎oT‏ بن اول و فتح میم بر
وزن مناصفه | بمعنی سپل وآسان ‎ath‏ ۰

‎deal‏ ۳" - بر وزن ‎AE‏ بمعنی
‎AST‏ است که گونه و صفت و طرز و روش
باشد .

‏کواسیمه ‎ee oF‏ اول ورابع‌بتحتانی
ردیده و فتح میم ؛ بمعنی کواسمه است که سهل
وآسان باشد ؛ و بمعنی‌آسالی هم گفته‌اند که در
‎Solin‏ دشواری است .

‏کواش *.- منم اول وسکونآخ رکه
شین ‎loaded‏ باشد ۰ بمعنی ‎AS‏ است که صفت
و گوله وطرز وروش باشد ‏

‏۱ - «مخفی‌نماندکه عبارت مصنف... درجمیح‌نخ موجوده بالاتفاق بهمین سیاق‌واقع‌است

‏ذبرمتتبم پوشیده نس ت که خزف درلغت سفال راکوبند » وازقرينة لفظ پوست‌ظاهر است که‌مراد
از خرینکه همین جانور سرطان (است) ... و چون سفال از جنس پوست نمی‌باشد » بهترین آن
پوست خرچنک بودن ‎[alk‏ معنی ندارد , شابد مصذف بسبب قلت اعتنا درین مقام خطا کرده ببا
ناسخین بتحریف این عبارت را آورده الد افاعلم » « چك ص ۹۱۲: ۲ » این قول را هدایت در
انجین آرا « مقدمه در ائتباهات برهان » آورده است . ۴ .ظ . مسحف «گوازه ور »
قس : چوبدار » و رك : گوازء . ۴ مصحف «کراز » (هم) « رشیدی ©

‏۴ - صحیح ‎CNS?‏ (.م.) است ‏ کوازه .

‏9 مصحف «کواژ ‎ »‏ کواژه ‎(pm)‏ ۱ - مسحف «کرازه» ‏ کراز (هم.).

‏۴ - ۶ و مرغانگردانیدنگرفتند و خابه وکواژء و آنچه ‎LY‏ روزمپر کان است‌ملواد
```


## [2026-10-17T00:03:55.707Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; for n in 610 611 628 629 630 631; do echo \"## $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v3_pages.txt | sed -n 2,3p; done"
}
```


### [2026-10-17T00:03:56.727Z] TOOL RESULT

```
## 610
one males

## 611
گز ‎Vo‏ - بنم اول و فتح دالابجد »
یمعنی پسندیده و تخاب کرده‌شده‌باشد سوتفیر
## 628
۱۳۱

## 629
BY ‏بنم اول و فقح‎ - ۱ om
‏و سکون ثالث ؛ ت رکیبی باشد مانند کل فند‎
## 630
NATE

## 631
بیان پانزدهم
```


## [2026-10-17T00:04:02.780Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++} index($0,\"vitaxtan vitdc-\"){print \"leaf\", n-1}' NYB_vol2_glossary.txt; grep -n '^vivāc\\|^vivac\\|^wiwāz\\|vivác\\|^gukār\\|^gukar\\|^vikār' NYB_vol2_glossary.txt | head; command ls incoming/FFD/; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'));print(d['FFD'].get('title') or d['FFD'])\" | head -5"
}
```


### [2026-10-17T00:04:03.269Z] TOOL RESULT

```
leaf 235
FFD_asmaneketab.pdf
FFD_pages.txt
Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
```


## [2026-10-17T00:04:07.081Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"} NR==80 || NR==81' FFD_pages.txt | head -90"
}
```


### [2026-10-17T00:04:07.511Z] TOOL RESULT

```
[pdf page 80]
ماده‌های ماضی و مضارع فارسی دری وی

گفت < فارسی میانه +801 < ایرانی باستان 80-42 *. برای 12 -> آراست. 6۵0 صورت
اصلی ۶باع است» ۳ پیش از 1 به ؟ بدل شده است. 90ع صورت ضعیف ريشهٌ 8200 به
معنی «گفتن» است.

گوی + فارسی میانه 83۷ < ایرانی باستان 8200-2*. برای ۵ > آرای.

گماردن. گماشتن

گمارد < فارسی میانه ۰8070370 (گماشت) در فارسی دری به قیاس با «کاشت».
«کار» به وجود آمده است.

گمار + فارسی میانه ۰801037

گواردن

گوار + فارسی میانه 6۳837 < ایرانی باستان ۷1-127-۵*. برای 2-> آرای. 137 صورت
بالاندةٌ ريشهٌ ۴۵۲ به معنی «کردنْ» است. ۷۷1 پیشوند فُعلی است.

مادهٌ ماضی در فارسی میانه 8083770 بوده که جعلی است. «گوارد» فارسی دری
بازماندة ۹1-137-1۵* ایرانی باستان است. برای 1۵ -> آراست.

گوالیدن (:بالیدن)

گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.

[pdf page 81]
وا فعلهای قارسی دری
دا 2 لشت.
لشت « ایرانی باستان 715-1۵*. برای 1۵ -> آراست. 7:2* صورت اصلی کل* است. 7
َ پیش از ۲ به 5 بدل شده است. ریشهٌ 72* صورت ضعیف ريشةٌ 7۵2* است» به معنی
«لیسیدن).
لیس + ایرانی باستان 1۵12-2*. برای 2 -> آرای. «س» در «لیس» به جای 2 آمده است.
ماندن
ماند < فارسی میانه 13324 < ایرانی باستان ۳30-12:*. برای 1۵ -* آراست. ريشهٌ
به معنی «صبرکردن» است.
مان < فارسی میانه 832 < ایرانی باستان 038-8*. برای 2 آرای.
«ماندن» فارسی دری و 38420 فارسی میانه جانشین دو ريشةٌ ایرانی باستان
شده‌اند» یکی 337 به معنی «صبرکردن» و دیگر 8 ج 0039۵ 930۵ که اسم
است و در فارسی دری «مان» شده» در ایرانی باستان به عنوان مادهٌ جعلی و با معتی
«سکونت کردن» به کار برده شده است.
مانست-
«مانست» مادةٌ ماضی جعلی است. از «مان» < فارسی میانه 830 < ایرانی باستان
42 13302 ماد مضارع جعلی است از 13382. 12372 اسم است به معنی «هیئت
ظاهری».
مُردن :
مُرد < فارسی میانه ۵۶۵ < ایرانی باستان 13-1۵" برای 12 > آراست. 17
صورت ضعیف ريشةٌ 1387 به معنی «مردن» است.
میر < فارسی میانه 3۲۲ < ایرانی باستان 2دیط*. برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.
```


## [2026-10-17T00:04:10.519Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; awk 'BEGIN{RS=\"\\f\"} NR==79' FFD_pages.txt | grep -n -A6 'گداخت'; grep -n 'گواژ' FFD_pages.txt | head -3"
}
```


### [2026-10-17T00:04:10.852Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:04:12.411Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; grep -n 'گداخت\\|گداز' FFD_pages.txt | head; "
}
```


### [2026-10-17T00:04:12.736Z] TOOL RESULT

```
882:به معنی «دویدن». از 12 در فارسی دری «گداختن» و «پرداختن» و «تاختن» هم آمده‌اند
883:ی گداختن و پرداختن و تاختن.
1908:گداختن
1909:گداخت « فارسی میانه ۷14371 < ایرانی باستان ۴۷۹-13۳1۵ برای 18 -> آراست. ۷1
1915:گداز < فارسی میانه 432 < ایرانی باستان -۳۹۷1-130. برای 2 - آرای. 6 به جای 1
```


## [2026-10-17T00:04:14.854Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; sed -n 1900,1920p FFD_pages.txt; awk 'NR<=1908 && /\\[pdf page/ {p=$0} END{}; NR==1908{print p}' FFD_pages.txt"
}
```


### [2026-10-17T00:04:15.228Z] TOOL RESULT

```
گاد < فارسی میانه 834. امروزه «گایید» به جای «گاد» به کار می‌رود. «گایید» مادهٌ
گای < فارسی میانه «(قع.گادن باید از ریشهٌ 83* به معنی «گاییدن» آمده باشد.
به‌شرح زیر
گاد < فارسی میانه 834 < ایرانی باستان 83-12 *. برای 18 - آراست.
گای < فارسی میانه (83 < ایرانی باستان 83-78" 2 برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.
گاشتن
صورت واداری «گشتن» است > گشتن.
گداختن
گداخت « فارسی میانه ۷14371 < ایرانی باستان ۴۷۹-13۳1۵ برای 18 -> آراست. ۷1
[pdf page 76]
ماده‌های ماضی و مضارع فارسی دری سا ۷۱
پیشوند فعلی است. 136 صورت اصلی 135 است» ۴ پیش از + به #بدل شده است. 13
صورت بالاندةٌ ريشةٌ 12۳ به معنی «دویدن» است.

گداز < فارسی میانه 432 < ایرانی باستان -۳۹۷1-130. برای 2 - آرای. 6 به جای 1
آمده است.

گذاردن, گذاشتن

گذارد. گذاشت < فارسی میانه 14374 ۷14331 . ۷14370 از ایرانی باستان
[pdf page 75]
```


## [2026-10-17T00:04:18.255Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:04:18.265Z] TOOL RESULT

```

```


## [2026-10-17T00:04:20.563Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wi",
 "prompt": "Summarize the etymology, meaning, and listed derivatives (especially Indo-Iranian vi-, *wi-tero-, Germanic *wiþra, *wīdaz, Avestan vītarəm, vīspa) verbatim where possible."
}
```


## [2026-10-17T00:04:21.269Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گداختن",
 "prompt": "Give the etymology section verbatim."
}
```


## [2026-10-17T00:04:21.970Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/wide",
 "prompt": "Give the etymology of wide verbatim, especially the PIE source."
}
```


## [2026-10-17T00:04:22.483Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/with",
 "prompt": "Give the etymology of with verbatim, especially the PIE source."
}
```


### [2026-10-17T00:04:22.815Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:04:22.821Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:04:27.934Z] TOOL RESULT

```
# Proto-Indo-European *wí

**Etymology:**
The term is "likely from *dwi-, with *d dropped, or possibly shifted to a *h₁ sound due to the Kortlandt effect."

**Meaning:**
The adverb conveys two senses: (1) "apart" or "asunder," and (2) "away from" or "against."

**Key Derivatives:**

- **Indo-Iranian *wí**: Descended directly, appearing in Sanskrit as विना (vínā, "without, except")

- ***wi-tero-* compounds**: Forms meaning "further apart," yielding Latin vitricus and generating widespread descendants

- **Germanic *wiþrą**: Derived from the adverbial accusative form *wíterom, meaning "toward, against; compared to, among"

- **Avestan vītarəm**: An Indo-Iranian adverbial form meaning "again, further"

- **Proto-Slavic *vъtorъ**: Meaning "second," traced through Balto-Slavic intermediates

- **Latin derivatives**: vitium ("fault, vice") and vitupero ("vituperate") reflect the sense of aberration or deviation

These forms demonstrate the prefix's widespread use across Indo-European languages to express separation, distinction, and directionality.
```


### [2026-10-17T00:04:28.815Z] TOOL RESULT

```
# Etymology Section

[Inherited](/wiki/Appendix:Glossary#inherited "Appendix:Glossary") from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[script needed\] (wtʾhtn' /⁠widāxtan⁠/), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*wi-](/w/index.php?title=Reconstruction:Proto-Iranian/wi-&action=edit&redlink=1 "Reconstruction:Proto-Iranian/wi- (page does not exist)")_ + _[\*taHč-](/w/index.php?title=Reconstruction:Proto-Iranian/taH%C4%8Dati&action=edit&redlink=1 "Reconstruction:Proto-Iranian/taHčati (page does not exist)")_ ("to melt"), from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*teh₂-k-](/wiki/Reconstruction:Proto-Indo-European/teh%E2%82%82- "Reconstruction:Proto-Indo-European/teh₂-")_ ("to melt"), cognate with [Northern Kurdish](https://en.wikipedia.org/wiki/Kurmanji "w:Kurmanji") _[bihatin](/w/index.php?title=bihatin&action=edit&redlink=1 "bihatin (page does not exist)")_, _[bihoştin](/w/index.php?title=biho%C5%9Ftin&action=edit&redlink=1 "bihoştin (page does not exist)")_ ("to melt"). Compare [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek "w:Ancient Greek") _[τήκω](/wiki/%CF%84%CE%AE%CE%BA%CF%89#Ancient_Greek "τήκω")_ (tḗkō, "to melt").
```


## [2026-10-17T00:04:30.332Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گواریدن",
 "prompt": "Give the etymology section verbatim."
}
```


## [2026-10-17T00:04:31.147Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/wide",
 "prompt": "Give the English etymology section verbatim, especially the Proto-Germanic and PIE source."
}
```


## [2026-10-17T00:04:32.077Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/wíćwas",
 "prompt": "Give the etymology section verbatim and the Iranian descendants (Avestan, Old Persian)."
}
```


## [2026-10-17T00:04:32.752Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/with",
 "prompt": "Give the English etymology section verbatim, especially Proto-Germanic *wiþ / *wiþrą and PIE."
}
```


### [2026-10-17T00:04:35.011Z] TOOL RESULT

```
Based on the content provided, there is no etymology section present on this Wiktionary page for گواریدن (govâridan).

The page only contains:
- Alternative forms (listing گواردن as an alternative)
- A Verb section defining it as "alternative form of گواشتن, to digest"

An etymology section is not included in this particular entry.
```


### [2026-10-17T00:04:35.637Z] TOOL RESULT

```
# Etymology Section

From Proto-Indo-European *wisos or *wí. Probably cognate with Proto-Slavic *vьxъ.

# Iranian Descendants

**Avestan:** 𐬬𐬍𐬯𐬞𐬀 (vīspa)

**Old Persian:** 𐎻𐎿 (vi-s /visaʰ/)
```


### [2026-10-17T00:04:37.165Z] TOOL RESULT

```
# English Etymology of "Wide"

From Middle English *wid*, *wyd*, from Old English *wīd* ("wide, vast, broad, long; distant, far"), from Proto-Germanic *\*wīdaz*, from Proto-Indo-European *\*h₁weydʰh₁-* ("to divide, separate").

The PIE root represents "a dissimilated univerbation from *\*dwi-* ('apart, asunder, in two') +‎ *\*dʰeh₁-* ('to do, put, place')."

[WebFetch note: this page's text is 101571 characters long and the answer above covers only characters 0 to 100000; the final 1571 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-17T00:04:37.447Z] TOOL RESULT

```
# English Etymology of "with"

The etymology section states that "with" comes "From [Middle English](https://en.wikipedia.org/wiki/Middle_English "w:Middle English") _[with](#Middle_English)_, from [Old English](https://en.wikipedia.org/wiki/Old_English "w:Old English") _[wiþ](/wiki/wi%C3%BE#Old_English "wiþ")_ ("against, opposite, toward, with"), from [Proto-West Germanic](https://en.wikipedia.org/wiki/Proto-West_Germanic_language "w:Proto-West Germanic language") _[\*wiþi](/wiki/Reconstruction:Proto-West_Germanic/wi%C3%BEi "Reconstruction:Proto-West Germanic/wiþi")_, a shortened form of [Proto-Germanic](https://en.wikipedia.org/wiki/Proto-Germanic_language "w:Proto-Germanic language") _[\*wiþrą](/wiki/Reconstruction:Proto-Germanic/wi%C3%BEr%C4%85 "Reconstruction:Proto-Germanic/wiþrą")_ ("against")."

The document does not provide Proto-Indo-European etymological information for this word.

[WebFetch note: this page's text is 147771 characters long and the answer above covers only characters 0 to 100000; the final 47771 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-17T00:04:43.453Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wi' 'https://en.wiktionary.org/wiki/گداختن' 'https://en.wiktionary.org/wiki/wide' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/wíćwas' 'https://en.wiktionary.org/wiki/with'; do python3 tools/fetch_source.py \"$u\" --note \"page 554, root Wi (part 2): etymology check\" 2>&1 | tail -1; done; cd data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=318 && NR<=323 && /auseinander/ {print \"leaf\",NR; print substr($0,1,200)}' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n 'vitarám\\|vitaram\\|vitardm' incoming/WLD/WLD_Bd1_pages.txt | head -3"
}
```


### [2026-10-17T00:04:45.506Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/523d3d3a216d0132.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d9038d2cdcd7cd2c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a6f462b49d2fcd5a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/50ddad252cf68be0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/096a05ab5e863389.txt
leaf 321
                                                                                                                 ;




KG. II 517) will. Abg. veniti „verkaufen       vino „dos“ usw. gehort zu Wz.
    
leaf 322
                                                                             ,
29805:      Komparativ *uitero-         :   ai. vitaram       „weiter, ferner“, av. vitararn „seitwarts“,
```


## [2026-10-17T00:04:47.999Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29775,29815p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200; grep -n \"^ *ui-\\b\\|^ui- \\|wi-, \\|^uí-\" IEC.txt | head; grep -n -i \"uitero\\|uí-tero\\|uiteros\" IEC.txt | head -3"
}
```


### [2026-10-17T00:04:48.507Z] TOOL RESULT

```
zweiten u ist auch trotz Fay IF. 32, 332 nicht wahrscheinlicher)
   zum St. *uisu-, u isuo- vermutlich auch gr. fiofog, ioog „gleich“ (fiir das andrer-
seits Herleitung aus *uidsuos zu *ueid- „erblicken“ erwogen wurde, s. d.; Ja-
cobsohn Ilerm. 44, 88 ff., der aber nicht iiberzeugend auch Yermittlung mit
Worten fiir ,.Biegung, Kreis“ von der s-Erw. der Wz. *uei- „biegen‘ sucht).                                              £




       Gr.   I'dtog,       fidtog ..eigen
                                                    £
                                                            (eigentlich ,,privatus ',
                                                                                     £
                                                                                         s.   Schulze    BPhW. 1896,
 13 68, KZ. 40, 417,  Brugmann IF. 16, 491 ff.; Bildung wie voopidiog zu voorpi
                                                                                                        ££
 u. dgl.). Yielleicht lat. vitium „Fehler, Gebrechen, Schaden      wenn nach                                 ,


 Schulze KZ. 40, 414 Anm. 1 als *ui-tio-m *Abweichung“ eine Bildung wie          ,
                                                                             ,




                                               nO — ulks-
                                               ul-kmti          r\                                              313

ai.ni-tya-, got. ni-pyis ursprgl. „innen befindlich“ (andere Deutungen ver-
zeichnet Yf. LEWb. 2 s. v,; Gl. 4, 381 ; 6, 348).
      Komparativ *uitero-         :   ai. vitaram       „weiter, ferner“, av. vitararn „seitwarts“,
vitara- „der weitere, spatere‘, oi&ra (d. i. vifrra) Adv. „be9onders, getrennt“,
got.    wipra Adv. in Zs. und Praep. m. Acc. „gegen, wider, gegeniiber, vor“,
anord. vidr Adv. und Praep. m. Dat. Acc. „gegen, wider, mit, bei“ (auch
vid nach Paaren wie nordr        nord), ags. wip Adv. und Praep. m. Gen. Dat.
                                          :



Acc. „gegen, gegeniiber wider, entlang, mit"', wiper- in Zs., ahd. ividar
Adv. „gegen, zuriick, wiederum“, Praep. m. Dat. Acc. „gegen, gegeniiber,
12415:ouis “sheep. I, 167 Skt. ávih, mf. id.; Arm. cf. aw-di, coll. aw-dik, id. (-di as in los-di, etc., sense of ‘creature’); Hiero-Hitt. hawas, id.; Gk. óïs, gp: oion, mf. id.; Lat. ovis, f. gp: ovium, id.; Umb. uvem, f. acc. id.; Olr. ói, Gael. ái, m. id.; OBr. cf. ou-sor ‘shepherd’ (for *ouzor?, cf. Ir. ao- dhaire, id.); OHG ou, au, f. np: awi, i-st. "ewe: OS ewi, f. id.; Go. aw-, awi-, cpds. id.; MHG ouwe, sf. id. OE &ow, m., eowu, f. id.; Du. ooi, Fris. ie, f. id.; LG cf. e-Ilamm 'ewe-lamb' and MHG ost, sn. (Csheepfold', fr. *awist-: Go. awistr, id.); ON ær, f. id.; OCS (and com. S1.) ovíca, dim. type f., id. (fr. *ouika); Srb. cf. ovan, n. ‘ram, teg’; Li. avis, gp: avit, f. ‘sheep’; Latv. avs, gp: avju, f. id. (Cpds. of type *ouil- in Skt. avila, f. ewe Lat. ovile, n. 'sheep- fold”, ovilis, adj. “of sheep’; type *ouin- in Lat. ovinus “of sheep'; Umb. unu, acc. id.; OCS ovínü, ovinij, id.; ovínü, m. ‘fram’; Slovene oven, R ovén, m. id.; Li. avinis, adj. “of sheep’; ávinas, m. ‘fram’; Latv. cf. avens, m. “tam; type *ouit- in OHG ewit, n. ‘flock’; OE eowd, f. ‘fold; flock; type *ouios in Gk. óios *sheep's'; Skt. ávyab, adj. id.
20263:ui-duiios, -duos ‘divided, separate, indivi- . dual, personal" Cf. duid-, duidh- Arm. cf. z-urk, adj. (‘depriveď’, fr. *dis- uiduos); Gk. ídios, dial. widios, adj. ‘personal, private’; Lat. cf. di-viduus, adj. (fdivisible,
```


## [2026-10-17T00:04:52.353Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o '^ui[- ][^‘]\\{0,60\\}‘[^’]*’' IEC.txt | head -20; grep -n -o '.\\{100\\}wide.\\{0,80\\}' IEC.txt | grep -i 'OE wid\\|wid,' | head -3; grep -n '^ALL\\|^12.\\?\\b.*WIDE\\|WIDE' SYN.txt | head -5"
}
```


### [2026-10-17T00:04:52.953Z] TOOL RESULT

```
20263:ui-duiios, -duos ‘divided, separate, indivi- . dual, personal" Cf. duid-, duidh- Arm. cf. z-urk, adj. (‘depriveď’
20433:e, f. “band, thong; ON vió, pl. -jar, ^withy, collar? beside mod. vóóvi, m. ‘muscle’; MHG wit, wid, wide, sf. ‘lash of withies'; LG Wiede, Widde, f. ‘withe’; Blg. vitva, f. (clematis',
22562:12.61 WIDE, BROAD
```


## [2026-10-17T00:04:54.923Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22562,22620p SYN.txt | grep -n -i -A3 'wid' | head -20; grep -n '^13.14 ALL\\|ALL (' SYN.txt | head -3"
}
```


### [2026-10-17T00:04:55.503Z] TOOL RESULT

```
1:12.61 WIDE, BROAD
2-Grk. — xAarts, ebpts Goth. braibs Lith. platus
3-NG tAatts, papdbs ON bretdr, vidr Lett. plats
4-Lat. latus Dan. bred, vid ChSl. Srokit
--
6:Fr. large OE° brad, wid Boh. &Siroky
7:Sp. ancho ME brood, wid Pol. _—szeroki Rum. lat (larg) NE wide, broad Russ. Srokij
8-Ir. lethan, fairsiung Du. _ breed, wijd Skt. prthu-, uru- NIr. — leathan OHG breit, wit Ay. poradu-, padana- W. Ulydan, eang MHG breit, wit
9-Br. ledan NHG breit
10:Words for ‘wide, broad’ rest on the more general notion of ‘spread out, spa- cious, extensive’, and the specialization to extent in a given direction, that is ‘wide’ in distinction from ‘long’ and the opposite of ‘narrow’, is only partial. For all of them may also be used in the more general sense. In the two Gmc. groups represented by NE broad and wide the wider sense is generally stronger in the Second group, and dominant in NHG
11-CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
12:weit, which is no longer used as the oppo- site of eng ‘narrow’, while, conversely, NE wide is the technical term in actual measurement (e.g. siz inches wide by three feet long).
13-1. IE *pjtu-, *pjino-, etc., fr. an ex tension of *pel- (*pela-, *pla-, etc.) De words for ‘spread out, flat’ as Lat. pla- nus ‘flat’, ChSI. polje ‘field’, OB feld ‘field’, ete. Walde-P. 2.99f., 61f. Thurneysen, Gram. 129, 131.
14-polly lethan, Nit. leathan,
15-ork. teal 1 an (beside W. led, Be
--
19:yal (possessiD 3 Byz, NG gapdis, orig. dub. G. Meyer Neugr. Stud. 4.94, connects with NG dial. papéos ‘large (meal-)bag ; jggnword fr. Ital. fardo or its source Amb, farda ‘bundle of goods’. Hatzi- dakis, Mec. 2.29, suggests deriv. fr, digpadts with semantic extension through ‘copious in speech’ > ‘wide’ in gneral. But the actual use of the rare dgpadjs connotes skill, rather than
20-copiousness, of speech.
21-4, Lat. latus (> Rum. lat), prob. fr. ‘ulatos (cf. stlatta, Festus) : ChSl. sttlati ‘spread out’, stelt, postelja ‘bed’. Walde- P, 2.643, Ernout-M. 527f. Walde-H. 1.172,
22:Tt. largo, Fr. large (Rum. larg ‘exten- Sve, spacious’, but under influence of Fr. large Sometimes used for lat ‘wide’, cf. Tiktin s.v.), fr. Lat. largus ‘abundant, ‘pious’, etym.?  Ernout-M. 524. Walde-H. 1.764. REW 4919,
11881:7.27 WALL (Of a Town; Partition Wall)
16900:10.23 FALL (vb.) Goth. driusan
23478:13.14 EVERY; ALL (pl.)
```


## [2026-10-17T00:04:57.603Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22585,22605p SYN.txt | grep -n -i 'vid\\|wid\\|wit' | head; sed -n 23478,23540p SYN.txt | grep -n -i 'visva\\|vispa\\|visa' | head"
}
```


### [2026-10-17T00:04:58.409Z] TOOL RESULT

```
8:ON vidr, OF wid, etc., general Gmc., except Goth., perh. fr. *wi-ito-, epd. of *wi- ‘apart, away’ (Skt. v-, etc.) and pple. of IE *ei- ‘go’ (Skt. 7-, Grk. eft), in form = Skt. vita- (vi-ita-) ‘gone, lack- ing, without’, but with development of ‘gone apart’ to ‘extensive, wide’. Walde- P. 1.108. Falk-Torp 1373.
12:Av. pasana- (with 6 for ¢ fr. paradu-), NPers. pahn: Grk. werdvviy: ‘spread out’, Lat. patére ‘stand open’, pandere ‘spread out, open’. Walde-P. 2.18.
4:telweder, al; alle Av. _vispa-; vispa- (in pl.) NHG jeder (all); alle
```


## [2026-10-17T00:05:02.142Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23478,23600p SYN.txt | grep -n -i -B1 -A2 'visva-\\|*wik' | head -12; grep -n -i 'vispo\\|vispa\\b' BRT.txt | head -3; grep -n 'Komparativ \\*uitero' incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} {n++} index($0,\"Komparativ *uitero\"){print \"leaf\",n; exit}' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-17T00:05:02.652Z] TOOL RESULT

```
ugrep: error: error at position 13
(?mi)visva-\|*wik
             \___empty (sub)expression


4146:der  Gesammtheit  der  stofflich  Seienden, 'die  Welt,  Menschheil'  (s.  I  la);  yasnyasla vahmyaüa  'nuhe  astvaite  Yt-fS*.  15;  Y.  65. 1%  Yt  y.146,  V.  2.24,  P.J5  (wo  arikeY\ *Vyt  J<?;  —  apam  napiss  tä  äps  .  .  -t3uhe astvaite . .  vl6ax/aiti  Yt.  Ä  34 ;  —  syai)^  na . . yä  'ühus  astvä  vfifzyäü  V.  75.  i;  Yt.  y. 12;  —  avi  °hüm  astvantpta  a-fpm  (sd.) *e}mS  jaiihintuY.  2.22*;  —  kascit  'ufiSus astfats  "ein  jeglicher  Mensch"  F.  2()", V.Äioo;  7.50,  70.19,  'Äaa.  P.y,  .<3;  — anys  kascit  "nhSu^  ash'atö  N.  63;  — yeiftyö  .  .  vlsp^mili  -uuÄe''  astvaite  Yt  10. 5.  aa)  mit  vispa-  Adj.  'die  gesammte
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
6165:•  j.  aSa-ä^ra-,  aäö.ÜdTa-'*  Adj.  'der seinen  Ursprung  im  Asa  hat':  vispanam vohunqm  vispanam  'ranam  H.  1. 1 ;  —  vis- palsu  var»hufu  vUpagsuca  -ra^iu  YL  1/.3'*; P.  27'';  -^  äps  ..  urvara  .  .  vitpa  voka 'ra  y.8.^.  a)  vlspa  *voAli  maxdaoäla 'ra  Y.ig.2,  22.3,  YL5.89,  y.88,  H.i.3, 16,  V.ii.i,  2,  10,  Vd.4;  —  i7^»t(  ..  vispa *voAa  mazdatiäta  'ra  Yti.  7.
29805:      Komparativ *uitero-         :   ai. vitaram       „weiter, ferner“, av. vitararn „seitwarts“,
leaf 322
```


## [2026-10-17T00:05:05.771Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i 'VITAX\\|VITAKH\\|WIDAXT\\|WIDAKH\\|GUGAR\\|GUKAR\\|VISPA\\|WITHER\\b' ARY_latin_index_pages.txt | head; grep -n 'گداختن\\|گوارد\\|گوارش' ARY_pages.txt | head -5"
}
```


### [2026-10-17T00:05:06.079Z] TOOL RESULT

```
12944:ZHERU CZECH) So GUKARITAN, PAHLAVI) «5 3h
12945:GERTL, GERIU (LITHUANIAN) gi) GUGARDAN, GUGARIDAN
15112:VAPSVA, VAPSA (LITHUANIAN) gl 53 AVISPA SPANISH) glilyel
13197:گواریدن گواردن / ۴۴۵
```


## [2026-10-17T00:05:07.937Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 12925,12950p ARY_latin_index_pages.txt; awk 'NR<=12944 && /\\[pdf page/ {p=$0} NR==12944{print p}' ARY_latin_index_pages.txt"
}
```


### [2026-10-17T00:05:08.800Z] TOOL RESULT

```
HOLD ENGLISH) iS g-3Si! GUALON (GREEK) gli
EOL, KLIUWE CULLEUS, (LATIN) oS
KOGEL (DUTCH) gabe :(OLD SCANDINAVIAN) AS She!
[pdf page 444]
[
|
| WO | dal Sui S
|
| REFERENCES oe bok GUGA (POLISH)  glang)
t POKORNY: 394-397 GUGLJA RUSSIAN) gay
MACKENZIE: (BALL) 103 GUGA :(LITHUANIAN) vigd
: BUCK: 907-908
YAPE DARE sbi db,
seetloal
S21 Sa s3 i shin Ob) 5203s cal
| PP HS AY OS 235s cal pe
1
|
ZHERU (RUSSIAN) gay) JARAITI HAVESTAN) glen yl
ZHERU CZECH) So GUKARITAN, PAHLAVI) «5 3h
GERTL, GERIU (LITHUANIAN) gi) GUGARDAN, GUGARIDAN
GIRATI (SANSKRIT) ey Sonilee
‘REFERENCES cata KERAY ARMENIAN) o \
POKORNY. ——~~S~S*~*«TASATS BORA, BIBROSKEIN (GREEK) (jhy
BARNHART: . VORARE, VORO (LATIN) oa
(VORACITY) 1211-1212 YVORACE (FRENCH) 41,5
[pdf page 444]
```


## [2026-10-17T00:07:30.863Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-554.py <<'EOF'\nimport json\nW_PIE=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wi\"\nW_GDX=\"https://en.wiktionary.org/wiki/گداختن\"\nW_WIDE=\"https://en.wiktionary.org/wiki/wide\"\nW_WITH=\"https://en.wiktionary.org/wiki/with\"\nW_VISP=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/wíćwas\"\nPOK_Q=\"POK_full.txt l.92991ff. (Page(s) 1175-1176) 'u̯i-1 Meaning: separate from; both, two. Material: Old Indic vi- apart, Avestan vī- apart; abseits ... entgegen (also vīš-: vīs-pat- go away, pass over) ... Avestan vīspaθā ringsum allenthalben ... Old Indic viśva- ... Avestan vīspa-, ap. vispa-; also Old pers. visa- ... comparative *uitero-: Old Indic vitaram, Avestan vītarəm sideways, vītara- the further, later, viθra adv. separately ... Gothic wiþra ... Old English wiþ ... References: WP. I 312 f.'\"\nWLD_C={\"src\":\"WLD\",\"where\":\"Bd. I 312-313 (WLD_Bd1_pages.txt l.29805, leaf 322)\",\"stance\":\"supports\",\"note\":\"'Komparativ *uitero-: ai. vitaram „weiter, ferner“, av. vitarəm „seitwärts“, vitara- „der weitere, spätere“, viθra Adv. „besonders, getrennt“, got. wiþra ... „gegen, wider“, anord. viðr ... ags. wiþ ... „gegen, gegenüber, wider, entlang, mit“' — same material Pokorny copied.\"}\nAHD_C={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wi- (AHD_watkins1985.txt l.1167)\",\"stance\":\"supports\",\"note\":\"'wi-. Apart, in half. 1. Suffixed form *wi-itos in Germanic *widaz in Old English wid, wide (< \\\"far apart\\\"): WIDE. 2. Suffixed (comparative) form *wi-tero- in Germanic *withrō, against ... Old English wither ... with its derivative with: WITH ... [Pok. 1. wi- 1175.]'\"}\nKLN_WITH={\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.267769 s.v. with\",\"stance\":\"supports\",\"note\":\"'with, prep. — ME. with, against; with, fr. OE. wiþ ... rel. to OE. wiþer, against ... Goth. wiþra ... derives fr. I.-E. *wi-t(e)ro-, lit. more apart ... fr. I.-E. base *wi-, against; apart, asunder; two, whence also OI. vi, Avestic vi- asunder, OI. vitarám ... Avestic vītarəm, sideward'.\"}\nKLN_WIDE={\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.267049 s.v. wide\",\"stance\":\"supports\",\"note\":\"'wide, adj. — ME. wide, fr. OE. wīd ... fr. Teut. *wīda-, corresponding to I.-E. *wi-ito-, which is formed fr. I.-E. base *wi-, asunder, and the pp. stem of I.-E. *ei-, to go'.\"}\nSYN_WIDE={\"src\":\"SYN\",\"where\":\"12.61 WIDE, BROAD (SYN.txt ~l.22590)\",\"stance\":\"supports\",\"note\":\"'ON víðr, OE wīd, etc., general Gmc., except Goth., perh. fr. *wi-ito-, cpd. of *wi- apart, away (Skt. vi-, etc.) and pple. of IE *ei- go ... in form = Skt. vīta- (vi-ita-) gone ... with development of gone apart to extensive, wide. Walde-P. 1.108.'\"}\nKNT_VI={\"src\":\"KNT\",\"where\":\"Lexicon s.v. vi- (KNT_full.txt l.28946)\",\"stance\":\"supports\",\"note\":\"'vi- prefix away, apart: Av. vī, Skt. vi; with verbal roots kan-, jan-, tar-, naθ-, mard-'.\"}\nKNT_VISA={\"src\":\"KNT\",\"where\":\"Lexicon p. 208 s.v. visa-, visadahyu-, vispa- (KNT_full.txt l.29036-29062)\",\"stance\":\"supports\",\"note\":\"'visa- adj. all: OP (Med.) vispa-, Av. vīspa-, Skt. víśva-, pAr. *viśva- ... for pIE *uiko- (OCS vĭsĭ all)'; 'visadahyu- adj. of or for all countries or provinces ... (with Med. vispa-) Akk. ú-is-pi-da-a-'-i; visa- all + dahyu- country'; 'vispa- adj. all: Median for OP visa-'.\"}\nBRT_SILENT={\"src\":\"BRT\",\"where\":\"BRT.txt grep vītarəm/vīspa/vīθra\",\"stance\":\"silent\",\"note\":\"Bartholomae's OCR is too corrupt to locate the headwords vī-, vītarəm, vīθra- (grep 'vitar', 'vlspa', 'viOra' gave only scattered citations such as 'vlspanqm', no headword); no usable statement.\"}\nnodes=[]\ndef N(id,lang,words,verdict,der,derfa,srcs,rc,con,**kw):\n    d=dict(id=id,lang=lang,words=words,verdict=verdict,derivation=der,derivation_fa=derfa,sources=srcs,ref_check=rc,consulted=con); d.update(kw); nodes.append(d)\n\nN(1,\"Avestan / Old Persian\",\"wi, vî 2, vi 3\",\"confirmed\",\n \"Avestan vī- and Old Persian vi- 'apart, away; against' are the regular Iranian continuation of Indo-Iranian *wi- (Skt. vi-), from PIE *wi- 'apart, asunder' (probably a reduced *dwi- 'in two'). In Avestan the preverb is written vī- (long ī in the script), in OP vi- (viyatarayāma, vijan-, vikan-). It survives in Middle Persian as wi- and, with the regular change of initial w- before u/i-preverb to g(u)-, as New Persian go-/gu- (gudāxtan, guzaštan, gumān), and in some words as b- (bīmār, bīst).\",\n \"پیشوند اوستایی vī- و پارسی باستان vi- «جدا، دور، به سوی مخالف» بازماندهٔ هندوایرانی *wi- (سنسکریت vi-) و هندواروپایی آغازین *wi- «از هم جدا» است. این پیشوند در فارسی میانه wi- و در فارسی نو با دگرگونی w- آغازین به گ به صورت «گُ-» (گداختن، گذشتن، گمان) و گاه «ب-» (بیمار، بیست) درآمده است. پوکورنی، کنت و ویکی‌واژه همگی این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n [W_PIE],\n [{\"ref\":\"POK:1175\",\"status\":\"supports\",\"note\":POK_Q},\n  {\"ref\":\"KNT:204\",\"status\":\"partial\",\"note\":\"Kent's lexicon entry 'vi- prefix away, apart: Av. vī, Skt. vi' (KNT_full.txt l.28946) supports the claim; the page on which it stands is c. p. 207-208 rather than 204 (leaf not confirmed).\"}],\n [WLD_C, KNT_VI, {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wi-\",\"stance\":\"supports\",\"note\":\"'wi-. Apart, in half ... [Pok. 1. wi- 1175.]'\"}, BRT_SILENT])\n\nN(2,\"Avestan\",\"vi-vačah; vi-taxtî; vi-kar\",\"plausible\",\n \"vi-taxtî: Avestan vītaxti- 'melting, thawing' (Horn no. 891 'aw. vītaxti- Schmelzen, Thauen') = vī- + taxti-, the verbal noun of a root meaning 'run, flow' (Nyberg: vi + Av. tak-) or, per Cheung 2007:376, *taHč- 'to melt' (PIE *teh₂-(k)-, Gk. tḗkō); the prefix analysis is secure, but Nourai's cross-reference to Dhogh (PIE *dʰegʷʰ- 'burn') is not supported by any source. vi-vačah 'to speak against' is not an attested Avestan word: the model is Vedic vivác- 'contest, dispute' (Hübschmann: 'np. guvāža Schelten = skr. vivac- streitend, Streit'), so this is a reconstruction *wi-wāč- from vī- + vač- 'speak'. vi-kar 'to digest' is likewise reconstructed (*wi-kāra-, Abolghasemi) behind MP gugār-; Avestan has no such verb in the meaning 'digest'.\",\n \"اوستایی vītaxti- «گداختن، ذوب شدن» از پیشوند vī- و ستاک taxti- است؛ نیبرگ جزء دوم را از ریشهٔ tak- «دویدن، روان شدن» و چونگ از *taHč- «ذوب شدن» (هم‌ریشه با یونانی tḗkō) می‌داند، و ارجاع نورایی به ریشهٔ Dhogh (سوختن) در هیچ منبعی تأیید نمی‌شود. vi-vačah و vi-kar در متن‌های اوستایی نیامده‌اند و بازسازی‌اند: اولی بر پایهٔ ودایی vivác- «ستیزه» (هوبشمان) و دومی *wi-kāra- (ابوالقاسمی). پس پیشوند vi- درست است ولی صورت‌ها با احتیاط پذیرفتنی‌اند.\",\n [W_GDX],\n [{\"ref\":\"NYB:217\",\"status\":\"supports\",\"note\":\"NYB_vol2_glossary.txt l.4248 (leaf 235; Cheung cites this as 'Nyberg II: 217a'): 'vitāxtan vitāc- trans. to melt ... Caus. of vi + Av. (624 sq.) tak-; MPrth wdxtn, wdc- ... NP gudāxtan gudāz- to liquify'. Supports vi- + Avestan root; does not support Dhogh.\"},\n  {\"ref\":\"FFD:75\",\"status\":\"supports\",\"note\":\"FFD_pages.txt pdf 80 (= p.75) s.v. گواردن: 'گوار < فارسی میانه gugār < ایرانی باستان *vi-kāra-... kār صورت بالاندهٔ ریشهٔ kar به معنی «کردن» است. vi پیشوند فعلی است' — supports vi-kar; for گداختن (pdf 75-76 = pp.70-71) Abolghasemi gives *vi-tāx-ta-, 'tāk صورت بالاندهٔ ریشهٔ tak به معنی «دویدن»'.\"}],\n [{\"src\":\"CHEUNG\",\"where\":\"p. 376 s.v. *taHč (CHEUNG.txt l.24490-24530)\",\"stance\":\"partial\",\"note\":\"'*taHč to melt / MIDDLE PERSIAN: (+ *ui-) MMP wdc- to melt ... BMP wt'htn /widāxtan/ ... NP gudāxtan/gudāz- to smelt, melt ... PIE \\\"enlarged\\\" *teH₂k- to melt = LIV 617 | Pok. 1053' — confirms vi- + melt-root, contradicts the Dhogh link.\"},\n  {\"src\":\"HUB\",\"where\":\"p. 95 note to Horn 1072 (HUB.txt l.3685) and §45 (l.5477)\",\"stance\":\"supports\",\"note\":\"'Np. guvāža Schelten = skr. vivac- streitend, Streit'; '§45 Ap. v = np. g: gudāxtan schmelzen = phl. v(i)tāxtan, zd. vītaxti-'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 891 (HRN.txt l.7744)\",\"stance\":\"supports\",\"note\":\"'891. gudāxten schmelzen, Praes. gudāz-em ... aw. vītaxti- Schmelzen, Thauen, vītaδina-; phlv. v(i)tāxtan'.\"},\n  BRT_SILENT])\n\nN(3,\"Persian\",\"govâžîdan; godâxtan; govârdan\",\"plausible\",\n \"godāxtan 'to melt' < MP widāxtan/widāz- (PHD 'widāxtan, widāz- melt, dissolve | N gudāxtan'), Parthian wdxtn, < OIr. *wi-tāxta- with initial wi- > gu- as in guzaštan < widardan; confirmed (Wiktionary, Cheung, Nyberg, Horn), though the second element is 'run/melt', not Dhogh. govārdan/govāridan 'digest' < MP gugārdan/gugār- (PHD 'gugār(i)dan digest | N guwāridan'); Hübschmann notes the k > g of Pahl. gukārtan, and Mo'in (BQT, s.v. گواردن) and Abolghasemi derive it from *wi-kāra- (vi- + kar- 'do'), whereas Aryanpur (p.445) puts it under PIE *gʷerh₃- 'swallow' (Av. jaraiti, Lat. vorāre) — so the vi- analysis is plausible but not unanimous. govāžīdan/govāže 'taunt, mockery' (Borhan: 'طعنه و سرزنش ... و بمعنی سخره') is a rare word; Hübschmann compares Skt. vivác- 'dispute' (*wi-wāč-), Horn calls it of doubtful existence; plausible. The quoted verse is by Abū Šakūr.\",\n \"«گداختن» از فارسی میانهٔ widāxtan / widāz- و ایرانی باستان *wi-tāxta- است؛ wi- آغازین در فارسی نو مانند «گذشتن» به «گُ» بدل شده و این بخش قطعی است (مکنزی، نیبرگ، چونگ، هرن). «گواردن/گواریدن» از فارسی میانهٔ gugārdan است و معین در حاشیهٔ برهان قاطع و ابوالقاسمی آن را *wi-kāra- (vi- + kar «کردن») می‌دانند، ولی آریان‌پور آن را از ریشهٔ *gʷerh₃- «بلعیدن» می‌گیرد. «گواژه» (طعنه، سرزنش، ریشخند) را هوبشمان با سنسکریت vivác- «ستیزه» سنجیده است. در مجموع پیوند این سه واژه با پیشوند vi- با احتیاط پذیرفتنی است.\",\n [W_GDX],\n [{\"ref\":\"BQT:1813\",\"status\":\"not_found\",\"note\":\"BQT vol.3 pdf 608 = printed 1811 (گزاید، گزر...), pdf 610-611 = گزیده: the cited pages 1813/1835 carry گزیدن/گمیختن of PART 1 of this chart, not this node's words. The node's words are at: گواژ/گواژه pdf 510 (printed ≈1717) 'گواژه — بفتح اول وزای فارسی؛ بمعنی طعنه زدن و سرزنش کردن باشد — و بمعنی سخره ... هم هست'; گداختن pdf 574 (p.1777) 'گداختن ... اوستا vitacina, vitaxti؛ پهلوی vitāxtan'; گواردن pdf 644 (≈p.1851) 'گواردن ... پهلوی gukāritan, vikar (تغییر دادن) هوبشمان ص ۹۵'. These pages support Nourai.\"},\n  {\"ref\":\"BQT:1835\",\"status\":\"not_found\",\"note\":\"Cited page lies in the گز-/گم- range (BQT_v3_pages.txt pdf ~628-631); none of گواژیدن/گداختن/گواردن stands there (see the correct pages in the BQT:1813 note).\"},\n  {\"ref\":\"FFD:75\",\"status\":\"supports\",\"note\":\"FFD p.75 (pdf 80): 'گوار + فارسی میانه gugār < ایرانی باستان *vi-kāra-... vi پیشوند فعلی است'; p.70-71 (pdf 75-76): 'گداخت < فارسی میانه vitāxt < ایرانی باستان *vi-tāx-ta- ... tāk صورت بالاندهٔ ریشهٔ tak به معنی دویدن'.\"}],\n [{\"src\":\"PHD\",\"where\":\"s.v. widāxtan; gugār(i)dan (PHD.txt l.651, l.384)\",\"stance\":\"supports\",\"note\":\"'widāxtan, widāz- [wt'htn', wtc- | (P wd'c-), N gudāxtan, gudāz-] melt, dissolve'; 'gugār(i)dan, gugār- [gwk'l-(y)tn' | N guwār-idan] digest'.\"},\n  {\"src\":\"NYB\",\"where\":\"II p.217 s.v. vitāxtan (NYB_vol2_glossary.txt l.4248)\",\"stance\":\"supports\",\"note\":\"'Caus. of vi + Av. tak- ... NP gudāxtan gudāz- to liquify'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 891 (l.7744); no. 162 note (l.10892)\",\"stance\":\"partial\",\"note\":\"no. 891 'gudāxten schmelzen ... aw. vītaxti-' supports; on guvāže Horn says words like 'vaj, guvāze, guvāžīden fristen auch nur ein ... zweifelhaftes Dasein'.\"},\n  {\"src\":\"HUB\",\"where\":\"pp. 95, 156 (HUB.txt l.3685, 5751, 8578)\",\"stance\":\"supports\",\"note\":\"'Np. guvāza Schelten = skr. vivac-'; 'guvāridan verdauen = phl. gukārttan' with k > g.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p.376 *taHč\",\"stance\":\"supports\",\"note\":\"'NP gudāxtan/gudāz- to smelt, melt' under (+ *ui-) *taHč.\"},\n  {\"src\":\"ARY\",\"where\":\"p.445 (pdf 444) s.v. گواریدن، گواردن (ARY_latin_index_pages.txt l.12925-12950)\",\"stance\":\"contradicts\",\"note\":\"Aryanpur files 'GUKARITAN (PAHLAVI), GUGARDAN, GUGARIDAN' with 'JARAITI (AVESTAN)', 'GIRATI (SANSKRIT)', 'VORARE (LATIN)' — PIE *gʷer- 'swallow', not vi- + kar-.\"}])\n\nN(4,\"Avestan\",\"viš 3, vît\",\"plausible\",\n \"Pokorny 1175 lists beside vī- an s-extended Avestan form vīš- (vīš-pat- 'go away, pass over'), = Skt. viṣu- 'in both directions' (*wis-u-), so Avestan viš- 'apart, away' is real as a preverb/stem element. 'vît' has no match in Pokorny, Walde-Pokorny or Kent; it is probably Nourai's abstraction of the vīt- in vītarəm/vītara- (*wi-tero-), not an independent word.\",\n \"پوکورنی در کنار vī- صورت گسترش‌یافتهٔ اوستایی vīš- را (در vīš-pat- «دور شدن، گذشتن») آورده که با سنسکریت viṣu- «از دو سو» هم‌ریشه است؛ پس viš- درست است. ولی «vît» در هیچ منبعی جداگانه نیامده و گویا نورایی آن را از vītarəm و vītara- جدا کرده است. ادعا با احتیاط پذیرفتنی است.\",\n [W_PIE],\n [{\"ref\":\"POK:1175\",\"status\":\"supports\",\"note\":\"POK_full.txt Page(s) 1175-1176: 'Avestan vī- apart ... (also vīs-: vīs-pat- go away, pass over); Old Indic viṣu- after various sides' — viš- yes, vît not mentioned.\"}],\n [WLD_C, {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wi-\",\"stance\":\"silent\",\"note\":\"lists only *wi-itos and *wi-tero-; no s-form.\"}, BRT_SILENT])\n\nN(5,\"Avestan\",\"viš-patha; viš-pat; vîspa; vîspa-dahyu\",\"plausible\",\n \"Pokorny cites Avestan vīspaθā 'ringsum allenthalben' (all around) and vīs-pat- 'go away' (vīš- + pat- 'fly, go'), and Avestan vīspa- / Skt. viśva- 'all' (Indo-Iranian *wíćwa-), Median vispa-, OP visa- (south-western ś from *ćw). Pokorny explains *wiḱwo- as 'spread apart on all sides' + k-suffix, i.e. from *wi-; Kent derives it from PIE *wiko- (cf. OCS vĭsĭ 'all') and Wiktionary from *wisos or *wí, so the link to *wi- is accepted by some but not certain. 'vîspa-dahyu' 'of all provinces' is really the Old Persian epithet visadahyu- (Xerxes, XPa 12), whose Median form vispa-dahyu- is reflected in Akkadian ú-is-pi-da-a-'-i; it is not an Avestan word.\",\n \"پوکورنی اوستایی vīspaθā «از همه سو» و vīš-pat- «دور شدن» و نیز vīspa- «همه» (سنسکریت viśva-) را زیر همین ریشه آورده است. پیوند vīspa- با *wi- را پوکورنی می‌پذیرد ولی کنت آن را از *wiko- (اسلاوی کهن vĭsĭ «همه») و ویکی‌واژه از *wisos یا *wí می‌داند؛ پس با احتیاط پذیرفتنی است. «vîspa-dahyu» «از آنِ همهٔ سرزمین‌ها» در اصل لقب پارسی باستان visadahyu- در سنگ‌نبشتهٔ خشایارشا و صورت مادی آن vispa-dahyu است و واژهٔ اوستایی نیست.\",\n [W_PIE, W_VISP],\n [{\"ref\":\"POK:1176\",\"status\":\"supports\",\"note\":\"POK_full.txt Page(s) 1175-1176: 'Avestan vīspaθā ringsum allenthalben ... Old Indic viśva- each, every, all, Avestan vīspa-, ap. vispa- ... (*uiḱuo-), out of it also Old pers. visa- with regular southwest development'.\"},\n  {\"ref\":\"KNT:208\",\"status\":\"supports\",\"note\":KNT_VISA[\"note\"]}],\n [WLD_C, KNT_VISA, {\"src\":\"SYN\",\"where\":\"13.14 EVERY; ALL (SYN.txt l.23478ff.)\",\"stance\":\"partial\",\"note\":\"table lists 'Av. vīspa-' for 'all'; Buck treats Skt. viśva-, Av. vīspa- as of uncertain origin.\"}, BRT_SILENT])\n\nN(6,\"Avestan\",\"vîtarem; vîtara; vithra; ôithara\",\"transcription_suspect\",\n \"vītarəm adv. 'sideways' and vītara- 'further, later' are the Avestan comparative *wi-tero- (= Skt. vitarám 'further'), and viθra adv. 'separately, especially' is *wi-tro-; all three are confirmed by Pokorny, Walde-Pokorny and Klein. The glosses 'tomorrow, morning' belong to the Sogdian descendant 'wc'q (Gharib 1862 '<Av. vītara-'), not to Avestan. 'ôithara: lonely' is not an Avestan word: Gharib's entry 2427 for Sogd. 'yw-wšy 'lonely' cites '<*wiθrai, Av. viθra', and the book prints 'ôithara' — Nourai's misprint/misreading of Av. viθra (or a mixing with aēva- 'one'); the extraction is faithful.\",\n \"اوستایی vītarəm «به یک سو» و vītara- «دورتر، بعدی» صورت تفضیلی *wi-tero- (سنسکریت vitarám) و viθra «جداگانه» از *wi-tro- است؛ پوکورنی، والده-پوکورنی و کلاین این‌ها را تأیید می‌کنند. معنای «فردا، بامداد» از واژهٔ سغدی برگرفته شده نه از اوستایی. «ôithara: تنها» واژهٔ اوستایی نیست؛ قریب در مدخل سغدی «تنها» به اوستایی viθra ارجاع داده و کتاب نورایی به خطا «ôithara» چاپ کرده است. این خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n [W_PIE],\n [{\"ref\":\"POK:1176\",\"status\":\"supports\",\"note\":\"'Avestan vītarəm sideways, vītara- the further, later, viθra Adv. particularly, separately' (POK_full.txt Page(s) 1175-1176) — no 'ôithara'.\"},\n  {\"ref\":\"KNT:208\",\"status\":\"not_found\",\"note\":\"Kent p.208 has visa-/vispa- only; Old Persian lexicon has no vītara-/viθra.\"},\n  {\"ref\":\"SOD:73\",\"status\":\"partial\",\"note\":\"SOD_pages.txt leaf 139 (p.73) no. 1862 ''wc'q ucak ? <Av. vitara-, vicak <*vitrak <*vitarak; morning, tomorrow' (source of Nourai's gloss); 'lonely' is no. 2427 (SOD.txt l.23694) ''yw wšy ēw-wiθē? <*wiθrai, Av. viθra; lonely' — so Gharib gives viθra, not 'ôithara'.\"}],\n [WLD_C, KLN_WITH, BRT_SILENT],\n error_in=\"book\", book_prints=\"ôithara\", correct_form=\"viθra\")\n\nN(7,\"Old Persian\",\"visa, vispa\",\"confirmed\",\n \"Old Persian visa- 'all' (DSf, DNa, XPa: visam, visahyā) and its Median doublet vispa- (vispā, vispazana-) continue Indo-Iranian *wíćwa- (Skt. viśva-, Av. vīspa-); OP has the south-western change *ćw > s, Median keeps sp (Kent §90). The words and meaning are certain; their ultimate tie to *wi- is Pokorny's view (see node 5).\",\n \"پارسی باستان visa- «همه» و صورت مادی آن vispa- (در vispazana- «دارای همه گونه مردم») بازماندهٔ هندوایرانی *wíćwa- (سنسکریت viśva-، اوستایی vīspa-) است؛ در پارسی باستان خوشهٔ *ćw به s بدل شده و در مادی sp مانده است. کنت و پوکورنی این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n [W_VISP],\n [{\"ref\":\"KNT:208\",\"status\":\"supports\",\"note\":KNT_VISA[\"note\"]}],\n [KNT_VISA, {\"src\":\"WLD\",\"where\":\"Bd. I 312\",\"stance\":\"supports\",\"note\":\"Walde-Pokorny lists 'ai. viśva-, av. vīspa-, ap. vispa-' and OP visa- under *uiḱuo- from *u̯i- (same text as Pokorny 1176).\"}])\n\nN(8,\"Sogdian\",\"`wc`q; `yw-wšy\",\"plausible\",\n \"Sogdian 'wc'q /ūčak/ 'morning, tomorrow' is explained by Gharib (no. 1862) as <*vitrak <*vitarak, from the Iranian comparative *wi-tara- 'later' (Av. vītara-), with Sogdian -tr- > -č-; Gharib marks the reading with '?', so it is a scholarly proposal, not certainty. ''yw-wšy' 'lonely' (Gharib no. 2427, Manichaean) is ēw- 'one' + a form Gharib traces to *wiθrai (Av. viθra 'separately'), i.e. 'one-apart'; also queried. Both are plausible derivations from *wi-.\",\n \"واژهٔ سغدی 'wc'q (اوچَک) «بامداد، فردا» را قریب از *vitarak و اوستایی vītara- «بعدی، دیرتر» می‌داند، و 'yw-wšy «تنها» را ترکیبی از ēw «یک» و صورتی از *wiθrai (اوستایی viθra «جداگانه») می‌شمارد. قریب هر دو را با نشانهٔ پرسش آورده، پس این پیوندها با احتیاط پذیرفتنی‌اند.\",\n [],\n [{\"ref\":\"SOD:73\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 139 (printed p.73), no. 1862: ''wc'q C / ucak ? <Av. vitara-, vicak <*vitrak <*vitarak / morning, tomorrow'. 'yw-wšy is entry 2427 on another page: ''yw wšy M / ēw- wiθē ? <*wiθrai Av. viθra / lonely'.\"}],\n [{\"src\":\"SOD\",\"where\":\"no. 2427 (SOD.txt l.23694)\",\"stance\":\"supports\",\"note\":\"''yw wšy M ... <*wiθrai A v. viθra / lonely / Sogdica 25.9; GMS 299'.\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 313\",\"stance\":\"partial\",\"note\":\"gives the Avestan bases vītara-, viθra (*uitero-) but no Sogdian.\"}])\n\nN(9,\"Germanic\",\"withro\",\"confirmed\",\n \"Proto-Germanic *wiþra- / *wiþrō 'against' (Goth. wiþra 'against, opposite', ON viðr, OE wiþer, OHG widar) is the comparative *wi-tero- 'more apart' (Grimm's law t > þ). Nourai's gloss 'apart with' is loose: the Germanic meaning is 'against, opposite', from which OE wiþ 'with' developed.\",\n \"نیای ژرمنی *wiþra- «در برابر، علیه» (گوتی wiþra، انگلیسی کهن wiþer) صورت تفضیلی هندواروپایی *wi-tero- «جداتر» است و t طبق قانون گریم به þ بدل شده است. معنای «apart with» که نورایی داده دقیق نیست؛ معنای ژرمنی «در برابر» بوده است. ادعای اصلی درست است.\",\n [W_WITH, W_PIE],\n [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. wi-: '2. Suffixed (comparative) form *wi-tero- in Germanic *withrō, against'.\"},\n  {\"ref\":\"KLN:1748\",\"status\":\"supports\",\"note\":KLN_WITH[\"note\"]+\" (Klein 1971, end of vol. II; page number not verified on leaf).\"}],\n [AHD_C, KLN_WITH, WLD_C])\n\nN(10,\"English\",\"with\",\"confirmed\",\n \"English with < Middle English with < Old English wiþ 'against, opposite, toward', a shortened form (PWGmc *wiþi) of *wiþra-; in Middle English it took over the sense 'in company with' from OE mid, while the old sense survives in withstand, withdraw, withhold.\",\n \"انگلیسی with از انگلیسی میانه with و انگلیسی کهن wiþ «در برابر، رو به» است که کوتاه‌شدهٔ ژرمنی *wiþra- است. در انگلیسی میانه معنای «همراهِ» را از mid گرفت و معنای کهن «در برابر» در withstand و withdraw مانده است. ادعای نورایی درست است.\",\n [W_WITH],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference.\"}],\n [KLN_WITH, AHD_C])\n\nN(11,\"Indo-European\",\"Wi-itos\",\"plausible\",\n \"*wi-itos 'gone apart' = *wi- + *i-tó-, the past participle of *h₁ei- 'go' (= Skt. vīta- 'gone away'), proposed by Watkins (AHD), Klein and Buck (after Walde-Pokorny I 108) as the source of Germanic *wīdaz 'wide'. Wiktionary (following Kroonen) instead derives *wīdaz from *h₁weydʰh₁- 'to separate' (< *dwi- + *dʰeh₁-), which still contains the 'apart' element but not 'go'. The reconstruction is therefore accepted by several handbooks but not by all.\",\n \"*wi-itos «از هم دور رفته» از *wi- و صفت مفعولی *i-tó- از ریشهٔ *h₁ei- «رفتن» (سنسکریت vīta-) ساخته شده و واتکینز، کلاین و باک آن را خاستگاه ژرمنی *wīdaz «پهن، گشاد» دانسته‌اند. ویکی‌واژه به پیروی از کروونن آن را از *h₁weydʰh₁- «جدا کردن» می‌گیرد. پس نظر نورایی با احتیاط پذیرفتنی است.\",\n [W_WIDE],\n [{\"ref\":\"KLN:1743\",\"status\":\"supports\",\"note\":KLN_WIDE[\"note\"]}],\n [AHD_C, KLN_WIDE, SYN_WIDE])\n\nN(12,\"Germanic\",\"wîdaz\",\"plausible\",\n \"Proto-Germanic *wīdaz 'wide, far' (ON víðr, OE wīd, OS wīd, OHG wīt) is certain; *wi-itos > *wīdaz would show contraction of i + i to ī and Verner's-law *-þ- > *-d- after the unaccented syllable. That this is the origin is the AHD/Klein/Buck view; Wiktionary derives it from *h₁weydʰh₁- instead.\",\n \"ژرمنی آغازین *wīdaz «پهن، دور» قطعی است (نوردی کهن víðr، انگلیسی کهن wīd، آلمانی کهن wīt). اگر از *wi-itos باشد، دو i به ī کشیده شده و t طبق قانون ورنر به d بدل شده است؛ این نظر واتکینز و کلاین و باک است ولی ویکی‌واژه آن را از *h₁weydʰh₁- می‌داند. پس با احتیاط پذیرفتنی است.\",\n [W_WIDE],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference.\"}],\n [KLN_WIDE, SYN_WIDE, AHD_C])\n\nN(13,\"English\",\"wide\",\"confirmed\",\n \"English wide < Middle English wid, wyd < Old English wīd 'wide, vast, far', from Proto-Germanic *wīdaz; ME ī became /aɪ/ in the Great Vowel Shift.\",\n \"انگلیسی wide از انگلیسی میانه wid و انگلیسی کهن wīd «پهن، گسترده، دور» و آن از ژرمنی *wīdaz است؛ ī در دگرگونی بزرگ واکه‌ها به /aɪ/ بدل شده است. ادعای نورایی درست است.\",\n [W_WIDE],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference.\"}],\n [KLN_WIDE, SYN_WIDE])\n\nentry={\"entry\":0,\"root\":\"Wi\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *wi- 'apart, asunder; against' (Pokorny 1175-1176 u̯i-1; Watkins wi-; probably < *dwi- 'in two')\",\n \"note\":\"Root, label and gloss are correct (Pokorny 1175 'u̯i-1 separate from; both, two'; WP I 312f.; AHD wi- 'apart, in half'). The derivatives through *wi-tero- (Av. vītarəm, vītara-, viθra; Gmc. *wiþra- > with) and Iranian vi- > NP go- (godāxtan) are standard. Weaker points: Nourai's cross-refs on node 2 (vi-taxtî ☞Dhogh) conflict with Cheung/Nyberg (*taHč 'melt' or tak- 'run'); Avestan 'vi-vačah' and 'vi-kar' are reconstructions; govārdan is put under *gʷer- 'swallow' by Aryanpur; vīspa- 'all' is tied to *wi- by Pokorny but not by Kent/Wiktionary; 'wide' via *wi-itos is AHD/Klein's view, Wiktionary prefers *h₁weydʰh₁-. 'ôithara' (node 6) is a misprint in the book for Av. viθra (Gharib). BQT:1813,1835 on node 3 belong to PART 1's words (گزیدن، گمیختن); the node's words are on BQT pp. ≈1717, 1777, ≈1851. Extraction matches the printed page (checked pdf 554 at 200 dpi, copy at data/verification/sources/refs/ocr/BOOK/554.png).\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *wi- «جدا، از هم، در برابر» (احتمالاً از *dwi- «دوپاره») در پوکورنی (ص ۱۱۷۵-۱۱۷۶)، والده-پوکورنی و واتکینز آمده و ریشه و معنایی که نورایی داده درست است. بازمانده‌های آن پیشوند اوستایی vī- و پارسی باستان vi-، صورت تفضیلی *wi-tero- (اوستایی vītarəm، انگلیسی with) و در فارسی نو پیشوند «گُ-» در گداختن است. چند جزء نمودار سست است: ارجاع گداختن به ریشهٔ «سوختن»، صورت‌های بازسازی‌شدهٔ vi-vačah و vi-kar، پیوند vīspa «همه» و wide با این ریشه، و «ôithara» که خطای چاپی کتاب به جای اوستایی viθra است.\",\n \"sources\":[W_PIE, W_WITH, W_WIDE],\n \"ref_check\":[{\"ref\":\"POK:1175,1176\",\"status\":\"supports\",\"note\":POK_Q}],\n \"consulted\":[WLD_C, AHD_C, KLN_WITH, {\"src\":\"IEC\",\"where\":\"IEC.txt grep '^ui-'\",\"stance\":\"silent\",\"note\":\"Mann has ui-duiios 'divided, separate' (l.20263) but no separate *wi- headword found.\"}, SYN_WIDE],\n \"nodes\":nodes}\nout={\"pdf_page\":554,\"book_page\":524,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[entry]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-554.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-554.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-554.json >/dev/null && python3 tools/verify_check.py 554"
}
```


### [2026-10-17T00:07:31.463Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 5, 'plausible': 7, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'partial': 2, 'not_found': 3, 'not_checked': 3}
books consulted: {'supports': 30, 'silent': 6, 'partial': 4, 'contradicts': 1} | by book: {'WLD': 7, 'AHD': 6, 'KLN': 6, 'BRT': 5, 'SYN': 4, 'KNT': 3, 'CHEUNG': 2, 'HUB': 2, 'HRN': 2, 'PHD': 1, 'NYB': 1, 'ARY': 1, 'SOD': 1}
```


## [2026-10-17T00:07:38.551Z] TOOL CALL #62: SubagentHandback

```json
{
 "message": "Page 554 (book page 524, root Wi, part 2) is verified. `verify_check.py 554` reports 13 of 13 nodes done and no PROBLEM lines.\n\n- **Root Wi:** confirmed (Pokorny 1175-1176; Walde-Pokorny I 312f.; Watkins/AHD).\n- **Node verdicts:** 5 confirmed, 7 plausible, 1 transcription_suspect, 0 disputed.\n\n**transcription_suspect (the book's error, not the extraction's)**\n- Node #6 (Avestan) \"ôithara: lonely\": there is no such Avestan word. Gharib's entry for Sogdian 'yw-wšy \"lonely\" cites Av. viθra, so the book prints \"ôithara\" where it should have viθra.\n\n**Other issues worth knowing (all marked plausible)**\n- Node #2: the \"vi-taxtî ☞Dhogh\" cross-reference goes against Cheung (*taHč \"melt\") and Nyberg (vi + tak- \"run\"). \"vi-vačah\" and \"vi-kar\" are reconstructions, not attested Avestan words.\n- Node #3 (govârdan): Aryanpur derives it from *gʷer- \"swallow\", not from vi- + kar-.\n- Node #3's own references point to the wrong pages. BQT:1813 and 1835 hold Part 1's words (گزیدن، گمیختن). This node's words are on BQT ≈1717 (گواژه), 1777 (گداختن) and ≈1851 (گواردن).\n- Node #5 (vîspa \"all\"): only Pokorny links it to *wi-; Kent and Wiktionary do not. Also, \"vîspa-dahyu\" is the Old Persian/Median visadahyu-, not an Avestan word.\n- Nodes #11 and #12 (wide from *wi-itos): this is the AHD/Klein/Buck view. Wiktionary prefers *h₁weydʰh₁-.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\nFiles are in /home/sfmqrb/git/rishe-private/data/verification:\n- page-554.json\n- sources/refs/ocr/BOOK/554.png (the page image I checked)"
}
```


### [2026-10-17T00:07:38.844Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
