# Verification process log — verify-page-564


## [2026-10-17T00:30:14.306Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 564 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-564.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-564.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-564.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 564` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.356Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:17.481Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:17.505Z] TOOL RESULT

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


## [2026-10-17T00:30:17.955Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-564.txt"
}
```


### [2026-10-17T00:30:17.974Z] TOOL RESULT

```
1	=== PDF page 564 (book page 534) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Yem : restrain, hold together (pair)  (refs POK:505)
4	#1 (parent #0) [Avestan] refs=KLN:1763; BRT:1301; IRN:5 | yemô, yemâ, yîma : twin, also a king. ; yima-xšaetem : brilliant king, title of king Jamshîd. ☞Ksei 2 | NOTE: King Jamshîd had a twin sister who was nicknamed "Yimâ:twin".
5	  #2 (parent #1) [Pahlavi] refs=BQT:587 | yam : king ; yam-šît : shining king
6	    #3 (parent #2) [Persian] refs=BQT:587; MON5:433; TZF:28 | jam «جم» : king ; Jamšîd «جمشید» : "brilliant king", a male name
7	#4 (parent #0) [Avestan] refs=POK:505 | yata, yâta, ya 2 : hold, keep, remember
8	  #5 (parent #4) [Pahlavi] refs=HRN:250 | yât, âyât
9	    #6 (parent #5) [Persian] refs=BQT:2412; SNS:85; TZF:22 | yâd «یاد» : memory ; došyâd «دُشیاد» : backbite ☞Dus
10	#7 (parent #0) [Latin] refs=AHD; POK:505 | geminus : twin (stars)
11	  #8 (parent #7) [English] refs=None | Gemini
12	--- entry 1 ---
13	ROOT Yero -> redirect to Ei
14	--- entry 2 ---
15	ROOT [Indo-European] Yes : to boil  (refs POK:506)
16	#1 (parent #0) [Avestan] refs=POK:506; KLN:1761 | yah 3 : to boil ; yaešyaiti : boils
17	  #2 (parent #1) [Persian] refs=BQT:571 | jastan «جَستن» : to jump up ; jahîdan «جهیدن» : to jump up
18	#3 (parent #0) [Greek] refs=KLN:1761; POK:506 | zein, zeein : to boil ; ek-zema : boiling out (pimples), a skin disease
19	  #4 (parent #3) [French] refs=None | eczema
20	    #5 (parent #4) [Persian] refs=MON:331 | ekzemâ «اکزما» : eczema
21	  #6 (parent #3) [Swedish] refs=AHD:1488 | zeolit : boiling stone, an aluminum silicate mineral
22	    #7 (parent #6) [French] refs=VOP:197 | zeolite
23	      #8 (parent #7) [Persian] refs=VOP:197 | zeolyt «زئولیت» : a mineral
24	    #9 (parent #6) [English] refs=AHD | zeolite
25	#10 (parent #0) [Germanic] refs=AHD | jest : yeast
26	  #11 (parent #10) [English] refs=None | yeast
27	
```


## [2026-10-17T00:30:18.637Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-564.json"
}
```


### [2026-10-17T00:30:18.675Z] TOOL RESULT

```
1	{
2	  "pdf_page": 564,
3	  "book_page": 534,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Yem",
8	        "lang": "Indo-European",
9	        "refs": "POK:505",
10	        "gloss": "restrain, hold together (pair)"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "KLN:1763; BRT:1301; IRN:5",
18	          "words": [
19	            {"translit": "yemô, yemâ, yîma", "gloss": "twin, also a king.", "script": null},
20	            {"translit": "yima-xšaetem", "gloss": "brilliant king, title of king Jamshîd.", "script": null, "see": ["Ksei 2"]}
21	          ],
22	          "note": "King Jamshîd had a twin sister who was nicknamed \"Yimâ:twin\".",
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Pahlavi",
29	          "refs": "BQT:587",
30	          "words": [
31	            {"translit": "yam", "gloss": "king", "script": null},
32	            {"translit": "yam-šît", "gloss": "shining king", "script": null}
33	          ],
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Persian",
41	          "refs": "BQT:587; MON5:433; TZF:28",
42	          "words": [
43	            {"translit": "jam", "gloss": "king", "script": "جم"},
44	            {"translit": "Jamšîd", "gloss": "\"brilliant king\", a male name", "script": "جمشید"}
45	          ],
46	          "note": null,
47	          "quote": {"text": "ای عمارت را چو جمشید - ای ولایت را چو جم - ای شجاعت را چو سهراب - ای سیاست را چو سام", "poet": "Farrokhî"}
48	        },
49	        {
50	          "id": 4,
51	          "parent": 0,
52	          "lang": "Avestan",
53	          "refs": "POK:505",
54	          "words": [
55	            {"translit": "yata, yâta, ya 2", "gloss": "hold, keep, remember", "script": null}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 5,
62	          "parent": 4,
63	          "lang": "Pahlavi",
64	          "refs": "HRN:250",
65	          "words": [
66	            {"translit": "yât, âyât", "gloss": null, "script": null}
67	          ],
68	          "note": null,
69	          "quote": null
70	        },
71	        {
72	          "id": 6,
73	          "parent": 5,
74	          "lang": "Persian",
75	          "refs": "BQT:2412; SNS:85; TZF:22",
76	          "words": [
77	            {"translit": "yâd", "gloss": "memory", "script": "یاد"},
78	            {"translit": "došyâd", "gloss": "backbite", "script": "دُشیاد", "see": ["Dus"]}
79	          ],
80	          "note": null,
81	          "quote": null
82	        },
83	        {
84	          "id": 7,
85	          "parent": 0,
86	          "lang": "Latin",
87	          "refs": "AHD; POK:505",
88	          "words": [
89	            {"translit": "geminus", "gloss": "twin (stars)", "script": null}
90	          ],
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 8,
96	          "parent": 7,
97	          "lang": "English",
98	          "refs": null,
99	          "words": [
100	            {"translit": "Gemini", "gloss": null, "script": null}
101	          ],
102	          "note": null,
103	          "quote": null
104	        }
105	      ]
106	    },
107	    {
108	      "root": {
109	        "name": "Yero",
110	        "redirect": "Ei"
111	      },
112	      "nodes": []
113	    },
114	    {
115	      "root": {
116	        "name": "Yes",
117	        "lang": "Indo-European",
118	        "refs": "POK:506",
119	        "gloss": "to boil"
120	      },
121	      "nodes": [
122	        {
123	          "id": 1,
124	          "parent": 0,
125	          "lang": "Avestan",
126	          "refs": "POK:506; KLN:1761",
127	          "words": [
128	            {"translit": "yah 3", "gloss": "to boil", "script": null},
129	            {"translit": "yaešyaiti", "gloss": "boils", "script": null}
130	          ],
131	          "note": null,
132	          "quote": null
133	        },
134	        {
135	          "id": 2,
136	          "parent": 1,
137	          "lang": "Persian",
138	          "refs": "BQT:571",
139	          "words": [
140	            {"translit": "jastan", "gloss": "to jump up", "script": "جَستن"},
141	            {"translit": "jahîdan", "gloss": "to jump up", "script": "جهیدن"}
142	          ],
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 3,
148	          "parent": 0,
149	          "lang": "Greek",
150	          "refs": "KLN:1761; POK:506",
151	          "words": [
152	            {"translit": "zein, zeein", "gloss": "to boil", "script": null},
153	            {"translit": "ek-zema", "gloss": "boiling out (pimples), a skin disease", "script": null}
154	          ],
155	          "note": null,
156	          "quote": null
157	        },
158	        {
159	          "id": 4,
160	          "parent": 3,
161	          "lang": "French",
162	          "refs": null,
163	          "words": [
164	            {"translit": "eczema", "gloss": null, "script": null}
165	          ],
166	          "note": null,
167	          "quote": null
168	        },
169	        {
170	          "id": 5,
171	          "parent": 4,
172	          "lang": "Persian",
173	          "refs": "MON:331",
174	          "words": [
175	            {"translit": "ekzemâ", "gloss": "eczema", "script": "اکزما"}
176	          ],
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 6,
182	          "parent": 3,
183	          "lang": "Swedish",
184	          "refs": "AHD:1488",
185	          "words": [
186	            {"translit": "zeolit", "gloss": "boiling stone, an aluminum silicate mineral", "script": null}
187	          ],
188	          "note": null,
189	          "quote": null
190	        },
191	        {
192	          "id": 7,
193	          "parent": 6,
194	          "lang": "French",
195	          "refs": "VOP:197",
196	          "words": [
197	            {"translit": "zeolite", "gloss": null, "script": null}
198	          ],
199	          "note": null,
200	          "quote": null
201	        },
202	        {
203	          "id": 8,
204	          "parent": 7,
205	          "lang": "Persian",
206	          "refs": "VOP:197",
207	          "words": [
208	            {"translit": "zeolyt", "gloss": "a mineral", "script": "زئولیت"}
209	          ],
210	          "note": null,
211	          "quote": null
212	        },
213	        {
214	          "id": 9,
215	          "parent": 6,
216	          "lang": "English",
217	          "refs": "AHD",
218	          "words": [
219	            {"translit": "zeolite", "gloss": null, "script": null}
220	          ],
221	          "note": null,
222	          "quote": null
223	        },
224	        {
225	          "id": 10,
226	          "parent": 0,
227	          "lang": "Germanic",
228	          "refs": "AHD",
229	          "words": [
230	            {"translit": "jest", "gloss": "yeast", "script": null}
231	          ],
232	          "note": null,
233	          "quote": null
234	        },
235	        {
236	          "id": 11,
237	          "parent": 10,
238	          "lang": "English",
239	          "refs": null,
240	          "words": [
241	            {"translit": "yeast", "gloss": null, "script": null}
242	          ],
243	          "note": null,
244	          "quote": null
245	        }
246	      ]
247	    }
248	  ]
249	}
250	
```


## [2026-10-17T00:30:22.811Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; command ls data/verification/sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BRT','IRN','BQT','MON','MON5','TZF','HRN','SNS','AHD','VOP','WLD','PHD','NYB','HUB','ARY','CHEUNG','SKT','WEB','FSD','IEC','SYN']:\n  v=d.get(k); print(k, v and {x:v.get(x) for x in ['kind','local_file','page_offset','lookup_hint']})\n\""
}
```


### [2026-10-17T00:30:23.470Z] TOOL RESULT

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
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
BRT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
IRN {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt'], 'page_offset': '222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.', 'lookup_hint': "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'kind': 'website+archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
MON5 None
TZF {'kind': 'website', 'local_file': None, 'page_offset': None, 'lookup_hint': 'Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).'}
HRN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
SNS {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt'], 'page_offset': '242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image', 'lookup_hint': "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping."}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
VOP {'kind': 'none', 'local_file': None, 'page_offset': None, 'lookup_hint': "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه\u200cشناختی واژه\u200cهای دخیل اروپایی, ketabnak 132354)."}
WLD {'kind': 'archive_djvu', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
PHD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HUB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
ARY {'kind': 'local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
CHEUNG None
SKT {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
WEB {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
FSD {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
IEC {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SYN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
```


## [2026-10-17T00:30:33.697Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-56*.json page-55*.json 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('page-558.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-17T00:30:34.043Z] TOOL RESULT

```
page-550.json
page-551.json
page-552.json
page-553.json
page-554.json
page-555.json
page-556.json
page-557.json
page-558.json
page-55.json
page-56.json
{
 "entry": 0,
 "root": "Xac 1",
 "verdict": "plausible",
 "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
 "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
 "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca|kāś-|kāçat'",
   "stance": "silent",
   "note": "no Pokorny entry for Skt. kāca- or kāś-."
  },
  {
   "src": "WLD",
   "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'",
   "stance": "silent",
   "note": "no hit."
  },
  {
   "src": "AHD",
   "where": "AHD_watkins1985.txt",
   "stance": "silent",
   "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Sanskrit",
   "words": "kâca",
   "verdict": "confirmed",
   "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and its sense 'glass' are secure.",
   "derivation_fa": "سنسکریت kāca- به معنای «شیشه، بلور، کوارتز» در سنسکریت کلاسیک به‌خوبی گواهی شده و در پالی kāca و هندی kā̃c (کانچ) و بنگالی kāc بازمانده است. باک آن را با تردید به ریشهٔ khac- «درخشیدن» می‌پیوندد و ویکی‌واژه آن را وامی از نورستانی می‌داند. معنای «مروارید» را معین در حاشیهٔ برهان قاطع به نقل از فرهنگ مونیر-ویلیامز آورده است (مهرهٔ شیشه‌ای). وجود واژه و معنای «شیشه» درست است.",
   "sources": [
    "https://en.wiktionary.org/wiki/काच"
   ],
   "ref_check": [
    {
     "ref": "SYN:620",
     "status": "supports",
     "note": "SYN p.620 GLASS table: 'Skt. kāca-'; para 7 'Skt. kāca- : khac- shine through (?)'."
    },
    {
     "ref": "BQT:1556",
     "status": "supports",
     "note": "BQT vol 3 p.1556 (pdf 349; vision file ocr/BQT/1556.vision.txt), footnote 9 to کاچ: 'قس: سانسکریت kâcá (شیشه، آبگینه، مروارید) «ویلیامز ۲:۲۶۸»'. Mo'in gives the Sanskrit word with these meanings."
    }
   ],
   "consulted": [
    {
     "src": "POK",
     "where": "POK_full.txt grep 'kāca'",
     "stance": "silent",
     "note": "not in Pokorny."
    },
    {
     "src": "WLD",
     "where": "WLD Bd1/Bd2 grep 'kāca'",
     "stance": "silent",
     "note": "not in Walde-Pokorny."
    },
    {
     "src": "SYN",
     "where": "p.620 §9.74",
     "stance": "supports",
     "note": "'Skt. kāca-' as the Sanskrit word for 'glass'."
    }
   ]
  },
  {
   "id": 2,
   "lang": "Persian",
   "words": "kâč; kâčî",
   "verdict": "plausible",
   "derivation": "NP kāč 'glass, ground glass' is a lexicographers' word. Jahangiri, quoted by Mo'in at BQT 1556, has 'کاچ آبگینه را گویند', and Borhan glosses it 'شیشهٔ صلایه کرده' (ground glass rubbed on pottery). Mo'in only compares it with Skt. kāca (قس), and Wiktionary treats the variant kāš 'glass' as 'likely borrowed from an Indo-Aryan language, probably Hindustani kā̃c, ultimately from Sanskrit kāca'. So kāč is a loan from Indic (with Indic c > Persian č), not an inherited word. kāčī 'thin glazed tile' (Jahangiri: 'brick or clay vessel on which glass has been poured') is equated by Mo'in with kāšī (Farhang: 'کاشی: کاچی، آجر لعاب‌دار'), and Wiktionary says kāšī is 'related to kāš glass'. The more usual explanation derives kāšī 'tile' from the city of Kāšān (Arabicised qāšānī; Mo'in's note at BQT 1568, after Qazvini). The book itself puts کاشی in parentheses beside kāčī, so the kāčī/kā
```


## [2026-10-17T00:30:43.285Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A40 'lemma: yem-' POK_full.txt | head -60; echo ====; grep -n -A40 'lemma: yes-' POK_full.txt | head -50"
}
```


### [2026-10-17T00:30:43.657Z] TOOL RESULT

```
Exit code 1
(eval):1: === not found
```


## [2026-10-17T00:30:47.194Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma: .*em-\\|lemma: .*es-' POK_full.txt | grep -i '^[0-9]*:.*lemma: [ij̯y]' | head; grep -n \"Page(s): 50[56]\" POK_full.txt | head"
}
```


### [2026-10-17T00:30:47.508Z] TOOL RESULT

```
52808:Root / lemma: Icem- {*k''ehum-) 
92561:Root / lemma: yes-8 {* haues-) 
92788:Root / lemma: yes-6{*hyes-) 
40778:Page(s): 506 
41218:Page(s): 505 
41277:Page(s): 505-506 
41338:Page(s): 506 
41388:Page(s): 506-507
```


## [2026-10-17T00:30:49.647Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41220,41345p POK_full.txt"
}
```


### [2026-10-17T00:30:50.221Z] TOOL RESULT

```
Root I \emma:jen9ter-, reduced case JenQtr-i/ptr-) 

Meaning: husband's brother's wife 

Comments: 

Root I \emma:jenater-, reduced case Jenatr-i/ptr-): husband's brother's wife = Root/ 

lemma: gen-1, gena-, gne- gnd-\ "to bear' suffixed in -/erformant. 

Material: 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 



labialized laryngeal PIE h™- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 

Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 

Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 

Old Indie yatar-6s. (pronunciation the strong case + vocalism of the weak case); 

Note: 

labialized laryngeal h2"a- > ya- Old Indie 

Phrygian Akk. lavarspa; 

Note: 

labialized laryngeal h2"a- > 0ya- Proto Phrygian > ia Phrygian 

gr. Evarrip " husband's brother's wife ' (Ionian Psilose), Hom. zwait^zc,, -spojv (ei- 
verbalized metr. lengthening for £v-), inschr. (klein Old Saxon-gr.) svarpi; 

Note: 

labialized laryngeal hre- > 0e- Greek = hre- > 0e- Hittite 

Truncated ( *ianiter) Armenian ner, more properly ner. Gen. niri^ the wives of brothers or 
the wives of the same husband ' (to the basic form supposition by HiJbschmann Arm. Gr. I 
478; Bugge IF. 1, 445, 449, Meillet BSL. 30, CR. 90, in the end Cuny Recherches 66 f.); 

Latin janitnces (extension from */an/ter aiter Fem. of noun agents in -/ic-) " the wives of 
brothers ' (/derives from *ia niter); 

Old Lithuanian *jente, -ers6s. {gente, ze/7/e through hybridization with ^e/7//5 'kinsman, 
relative', ze/7/a5 "son-in-law'), Latvian letere, /eta/'aan6 Curon\an Jen fere 6s.; 

Old Church Slavic j^i^/zy (ending after svekry), russ. -Church Slavic ya//yds., serb.Jetrva 
ds. 

References: WP. I 207 f., WH. I 668, Trautmann 107 f., Schwyzer Gr. Gr. I 568. 
Page(s): 505-506 

Root / \emma:jes- 
Meaning: to foam, boil 
Material: 

Note: 



labialized laryngeal hre- > 0e-, h3"o- > hu-, h2™a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old Indie *yasati, yasyat/" bubbles, boils; struggles ', yayastu^ shall scald '; with a- ' exert 
oneself {a-yas-ta-^ arouses, instigates, strains, exhausts, grows tired, languishes ', a-yas- 
aya//' strains, fatigues, afflicts'), pra-yasta-^ boiling, bubbling ', Intens. i-yas-yate^ grows 
tired, dies away, disappears ', redupl. yesati {*Je-js-) ' flows, bubbles ', Avestan yaesye/t/" 
boils (intr.)'; 
Note: 
labialized laryngeal hre- > yei-, ye- Avestan, h2"a- > ya- Old Indie 

gr. ^£U) (= yasati) "cook, boil, simmer, seethe, boil (intr.)', ^tooz, ^egtoc;, ^sapa and ^spa 
" decoction, extract acquired by boiling', ^6r| to snavw tou ij£Aito(; ("scum, froth, foam') 
Hes.; 

Maybe alb. {*Je-) ziej, zjej^ cook, boil, simmer, seethe ', in -/r7-formant like {*^ta\}o) ^spa " 
decoction ' : alb. {*zesm-) zemeroj' make angry', zemerim^ anger', zemer^ heart '. 

Note: 

labialized laryngeal hre- > Proto Greek ye- > ge- > Old Greek ze-, hs^o- > Proto Greek yo- 
> go- > Old Greek zo-, h2"a- > Proto Greek ya- > ga- > Old Greek za- 

gallo-rom.„/es/a"scum, froth, foam' (v. Wartburg), cymr. iasi., PI. iasau^ boiling, foam, 
bubbles, cooking '; Old Irish essru. (older n., from *Jestu) "waterfall'; bret. p'o/ "ferment, 
seethe' perhaps abstracted from gdeiryeasi' {*upo-ies-lo)\ (common Celtic lllyrian -si- > - 
II-) 

Note: 

labialized laryngeal hre- > Proto Celtic ye-. Old Celtic ie-, ha^o- > Proto Celtic yo-. Old 
Celtic io-, h2"a- > Proto Celtic ya-. Old Celtic ia- 

Old High German yes5/7 "ferment, seethe, foam ' = Swedish Dialectal esa{as) "ferment, 
seethe', Norwegian sese, Swedish Dialectal asa{*jesian) ds., Norwegian Dialectal asa 
{*jasan, preterit ds) "flare up, foam, ferment, seethe, roar, storm, dash', esja {*jasjan) 
"ferment, seethe'. Old Norse 0sa {*JdsJan) " stir in violent movement ', compare Norwegian 
Dialectal " the roaring, restlessness in animals and people ', Old Norse yips//", Qeu. Jastarru. 



(at first from *estuz, *estauz, olderyes-) and Jastrn. (at first from *estra) "yeast', Old 
English ^/e5/(engl. yeast) "scum, froth, foam, slobber, yeast'. Middle Low German gest 
"yeast'. Middle High German yes/, gestm. "scum, froth, foam'. Modern High German Gest 
and G/scht^ scum, froth, foam, yeast'; 

Tocharian A yas- "simmer, seethe, boil'. 

References: WP. I 208. O'Rahilly Eriu 13, 144 f. 
Page(s): 506 

Root / lemmai^e/'- 

Meaning: to set out for; to strive 

Material:
```


## [2026-10-17T00:30:52.657Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41160,41219p POK_full.txt; grep -n 'lemma:\\s*jem\\|lemma: jem\\|emma:jem' POK_full.txt"
}
```


### [2026-10-17T00:30:53.149Z] TOOL RESULT

```
ayasata, participle Avestan yata- "hold, stop', ya/a- "assigned allotment, possession ' (to a 
compare the heavy root form Old \v\(i\c yamitavai, Bartholomae IF. 11, 141 f.); Old Indie 
yama-hm., Avestan ydma-m. "twin'; Old Indie GN Vama-h't\N\n, hermaphrodite ' = 
Avestan Y/md; 
Note: 
labialized laryngeal hre- > yei-, yi- Avestan, h2™a- > ya- Old Indie 

Latin geminus " born at the same time, twin-born, twin ' probably g- is attributed to the 
root gem-^ grasp, press together ' (above S. 368 f.); 

Note: 

labialized laryngeal hre- > je- Proto lllyrian > ge- Latin, lllyrian (an lllyrian substrate 
because Latin would have produced je- > ie-) 

Middle Irish emonm., emu/nt {*emno-, *emnl) " pair of twins ', emnaid^ double '; 

Note: 

labialized laryngeal hre- > 0e- Celtic = hre- > 0e- Hittite 

perhaps here Germanic *ibna-^ even, equable, uniform ', whether from *imna-< 
*Jemn6-, in Gothic ibns^ even ', Old Horse Jafn, Jamn, Old English efn, engl. even, asachs. 
edan, Old High German eban^ flat, even '; 

after GiJntert (Weltkonig 337 ff.) here the Old Norse GN Ymiras " hermaphrodite ' from 
Germanic *Jumiiaz, Indo Germanic *iem(i}i6sl 



Note: 

labialized laryngeal hre- > Proto Germanic ye-, Old Germanic e-, i-, y-, h3"o- > Proto 
Germanic yo-, Old Germanic jo-, io-, h2"a- > Proto Germanic ya-. Old Germanic ja-, ia- 

it is not certain, whether it also belongs here gr. nM^PO"^ "tame, domesticated, mild', 
nijepiq, -iSoc; " the cultivated vine ', npspou) " tame, make tame ' (with lengthened grade e), 
and as zero grade Latin redimio^io bind round, wreathe round, encircle, gird, wind, deck, 
crown', as well as infula "a white and red fillet or band of woollen stuff, worn upon the 
forehead, as a sign of religious consecration and of inviolability, a sacred fillet; so a priest's 
fillet' {*im-6^laRl). 

That with gr. r|M£po(; identical Old High German asachs. jama r. Old English geomor^ 
sad ', Subst. Old High German 73/773/"' sorrowful, sad, regretful, full of pain, grieving, 
mourning, lamenting ' (originally supposedly " sad, gloomy ') might belong though because 
of Old Norse amra " lament', that to emja, ymja "howl', has rather originated from an 
interjection. Cymr. a/^/'"affliction, lament' (Middle Irish amar ds.) could not have lost/ and 
therefore it must have already been been absent. 

Note: 

labialized laryngeal hre- > Proto Germanic ye- > 0e- Celtic, Greek 

labialized laryngeal h3"o- > Proto Germanic yo- > 0o- Celtic, Greek 

labialized laryngeal h2"a- > Proto Germanic ya- > 0a- Celtic, Greek 

References: WP. I 572, WH. I 587, Marstrander Eriu 5, 160. 
Page(s): 505
```


## [2026-10-17T00:30:55.529Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41140,41160p POK_full.txt; grep -n -i '^yem-\\|^yes-\\|^jem\\|^jes' AHD_watkins1985.txt IEC.txt | head; "
}
```


### [2026-10-17T00:30:55.929Z] TOOL RESULT

```
'heal, cure', but because of Old Irish hTcc{\v\6o Germanic e) it is not credible. 

Page(s): 503-504 



Root / lemma:7e/77- 
Meaning: to hold 
Material: 

Note: 

labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite 

labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old \r\6'\c yamat/" reins, steers; stretches, presents ', yacchat/ds., yata-h^kept, held', 
yama-hm. "rein', yantra-n. 'rope, band, strap'; Avestan yam-, yasaite. Old pers. Imperf. 
ayasata, participle Avestan yata- "hold, stop', ya/a- "assigned allotment, possession ' (to a 
AHD_watkins1985.txt:1191:yem-. To pair. Perhaps altered into Latin geminus, twin, paired: GEMINATE, GEMINI, GIMMAL; BIGEMINAL, TRI- GEMINUS. [Pok. iem- 505.]
AHD_watkins1985.txt:1193:yes-. To boil, foam, bubble. 1. Germanic *jest- in Old English gist, yeast: YEAST. 2. Greek zeein, zein, to boil: ECZEMA, ZEOLITE. [Pok. jes- 506.]
AHD_watkins1985.txt:1699:JEST gerere
```


## [2026-10-17T00:30:59.931Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==272' HRN.txt | head -80; echo; grep -n 'yäd\\|yād\\|yad ' HRN.txt | head; grep -n 'yäd\\|yād\\b' HUB.txt | head"
}
```


### [2026-10-17T00:31:00.378Z] TOOL RESULT

```
— 250 —
1,V.
1118. i, L Izäfe.
aw. f/at; phlv. /", päz. i.
Das Neutrum nimmt auch Caland, Zur Syntax
der Fronomina im Awesta, S. 24 als Grundform des
np. ? der Izäfe an ').
{^118»''^ yfi oder.
Da die Lesung des entsprechenden, jedenfalls aber
mit %" anlautenden Pehlevlwortes ganz unsicher ist,
so lässt sich keine sichere Etymologie aufstellen.
Die neueste Fr. Müller\s (WZKM. IV, :35(i), der
als Grundform ap. "^adcivd annimmt, ist möglich aber
auch nicht beweisbar. ,, . , ,.
\/fll9. {\)yäd ^Erinnerung, Gedächtniss', yädifär.
aw. yäta- 'Gedächtniss (Geldner, Studien I, 10,
Note 2); phlv. ijät (vd. 19 (96)), sonst äyät^).
Anders Fr. Müller, WZKM. 5, 265.
1120. {lyyäd (Suflix), in hunyäd,
ap. 'data-, vergl. No. 521.
Wl21. yär 'Freund', yärl-, yärwer (Sahn. I, 126 Vers 1117).
V
yäwer^ yawert (AM. 162 Zeile 2; Sahn. I, 219 Anm. 5,
Calc).
phlv. äyär (die Lesung scheint durch haniäyär, z. B.
Men. 2, 77, erwiesen zu werden; der 6-Strich ist
wie in äyät 'Erinnerung ganz belanglos bezw. un-
gehörig), äyünh'^).
Fr. Müller sucht WZKM. 5, 67 noch über das
PehlevT hinaus zu kommen, meiner Ansicht nach
^) Die Wiedergabe der Izafe durcli e im zweiten Paraslprakä^a
(Weber, S. 8) ist ohne etymologischen Wert und kann nicht zu sprach-
lichen Schlüssen verwendet werden; richtig mit / findet sie sich 8. 25
Note 7 und 49 Note 2 ausgedrückt. Mit e (oder vielmehr ye) wird die
Izäfe im heutigen Persisch, so viel ich weiss, nur nach vorhergehendem
hä-i maxfty ausgesprochen, z. B. bende-ye isläm.
^) Phlv. yät ist vielleicht nur umschreibend.
3j Beruht mand. LW. j<T){<nN *Helfer' (Nöldeke, Mand. Gr.
41H Note 2) nur auf einer falschen Päzendlesung? Aber np. yärer?

560:ap. vergl. Äd^rina-, Ä&riyädiya- ; aw. äfar- 'Feuer ;
2359:229. {2)bun 'Fundament, Grund*, vergl. bunyad {*bundad),
3274:347. piyäde Tussgänger, Fusssoldat*.
3277:LW. kurd.|)^«/cl; af;'. piyäda; bei. plyädag, n, piyCLöay,
6720:ap. yßäyad iyänäm ysäyadiya *der Könige König',
7206:828. feryäd *Hilfe; Hilferuf, Klage.
9654:\/fll9. {\)yäd ^Erinnerung, Gedächtniss', yädifär.
9658:1120. {lyyäd (Suflix), in hunyäd,
9696:Ishendyäd nach.
10535:oss. d. yädä, t. qäd 'Baum, Balken, Holz, Wald' (?)
```


## [2026-10-17T00:31:06.159Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ayād\\|^ayāb\\|^ayād\\|^yam\\b\\|^jam\\b\\|^jamšēd\\|^jah\\|^jastan\\|^yāt\\|^jast' PHD.txt | head; grep -n -i 'ayād\\|ayyād\\|^ayāt\\|^āyāt' NYB_vol2_glossary.txt | head; grep -n 'Yim\\|yim' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:31:06.467Z] TOOL RESULT

```
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
5578:jahišnayār
2812:ham-oden < *ham-aßden), whence NP ummēd ; in SW > *aißimati- > *ayißmati- > *ayim(m)ét, whence émét (written 'dmet, cf n. pr. Ēmēt, patr. Ēmētān, q.v., also with secondary aspiration Hémét; Arab ’Imäd) or ah(im)mét > ahmét ['smyt! S, I, 25 + NP amid].
4256:Vivanghänän [wywngh’n’n'] patr. of Vi- vanghān the father of Yam (Yima) 47°. 1015, — Vivanghän is in itself a patr., Av.
4259:(1451) vivanghana-, from (1452) Vivah- vant-, the old Aryan name of Yima’s father (RV Vivasvant).
4410:Yam [ym] one of the primeval heroes, son of Vivanghan, 3918, 4425, 455, 478. 781, 9012, 1014. 11315, 1147; ~ i šēt = NP Jamšed 10524, v. sé. — Av. (1300 sq.) Yima (OInd Yama-); Paz. Jim; NP Jam; v. Yam-kart.
4414:Yam-kart [ymkrt'] made, built by Yam. 9718, of the var or fortress in which Yima saved the living beings from the Great Inundation (Vd. 2); ~ is almost used as the n. pr. of this var.
5468:yaz-: yaštan, izišn yazata-: yazčt Yima: Yam yujyasti-: yujiyast yüxta-: yuxt yūšmāka-: šmāh yvan-, yavan-: yuvān
```


## [2026-10-17T00:31:10.244Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'jah-\\|jastan\\|jahīdan\\|jahidan' CHEUNG.txt | head -20; grep -n '^šēt\\|šēt \\[' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:31:10.706Z] TOOL RESULT

```
14477:*KHOTANESE: ? Jah- ‘to be cleansed’, jeh- (caus.) ‘to cleanse’ = SGS: 35, 37 
14624:aujah- (YAv. pairi.aojastara- ‘stronger’), cf. AIW: 862; Nyberg II: 160b. However, 
25549:*AVESTAN: ОАу. i@tiejah- [п] ‘abandonment (?)’ (Y 34,8), YAv. iðiiajah-, i0iiejah- 
30586:*MIDDLE PERSIAN: ? BMP yh- /jah-/ *to jump; arise, happen, occur' (see below) 
30606:*NWIR: ? NP jastan/jah-, Khuns. £is(s)- (inch. ?) ‘to jump’, Bal. jist/fih- ‘to flee’ (< 
30608:old connection cited by Horn 1893: 94 for NP jastan/jah- is semantically 
33491:i0iiajah-, iOiiejah-, 393 
35773:yh- /jah-/, 473 
36800:jah-, 215 
41100:Jastan/jah-, 474 
2026:hēšītan to dry, to wither (intr.): pres. 3d p. sg. hēšēt [hwšyt'] 9612-13, 9811, hošet [hwšty] 128%. — Av. (1738) hao$-; MPrth pres. hwš-, xwš- (MHC); Bal husay; NP xoSidan. V. also husk.
4354:x'ar-xšēt [hwlhšyt'] 869. 872-15, 884-8, 8914, 903, elsewhere xvar-šēt [hwlšyt'] the sun. — Av. (1848 sq.) hvaro.xšaēta- from hvar-, x"an- (1847 sq.) ‘the sun’ + (541) ašaēta- 'splendent'; MPrthPrs xwrxšyd; Paz. xtarsed, xuršed; NP xuaršed, xuarščid.
```


## [2026-10-17T00:31:13.586Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30570,30625p CHEUNG.txt"
}
```


### [2026-10-17T00:31:13.851Z] TOOL RESULT

```
*IE COGNATES: Gr. yevouat, Lat. gusto ‘I taste’, gustus ‘taste, enjoyment’, Olrish 


do-goa (3sg.) ‘chooses’, Goth. ga-kiusan ‘to test’, NHG kosten ‘to taste’ 
*REFERENCES: EVP: 103; DKS: 354b; Werba 1997: 187; NEVP: 104 


*zgad ‘to go on, gallop, mount’ 
*AVESTAN: YAv. zgaó(/0)- ‘to go on horseback, gallop’ || (+ *fra-) ‘to go forth’ 


c» Liste: 69 
Pres. them.: IND. med. 3sg. YAv. zgaóaite (V 9.46), Y Av. frazgaóaite (Yt 5.97), INJ. 35р. ? YAv. zga0at 
(F 20), med. 35р. Y Av. frazgaóata (Yt 19.56, Yt 19.82) 


*MIDDLE PERSIAN: ? BMP yh- /jah-/ *to jump; arise, happen, occur' (see below) 
Pres.: IND. 3sg. BMP yhyt /jahed/; Partic.: perf. pass. BMP yst /jast/ 


*KHOTANESE: (+ *aua-) LKh. va’ysged- ‘to dismount’ || (+ *fra-) OKh. haysgas- 
(pret. stem) ‘to walk’ = SGS: — 


474 *zgar (*Zgar ?) 


*SOGDIAN: (+ *abi-) BSogd. Bzyó, CSogd. bzyd, MSogd. Bjyst- ‘to mount’ || (+ 
*aua-) BSogd. ’wzy6 ‘to dismount from a horse’ || (+ *ham-) ? CSogd. ’zgd ‘to leap 
u 

EN Impf.: IND. 35р. SSogd. B'zyó, 3р1. BSogd. B'zyó nt, CSogd. b’Zydnt, Pass.: pperf. intr. IND. 
3sg. MSogd. Pjystyy wm’t ‘was mounted’ || (+ *aua-) Impf.: IND. 3sg. BSogd. w’zyö, 3р1. BSogd. 
w’zyö’nt, Perf.: IND. 3sg. MSogd. ’wjystyy "'styy ‘is descended’ (ВВВ: 34) || (+ *ham-) Impf.: IND. 
3sg. CSogd. ’zgd 

*NWIR: ? NP jastan/jah-, Khuns. £is(s)- (inch. ?) ‘to jump’, Bal. jist/fih- ‘to flee’ (< 
NP ?), Qohr. jugada/jug- (with a hiatus filler -g-), Tr. Zva(yayZv- ‘to walk’. Ф The 
old connection cited by Horn 1893: 94 for NP jastan/jah- is semantically 
implausible, cf. Hübschmann 1895: 50. Bailey suggested a connection with Av. 
zgad- (scribbled on his copy of Horn 1893: 94 ad jesten). The initial j- of the verb 
would go back to the palatalised variant *dj-< Plr. *zj- ? 

*NEIR: Pash. zyastal/zyal- ‘to run’, Yi. zoyal-/zoyast- ‘to run away [from a wild 
animal]’, Sangl. ziö-/züst ‘to flow, run’ 

*MISC: (+ *aua-) Par. uzg-/uzgi ‘to descend’ 

© The root is exclusively Ir. 

*PIE— > LIV: — | Pok.: 

*REFERENCES: EVP: 101; IIFL I: 238a; IIFL II: 275a, 424b; DKS: 355b, 466b; Lecoq 2002: 122, 129; 
NEVP: 101; Korn 2005: 94, 318, 369.
```


## [2026-10-17T00:31:17.348Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==116' HRN.txt | grep -n -B2 -A12 'jas\\|jah'; echo -----; awk 'BEGIN{RS=\"\\f\"} NR==61' HUB.txt | grep -n -B2 -A10 'jas\\|jah'"
}
```


### [2026-10-17T00:31:17.696Z] TOOL RESULT

```
25-ai. \/^yaS', ydsyati, yäsati 'sprudeln , skr. 's. abmühen,
26-s. anstrengen*; aw. [/^yah- 'sieden', vergl. yaesyantim
27:äpetn; phlv. Jastan, jahet (Men.) bezw. yastan,
28-bei. LW. jihag 'entkommen, entrinnen' (115).
29-Hörn, KZ. 32, 587 No. 22. Die Grundbedeutung
30-der V^yeS' ist 'sprudeln, kochen, sieden , vergl. auch
31-gr. 'Qsm.
32-421. jenk 'Unglück* (unbelegt).
33-aw. yaska- 'Krankheit'; phlv. yask (N. pr. Yaskdat
34-auf einer Gemme ZDMG, 44, 652 No. 7 ist zweifel-
35-haft), tsk (Bund.).
36-422. JeSn 'Fest, Gelage* »).
37-*) Im FJ durch einen Vers Euveri's belegt. Häufig im Sähname.
-----
3-ju. Ira Afgh. liest Geiger zdvql zlHfql *nagen, beissen,
4-kauen, Raverty jovul^ joyil, zdvul, Sdyal 'to chew'.
5:416. Np. jah *Wurde, Stellung' kann nicht = skr. yata-
6-(das = np. *yad ware) sein, es miisste vielmehr auf
7-skr. *yatU' (vgl. wegen h aus t np. gah und iah) oder
8-yatha- *Bahn (in dtrghayathd-) zuruckgefiihrt werden.
9-Vielleicht ist Jah urspr. arabisch (No Id eke).
10-417. Sehr bedenklich, da jdi 'Ort* auf ap. *yada' deutet.
11-418. Lies aw. yuta- (fiir yuta-) vd. 5, 55.
12-419 — 420 sind wegen der Bedeutung fsuchen' = *karapfen',
13-*springen' = 'sieden') unsicher.
14-423. Dazu afgh. LW. juy 'the yoke of a plough'.
15-424. Tax afgh. LW. jiift genau, richtig, Paar gehort
```


## [2026-10-17T00:31:31.156Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^ *1301 *$\\|^ *1300 *$\\|^ *1302 *$' BRT.txt | head; grep -n -i 'Zwilling' BRT.txt | head; grep -n 'Gedächtnis\\|Gedachtnis' BRT.txt | head; grep -n 'yaēšy\\|yaesy\\|sieden' BRT.txt | head"
}
```


### [2026-10-17T00:31:31.744Z] TOOL RESULT

```
19894:•)  Sie  werden  «Is  Zwillinge  gedacht  {%.yima- mit  Litt),  die  in  ewigem  Kampf  mit  einander liegend  alles  Seiende  gcschafTen  haben.  Nicht ganz  klar  erscheint  das  Verhältnis  des  guten (heiligen)  Geists  zu  AkuraMoidäh.  Es  kommt das  dahei,  dass  Zca-i^üiirai  Lehre  eben  doch nicht  rein  dualistisch  ausgedacht  ist ,  sondern das*  sie  über  die  beiden  uranfan glichen  und g;Ie ichmächtigen  Geister  des  streng  dualistischen Gedankens  die  Gottheit  dt^AkuroMaidSh  hinaus- hebL  Auf  diese  Weise  «iid  der  heilige  Geist, wo  er  in  Beziehung  zu  AhM.  gesetzt  ist,  lu einem  dienenden  und  yennitielnden  Gci«(  de» AML,  nicht  anders  als  Aia,  VohuManak  usw., und  als  nener  Gegensatz  ergibt  sich  nanmebr AhuraMaidäh  und  AnraMainyav.  Litt  bei  In. GIrPh,  3.  630  f.
3603:unvergänglich':  däya  .  .  xratüm  paslaaa masitim  mazänUm  "nm  "gib  .  .  alsdann Gedächtniskrafi,  grosse,  umfassende,  un- vergängliche" Y.  62.4.
4578:•)  Vgl.  noch  3rat>d-  mit  vi.  Die  Lebrieit  des Awestaschulers  ist  drei  Jahre,  je  eins  bei  drei I-ehrem.  Bei  jedem  soll  er  nach  einem  halben Jahre  das  Gelernte  bereits  sicher  im  Gedächtnis haben,  so  dass  er  beim  Vortrag  keine  Verstösse macht.   Andernfalls  ist  der  Lehrer  lu  wechseln;
9152:—  afrin>in  ifmiavät  Az,  2;  Vyt.  J  (wo k^rjnofilAi);  —  va!s  paoirlm  miirsm k^rmaoiti  V.J.3;  —  iian  (sd.)  hä  iiisläta iiryatii>  Yt.  10.  109;  —  ^fö  0ng  /rS.ga pa^mSng  hucistöis  (sd.)  *carat  (Konj.)9> ; \.4li.a,\  —  k(ii:a..  zarjm  (sd.)  (ar,l»r'>' kaca  xsmal  Y.  44. 1 7.  a)  mit  Adv,  statt Akk.:  II  ya^äsäm  hacärnJ"  d^ahyJ'  ara^^J *aJh/riavaya"li '^  Bh.  j.  S;  —  <iai  yimd ara'ia  k^rjfiaat ya'>a..'V.-J.$2.  h)  mit Inf.  als  Obj.:  yaf  kirsnaot..  c^airyqn  (sd.) 3far?i>m  ajyamnum  Y.'y.4; 75,16  {k}rma-\ rJni).  S- S.  2a)  mit  sksfuiem  'etwas' (Akk.)  zerbrechen,  zerstören';  shnd?m  (sd.) sl  mauö  k^nnüi'A  Y.  i/.  28.  b)  ;  mit züre^  'Jemandem  (Akk.)  Unrecht  tun': naiy  "sakurim  .  .  zür,^  (sd.)  akunavam Bh,4. 13.  c)  mit  ntazdam  Med.  'sich etwas  (Akk.)  ins  Gedächtnis  rufen,  recor- dari':  inasdqmcä  büirüä  (s.  bei  5)  ktrshul ,  .  xrapaitl  (sd.)  hyat  ahmat  aibi  Y. 40.  1 .  3a)  'Jemanden,  etwas  (Akk)  iiin- schaffea  zu  -,  verbringen,  versetzen  in  -'; a)  mit  Lok.  des  Ziels:  II  pasäva^dis a''ura^mazd<l  maiiä  dastayi  (sd.)  akunaus Bh,  4. 4,  1-)  mit  Lok.  eines  Nom.  act. zur  Umschreibung  des  Verbs:  vispqm  .  . taiiüm  ayao^dsta  (sd.)  k)rJiiaoiti  V.<V,4o;
9182:'dem  Gedächtnis  einprägen"';  vahists ahurö  uiazd-l  ahun^m  rairtm  Jrilmraoi vahistö  häind  karayat  "der  beste  AhM. hat  den  AhunaVairya  kund  getan,  der selbe  beste  hat  ihn  dem  (unserm  ?j  Gedächt- nis eingeprägt"  \.ig.\t,; — a'ia  tkalhm kärayäti  "in  dieser  Weise  prägt  er  (uns) ein    Dogma    ein"   Y.  :;o.  1.  a)    in    der
10609:mönnäat  (sd.)  .  .  jyStSul  .  .  'tum  ('Plan')  |  itJ.107 Y-J2.9;  — ya  angrayä  karapanS  urspa- ydntJ  (sd.)  yäcä  'tä  (IS.,  'Absicht')  dus»- xid^ra  .  .  'S:.  48.  10;  —  vT6vä  avoi kava  Orca  ('Absicht')  paraiti  V.  75. 2.  a)  'Geisteskraft,  Einsicht,  Verstand  ; Gedächtnis  kraft,  Weisheit':  mana  'üwa^a ästica  (sd.)  Yt/.  26;  —  tat  müi  'tSui ('Verstand')  manankascä  vTä%?m  (sd.)  Y. .,^6'.  18;  —  hyat  .  .  ma-dj  .  .  gal^ascä tasü  damäsca  (sd.)  . .  -tus'cä  (AP. ;  'Geistes- kräfte').. Y.j/.i  i;  —  data  't^us  ('Geistes- kraft')  ..rdzA^f  vaha  sähtt  (sd.)  mananha Y,  50. 6 ;  —  hvd  -'iwa  ('Geisteskraft')  damis (sd.)  ahm  Y.  _?/.;;  —  vJdva  yai^l  güzrä (sd.)  singha»hg..vai3hsul  °'>:ina  ('Geistes- kraft') mananhö  Y.48.3;  —  aiJ  h^m firasvä  (sd.)  Jiw,?  '>wit  ('Verstand')  Y. 53-y<  —  *vfm4   aiat  hava   -^wa  Y.21
12847:(Akk.)  festhalten,  es  beobachten,  nicht davon  abgehen':  \datant  tyJ'  mans  atti^ *adariy''^  "das  Gesetz,  das  meine,  es  wurde gehalten"  D.  6'.  3 ;  —  Ayat  aksyü  (sd.)  ults yS  ahm  dadrl  Y._5J.8;  —  nanm  asavan^m dalrän^m^^  Aumahm^a  maus  .  .  Vr.  2. 5.  a)  fest  im  Gedächtnis  behalten, immer  daran  denken':  siaeta  yemya  .  . dadräna^*  paid/äna  Y.55.6; — yal  dim (nämt,  ahutum  vairTm)  .  .  aakus  .  .  asa- xtai  (sd.)  *sa^qs  dadrän5'°'^  ..  Y.  sg. 10.  3)    'darauf   halten,    dass  — ',    mit
12935:•  j.,  g.  daradi^i  InC  i)  'in  seinen  Besitz zu  bringen,  sich  zu  erwerben':  kads  .  . uxfanS  (sd.)  asnqm  anhJuf  d'  frö  alahyä /rannt!  ".  .  auf  das  die  Welt  das  ^a sich  erwerbe"  Y.  46'.3.  3)  'au&ufassen, zu  vernehmen':  uH  ahurahe  masda  yata- maide  d'  mq%rahe  spmtahe  . .  xratüm  .  , marä^rai  .  .  Aitvqm  .  .  fravakai  "wir  ver- ehren die  Ohren  (das  Gehör)  des  AAM., dass  er  das  heilige  Wort  vernehme, . .  die Gedächtniskraft  . .,  dass  er  (es)  behalte, die  Zunge  ,  .,  dass  er  (es)  verkünde"  Yt
19871:•  g.  mand-  V.  'dem  Gedächtnis  ein- piägen;  im  Gedächtnis  behalten*.  Praes. (5)"  mSn  . .  äad-'^.  —  In£  *iiundaidyäi'\ mSn  . .  daidyäi'^,
19872:i)  'dem  Gedächtnis  einprägen':  säsfsnj ..  msaca  i  mqxäasdam  ** ..  "Lehren ..;  prägt sie  auch  ins  Gedächtnis  und  .  ."  Y.^y. S.  3)  'im  Gedächtnis  behalten,  ein- gedenk sein',  mit  Inf.:  yS  *urvatum  trOn £airl{sä.)  ..  dadl(iSPM.)  Y.2Ä4.
19950:i)  'etwas  (Akk)  merken,  im  Gedächtnis behalten,  dessen  eingedenk  sein' :  mat  täÜ vTspai^  ylfi  tsi  mq%ra  tnanntl  "mit  allen denen,  die  deiner  Worte  eingedenk  sind" y.43.1^; — ta  vs  urvotä  i&A.)  manntn .  .  sJngAamahX  Y.  31.  i.  a)  'merken auf—'  (Akk.):  ^ass  itthaire  . .  ave  aipi daß,yaniS..Aismar3ntB'^Uo.^S;  b)'be- merken':  karS  masyS yB  ranh^h .  .varjss.- '  stavanhm  äpS  urvaäim  marayäte  Yt. 14.29.         2)  Gebete  usw.  (Akk.)  'sich  ins
14854:Ä8.  a)  mit  Abi.  'aus  -':  paourva.-  daliß&z\ia  Art  'herangehen  zu-';  a)  mit namat patai  dyaoHf^A.)  .  .  anrö  mainyus  -qxl.:  hamaka  airyabyU  daiAhubyB  hatna Yt. j.  iz;—ptat  (3SPrA.) F.  10.  3) ^oia ,  f^apatänti")  Yt  S.  61.  b)  m\tpaiH und Wasser;  a)  'herabfallen,  -strömen',  vom  j  Akk,;  s.  a/rapatai  Int Regenwasser:  s.-V««/-(in/«/.3A).  b)'über-  mit  z^r(z'(/)  in  rfo^Hscher  Art 'weg-,  fort- fliessen',vomsiedendenWasser(?):><W««/a  l,gn,.  ^fj- ^pam  Ha patmiu  vi  dalvhM (sd.)  patmla  F.  4  f.  4)  Term.  techn.  für  %j  ^  g  yf /o.  i . dasGehen  rfjftTschcr  Wesen:  hamySila  ..\  mit,ia«'fallen,hinabstürzen in-'(Akk.): davqi>ya  patqi^yä  Y.g.  18;  —  vagn^mn^  \  ^ru/asianam(sd.)  haMpataiti{T&m\.daevd) (sd.)  anmat  para  dalva  patayin  Yt  ig.  80; '  V  70  4.1    '  *
21503:•  j.  yah-  V.  'sieden'  (intrans.).  Praes.  6 jraesa-'\  2^  jyagsya-.  —  FP[P.  yaäa-i?)».
21504:'sieden,  sich  in  Siedehitze  befinden': yaihnia  (3?.)^'  fatmta  "(die  Wasser) siedeten,  flössen  über"  F.  4f-;  —  ffqs (sd.)  ayanhsjrasparat  yais'yantim  äptm *paraiihät  "..dassiedendeWasser schüttete er  um"  Y.p.ii;  —  *ya!s?ntim*'  äp>m F-^f.;  —  niioyäti  (sd.)  il . ,  ätari . .  kala yastibys  (DPf.)"  aiwyiJ  ".  .  vor  den siedenden"  Wassern"  P.  2/.
```


## [2026-10-17T00:31:45.810Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'yima-  m\\|yima- m\\|Yimö\\|ai.  Yama\\|ai. Yama' BRT.txt | head; grep -n 'yäta-\\|yata-  n\\|yäta-  n' BRT.txt | head"
}
```


### [2026-10-17T00:31:46.404Z] TOOL RESULT

```
19894:•)  Sie  werden  «Is  Zwillinge  gedacht  {%.yima- mit  Litt),  die  in  ewigem  Kampf  mit  einander liegend  alles  Seiende  gcschafTen  haben.  Nicht ganz  klar  erscheint  das  Verhältnis  des  guten (heiligen)  Geists  zu  AkuraMoidäh.  Es  kommt das  dahei,  dass  Zca-i^üiirai  Lehre  eben  doch nicht  rein  dualistisch  ausgedacht  ist ,  sondern das*  sie  über  die  beiden  uranfan glichen  und g;Ie ichmächtigen  Geister  des  streng  dualistischen Gedankens  die  Gottheit  dt^AkuroMaidSh  hinaus- hebL  Auf  diese  Weise  «iid  der  heilige  Geist, wo  er  in  Beziehung  zu  AhM.  gesetzt  ist,  lu einem  dienenden  und  yennitielnden  Gci«(  de» AML,  nicht  anders  als  Aia,  VohuManak  usw., und  als  nener  Gegensatz  ergibt  sich  nanmebr AhuraMaidäh  und  AnraMainyav.  Litt  bei  In. GIrPh,  3.  630  f.
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
5818:Im  Anschluss  an  den  AS.  astim  gebildet.  — Hid-  Adj.,  zum  ai.  V.  bhinädmi;  ai.  'hhid-  Adj-, afy.  vgl.  Äifa/ 'getrennt' (?).  —  Pü.:  asi  ikan. — ')  sva.  'yäta-,  sd.
21269:•  h  S>  P-  'y^'oa-  V.  'halten; fassen'.  Praes. I  yam-,  14  yasa-.  —  PPfP.  'yata-;  PFP. apayanta'  (Ableit);  Inf.  'yatie,  °yätT, 'ynne.        S.  noch  'yäta-,
21540:•  j.  'yäta-  n.  'der  Jemandem  zugewiesene Anteil;  Besitz':  myazdavh  raiui  amyasda- vatam  raiunaim  *tfm  gal'hanqm  frapirf- naotti  ". .  verurteilt  den . .  Laien  zum  Ver- lust seines  Anteils  an  Hab  und  Gut"  A. ^.11;  —  bao6asca  urvStitmla  'Um  gaz'ia- natu  paiti.jaihydnti  dahm  astvainti  aahvB **, .  befragen  sie  nach  dem  Anteil  an  Hab und  Gut,  der  (dem  Verstorbenen)  . .  ver- lieben war"  V.jp.  29";  F.^f
21542:•  j.  'yäta-  n.  Terni.  techn.  für  die  der Schwere  nach  dritte  Art  von  Körperver- letzung"; %rUäm  tarS  x^araya  (sd.)  .  . vUp)m  larS  *yär?Jräjahehim  °t)m  ästrydti N.42i  F.4f.i  —  'fa  raifqm  . .  N.77T{?).
23762:•  g.  v«razyäta- f.  'landwirtschaftliche Tätig- !  6 1.  a) 'Überschwemmung  durchFeindes- keit,  Landwirtschaft':  yaoidä  (Sp.  1 236  m.)  [  heer,  Einbruch':  vUan.qsahyekeca  paiü  vl- mafyai  *aipT.tq^>m  vahiltJ  gavBi  'tarn  1  tart.ibaEsahyeheia  pairi  *halnySsia  "fnäuyS tarn  nJ  ifartkai  fsuyS  {S^.  1028  m.)  '^^&\aun>a'^aabyasia  pars  "zur  Überwindung . .  vollbringt  . .,  fUr  das  Rind  aber  die  der  Not  und  Drangsal  in  Folge  der  Ein- Landwirtschaft; . ."  Y.  4S.  5  ".  j  brüche  des  Feindesheeres  und  von  Seiten
```


## [2026-10-17T00:31:51.038Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>21540 && NR<21800 && /[Yy]i?ma-|Zwilling|Yama/ {print NR\": \"substr($0,1,600)}' BRT.txt | head -20"
}
```


### [2026-10-17T00:31:51.486Z] TOOL RESULT

```
21631: Man  erwartete  *yavärina;  all  Komp.  au«  yma- +*ar3iia-  n.,  eig.  Instrament  zum  Mahlen des  Getreides';  ■.  zn1izJa-undGIrFh./.3ti[. — np. yävar, yär.  — Pfi. :  iur/öt  1  ör/'gemahlenei Getreide'i    erLi    äiyäi  i  fa  datt  '«ine  Hand*
```


## [2026-10-17T00:31:58.042Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'xsaeta\\|xsaäta\\|xsaSta' BRT.txt | grep -i 'yim\\|jam' | head -5; grep -n -i \"Jamse\\|Jamsed\\|jamsid\" BRT.txt | head -5; grep -n 'yzmJ\\|yJmö\\|ya-m-\\|y?ma-\\|yjma\\|y»ma\\|yama-' BRT.txt | head"
}
```


### [2026-10-17T00:31:58.583Z] TOOL RESULT

```
10698:•  j,  xSaeta-  Adj.,  fem.  xsöiSni-"  'licht, strahlend,    glänzend,    herrlich';    i)    vom Licht  usw.:    °ta    rae^A    Ytj.  1;    —    ." *bamya   -«/{als    GS.)    Yt.70. 143;'* usänhfm  .  .  '^nfm  G.  5.  5;  —   'ünyJl usayll  YtÄ35.  2)   von  Göttern  und Menschen:    bfrizanlim    akur^m apqnt    napätptn  Y.  2.  5 ;    —    asis  .  .  srlra 0«(  Ytij.  107;    —    asim    ..    ''inim  Y. 2.14,  Yt/J.  i;  —  arptfplm  ..  ''hnim  YL 5.  1 5 ;  —  am3sanqm    spmtanqm    'tanqm Y.2tf.3;    —    nar/ A?hrpa  .  .'"ta/ie  Yi.8. 13;    —    kainlnS    kikrpa  ..  ''ä-nyä    H.  2. 9;    —  frazantsis   .  .  '^nyä  (GS.)  Yt  ij. 134.          a)   bes.  von    Yima:  yS  yimd  'tö
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
6281:—  r3laca  vaauhi  .  .  °saane  (VS.)  V.  /(?. 19,  Vytjö;  S,  1.5,  2.5;  —  raziflam  astim ..  "saonJm  Yt.16.1,  4;  o,  20;  —  airyama- mm  iitm  '^avan^m  Vr.  24-  3 ;  —  kaomS °^ava  Y.p.a';  10,14;  —  haoma  °lava (als  Vok.)"'  duraosa  Y.  j/.  10;  —  rasmiö °lilum  Yt  J2. 7;  9; —  sraohm  .  .  '/avarum Y-  57-  2i  33,  Yt.  II. T,  —  Aaurvat3t>m 'savaram''^  asahe  ratüm  Y.  71.  12;  — am^ntät^m  "savanpm'i^  asahe  ratüm  Y.7J, 13;  —  ahura  müra  .  .  •s'avana  (AD.) Y.  2. 1 1 ;  YL  70. 14s;  —  ahuraHbya  miitraei- iya  '/avanaäiya  Y,  j.  11,  a)  bes.  von Ahura Mazääh:  3  äim  tä  vaca  rämayal ahurS  masdä  'sava  alavansm  zarä^ulinm V.5.2I;  jp.15  (statt  Akk.),  Y.7/.4,  5,  57. 24,  Yt.S.i,  11.1%  12.4,  16.3,  Yt/0.89, 7J.  14,  15;  —  ahur)m  mazdqm  'iavamm aiahe  ratüm  Y.2,2,    t6.\,  ^5.1,  7/.2,  4;
17358:ae'iaahö  (sd.)  ä  maxUtam  ayjmaite  *'üjim  £'=;-  'anfmetksam',  rnm  V.  U-d-,  vgL  M^m.
19954:Gcdidinüs  zorlckiTdiai',  indon  nun  s^'jrmmaroite  A.^5;  —  j{U:a  ..  i«7M  . . m  fyrtanlrwi  odcT  Idsc  nann^nd  wieder-  m*räl  JrS  vi  mmrS  Jnm/^st . .  V.  tg.  6; ho\ti  jat  ja^  <^f  ..  äa}St  aoa  m^^ttm  —  ttjt^  Tt^iy*  ■  ■  f^^immr^wma  fnt- .  .  wLoirjli  V.J.  33t*';  —  mryjmatvm  .  .  martmma  SPm.)  Y.55.6; — yiai  ''fjtam^ iiim..bm  *ML3riMti-  ta^.yjKUfiVi.4,1:  räjm /ntmiargili  ü.  4^ ;  —  *MXavaa  rttüf — /ai  ma^rTm^ramrtnJ  'marä  rSYt.4,  frii  yazat  framaraUi  S-jS;  2/  ('Jlrl;  — 4;  —  yAS:a  . .  ijjam  akuKaJu  'zairydie  ya-Jltt  •A.\  aiti  framarmü  N.32;  2/%  2J; marJf*' ..  dr7m;jjit  . .  srsrayjt . .  ya^^iu  jd:  — *iKa'jmy*  *z^a  fram*r»mMf  S.2Ö. Y./5.6;  —  iti^3  jwxiird  .  .  mar»mna\ J^iftiLj  xanmmna  *tixijwaia  sl^syamna  ..\
21285:•  j.  yama-'*  dl  'Glas,  Glasgefäss':  yavat .  .  °manam  paitinam  sairinam  (sd.)  V. Ä8S-
21624:np.  Jäm  'Glas,  Becher'.  Wgh  yama-.  —  Pü. : xumbai  ape  yämii  palin,  erl. ;  däsht  (?)  karän  \ vgl.  Darabs  Bemerkung  dazu.
21734:käryam,  mahattvani,  (m  Y.  4ßy.  samgrämi,  —  i  j.,  g.  yant:  c  ^yama-  mit  No.  3.
```


## [2026-10-17T00:32:06.824Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'yima-  m\\.\\|yima-  m\\|yim[ao]-  m' BRT.txt | head; awk 'NR>=21780 && NR<=21900 && /Vivah|Vlvah|vtvanh|Vivanh/ {print NR\": \"substr($0,1,400)}' BRT.txt | head"
}
```


### [2026-10-17T00:32:07.172Z] TOOL RESULT

```
21827: •  j.,  g.  yiroa-  m.  EN.  eines  sagenhaften Königs  von  Iran*':  yS''>  yims  xfaiß  kvq- ^ws  3far>nat3tthast3mS  zütanam  Y.p.4; YLj.is,  ly.  31,  ig.  34',  V.  2.  ao,  Az.5, V.2.3,  10,  II,  31,  32,  19PÜZ.;  —  "ms vlvatiuhats  ptikrS  Y.  (?.  5;  —  jtfm''  'mtm xic^im  Yt  /ß.  3 1 ;  —  'ma  srfra  vlvanhana V.2.3,  9, ä'j  41*3,24;  —  *mahe vlvaaha- nahe  Yt  y- 130;  —  'tnat
```


## [2026-10-17T00:32:09.372Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21827,21835p BRT.txt | cut -c1-2500"
}
```


### [2026-10-17T00:32:09.793Z] TOOL RESULT

```
•  j.,  g.  yiroa-  m.  EN.  eines  sagenhaften Königs  von  Iran*':  yS''>  yims  xfaiß  kvq- ^ws  3far>nat3tthast3mS  zütanam  Y.p.4; YLj.is,  ly.  31,  ig.  34',  V.  2.  ao,  Az.5, V.2.3,  10,  II,  31,  32,  19PÜZ.;  —  "ms vlvatiuhats  ptikrS  Y.  (?.  5;  —  jtfm''  'mtm xic^im  Yt  /ß.  3 1 ;  —  'ma  srfra  vlvanhana V.2.3,  9, ä'j  41*3,24;  —  *mahe vlvaaha- nahe  Yt  y- 130;  —  'tnat  haia  vtvanhuiai Ytip.35;  35;  —  'mS  asti  fof3i«(sd.) x/a^royä  V.  2. 7;  —  aal  •mOi  xiahroi *^risatö.uma  ^funjasmia  V.2.  8;  u,  16;
—  -malte  x/dire  .  .  nSil  saurva  änha nSii  rnfry%yu/  Y.  g.  5;  —  'mJi  srirai  .  . paoiryB  masyänqm  aptrise  aam  yS  ahurl V.  2.  2;  9,  23,  75.39;  —  äat  'ms  varsm (sd.)  kirmaot  V.  2. 33';  39;  —  aisqm atnanhqm  vlvanhusS  trOvl  'masct{  "zu diesen  Frevlem  gehört,  wie  bekannt,  auch y.,  der  Sohn  des   Vtv."  Y.32.&.
')  Sohn  des  lifuhan/,   Erbauer  des  l'ar  (V.
3.  23  ff.).  Er  föbn  e in e'tausendj Ihrige  (V.  3. 8,  13, I  16,  19  PüZ.)  glückliche,   von  Hitze  und  Kalte.
Krankheit   und  Tod  verschonte  Herrschaft   |Y.
(j.  4  f.),  bis  er  in  Folge  lügneritcher  Red«  de* ,  j^ariitah  verlustig  geht,  worauf  er  bis  id  seiner
ob,Google
J/-  3 ff-.  34-*>  Roth  ZDMG.  4.  416,  Windisch- mann ZSt-  19,  147,  DsT.  ZA.  3.  16,  Fov  IFAni- S.  30.  wo  weitere  Lilt.,  Justi  PrJ.  SS.  236. KompA.  —  aL  yamä-  m.  EN.,  np. /««(ffc)''- —  Eig.  Bed.?  Zuletit  Fov  IFAni.  8.  33.  — >)  Die  häußgc  VonnsteUung  des  Relativs  (als Artikel)  verdient  Beachtung-  —  *>  D.  i.  yimä
•  j.  ytmo.k9r«nta-  Adj,  'den  Y,  zerschnei- dend, entzweischneidend':  sfi'tyurvmia (sd.) •t?m  Yt  ig.  46.
```


## [2026-10-17T00:32:17.146Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | grep -i 'usage\\|argv\\|arg' "
}
```


### [2026-10-17T00:32:17.614Z] TOOL RESULT

```
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
    url = args[0]
```


## [2026-10-17T00:32:22.103Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/یاد' 'https://en.wiktionary.org/wiki/جستن' 'https://en.wiktionary.org/wiki/جم' 'https://en.wiktionary.org/wiki/جمشید' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yemHós' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yes-' 'https://www.etymonline.com/word/eczema' 'https://www.etymonline.com/word/zeolite' 'https://www.etymonline.com/word/yeast' 'https://www.etymonline.com/word/Gemini' 'https://en.wiktionary.org/wiki/geminus' 'https://en.wiktionary.org/wiki/جهیدن'; do python3 tools/fetch_source.py \"$u\" --note \"page 564, roots Yem/Yes\" 2>&1 | tail -2; done"
}
```


### [2026-10-17T00:32:27.455Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/097fb2128871ac10.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f69812821424ee36.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c228eda0d57f44a7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/39c14cb2c68ae658.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cbb1cc89a3ebebe0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/00af9c24694c8729.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f9f43bfac495491f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b8afed575c2c6b11.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/48b14bd669d471dc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bf1125400ec8be9e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e858cd401fda6310.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d43e4c4729b96deb.txt
```


## [2026-10-17T00:32:30.544Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 097fb2128871ac10 f69812821424ee36 c228eda0d57f44a7 39c14cb2c68ae658 cbb1cc89a3ebebe0 00af9c24694c8729 d43e4c4729b96deb; do echo \"#### $f\"; wc -c < $f.txt; grep -n -i -A6 'Etymology' $f.txt | head -30; done"
}
```


### [2026-10-17T00:32:30.926Z] TOOL RESULT

```
#### 097fb2128871ac10
13767
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
87: Etymology 1 
88-
89- 3.1.1 
90- Pronunciation 
91-
92- 3.1.2 
93- Adjective 
--
99: Etymology 2 
100-
101- 3.2.1 
102- Pronunciation 
103-
104- 3.2.2 
105- Noun 
--
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
121- 4.3 
#### f69812821424ee36
13436
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
--
74: Etymology 2 
75-
76- 1.2.1 
77- Pronunciation 
78-
79- 1.2.2 
80- Verb 
--
164: Etymology 1
165- [ edit ] 
166-
167- From Middle Persian [Book Pahlavi needed] ( ystn', yh- /⁠jastan, jah-⁠/ , “ to happen, occur, chance ” ) , [ 1 ] from Proto-Iranian *zgad- ( “ to go on, gallop, mount ” ) . Cognate with Northern Luri جستێ ( cestı ) , Baluchi جہگ ( jihag , “ to flee, escape ” ) , Pashto زغلېدل ( zğaledəl , “ to run ” ) , with no further cognates outside of Iranian.
168-
169- Pronunciation
170- [ edit ] 
--
522: Etymology 2
523- [ edit ] 
524-
525- From Proto-Iranian *Hyawd- ( “ to fight, struggle (for something), strive, seek ” ) , from Proto-Indo-Iranian *Hyawdʰ- ( “ to fight, struggle ” ) .
526-
527- Pronunciation
#### c228eda0d57f44a7
9548
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Adjective 
--
74: Etymology 2 
75-
76- 1.2.1 
77- Verb 
78-
79- 2 
80- Khowar 
--
101: Etymology 
102-
103- 4.2 
104- Noun 
105-
106- 4.3 
107- References 
--
115: Etymology 
116-
117- 5.2 
118- Pronunciation 
119-
120- 5.3 
#### 39c14cb2c68ae658
4778
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Proper noun 
--
154: Etymology
155- [ edit ] 
156-
157- Inherited from Middle Persian [Book Pahlavi needed] ( ymšyt' /⁠jamšēd⁠/ ) , from Old Persian *Yamaxšaitah , a Persian formation of Avestan 𐬫𐬌𐬨𐬀⸱𐬑𐬱𐬀𐬉𐬙𐬀 ( yima.xšaēta ) , from Proto-Iranian *yamHáh ( “ Yama; twin, pair ” ) +‎ *xšaytah ( “ bright, shining ” ) , ultimately from Proto-Indo-European *yemHós .
158-
159- Pronunciation
160- [ edit ] 
#### cbb1cc89a3ebebe0
3550
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Inflection 
--
134: Etymology
135- [ edit ] 
136-
137- From *yemH- ( “ twin ” ) +‎ *-ós .
138-
139- Noun
140- [ edit ] 
#### 00af9c24694c8729
4980
#### d43e4c4729b96deb
136
```


## [2026-10-17T00:32:35.395Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 140,200p 097fb2128871ac10.txt | grep -v '^\\s*$' | head -30; echo ----; grep -v '^\\s*$' c228eda0d57f44a7.txt | sed -n '/Persian/,$p' | grep -i -A3 'etymology' | head -30; echo ----; grep -v '^\\s*$' cbb1cc89a3ebebe0.txt | sed -n '/Descendants/,$p' | head -40; echo; grep -v '^\\s*$' 00af9c24694c8729.txt | head -60 | tail -40"
}
```


### [2026-10-17T00:32:35.719Z] TOOL RESULT

```
 5.2 
 Pronunciation 
 5.3 
 Noun 
 5.3.1 
 Declension 
 5.4 
 Further reading 
 6 
 Urdu 
 Toggle Urdu subsection 
 6.1 
 Etymology 
 6.2 
 Pronunciation 
 6.3 
 Noun 
 6.3.1 
 Declension 
 6.3.2 
 Derived terms 
 7 
 Ushojo 
 Toggle Ushojo subsection 
 7.1 
 Etymology 
 7.2 
 Noun 
 Toggle the table of contents 
 یاد 
----
 Etymology 
 5.2 
 Pronunciation 
 5.3 
--
 Etymology 
 6.2 
 Noun 
 6.2.1 
--
 Etymology 1
 [ edit ] 
 Pronunciation
 [ edit ] 
--
 Etymology 2
 [ edit ] 
 See the etymology of the corresponding lemma form.
 Verb
 [ edit ] 
 جِمْ • ( jim ) ( form I ) /d͡ʒim/ 
--
 Etymology
 [ edit ] 
 From Persian جم ( jam ) , referring to Jamshid , a legendary ruler of ancient Iran.
 Noun
--
 Etymology
 [ edit ] 
 From Middle Persian 𐭩𐭬 ( ym /⁠jam⁠/ ) , from Old Persian *Yamah .
----
 Descendants 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ yemHós 
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
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Etymology
 [ edit ] 
 From *yemH- ( “ twin ” ) +‎ *-ós .
 Noun

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
 References 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ yes- 
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
```


## [2026-10-17T00:32:39.079Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 097fb2128871ac10.txt | grep -n -i 'middle persian\\|from \\|ayād' | head; echo ----; grep -v '^\\s*$' cbb1cc89a3ebebe0.txt | sed -n '/Noun/,$p' | sed -n 1,40p | grep -i 'twin\\|Latin\\|Avestan\\|Sanskrit\\|gem' ; echo ---; grep -v '^\\s*$' 00af9c24694c8729.txt | sed -n '/Root/,$p' | sed -n 30,70p"
}
```


### [2026-10-17T00:32:39.490Z] TOOL RESULT

```
166: From Wiktionary, the free dictionary
172: From Middle Persian یاد ( ayād , “ memory, remembrance ” ) .
219: Inherited from Proto-Common Turkic *yāt ( “ alien, foreign, unfamiliar ” ) .
232: Borrowed from Persian یاد ( yâd , “ memory ” ) .
247: From Middle Persian [Term?] ( /⁠ayād⁠/ ) , [ 1 ] [ 2 ] from Proto-Iranian *Habí- + *yáH- ( probably from Proto-Indo-European *yeh₂- ( “ to go; to go in, to enter ” ) , with Iranian semantic shift "to enter [the mind]" > "to remember" ) . [ 3 ] Compare Tocharian A [Term?] ( opyāc , “ in remembrance ” ) , probably borrowed from an Eastern Iranian language.
279: از یاد بردن ( az yâd bordan , “ to forget; to cause to forget ” , literally “ to take away from memory ” ) 
280: از یاد رفتن ( az yâd raftan , “ to be forgotten ” , literally “ to go from memory ” ) 
289: یاد رفتن ( yâd raftan , “ to be forgotten ” , literally “ to go from memory ” ) 
329: ^ MacKenzie, D. N. ( 1971 ), “ayād”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 15 
335: Borrowed from Classical Persian یَاد ( yād ) .
----
---
 Print/export
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Proto-Indo-European
 [ edit ] 
 Root
 [ edit ] 
 *yes- [ 1 ] [ 2 ] [ 3 ] 
 to foam 
 to boil 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *yes- (7 c, 0 e) 
 *yés-e-ti ( thematic root present ) 
 *yé-yes-ti ~ *yé-ys-n̥ti ( athematic reduplicated present ) 
 Proto-Indo-Iranian: *yáyasti 
 Proto-Indo-Aryan: *yáyasti 
 Vedic Sanskrit: ययस्तु ( yayastu , 3sg.impv.act. ) 
 ⇒ Sanskrit: येषति ( yéṣati ) ( thematized from weak stem ) 
 Proto-Iranian: 
 Avestan: 𐬫𐬀𐬉𐬱𐬌𐬌𐬈𐬌𐬙𐬌 ( yaēšiie i ti , “ to boil ” ) ( with *-ya- added to weak stem [ 1 ] ) 
 *yós-e-ti ( o-grade root present ) 
 Proto-Germanic: *jasaną 
 Old Norse: *asa 
 Icelandic: asa 
 Faroese: asa 
 Norwegian: ase 
 ⇒ Proto-Germanic: *jōsiz 
 ⇒ Proto-Germanic: *jōsijaną ( see there for further descendants )
 *yos-éye-ti ( causative ) 
 Proto-Germanic: *jazjaną ( see there for further descendants )
 Proto-Indo-Iranian: *yāsáyati 
 Proto-Indo-Aryan: *yāsáyati 
 Sanskrit: यासयति ( yāsáyati ) 
 *yes-nós or *is-nós
```


## [2026-10-17T00:32:44.197Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' cbb1cc89a3ebebe0.txt | sed -n '/^ Noun$/,$p' | sed -n 1,30p; grep -v '^\\s*$' e858cd401fda6310.txt | grep -i -m3 -A2 'etymology$\\|uncertain\\|From Proto'; for f in f9f43bfac495491f b8afed575c2c6b11 48b14bd669d471dc bf1125400ec8be9e; do echo \"## $f\"; grep -v '^\\s*$' $f.txt | grep -i -m4 'from \\|greek\\|swedish\\|Cronstedt' ; done"
}
```


### [2026-10-17T00:32:44.796Z] TOOL RESULT

```
Exit code 1
 Noun
 [ edit ] 
 *yemHós   m ( non-ablauting ) 
 twin 
 Inflection
 [ edit ] 
 Thematic
 singular
 nominative
 *yemHós 
 genitive
 *yemHósyo 
 singular
 dual
 plural
 nominative
 *yemHós 
 *yemHóh₁ 
 *yemHóes 
 vocative
 *yemHé 
 *yemHóh₁ 
 *yemHóes 
 accusative
 *yemHóm 
 *yemHóh₁ 
 *yemHóms 
 genitive
 *yemHósyo 
 *? 
 Etymology
 [ edit ] 
 Presumably from Proto-Italic *yemanos , from Proto-Indo-European *yemH- ( “ twin ” ) , in view of Proto-Celtic *yemonos ( Old Irish emon ( “ twin ” ) ). If this is true, the g- must have been analogically introduced from gignō ( “ to give birth to ” ) , genus ( “ offspring ” ) . [ 1 ] 
 Pronunciation
 [ edit ] 
--
 Categories : Latin terms inherited from Proto-Italic 
## f9f43bfac495491f
## b8afed575c2c6b11
## 48b14bd669d471dc
## bf1125400ec8be9e
```


## [2026-10-17T00:32:49.912Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in f9f43bfac495491f b8afed575c2c6b11 48b14bd669d471dc bf1125400ec8be9e d43e4c4729b96deb; do echo \"## $f\"; wc -c <$f.txt; head -c 600 $f.txt; echo; done"
}
```


### [2026-10-17T00:32:50.306Z] TOOL RESULT

```
## f9f43bfac495491f
133
URL: https://www.etymonline.com/word/eczema
FETCHED: 2026-10-17T00:32:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
## b8afed575c2c6b11
134
URL: https://www.etymonline.com/word/zeolite
FETCHED: 2026-10-17T00:32:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
## 48b14bd669d471dc
132
URL: https://www.etymonline.com/word/yeast
FETCHED: 2026-10-17T00:32:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
## bf1125400ec8be9e
133
URL: https://www.etymonline.com/word/Gemini
FETCHED: 2026-10-17T00:32:25Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
## d43e4c4729b96deb
136
URL: https://en.wiktionary.org/wiki/جهیدن
FETCHED: 2026-10-17T00:32:27Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-17T00:32:54.748Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/eczema' 'https://en.wiktionary.org/wiki/zeolite' 'https://en.wiktionary.org/wiki/yeast' 'https://en.wiktionary.org/wiki/Gemini' 'https://en.wiktionary.org/wiki/zeolit' 'https://en.wiktionary.org/wiki/ζέω' 'https://en.wiktionary.org/wiki/𐬫𐬌𐬨𐬀'; do python3 tools/fetch_source.py \"$u\" --note \"page 564, roots Yem/Yes\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:32:59.071Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e0515f60aebfd992.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/adcd43fa37d01541.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e8b0be43f3a41930.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/41dc055ee5a64cab.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a2d5d45c9f42d876.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/29981ededd48f1ba.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/12793db03604b43a.txt
```


## [2026-10-17T00:33:02.346Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in e0515f60aebfd992 adcd43fa37d01541 e8b0be43f3a41930 41dc055ee5a64cab a2d5d45c9f42d876 29981ededd48f1ba 12793db03604b43a; do echo \"## $f\"; grep -v '^\\s*$' $f.txt | grep -m4 -i '^ *\\(from\\|borrowed\\|coined\\|inherited\\|learned\\)' | cut -c1-500; done"
}
```


### [2026-10-17T00:33:02.843Z] TOOL RESULT

```
## e0515f60aebfd992
 From Wiktionary, the free dictionary
 Learned borrowing from Latin eczema , from Ancient Greek ἔκζεμᾰ ( ékzemă , “ cutaneous eruption ” ) , from ἐκζέω ( ekzéō , “ to boil out, break out ” ) +‎ -μᾰ ( -mă , nominal suffix ) .
 From Ancient Greek ἔκζεμα ( ékzema ) .
 Borrowed from Ancient Greek ἔκζεμᾰ ( ékzemă ) .
## adcd43fa37d01541
 From Wiktionary, the free dictionary
 From Swedish zeolit , and its source, New Latin zeolites , from Ancient Greek ζέω ( zéō , “ to boil, bubble ” ) +‎ -lite .
## e8b0be43f3a41930
 From Wiktionary, the free dictionary
 From Middle English yest , yeest , gest , gist , from Old English ġist , ġyst , from Proto-West Germanic *jestu , from Proto-Germanic *jestuz . Cognate with Saterland Frisian Jääst ( “ yeast ” ) , West Frisian gêst , gist ( “ yeast ” ) , Dutch gist ( “ yeast ” ) , German Low German Gest ( “ yeast ” ) , German Gischt ( “ sea foam ” ) , Swedish jäst ( “ yeast ” ) , Norwegian jest ( “ yeast ” ) , Icelandic jöstur ( “ yeast ” ) .
## 41dc055ee5a64cab
 From Wiktionary, the free dictionary
 Borrowed from Latin geminī , plural of geminus ( “ twin ” ) , calque of Ancient Greek Δίδυμοι ( Dídumoi ) , calque of Akkadian 𒀯𒈠𒀸 ( māšu ) , calque of Sumerian 𒀯𒈦𒋰𒁀 ( mul MAŠ.TAB.BA , “ the Divine Twins, in Mesopotamia identified as Lugal-irra and Meslamta-ea; name of constellation ” ) . [ 1 ] See Lugal-irra and Meslamta-ea .
 From geminī ( “ twins ” ) .
 Learned borrowing from Latin gemini .
## a2d5d45c9f42d876
 From Wiktionary, the free dictionary
 Borrowed from Dutch zeoliet .
 Borrowed from French zéolit(h)e .
## 29981ededd48f1ba
 From Wiktionary, the free dictionary
 From Proto-Indo-European *yes- ( “ to boil, foam ” ) . Compare Sanskrit येषति ( yeṣati , “ to boil, bubble up ” ) , यसति ( yásati , “ to froth up, foam ” ) , English yeast . [ 1 ] 
## 12793db03604b43a
```


## [2026-10-17T00:33:07.948Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^yeast,\\|^eczema,\\|^zeolite,\\|^Gemini,\\|^geminate,\\|Yima\\|^Ymir\\|^Yama' KLN_1966.txt | head -20"
}
```


### [2026-10-17T00:33:08.313Z] TOOL RESULT

```
15916:geminate,  adj.,  found  in  pairs.  —  L.  gemindtus, pp.  of  geminare,  ‘to  double,  repeat’,  fr.  geminus. See  Gemini  and  adj.  suff.  -ate. geminate,  tr.  v.,  to  double.  —  See  prec.  word, gemination,  n.  —  L.  geminatio,  gen.  -dnis,  ‘a doubling’,  fr.  gemindtus,  pp.  of  geminare.  See geminate,  adj.,  and  -ion.
15917:Gemini,  n.  pi.,  1)  the  constellation  of  Castor  and Pollux;  2)  the  third  sign  of  the  Zodiac.  —  L., ‘twins’,  specif,  ‘the  constellation  Castor  and Pollux’;  prob.  cogn.  with  OI.  yamah,  Avestic y'md,  ‘twin’,  Mir.  emon  (masc.),  emuin  (fern.), ‘pair  of  twins’.  These  words  possibly  derive  fr. I.-E.  base  *gem-,  ‘to  press’,  whence  also  Gk. yepieiv,  ‘to  be  pregnant,  to  be  full  of’,  Mir. gemel,  W.  gefyn,  ‘fetter’.  Gk.  yapEiv,  ‘to  marry’, is  not  cogn.  with  L.  geminus.  Cp.  gemel,  tri- geminous.
```


## [2026-10-17T00:33:16.614Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'yeast,  n\\|^yeast\\|eczema,  n\\|zeolite,  n\\|^Ymir\\|Yima' KLN_1966.txt | cut -c1-700 | head"
}
```


### [2026-10-17T00:33:16.950Z] TOOL RESULT

```
12625:ectro-,  combining  form  denoting  congenital  ab¬ sence  (med.)  —  Fr.  Gk.  Exxpaxric,  ‘miscarriage’, fr.  EXTixpcoaxetv,  ‘to  miscarry’,  fr.  ex  (see  ec-) and  TixpdxrxEiv,  ‘to  wound,  hurt,  injure’.  See throw  and  cp.  words  there  referred  to. ecu,  n.,  an  old  French  silver  coin.  —  F.,  fr.  OF. escu,  fr.  L.  scutum,  ‘shield’.  See  scutum  and  cp. escudo.  The  coin  was  called  ecu  (‘shield’)  from the  coins  issued  under  Louis  IX,  which  had  the shield  of  France  as  device, ecumenic,  ecumenical,  adj.,  general,  universal.  — Late  L.  oecumenicus,  fr.  Gk.  oixoup.Evrxoc,  ‘open to  the  whole  world’,  fr.  oixoupivr]  (scil.  yt)), ‘the
33437:yeasts  (bot.)  —  ModL.,  lit.  ‘sugar  fungi’  (see saccharo-  and  -myces),  prop,  a  loan  translation of  G.  Zuckerpilz,  a  name  given  to  yeast  by Theodor  Schwann  (1810-82).  See  C.  C.  Mettler, History  of  Medicine,  Philadelphia  -  Toronto, 1947,  p.  261.
```


## [2026-10-17T00:33:20.068Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i '.\\{0,50\\}eczema,  n.\\{0,500\\}' KLN_1966.txt | head -2; grep -o -i 'yeast,  n.\\{0,700\\}' KLN_1966.txt | head -2; grep -o -i 'zeolite,  n.\\{0,400\\}' KLN_1966.txt | head; grep -o -i '.\\{0,20\\}Yima.\\{0,300\\}' KLN_1966.txt | head -3"
}
```


### [2026-10-17T00:33:28.793Z] TOOL RESULT

```
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,500}
                            \___exceeds complexity limits
```


## [2026-10-17T00:33:35.445Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read()\npages=t.split('\\f')\nfor pat in ['eczema,  n','eczema, n','yeast,  n','yeast, n','zeolite,','Yima','Jamshid','zeal,  n']:\n  for i,p in enumerate(pages):\n    for m in re.finditer(re.escape(pat),p):\n      print('LEAF',i,pat,'::',p[m.start():m.start()+600].replace('\\n',' '));print()\nE"
}
```


### [2026-10-17T00:33:35.980Z] TOOL RESULT

```
LEAF 272 eczema,  n :: eczema,  n.,  inflammatory  disease  of  the  skin (med.)  —  Medical  L„  fr.  Gk.  gx^Efia,  prop, ‘something  thrown  out  by  heat’,  fr.  ix  (see  ec-) and  £e[zx,  ‘that  which  is  boiled’,  fr.  I.-E.  base *yes-,  ‘to  boil,  seethe’.  See  yeast  and  cp.  the first  element  in  zeolite  and  the  second  element in  apozem. eczematous,  adj.,  of  the  nature  of  eczema.  — Formed  with  suff.  -ous  fr.  Gk.  Ix^epta,  gen. ExCeptaxoc.  See  prec.  word. -ed,  1)  pp.  suff.  of  weak  verbs  in  English;  2)  used also  to  form  adjectives:  a)  from  nouns,  as  in cultured;
```


## [2026-10-17T00:33:40.033Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor fn in ['KLN_1966.txt','KLN_1971.txt']:\n  t=open(fn,encoding='utf-8',errors='ignore').read()\n  pages=t.split('\\f'); print(fn,len(pages))\n  for i,p in enumerate(pages):\n    for pat in ['yeast','zeolite','Yima','yima','Jamsh']:\n      for m in re.finditer(pat,p):\n        print(fn,'LEAF',i,pat,'::',p[max(0,m.start()-100):m.start()+400].replace('\\n',' '));print()\nE"
}
```


### [2026-10-17T00:33:40.564Z] TOOL RESULT

```
KLN_1966.txt 903
KLN_1966.txt LEAF 48 zeolite ::   to,  or  connected  with,  the anus.  See  anus  and  adj.  suff.  -al. analcite,  n.,  a  white  zeolite  (mineral.)  —  Formed with  subst.  suff.  -ite  fr.  Gk.  dvaXx-fc,  ‘weak, feeble’,  fr.  dv-  (see  priv.  pref.  an-)  and  dXxr), ‘protection,  help,  strength’;  so  called  in  allusion to  the  weak  electricity  it  acquires  when  rubbed. Gk.  dXxfj  is  rel.  to  dXsxE'.v,  ‘to  ward  off’, whence  the  desiderative  verb  dXl'Eiv,  ‘to  ward off,  keep  off,  turn  away,  defe

KLN_1966.txt LEAF 65 zeolite :: m,  acc.  of  ardor,  ‘heat’, fr.  ardere,  ‘to  burn'.  See  ardent  and  -or. arduinite,  n.,  a  zeolite  (mineral.)  —  Named  after the  Venetian  geologist  Giovanni  Arduino.  For the  ending  see  subst.  suff.  -ite. arduous,  adj.  —  L.  arduus,  ‘high,  lofty,  steep  ,  fr. I.-E.  base  *eredh-,  * erdh -,  'to  grow;  high’, whence  also  Avestic  er*dva-,  'high',  Olr.  ard, ‘high’,  Alb.  rit,  OSlav.  rastp,  ‘I  grow’.  Cp.  I.-E. base  *weredh-,  ‘to  grow;  high’,  whence  O

KLN_1966.txt LEAF 89 yeast ::   cp.  barn, barton.  For  the  second  element  see  adj.  suff.  -ly and  like,  adj. barm,  n.,  yeast.  —  ME.  berme,  fr.  OE.  beorma, rel.  to  Du.  berm,  MLG.  berm,  barm,  LG.  barme (whence  G.  Barme),  and  cogn.  with  L.  fermen- tum,  �

KLN_1966.txt LEAF 272 yeast ::   ec-) and  £e[zx,  ‘that  which  is  boiled’,  fr.  I.-E.  base *yes-,  ‘to  boil,  seethe’.  See  yeast  and  cp.  the first  element  in  zeolite  and  the  second  element in  apozem. eczematous,  adj.,  of  the  nature  of  eczema.  — Formed  with  suff.  -ous  fr.  Gk.  Ix^epta,  gen. ExCeptaxoc.  See  prec.  word. -ed,  1)  pp.  suff.  of  weak  verbs  in  English;  2)  used also  to  form  adjectives:  a)  from  nouns,  as  in cultured;  b)  from  other  adjectives  ending  in  -ate (der

KLN_1966.txt LEAF 272 zeolite :: led’,  fr.  I.-E.  base *yes-,  ‘to  boil,  seethe’.  See  yeast  and  cp.  the first  element  in  zeolite  and  the  second  element in  apozem. eczematous,  adj.,  of  the  nature  of  eczema.  — Formed  with  suff.  -ous  fr.  Gk.  Ix^epta,  gen. ExCeptaxoc.  See  prec.  word. -ed,  1)  pp.  suff.  of  weak  verbs  in  English;  2)  used also  to  form  adjectives:  a)  from  nouns,  as  in cultured;  b)  from  other  adjectives  ending  in  -ate (derived  from  L.  pp.s  in  -atus),  as  in

KLN_1966.txt LEAF 292 yeast :: .  Cp. also  organ,  orgy. crgosterol,  n„  an  alcohol,  C28H440,  occurring  esp. in  ergot  and  yeast  ( biochem .)  —  Compounded of  ergot  and  sterol. ergot,  n.,  a  disease  of  cereals  caused  by  a  fungus (pathol.)  —  F.,  fr.  OF.  argos,  argot,  lit.  ‘a  cock’s spur’;  of  unknown  origin, ergoted,  adj.,  infected  with  ergot.  —  Formed  fr. ergot  with  suff.  -ed. ergotin,  ergotine,  n.,  an  extract  of  ergot  (pharm.) —  Formed  fr.  ergot  with  chem.  suff.  -in. er

KLN_1966.txt LEAF 361 zeolite ::   bom  of’,  fr.  yovo9,  ‘that which  is  begotten,  offspring’.  See  gono-. gonnardite,  n.,  a  zeolite  (mineral.)  —  Named  after the  French  mineralogist  Ferdinand  Gonnard , who  first  analyzed  it.  For  the  ending  see  subst. suff.  -ite. gonnof,  gonnoph,  also  ganef,  n.,  a  thief.  —  Yiddish ganef  fr.  Heb.  ganndbh  (in  Modem  Heb.  pro¬ nunciation  ganniv),  ‘thief’,  fr.  gandbh,  ‘he stole’.  See  gambit. gono-,  before  a  vowel  gon-,  combining  form meaning  ‘sexu

KLN_1966.txt LEAF 370 yeast ::  ‘to  ferment’  (tr.),  fr.  MHG.  jesen,  ‘to ferment’  (intr.),  fr.  OHG.  jesan,  of  s.m.  See yeast  and  cp.  the  second  element  in  kieselguhr. guidage,  n.,  r)  guidance:  2)  fee  for  guidance  tob- sol.)  -  A  hybrid  coined  fr.  guide  and  -age,  a suff.  of  Latin  origin. guidance,  n.  —  A  hybrid  coined  fr.  guide  and -ance,  a  suff.  of  Latin  origin, guide,  tr.  v.  —  ME.  gulden,  guyden,  gyden,  fr,  F. guider,  ‘to  guide,  lead,  conduct’,  refashioned — af

KLN_1966.txt LEAF 459 yeast :: ,  a  Russian  fermented  drink  made  from rye  or  barley.  —  Russ,  kvas,  fr.  OSlav.  kvasu, ‘yeast’,  which  is  cogn.  with  L.  caseus,  ‘cheese’. See  cheese,  ‘milk  curd’. kyanize,  tr.  v.,  to  preserve  wood  from  decay  by impregnating  it  with  corrosive  sublimate.  — Formed  with  suff.  -ize  from  the  name  of  John H.  Kyan  (1774-1850),  who  invented  this  process in  1832. kyle,  n.,  a  strait,  a  narrow  channel.  —  Gael.  caol. kymatology,  n.,  the  science  of

KLN_1966.txt LEAF 538 zeolite :: he  city  of  Babylon,  whence  also  the Babylonian  PN’s  Mardukea,  Marduka. mordenite,  n.,  a  zeolite  (mineral.)  —  Named  after Morden  in  Nova  Scotia.  For  the  ending  see subst.  suff.  -ite. mordent,  n.,  an  ornament  of  three  tones,  a  trill (mus.)  —  G.,  fr.  It.  mordente,  lit.  ‘biting’,  pres, part,  of  mordere,  fr.  VL.  "mordere,  correspond¬ ing  to  Classical  L.  mordere,  ‘to  bite’.  See  mor¬ dant  and  -ent. more,  adj.  —  ME.  more,  fr.  OE.  mara,  ‘la

KLN_1966.txt LEAF 728 yeast :: ro-,  combining  form.  —  See  sacchar-. Saccharomyces,  n.  pi.,  a  genus  of  fungi,  the 13/U- yeasts  (bot.)  —  ModL.,  lit.  ‘sugar  fungi’  (see saccharo-  and  -myces),  prop,  a  loan  translation of  G.  Zuckerpilz,  a  name  given  to  yeast  by Theodor  Schwann  (1810-82).  See  C.  C.  Mettler, History  of  Medicine,  Philadelphia  -  Toronto, 1947,  p.  261. saccharose,  n.,  cane  or  beet  sugar.  —  Formed  fr. Gk.  oaxyapov,  ‘sugar’  (see  sacchar-),  and  subst. suff.  -ose

KLN_1966.txt LEAF 728 yeast :: (see saccharo-  and  -myces),  prop,  a  loan  translation of  G.  Zuckerpilz,  a  name  given  to  yeast  by Theodor  Schwann  (1810-82).  See  C.  C.  Mettler, History  of  Medicine,  Philadelphia  -  Toronto, 1947,  p.  261. saccharose,  n.,  cane  or  beet  sugar.  —  Formed  fr. Gk.  oaxyapov,  ‘sugar’  (see  sacchar-),  and  subst. suff.  -ose. sacciform,  adj.,  sack-shaped.  —  Compounded  of L.  saccus ,  ‘sack,  bag’  and  forma,  ‘form,  shape'. See  sack,  ‘bag’,  and  form,  n. sacc

KLN_1966.txt LEAF 804 zeolite :: biochem .)  —  Coined  fr.  stilbene,  estrvs  and  suff. -ol. stilbite,  n.,  a  mineral  of  the  zeolite  family, Na2CaAl2  Si60„.6H20.  —  A  word  coined  by  the French  mineralogist  Abb6  Rene-Just  Haiiy (1743-1822)  in  1796  fr.  Gk.  axlXpsiv,  ‘to  glitter’; so  called  by  him  because  of  its  luster.  Gk. axLXjDetv  is  rel.  to  nxtXirv6?,  ‘glittering’,  and prob.  cogn.  with  OIr.  sell,  ‘eye’,  sellaim,  ‘I  re¬ gard,  consider’.  For  the  ending  see  subst.  suff. -ite.

KLN_1966.txt LEAF 865 yeast ::   -ous. Derivatives:  torturous-ly,  adv.,  torturous-ttess, n. torula,  n.,  1)  any  of  certain  yeasts;  2)  (cap.)  a genus  of  fungi  (bot.)  —  ModL.,  fr.  L.  torulus,  ‘a little  elevation;  muscle,  brawn;  tuft’,  dimin.  of torus.  See  torus  and  -ule. torulifonn,  adj.,  resembling  a  torula.  —  Com¬ pounded  of  ModL.  torula  and  L.  forma,  form, shape’.  See  prec.  word  and  form,  n. torus,  n.,  1)  a  round  convex  molding  ( archil .);  2) a  protuberance  (amt.) ;

KLN_1971.txt 1
KLN_1971.txt LEAF 0 yeast :: rrage, and cp. barn,  barton. For the second element see adj. suff. -ly  and like, adj.   barm, n., yeast. — ME. berme , fr. OE. beorma ,  rel. to Du. berm, MLG. berm , barm, LG. barme  (whence G. Barme), and cogn. with L. fermen-  tum, ‘substance causing fermentation’, fr. I.-E.  base *bher~, ‘to boil, seethe’, whence also OI.  bhurati , ‘moves convulsively, quivers’, Mir.  berbaim , ‘I boil, seethe’. Cp. brand, bread, brew,  broil (in both senses), broth. Cp. also ferment.   bar mitzvah, a mal

KLN_1971.txt LEAF 0 yeast ::  heat’, fr. lx (see ec-)  and ‘that which is boiled’, fr. I.-E. base  *yes-, ‘to boil, seethe’. See yeast and cp. the  first element in zeolite and the second element  in apozem.   eczematous, adj., of the nature of eczema. —  Formed with suff. -011s fr. Gk. £x£ep ia, gen.  hx^luoLxoc. See prec. word.   -ed, 1) pp. suff. of weak verbs in English; 2) used  also to form adjectives: a) from nouns, as in  cultured; b ) from other adjectives ending in -ate  (derived from L. pp.s in -at us), as in fol

KLN_1971.txt LEAF 0 yeast :: , theurgy. Cp.  also organ, orgy.   ergosterol, n., an alcohol, QkHmO, occurring esp.  in ergot and yeast (biochem.) — Compounded  of ergot and sterol.   ergot, n., a disease of cereals caused by a fungus  (pat hoi.) — F., fr. OF. argos, argot, lit. ‘a cock’s  spur’; of unknown origin,  ergoted, adj., infected with ergot. — Formed fr,  ergot with suff. -ed.   ergotin, ergotine, n., an extract of ergot (pharm.)   — Formed fr. ergot with chem. suff. -in.  ergotism, n., disease contracted by eating

KLN_1971.txt LEAF 0 yeast ::   G. garen, ‘to ferment’ (tr.), fr. MHG. jesen, ‘to  ferment’ (intr.), fr. OHG. jesan, of s.m. See  yeast and cp. the second element in kieselguhr.  guidagc, n., i) guidance; 2) fee for guidance (ob-  sol.) — A hybrid coined fr. guide and -age, a  suff. of Latin origin.   guidance, n. — A hybrid coined fr. guide and  -ance, a sulT. of Latin origin,  guide, tr. v. — ME. guiden , guyden , gyden, fr. F.  guider , ‘to guide, lead, conduct’, refashioned—  after the noun guide — fr. OF. guier (whence 

KLN_1971.txt LEAF 0 yeast :: ,  kvass, n., a Russian fermented drink made from  rye or barley. — Russ, kvas, fr. OSlav. kvasu,  ‘yeast’, which is cogn. with L. caseus , ‘cheese’.  See cheese, ‘milk curd’.   kyanize, tr. v., to preserve wood from decay by  impregnating it with corrosive sublimate. —  Formed with suff. -ize from the name of John   H. Kyan (1774-1850), who invented this process  in 1832.   kyle, n., a strait, a narrow channel. — Gael, caol .  kymatology, n., the science of waves, — Com-  pounded of Gk. xujxa, 

KLN_1971.txt LEAF 0 yeast :: f. -ine.  saccharo-, combining form. — See sacchar-.  Saccharomyces, n. pi., a genus of fungi, the  yeasts (bot.) — ModL., lit. ‘sugar fungi’ (see  saccharo- and -myces), prop, a loan translation  of G. Zuckerpilz, a name given to yeast by  Theodor Schwann (1810-82). See C. C. Mettler,  History of Medicine, Philadelphia - Toronto,  1947, p. 261.   saccharose, n., cane or beet sugar. — Formed fr.  Gk. ad.xyct.gov, ‘sugar’ (see sacchar-), and subst.  suff. -ose.   sacciform, adj., sack-shaped. — C

KLN_1971.txt LEAF 0 yeast :: gar fungi’ (see  saccharo- and -myces), prop, a loan translation  of G. Zuckerpilz, a name given to yeast by  Theodor Schwann (1810-82). See C. C. Mettler,  History of Medicine, Philadelphia - Toronto,  1947, p. 261.   saccharose, n., cane or beet sugar. — Formed fr.  Gk. ad.xyct.gov, ‘sugar’ (see sacchar-), and subst.  suff. -ose.   sacciform, adj., sack-shaped. — Compounded of  L. saccus , ‘sack, bag’ and fotma, ‘form, shape’.  See sack, ‘bag’, and form, n.  saccule, n., a little bag. — L. sac

KLN_1971.txt LEAF 0 yeast ::  and -ous.   Derivatives: torturous-ly , adv., torturous-ness ,  n.   torula, n., 1) any of certain yeasts; 2) {cap.) a  genus of fungi {bot.) — ModL., fr. L. torulus, ‘a  little elevation; muscle, brawn; tuft’, dimin. of  torus. See torus and -ule.  toruliform, adj., resembling a torula. — Com-  pounded of ModL. torula and L. forma , ‘form.     shape’. See prec. word and form, n.  torus, n., 1) a round convex molding {archit.) ; 2)  a protuberance ( anat .); 3) receptacle of a flower  {bot.) — 

KLN_1971.txt LEAF 0 yeast :: ll,  ‘eager, zealous’. See yearn and full, adj.  Derivatives: yearnful-ly, adv., yearnful-ness, n.  yeast, n. — ME. yest, fr. OE. gist, giest , rel. to  ON. jastr, jostr, Swed. jast, Du. gist, ‘yeast’,  MHG. gestyjest, G. Gischt , ‘foam, froth’, OHG.  jesan, MH G. jesen, jem, gem, ‘to ferment’, G.  garen , ‘to ferment’ (tr.), and cogn. with OI.  yasyati , ‘it boils, seethes', Avestic yaeshyeiti ,  ‘boils, seethes’ (intr.), Toch. A yds-, ‘to seethe’.     Gk. £sTv, ‘to boil’, £673, ‘foam’, W. ias,

KLN_1971.txt LEAF 0 yeast :: , n.  yeast, n. — ME. yest, fr. OE. gist, giest , rel. to  ON. jastr, jostr, Swed. jast, Du. gist, ‘yeast’,  MHG. gestyjest, G. Gischt , ‘foam, froth’, OHG.  jesan, MH G. jesen, jem, gem, ‘to ferment’, G.  garen , ‘to ferment’ (tr.), and cogn. with OI.  yasyati , ‘it boils, seethes', Avestic yaeshyeiti ,  ‘boils, seethes’ (intr.), Toch. A yds-, ‘to seethe’.     Gk. £sTv, ‘to boil’, £673, ‘foam’, W. ias, ‘seeth-  ing, foaming’ (n.) All these words derive fr. I.-E.  base *yes-, ‘to boil, seethe’. 

KLN_1971.txt LEAF 0 yeast :: e words derive fr. I.-E.  base *yes-, ‘to boil, seethe’. Cp. eczema. Cp. also  guhr.   Derivatives: yeast-y, adj., yeast-i-ness , n.   yell, intr. and tr. v. — ME. yellen , fr. OE. giellan,  also gillan, ‘to yell, shout', rel. to ON. gjalla ,  Swed. gdlla, ‘to resound’, MDu. ghellen, Du.  gillen, OHG. gellan, MHG., G. gellen, ‘to yell’,  OHG., OS., OE. galan, ON. gala, ‘to sing’, OS.,  OHG. galm , ‘outcry’, ON. hana-gal, ‘cockcrow’,  ON. galdr, OE. gealdor, OHG. galtar, ‘song’,  ON. galend, ‘sor

KLN_1971.txt LEAF 0 yeast :: fr. I.-E.  base *yes-, ‘to boil, seethe’. Cp. eczema. Cp. also  guhr.   Derivatives: yeast-y, adj., yeast-i-ness , n.   yell, intr. and tr. v. — ME. yellen , fr. OE. giellan,  also gillan, ‘to yell, shout', rel. to ON. gjalla ,  Swed. gdlla, ‘to resound’, MDu. ghellen, Du.  gillen, OHG. gellan, MHG., G. gellen, ‘to yell’,  OHG., OS., OE. galan, ON. gala, ‘to sing’, OS.,  OHG. galm , ‘outcry’, ON. hana-gal, ‘cockcrow’,  ON. galdr, OE. gealdor, OHG. galtar, ‘song’,  ON. galend, ‘sorcerer’, lit. ‘s

KLN_1971.txt LEAF 0 yeast ::  Cronstedt (1722-65) fr. Gk. £eTv, ‘to  boil’, and XiO-o<; } ‘stone’ (see eczema and -lite  and cp. yeast) ; so called by him because it swells  up when heated.   Derivatives: zeolit-ic, adj., zeolit-ize , tr. v.,  zeolit-iz-ation, n.   Zephaniaji, 1) masc. PN.; 2) in the Bible, the  ninth in the order of the Twelve Prophets  (Bible). — Heb. Tz & phanyd k , lit. ‘the Lord has  hidden’. The first element of this compound  name derives fr. Heb. tzaphdn , ‘he has hidden’,  whence also tzdphon , ‘no

KLN_1971.txt LEAF 0 yeast :: oke together’. See  zygoma.   zym-, form of zymo- before a vowel,  zymase, n., an enzyme present in yeast (biochem.)  — Coined by the French physician and chemist  Pierre- Jacques Antoine (1816-1908) in 1875 fr.  Gk. Cu(nrj (see next word) and suff. -ase.  zyme, n., ferment (med.) — Gk. ‘leaven,   ferment’, (for I.-E. *yus-md), rel. to Gk.   ‘broth’ (prob. for I.-E. *yo(u)smos), fr. I.-E.  base *yus-y whence also OI. yu$-, ‘broth’, L.  jus, ‘broth, soup’; see juice and cp. zymosis,  zymurgy, azy

KLN_1971.txt LEAF 0 yeast :: ation’, fr. ^ujxouv, ‘to fer-  ment’ fr. See zyme and -osis.  zymosterol, n., a sterol occurring in yeast (bio-  chem.) — Formed fr. zymo- and sterol,  zymotic, adj., pertaining to, or causing, fermen-  tation. — Gk. ‘causing to ferment’,   fr. CupzcoTos, ‘fermented’, verbal adj. of ^ujxouv.  See prec. word and -otic,  zymurgy, n., that branch of chemistry which  deals with wine making and brewing. — Com-  pounded of Gk. vjpiY], ‘leaven’, and -oopyia,  ‘a working’. Cp. ^ufzoupy6<;, ‘maker of lea

KLN_1971.txt LEAF 0 zeolite :: ., pertaining to, or connected with, the  anus. See anus and adj. suff. -al.  analcite, n., a white zeolite (mineral.) — Formed  with subst. suff. -ite fr. Gk. AvaXx^s, ‘weak,  feeble’, fr. av- (see priv. pref. an-) and aXx^j,  ‘protection, help, strength’; so called in allusion  to the weak electricity it acquires when rubbed.  Gk. AXxtj is rel. to AX6xav, ‘to ward off’,  whence the desiderative verb dXe£eiv, ‘to ward  off, keep off, turn away, defend, protect’. See  Alexander.   analectic, adj

KLN_1971.txt LEAF 0 zeolite ::  L. ardorem , acc. of ardor , ‘heat’,  fr. ardere , To burn’. See ardent and -or.  arduinlte, n., a zeolite (mineral.) — Named after  the Venetian geologist Giovanni Arduino. For  the ending see subst. suff. -ite.  arduous, adj. — L. arduus , ‘high, lofty, steep*, fr.  I.-E. base *eredh -, *erdh-. To grow; high’,     whence also Avestic' *r*dva~, ‘high’, OIr. ard,  ‘high*. Alb. rit, OSlav. rastg , ‘I grow*. Cp. I.-E.  base *weredh-. To grow; high’, whence OI.  urdhvdh, ‘high’, vdrdhatS, ‘causes 

KLN_1971.txt LEAF 0 zeolite :: which is boiled’, fr. I.-E. base  *yes-, ‘to boil, seethe’. See yeast and cp. the  first element in zeolite and the second element  in apozem.   eczematous, adj., of the nature of eczema. —  Formed with suff. -011s fr. Gk. £x£ep ia, gen.  hx^luoLxoc. See prec. word.   -ed, 1) pp. suff. of weak verbs in English; 2) used  also to form adjectives: a) from nouns, as in  cultured; b ) from other adjectives ending in -ate  (derived from L. pp.s in -at us), as in foliated ,  dentated. — ME. -ed, fr. OE

KLN_1971.txt LEAF 0 zeolite ::  producing; bom of’, fr. y6vo;, ‘that  which is begotten, offspring’. See gono-.  gonnardite, n., a zeolite (mineral.) — Named after  the French mineralogist Ferdinand Gonnard ,  who first analyzed it. For the ending see subst.  suff. -ite.   gonnof, gonnoph, also ganef, n., a thief. — Yiddish  ganef, fr. Heb. ganndbh (in Modern Heb. pro-  nunciation ganndv ), ‘thief’, fr. ganabh , ‘he  stole’. See gambit   gono-, before a vowel gon-, combining form  meaning ‘sexual, reproductive’. — Gk. yovo-, 

KLN_1971.txt LEAF 0 zeolite ::  god of the city of Babylon, whence also the  Babylonian PN’s Mardukea , Marduka.  mordenite, n., a zeolite (mineral.) — Named after  Morden in Nova Scotia. For the ending see  subst. suff. -ite.   mordent, n., an ornament of three tones, a trill  (mus.) — G., fr. It. mordente , lit. ‘biting’, pres,  part, of mordere, fr. VL. *mordere, correspond-  ing to Classical L. mordere, ‘to bite’. See mor-  dant and -ent.   more, adj. — ME. more, fr. OE. mqra, ‘larger,  greater, more’ (used as compar. of 

KLN_1971.txt LEAF 0 zeolite :: H 20 O 2  (biochem.) — Coined fr. stilbene, estnis and suff.  -ol.   stilbite, n., a mineral of the zeolite family,  Na 2 CaAl 2 Si 6 0 lfl .6H 2 0. — A word coined by the  French mineralogist Abb6 Rene- Just Haiiy  (1743-1822) in 1796 fr. Gk. ox(X{3eiv, ‘to glitter’ ;  so called by him because of its luster. Gk.  ox(Xf3eiv is rel. to cttiX7tv 6<;, ‘glittering’, and  prob. cogn. with OIr. sell, ‘eye’, sellaim , T re-  gard, consider’. For the ending see subst. suff.  -ite. Cp. Astif be.   stile,

KLN_1971.txt LEAF 0 zeolite :: ,  ‘he overpowers, oppresses’, jdyati , ‘he van-  quishes, conquers’, jaydh , ‘victory’. Cp. Jain,  zeolite, n., hydrous silicate formed in igneous  rocks (mineral.) — ModL. zeolites, lit. ‘boiling  stone’, coined by the Swedish mineralogist Axel  Fredric Cronstedt (1722-65) fr. Gk. £eTv, ‘to  boil’, and XiO-o<; } ‘stone’ (see eczema and -lite  and cp. yeast) ; so called by him because it swells  up when heated.   Derivatives: zeolit-ic, adj., zeolit-ize , tr. v.,  zeolit-iz-ation, n.   Zephania

KLN_1971.txt LEAF 0 zeolite :: h , ‘victory’. Cp. Jain,  zeolite, n., hydrous silicate formed in igneous  rocks (mineral.) — ModL. zeolites, lit. ‘boiling  stone’, coined by the Swedish mineralogist Axel  Fredric Cronstedt (1722-65) fr. Gk. £eTv, ‘to  boil’, and XiO-o<; } ‘stone’ (see eczema and -lite  and cp. yeast) ; so called by him because it swells  up when heated.   Derivatives: zeolit-ic, adj., zeolit-ize , tr. v.,  zeolit-iz-ation, n.   Zephaniaji, 1) masc. PN.; 2) in the Bible, the  ninth in the order of the Twelve P

KLN_1971.txt LEAF 0 Yima :: ly cogn. with L. red-imio, -ire, ‘to  wreathe round’, redimiculum, ‘band, fillet, front-  let’. Cp, Yima.   yamen, n., in China, official residence. — Chin.,  ‘office’, lit. ‘gate with flags’, fr. ya, ‘flag’, and  men, ‘gate’ ; so called from the flags placed be-  fore official buildings. Cp. Tsung-li-yamen.  yammer, intr. v., to lament (colloq.) — ME.  yameren , alteration of ME. yomeren, fr. OE.  geomerian, geomrian , ‘to mourn, complain’,  which is rel. to OE. geomor , OS. jamar , ‘sad,  sorr

KLN_1971.txt LEAF 0 Yima ::  adj., yield-ing-ly,  adv.   Yiroa, n., the Avestic equivalent of Yama (Persian  mythol.) — Avestic Yima-, rel. to OI. Yamah.  See Yama.   -yl, combining form used to form the names of  chemical radicals. — F. - yle , fr. G. -yl, fr. Gk.  ua7j, ‘wood, forest; material, matter’, which is      YLANG-YLANG     838     of uncertain origin; cp. hylo-, odyl. The term -yl  was introduced into chemistry by the German  chemists Justus Liebig (1803-73) and Friedrich  Wohler (1800-82) in 1832, when they co
```


## [2026-10-17T00:33:44.153Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('KLN_1971.txt',encoding='utf-8',errors='ignore').read()\ni=t.find('Cp, Yima.'); print(t[i-900:i+20])\nE"
}
```


### [2026-10-17T00:33:44.567Z] TOOL RESULT

```
yv 6 <;, ‘holy, chaste’. See hagio- and cp. 
Yasna. 

yak, n., wild ox of Tibet and Central Asia. — 
Tibetan gyak. 

yaksha, n., a class of divine beings, the gods of 
wealth ( Hindu mythol.) -— OI. yakfdft, rel. to 
yak$ati, ‘he reveres, honors', which is prob. a 
a -enlargement of yajati , ‘he worships’. See 
Yajna. 

yam, n., 1 ) the edible root of several tropical 
climbing plants of the genus Dioscorea; 2) any 
of these plants. — Port, inhame, lit. ‘edible’ 
(with reference to the edible root), fr. Senegal 
nyami , ‘to eat’. 

Yaraa, n., the first of men that died, the judge of 
the dead (Hindu mythol.) — OI. Yamrih, of un- 
certain origin. It means perh. lit. ‘the restrainer’, 
fr. OI. yamah , ‘rein, bridle’, and is rel. to 
yamati, yacchati, ‘holds together, reins in, curbs’ 
and possibly cogn. with L. red-imio, -ire, ‘to 
wreathe round’, redimiculum, ‘band, fillet, front- 
let’. Cp, Yima. 

yamen, n
```


## [2026-10-17T00:33:54.937Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:587 BQT:571 BQT:2412; do echo \"######## $r\"; timeout 300 python3 tools/ref_page.py $r 2>&1 | head -150; done"
}
```


### [2026-10-17T00:34:02.219Z] TOOL RESULT

```
######## BQT:587
no scan of BQT covers printed page 587 (see 'scans' in refs_online.json)
######## BQT:571
no scan of BQT covers printed page 571 (see 'scans' in refs_online.json)
######## BQT:2412
(no exact page map; using offset -1917 -> pdf page 495; check the printed number and re-run with --pdf-page if off)
REF: BQT:2412  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 495  OCR-lang: fas

باختن -4۱۳-<

و زمیتی را کوبند که سلاطین در وجه ممیشت دیگر - و بمعنی خجره که آن خانه است9 -
اریاب استحقاق وغیره دهند و بتر کی سیورشال | وخمره که خم كوچك باشد هم هست9 - و شیه
خوانند۱ .4 ونظیر ومانند را نیز گوبنده .

یاخْض - بروزن ساختن, بمعتی پبرون یاخقی؟ « بروزن‌ساختی, ماضی‌باختن
کنیدن باعد مطلقاً وبرآوردن تیغ ازغلاف؟ - ۱ باشد بمنی‌تیغ‌را بیرون کشید - وقصد کرد واراده
ویممتی‌زدن‌وانداختن- و آشکارا کردن- وپرسیدن | انمود- وانداخت - وزد- وآشکارا نمود- ویمعنی
وسوال نمودن هم هست۴ . بیرون می‌کشید ومی انداخت وقسد میکرد هم

پاخعه؟ - بروزن ساخته, بممنی‌بیرون | هت - وبمعنی مخاطب هم آمده است پمنی نو
آشدیده باشد اعم ازآنکه شمشیروتیخ را ازفلای | بیرون کشیدی ولوقسد کردی وتو انداختی .
بیرون کعیده باشند با چیزی دیگر وا از جای یا۷۵ - براوزن شاد » معروف است که

. ‏.کمترین بابری ز احانت ملك ففقور وقیصر ورای امت‎ ٩

ملی غطرنجی «جهانگیری».

- آختن (.م.) " بازیسن (ه .( ۰

هیان تنگه خون ربختن را بست ببهرام آذر مهان یافت دمت .
فردوسی طوسی «شاهنامةٌ بخ ج۸ ۰۲۵۷۶

۴ - درجهانگیری ووشیدی وانجمن‌آرا بمعانی اخیر لیامده .

۴ - اسم مفعول «یاختن» . 8.- درجهانگیری بهمین معنی آمده و رشیدی ازو
فقل کرده است. ‎٩‏ - این صورت هم سوم شخص مفرد (مفرد مغایب) ماضی «باخت» است
با «ی» استمراری بعنی می‌کنید » وهم دوم دخص مفرد (مفرد مخاطب) بعنی توکشیدی .

۷ - اوستا- 9218 (حافظه). پهلوی )2لا. 2221 «اسدق۱۱۱۹. بادداشتن» ازبرداشتن
و بخاطر نگاه داشتن «بیرولی التفهیم ص۸۹> ور4: مقدمةٌ التفهیم ص قفه . - بادکرفتن » بخاطر
سهردن: «اين را یا دگرفتیم وحر ز کردیم.» «بیرونی. النفهیم. مقدمه ص‌قفه > - باد دادن» تملیم ۰
آموختن .

ن بالاقای < باناغان ۳ پتغان(بتفان)[ بفتم‌اول و وی ۹
سوم ]نرکی, که‌درفرانوی818888ل کردیده؛نومی‌خنجر سص وه
متحن ی که ترکان درجنگه بکار می‌بردند . - امروزه بحلقهٌ
فلزی ماغینما اطلاق شود که میله‌ای در درون آدست .۰ باتاقان

با - پپلوی 81۷20 « ابراهامیان » راهنمای زبان پپلوی س 4۱ ۰ پازند 8180
«باروچا ص0۹ 4* ور4: اسشق 1019۱۱۱۸؛ حرف عطف است که درجمله تردید واتخاب واختیاررا
رساند» گاه یکبار درجمله آید: کی که میاآید حن امت با حین» وگاه مکررشود: اي ن کتاب
با تألیف افلاطون است با ارسطو .- وگاه با پرسردو جملةٌ متشاد بامتباین آید (یتکرار) :

پا بزرگی و عزولعمت و جاه با چو مردانت مر که رویاروی .

: حنظلةٌ بادفیمی «یرکزیده ش ج۱ ص۰۱ .

با مکن با پیلبالان دوستی با بناکن خانهای درخورد پیل .
```


## [2026-10-17T00:34:07.940Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; command ls BQT | grep -i '2412\\|2413'; command ls MON* 2>/dev/null | head; grep -n -A3 '\"BQT\"' ../../refs_online.json | grep -i scans | head -2; python3 -c \"\nimport json;d=json.load(open('../../refs_online.json'));print(d['BQT'].get('scans'));print(d.get('MON',{}).get('scans'))\""
}
```


### [2026-10-17T00:34:08.345Z] TOOL RESULT

```
2412.png
2412.txt
(eval):1: no matches found: MON*
5-  "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
None
```


## [2026-10-17T00:34:11.892Z] TOOL CALL #39: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2412.png"
}
```


### [2026-10-17T00:34:12.413Z] TOOL RESULT

```

```


## [2026-10-17T00:34:12.408Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:34:22.826Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 2412.vision.txt <<'E'\n[BQT vol 4, printed p. ۲۴۱۲ (pdf 495) — read from page image]\nیاد ۷ - بروزن شاد ، معروف است که ... (continues next page)\nfootnote ۷ - اوستا yâta (حافظه)، پهلوی yât ، âyât «اسشق ۱۱۱۹». یادداشتن، ازبرداشتن و بخاطر نگاه داشتن «بیرونی التفهیم ص۸۹» ورک: مقدمهٔ التفهیم ص قفه . - یادگرفتن، بخاطر سپردن: «این را یادگرفتیم وحرز کردیم.» «بیرونی. التفهیم. مقدمه ص قفه» - یاد دادن، تعلیم، آموختن.\nE\ncd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nfor fn in ['BQT_v2_pages.txt']:\n  pages=open(fn,encoding='utf-8',errors='ignore').read().split('\\f')\n  for i in range(20,60):\n    p=pages[i]\n    for pat in ['جمشید','جستن','جهیدن','yima','Yima','yah','jastan','yam']:\n      if pat in p: print(i,pat)\nE"
}
```


### [2026-10-17T00:34:23.213Z] TOOL RESULT

```
42 جمشید
45 جمشید
46 جمشید
```


## [2026-10-17T00:34:30.640Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in [42,44,45]:\n  p=pages[i]\n  print('=====LEAF',i, p[:150].replace('\\n',' '))\n  for line in p.split('\\n'):\n    if any(k in line for k in ['جمشید','جم ','اوستا','yim','yam','jam','Yim']): print('  ',line[:300])\nfor i in range(22,36):\n  p=pages[i]\n  if 'جست' in p or 'جهید' in p:\n    print('=====LEAF',i,p[:100].replace('\\n',' '))\n    for line in p.split('\\n'):\n      if 'جست' in line or 'جهید' in line or 'اوستا' in line: print('  ',line[:300])\nE"
}
```


### [2026-10-17T00:34:31.186Z] TOOL RESULT

```
=====LEAF 42                                        ‫بیان شدانهزم‬             ‫و هفت لغت و کنات‬             ‫در جيم آبجد با میم مشتمل رست‬  ‫ابنیمع»نی | سلیمان ا
                                                                        ‫سا‬‫جم ‪ = ۲‬بت‬
   ‫وجمشید همهست ‪ . ۴‬لیکن درجایی که بانگین | میشود اسکندر ‪ -‬و بمعنی مردمك چشم هم‌بنظر‬
     ‫شبیه بود و ایرانان م رکز جمشید داستانی‌را کشور فاری‌مبداننته‌اند و آثاربافی ماندء داربوش‬
      ‫وخشیارشا ودیگر یادشاعان هخامنشی را بجم(جمتید) انتاب داده اند و نام «تخت جمشید» خود‬
      ‫یق=ه بکراول و" فتح پنجم » از ترکی از فرانه ‪ « 468‬محمد علی‬
=====LEAF 44  ‫‪“OAT‬‬                                                                              ‫جمد چیتی‬  ‫ثانی آب و در الث فیاتات وعرب اخگرآ شرا‬           
     ‫کفته‌اند که جم بمعتی‌جفت‌است ودهار بمعنی‌عذ کور» پس دربنصورت بمعنی دو دمه باشد واین‬
                     ‫‪ ۰.‬درسان کربت ‪ [۳200012‬مرک از ‪4۳ :‬ھز ( جم خ‬                          ‫اقرب است‬
=====LEAF 45   ‫سقف‬   ‫‪۳‬‬ ‫‪۰‬‬                                                                                         ‫وس‬                                    
   ‫واو در اول جم نام داشت یعنی ساطان‬                                                             ‫ج‬‫ج‬
   ‫ویادشاه‌بزر که ‪ ,‬و سبب‌جمشید کفتن آن شدکه‬       ‫»بیان قطه‌دار بروزن‬
   ‫که تخت مرصمی را در جای بلندی کتاشتند‬           ‫بگویند ‪ ۴‬و نامیس جمشید‬           ‫بصاجراماوحی‬
   ‫اینلفظ را برهجم» افزودند و جمشید گفتند یعنی‬      ‫وای‬         ‫یی ادارا‬           ‫کے کک کی‬
     ‫‪ - ۱‬از ‪ :‬جم ا(وستا ‪ , 20111۷‬ساسکریت (ودا) ‪ 21712۷۰‬پهلری‪ < 012۷‬بارتولمه‬
    ‫خا ‪,‬عنی جم درخشان ؛ جمدرکاتها بدون صفت دششه آمده « بنای ‪ » ۸ : ۲۳‬و جدها این‬
    ‫میکند ‪ ۰‬دارستانهای ملی ما نز آمده که مدت سبصدسالدرزمان جم بیماری وم که‌نبود يااو‬
     ‫کمراه شد وجهان بآرشفت و بیماری ومر که‌بازکشت‪« .‬شاهنامة فردوسی» بقول اوستا (وندیداد‪.‬‬
     ‫جم یکی از بکزتررین پادشاهان سلسلةٌپیشدادی است و در ادییات پارسی « جام جهان لما“ پدو‬
            ‫چه مايه بدو گوهر اسر شاخت‬                    ‫‪ -۷‬برکفیانی یتکخیت ساخت(جمشید)‬
=====LEAF 29    ‫جى‬   ‫جز لگ بنتح اول و انی و سکون‌کاف‪.‬‬                        ‫جزغال؟ س بکراول بروزن امثال‪,
                                                            ‫»ماض‬    ‫عبقتح اول بروزژهمست‬        ‫جست‪°‬‬
                                                                            ‫و جستجو کردن و بافتن " ‪۶.‬‬
      ‫از فن‌جدل » معرب آن نیزجست است ‪ :‬کان اما مافی فن‌الخلاف خصوصاً الجست وهواول من‌افرده‬
         ‫‪- ۸‬اوستا‪( 16۲۱۵۷) ۰ ۰ ۲۳0۵۵۷ -‬جنک کردن)‪ .‬هندی باسان الله‬
      ‫‪ ۵‬جستار ‪ -‬بضم اول » از ‪ :‬جت ‪ ۳‬آر (پسوند ساختن |سم از فعل )؛ بحث ‪ .‬مبحت ‪:‬‬
```


## [2026-10-17T00:34:39.094Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in range(25,31):\n  p=pages[i]\n  print('=====LEAF',i)\n  for line in p.split('\\n'):\n    if any(k in line for k in ['اوستا','جستن','جهیدن','جهید','بفتح اول بروزن بستن','yah']): print('  ',line.strip()[:250])\nE"
}
```


### [2026-10-17T00:34:39.499Z] TOOL RESULT

```
=====LEAF 25
=====LEAF 26
=====LEAF 27
=====LEAF 28
=====LEAF 29
   ‫‪- ۸‬اوستا‪( 16۲۱۵۷) ۰ ۰ ۲۳0۵۵۷ -‬جنک کردن)‪ .‬هندی باسان الله‬
=====LEAF 30
   ‫‪ ۴‬اوستا ‪ , 80۳537 .‬بهلوی ‪ [70152‬با ‪ ( 00152۷‬جشن ) « استق ‪١۲٤‬‏ »كل‪.‬مةٌ‬
   ‫اوستایی ‪ 2052‬وسان کرت ‪ 802۷‬و پپلوی ‪ 015228۷‬بمعنی ستایش و پرستش است‬
```


## [2026-10-17T00:34:44.110Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\npages=open('BQT_v2_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in [28,29]:\n  print('=====LEAF',i)\n  for line in pages[i].split('\\n'):\n    if line.strip(): print(line.strip()[:220])\nE"
}
```


### [2026-10-17T00:34:44.463Z] TOOL RESULT

```
=====LEAF 28
‫وبا وت‬                                                                                              ‫جر مه‬
‫لسره ‪ .‬للم دختر‬        ‫جرب ره » بر وزن‬               ‫بروزن ندیده ‪ .‬تنها وفردرا‬                  ‫جلره‬
‫پیران وبه است که زن سیاوش بوده و فرود‬                 ‫‪9.‬‬
‫مره‬   ‫و‬    ‫=‬     ‫و دفتررا هم گفته‌الد ‪۴‬‬   ‫‪-‬‬   ‫کو نتف ‪۱‬‬
‫پر اوست؟‬                               ‫گیوزمند ‪.‬‬
‫کوچك قلندران را ن‬
‫بیان هفتم‬
‫درجم آبچد با زایهوز مشتمل برهشت لغت‬
‫صفدر »‬       ‫=فتح اول بورزن‬
‫جز در ب‬                   ‫بفتح اول و سکون ثانی ‪| ۰‬‬                    ‫جز ‪-‬‬
‫جزا ست که دئبهٌ برشته کرده باشد ‪.‬‬           ‫نمعئی‬
‫کنار دربا و مان در بارا کونند ‪۴‬‬                   ‫جر مر‬
‫وبکر اول‌نیز همین معنی‌آمده است ؛ و جزدره‬             ‫و یکر اول دقبةٌ برشته شده باشد که برروی‬
‫‪۶#‬‬       ‫آش آرد رور تد‬
‫هم میگویند که بروزن مسخره باشد ‪.‬‬
‫ون‬
‫جزع = بکس اول وسالکىو‬
‫غین نقطه‌دار » بمعنی جزدر استدنکبهٌبرشته‬           ‫جانوری باشد سب رتککشبیه‌بملخ و بیسنگوند‬
‫آوزمرها و علف نج‬
‫که‬                        ‫که جنل ا‬
‫‪۰‬‬    ‫آرد ربزدد ‪۷‬‬     ‫کرده باشد که در رویآشهای‬
‫بیشیار مضزی لظر باز کن ‪.‬‬                      ‫‪eT‬‬
‫نظاعی کنجوی‪ «.‬کنجینه ‪ 5‬ی‬
‫سپاء‬     ‫‪,‬باوردی‌من‬
‫بیامد ب‬                         ‫‪ - ۴‬عرض با جریده بنزديك‌شاه‬
‫موار‬    ‫درمیان‬    ‫یاده بی‬                       ‫هزار‬      ‫شمار سیاه آمدش صد‬
‫«تاهنامة بخ ج ‪ ۸‬ص‪.*۸۵۲‬‬
‫چو بابد ترا (سیاوشرا)بنده‌بایدشمرد‬       ‫من(بیران) چهارندخرد‬              ‫‪ - ۴‬ررد‬
‫که از خورویان ندارد همال‪.‬‬                ‫مهتر سال‬          ‫است‬    ‫از امئان جر فره‬
‫«شاهنامةٌ بخ ج ‪ ۳‬ص ‪۰۱٩‬‏ ‪.‬‬
‫‪ - ۴‬باين معثی مخفف «جزبره» گرفته‌اند ومعقول بنظر نمیرسد ‪ .‬جز بفتح اول و شدید‬
‫دوم‬   ‫دوم ول مسجم البلدان قربهاست از اصفهان " ولف در فهر ست خود جز ( که‌گاه سشدید‬
‫امال دارا رمن باهر دانشة ‪:‬‬
‫بنخچیر پاید شدن سوی جز‬                         ‫چو ما مهرکانیبپوشیم خز‬
‫بادگاری کنیم‪...‬‬      ‫اون‬                           ‫مدان د شت نخچرکاری کنیم‬
‫شده چون لی ليزه بالای گز ‪.‬‬                          ‫میایان که من‌دیده ام زیر جز‬
‫‪۸۷‬ص‪۸۱۲-۹۷‬‏ ‪.‬‬
‫«شاحنامة بخ ج ‪٩‬‬
‫جز‪-‬ردگر» جزغ‪.‬‬
‫‪ - ۷‬رك ‪ :‬جزد» جزدر و جرغال‪.‬‬                 ‫و جرواك‪.‬‬       ‫رك ‪ :‬جراك‬       ‫‪-‬‬   ‫‪3‬‬
‫‪.‬‬    ‫از‬
‫ر‪.‬‬‫بای‬
‫غتثن‬
‫‪۹٤۲‬‏ »؛ کلم استثنا ‪,‬مکر» باس‬                   ‫ر)ك‬‫بم‬
‫ی( ه‬
‫«چدا‬
‫و‬
=====LEAF 29
‫جى‬
‫جز لگ بنتح اول و انی و سکون‌کاف‪.‬‬                        ‫جزغال؟ س بکراول بروزن امثال‪,‬‬
‫نام علتی ومرضی است که مرغان و پرندکانرا‬                 ‫روی `‬   ‫دلبةً برشته کرد‬   ‫که‬   ‫بمعنی جزغ است‬
‫آش باشد ‪۴‬‬
‫باستخوان سوراخ گردد ‪.‬‬
‫جز لذن = بروزن کزین » بمعنی‌تغییر‬                       ‫جزغال است که پارچهای دب برشته شده‬
‫و تبدیل باشد ‪. ۴‬‬                                                 ‫باشد ‪. ۴‬‬
‫بیان هشتم‬
‫در جیم آبجد باسین سعفص مشتمل برشش لغت‬
‫جسر و دا رو سر اختیارات ‪٩‬‏ بمعنی‬                       ‫زعفران را‬    ‫بر وزن فاد »‬           ‫جاد‬
‫خرودارو نوشته شده است که خولنجان باشد‬                  ‫کوبند و آنرا بعربی شمورالسقالبه با صاد وبای‬
‫و بعضی کوبند معرب خرو دارو است *‬                                                 ‫‪.‬‬   ‫خوانند‬   ‫اد‬
‫»ماض‬    ‫عبقتح اول بروزژهمست‬        ‫جست‪°‬‬
‫و کاف » محنت و رنج و بلارا گویند ‪.‬‬             ‫جتن و گریختن باشد و طم اول ماضی‌جتن‬
‫و جستجو کردن و بافتن " ‪۶.‬‬
‫جسمی د بفتح اول وسکون ثالی ومیم‬                            ‫‪۱‬‬           ‫ل‬          ‫‏‪E‬‬
‫خك‬‫» خار <‬   ‫«محتالی کشده‬        ‫بفتح ول بروزن بستن » بمعنی‬     ‫۔‬    ‫جسن‬
‫آن‬    ‫و‬   ‫را کونند ‪.‬‬
‫خاری باشد سه‬
‫رها شدن و خیز کردن و کرب ‪۱‬ختن باشد ‪- ۷‬‬
‫لو‬             ‫نا‬                  ‫و بم اول بممنی‌طلب لمودن و بافتن ‪. ۸‬‬
‫حر در‬      ‫رك ‪ :‬جرد‬    ‫‪- ۲‬‬              ‫آل ( پنوند ) ‪.‬‬         ‫‪ - ۱‬از ‪ :‬جزغ («‪.‬م ‪+).‬‬
‫فرهنك دسائیر ‪. ۱۶۲‬‬       ‫‪۴‬‬                  ‫غا‪:‬ل‪.‬‬
‫جزرك‬
‫‪۴‬‬                  ‫و جز غ‬
‫‪٩‬‏ ‪ -‬جت بمعنی‌تقحص و تجسی و همچنین شعبه‌است‬                              ‫‪.‬‬      ‫ن‬
‫ت‪.‬‬‫ج رك‬
‫‪۵‬‬
‫از فن‌جدل » معرب آن نیزجست است ‪ :‬کان اما مافی فن‌الخلاف خصوصاً الجست وهواول من‌افرده‬
‫ص‪.» ۶۹‬‬
‫بالتصنیف ‪ .‬ابن خلکان « دزی ج ‪٩‬‏ ‪۱‬‬
‫‪۷‬ق‪-‬ول هرن از ره هندی باستان ‪ ( 125۷, 2 52‬جوشیدن » فوران )»‬     ‫ب‬
‫‪ « ۳1/0201562 0۳1602‬اسعق*‪ .»۲4‬برك این اشتقاق‬  ‫‪( # ۵۵‬جوشیدن) ›‬    ‫اوتا ‪-‬‬
‫را تپذیرفته آرا از ‪ 2‬للا ‪( ۵‬انداختن) مشتق داند «یبرك ‪ .5۱۱6‬پهلوی ‪1484‬ز‬
‫با ‪ 780521‬بلوچی ‪( 82211‬فرار کردن) « اسشق *‪.۲4‬‬
‫‪- ۸‬اوستا‪( 16۲۱۵۷) ۰ ۰ ۲۳0۵۵۷ -‬جنک کردن)‪ .‬هندی باسان الله‬
‫طلز ‪ .‬بهلوی ع‪9(1)۵‬ز ‪ « ,‬استق‪٩۱1‬‏ › ‪.‬‬
‫‪-‬‬                          ‫‪1‬‬
‫‪ - 4‬مراد اختیادات بدیمی است ‪.‬رك ‪ :‬ص حشتاد وشش دقدمه ‪.‬‬
‫‪ - ۱‬اوسا ‪(86529 -‬ناخوشی)‬               ‫‪۰‬‬   ‫‪ ۰‬رك ‪ ۳‬خسرودارو‬     ‫مصحف‌خسروداروست‬         ‫‪۰‬‬
‫«سشق ‪. > ۱۲4‬‬  ‫پهلوی )‪54‬ل ا‬
‫‪ ۵‬جستار ‪ -‬بضم اول » از ‪ :‬جت ‪ ۳‬آر (پسوند ساختن |سم از فعل )؛ بحث ‪ .‬مبحت ‪:‬‬
‫سجتالی ص ‪.*4‬‬        ‫« چستار اول در دور کون چیزی از آفربد کار » «کات‬
```


## [2026-10-17T00:34:52.733Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; A=incoming/ARY/ARY_pages.txt; for w in 'یاد' 'جمشید' 'جستن' 'جهیدن' 'yem' 'yes-' 'jes-'; do echo \"## $w\"; grep -n -- \"$w\" $A | head -4 | cut -c1-200; done; grep -n -i 'YAD\\b\\|JAMSHID\\|JASTAN\\|JAHIDAN' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:34:53.089Z] TOOL RESULT

```
## یاد
112:کشاورزی و اهل‌سازی دام‌ها نو آوری شد و این نوآوری‌ها شهرزیستی و ازدیاد جمعیت و ایجاد
158:(8۸ظ۸ 283/7391818 ۸1۸1/1724) اگر حوزه‌ی گسترش یکه زبان زیاد شود» گویش‌های
233:اندیشه‌ی فوق را تأیید می‌کند: زبانهای ژرمنی همسانی‌های نسبتاً زیادی با زبان‌های واقع در باختر
234:خود (یعنی سلتی و لاتئین دارند). از سوی دیگر همین زبان‌های ژرمنی شباهت نسبتاً زیادی با
## جمشید
## جستن
## جهیدن
## yem
## yes-
## jes-
14674:(esl gail ya" aad’ pe 44) Gangs Gasilyad ys PERSIAN) yyubb
15321:HWYAD AGAULISH) SS (PAHLAVI) 63 shay
```


## [2026-10-17T00:34:58.784Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'اکزما' 'اگزما' 'زئولیت' 'دشیاد' 'دشیار'; do echo \"## $w\"; grep -h -- \"$w\" MON_part1.txt MON_part2.txt | head -3 | cut -c1-250; done; grep -n -i 'ayād\\|ayad\\|dušyād\\|dusyad\\|duš-ayād\\|dusayad\\|ayyad' SNS_pages.txt | head; grep -n -i 'duš-ayād\\|dušayād\\|dušāyād\\|dušyād' PHD.txt NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:34:59.246Z] TOOL RESULT

```
## اکزما
## اگزما
## زئولیت
## دشیاد
## دشیار
3304:                                                                  -A-T/n J             <oi|               luz.jl-iiU v^j-O'j-wW^                     (Tayadia. p. 116)     Ss**^:
4108:               /ya jl abi+yata- ;b-                         «>W:ayyad / ayad
5580:                               .«tf <jili<t>*j*Wj» :frayadarX*i«^«J
8110:                                                            (Tayadia, SnS.              p. 86. nl sj^) *«*k«Afe &r *W jjjj «r^
8161:                                                                                                        (Tayadia, p. 56                 :*%)   .d.^ nisSyet CifrfeV'jW
10709:           —* **<»'*": i72)wyc :;;;.;;"                                   -dtfW^Wf^'4^ rpayad:                         NTLWN,            t:>*    :    *>,>>*,
11739:                                                                                     Tay:      ^U. ^jlj^l^ 'JlrfW:ayad:                                    J
15838:                                                         spand 176/7                       stayad 178/6
15926:payad 268/21            pahlura ciS 114/14
16205:frayadar 129/9
```


## [2026-10-17T00:35:04.306Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4100,4112p SNS_pages.txt | cut -c1-250; grep -n 'dus\\|duš' SNS_pages.txt | grep -i 'ya' | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:35:04.613Z] TOOL RESULT

```
                                                                      6f-6T-6W1                          I't/T^.ub^.ts,: B t3v                                ,A
                                                                                                                                            .
                                      Uicu-^U^U^Ij
A6                                                                                                      g^rUjc^U^L 4jL
                                                                                                                                       AT

               /ya jl abi+yata- ;b-                         «>W:ayyad / ayad

     WW. 224-26) %'d: j* V*                                 «j>» (OTP*.
                                                                ;
                                                                               250)
16319:dast soy 187/19             der-zaraan 183/13            drayan javisnih 319/16     -dus 332/16
```


## [2026-10-17T00:35:14.789Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://abadis.ir/fatofa/دشیاد/' 'https://abadis.ir/fatofa/جستن/' 'https://abadis.ir/fatofa/اگزما/' 'https://abadis.ir/fatofa/جمشید/'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 564 Mo'in/Dehkhoda lookup\" 2>&1 | tail -1); echo \"## $u $f\"; grep -v '^\\s*$' $f | grep -m8 -i 'معین\\|دهخدا\\|اوستا\\|پهلوی\\|فر\\.\\|بدگو\\|غیبت' | cut -c1-300; done"
}
```


### [2026-10-17T00:35:20.553Z] TOOL RESULT

```
## https://abadis.ir/fatofa/دشیاد/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/ab7be8d54a3dae96.txt
 ( دش+یاد ) . از کسی بد یاد کردن. سخن بد روا یا نارو گفتن از کسی هنگامی که وی در آنجا نباشد. تازیان به آن غیبت می گویند. پیامبر گرامی در نکوهش آن فرموده اند دشیاد از زنا بدتر است
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده اس
## https://abadis.ir/fatofa/جستن/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/6544ba77a3b0a3ee.txt
 لغت نامه دهخدا
 جستن. [ ج ُ ت َ ] ( مص ) یافتن. ( بهارعجم ) ( آنندراج ) ( برهان ). یافتن و پیدا کردن. ( فرهنگ فارسی معین ). یافتن و گم کرده را پیدا کردن. ( ناظم الاطباء ). در تداول عوام ، یافتن و یافتن چیزی گمشده. ( یادداشت مؤلف ) : 
 || توده کردن و انباشتن. ( ناظم الاطباء ). || پرسیدن. استفسارکردن. امتحان کردن. ( ناظم الاطباء ). پرسیدن. ( فرهنگ فارسی معین ). تحقیق کردن : 
سلطان سعید بفرمود که او را بجویند تا هیچ کار دارد. گفتند ای خداوند او مردی پیر است پایها خوشیده می گوید خوابی دیده ام. ( راحةالصدور راوندی ). || تفتیش کردن و پرسیدن. ( ناظم الاطباء ) ( فرهنگ فارسی معین ). کاویدن از چیزی. پژوهیدن. از چیزی کاوش کردن. گردیدن. تفحص کردن. ( یادداشت مؤلف ) : 
 فرهنگ معین
 واژه جستن کاملا پارسی است ریشه پهلوی دارد در عربی می شود یتخطى این واژه یعنی جست صد درصد پارسی است. 
منبع. فرهنگ لغت معین
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده اس
## https://abadis.ir/fatofa/اگزما/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/3c58451d85121042.txt
 فرهنگ معین
 (اِ زِ ) [ فر. ] (اِ. ) نوعی بیماری جلدی که عوارض آن عبارت است از تورم پوست و سرخ شدن آن و بروز تاول های ریز که بعد از پوسته شدن خارش بسیار دارد و گاهی تاول ها آب پس می دهد. 
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده اس
## https://abadis.ir/fatofa/جمشید/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/4e36227bb3aadac1.txt
 لغت نامه دهخدا
 جمشید. [ ج َ ] ( اِخ ) نام پادشاهی است معروف که او را عربان منوشلخ گویند. وی در اول جم نام داشت یعنی سلطان و پادشاه بزرگ و سبب جمشید گفتن آن شد که او سیر عالم میکرد، چون به آذربایجان رسید روزی بود که آفتاب بنقطه اول حمل آمده بود، فرمود که تخت مرصعی را در جای بلندی گذاشتند و تاج مرصعی برسر نهاده بر 
 در ( ودا ) ( جم ) پسر خورشید و نخستین بشری است که مرگ بر او چیره شده بر دوزخ حکومت میکند . در داستانهای ملی ما نیز وی یکی از پادشاهان سلسله داستانی پیشدادی است بقول اوستا او نخستین کسی است که اهور مزدا دین خود بدو سپرد . در روایات ایرانی آمده که مدت سیصد سال در زمان جم بیماری و مرگ نبود تا او گمراه
 (یا: جَم) از شخصیت های اساطیری ایران و هند و از بزرگ ترین شاهان خداگونۀ پیشدادی، در شاهنامۀ فردوسی. اختراع بسیاری از چیزها را به او نسبت داده اند؛ و نیز او را واضع بسیاری از هنجارها و آیین ها و رفتارهای مدنی دانسته اند. در اَوِستا، یَمَه و در متون پَهلوی، یَمَک و جَمَک است. در اوستای متأخر، یکی از 
همانطور که در دانشنامه ایرانیکا نیز قید شده، استفاده از نام "یاما" دراوستایی ( یا "جم" در پارسی میانه ) برای دوقلوها بسیارمعمول بوده. جمشید خواهری دوقلو داشت و از اینرو او را Yima ( دوقلو ) و بعد ها دوقلوی روشن میخواندند که در پارسی میانه و فارسی نو تبدیل به "جمشید" شد و معنی لفظی یا ریشه ای "دوقلو"
 جمشید یا یمه ( به ایلامی: ت. ت.   'yamakšedda' ؛ به پارسی باستان: ت. ت.   'yama - xšaita' ؛ به اوستایی: 𐬫𐬌𐬨𐬀 ت. ت.   'یمه' ؛ به پارسی میانه: ت. ت.   'جَم' ) ، یکی از پادشاهانِ اساطیری ایرانی است و قدمتی بس کهن دارد. نام او در اوستا و نوشتارهای پهلوی و نوشتارهای دوران اسلامی آمده است. در اسطوره های 
جمشید در اوستا همان یِمه ( به انگلیسی:Yima ) پسر ویوَهوَنت ویوَنگهَنت ( ویونگهان ) است که با یَمه پسر ویوَسوَنت اساطیر هندی مطابقت دارد. بنا بر آوانویسی آندریاس ابن نام ها به گونه Yomo پسر Vihvohvont. خوانده می شود. نام او در اوستا به گونهٔ «ییمَ» ( یمه ) آمده است. واژهٔ جمشید از دو بهره ساخته شده ا
در فرهنگ واژه های اوستا در پی نام جمشید چنین آمده است: «جمشید: دوران تابندگی و درخشش زندگی آریاییان. زمان جمشید زمانی بود که در آن مردمان به زدن خشت و ساختن ایوان و گرمابه و شهر، جام ها و آوندهای سفالین، رشتن و بافتن ابریشم و کتان و پنبه، برآوردن گوهرها از دل سنگ، ساختن کشتی و بو و عطر و می و… دست ی
```


## [2026-10-17T00:35:25.535Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py IRN:5 2>&1 | grep -n 'جم\\|یم\\|همزاد\\|Yim\\|PDF' | head"
}
```


### [2026-10-17T00:35:30.944Z] TOOL RESULT

```
2:REF: IRN:5  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 16  OCR-lang: fas
16:حجمشهد 32612* ۷12 پمعنی توأٌم د رخشان که با خواهرش قا7 همزاد بود
18:افزا یش مردم و چارپایان بپردازد . همین جمشید در ادبیات باستانی هند نیز دیده
23:۲ در اوستا جمشید 3۸21۵: ۷10۵ پسر ویو نگهت ۷1۷۸121 سومین پادشاه جهان‌است
```


## [2026-10-17T00:35:39.758Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'ayād\\|NP yād\\|yād ' CHEUNG.txt | head; grep -n -i '\\*yam\\b\\|^\\*yam ' CHEUNG.txt | head -3"
}
```


### [2026-10-17T00:35:40.055Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:35:43.654Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'yad\\b\\|yäd\\|ayad' CHEUNG.txt | head; grep -n '^\\*[iy]̯\\?am\\|^\\*i̯am\\|^\\*yam\\|i̯ā ' CHEUNG.txt | head"
}
```


### [2026-10-17T00:35:44.001Z] TOOL RESULT

```
7458:dévár-/déwár- < *ati-bar'-) ‘to insert, introduce’ || (+ *à-) Sangl. oyoó, Ishk. dyad 
10843:amé(y)) ‘to come’ || (+ *upa-) NP bayad, Gil. (Rsht.) va ‘must [mod. aux.]’, Ard. 
12048:remember [intr.]’, BMP ’dyb’tyn- /ayaden-/ (sec. caus.) ‘to remember’ = DMMPP: 
12052:BMP ’dyb’tynyt /ayadénid/ 
12065:*NWIR: (+ *abi-) NP yad ‘memory, remembrance’, widely borrowed (e.g. in Bal. yat, 
12066:Kurd., Qohr. yad) 
14462:pry’d-, BMP plyd't- /frayad-/ ‘to help, assis" > DMMPP: 372a, 282a 
14465:/frayadéd/, 3pl. MMP pry’dynd, IMPV. 2sg. MMP pry’d-; Partic.: perf. pass. MMP fry’dg, pry’d’g’n, 
14494:*NEIR: Sh. yad- ‘to come’, Rosh. yad- ‘to come’, ? Yghn. yat-/yätta ‘to find a place, 
14769:*OLD PERSIAN: yad- ‘to worship’ = Kent: 204b 
14242:*iam 211 
55313:*iam (s.v.), *spas, *xaiz (s.v.) 
56899:*iam, *iau' 
57520:*iam 
58279:*yamH
```


## [2026-10-17T00:35:46.905Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12030,12080p CHEUNG.txt"
}
```


### [2026-10-17T00:35:47.272Z] TOOL RESULT

```
«PIE *Hiieb"- ‘to have sexual intercourse’. 0 The postulation of an initial *H;- in IE 
is based on the Gr. reflex (zero grade *Hiib^- or, more likely, redupl. *H;eHib’-), 
on which see Peters 1980: 96 ff.; Beekes 1969: 131. The presence of the laryngeal 
may also explain the long -i- in the Skt. desid. forms yiyapsyata (ASS. 10,8,11), 
yiyapsyate (ASS. 8,3,24), уїуарѕуатапа (SSS. 12,23,5), which Hoffmann, Aufs. 2: 
572 f. merely regarded as "irregular". See also *ia(m)b/p. > LIV: 309 | Pok.: 298 


*IE COGNATES: Russ. ebät’, Ukr. jebáty, Gr. оїфо ‘to have sexual intercourse’ 
*REFERENCES: EVS: 37b; Werba 1997: 221; NEVP: 30 


*HiaH ‘to remember’ 

*OLD PERSIAN: (+ *abi-) *abiyataka- ‘remembering’ (in Hes. оВотоко) 

*MIDDLE PERSIAN: (+ *abi-) MMP ’y’s-, BMP ’byd’s- /ayyas-/ (old inch.) ‘to 
remember [intr.]’, BMP ’dyb’tyn- /ayaden-/ (sec. caus.) ‘to remember’ = DMMPP: 
80a f. 

Pres.: IND. 1р1. MMP ’y’s’m; Partic.: perf. pass. MMP viet BMP ’byd’syt /ayasid/, caus. IND. 35р. 
BMP ’dyb’tynyt /ayadénid/ 


176 *Hiaud 


*PARTHIAN: (+ *abi-) *by’s- ‘to remember [intr.] = Ghilain: 83 | DMMPP: 16a 
Pres.: IND. 3sg. ’by’syd 

*KHOTANESE: (+ *abi-) byata- ‘remembered, memory’ 

*SOGDIAN: (+ *abi-) SSogd. ’By’tw (Asg. m.) ‘memory, remembrance’ 

*NWIR: (+ *abi-) NP yad ‘memory, remembrance’, widely borrowed (e.g. in Bal. yat, 
Kurd., Qohr. yad) 

*MISC: (+ *abi-) Par. awé ‘remembering’, also Toch. A opyäc, B ep(i)yac ‘in 
remembrance’ (< Ir., possibly Bact.) 

*SANSKRIT: ya ‘to drive, speed’ (RV+) = EWAia II: 407 

© This root with the meaning ‘to remember’ is solely attested with the preverb *abi-. 
It is probably originally identical to *HiaH ‘to go, drive to’ (Skt. ya, etc.) that has 
acquired a specialized meaning with *abi-: > *‘to come to mind’ > ‘to remember’. 
The peculiar form OAv. “’yamang gen. sg. ‘course’ (Y 48.2) may actually contain 
*HiaH ‘to go, drive to’, on which see, for instance, Insler, Gathas: 286. 

*PIE *HJeH>- ‘to go, drive to’ = LIV: 319 f. | Pok.: 293 ff.
```


## [2026-10-17T00:36:08.764Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,60p tools/verify_check.py | head -80; python3 -c \"import json;d=json.load(open('data/verification/page-558.json'));print(d['verified_by'],d['verified_on'])\""
}
```


### [2026-10-17T00:36:09.130Z] TOOL RESULT

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
claude-opus-5.5 2026-10-16
```


## [2026-10-17T00:36:12.619Z] AGENT

Now I'll write the JSON.


## [2026-10-17T00:38:52.840Z] TOOL CALL #53: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-564.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\ndef rc(ref,st,note): return {\"ref\":ref,\"status\":st,\"note\":note}\ndef cs(src,where,st,note): return {\"src\":src,\"where\":where,\"stance\":st,\"note\":note}\ndef nd(i,lang,words,v,der,fa,src,refc,cons): return dict(id=i,lang=lang,words=words,verdict=v,derivation=der,derivation_fa=fa,sources=src,ref_check=refc,consulted=cons)\n\nPOK505 = \"POK_full.txt (lemma jem- 'to hold', Page(s): 505): 'Old Indic yamati reins, steers ... yata-h kept, held, yama-h rein ... Avestan yam-, ... participle Avestan yata- hold, stop, yata- assigned allotment, possession ... Old Indic yama-h, Avestan yama- twin; Old Indic GN Yama-h = Avestan Yima; Latin geminus ... twin'.\"\ne0_nodes = [\n nd(1,\"Avestan\",\"yemô, yemâ, yîma; yima-xšaetem\",\"confirmed\",\n  \"Av. Yima- (YAv., Bartholomae col. 1300 f.: 'EN. eines sagenhaften Königs von Iran', son of Vīvaŋhvant) = Vedic Yama-, son of Vivasvant. Both continue Proto-Indo-Iranian *yamá- 'twin', from PIE *yemHós (Wiktionary). The common noun 'twin' survives in Gathic dual yə̄mā 'the twin (spirits)' (Y. 30.3); Nourai's 'yemô, yemâ' are this word, written with e for ə. The epithet yima- xšaēta- 'radiant Yima' is frequent ('yō yimō xšaētō hvąθwō', Y. 9.4; Bartholomae s.v. xšaēta- 'bes. von Yima'). xšaēta- 'shining' is from the root *xšay- 'shine' (chart's Ksei 2). Nourai glosses Yima as 'king', but that is not the word's meaning. The twin sister in the NOTE is the Pahlavi Yimag/Jamag of the Bundahišn, matching Vedic Yamī, Yama's twin in RV 10.10. That sister is the reason the name is read as 'twin'.\",\n  \"«جم» در اوستا Yima- نام پادشاه افسانه‌ای و پسر ویونگهونت است و با یمهٔ ودایی، پسر ویوسونت، یکی است. هر دو از هندوایرانی *yamá- «همزاد، توأمان» و هندواروپایی آغازین *yemHós می‌آیند. صورت گاهانی yə̄mā «دو همزاد» (یسنا ۳۰، بند ۳) همان است که نورایی yemâ نوشته است. لقب yima- xšaēta- «جمِ درخشان» از xšaēta- «تابان» ساخته شده است. خواهر همزادِ جم در بندهش «جمگ» (یمگ) نام دارد و با یمیِ ودایی برابر است. ادعای نورایی درست است، اما معنای «پادشاه» برای Yima در اوستا دقیق نیست و این واژه نام خاص است.\",\n  [W+\"جمشید\",W+\"Reconstruction:Proto-Indo-European/yemHós\",\"https://abadis.ir/fatofa/جمشید/\"],\n  [rc(\"KLN:1763\",\"partial\",\"KLN_1971.txt s.v. Yima: 'the Avestic equivalent of Yama (Persian mythol.) — Avestic Yima-, rel. to OI. Yamah. See Yama.' Klein's Yama entry: 'of uncertain origin. It means perh. lit. the restrainer, fr. OI. yamah, rein, bridle'. Under Gemini he gives 'OI. yamah, Avestic yema, twin'. Klein supports the Yima = Yama equation and the link to the root, but he prefers the meaning 'restrainer' over 'twin' for the name.\"),\n   rc(\"BRT:1301\",\"supports\",\"BRT.txt line 21827 (cols. 1300-1301): 'yima- m. EN. eines sagenhaften Königs von Iran: yō yimō xšaētō hvąθwō ... Y.9.4 ... ai. yamá- m. EN., np. jam(šēd). Eig. Bed.?'. The name, the Yima xšaēta formula and the NP outcome are all there. Bartholomae leaves the original meaning open.\"),\n   rc(\"IRN:5\",\"supports\",\"IRN pdf p.16 = printed p.5 (tools/ref_page.py IRN:5, OCR): 'جمشید yima xšaēta بمعنی توأم درخشان که با خواهرش ... همزاد بود'. This is exactly Nourai's 'twin' reading and the twin-sister note.\")],\n  [cs(\"BRT\",\"col. 1300 s.v. yima-; s.v. xšaēta- (line 10698)\",\"supports\",\"'yima- m. EN. eines sagenhaften Königs von Iran ... ai. yamá-, np. jam(šēd)'; xšaēta- 'licht, strahlend ... bes. von Yima: yō yimō xšaētō'.\"),\n   cs(\"POK\",\"p. 505 lemma jem-\",\"supports\",\"'Old Indic yama-h m., Avestan yama- m. twin; Old Indic GN Yama-h ... = Avestan Yima'.\"),\n   cs(\"NYB\",\"Glossary s.v. Yam\",\"supports\",\"'Yam [ym] one of the primeval heroes, son of Vivanghan ... ~ i šēt = NP Jamšed ... Av. (1300 sq.) Yima (OInd Yama-); Paz. Jim; NP Jam'.\")]),\n nd(2,\"Pahlavi\",\"yam; yam-šît\",\"plausible\",\n  \"Book Pahlavi Yam [ym] 'Yima', and Yam ī šēd [ym šyt'] 'radiant Yam' (NYB s.v. Yam: '~ i šēt = NP Jamšed'), continue Av. Yima- and Yima xšaēta-. Avestan -i- in the open first syllable became MP -a-, and xšaēta- became MP šēd: initial xš- was simplified to š-, OIr. ai became ē, and intervocalic -t- was voiced to -d-. The same development gives xwaršēd 'sun' < hvarə xšaēta-. Wiktionary also cites MP ymšyt' /jamšēd/, read with j-, as in Pazand Jim. The words and the derivation are right, but the gloss 'king' for yam is not: in Pahlavi Yam is only a proper name.\",\n  \"در پهلوی Yam (ym) نام همان جم است و «Yam ī šēd» (ym šyt') یعنی «جمِ درخشان». این صورت‌ها از اوستایی Yima- و yima- xšaēta- آمده‌اند: xš- آغازین به š- ساده شده، ai باستان به ē بدل شده و t میان دو واکه به d نرم شده است، همان‌گونه که در «خورشید» (xwaršēd از hvarə xšaēta-) می‌بینیم. نیبرگ و ویکی‌واژه این روند را تأیید می‌کنند. اما معنای «پادشاه» که نورایی به yam داده در پهلوی دیده نمی‌شود، چون yam در پهلوی تنها نام خاص است. پس ادعای او با احتیاط پذیرفتنی است.\",\n  [W+\"جمشید\",W+\"جم\"],\n  [rc(\"BQT:587\",\"supports\",\"BQT_v2_pages.txt leaf 45 (printed p. ~587-588), footnote 1 to جمشید (OCR): 'از: جم (اوستا yima، سانسکریت (ودا) yama، پهلوی yam «بارتولمه ...») + شید ... یعنی جم درخشان'. Mo'in gives the Pahlavi yam and the meaning 'radiant Jam'.\")],\n  [cs(\"NYB\",\"Glossary s.v. Yam, Yam-kart\",\"supports\",\"'Yam [ym] ... ~ i šēt = NP Jamšed ... Av. Yima'.\"),\n   cs(\"PHD\",\"PHD.txt grep '^yam\\\\b|jamšēd'\",\"silent\",\"MacKenzie's headword list (proper names are mostly omitted) gives no entry for Yam/Jamšēd in the OCR.\"),\n   cs(\"NYB\",\"Glossary s.v. x'ar-xšēt\",\"supports\",\"'Av. hvaro.xšaēta- ... + ašaēta- splendent; ... NP xuaršed' gives the parallel xšaēta- > šēd development.\")]),\n nd(3,\"Persian\",\"jam; Jamšîd\",\"confirmed\",\n  \"NP Jam / Jamšēd (Classical Jamšēd, modern Jamšid) < MP Yam / Yam-šēd (Wiktionary: 'Inherited from Middle Persian ymšyt' /jamšēd/ ... from Avestan yima.xšaēta'). OIr. initial y- becomes NP j- (compare yuga- > joft, yav- > jow). Majhul ē became i in Iranian Persian, so šēd > šid. Lexicographers took jam secondarily as an appellative 'great king' (Borhan: 'جم نام داشت یعنی سلطان و پادشاه بزرگ'), which explains Nourai's gloss 'king'. The Farrokhi line pairs Jamšid and Jam as two names of one king.\",\n  \"«جم» و «جمشید» از پهلوی Yam و Yam-šēd آمده‌اند. y- آغازین ایرانی باستان در فارسی نو به ج بدل شده است (همچنان که در «جفت» و «جو») و یای مجهول ē در فارسی امروز ایران به ی (šid) گراییده است. معنای «پادشاه بزرگ» برای «جم» را فرهنگ‌نویسان، از جمله برهان قاطع، بعدها از روی نام جمشید ساخته‌اند. معین در حاشیهٔ برهان قاطع این واژه را از اوستایی yima، سنسکریت yama و پهلوی yam می‌داند و جمشید را «جمِ درخشان» معنی می‌کند. ادعای نورایی درست است.\",\n  [W+\"جمشید\",W+\"جم\",\"https://abadis.ir/fatofa/جمشید/\"],\n  [rc(\"BQT:587\",\"supports\",\"BQT_v2_pages.txt leaf 45, s.v. جمشید: 'واو در اول جم نام داشت یعنی سلطان و پادشاه بزرگ'; footnote: 'از: جم (اوستا yima ...، پهلوی yam ...) ... یعنی جم درخشان'.\"),\n   rc(\"MON5:433\",\"not_checked\",\"Mo'in vol. 5 (proper names) is not on disk. Online Dehkhoda/Mo'in at abadis.ir s.v. جمشید quotes the same Borhan text and the Vedic/Avestan Yama/Yima.\"),\n   rc(\"TZF:28\",\"not_checked\",\"Tafazzoli's book is not accessible (refs_online: no copy).\")],\n  [cs(\"HRN\",\"HRN.txt grep 'jam'\",\"silent\",\"no Horn entry for Jam/Jamšēd (proper names are outside the Grundriss).\"),\n   cs(\"BQT\",\"vol. 2 leaf 45\",\"supports\",\"as in ref_check.\"),\n   cs(\"NYB\",\"s.v. Yam\",\"supports\",\"'NP Jam', 'NP Jamšed'.\"),\n   cs(\"ARY\",\"ARY_pages.txt grep 'جمشید'\",\"silent\",\"no entry.\")]),\n nd(4,\"Avestan\",\"yata, yâta, ya 2\",\"plausible\",\n  \"Av. yam- 'hold, restrain' (Bartholomae: 'yam- V. halten; fassen', past participle yata-) is a genuine descendant of PIE *yem- 'hold' (Pokorny 505: 'Avestan yata- hold, stop, yata- assigned allotment, possession'). Bartholomae's yāta- n. means 'der Jemandem zugewiesene Anteil; Besitz' (allotted share, possession), not 'remember'. The sense 'memory' for yāta- comes from Geldner (Studien I 10 n. 2, cited by Horn No. 1119), and Bartholomae does not accept it. So 'hold, keep' is right, while 'remember' rests only on Geldner's rejected reading.\",\n  \"در اوستا ریشهٔ yam- «نگه داشتن، گرفتن» و صفت مفعولی آن yata- به‌راستی از هندواروپایی *yem- «نگه داشتن» است، و پوکورنی (ص ۵۰۵) همین yata- را «نگه‌داشته» معنی می‌کند. اما yāta- در فرهنگ بارتولومه به معنای «بهرهٔ واگذارشده، دارایی» است، نه «یاد». معنای «حافظه» را گلدنر پیشنهاد کرده و هرن از او نقل کرده است، ولی بارتولومه آن را نپذیرفته است. پس بخش «نگه داشتن» درست است و بخش «به یاد داشتن» سست است.\",\n  [W+\"Reconstruction:Proto-Indo-European/yemHós\"],\n  [rc(\"POK:505\",\"partial\",POK505+\" Pokorny has yata- 'hold, stop' and yāta- 'allotment', but no 'remember' sense.\")],\n  [cs(\"BRT\",\"line 21269 s.v. yam-; line 21540 s.v. yāta-\",\"partial\",\"'yam- V. halten; fassen ... PPfP. yata-'; 'yāta- n. der Jemandem zugewiesene Anteil; Besitz' — no meaning 'memory'.\"),\n   cs(\"HRN\",\"No. 1119 (p. 250)\",\"supports\",\"'aw. yāta- Gedächtniss (Geldner, Studien I, 10, Note 2)'.\"),\n   cs(\"CHEUNG\",\"s.v. *Hi̯aH 'to remember' (p. 175)\",\"contradicts\",\"the 'remember' root is *HiaH (only with *abi-), not *yam.\")]),\n nd(5,\"Pahlavi\",\"yât, âyât\",\"disputed\",\n  \"The Pahlavi word is real: MacKenzie p. 15 'ayād [ʾdyʾt' | M ʾyʾd, N yād] memory', with the verb ayāsīdan 'remember'. Horn's 'āyāt / yāt' is the older reading of the same spelling ʾ(d)yʾt; the -d- written in Pahlavi is a historical spelling of *abi-. Modern analysis derives ayād from *abi-yāta-, the past participle of *HiaH- 'to go, come' with the preverb abi-, giving 'come to mind' > 'remembered'. Cheung gives *abi-yāta- (Khotanese byāta- 'memory', Sogdian ʾβyʾtw), and Tavoosi (SNS) gives 'ayyād / ayād < abi+yāta-'. Abi- became ay(y)- by the usual lenition of b to y. The word therefore does not come from Av. yāta-/*yem- 'hold' as the chart draws it.\",\n  \"پهلوی «ayād» (با نگارش ʾdyʾt) به معنای «یاد، حافظه» در فرهنگ مکنزی آمده است و «āyāt / yāt» در کتاب هرن خوانش کهنه‌تر همین واژه است. پژوهش امروزی (چونگ، و طاووسی در واژه‌نامهٔ شایست نشایست) آن را از ایرانی باستان *abi-yāta- می‌داند، یعنی پیشوند abi- و صفت مفعولی ریشهٔ *yā- «رفتن، آمدن»، با تحول معنایی «به ذهن آمده» به «به یاد آمده». در این واژه b پیشوند abi- به y بدل شده است. پس پیوند آن با yāta- اوستایی و ریشهٔ *yem- «نگه داشتن»، چنان‌که نورایی کشیده، پذیرفته نیست.\",\n  [W+\"یاد\"],\n  [rc(\"HRN:250\",\"partial\",\"HRN p. 250 No. 1119: '(1) yād Erinnerung, Gedächtniss ... aw. yāta- Gedächtniss (Geldner ...); phlv. yāt (vd. 19 (96)), sonst āyāt'. Horn gives the Pahlavi forms and the yāta- link, but no tie to *yem-.\")],\n  [cs(\"PHD\",\"p. 15 s.v. ayād\",\"partial\",\"'ayād [ʾdyʾt | M ʾyd, N yād] memory. ~ kardan: remember' (word confirmed, no etymology).\"),\n   cs(\"NYB\",\"Glossary grep 'ayād|āyāt'\",\"silent\",\"no headword found in the OCR.\"),\n   cs(\"CHEUNG\",\"s.v. *HiaH\",\"contradicts\",\"'(+ *abi-) NP yād memory ... This root with the meaning to remember is solely attested with the preverb *abi-. It is probably originally identical to *HiaH to go, drive to'.\")]),\n nd(6,\"Persian\",\"yâd; došyâd\",\"disputed\",\n  \"NP yād 'memory, remembrance' < MP ayād [ʾdyʾt]. The initial a- was lost by aphaeresis, as in ayār > yār and ayāftan > yāftan. MP ayād continues *abi-yāta- from *HiaH- 'go' (Cheung; Wiktionary: 'from Proto-Iranian *Habí- + *yáH-, probably from PIE *yeh₂- to go ... with Iranian semantic shift to enter [the mind] > to remember'). Horn (No. 1119) and Mo'in (BQT 2412) linked it instead to Av. yāta-. Nobody connects it with *yem- 'hold', so the chart's root is not accepted. došyād (دشیاد) 'backbiting' = duš- 'bad, ill' (Av. duš-, MP duš-) + yād, a rare, purist-style compound glossed by Dehkhoda as 'از کسی بد یاد کردن ... غیبت'. Its parts are sound, but it inherits the same problem with the root.\",\n  \"«یاد» در فارسی نو از پهلوی ayād آمده و واکهٔ آغازین آن افتاده است، همان‌گونه که «یار» از ayār و «یافتن» از ayāftan آمده است. ریشهٔ پهلوی، به گفتهٔ چونگ و ویکی‌واژه، ایرانی باستان *abi-yāta- از ریشهٔ *yā- «رفتن» است که معنای «به یاد آمدن» گرفته است. هرن و معین (در حاشیهٔ برهان قاطع، ص ۲۴۱۲) آن را به yāta- اوستایی پیوند داده‌اند، ولی هیچ منبعی آن را از *yem- نمی‌داند. پس پیوند نورایی با این ریشه را پژوهش امروزی رد می‌کند. «دُشیاد» یعنی «بدگویی پشت سر کسی، غیبت» و از «دُش-» (بد) و «یاد» ساخته شده است. این ترکیب درست است، اما در اشکالِ ریشهٔ «یاد» شریک است.\",\n  [W+\"یاد\",\"https://abadis.ir/fatofa/دشیاد/\"],\n  [rc(\"BQT:2412\",\"supports\",\"BQT vol. 4 p. ۲۴۱۲ (pdf 495; vision file ocr/BQT/2412.vision.txt), footnote 7 to یاد: 'اوستا yâta (حافظه)، پهلوی yât، âyât «اسشق ۱۱۱۹»'. This is the source of Nourai's chain Av. yāta → Pahl. yāt/āyāt → yād. Mo'in does not mention *yem- either.\"),\n   rc(\"SNS:85\",\"partial\",\"SNS_pages.txt line 4108 (page offset undetermined): 'ayyād / ayād ... abi+yāta-'. Tavoosi derives the Pahlavi word from *abi-yāta-, which supports the Pahlavi-to-Persian step but not the *yem- root.\"),\n   rc(\"TZF:22\",\"not_checked\",\"Tafazzoli not accessible.\")],\n  [cs(\"HRN\",\"No. 1119\",\"partial\",\"'yād Erinnerung ... aw. yāta- Gedächtniss ... phlv. yāt, sonst āyāt'.\"),\n   cs(\"HUB\",\"HUB.txt grep 'yād'\",\"silent\",\"no remark on No. 1119 found.\"),\n   cs(\"CHEUNG\",\"s.v. *HiaH\",\"contradicts\",\"NP yād < *abi- + *HiaH; PIE *h1yeh2- 'go' (Pok. 293 ff.).\"),\n   cs(\"PHD\",\"p. 15\",\"supports\",\"'ayād ... N yād memory'.\"),\n   cs(\"ARY\",\"ARY_pages.txt grep 'یاد'\",\"silent\",\"no headword entry.\")]),\n nd(7,\"Latin\",\"geminus\",\"plausible\",\n  \"Lat. geminus 'twin, twin-born; double' (plural geminī, the Twins Castor and Pollux). Pokorny, AHD ('Perhaps altered into Latin geminus') and Wiktionary all connect it with *yem(H)- 'twin' (Skt. yamá-, Av. yə̄ma-, OIr. emon 'twins'). Wiktionary: 'Presumably from Proto-Italic *yemanos, from PIE *yemH- twin ... If this is true, the g- must have been analogically introduced from gignō, genus'. Pokorny prefers to explain g- from *gem- 'press together' (or as an Illyrian substrate); Klein mentions a base *gem- 'to press'. The connection is widely accepted but depends on that ad hoc explanation of g-.\",\n  \"لاتینی geminus «همزاد، دوقلو» را پوکورنی، فرهنگ امریکن هریتیج و ویکی‌واژه با *yem(H)- «همزاد» (سنسکریت yamá-، اوستایی yə̄ma-، ایرلندی کهن emon) هم‌ریشه می‌دانند. g- آغازین آن قاعده‌مند نیست و آن را نتیجهٔ قیاس با gignō «زادن» و genus «تبار» می‌شمارند. پوکورنی خود این g- را از ریشهٔ *gem- «فشردن» یا از زبانی زیرلایه‌ای (ایلیری) می‌داند. پس هم‌ریشگی پذیرفتنی است، ولی قطعی نیست.\",\n  [W+\"geminus\"],\n  [rc(\"AHD\",\"supports\",\"AHD_watkins1985.txt line 1191: 'yem-. To pair. Perhaps altered into Latin geminus, twin, paired: GEMINATE, GEMINI ... [Pok. iem- 505.]'\"),\n   rc(\"POK:505\",\"partial\",\"POK p. 505: 'Latin geminus born at the same time, twin-born, twin probably g- is attributed to the root gem- grasp, press together ... (an Illyrian substrate because Latin would have produced je- > ie-)'.\")],\n  [cs(\"KLN\",\"s.v. Gemini\",\"partial\",\"'L., twins ... prob. cogn. with OI. yamah, Avestic yema, twin, MIr. emon ... These words possibly derive fr. I.-E. base *gem-, to press'.\"),\n   cs(\"WLD\",\"Bd. I 207 / via POK reference 'WP. I 572'\",\"silent\",\"not re-read; Pokorny's entry cites WP I 572 for jem-.\"),\n   cs(\"AHD\",\"yem-\",\"supports\",\"as in ref_check.\")]),\n nd(8,\"English\",\"Gemini\",\"confirmed\",\n  \"English Gemini (late 14th c., the constellation and zodiac sign) is borrowed from Latin Geminī, plural of geminus 'twin'. The Latin name is a calque of Greek Δίδυμοι 'the Twins', itself after Babylonian māšu (MUL.MAŠ.TAB.BA 'the great twins') (Wiktionary).\",\n  \"انگلیسی Gemini «جوزا، دوپیکر» از لاتینی Geminī، جمع geminus «همزاد»، وام گرفته شده است. خودِ این نام لاتینی گرته‌برداری از یونانی Δίδυμοι «همزادان» است که آن هم از نام بابلی صورت فلکی «همزادان بزرگ» گرفته شده است. ادعای نورایی درست است.\",\n  [W+\"Gemini\"],\n  [rc(\"None\",\"not_checked\",\"No reference cited by Nourai for this node.\")],\n  [cs(\"KLN\",\"s.v. Gemini\",\"supports\",\"'Gemini, n. pl., 1) the constellation of Castor and Pollux; 2) the third sign of the Zodiac. — L., twins'.\"),\n   cs(\"AHD\",\"yem-\",\"supports\",\"'GEMINATE, GEMINI'.\")]),\n]\n\ne2_nodes = [\n nd(1,\"Avestan\",\"yah 3; yaešyaiti\",\"confirmed\",\n  \"Av. yah- 'to boil, seethe (intr.)', present yaēšiia- (yaēšyeiti, participle yaēšyantīm āpəm 'boiling water', Y. 9.11). It continues PIE *yes- 'boil, foam'. The present is built on the weak stem *ys- with -ya- (*ye-ys-ye-), and Indo-Iranian *ay before š gives Avestan aē. Cognates are Skt. yásyati, yeṣati and Greek zéō (Pokorny 506; Wiktionary). The '3' marks Bartholomae's third homonymous root yah-.\",\n  \"در اوستا ریشهٔ yah- به معنای «جوشیدن» و ستاک حال yaēšiia- (yaēšyeiti «می‌جوشد») به کار رفته است، چنان‌که در یسنا ۹، بند ۱۱، از «آب جوشان» (yaēšyantīm āpəm) سخن می‌رود. این ریشه از هندواروپایی آغازین *yes- «جوشیدن، کف کردن» است و با سنسکریت yásyati و yeṣati و یونانی zéō هم‌ریشه است. پوکورنی، بارتولومه و ویکی‌واژه این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yes-\"],\n  [rc(\"POK:506\",\"supports\",\"POK_full.txt lemma jes- 'to foam, boil', Page(s): 506: '... redupl. yesati ... Avestan yaesyeiti boils (intr.)'.\"),\n   rc(\"KLN:1761\",\"supports\",\"KLN_1971.txt s.v. yeast: '... cogn. with OI. yasyati, it boils, seethes, Avestic yaeshyeiti, boils, seethes (intr.) ... All these words derive fr. I.-E. base *yes-'.\")],\n  [cs(\"BRT\",\"line 21503 s.v. yah-\",\"supports\",\"'yah- V. sieden (intrans.). Praes. ... yaēšya- ... yaēšyantīm āpəm .. das siedende Wasser'.\"),\n   cs(\"AHD\",\"yes-\",\"supports\",\"'yes-. To boil, foam, bubble ... [Pok. jes- 506.]'\"),\n   cs(\"WLD\",\"via POK 'WP. I 208'\",\"silent\",\"Pokorny's entry refers to WP I 208; not re-read.\")]),\n nd(2,\"Persian\",\"jastan; jahîdan\",\"disputed\",\n  \"NP jastan / jah- 'to jump, leap; escape' (and jahīdan, built on the present stem jah-) continues BMP jastan / jah- 'to jump; arise, happen' (Cheung). Horn (No. 420) derived it from Av. yah- 'to boil' ('Die Grundbedeutung ... sprudeln, kochen, sieden'), and Nourai follows him. Hübschmann (Pers. Stud. 50) already called this 'unsicher' because of the meaning: 'springen' = 'sieden'? Cheung calls it 'semantically implausible' and, after Bailey, tentatively derives the verb from Proto-Iranian *zgad- 'to go on, gallop, mount', with j- < *dj- < *zj-, comparing Pashto zğaledəl 'run' and Baluchi jihag 'flee'. Wiktionary follows Cheung. The modern view is therefore that jastan is not from *yes- 'boil'.\",\n  \"«جَستن / جهیدن» به معنای «پریدن، جهش کردن» از پهلوی jastan / jah- آمده است. هرن آن را از اوستایی yah- «جوشیدن» دانسته بود و نورایی از او پیروی کرده است. هوبشمان همان زمان این پیوند را به سبب ناسازگاری معنایی («پریدن» با «جوشیدن») نامطمئن خواند. چونگ نیز آن را از نظر معنا ناپذیرفتنی می‌داند و به پیروی از بیلی آن را با تردید از ایرانی باستان *zgad- «تاختن، برنشستن» می‌گیرد، با هم‌ریشه‌هایی چون پشتو zğaledəl «دویدن» و بلوچی jihag «گریختن». معین در حاشیهٔ برهان قاطع هم سخن هرن و هم ردّ آن را آورده است. پژوهش امروزی پیوند «جستن» با *yes- را رد می‌کند.\",\n  [W+\"جستن\"],\n  [rc(\"BQT:571\",\"partial\",\"BQT_v2_pages.txt leaf 29 (printed p. ~571-572), footnote 7 to جَستن (OCR): 'بقول هرن از ریشهٔ هندی باستان yas (جوشیدن، فوران)، اوستا yah (جوشیدن) «اسشق ۴۲۰». ... این اشتقاق را نپذیرفته آنرا از ... (انداختن) مشتق داند ... بلوچی jihag (فرار کردن)'. Mo'in gives Horn's derivation and also records that it was rejected.\")],\n  [cs(\"HRN\",\"No. 420 (p. 94)\",\"supports\",\"'jastan ... skr. yas-, yasyati sprudeln ... aw. yah- sieden ... phlv. jastan, jahet ... bel. LW. jihag entkommen ... Die Grundbedeutung der yes- ist sprudeln, kochen, sieden'.\"),\n   cs(\"HUB\",\"p. 50\",\"contradicts\",\"'419-420 sind wegen der Bedeutung (suchen = kämpfen, springen = sieden) unsicher'.\"),\n   cs(\"CHEUNG\",\"s.v. *zgad (p. 473 f.)\",\"contradicts\",\"'? NP jastan/jah- ... The old connection cited by Horn 1893: 94 for NP jastan/jah- is semantically implausible, cf. Hübschmann 1895: 50. Bailey suggested a connection with Av. zgad-'.\"),\n   cs(\"ARY\",\"ARY_pages.txt grep 'جستن|جهیدن'\",\"silent\",\"no entry.\")]),\n nd(3,\"Greek\",\"zein, zeein; ek-zema\",\"confirmed\",\n  \"Ancient Greek zéō (infinitive zeîn, uncontracted Epic/Ionic zéein) 'to boil, seethe' < *yes-ō. PIE initial *y- gives Greek z- (Pokorny: 'gr. zéō (= yasati) cook, boil'; Wiktionary ζέω: 'From PIE *yes-'). ékzema 'a boiling out; cutaneous eruption' is ek- 'out' + zéma 'that which is boiled' (-ma noun suffix), from ekzéō 'boil out, break out'. It was used by the physician Aëtius of Amida (6th c.).\",\n  \"یونانی zéō (مصدر zeîn و صورت کهن‌تر zéein) به معنای «جوشیدن» از هندواروپایی *yes- است، و y- آغازین هندواروپایی در یونانی به z- بدل شده است. ékzema یعنی «بیرون‌جوشی، جوش پوستی» و از ek- «بیرون» و zéma «جوشیده» ساخته شده است. پوکورنی، کلاین و ویکی‌واژه این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  [W+\"ζέω\",W+\"eczema\"],\n  [rc(\"KLN:1761\",\"supports\",\"KLN_1971.txt s.v. yeast: 'Gk. zein, to boil, zesis, foam ... All these words derive fr. I.-E. base *yes-'; s.v. eczema (KLN_1966 leaf 272): 'fr. Gk. ekzema, prop. something thrown out by heat, fr. ek and zema, that which is boiled, fr. I.-E. base *yes-'.\"),\n   rc(\"POK:506\",\"supports\",\"POK p. 506: 'gr. zéō (= yasati) cook, boil, simmer, seethe ... zéma and zéra decoction'.\")],\n  [cs(\"AHD\",\"yes-\",\"supports\",\"'2. Greek zeein, zein, to boil: ECZEMA, ZEOLITE'.\"),\n   cs(\"KLN\",\"s.v. eczema\",\"supports\",\"as above.\"),\n   cs(\"WLD\",\"WP I 208 (via POK)\",\"silent\",\"not re-read.\")]),\n nd(4,\"French\",\"eczema\",\"confirmed\",\n  \"Greek ékzema went into Modern (medical) Latin eczema (18th c.; English 1753). French eczéma is attested in medical French from the late 18th or early 19th century. The chart's French link is right as the intermediary for Persian, although strictly the word went Greek > New Latin > French.\",\n  \"یونانی ékzema نخست در سدهٔ هجدهم به لاتینی نوین پزشکی (eczema) راه یافت و از آنجا به فرانسوی eczéma رسید. فرانسوی میانجی ورود این واژه به فارسی است. ادعای نورایی درست است و تنها حلقهٔ لاتینی نوین در نمودار نیامده است.\",\n  [W+\"eczema\"],\n  [rc(\"None\",\"not_checked\",\"No reference cited by Nourai for this node.\")],\n  [cs(\"KLN\",\"s.v. eczema\",\"supports\",\"'Medical L., fr. Gk. ekzema'.\"),\n   cs(\"SKT\",\"SKT.txt grep '^ECZEMA'\",\"silent\",\"not in Skeat's concise dictionary OCR.\")]),\n nd(5,\"Persian\",\"ekzemâ\",\"confirmed\",\n  \"NP egzemā / ekzemā (اگزما / اکزما) 'eczema' is a modern medical loan from French eczéma (Mo'in: '[فر.] نوعی بیماری جلدی'). It came in with French-language medical teaching at the Dār al-Fonun and the Tehran medical school, late 19th to 20th century. Mo'in spells it with گ (اِ زِ), the book with ک; both spellings occur.\",\n  \"«اگزما / اکزما» وام‌واژه‌ای پزشکی از فرانسوی eczéma است. فرهنگ معین آن را با نشان [فر.] «نوعی بیماری جلدی» معنی کرده است. این واژه با آموزش پزشکی به زبان فرانسه در دوران قاجار و پهلوی به فارسی آمد. معین آن را با «گ» نوشته و کتاب با «ک»، و هر دو صورت رایج است. ادعای نورایی درست است.\",\n  [\"https://abadis.ir/fatofa/اگزما/\"],\n  [rc(\"MON:331\",\"supports\",\"Mo'in's printed page cannot be mapped online. abadis.ir (فرهنگ معین) s.v. اگزما: '(اِ زِ) [فر.] (اِ.) نوعی بیماری جلدی ...' confirms the French origin.\")],\n  [cs(\"MON\",\"MON_part1/2.txt grep 'اکزما|اگزما'\",\"silent\",\"not found in the 2-vol abridgement OCR; online Mo'in (abadis) supports.\"),\n   cs(\"KLN\",\"s.v. eczema\",\"supports\",\"source-language chain Gk. > Medical L.\")]),\n nd(6,\"Swedish\",\"zeolit\",\"confirmed\",\n  \"The Swedish mineralogist Axel Fredrik Cronstedt coined zeolit (New Latin zeolites) in 1756, from Greek zéō 'boil' + líthos 'stone'. He named it 'boiling stone' because the mineral froths and gives off steam when heated in a blowpipe flame, releasing its water of crystallisation. Zeolites are hydrated aluminosilicates, matching the chart's gloss.\",\n  \"زئولیت را کانی‌شناس سوئدی، آکسل فردریک کرونستِت، در سال ۱۷۵۶ با نام سوئدی zeolit (لاتینی نوین zeolites) نام‌گذاری کرد. این نام از یونانی zéō «جوشیدن» و líthos «سنگ» ساخته شده و به معنای «سنگ جوشان» است، چون این کانی هنگام گرم شدن آب درون خود را بیرون می‌دهد و گویی می‌جوشد. کلاین و ویکی‌واژه این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  [W+\"zeolite\"],\n  [rc(\"AHD:1488\",\"supports\",\"AHD 1976 p. 1488 is not online. The same root entry in AHD_watkins1985.txt line 1193: 'yes-. ... 2. Greek zeein, zein, to boil: ECZEMA, ZEOLITE. [Pok. jes- 506.]'\")],\n  [cs(\"KLN\",\"KLN_1971.txt s.v. zeolite\",\"supports\",\"'ModL. zeolites, lit. boiling stone, coined by the Swedish mineralogist Axel Fredric Cronstedt (1722-65) fr. Gk. zein, to boil, and lithos, stone ... so called by him because it swells up when heated'.\"),\n   cs(\"AHD\",\"yes-\",\"supports\",\"'ZEOLITE'.\")]),\n nd(7,\"French\",\"zeolite\",\"confirmed\",\n  \"French zéolithe / zéolite was borrowed from Cronstedt's Swedish/New Latin term in 18th-century mineralogy (Wiktionary records Dutch and other borrowings 'from French zéolit(h)e').\",\n  \"فرانسوی zéolithe (zéolite) در کانی‌شناسی سدهٔ هجدهم از اصطلاح سوئدی و لاتینی نوین کرونستت گرفته شد. ادعای نورایی درست است.\",\n  [W+\"zeolit\",W+\"zeolite\"],\n  [rc(\"VOP:197\",\"not_checked\",\"VOP not accessible (refs_online: kind none).\")],\n  [cs(\"KLN\",\"s.v. zeolite\",\"supports\",\"origin in Cronstedt's coinage.\"),\n   cs(\"DEV\",\"not applicable\",\"silent\",\"French/Arabic sources are irrelevant (not an Arabism).\")]),\n nd(8,\"Persian\",\"zeolyt\",\"plausible\",\n  \"NP zeolit (زئولیت) is a technical loan from French zéolite, the usual source of Persian mineral names in -it (compare grānit, bāzālt). The book's 'zeolyt' is Nourai's way of writing -it. I found no dictionary entry to check against, because Nourai's VOP is unavailable and Mo'in has no entry. The form is plausible and the term is in current use in Persian chemistry and geology.\",\n  \"«زئولیت» وام‌واژه‌ای علمی از فرانسوی zéolite است، همانند بسیاری از نام‌های کانی‌ها در فارسی که به «-یت» ختم می‌شوند (مانند «گرانیت»). منبع نورایی (VOP) در دسترس نیست و فرهنگ معین هم این واژه را ندارد. با این حال کاربرد آن در زمین‌شناسی و شیمی فارسی رایج است، پس ادعا پذیرفتنی است.\",\n  [W+\"zeolite\"],\n  [rc(\"VOP:197\",\"not_checked\",\"VOP not accessible.\")],\n  [cs(\"MON\",\"MON_part1/2.txt grep 'زئولیت'\",\"silent\",\"no entry.\"),\n   cs(\"KLN\",\"s.v. zeolite\",\"supports\",\"the European source term.\")]),\n nd(9,\"English\",\"zeolite\",\"confirmed\",\n  \"English zeolite (1777) is borrowed from Swedish zeolit / New Latin zeolites (Wiktionary: 'From Swedish zeolit, and its source, New Latin zeolites, from Ancient Greek ζέω + -lite').\",\n  \"انگلیسی zeolite در سال ۱۷۷۷ از سوئدی zeolit و لاتینی نوین zeolites وام گرفته شد. ادعای نورایی درست است.\",\n  [W+\"zeolite\"],\n  [rc(\"AHD\",\"supports\",\"AHD_watkins1985.txt yes-: 'Greek zeein, zein, to boil: ECZEMA, ZEOLITE'.\")],\n  [cs(\"KLN\",\"s.v. zeolite\",\"supports\",\"'coined by ... Cronstedt'.\"),\n   cs(\"SKT\",\"SKT.txt grep '^ZEOLITE'\",\"silent\",\"not in Skeat.\")]),\n nd(10,\"Germanic\",\"jest\",\"confirmed\",\n  \"Proto-Germanic *jestuz / *jest- 'foam, yeast' (AHD: 'Germanic *jest- in Old English gist, yeast') is the s-stem noun from *yes- 'boil, ferment'. PIE *y- is kept as Germanic j-. Cognates are OHG jesan 'ferment', MHG jest/gest 'foam', German Gischt 'spray', ON jastr 'yeast' and Dutch gist. The chart's 'jest' is the Germanic stem, not an attested word.\",\n  \"ژرمنی آغازین *jestuz (*jest-) به معنای «کف، مایه» از ریشهٔ *yes- «جوشیدن، تخمیر شدن» است و y- هندواروپایی در ژرمنی به صورت j- مانده است. هم‌ریشه‌های آن آلمانی کهن jesan «تخمیر شدن»، آلمانی Gischt «کف موج» و هلندی gist «مایه» است. پوکورنی، فرهنگ امریکن هریتیج و کلاین این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  [W+\"yeast\",W+\"Reconstruction:Proto-Indo-European/yes-\"],\n  [rc(\"AHD\",\"supports\",\"AHD_watkins1985.txt line 1193: 'yes-. To boil, foam, bubble. 1. Germanic *jest- in Old English gist, yeast: YEAST'.\")],\n  [cs(\"POK\",\"p. 506\",\"supports\",\"'Old High German jesan ferment ... Old English gist (engl. yeast) scum, froth, foam, slobber, yeast. Middle Low German gest yeast'.\"),\n   cs(\"KLN\",\"s.v. yeast\",\"supports\",\"'rel. to ON. jastr, Swed. jäst, Du. gist ... OHG. jesan'.\")]),\n nd(11,\"English\",\"yeast\",\"confirmed\",\n  \"English yeast < Middle English yest, yeest < Old English ġist / ġyst 'yeast, froth' < Proto-West Germanic *jestu < Proto-Germanic *jestuz (Wiktionary). OE ġ- before a front vowel was pronounced /j/, spelled y- from Middle English onward.\",\n  \"انگلیسی yeast «مایهٔ خمیر» از انگلیسی میانه yest و انگلیسی کهن ġist «کف، مایه» آمده است و آن از ژرمنی آغازین *jestuz. ġ- در انگلیسی کهن پیش از واکه‌های پیشین «ی» تلفظ می‌شد و بعدها y- نوشته شد. ادعای نورایی درست است.\",\n  [W+\"yeast\"],\n  [rc(\"None\",\"not_checked\",\"No reference cited by Nourai for this node.\")],\n  [cs(\"KLN\",\"s.v. yeast\",\"supports\",\"'ME. yest, fr. OE. gist, giest ... fr. I.-E. base *yes-, to boil, seethe'.\"),\n   cs(\"SKT\",\"SKT.txt grep '^YEAST'\",\"silent\",\"no hit in the OCR.\"),\n   cs(\"AHD\",\"yes-\",\"supports\",\"'YEAST'.\")]),\n]\n\nout = {\"pdf_page\":564,\"book_page\":534,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Yem\",\"verdict\":\"plausible\",\n  \"modern_form\":\"PIE *yem- 'to hold, restrain' (LIV) and, separately, *yemHós 'twin' (Wiktionary); Pokorny 505 treats both under one lemma jem-\",\n  \"note\":\"Pokorny 505 has a single lemma jem- 'to hold' that includes Skt. yamati 'reins in', Av. yata- 'held', and also Skt. yama-, Av. yə̄ma- 'twin', Yama/Yima and Latin geminus. Nourai's gloss 'restrain, hold together (pair)' follows Pokorny. Watkins (AHD yem- 'to pair') and Wiktionary keep *yemHós 'twin' apart, and LIV keeps *yem- 'hold' apart. The twin branch (Yima > Jam/Jamšid; geminus > Gemini) is well founded. The yād branch is not: NP yād < MP ayād < *abi-yāta- from *HiaH 'go' (Cheung). Horn and Mo'in connected yād with Av. yāta-, but no one derives it from *yem-. The extraction matches the chart text; no transcription problems.\",\n  \"note_fa\":\"نورایی ریشه را هندواروپایی *yem- «نگه داشتن، به هم بستن (جفت)» گرفته است. این پیروی از پوکورنی (ص ۵۰۵) است که معنای «نگه داشتن» و «همزاد» را زیر یک ریشه آورده است. پژوهش امروزی (واتکینز، ویکی‌واژه، LIV) این دو را از هم جدا می‌کند: *yem- «نگه داشتن» یک ریشه است و *yemHós «همزاد» ریشه‌ای دیگر. شاخهٔ «همزاد» (جم و جمشید، geminus و Gemini) استوار است. اما «یاد» به گفتهٔ چونگ از *abi-yāta- و ریشهٔ «رفتن» است و ربطی به این ریشه ندارد. پس ادعای نورایی دربارهٔ خود ریشه با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/yemHós\",W+\"جمشید\",W+\"یاد\"],\n  \"ref_check\":[rc(\"POK:505\",\"supports\",POK505)],\n  \"consulted\":[cs(\"AHD\",\"AHD_watkins1985.txt line 1191\",\"partial\",\"'yem-. To pair. Perhaps altered into Latin geminus ... [Pok. iem- 505.]' — 'pair' only, no 'hold' sense.\"),\n   cs(\"WLD\",\"WP I 572 (cited by POK)\",\"silent\",\"not re-read; Pokorny's references 'WP. I 572, WH. I 587'.\"),\n   cs(\"IEC\",\"IEC.txt grep '^yem-|^jem'\",\"silent\",\"no headword found in OCR.\"),\n   cs(\"KLN\",\"s.v. Yama / Gemini\",\"partial\",\"Yama 'perh. lit. the restrainer, fr. OI. yamah, rein'; Gemini 'prob. cogn. with OI. yamah, Avestic yema, twin'.\")],\n  \"nodes\":e0_nodes},\n {\"entry\":2,\"root\":\"Yes\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *yes- 'to boil, foam'\",\n  \"note\":\"Pokorny 506 jes- 'to foam, boil'; AHD yes- 'to boil, foam, bubble'; Wiktionary *yes-. Root, label and gloss are correct, and the Avestan, Greek, Germanic and Western loan branches are all standard. The one weak point is NP jastan/jahīdan 'jump'. Horn derived it from Av. yah- 'boil', Hübschmann doubted this, and Cheung (2007) rejects it in favour of a tentative *zgad- 'gallop, mount'. The extraction matches the chart text.\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *yes- «جوشیدن، کف کردن» در پوکورنی (ص ۵۰۶)، فرهنگ امریکن هریتیج و ویکی‌واژه آمده است. ریشه، زبان و معنا درست است و شاخه‌های اوستایی (yah-)، یونانی (zéō، اگزما، زئولیت) و ژرمنی (yeast) همه پذیرفته‌اند. تنها «جستن / جهیدن» به معنای «پریدن» محل تردید است. این پیوند پیشنهاد هرن بود که هوبشمان در آن تردید کرد و چونگ آن را رد می‌کند و آن را از *zgad- «تاختن» می‌گیرد.\",\n  \"sources\":[\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yes-\"],\n  \"ref_check\":[rc(\"POK:506\",\"supports\",\"POK_full.txt 'Root / lemma: jes- Meaning: to foam, boil ... Page(s): 506'.\")],\n  \"consulted\":[cs(\"AHD\",\"AHD_watkins1985.txt line 1193\",\"supports\",\"'yes-. To boil, foam, bubble. 1. Germanic *jest- ... YEAST. 2. Greek zeein, zein ... ECZEMA, ZEOLITE. [Pok. jes- 506.]'\"),\n   cs(\"KLN\",\"s.v. yeast\",\"supports\",\"'All these words derive fr. I.-E. base *yes-, to boil, seethe'.\"),\n   cs(\"WLD\",\"WP I 208 (cited by POK)\",\"silent\",\"not re-read.\"),\n   cs(\"BRT\",\"s.v. yah-\",\"supports\",\"'yah- V. sieden (intrans.)'.\")],\n  \"nodes\":e2_nodes}\n]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-564.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-564.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-564.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 564"
}
```


### [2026-10-17T00:38:53.463Z] TOOL RESULT

```
nodes verified: 19/19
node verdicts: {'confirmed': 12, 'plausible': 4, 'disputed': 3}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 6, 'supports': 14, 'not_checked': 8}
books consulted: {'supports': 28, 'silent': 16, 'partial': 4, 'contradicts': 5} | by book: {'KLN': 11, 'AHD': 6, 'NYB': 5, 'HRN': 4, 'CHEUNG': 4, 'BRT': 3, 'PHD': 3, 'ARY': 3, 'WLD': 3, 'SKT': 3, 'POK': 2, 'HUB': 2, 'MON': 2, 'BQT': 1, 'DEV': 1}
```


## [2026-10-17T00:39:10.731Z] TOOL CALL #54: SubagentHandback

```json
{
 "message": "I verified page 564 (book page 534) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-564.json`. `verify_check.py 564` shows 19/19 nodes verified and 0 PROBLEM lines.\n\n**Verdicts:**\n- **Roots:** Yes is confirmed. Yem is plausible: Pokorny 505 puts \"hold\" and \"twin\" under one root, while Watkins (AHD), LIV and Wiktionary treat *yem- \"hold\" and *yemHós \"twin\" as separate roots.\n- **Nodes:** 12 confirmed, 4 plausible, 3 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **Yem / Pahlavi yât, âyât (#5):** the word is real (MacKenzie's ayād \"memory\"). But Cheung and the Shayast-ne-Shayast glossary (SNS) derive it from *abi-yāta-, from *HiaH \"to go\", not from Av. yāta- or *yem-.\n- **Yem / Persian yâd; došyâd (#6):** yād comes from MP ayād and so from *abi-yāta- (Cheung, Wiktionary). Horn 1119 and Mo'in (BQT 2412) link it to Av. yāta-, but no source derives it from *yem-. došyâd = duš- + yād and is fine as a compound.\n- **Yes / jastan, jahîdan (#2):** this is Horn's derivation from Av. yah- \"boil\". Hübschmann (p. 50) called it unsure because of the meaning, and Cheung calls it \"semantically implausible\", preferring *zgad- \"gallop, mount\". Mo'in's footnote at BQT ~571 reports both Horn and the rejection.\n\n**Plausible:**\n- Pahlavi yam glossed \"king\": in Pahlavi Yam is only a proper name.\n- Av. yāta glossed \"remember\": this is Geldner's meaning; Bartholomae gives \"allotted share\".\n- Latin geminus: its g- is unexplained.\n- Persian zeolyt: Nourai's source VOP is unavailable, so I could not check it.\n\n**Extraction errors:** none. The JSON matches the chart text, and I did not need to check the page image.\n\n**Other notes:**\n- I saved my reading of the BQT p.2412 page image as `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2412.vision.txt`.\n- Etymonline returned 403 for every request, so I used Wiktionary instead; all web sources I cite were archived with fetch_source.py.\n- I could not check these references because no copy is available: MON5, TZF and VOP."
}
```


### [2026-10-17T00:39:10.976Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
