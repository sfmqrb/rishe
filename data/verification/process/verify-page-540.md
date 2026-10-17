# Verification process log — verify-page-540


## [2026-10-17T00:00:15.226Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 540 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-540.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-540.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-540.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 540` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.266Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.420Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.500Z] TOOL RESULT

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


## [2026-10-17T00:00:18.915Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-540.txt"
}
```


### [2026-10-17T00:00:19.011Z] TOOL RESULT

```
1	=== PDF page 540 (book page 510) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wel 2 : to tear, pull, wound  (refs POK:1144)  PART 1
4	#1 (parent #0) [Sanskrit] refs=BQT:2253 | vrana : wound
5	  #2 (parent #1) [Persian] refs=MON:4966; POK:1145 | vâlâneh, valâneh «والانه ، ولانه» : wound
6	#3 (parent #0) [Latin] refs=AHD | vulmus : wound ; vellere : to tear
7	  #4 (parent #3) [English] refs=None | vulnerable ; vulture
8	--- entry 1 ---
9	ROOT [Indo-European] Welâ, Wlnâ, Wolko : plucked off (wool)  (refs POK:1139)
10	#1 (parent #0) [Avestan] refs=POK:1139 | varesa : hair
11	  #2 (parent #1) [Pahlavi] refs=HRN:202 | vars : curly hair
12	    #3 (parent #2) [Persian] refs=MON:5004; SNS:285; BQT:1794; KLN:856 | vares «وَرس (وریس)» : a string used in Zoroastrian ceremonies ; gors 2 «گُرس ۲» : curly hair
13	#4 (parent #0) [Sogdian] refs=SOD:412 | wrs : hair
14	#5 (parent #0) [Germanic] refs=AHD | wullâ : wool
15	  #6 (parent #5) [English] refs=None | wool
16	#7 (parent #0) [Latin] refs=AHD | villus : shaggy hair
17	  #8 (parent #7) [English] refs=None | velvet
18	--- entry 2 ---
19	ROOT [Indo-European] Wlkwo : tearing animals, wolf  (refs KLN:1750)
20	#1 (parent #0) [Avestan] refs=KLN:1750; SOD:423 | vherka, vehrka : wolf
21	  #2 (parent #1) [Pahlavi] refs=HRN:202 | gurg
22	    #3 (parent #2) [Persian] refs=BQT:1797 | gorg «گرگ» : wolf
23	#4 (parent #0) [Old Persian] refs=KNT:206 | varkana : wolf land
24	  #5 (parent #4) [Pahlavi] refs=KNT:206 | gorgân
25	    #6 (parent #5) [Persian] refs=KNT:206 | Gorgân «گرگان» : a district S.E. of the Caspian sea
26	#7 (parent #0) [Sogdian] refs=SOD:423 | wyrk : wolf
27	#8 (parent #0) [Germanic] refs=AHD | wulfaz : wolf
28	  #9 (parent #8) [English] refs=None | wolf
29	
```


## [2026-10-17T00:00:19.356Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-540.json"
}
```


### [2026-10-17T00:00:19.619Z] TOOL RESULT

```
1	{
2	  "pdf_page": 540,
3	  "book_page": 510,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wel 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1144",
10	        "gloss": "to tear, pull, wound"
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Sanskrit",
18	          "refs": "BQT:2253",
19	          "words": [
20	            {"translit": "vrana", "gloss": "wound", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "MON:4966; POK:1145",
30	          "words": [
31	            {"translit": "vâlâneh, valâneh", "gloss": "wound", "script": "والانه ، ولانه"}
32	          ],
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 0,
39	          "lang": "Latin",
40	          "refs": "AHD",
41	          "words": [
42	            {"translit": "vulmus", "gloss": "wound", "script": null},
43	            {"translit": "vellere", "gloss": "to tear", "script": null}
44	          ],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 3,
51	          "lang": "English",
52	          "refs": null,
53	          "words": [
54	            {"translit": "vulnerable", "gloss": null, "script": null},
55	            {"translit": "vulture", "gloss": null, "script": null}
56	          ],
57	          "note": null,
58	          "quote": null
59	        }
60	      ]
61	    },
62	    {
63	      "root": {
64	        "name": "Welâ, Wlnâ, Wolko",
65	        "lang": "Indo-European",
66	        "refs": "POK:1139",
67	        "gloss": "plucked off (wool)"
68	      },
69	      "nodes": [
70	        {
71	          "id": 1,
72	          "parent": 0,
73	          "lang": "Avestan",
74	          "refs": "POK:1139",
75	          "words": [
76	            {"translit": "varesa", "gloss": "hair", "script": null}
77	          ],
78	          "note": null,
79	          "quote": null
80	        },
81	        {
82	          "id": 2,
83	          "parent": 1,
84	          "lang": "Pahlavi",
85	          "refs": "HRN:202",
86	          "words": [
87	            {"translit": "vars", "gloss": "curly hair", "script": null}
88	          ],
89	          "note": null,
90	          "quote": null
91	        },
92	        {
93	          "id": 3,
94	          "parent": 2,
95	          "lang": "Persian",
96	          "refs": "MON:5004; SNS:285; BQT:1794; KLN:856",
97	          "words": [
98	            {"translit": "vares", "gloss": "a string used in Zoroastrian ceremonies", "script": "وَرس (وریس)"},
99	            {"translit": "gors 2", "gloss": "curly hair", "script": "گُرس ۲"}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 4,
106	          "parent": 0,
107	          "lang": "Sogdian",
108	          "refs": "SOD:412",
109	          "words": [
110	            {"translit": "wrs", "gloss": "hair", "script": null}
111	          ],
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 5,
117	          "parent": 0,
118	          "lang": "Germanic",
119	          "refs": "AHD",
120	          "words": [
121	            {"translit": "wullâ", "gloss": "wool", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 6,
128	          "parent": 5,
129	          "lang": "English",
130	          "refs": null,
131	          "words": [
132	            {"translit": "wool", "gloss": null, "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 7,
139	          "parent": 0,
140	          "lang": "Latin",
141	          "refs": "AHD",
142	          "words": [
143	            {"translit": "villus", "gloss": "shaggy hair", "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 8,
150	          "parent": 7,
151	          "lang": "English",
152	          "refs": null,
153	          "words": [
154	            {"translit": "velvet", "gloss": null, "script": null}
155	          ],
156	          "note": null,
157	          "quote": null
158	        }
159	      ]
160	    },
161	    {
162	      "root": {
163	        "name": "Wlkwo",
164	        "lang": "Indo-European",
165	        "refs": "KLN:1750",
166	        "gloss": "tearing animals, wolf"
167	      },
168	      "nodes": [
169	        {
170	          "id": 1,
171	          "parent": 0,
172	          "lang": "Avestan",
173	          "refs": "KLN:1750; SOD:423",
174	          "words": [
175	            {"translit": "vherka, vehrka", "gloss": "wolf", "script": null}
176	          ],
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 2,
182	          "parent": 1,
183	          "lang": "Pahlavi",
184	          "refs": "HRN:202",
185	          "words": [
186	            {"translit": "gurg", "gloss": null, "script": null}
187	          ],
188	          "note": null,
189	          "quote": null
190	        },
191	        {
192	          "id": 3,
193	          "parent": 2,
194	          "lang": "Persian",
195	          "refs": "BQT:1797",
196	          "words": [
197	            {"translit": "gorg", "gloss": "wolf", "script": "گرگ"}
198	          ],
199	          "note": null,
200	          "quote": null
201	        },
202	        {
203	          "id": 4,
204	          "parent": 0,
205	          "lang": "Old Persian",
206	          "refs": "KNT:206",
207	          "words": [
208	            {"translit": "varkana", "gloss": "wolf land", "script": null}
209	          ],
210	          "note": null,
211	          "quote": null
212	        },
213	        {
214	          "id": 5,
215	          "parent": 4,
216	          "lang": "Pahlavi",
217	          "refs": "KNT:206",
218	          "words": [
219	            {"translit": "gorgân", "gloss": null, "script": null}
220	          ],
221	          "note": null,
222	          "quote": null
223	        },
224	        {
225	          "id": 6,
226	          "parent": 5,
227	          "lang": "Persian",
228	          "refs": "KNT:206",
229	          "words": [
230	            {"translit": "Gorgân", "gloss": "a district S.E. of the Caspian sea", "script": "گرگان"}
231	          ],
232	          "note": null,
233	          "quote": null
234	        },
235	        {
236	          "id": 7,
237	          "parent": 0,
238	          "lang": "Sogdian",
239	          "refs": "SOD:423",
240	          "words": [
241	            {"translit": "wyrk", "gloss": "wolf", "script": null}
242	          ],
243	          "note": null,
244	          "quote": null
245	        },
246	        {
247	          "id": 8,
248	          "parent": 0,
249	          "lang": "Germanic",
250	          "refs": "AHD",
251	          "words": [
252	            {"translit": "wulfaz", "gloss": "wolf", "script": null}
253	          ],
254	          "note": null,
255	          "quote": null
256	        },
257	        {
258	          "id": 9,
259	          "parent": 8,
260	          "lang": "English",
261	          "refs": null,
262	          "words": [
263	            {"translit": "wolf", "gloss": null, "script": null}
264	          ],
265	          "note": null,
266	          "quote": null
267	        }
268	      ]
269	    }
270	  ]
271	}
272	
```


## [2026-10-17T00:00:36.094Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','CHEUNG','BQT','MON','ARY','SOD','KLN','SKT','FSD','WEB','SNS']:\n  v=d.get(k,{}); print(k, v.get('local_file'), v.get('page_offset'), v.get('kind'), (v.get('lookup_hint') or '')[:120])\n\"; cat tools/verify_check.py | head -60"
}
```


### [2026-10-17T00:00:36.558Z] TOOL RESULT

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
POK /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-
WLD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). archive_djvu Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm 
AHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. archive_djvu+website+archive_restricted Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- 
IEC /home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Al
SYN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1.
BRT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start
KNT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. gre
PHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^ab
NYB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -
HRN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word 
HUB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by par
CHEUNG None None None 
BQT ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). archive_djvu+local_scan_ocr grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or us
MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None website+archive_djvu Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (P
ARY ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 local_scan_ocr Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, Ma
SOD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'] printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) archive_djvu Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than 
KLN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivati
SKT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
FSD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 M
WEB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> archive_djvu Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 
SNS ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt'] 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image archive_djvu grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive
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
```


## [2026-10-17T00:00:41.732Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 60,200p tools/verify_check.py"
}
```


### [2026-10-17T00:00:42.069Z] TOOL RESULT

```
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


## [2026-10-17T00:00:54.356Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vraṇ\\|vrana\\|vraņ' POK_full.txt | head; grep -n -i 'vulnus' POK_full.txt | head; grep -n -i 'varəsa\\|varesa\\|varasa' POK_full.txt | head; grep -n -i 'vəhrka\\|vehrka\\|v[eə]hrka' POK_full.txt | head"
}
```


### [2026-10-17T00:00:54.728Z] TOOL RESULT

```
7703:Karauaai E^avrAnaai, KaraSuaai, KaOauaai acpaviaai (Spritus asper after the former 
91306:Slavic vrana, serb. vrana, russ. i/c»/'d/75 (glottal stop through Vriddhi); Hittite uar- 'burn', 
92178:(therefrom i/c»/'d/7/ra"Trichter'), poln. wrona, Czech vrana ^ aperture '; ure-no-, uro-no-\r\ Old 
92179:Indie vrana-rr\. n. 'wound, crack' besides urd-na\r\ Old Church Slavic russ. etc. rana 
90393:auf " flexible rod') and Avestan varasa-, npers. gurs= Old Church Slavic vlasi^, russ. volos
```


## [2026-10-17T00:01:00.530Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90370,90420p POK_full.txt; echo ======; sed -n 92150,92200p POK_full.txt"
}
```


### [2026-10-17T00:01:01.094Z] TOOL RESULT

```
Exit code 1
Material: A. Old Indie urnai. (compare Old Indie urna-vabhi- ' spider ', above S. 1114) 
'wool', Avestan varana6s., gr. Anvoc;, Doric Aavoc; n. 'wool', Latin lana ds., lanugo' fluff, 
underfurof Bartes, Milchhaare', Gothic wulla, Old High German wolla etc. 'Wolle = wool', 
Lithuanian i////7a 'Wollfaser', PI. 'wool', Latvian i//Za5 'wool'. Old Prussian wllna'Rock', r.- 
Church Slavic vibna, serb. vuna'\Noo\'; schwachere Ablautform *ulana\n cymr. gwlan, 
corn, gluan, bret. gloan{bn{. loanword is Middle Irish olann) 'wool'; 

other vowel gradation in Latin vellus, -e/75 'fleece' (i///A/s'das zottige, wollige Haarthe 
animal') = Old English m///-/77c»o''coIus' (i.e. 'Wollstange', as wul-mod), probably also 
Armenian gelmn'woo\, fleece'; relationship to Latin vellere {uel-8) from *uel-s-d\\es near; 



*ul6- in gr. Awpa n. "hem, Gespint', Germanic V/c»/7a- (under B) and Indo Germanic *ul6- 
ro-{uel-7)S. 1143. 

B. guttural extensions: 

Old Indie valka-m. "bast, splint', i/5//r5/5-"Bastgewand', vrkala-v\. "Bastgewand; a 
certain intestine, entrails '; isl. /of., Danish /^"Tuchflocke, das Rauhe an Kleidern', Old 
English Old Saxon wloh^ fibre, filament, fringe, Flocke' (Germanic *wldha-)\ Old Icelandic 
lagdr^ tuft of Wolle or Haar' ( *wlagat^a-)\ Old Church Slavic vlakno, russ. volokno " fibre, 
filament '; with Indo Germanic ^.Old Indie valsa-m. "sprout, twig, branch' (these point at 
auf " flexible rod') and Avestan varasa-, npers. gurs= Old Church Slavic vlasi^, russ. volos 
"hair'; to a from beiden root form belongs gr. Aaxvr) f. "krauses hair' ( *ulksna), Kayyoc, m. 
"wool'; 

compare under *uel- "turn' die likewise auf *i/c»//r- indicating Old English wielgan^roW, 
Old High German wal(a)gdn. 

C. Dental extensions: 

Gr. Kdmoc, (*FAaTiO(;, Indo Germanic *ult-lios) "dense with Wolle or Haaren, also 
brushwood bewachsen'; Old Irish /b//"hair', cymr. gwallt, acorn, gols, abret. guo/f6s., 
therefrom abret. guiltiat, guiliat, guoliat. Middle Breton guilchaV fleece, Tonsur' and cymr. 
gwellaif, acorn. gu/7//h/m ^ sassors' , perhaps also cymr. gwellt, corn, ^n/e/s "grass', abret. 
gueltiocion fenosa' (or to Middle Irish ^e/Zit'o//? "pabulum', ^e//ic/"grast' S. 365, with gwaiter 
gwallfl); 

Old High German Old Saxon wa/c/^\NOo6, forest'. Old English wea/c/6s., Old Icelandic 
i/(?///-"meadow'; after E. Lewy (KZ. 40, 422) and Holthausen (KZ. 46, 178) wijrde Wa/d as 
*(s)ualtus\.o Latin saltus^ defile, narrow passage between mountains, mountain forest ', 
belong, das then from s5//^s "spring' to separate would be (above S. 899), during Ernout- 
Meillet ^889 both unite (compare Pas de Ca/a/s etc.); other place Wa/dto Gothic wilt^eis 
"wild'. Old Icelandic v/7/r^\N\\6, verriJckt', Old English w/7de, Old Saxon Old High German 
wildi^ wild, unbebaut' {*ueltiio-). Modern High German Wild {* ueltos), wherefore further 
cymr. gwyllt^WM, phrenetical, quick, fast' {*ueltT-), corn. ^^y/s"wild, unbebaut', abret. 
^^e/o'-e/7es "insula indomita' (Middle Irish ^e///"Wahnsinniger' is probably brit. loanword); 

Lithuanian i/5///s"Haferrispe, Haferspelte' (also "thread, string'). Old Prussian wolti^ ear 
', ukr. i/c»/d/i."Rispe', serb. etc. i//a/" ear'; 
(eval):1: ===== not found
```


## [2026-10-17T00:01:04.635Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92160,92215p POK_full.txt; grep -n \"Page(s): 113[89]\\|Page(s): 114[0-6]\\|^Root / lemma: uel\\|^Root / lemma: u̯el\" POK_full.txt | head -30"
}
```


### [2026-10-17T00:01:05.124Z] TOOL RESULT

```
Material: A. uerd-: kvesiau varadva- 'soit, lax ', Old Church Slavic vredb, russ. vered 

"wound'; ured-:0\6 Indie avradanta ' s\e wurden weich', vrand/n- 'murbe werdend'; ured-: 

Old Prussian /'eo'c»"Ackerfurche', Old Danish vraade, i//'c»ofe"dig, aufbohren'; urdd-:\-aWv\ 

rodo, -ere^ gnaw, consume', rostrum {* rod -troni) n. "Nagewerkzeug, snout, bill, beak, neb'. 



Old English wrotan^ gnaw, dig', Old Icelandic rota 6s., Old High German z^yoz// 'suscitat, 
movet'. Old English wrot. Middle High German ruozel, ruezel. Modern High German 
Russel{ *wrdtila-)\ in addition zero grade in Swedish dial, rota, ruta'6\g'; after Frisk (Etyma 
Armen. 30) in addition still Armenian gercum ' s\r\a\/e' from *^e/'o'-s- (originally Aorist 
formation). 

B. uoma:a\b. varre^\N0un6', russ. KC»/'c»/75"Ruderloch in Schiffsheck, Hennensteift' 
(therefrom i/c»/'d/7/ra"Trichter'), poln. wrona, Czech vrana ^ aperture '; ure-no-, uro-no-\r\ Old 
Indie vrana-rr\. n. 'wound, crack' besides urd-na\r\ Old Church Slavic russ. etc. rana 
"wound'. 

Maybe alb. {*varna) Ka/r'grave' [common alb. /77->/7'- shift]. 

C. uergh-:0\6 Indie vrhat/" re\Q>tiro{r\', Aor. varh/, participle vrdha-, mu/a-vrt'6'\e roots 
ausreiftend' (Wackernagel KZ. 67, 166 ff.). 

D. uerk-, urek-sgr. paKO(;, Aeolic ppaKO(; (*FpaKoc;) n. "rag, zerlumptes dress; wrinkle'; 
ppaKaAov ponaAov Hes.; ppaKSTOV 5p£navov, KAaSsurripiov Hes., paKSTpov ds.; 

E. uresk- {from *urek-sk-), ufsk-0\6 Indie vrscat/ 'hautab, splits', vrascana- 'abbauend', 
n. "das Abhauen', pra-vraska-m. "cut'; ava-vrasca- 'sp\\r\ter'; russ.-Church Slavic vraska 
etc. "wrinkle' {*uorska). 

Maybe alb. Kras'kill' [alb. possible -ska > -s] 

F. ur-ei-, un-:gr. pivri "file, tool for smoothing surfaces, Raspel' {*yr/ha; or onomatopoeic 
word?) and "Haifisch' (from seiner zum Polieren verwendeten rauhen RiJckenhaut'); pTv6(; 
"skin; Lederschild', (Aeolic) YpTvo(; (i.e. FpTvo(;) Ssppa Hes., hom. laKaOpwoq 
"schildtragend' (compare M. Leumann, Homer. Worter 196 ff.); 

with o<-extension (originally o<-present?) Old English wrTtan^ dig in, ritzen, write, paint ', 
Old Saxon wrTtan^iear, verwunden, ritzen, write ', Middle Low German wrften^ rend, write, 
draw, sign ', Modern High German reiden, Proto Norse wrait^sc\\r\eb, ritzte' (besides 
Germanic *rTtan\r\ Old Swedish rftads., compare unter/"©/-, rei-d- "ritzen'); Gothic writs 
"line'. Old English M//7/"Schrift', m//'^// "ornament, decoration, jewellery, jewel' ; 

after Frisk (Etyma Arm. 28 ff.) here Armenian erg/canem 'tear, break, rupture, grind, 
carve, slit, injure, stir, tease, irritate' from *ureid-s-. 

References: WP. I 286 f., Trautmann 236, Vasmer 1 , 229. 



Page(s): 1163-1164 

90187:Root / lemma: uelk-1 
90202:Root / lemma: uelk-2, uelg- 
90237:Page(s): 1145-1146 
90239:Root / lemma: uel-1 
90264:Root / lemma: uel-2, ulei-, ule(i)- 
90323:Root / lemma: uel-3 
90430:Page(s): 1139-1140 
90432:Root / lemma: uel-5, uela- 
90448:Page(s): 1140 
90450:Root / lemma: uel^ 
90460:Page(s): 1140 
90462:Root / lemma: uel-7, uela-, ule- 
90695:Page(s): 1140-1144 
90752:Page(s): 1144-1145 
91006:Page(s): 1146-1147
```


## [2026-10-17T00:01:09.319Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90323,90345p POK_full.txt; echo ====; sed -n 90690,90760p POK_full.txt; sed -n 92120,92140p POK_full.txt"
}
```


### [2026-10-17T00:01:09.669Z] TOOL RESULT

```
Exit code 1
Root / lemma: uel-3 
Meaning: to press, push 

Material: Hom. siAu) (*F£A-vci)); Inf.-Aor. eAqqi and with suggestion EcAaai, Aor. Pass. 
£aAr|v, aAri|j£vai, ep. Ionian siAsw {*FzK-ytuS), Attic siAAu) (*£F£Ajaj with Vorschlags-s), Doric 
el. Fr|A£U), redupl. lAAu) (*Fi-FAci)) "drange, push, press, presse'; lakon. pr|Ar||ja KcbAupa, 
cppaypa £v noraiJU) Hes., messen. riAr||ja, Ionian £iAr| "troop, multitude, crowd' (F£Av-), next 
to which probably with /= ©(as niAvapai) AtticlAr), DoriclAa "troop, multitude, crowd' 
(*FiAva), hom. (*iAa56v "scharenweise', pamph. FiAaioc; Gen. from -k; " crowdedness'; 

hom. (Aeolic) azKKr]c, (*aF£Avn(;) "dense zusammengezogen' (KOviaaAoq) and aoKKv\c, 
(*aFoAvric;) "versammelf (with Aeolic -oA-); compare die auf *aFaAAnq from *aVaKyv\c„ 
*aFA/n(; zuriJckgehenden Ionian aKv\c„ aKv\c, "versammelf, aAi^u) " assemble ', aAir) 
"congregation, meeting', Doric aAia and aAiaia ds. (); Attic rjAiaia "place of Gerichts, das 



hochste court in Athen' together with nAia^w, nAiaaTn(; is borrowed from argiv. aAiaia, 
ciAia^u), with Ersetzung from Doric a through Attic n, das as the Asper an i\k\oq eine pad 
fand; das aniaut. a- is kopul. a-; 

ak\q 'scharenweise, sufficient ' (Hom.), yoik\ iKovov Hes.; hom. ouAap6(; "Getummel, 
scuffle ' (because of yoAaiJOc; Siojymcx; Hes. metr. lengthening for *FoAa|JO(;), Attic s^ouAr) 
(eval):1: === not found
```


## [2026-10-17T00:01:19.739Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=90690 && NR<=90790' POK_full.txt; "
}
```


### [2026-10-17T00:01:20.292Z] TOOL RESULT

```
repulsion, loathing feel', wa/gunge' seasickness '. 

References: WP. I 298 f., WH. I 822, II 728 ff., 825, 832 ff., Trautmann 349, Vasmer 1, 165 
f., 234, Frisk 36, 42, 457 f., 461 f.; 
See also: compare ue/-3. 
Page(s): 1140-1144 

Root / lemma: ue/-8 

Meaning: to tear, wound; to steal 

Note: with the ablaut uo/-. uo/-, die perhaps as independent group (A.) abzulosen are 

Material: A. Old Irish fu/7t 'blood'. Middle Irish /^////'bloody Wunden', cymr. gweli {*uolTso- 

?) "wound', corn, goly, PI. golyow. Middle Breton goulyow6s.\ Old Icelandic valrm. "die 

Leichen auf the battlefield ', Old English waelu. "ds., battlefield, Blutbad', Old High German 

walu. ds. ( 'Walstatt), Old Saxon M/a/-o''ao'" murder'. Old Icelandic i/5/Ay/75"Walkure', Old 

English waelcyrige^ euuys, Zauberin' m.; lengthened grade Old High German wuor 

beating, ruin, epidemic ' (but M/i/o/e/7"dig' see below 'Ve/-"turn'), Old Saxon wol. Old 

English wolm. f. " epidemic, pestilence, plague '; 

kir. valjava^W\\h Gefallenen bedecktes battlefield ', Czech 1/5/e// "fight, battle', valka 
"war, fight', wruss. i/a/Aa "fight, struggle, Holzfallen', va/c/c'\N\n, triumph'. Old Prussian u//nt 
(from *walint} "fight'; 

Lithuanian velesor veles^ the ghostly figures of the deceased ', velinas, nowadays 
Ke//7/a5 "devil' (originally "ghost' as Old Lithuanian veluokas), Latvian i/e//" the spirits of the 
deceased '. 

B. Gr. aAioKoiJai "werde gefangen' (Thessalian FaAiaoKETai, Arcadian FqAovtok;), Aor. 
(F)aAaJvai, sdAwv (*ri-FaAu)v), qAwtoc; "gefangen', presumably also Ionian Attic £TAu)T£(;, 
EiAaJrai "Heloten' (from lak. *r|Au)T£(;for *£-F£Au)T£(;); avaAioKU) (*ava-FaAiaK(ji)), Fut. 
avaAcbau) "aufwenden, consume, slay' ("*zum Gebrauch hernehmen, an sich reiften'), 
avaAou) "destroy, smash'; 

hom. Attic ouAr) "wound, scar' (*FoAva or *FoAaa), np. valana, valana "wound', Latin 
volnus, -e/75 "wound' {*ulsnos= Old Irish flann^b\oo&, blutrot'); \/tkka\ iTAai Hes. (i.e. 
FeAAqi; Fick KZ. 44, 438); 



Latin vello, -ere, velliav\6 volsi{vulsi), volsum {vulsum) "pluck, tear, rend; ausreiften, 
ausrupfen, abzupfen'; 

Gothic wilwan^'cob\ wulwa^ robbery'; 

Hittite t/a//7/77/" beldam pfe'; 

in Germanic furtlier formations Middle Low German wietei. "wound, Schmift', Middle 
High German /e/ze/? "injure' (Indo Germanic *LJ[e]lecP}, probably also Old Frisian wiemma 
"damage, injure'. Middle Low German wlame^ disability, SiJndhaftigkeit'; 

Hittite hullai-, hu////a- l\ght, struggle' (?). 

References: WP. I 304 f. WH. II 729 f., 827, Trautmann 348, Frisk 74; 
See also: perhaps in addition ue/k-1'z\e\r\en'. 
Page(s): 1144-1145 

Root / lemma: ue-4, uo- ues- 
Meaning: " down, downward ' 
See also: see above S. 73 {au-). 
Page(s):1114 

Root / lemma: ue-5, uo- 

Meaning: " those, that, pronoun used to indicate specific people or objects ' 

See also: see above S. 75 {au-). 

Page(s):1114 

Root / lemma: uem-, uema- 

Meaning: to spit, vomit 

Material: Old Indie vami-ti, newer 1/5/775// "ausspeien, vomit', 1/5/7/5- "gespien', vamathu-m. 

"Erbrechen', Avestan 1/5/77- "vomit'; npers. 1/5/5/r "saliva' {*um-to-); 

gr. £fj£U) (for *£fj£-|ji), Aor. £|j£aaai "vomit', £[J£to(; m., £p£aic; f. "Erbrechen' (£|juc; 
"Sumpfschildkrote'?); 

Latin vomo {* uemo) "erbreche', i/o/77//i/s" Erbrechen', vom/ca'u\cer, abscess, boil '; 

Norwegian dial. 1///77/5 "nausea feel', i///77/'5 "nausea cause'. Old Swedish vam/m. " 
disgust, repulsion, loathing '; Old Icelandic 1/5/775 "nausea ', vamr' disgusting person'; 



Lithuanian i/e/77// "vomit', vema/arvomW, v/'mdyt/" erbrechen make', Latvian vemt's\ch 
erbrechen'; 

maybe truncated alb. {*vema/a?j iye//"vomit', older i/e/"overeat, feel nausea ' , a Lithuanian 
loanword
```


## [2026-10-17T00:01:31.358Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^ *wel-\\|wel-[0-9]\\|wlkwo\\|wlk\\*o\\|wulfaz\\|wullo\\|wulla' AHD_watkins1985.txt | head -30"
}
```


### [2026-10-17T00:01:31.656Z] TOOL RESULT

```
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
537:gva-. Also grem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumo6n-, he who comes, a guest, in compound *wil-ku- mon-, a desirable guest (*wil-, desirable; see wel-2), in Old English wilcuma, a welcome guest, and wilcume, the greeting of welcome: WELCOME; C. compound *bi-kuman, to arrive, come to be (*bi-, intensive prefix; see ambhi), in Old English becuman, to become: BECOME. 2. Suffixed form *g“(e)m-yo- in Latin venire, to come: VENIRE, VENUE; ADVENT, (ADVENTITIOUS), (ADVENTURE), (AVE- NUE), CIRCUMVENT, CONTRAVENE, CONVENE, (CONVEN- IENT), (CONVENT), (CONVENTICLE), (CONVENTION),
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1045:swel-3, Post, board. Germanic *suljé- in Old English sylXe), doorsill, threshold: stLL. [Pok. 2. sel-, swel- 898.] swem-. To move, stir, swim. Possibly an Indo-European root, but perhaps Germanic only. 1. Germanic *swimjan in Old English swimman, to swim: SWIM. 2. Suffixed zero-grade form *swum-to- in Germanic *sundam in: a. Old English sund, swimming, sea: SOUND’; b. Old French sonde, sounding line: SOUND‘; RADIOSONDE, ROCKETSONDE. [Pok. syem- 1046.]
1139:wel-3
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1141:wel-4
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1293:BENEVOLENT deu-2, wel-2
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1382:COL kwel-1 COLANDER kagh- COLCANNON kaul-, weid- COLD gel-3
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1448:ELDER? el-2 ELDEST al-3 ELECAMPANE wel-3 ELECT leg-1 ELECTUARY leigh- ELEVATE leg*h- ELEVEN oi-no- ELF albho-
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1462:ENTELECHY kWel-1, segh-
```


## [2026-10-17T00:01:43.841Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o 'wel-4[^[]*\\[Pok[^]]*\\]' AHD_watkins1985.txt | head -3; grep -o 'wela-1[^[]*\\[Pok[^]]*\\]\\|wele-1\\. [^[]*\\[Pok[^]]*\\]' AHD_watkins1985.txt | head; grep -o 'VULTURE [^ ]*\\|VELVET [^ ]*\\|VULNERABLE [^ ]*\\|WOOL [^ ]*\\|WOLF [^ ]*\\|VELLICATE [^ ]*' AHD_watkins1985.txt | sort -u"
}
```


### [2026-10-17T00:01:44.356Z] TOOL RESULT

```
VELVET wel-4
VULNERABLE wele-2
VULTURE g@Itur-
WOLF er-2,
```


## [2026-10-17T00:01:49.504Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o 'wel-4[^]]\\{0,1200\\}' AHD_watkins1985.txt | head -3; grep -n -o 'wela-2[^]]\\{0,900\\}\\|wele-2[^]]\\{0,900\\}' AHD_watkins1985.txt | head -3; grep -n -o 'g.ltur-[^]]\\{0,600\\}' AHD_watkins1985.txt | head -3; grep -n -o 'wela-1[^]]\\{0,900\\}\\|wele-1[^]]\\{0,900\\}' AHD_watkins1985.txt | head -3"
}
```


### [2026-10-17T00:01:50.223Z] TOOL RESULT

```
1141:wel-4
1271:wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1394:wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
501:wele-2). 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST?), GUSTO; DISGUST, RAGOUT; b. Latin gustdre, to taste: DEGUST. [Pok. geus- 399.
542:wela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.
1142:wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.
1418:wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1516:wele-1 FLAP plab-
1729:wele-1 LAND lendh-2 LANDSCAPE lendh-2, skep- LANDSMAN2 lendh-2, man-1 LANGLAUF del-1, klou- LANGUAGE dnghi LANGUET dnghi LANGUISH slég- LANIFEROUS wele-1 LANK kleng- LANOLIN wele-! LANTERN [ap- LANTHANUM [|adh- LANUGO wele-1 LAP! {eb-1
```


## [2026-10-17T00:01:54.697Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1141p AHD_watkins1985.txt | cut -c1-2500; grep -n -o 'g.ltur-\\. [^]]\\{0,400\\}' AHD_watkins1985.txt | head -3"
}
```


### [2026-10-17T00:01:55.195Z] TOOL RESULT

```
wel-4
```


## [2026-10-17T00:02:02.296Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1141,1143p AHD_watkins1985.txt | grep -o 'wel-4\\. .\\{0,700\\}\\|wele-1\\. .\\{0,900\\}' ; grep -o 'g.ltur-\\. .\\{0,300\\}' AHD_watkins1985.txt"
}
```


### [2026-10-17T00:02:02.656Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:02:05.596Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o 'To tear, pull.\\{0,600\\}' AHD_watkins1985.txt; grep -n -o 'Wool\\. .\\{0,900\\}' AHD_watkins1985.txt; grep -n -o 'Vulture\\..\\{0,300\\}' AHD_watkins1985.txt"
}
```


### [2026-10-17T00:02:06.309Z] TOOL RESULT

```
1142:To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2.
736:Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
1142:Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk-
553:Vulture. Possible root. Latin vultur, vulture: VULTURE. [Pok. gvltur(os) 482.]
```


## [2026-10-17T00:02:17.554Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo HRN; grep -n -i 'gurs\\b\\|gurg\\b\\|gurgân\\|gurgan' HRN.txt | head; echo HUB; grep -n -i 'gurs\\b\\|gurg\\b' HUB.txt | head; echo PHD; grep -n -i '^wars\\|^gurg\\|^wurg\\|^gurgān\\|^gurgan' PHD.txt PHD_mackenzie.txt | head; echo NYB; grep -n -i '^gurg\\|^wars\\|^gurgān\\|^varš\\|^vars' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-17T00:02:18.244Z] TOOL RESULT

```
HRN
1921:Die sprichwörtliche Redensart gurg-l bärändide *ein *Wolf, der nass
7887:910. gurg 'Wolf.
7889:ap. Varkäna-; aw. cehrka- 'Wolf; phlv. gurg; ai.
10236:cun^) gurg^ bäs^ kl rind ufted fmyän-% r^me
10529:Np. gurs ist unbelegt (vergl. oben No. 908).
HUB
3266:gurs, besser gars im alteren Neupersisch vorhanden
5053:veretka-f choras. kurd. bulk ZDMG. 38, 53; gurs^) 'Hunger',
5054:gursina 'hungrig aus "^vrsa-, *vrsna-; gurg *Wolf = zd.
5063:') Ueber gurs *Lockenhaar* (fiir gars) s. oben p. 92.- 145 —
5156:(aber pr. mired), muru 'bird', guzurg *great', gurg wolf,
5179:pursldan *to ask' p. 110, gurt *a hero', p. 275, gurg Volf
5505:zd. veredka-^ veretka-; gurs 'Hunger*, gursina^ gusna, gusna
5508:vgl. Horn Nr. 907, dazu afgh. vaMi'hungrig, also gurs =
5509:zd. *veresa' (oben p. 92) ; gurg 'Wolf* = phi. giirg Gl. and
5537:gurs Xocken' (unbelegt), besser gars = phi. gars, vars, zd.
PHD
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD.txt:5447:gurg
PHD_mackenzie.txt:2627:gurg [gwlg IN,..,] wolf.
PHD_mackenzie.txt:2628:gurganig [gwlg'nyk l I N ......,i] of (the province) Gurgan.
PHD_mackenzie.txt:5216:wars [wls] hair.
PHD_mackenzie.txt:10715:gurginig
NYB
1740:gurg [gwlg] wolf 4927, 505-13, 9615-18, 1028, — Av. (1418 sq.) vohrka-; NP gurg.
1741:Gurgin [gwlg'n'] the province Gurgan 1144, — Av. (1419) vohrkáno[.Sayana-], OP Vrkāna-; Gr ‘Yoxavta, *Yox&vtov; KZSPrth wrkn, Prs gwlk?n.
3980:vars [wls] hair 26°”. — Av. (1374) varasa-; Paz. vars (SGV); Arm. lw. vars-k* (pl.); NP gurs ‘curled hair’.
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
6863:vars: ~ -VAIZ: varc vas: ~
```


## [2026-10-17T00:02:22.008Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7870,7900p HRN.txt; echo ===; sed -n 10522,10532p HRN.txt; echo ===HUB; sed -n 3258,3275p HUB.txt; sed -n 5535,5540p HUB.txt; sed -n 5052,5056p HUB.txt"
}
```


### [2026-10-17T00:02:22.693Z] TOOL RESULT

```
Exit code 1
907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
(Js. 8, 4), ^r:i'^i: (Js. 5, 13).
g. vasne, vasnegi; Kä§. ves, vesd, vesS, vesegl.
phlv. gursak (AV.), gursakth (Men.), gursUan (vd.
9 (132) GL); kurd. vürsl, vürsigt, vdsa (H.-Sch.).
LW. bei. gusnag, n. gumag (120); siyn. gusna.
Wegen g. vasne etc. muss der Anlaut ursprüng-
lich ein V gewesen sein, also ist bei. gusnag entlehnt.
908. {2)gur8 Xockenhaar (unbelegt).
aw. varesa- 'Haar; phlv. vars, arm. LW. vars;
ksl. vlasu,
909. yiriften 'ergreifen*, Praes. glr-etn,
g. gereftmün,
ap. [/^grab-, agarbayam ergreifen'; aw. [/^grab-,
gerewnäiti; phlv. graftan; ai. l^grabh^, gfbhndti,
kurd. girtin 'ergreifen ; bei. girag , n. giray (106);
sar. vayreiy-am,
910. gurg 'Wolf.
Käs. var, varg, mrg\ mäz. vurg.— 203 —
ap. Varkäna-; aw. cehrka- 'Wolf; phlv. gurg; ai.
vfka- Wolf; arm. gaU (H. No. 62).
kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
(60, unsicher) ; bei. gvark, gurk, n. giirß (140) ; yidg.
yter;', yaj'n. aurak,
911. germ Varm*, gerniä 'Wärme', germJ, germis (AM. 54
Zeile 13; 182 Zeile 9).
ap. garma- in Garmalpada-; aw. garema- warm';
phlv. garm^ garmäk, garmth; ai. gharmd- 'Wärmen-
arm. J^rm 'warm', Jermn 'Fieber , jernum *sich erwärmen,
warm werden, erglühen' etc. (H. No. 243).
kurd. bei. (100) garm, bei. garmag (LW. ? 101); afy.
(eval):1: == not found
```


## [2026-10-17T00:02:26.421Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3260,3272p HUB.txt; sed -n 5535,5540p HUB.txt; sed -n 5050,5056p HUB.txt; echo BRT; grep -n -i 'varəsa\\|varesa-\\|varasa-\\|vəhrka\\|vehrka\\|v.hrka-' BRT.txt | head -20"
}
```


### [2026-10-17T00:02:26.866Z] TOOL RESULT

```
907. Die Nebenform gusna *hungrig' ist durch Anlehnung
an tisna 'durstig entstanden, wie afgh. va^ai 'hungrig'
von ta^ai *durstig' beeinflusst ist. Fiir das Altpers.
ist *vrsa^y *vrsna- anzusetzen.
908. Die Nummer will Horn streiehen (Einleitung p. IX,
Anm.), wohl weil np. guvs unsicher ist. Doch muss
gurs, besser gars im alteren Neupersisch vorhanden
gewesen sein, da die jiingere Form gars auch im Phi.
(vgl. Horn p. 278 Nr. 90) neben alterem phi. paz. vars
(Shk. 270) und arm. vars vorliegt. Zu zd. varesa-
1= *vorh^O') stellt Joh. Schmidt, KZ. 32, 386 gr.
ovXog, was nicht moglich ist.
909. Lies ap. agrhdyam wie in Nr. 910 ap. Vrhana", Die
vazra-; Gulds = Balas, phi. Valaxs Tab. 10; syr. gnhistazdi)
= mp. ^vahiStazad Hoffmann, Ausziige p. 15, Nr. 100;
gurs Xocken' (unbelegt), besser gars = phi. gars, vars, zd.
varesa- (oben p. 92).
§ 48. Ap. ra- wird zu bu- (statt ha-):
'htm 'Baum' (als 2. Glied vom Komp.) = paz. van Min.
dazu auch np. slmury *Vogel Greif = zd. sa^no -\- mereyo ;
mw/'Wein, skr. wrdv«A^*Weintraube'; grwrd 'Held' aus */;rto-,
\^. zi. hqmvareti' *Tapferkeit* ; gurda Niere' = zd. t?«r«<)A;flf-,
veretka-f choras. kurd. bulk ZDMG. 38, 53; gurs^) 'Hunger',
gursina 'hungrig aus "^vrsa-, *vrsna-; gurg *Wolf = zd.
vehrka^; Gurgdn *ein Land' = zd. vehrkdna-, ap. vrkCLna-;
*) Np. mu§tan ist der regelreohte Infinitiv zum Praesens m&lam^
BRT
17300:•  j.  bt-zangra-,  "z^ngra-  Adj.  'mit  zwei Fussknöcheln,  zweiTdssiz',  von  ^n^schen Wesen'*:  maityS  drvä  'zangrd  ava%a abmaeyö  'V.5. 35;  —  maiyäca  'angra (NP.)  Yt.5.  89; —  mairyanamca  "zangra- nqm  astmaoyanamla  'zangranam  vihrka- nqmca  ca%war3.zangranqm  Y.ff.  18;  — yasca  dim  Jana^  . .  vthrk^m  yim  'zangnm dagvayasnsm  V.  7. 5  a  PilZ.
22893:•  j.  varaSa-  m.  i)  'Mehren,  Grossmachen' (nur  Komp.).  2)  Name  einer  Pflanze, vll.  "Rose':  yS  bar^smqtt  *frast)rmte  hae- mqsca   'iss:a  "hanvasca   antar).d3ta    "wer
22991:•  j.  varasa-  ■>  m.,  n.  'Haar*  der  Menschen und  Tiere,  meist  Kopfhaar '>i  Sing,  auch kollektiv;  a)  der  Menschen:  *JiourusS {iA.) asti  "sS  V.7.57;  —  maüstna  .  ,  yaHbyS äste  nasukaia  frasnayante  °taica  tanümla V.  Ä  1 1 ;  —  'Sftn  vä  ianUm  vä  Vd.  4;  — *x''alpaiä,ya{%^)ca  -ja  V,  15.46;  F. jb; — astssca  's3saiYt.io.T2i  —  astqmca  °sqmca (GP.)  V.(),7,  2g; — yalißm..'s3sca'  *Äqm.- razayaiaha  . .  ''pairUrinattAa  "wenn  du  dir die  Haare  geordnet  ..  verschnitten  hast"^ V.  i7.  4;  2;  —  yat  Al  .  .  -jo  (NPq.)  Aiku bavax  "bis  dass  seine  Haare  trocken  wer- den" V.  i5',38;  —  avava^  ..ya%a  *sar?ma 'sanqm  barami  "soviel  als  ich  Haare  auf dem  Kopf  trage"  Ytj.  77.  b)  der Tiere:  aspalm  'am  Yt/4. 31,  i6.\o;  — ^us  vä  aspaht  vä  •sa*''  Vd,^,  S;  ^.^S, Vd.  iJ,  ^,  lO;  —  °iäi  Aaomö.anAanzäHäi (sd.)  Vr.jo.2.
23594:vahrka-
28757:Bed.  uniicher;  'vatia-  >—  j.  vanka-  'Blalt' oder  ^  j.  vihrka-  'WolT;  t.  JOppERT  Les M6de»  sog.  Nöi.oEKE  LC.  i8g4.  151,  Jipsti PrJ.  88.  57,  GltPh.  2.  401,  Bthl.  BB.  13. 70, Fov  KZ.  35.  50.  Ist  •vargi  lu  schreiben, wie  man  nach  der  babyl.  UmichiifC  be. hauptet')  -  mit  allzu  viel  Sicherheit,  da  sie doch  auch  laraiigS  für  in^ta-  bietet  -  so  sind beide  Deutungen  falsch,  s.  Fov  a.O.  —  >)  Auig. hat  ßlschlich  Aum',  BB.  /j.  70.  —  >)  Vgl. JUSTI  aO.,  HösiNG  Iran.  Eigenn.  3a.
```


## [2026-10-17T00:02:30.490Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'v.hrka-  m\\|v.hrka- m\\|v.hrkäna\\|vrkäna\\|vrkana' BRT.txt | head; awk 'BEGIN{RS=\"\\f\"} /varasa-  ■>  m/ {print NR-1; exit}' BRT.txt; grep -n 'vahrka-' BRT.txt | head -3; sed -n 23590,23600p BRT.txt | cut -c1-600"
}
```


### [2026-10-17T00:02:31.084Z] TOOL RESULT

```
755
23594:vahrka-
•  j.  väatryä-  f,  'Beschäftigung  mit  Feld- wirtschaft, Landbaubetrieb':  runHi  ac^ar^n- tarn  tva  nSit  .  .  alayqm  (sd.)  nBii  uyrqm 'yqm  V,  j.  33,         a)    'Feld-,    bäuerlidie
dby  Google
1417
västryavar^z-
vahrka-
1418
Aibeif  (als  Strafe):  *h*7  vä  azaiti  ayan.- ära/Bvä  'j/äj'^  a.42,4,^,6g,  *j,  10g;  6g. Zum  Praes,  i-üjftyo-.  —  Pü.  (laN.):  vJstrySiTA, (laV.):  ^r  /v  iär  i  vaiwmi.—  •)  Man  ver- langte GS.  'yä.
•  j.  västryä-varaz-  Adj.  'Feldarbeit  ver- richtend,  in  der  Landwirtschaft  tätig': narqmca  näirinamca  apfrynäyäkanqmcit kainikanqmca  'zanqmca ''  ".  .  und  den Männern  und  Frauen  und  den  Knaben und  Mädchen  und  (Überhaupt  allen),  die in  der  Landwirtschaft  tätig  sind"  V.  68. 12;  —  dahma  näirike  apsrtnäyake  kainiki '«'■>  Y.  2^.3(?).
Vgl.  gaväsiryavanz-.  —  Pü.!  iär  i/arutär.  — ')  Them.  —  >)  Kasus?     Geringe  SteUe.
•  j-  y^  g^ä  srävayeiti  afs  vä  paitii.- sfaine  (sd.)  .."s-ä^anqm  (sd.)  va  väsyan- tanam"'*  N.  2Ö,
Pu.'  usw.:  s,   vi'"gä%anqm,  Sp.  5190.  —  ')T:
```


## [2026-10-17T00:02:38.811Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo KNT; grep -n -i 'varkana\\|vrkāna\\|vrkana\\|Hyrcania' KNT_full.txt | head; echo SOD; grep -n -i ' wrs\\b\\|wrs \\|wyrk' SOD_pages.txt | head; echo KLN; grep -n -i '^wolf,\\|^vulture,\\|^vulnerable,\\|^velvet,\\|^wool,\\|^villus' KLN_1966.txt | head"
}
```


### [2026-10-17T00:02:39.214Z] TOOL RESULT

```
KNT
2864:Varkana =  Vpküna, Elam. Mi-ir-qa-nu-ia-ip 
2865:‘Hyrcanians’, РЫ. MPers.  Gurgün, Gk. 
5690:pIE *ulgto- "wol in Skt. vfka-s, OP Varkana- 
5691:‘Hyrcania’, Eng. wolf. 
8569:‘Hyrcania’ and towns Patigraband, Višpauzā- 
12414:In DB 2.921 Раша uta Varkana hami- 
12416:and Hyrcania became rebellious from me, they 
17547:Hyrcania became rebellious from me, called 
28794:Varküna- sb. ‘Hyrcania’, a district southeast 
28796:ja-ip ‘the Hyrcanians’, РЫ. and NPers. Gurgan, 
SOD
5765:                                                                         708 »Ys'yn wrs>k     B                                 JJiy>
8807: 1742 'sk'wrS B                          jr^«o3~
8810:        =»sk}wr5, skwrS                                                  (o)skuc-(o)patrxusk ?
16339:                                                                      4428 Ywrs B, C                                ;/<-»>
22876:6666 pckwyrKkh)    B, M                      ^j
25534:      OcOgive                                                       pdfwrs; MP phypwrs =>ptfs-
33122:10167 wrn-1 C, S               jju j^f « ^I^UipU jsibjjl £H 10177   wrs    B, S, C                               yj \y
33132:                                                            10178 wrs»k        B                                 ^J \y
33134:       faith, belief                                                warse,warsak ©in compd. ^ys'yn wrs>k
33878:        Frag. 5.8, IIJ 1996, 49                              10431 wyrq-    C =* wyrk-
KLN
```


## [2026-10-17T00:02:42.556Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28790,28800p KNT_full.txt; sed -n 33118,33140p SOD_pages.txt | cut -c1-200; grep -n 'wyrk' SOD_pages.txt SOD.txt | head; "
}
```


### [2026-10-17T00:02:42.918Z] TOOL RESULT

```
vāra- sb., see Uvárazmi-. 
varka- sb. ‘wolf’, see Varkdna-. 


Varküna- sb. ‘Hyrcania’, a district southeast 
of the Caspian Sea (§166.1): Elam. mi-ir-qa-nu- 
ja-ip ‘the Hyrcanians’, РЫ. and NPers. Gurgan, 
Gk. ‘Tpxavia (830, $99, $107); ‘Wolf-Land’, deriv. 
of pIE *ylg*o-, Av. vohrka-, Skt. vfka-, Lith. vilkas, 
Gt. wulfs ($143.IIT): see also Varkazana-. Var- 
kāna nsm.-.DB 2.92f. 
      Thursday
                                                                    C2, 57R5, 27, 29; Benv. BSL 1958, 70; Schwartz.
        BBB 724
                                                                      STSC 86; BSTii 903.5, 90427, 29
10167 wrn-1 C, S               jju j^f « ^I^UipU jsibjjl £H 10177   wrs    B, S, C                               yj \y
      warn ©trans, pret. wrnd^r-                                    wars     ©Av. vardsa   ©pi. -t(h)
      OcObelieve, (/cOhave faith                                    hair
      GMS 579; TSP 2.657; STi; BSTi, 142; C2 gloss.
                                                                    VJ 837, 1262, 545; TSP 2.525, 192a, C2, 87V4,
        p230; Frag. Len. 39.5; KG 565; Sund. AoFi                     91R6; Sund. AoFi 1974, lOii R10; AI 1988,
        1974, 6V17
                                                                       185; wrstK VJ 545; Gersh. AHM      p265
10168 wrn-2                        *ia*l o^J o^                       y^vart-
      warn, warn ©Av. vardna ©nom. ob. -y(y);
                                                            10178 wrs»k        B                                 ^J \y
         ace. -w; abl. -1
       faith, belief                                                warse,warsak ©in compd. ^ys'yn wrs>k
                                                                    hair
       GMS 62, 513, 1168n 1; TSP 6.70, 8.168; W-Lii
         547.1; BSTBL 634; Dhu. 88; C2 gloss. p230;               VJ 40d; SCE 88
         KG 603, 610; STii 2.1, 20, 8.7; Sund. AoFviii      10179 wrt S                                          *j*<>y
         1981, 20 Rl, 25V5; BSTii 844.60, 886.18,                   wart ©pi. #wr-
         915.5, 916.5                                               interest
SOD.txt:78654:10431  wyrq-    C  =*  wyrk- 
SOD.txt:78656:10432  wyrk-   B 
SOD_pages.txt:33878:        Frag. 5.8, IIJ 1996, 49                              10431 wyrq-    C =* wyrk-
SOD_pages.txt:33880:                                                             10432 wyrk- B
```


## [2026-10-17T00:02:51.489Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 33878,33895p SOD_pages.txt | cut -c55-200; grep -n -i 'wolf' SOD_pages.txt | head"
}
```


### [2026-10-17T00:02:51.917Z] TOOL RESULT

```
       10431 wyrq-    C =* wyrk-
                -ysty
       10432 wyrk- B

             work, wirk (wyrq-) ©<*wrka; Av. vdhrka
 **l           ©nom. -y; ob. -}, -y; pi. -yh, -yst\ ob. pi.

             wolf

             GMS 141, 485, 511; TSP 2.330, 635, 682, 714,
               812; TSP 3243, 246, 6.8; SCE 310, 358, 137,

               pred. inst4 GMS 1182; BSTii 889.23; C2,
               60R23; Frag. Len. 68, 13, 19; pi. wrkyK TSP

               2.635; wyrqysU C2, 12R3, 12V4; STi 6.8; GMS
               1186

3177: /wrk/       wyr*-       wolf          *vfka-                  they become lb d, j,gl\ Olr. /*fe, *d, *;, *gl become
33885:      saw                                                          wolf
39898:wild cat 5561                             with it 3715, 3745, 3748, 3750,            wolf     10432
```


## [2026-10-17T00:02:56.829Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in wolf vulture vulnerable velvet wool villus; do echo \"== $w\"; grep -n -i \"^$w\\b\" KLN_1966.txt | head -3; done; for w in WOLF VULTURE VULNERABLE VELVET WOOL; do echo \"== SKT $w\"; grep -n \"^$w\\b\" SKT.txt | head -2; done"
}
```


### [2026-10-17T00:02:57.351Z] TOOL RESULT

```
== wolf
== vulture
== vulnerable
== velvet
== wool
== villus
== SKT WOLF
== SKT VULTURE
== SKT VULNERABLE
== SKT VELVET
== SKT WOOL
```


## [2026-10-17T00:03:00.533Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"wolf, n\\|vulture, n\\|vulnerable, adj\\|velvet, n\\|wool, n\\|villus, n\" KLN_1966.txt KLN_1971.txt | head; grep -n -i \"^ *wolf\\|^ *vulture\\|^ *vulnerable\\|^ *velvet\\|^ *wool,\" SKT.txt | head"
}
```


### [2026-10-17T00:03:00.885Z] TOOL RESULT

```
KLN_1971.txt:3950:aardwolf, n., a South African hyena-like mam- 
KLN_1971.txt:106224:griffon vulture, n., a large species of vulture (Gyps 
KLN_1971.txt:126444:Invulnerable, adj. — L. invulnerabilis, ‘invulner- 
KLN_1971.txt:195649:pulvillus, n., the pad between the claws on an in- 
KLN_1971.txt:259982:velvet, n. — ME. veluet, velwet, fr. VL. velluetum , 
KLN_1971.txt:262165:villus, n., a hairlike vascular process ( anat .) — 
KLN_1971.txt:264156:vulnerable, adj., 1) that can be wounded; 2) open 
KLN_1971.txt:264229:vulture, n. — ME. vultur , fr. OF. voltour y voutour 
KLN_1971.txt:266194:werewolf, also werwolf, n., a person changed into 
KLN_1971.txt:268019:wolf, n. — ME., fr. OE. wulf, rel. to OS. wulf 
21081:Vulnerable.  (L. )  1*  uuln liable  to  injuiy. —  L.  uulnerart,  to —  L.vw/H/r-, crude  forrn  oiuHlnuj.i Allied  to  uttlert.  to  pluck.,  tear, vraaa,  a  wound,  Ir&cture.     l^  W>
```


## [2026-10-17T00:03:03.673Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 259982 262165 264156 264229 268019; do sed -n \"${n},$((n+14))p\" KLN_1971.txt | tr '\\n' ' '; echo; echo; done; grep -n -i \"^ *wool\\b\\|^wool\" KLN_1971.txt | head -3"
}
```


### [2026-10-17T00:03:04.456Z] TOOL RESULT

```
velvet, n. — ME. veluet, velwet, fr. VL. velluetum ,  fr. *villutus , ‘shaggy’, fr. L. villus, ‘shaggy hair’.  See villus and cp. velours, velure.   Derivatives: velvet , velvet-ed, adjs., velveteen  (q.v.), velvet-y, adj.   velveteen, n., imitation velvet. — Formed fr.  velvet with suff. -een (= a var. of -ine).  venada, n., the pudu. — Fem. of Sp. venado,  ‘deer’, fr. L. vendtus , ‘game’, fr. vendtus , pp. of  venari, ‘to hunt, chase’. See venery, ‘hunting’,  venal, adj., that can be corrupted; mercenary;  corrupt. — L. venalis , ‘that which can be  boughf*ir..ve/j«m or venus. ‘sale’, which is cogn.  

villus, n., a hairlike vascular process ( anat .) —  L., ‘shaggy hair, tuft of hair’, a collateral form  of vellus , ‘fleece’. See vellicate.  vim, n., vigor, energy. — L., acc. of vis, ‘force’.  See vis.   vimana, n., tower of a temple ( Indian archit.) —  OI. vimanah, ‘celestial chariot of the gods; car;  imperial palace; tower’, lit. ‘something meas-  ured out’, fr. pref. vi-, ‘asunder, away from;  very, through’ and mad, ‘measures’, OI. vi - de-  rives fr. I.-E. base *m*-, ‘asunder’; see with and  cp. vice, ‘a moral fault’, and the first element in  vihara. OI. mad, ‘measures’, derives fr. I.-E. base  *me -, ‘to measure’. See meditate and cp. matra  

vulnerable, adj., 1) that can be wounded; 2) open  to attack — Late L. vulnerabilis, fr. L. vulnerdre ,  ‘to wound’, fr. volnus, vulnus, ‘a wound’, which  is cogn. with Gk. o&ki] (for *foXvoc or *foX-  aot), ‘wound, scar’, W. gweli (for *woliya),  ‘wound’, from. I.-E. base *wel-, ‘to tear’,  whence also vellere , ‘to pluck, tear’. See velli-  cate and cp. vulture. Cp. also parulis. For the  ending see suff, -able.   Derivatives: vulnerability, n., vulnerable-ness,  n., vulnerabl-y, adv.   vulnerary, adj., used for healing wounds. — L.  vulnerarius, ‘pertaining to wounds, used for  

vulture, n. — ME. vultur , fr. OF. voltour y voutour  (= F. vautour ), fr. L. voltur , vultur (whence also  Ruman. vultur , It, avoltojo , Proven£. voltor, Sp.  buitre , Port. abutrt) y lit. meaning ‘the tearing  (bird)’, and in gradational relationship to vellere ,  ‘to tear’. See vellicate and cp. prec. word and     vulnerable. Cp. also wolf,  vulturine, adj., pertaining to, or resembling, a  vulture. — L. vulturinus, ‘pertaining to a vul-  ture, vulturelike’, fr. vultur. See prec. word and  -ine (representing L. -irius).  vulturous, adj., 1) resembling a vulture; 2) rapa-  

wolf, n. — ME., fr. OE. wulf, rel. to OS. wulf  ON. ulfr, Swed. ulf OFris., Du., OHG., MHG.,  G. wolf, Goth, wulfs, fr. I.-E. *wjq H> os-, ‘wolf’,  whence also OI. vfkas, Avestic v & hrka-. Alb. ul'k,  OSlav. vluku, Lith. viJkas, Lett, vllks, OPruss.  w ilk is, ‘wolf’, and prob. also Gk. >.6xo^, L. lu-  pus, of s.m. I.-E. *w(q w os- possibly derives fr.  base *wel-, ‘to tear’, and prop, denotes ‘the  tearing animal’. See vellicate and cp. vulture.  Cp. also wolfram, wolverine and the second ele-  ment in werewolf, Adolph, Bardolph, Ralph,  Randal. Cp. also lupine, adj. andn., andlyceum.  Derivatives: wolf “ tr. v., to devour greedily;  intr. v., to hunt for wolves, wolf-ed, adj., wolf-er ,  n., wolf-ish , adj., wolf-ish-ly, adv., wolf-isk-ness  

35475:woolen cloth’, hence bureau orig. meant ‘table 
91307:wool, fleece’, Gk. wexstv, Att. 7 textelv, ‘to 
172939:woolly, hairy seed of certain plants’, fr. Gk.
```


## [2026-10-17T00:03:11.781Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; grep -n 'والانه\\|ولانه' BQT_v4_pages.txt BQT_v4_pages_faseng.txt | head; grep -n 'گرس\\b' BQT_v3_pages.txt | head -5; grep -n 'ورس' BQT_v4_pages.txt | head -5; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | grep -E '^(1794|1797|2253)' "
}
```


### [2026-10-17T00:03:12.326Z] TOOL RESULT

```
ugrep: warning: BQT_v4_pages_faseng.txt: No such file or directory
13597:‎٩‏ عولانه «سروری » « اسشق ۰۲۱*۷۵ سانسکریت -۷۳2۵18 ( زخم ) » قس‌:لاتینی
15084:ولانه ه « بفتح اول پروزن زمانه,بممنی است یمنی که ارواح موّمنان با خدای‌تعالی بدان
15099:۴ - ركسروری. ‏ #۶ ولادة (ولادت). 8 - «غفف‌والانه (۸م.) ‎٩‏ اکنون
15167:برخوان وی آندر میان خانه هم نان تنك بود و هم ولانه ۰ >
2350:‎SW py‏ بدان نگرستی بگرستی و صورت
6377:‏وشمانید. ‎pales‏ ازتعنگی ودمادم از گرسنگی؛ وغربووغرنگ»وغرن» «لفت‌فرس*#۱۲ومرادآ ست که
10027:۵ - ضرم ‎ci)‏ اول و دوم) (عر) سخت گرسنه گردیدن « تاج
14245:بانگه و دمدمه و نوحه دروقت گرستن‌را گوبند
16267:‎Vast‏ میگوبند . مصلح معده وجگرسردباشد.
69:ورسایلی که فقط یکی‌دوبار از آنها استفاده شده‌است) .
316:در مجلد چهارم از کتابها ورساله‌هایی استفاده شده است که نامآنها
645:ومطیع سازئدة مار ویرآورندة زهر باشد از پدن مارچوبه < با جیم قارسی بواورسیده
957:ماطو نیون - با طای حطی‌بواورسیده | حلوا (7) باشد وآیرا هاقوآی هم میکویند۹ -
1015:کرده ونوشته آند : « صحیح است » [ رس بمعنی طناب وکند ورسن است . رك : برهان فاطع :
```


## [2026-10-17T00:03:15.251Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; sed -n 13585,13600p BQT_v4_pages.txt; echo ====; sed -n 15080,15100p BQT_v4_pages.txt; awk 'BEGIN{RS=\"\\f\"} /سانسکریت -۷۳2۵18/ {print \"leaf\",NR-1}' BQT_v4_pages.txt"
}
```


### [2026-10-17T00:03:15.581Z] TOOL RESULT

```
Exit code 1
کل ی که بدان دیوار پرآرند . تزاری ( قهستانی گوید :

"بفال خجسته بعزم مصمم به بنیاد ثابت بوالان محکم. «رشیدی؟.
درینجا معنی دیوار هم صادق است. ۴ < والانکر (ر4 : ح») از : والاد (۸.ع) + کر
(پوند شغل ومبالفه ).8 - دوالان , رازبان » لیکن‌اسح آست که والان بردوقم است: والان
بز رکه رازبان؛ووالان خورد (خرد) شبت, وچون مطلق کوبند عبارت ازبادیان" باشد.» « رشیدی»
ورك : تحفةٌ حکیم موّمن : والان بز رکه , والان کوچك :

که فرمود ز اول که درد شکم را فرز باید از چین و از روم والان +

« ناصرخسرو بلخی . ص ۰۳۹۹

‎٩‏ عولانه «سروری » « اسشق ۰۲۱*۷۵ سانسکریت -۷۳2۵18 ( زخم ) » قس‌:لاتینی
598 * اسشق ایضاً » هوبشمان « ۱*۷۵ > کوید: ۷۵128 از - ۵۷8128 # هند وژرمانی
7 . لانینی ۷۵1819 ۳ هند و ژرمانی ۷۵1609 . ۷ #ولغونه ‏ از : ول
(ت کل)۳-غونه (گونه) قی : «آلفونه» * آلگونه (هم.) ۸ ولا (هم.) :
(eval):1: === not found
```


## [2026-10-17T00:03:33.779Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:2253 BQT:1794 BQT:1797; do echo \"######## $r\"; timeout 300 python3 tools/ref_page.py $r 2>&1 | head -150; done"
}
```


### [2026-10-17T00:03:41.988Z] TOOL RESULT

```
######## BQT:2253
(no exact page map; using offset -1917 -> pdf page 336; check the printed number and re-run with --pdf-page if off)
REF: BQT:2253  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 336  OCR-lang: fas

۳و۷ واله
وعمارت رنگین نقاشی کرده را هم میگویند ۱ » | وجراحت را کوبند .
وبستیدیواری‌را گفته‌اند که ازخنت پشتهرسنکه | اوالفو‌فه ۷.» باغین نقله دار بروزت
ی ۳ سرخی وسفیداب را گفته اند .
را دز گفته اند که در عمارت کردن بکار برند -
والادگر ۴ (۲) » بفتح کاف فارسی | واسوزانیدن » بمعنی تقلید کردن باشد پمنی
وسکون‌رای قرشت, بنا وعمارت کنند. راکوبند, | کفتگو و حرف زدن شخصی را بطربق آن‌شخصس
وبسی دیوارساز ودای کررا کفته‌اند وآن‌شخسی | واکفتن .
باشد که دیوارکلی‌را چینه‌چینه بربالای‌هم گذارد وال - بفتح ثالت وخفای‌ها بروزن‌لاله,
واو را بعربی رهاس خوانند بکر رای بی نقطه | پمعنی دویم والا است که نوعی از بافتةٌ ابربشمی
وهای مشدد بالف کشیده وصاد بی‌نقطه . باشد ۸ - از خشینهٌ سفید را نز کوبند و آن "
والان - پروزن‌نالان » بادیان‌را کوند پارچه است سفید و خود رنگه که آنرا سفید
که رازبانه باغده . نکرده باشند وهمجنان سفید بافته شده باشد -
والانه ۱ < بر وزن کاشانه » رش | وبمعتی سراب‌هم هت وآن چیزی باشد که در

(۱) چش :۳+ بنظر . (۲) خم۱: ولا نکر.

۷۱« در دخه میرزا ( ابراهیم ) عمارت رلگین و در موّید ( الفنلاء ) عمارت کلین
گفته » ‎٩‏ رشیدی >. ۴ - رشیدی کوبد: «ممنی اول ( رده دیوار ) اصح‌است. چه دراکش
اشمار مقابلهٌ بنیادآ ورده‌اند . آنوری ( ابیوردی ) گوید:

فلك را قدر تو والان عالی جهالر! حزم تو بنیاد محکم.
لیکن درین بیت و در بیت لزاری معنی دیوار نیز مناسب است » والانکر بنائی که دیوارچنه چنه
و رده رده بلند کند .> ورك : فرهنکه نظام . ۴ ۳ والان. » ردء دیوار » و بعضی گفته‌اند
کلی که بدان دیوار برآرند . بزاری ( قهستانی ) کوید :
بفال خجته بعزم مصمم به بنیاد ثابت بوالاف محکم. «رشیدی؟.
درینجا معنی دیوار هم صادق است. ۴ << والان کر (ر4 :ح۳) از : والاد («.ع) + کر
(پوند عغفل ومبالفه ‎٩6‏ - دوالان » رازبان » لیکن‌اسح آست که والان بردوقم است: والان
بز رکه. رازبان؛ووالان خورد (خرد) شبت, وچون مطلق کوبند عبارت ازبادیان" باشد.» « رشیدی»
ورك : تحفةٌ حکیم موّمن : والان بز رکه » والان کوچك :
که فرمود ز اول که درد شکم را فرز باید از چین و از روم والان ۰
ناصرخرو بلغی . ص ۰.۳۱۹

۹ "ولانه ۶« سروری » « اسشق ره ناکرت -۷۳۲214 ( زخم (" قی‌:لاتینی
5 « اسشق ایشا » هوبشمان « ۱*۷۵ > کوید: ۷۵1288 از - ۵۷8148 *هند وژرمانی
71 » لانینی ۷۵1819 * هند و ژرمانی ۷۵16209 . ۷ «ولغونه . از : ول
(ه کل) ۲ غونه (کوه) قی : «آلغونه» ‏ آلگونه (.م.) ۸ سوالا (و.م.) :

مرا زمفخر تبربز دلق کهنه بس است برو برو که بقد زنان بود واله .
مولوی بلخی رومی « جهانگیری *.

######## BQT:1794
(no exact page map; using offset -1205 -> pdf page 589; check the printed number and re-run with --pdf-page if off)
REF: BQT:1794  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 589  OCR-lang: fas

کردن نهادن : اهنجمنه
گردن نهادن - کدایه از فروتنی - و بالش کرد را نیز گفته‌اند - و بمعنی همه
کردن - وفرمانبرداری‌واطاعت نمودن (۱)نمودن | ومجموع هم هست- ویمعتی نگاه نیز (۲) آهده
باغد ‎٩‏ . رز امت - و بفتح اول ۸ خاکهٌ نقاشان باشد وآن
گرد نی کردن > کنانه از سر کی زغال سوده اس ت که در پارچه معه‌اند و برکاغد
ونافرمانی کردن باشد . های سوزن زده طراحی کرده مالند یا از آن‌طرح
گردو ۳ بکر اول وتات بواو و نقش بجای دیگر نشیند - وآن‌کاغذ سوزن‌زده
کشیده , کردکان را گوبند .9# را نی ز کوبند ‎٩‏ .
گردون سرشت - کندایه از مردم گرده آ الق - بنم اول . بمعنی آلو
صاحب عجب و تکبر و با وقار و تمکین و کاهل | کرد باشد » وآن میوه‌است شبیه پزردآ لو .
وتاموافق باشد ۴ گرده‌ بات - بابای‌ابجد بروزن‌اسفهان.
گردون مینا < کنابه از آسان بمعنی‌نگاهبان‌باشد چه گرده بمعنی‌نگاه هم‌آمده
: گرده پکسر اد رد کح نا ً کردم چرخ - کناها زآتاب‌است-
نوعی از بان غیر تنك باشد 6 - و «رچیز مدور
و گرد راگویند عموماً - وپارچهٌ زرد.مدوریرا که وماه را نیز کویند .
ازملمانان خصوصاً وآنرا بعربی‌غیار٩؟‏ خوانند ۷ | است که کنایه ازآفتاب وماء باشد .4

(۱) چش: - واطاعت. (۷) خم۱ :۳+ بنظر -

۱ -رك : رشیدی - وحاضر شدن برای کشته شدن «* فرهنگه نظام > -

۴ - از :کرد ( بکسر )+ و ( پسوند تصفیر , سازندة اسم از صفت ) » رك: کردکان .
درختی است ( 1181288 ) از دسَهٌ غان‌ها » باجوب محکم وبرگهای مرک ب که مغز آن روغن
بیاردارد. «کل کلاب ص ۲۷۸ 4 ۴ -رك : رشیدی . ۴ - از: گرد (بکر)+
شود . پهلوی 81718۷ * » ارمنی 871216 » معرب جردقه « هوبشمان ۹*۹ ۰

۹ - رك : غیار .

۷ -کرده پبردوش راهب دیرم حلقه درکوش ناجد لاتم . نزاری فهستانی «رشیدی»-

۸ - از :کرد ( بفتح )۰ ( دبت ) . ‎٩‏ - بم اول . بمعنی‌کلیه (ع) امت.
اوستا - ۷۵۲۵۵۵ ۰ -۷6۲۵1۵8 (کلیتین) » پپلوی 8۳1816 » هندی - پرا کربت -۷۲4
(کلیه) . کردی 870216 ۰ بلوچی 81111810 . وخی ]۷۵ ۶ اسشق ۹*۵ .

گردون - بفتح اول . از: کرد (کردیدن)+-ون ( پسوند فاعلی ) ۳ کردان.یپلوی
0 . 382۳1۵0 با 0۷27108 3۷27108 ۶ هوبشمان ۹*۶ ۰ ورك : اسشق ۹*۶ .
گردنده » چرخ - ارابه » کالسکه - آسمان , فلك . ۱

۲ گردیدن - بفتح اول و پنجم < گشتن . پپلوی 827111827 « بندهشنه۹ زو ها
00 اوستا - ۶۷2۳61 بارتولمه ۱۳۹۸ * » هندی‌باستان ۷2۳1216 « نیب رکه ص۲۳۹
نیز هندی باستان ۷8۳ [ گردیدن ۰ چرخیدن | ) « اسفا ۱: ۲ ص 6۹۹ کردی [ا ت۰1
( کرش کردن » گردیدن ) « ژابا ص ۳۹۱ ؛ دور زدن » چرخیدن - شدن ,گشتن - برکشتن,
تغبی رکردن - سرنگون شدن - سیر کردن »کردش کردن .

######## BQT:1797
REF: BQT:1797  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 592  OCR-lang: fas

-۱۷۹۵- کرشغب
گرست - بفتح اول و ثالی و سکون گرسنه چشم - بنم اول ونان کنایه
ثالثك و فوقالی » بمعنی سیاه مت باشد وبعریی | از بخیل و مك باشد - و مردم ققیر وکدا را
طافح کوبند ۱ - و بزبان علمی هند فرو بردن | هم میگویند 9 - وکنایه از مردمی‌هم هت که
لقمه و امثال آن باشد و عربان بلم خوانند. از قحط وغلا برآمده باشند .
گرستی ؟ » بکر اول وثانی »مخفف گرسنه چشمان کنعان - کنایه
گربستن است که کربه کردن باشد . از برادران بوسف علیه‌اللام است .
گرستودن ی * بفتح‌اول وثالی‌بروزن گرسیان > با بای‌حطی ونون وحر کت
تبفرودن » بمعنی کهان است وآن ترازو مانندی | غیرمعلوم » نوعی‌ازسنگه باشد وآن درهندوستان
است که بستها و تنگهای بار را بدان سنجند .| بهم میرسد ودر صنمت کیمیا بکارآید .
گرستون ۴ - بفتح اول ونانی بروزن گرسیوز ۱ - بنتح‌اولوتحتانیمجهول
شفق کون » بمعنی گرستودن است که قپان‌باشد- | بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
وبه‌عنی کیل وپیمالةٌ بز رکه هم‌آمده است‌ومعرب کاف تازی هم بنظرآهده است .
آن قرسطون باشد #۰ گرشاسب ۲ - باشین ضلهدار بروزن
۱ - باز رسید مت ما ء داد فدح بدست ما
کر دهدی بدست تو شاد و خوشی و کرستی -
مولوی بلخی رومی «جهانگیری» وبنابرین بیت با اول وسوم مفتوح وسکون دوم است .
۳۲ -مخفف گرستن: رك: لغت فری‌س4۹. ۴ - ظ. مصحف کرستون».رك: کرستون.
۴ << کرستون (۸.م.) < قرسطون. ر4: فرسطون .8 - وحاصل مصدر(اسم‌معنی) آن
«گرسنه چشمی » است . ‎۹٩‏ * کرسیوز . در اوستا ۳6۳۴۹8۷8248 ( از دو جزه :
2 لاغر واند4 , ۷۵208 فوت » پابداری ) ( بمعنی استقامت و پایدار یکم دارندء ) تم
برادر افراسیاب است « پورداود . بشتها ج ۱ ص ۲۱۱ ۷ - در شاهنامه بنام‌د و گرشاسب
برمیخورم : ۱- در برخی ازنخ شاهنامهٌ فردوسی( شاهنامة بخ اج ۱ص ۱۰۹ ح ) آندرعنوان
( تاخت کردن منوچهر برسپاه‌تور ) داستان بمیدان آمدن شیروی پپلوان تورانی و برزم طلبیدن
کرشاسب جهان پهلوان ایرانی » در ضمن سی‌وشش بیت آمده »که درنتیجه شیروی کشته شدم.
- ازگرشاسب پسر زو ( زاب ) ودهمین پادشاه پیشدادی که نه سال پادشاهی کرد » باد شهج
( خاهنامةٌ بخ ج ۱ ص ۲۸۲ ) . موضوع گرشاسب نامه اسدی طوسی همان کرشاسب نختی‌است.
گرشاسب در اوستا صورت 3676889802 و درسانسکریت 3۳928۷8 آهده مرکب از دوجزه:
اول 167658 بمعنی‌لاغر » جزء دوم 2888 همان اسب فارسی است [ دو 2 در اوستا تبدیل به 8
شده ] مجموعاً بمعنی دارندة اسب لاغر کس ی که اسبش لاغر است. بنابرین لغة اصح کرشاسب
بقیه در مفحةٌ ۱۷۹۹
گرسته - جم اول وکسر دوم و چپارم ( در لهجهٌ مرکزی ) و نیز ام اول و دوم و
فتح چهارم» و در شعر بضرورت بم اول و سکون دوم وفتح سوم و چهارم » پهلوی 811۳881 »
010 «اسشق ۹۰۷ تحرانی 81818088 ,گیلکی ۷191018 . مخفف آن «کرس» .«کتد»؛
ک ی که محتاج‌بخوردن غذاست ۰آنکه احای احتیاج بخوردن کند :
« کلتان ۰۳۶
```


## [2026-10-17T00:03:51.523Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 591 594; do echo \"######## $p\"; timeout 300 python3 tools/ref_page.py BQT:$([ $p = 591 ] && echo 1794 || echo 1797) --pdf-page $p 2>&1 | head -120; done"
}
```


### [2026-10-17T00:03:52.178Z] TOOL RESULT

```
######## 591
REF: BQT:1794  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 589  OCR-lang: fas

کردن نهادن : اهنجمنه
گردن نهادن - کدایه از فروتنی - و بالش کرد را نیز گفته‌اند - و بمعنی همه
کردن - وفرمانبرداری‌واطاعت نمودن (۱)نمودن | ومجموع هم هست- ویمعتی نگاه نیز (۲) آهده
باغد ‎٩‏ . رز امت - و بفتح اول ۸ خاکهٌ نقاشان باشد وآن
گرد نی کردن > کنانه از سر کی زغال سوده اس ت که در پارچه معه‌اند و برکاغد
ونافرمانی کردن باشد . های سوزن زده طراحی کرده مالند یا از آن‌طرح
گردو ۳ بکر اول وتات بواو و نقش بجای دیگر نشیند - وآن‌کاغذ سوزن‌زده
کشیده , کردکان را گوبند .9# را نی ز کوبند ‎٩‏ .
گردون سرشت - کندایه از مردم گرده آ الق - بنم اول . بمعنی آلو
صاحب عجب و تکبر و با وقار و تمکین و کاهل | کرد باشد » وآن میوه‌است شبیه پزردآ لو .
وتاموافق باشد ۴ گرده‌ بات - بابای‌ابجد بروزن‌اسفهان.
گردون مینا < کنابه از آسان بمعنی‌نگاهبان‌باشد چه گرده بمعنی‌نگاه هم‌آمده
: گرده پکسر اد رد کح نا ً کردم چرخ - کناها زآتاب‌است-
نوعی از بان غیر تنك باشد 6 - و «رچیز مدور
و گرد راگویند عموماً - وپارچهٌ زرد.مدوریرا که وماه را نیز کویند .
ازملمانان خصوصاً وآنرا بعربی‌غیار٩؟‏ خوانند ۷ | است که کنایه ازآفتاب وماء باشد .4

(۱) چش: - واطاعت. (۷) خم۱ :۳+ بنظر -

۱ -رك : رشیدی - وحاضر شدن برای کشته شدن «* فرهنگه نظام > -

۴ - از :کرد ( بکسر )+ و ( پسوند تصفیر , سازندة اسم از صفت ) » رك: کردکان .
درختی است ( 1181288 ) از دسَهٌ غان‌ها » باجوب محکم وبرگهای مرک ب که مغز آن روغن
بیاردارد. «کل کلاب ص ۲۷۸ 4 ۴ -رك : رشیدی . ۴ - از: گرد (بکر)+
شود . پهلوی 81718۷ * » ارمنی 871216 » معرب جردقه « هوبشمان ۹*۹ ۰

۹ - رك : غیار .

۷ -کرده پبردوش راهب دیرم حلقه درکوش ناجد لاتم . نزاری فهستانی «رشیدی»-

۸ - از :کرد ( بفتح )۰ ( دبت ) . ‎٩‏ - بم اول . بمعنی‌کلیه (ع) امت.
اوستا - ۷۵۲۵۵۵ ۰ -۷6۲۵1۵8 (کلیتین) » پپلوی 8۳1816 » هندی - پرا کربت -۷۲4
(کلیه) . کردی 870216 ۰ بلوچی 81111810 . وخی ]۷۵ ۶ اسشق ۹*۵ .

گردون - بفتح اول . از: کرد (کردیدن)+-ون ( پسوند فاعلی ) ۳ کردان.یپلوی
0 . 382۳1۵0 با 0۷27108 3۷27108 ۶ هوبشمان ۹*۶ ۰ ورك : اسشق ۹*۶ .
گردنده » چرخ - ارابه » کالسکه - آسمان , فلك . ۱

۲ گردیدن - بفتح اول و پنجم < گشتن . پپلوی 827111827 « بندهشنه۹ زو ها
00 اوستا - ۶۷2۳61 بارتولمه ۱۳۹۸ * » هندی‌باستان ۷2۳1216 « نیب رکه ص۲۳۹
نیز هندی باستان ۷8۳ [ گردیدن ۰ چرخیدن | ) « اسفا ۱: ۲ ص 6۹۹ کردی [ا ت۰1
( کرش کردن » گردیدن ) « ژابا ص ۳۹۱ ؛ دور زدن » چرخیدن - شدن ,گشتن - برکشتن,
تغبی رکردن - سرنگون شدن - سیر کردن »کردش کردن .

######## 594
REF: BQT:1797  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 592  OCR-lang: fas

-۱۷۹۵- کرشغب
گرست - بفتح اول و ثالی و سکون گرسنه چشم - بنم اول ونان کنایه
ثالثك و فوقالی » بمعنی سیاه مت باشد وبعریی | از بخیل و مك باشد - و مردم ققیر وکدا را
طافح کوبند ۱ - و بزبان علمی هند فرو بردن | هم میگویند 9 - وکنایه از مردمی‌هم هت که
لقمه و امثال آن باشد و عربان بلم خوانند. از قحط وغلا برآمده باشند .
گرستی ؟ » بکر اول وثانی »مخفف گرسنه چشمان کنعان - کنایه
گربستن است که کربه کردن باشد . از برادران بوسف علیه‌اللام است .
گرستودن ی * بفتح‌اول وثالی‌بروزن گرسیان > با بای‌حطی ونون وحر کت
تبفرودن » بمعنی کهان است وآن ترازو مانندی | غیرمعلوم » نوعی‌ازسنگه باشد وآن درهندوستان
است که بستها و تنگهای بار را بدان سنجند .| بهم میرسد ودر صنمت کیمیا بکارآید .
گرستون ۴ - بفتح اول ونانی بروزن گرسیوز ۱ - بنتح‌اولوتحتانیمجهول
شفق کون » بمعنی گرستودن است که قپان‌باشد- | بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
وبه‌عنی کیل وپیمالةٌ بز رکه هم‌آمده است‌ومعرب کاف تازی هم بنظرآهده است .
آن قرسطون باشد #۰ گرشاسب ۲ - باشین ضلهدار بروزن
۱ - باز رسید مت ما ء داد فدح بدست ما
کر دهدی بدست تو شاد و خوشی و کرستی -
مولوی بلخی رومی «جهانگیری» وبنابرین بیت با اول وسوم مفتوح وسکون دوم است .
۳۲ -مخفف گرستن: رك: لغت فری‌س4۹. ۴ - ظ. مصحف کرستون».رك: کرستون.
۴ << کرستون (۸.م.) < قرسطون. ر4: فرسطون .8 - وحاصل مصدر(اسم‌معنی) آن
«گرسنه چشمی » است . ‎۹٩‏ * کرسیوز . در اوستا ۳6۳۴۹8۷8248 ( از دو جزه :
2 لاغر واند4 , ۷۵208 فوت » پابداری ) ( بمعنی استقامت و پایدار یکم دارندء ) تم
برادر افراسیاب است « پورداود . بشتها ج ۱ ص ۲۱۱ ۷ - در شاهنامه بنام‌د و گرشاسب
برمیخورم : ۱- در برخی ازنخ شاهنامهٌ فردوسی( شاهنامة بخ اج ۱ص ۱۰۹ ح ) آندرعنوان
( تاخت کردن منوچهر برسپاه‌تور ) داستان بمیدان آمدن شیروی پپلوان تورانی و برزم طلبیدن
کرشاسب جهان پهلوان ایرانی » در ضمن سی‌وشش بیت آمده »که درنتیجه شیروی کشته شدم.
- ازگرشاسب پسر زو ( زاب ) ودهمین پادشاه پیشدادی که نه سال پادشاهی کرد » باد شهج
( خاهنامةٌ بخ ج ۱ ص ۲۸۲ ) . موضوع گرشاسب نامه اسدی طوسی همان کرشاسب نختی‌است.
گرشاسب در اوستا صورت 3676889802 و درسانسکریت 3۳928۷8 آهده مرکب از دوجزه:
اول 167658 بمعنی‌لاغر » جزء دوم 2888 همان اسب فارسی است [ دو 2 در اوستا تبدیل به 8
شده ] مجموعاً بمعنی دارندة اسب لاغر کس ی که اسبش لاغر است. بنابرین لغة اصح کرشاسب
بقیه در مفحةٌ ۱۷۹۹
گرسته - جم اول وکسر دوم و چپارم ( در لهجهٌ مرکزی ) و نیز ام اول و دوم و
فتح چهارم» و در شعر بضرورت بم اول و سکون دوم وفتح سوم و چهارم » پهلوی 811۳881 »
010 «اسشق ۹۰۷ تحرانی 81818088 ,گیلکی ۷191018 . مخفف آن «کرس» .«کتد»؛
ک ی که محتاج‌بخوردن غذاست ۰آنکه احای احتیاج بخوردن کند :
« کلتان ۰۳۶
```


## [2026-10-17T00:03:56.473Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py -h 2>&1 | head -30; command ls data/verification/sources/refs/ocr/BQT/ | grep -E '179|2253'"
}
```


### [2026-10-17T00:03:57.479Z] TOOL RESULT

```
expected ABBR:page (e.g. BQT:918 or MON5:528)
1793.png
1793.txt
1794.png
1794.txt
1795.png
1795.txt
1796.png
1796.txt
1797.png
1797.txt
2253.png
2253.txt
```


## [2026-10-17T00:03:59.912Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -n 'pdf-page\\|argv' tools/ref_page.py | head -20; head -3 data/verification/sources/refs/ocr/BQT/1796.txt"
}
```


### [2026-10-17T00:04:00.247Z] TOOL RESULT

```
6:    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping
31:def main(argv):
32:    args = [a for a in argv if not a.startswith("--")]
50:    if "--pdf-page" in argv:
51:        pdf_page = int(argv[argv.index("--pdf-page") + 1])
60:            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
84:    if "--image" in argv:
95:    sys.exit(main(sys.argv[1:]))
REF: BQT:1796  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 591  OCR-lang: fas

کرزه -۱۷۹-
```


## [2026-10-17T00:04:06.243Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; for f in 1794 1795 1796 1797; do echo \"== $f\"; head -4 $f.txt | tail -2; grep -n 'گرس\\b\\|گرس \\|گرگ\\|کرگ\\|ورس\\|لاتینی\\|اوستا' $f.txt | head -10; done; command ls | grep -E '^(179[89]|180[0-9])\\.'"
}
```


### [2026-10-17T00:04:06.767Z] TOOL RESULT

```
== 1794
کردن نهادن : اهنجمنه
گردن نهادن - کدایه از فروتنی - و بالش کرد را نیز گفته‌اند - و بمعنی همه
34:اوستا - ۷۵۲۵۵۵ ۰ -۷6۲۵1۵8 (کلیتین) » پپلوی 8۳1816 » هندی - پرا کربت -۷۲4
42:00 اوستا - ۶۷2۳61 بارتولمه ۱۳۹۸ * » هندی‌باستان ۷2۳1216 « نیب رکه ص۲۳۹
== 1795
شتمنه کرزن
گر ۱ -«بم اول وسکون نانی وزای کوبند ۴ ؛ و باکاف تازی هم بنظر آمده است.
24:۱ - پهلوی ۰۷227 اوستا- ۷2272 ۸ بارتولمه۱۳۹۲*. معرب جرز. ارمنی ع۷272هندی
33:اوستا 0438282 827۵6 . ۸۳۱288 827۵ پازند 82761۳128 ۰ مغدی ۰8۳27043388
== 1796
کرزه -۱۷۹-
و پیمانه پز رکه راکوبند ‎٩‏ سار آست که کرز فربدون باشد .
16:کاوپیکی است که کرز وه باه گرس - بنم اول و سکون نانی وسین
== 1797
-۱۷۹۵- کرشغب
گرست - بفتح اول و ثالی و سکون گرسنه چشم - بنم اول ونان کنایه
4:گرست - بفتح اول و ثالی و سکون گرسنه چشم - بنم اول ونان کنایه
8:گرستی ؟ » بکر اول وثانی »مخفف گرسنه چشمان کنعان - کنایه
10:گرستودن ی * بفتح‌اول وثالی‌بروزن گرسیان > با بای‌حطی ونون وحر کت
13:گرستون ۴ - بفتح اول ونانی بروزن گرسیوز ۱ - بنتح‌اولوتحتانیمجهول
14:شفق کون » بمعنی گرستودن است که قپان‌باشد- | بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
20:۳۲ -مخفف گرستن: رك: لغت فری‌س4۹. ۴ - ظ. مصحف کرستون».رك: کرستون.
22:«گرسنه چشمی » است . ‎۹٩‏ * کرسیوز . در اوستا ۳6۳۴۹8۷8248 ( از دو جزه :
30:گرشاسب در اوستا صورت 3676889802 و درسانسکریت 3۳928۷8 آهده مرکب از دوجزه:
31:اول 167658 بمعنی‌لاغر » جزء دوم 2888 همان اسب فارسی است [ دو 2 در اوستا تبدیل به 8
34:گرسته - جم اول وکسر دوم و چپارم ( در لهجهٌ مرکزی ) و نیز ام اول و دوم و
1800.png
1800.txt
1802.png
1802.txt
1803.png
1803.txt
1803.vision.txt
1806.png
1806.txt
1807.png
1807.txt
1809.png
1809.txt
```


## [2026-10-17T00:04:12.820Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; for p in 593 594; do pdftoppm -f $p -l $p -r 110 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt540-$p; done; pdftoppm -f 540 -l 540 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg540; command ls $S | grep 540"
}
```


### [2026-10-17T00:04:14.688Z] TOOL RESULT

```
bqt540-593.png
bqt540-594.png
pg540.png
```


## [2026-10-17T00:04:21.140Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg540.png"
}
```


### [2026-10-17T00:04:21.617Z] TOOL RESULT

```

```


## [2026-10-17T00:04:21.613Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:04:25.055Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt540-594.png"
}
```


### [2026-10-17T00:04:25.080Z] TOOL RESULT

```

```


## [2026-10-17T00:04:30.031Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 591 -l 591 -r 130 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt540-591; sed -n 10,40p data/verification/sources/refs/ocr/BQT/1796.txt"
}
```


### [2026-10-17T00:04:30.994Z] TOOL RESULT

```
میگویند - و بم اول, هم بممتی اول‌وهم‌یمعنی | وعلاجکردن است .
کرز باشد که عربانعمود کوبند 9 . گرزیی ۸ - بکسراول بروزنمسکن.
گرزة ماو پیکر ۱ - کرزفربدون | تاج کیانیرا کویند و آنرا مرصع ساخته از بالای
را کوبند چه آنرا بهیأت سر کاومیش از فولاد تخت محاذی‌سرابشان بازاجیر طلاآ وبشته‌بوده‌اند
ساخته بودند . - وبمعتی زبیل هم‌آمده است - و تیر پیکان‌دار
گرزة او چهر ‎٩‏ - پنسرکرده ۱ دانیزگت‌الد :
کاوپیکی است که کرز وه باه گرس - بنم اول و سکون نانی وسین
و ت‌ د فر«دون باشد . - ۰
۰ بی‌نقطه »کرسنگی راکویند که در مقابل سیری
گر زة‌گاوسار ۱ - بسمنی کرزء کاو است ‎٩‏ - و بمعنی چرك وریم جامه و بدن هم
چهراست که عمود فربدون باشد. آمده است - وموی پیجیده وموی پیچه را لیز
گر زة گاوسر ه بمعنی کرزةکاو | گفته‌اند که موباف زنان باشد *۹.
)۱( چش : - وآنرا بودند .
ک ککگ اااا ‏ ای
۱ - قی :کرزن « دزی ج ۲ ص 400 ‎ »‏ ورك : هرمزدنامه ی ۸-۳۰۷ « نم‌تاجی
بود از دیبا بافند بزر و کوهر مغرق کرده . وکوبند ناجی بود بز رک وزین پرجواهر ومئوك ازبر
او میر لیکوان جهادت و نیکوبی تاجست وسال وماه مر اورا چوکرزنست .»
« لغت فری ۳۵۹ .
۴ - بدی مار کرزه است , از او دورپاش که بد بدتر از مارکرزه کزد .
ناصرخرو بلخی . دیوان ص ۱۱۲ *.
۴ - مرادگیلان است. ۴ - درلاهیجان وحوالی آن 88728 (موش) «میررفمتی»
۵ «کرز(هم.) ‎٩‏ -ر4 :کاوپیکر ‎ .‏ ۷ - مصحف «کزریدن > * کزردن
رك : کرزدن » ۸ - رك :کرزن . ‎٩‏ ۳ کوری , رك : کرسته ,کشنه » کاشانی
۷۵۵, 4ط۷۶ , 6ط۶ع۷, نوعط۰۷6۶ پهلوی 8075۵۴ طْ801798, 81751138 ؛ کردی
۷1 . 1وز۷۵۲۶ , ۰۷852 بلوچی ع۰8150886 شفنی8191088 « اسشق ۹*۷ ۲ ۰ شکل
پارسی باستان - 8۷۳۲98, 0۷۳588 هوبشمان ۹*۷ > رك : «کرسنه > (ه.م.) ورك : رشیدی و
کری‌ازدلم یبرد غم زلف وخال دوست ‏ جان باخیال رشته فتاد ازخیال‌دوست. بحاق اطعمه.
اما در دیوان بحاق چاپ قطنطنیه ص ۳۸ بجای کرس « جوع > وبجای خیال اول در مصراع
دوم « حبال > آمده است . رك : اسشق - هوبشمان ۹*۶۸ ۰
(برهان قاطمه۲۳)
```


## [2026-10-17T00:04:36.975Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wars\\b\\|wars ' SNS_pages.txt | head; grep -n 'ورس\\|وریس' incoming/BQT/BQT_v4_pages.txt | head; grep -n 'ورس\\b' MON_part2.txt | head -5; grep -n 'والانه' MON_part2.txt MON_part1.txt | head"
}
```


### [2026-10-17T00:04:37.551Z] TOOL RESULT

```
69:ورسایلی که فقط یکی‌دوبار از آنها استفاده شده‌است) .
316:در مجلد چهارم از کتابها ورساله‌هایی استفاده شده است که نامآنها
645:ومطیع سازئدة مار ویرآورندة زهر باشد از پدن مارچوبه < با جیم قارسی بواورسیده
957:ماطو نیون - با طای حطی‌بواورسیده | حلوا (7) باشد وآیرا هاقوآی هم میکویند۹ -
1015:کرده ونوشته آند : « صحیح است » [ رس بمعنی طناب وکند ورسن است . رك : برهان فاطع :
1569:هرفن - وزیرك ورسا در هرامن - و ليك شناور » مهرة محر كة جمع > * منتهی‌الارب > .
2086:نام جانوریست که اقسام غله را خایع کند و آنرا مخت (۱) - بن اول و اسکون نانی
2711:که از کندم و کاورس و جو میازند - و مقعد آمده است که بفتح ثالك باشد - و عربان مهت
2717:مخرج سقلی هم آمده است ‎٩‏ - و موش رالیز | است - وکورستان وقبرستانر| نیز کفته‌اند.
2720:فارسی ۰ نام یکی ازآتش پرستان است . وبکسر | وکورستان - وآتغدان باشد ۱۴.
1510:غریبان» خانهٌ غرباء. (کد.) گورستان» مقبره. 
11162:که مردگان را در 5 دفن کنند؛ گورستان. 
11725:تمام راه رفتن. . قدم نورسیده مار کك!: به 
14706:است که ۵ از ره ورس تما آگاه نباشی 
19762:ذرت و گاورس را گویند که هم به مصرف 
MON_part2.txt:87260:ولانه: (م«مقاده ز- والانه] (.) جراحت»
```


## [2026-10-17T00:04:40.509Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:04:40.523Z] TOOL RESULT

```

```


## [2026-10-17T00:04:42.326Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/व्रण",
 "prompt": "Give the Sanskrit etymology of vraṇa 'wound' exactly as stated, including PIE root and cognates."
}
```


## [2026-10-17T00:04:43.139Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/vulnus",
 "prompt": "Give the Latin etymology of vulnus exactly as stated."
}
```


## [2026-10-17T00:04:43.889Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/vultur",
 "prompt": "Give the Latin etymology of vultur exactly as stated."
}
```


## [2026-10-17T00:04:44.825Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گرگ",
 "prompt": "Give the Persian etymology of gorg 'wolf' exactly as stated, with Middle Persian, Proto-Iranian, PIE forms."
}
```


## [2026-10-17T00:04:46.321Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wĺ̥kʷos",
 "prompt": "Give the etymology note (any link to *welh- 'tear') and the Indo-Iranian, Avestan, Old Persian, Sogdian, Persian, Germanic descendants."
}
```


## [2026-10-17T00:04:47.486Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wĺ̥h₁neh₂",
 "prompt": "Give the etymology and descendants (Germanic *wullō, English wool, Latin lana, villus/vellus, any Iranian) for PIE wool."
}
```


### [2026-10-17T00:04:50.773Z] TOOL RESULT

```
# Latin Etymology of *vultur*

According to the Wiktionary article, the etymology is stated as follows:

"Perhaps from the same source as _[vellere](/wiki/vellere#Latin "vellere")_ ("to tear, pluck"), but the ending is unclear."

The article further notes that despite observations about potential connections to the word *turtur* ("dove") as a rhyming formation, there remains significant scholarly doubt about reconstructing a hypothetical proto-form.
```


### [2026-10-17T00:04:51.521Z] TOOL RESULT

```
# Latin Etymology of Vulnus

According to the Wiktionary entry, the Latin etymology is stated as follows:

"From Proto-Italic *welanos, perhaps from Proto-Indo-European *welh₃- ('to hit'). Cognate with Latin vellō."

The entry indicates the word traces back through Proto-Italic to a possible Proto-Indo-European root meaning "to hit," with a related Latin verb being vellō.
```


### [2026-10-17T00:04:51.864Z] TOOL RESULT

```
# Etymology Note on *welh₂-

The document mentions an alternative etymological possibility: "the word may be a derivative of the verbal root *welh₂- ('to tear up')."

# Indo-Iranian Descendants

The page lists **Proto-Indo-Iranian: *wŕ̥kas** with a note directing readers to "see there for further descendants," but it does not provide specific details about Avestan, Old Persian, Sogdian, or Persian reflexes on this page.

# Germanic Descendants

For Germanic, the document specifies **Proto-Germanic: *wulfaz** and notes that most Germanic reflexes underwent unusual sound changes. Examples include Old English *wylf* and Middle High German *wülpe*.

The page does not contain information about Avestan, Old Persian, Sogdian, or Persian descendants beyond the general Proto-Indo-Iranian reference.
```


### [2026-10-17T00:04:51.928Z] TOOL RESULT

```
# Sanskrit Etymology of व्रण (vraṇa)

According to the Wiktionary source, the Sanskrit etymology is stated as follows:

The word may derive from Proto-Indo-European **\*wer-** meaning "to cut, scratch, tear, sketch an outline." 

Cognate languages include:
- Armenian *գիր* (gir, "letter")
- Ancient Greek *ῥινός* (rhinós, "skin")
- Russian *рана* (rana, "wound")
- Old High German *rīzan* (modern German *reißen*)
- Old English *wrītan* (modern English *write*)
```


### [2026-10-17T00:04:52.049Z] TOOL RESULT

```
# Persian Etymology of گرگ (gorg) "wolf"

According to the Wiktionary entry, the Persian word derives as follows:

The term is "inherited from Middle Persian 𐭢𐭥𐭫𐭢 (gʿlg /gurg/), from Old Persian 𐎺𐎼𐎣 (v-r-k /varka-/), from Proto-Iranian *wŕ̥kah, from Proto-Indo-Iranian *wŕ̥kas, from Proto-Indo-European *wĺ̥kʷos."

The source notes this PIE root may derive from an adjective meaning "dangerous," though this connection is presented as uncertain ("possibly from").
```


### [2026-10-17T00:04:52.673Z] TOOL RESULT

```
# PIE *h₂wĺ̥h₁neh₂ (Wool): Etymology and Descendants

## Etymology

The term derives from "*h₂welh₁-" meaning "hair; wool" combined with the suffix "*-néh₂". An alternative pre-Anatolian form was "*h₂ulh₁nos".

## Major Descendants

**Germanic:** Proto-Germanic "*wullō" developed into English "wool" and related Germanic terms.

**Italic:** The form evolved into Latin "lāna" (wool), which produced Romance descendants and also Latin "villus" and "vellus" (fine hair/fleece).

**Greek:** Proto-Hellenic "*wlḗnos" became Ancient Greek "λῆνος" (lênos).

**Balto-Slavic:** Descended as "*wílˀnāˀ" with further development in individual languages.

**Celtic:** Produced Proto-Celtic "*wlanā".

**Iranian:** Proto-Indo-Iranian "*Hwŕ̥HnaH" developed into various Iranian language forms.

**Anatolian:** Possibly reflected in Hittite "ḫulanaš" (marked with uncertainty).

The word represents a thematic feminine noun in the *-eh₂ stem class, showing consistent meaning across Indo-European branches.
```


## [2026-10-17T00:04:54.913Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/velvet",
 "prompt": "Give the etymology chain of velvet."
}
```


## [2026-10-17T00:04:55.572Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/gorgan-iv",
 "prompt": "What does it say about the name Gorgan / Hyrcania / Varkāna and its etymology (wolf land)?"
}
```


## [2026-10-17T00:04:56.548Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ورس",
 "prompt": "Quote the Mo'in entry for ورس / وریس (varas), especially any meaning about hair or a string in Zoroastrian ceremonies, and its etymology."
}
```


### [2026-10-17T00:04:57.341Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:04:57.352Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:05:01.062Z] TOOL RESULT

```
# Mo'in Dictionary Entry for ورس (Varas)

According to the Mo'in Dictionary entry displayed, **ورس** has two primary definitions:

1. "طنابی که از خوشه های خشکیدة برنج باشد" – a rope made from dried rice stalks

2. "ریسمانی که از موی گاو بافته می شود و شاخه های برسم را با آن به هم می پیوندند" – a cord woven from cow hair used to bind branches in fire temples

The second meaning specifically relates to ceremonial use in Zoroastrian fire temples (آتشگاه), making it a string employed in religious contexts.

The entry does not provide etymological information in the section shown. The page indicates additional meanings exist under "ورس (2)" and references to the same word appear in other Persian dictionaries (Dehkhoda, Amid, and Mazani dialect dictionaries) available through the same resource.
```


## [2026-10-17T00:05:07.115Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -n -i 'wars\\|vars\\b' data/verification/sources/refs/SNS.txt | head -5; grep -n -i 'gurgan\\|gorgan' data/verification/sources/refs/PHD_mackenzie.txt | head -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/व्रण' --note 'page 540, root Wel 2: Skt vrana etymology (PIE *wer-)' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vulnus' --note 'page 540, Wel 2: Latin vulnus'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/vultur' --note 'page 540, Wel 2: Latin vultur uncertain'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/گرگ' --note 'page 540, Wlkwo: Persian gorg'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wĺ̥kʷos' --note 'page 540, Wlkwo root'; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wĺ̥h₁neh₂' --note 'page 540, Wela wool root'; python3 tools/fetch_source.py 'https://vajehyab.com/moein/ورس' --note 'page 540, Wela: Mo in varas cow-hair cord for barsom' 2>&1 | tail -20"
}
```


### [2026-10-17T00:05:09.525Z] TOOL RESULT

```
5763:^if/fc. 401-403) urvSra : ^j-*^ urvarS-: t - 
10616:. 6/ Y^. i J U:.syawarsan s©i-CAiffl>. 1631)syava- jfc- 
15617:»*• 'o-jj :vars: -OJ> 
30840:vars 280/13 
2628:gurganig [gwlg'nyk l I N ......,i] of (the province) Gurgan.
5160: - i gurganig: pistachio tree.
7290:   gurganig.                               populous abad.
/home/sfmqrb/git/rishe-private/data/verification/sources/web/91c5e63cffb1e302.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/404ff786c0acdbef.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5bf4bde7a46f6ed9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae19f932ce0cfd3f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/16f3b746f4c6fe18.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6a705dda3a88f075.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dcd269fddb2bbf71.txt
```


## [2026-10-17T00:05:13.369Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 15610,15622p SNS.txt; sed -n 30836,30842p SNS.txt; grep -n 'vars\\b\\|vars ' SNS_pages.txt | head -3; echo ---IEC; grep -n -i '^wl.k.o\\|^wlk\\|^w.l.kwos\\|^wlna\\|^wl.na' IEC.txt | head; echo SYN; grep -n -i 'Av. v.hrka\\|vəhrka\\|v.hrka-' SYN.txt | head -3; grep -n -i 'varəsa\\|var.sa-' SYN.txt | head -3; echo WLD; grep -n -i 'vehrka\\|v.hrka\\|varesa\\|var.sa-\\|vrana\\|vraṇ' incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:05:13.953Z] TOOL RESULT

```
\ 



•Vi/VY* jl « J r^ J, '^JJJ:varzId: 1^ *h 
■ Y/VTiS .^.^^l,.^ :varzed:>^^l 

»*• 'o-jj :vars: -OJ> 
! i«'er- Wt^.l374)vSlSa-: 4 jfS rf -3- va rdsa- : 6. 
\ \f\b>S -jS^'/ivarsavIr : 

.T/T^.J-^(t) .1/1.^ •4t**a*jf<*».(ft) varcrDao: *>' 
(AWi-.Jtan.IIl,63)wrg : >* («**.. tf fl «. I,38)wrg , aM 
varSmandlh 279/10 
varSraand kardan 279/8 
varra 280/18 
varra kardan 281/2 
vars 280/13 
var ud goraSz 278/17 
varz 209/2-280/3 
11210:                                                                                                                                                                           »*• 'o-jj   :vars: -OJ>
15706:vars 280/13
---IEC
SYN
4946:ANIMALS 185 3.71 WOLF Goth. wulfs Lith. vilkas J, Noxos ON ulfr, vargr Lett. vilks ce oKos Dan. ulv ChSl. luk Be lupus Sw. varg, ulv SCr. vuk re [upo OE wilf Boh. lk Ir. loup ME wolf Pol. = wilk gp. lobo NE wolf Huss pelh , lp. 5 j Du. wolf 5 ur. aa facl, teat eto OHG wolf Av. __ vahrka- Nir. ct rely MHG wolf slaidd NHG wolf wy bleiz
1535:142 TREE Grk.  dé5pov Goth. bagms Lith. medis NG ba Spov ON tré, badmr (poet.) Lett. kuoks Lat. arbor Dan. ire t ChSl. drévo, dqbit It. albero Sw. irdd SCr.  drvo Fr. arbre OE tréow, béam Boh. strom Sp. Grbol ME ttre Pol. drzewo Rum. —arbore, copac NE tree Russ. derevo Ir. crann, fid Du. boom Skt. urkga-, vana-, dru- NIr.  crann OHG boum ma-, etc. W. coeden, pren MHG boum Av. vand- (varasa-?) Br. gwezenn NHG baum
1565:8. Skt. vrksa- ‘tree’, Av. varasa- ‘tree’ or ‘woods’ (? cf. Barth. IF 9.273, ftn.), etym.? Walde-P. 1.286, 289.
5376:414 HAIR tly distinguished as a) of the Head, b) of the Body, of Animals) ar s (P PEO) Goth. tagl, skuft (a) ae poe Sate (b) oplt, pi. Pixs) ON har, skopt (a) ett. mats, spalva (b) Gr year pexes 187 a ChSl. last NG 70lxe FE ) Dan. haar padded a ), erimis Sw. hdr SCr.  vlas, kosa (a), dlaka Lat. capillus , (a), Bi- OE har, feax (a) OF ie : ME here, fax (a) Boh we oak (a), pelo (b) NE hair ae wi i ae ae (a), poi Du. =—haar uss. volos _ _ chevett ‘ Ma (a) OHG shar, fahs (a) Skt. _ keca- (a), roman- (b) anne piel} cave MHG har, vahs (a) Av. varasa- (2), gaona- (b) Rum. NHG _ haar
WLD
27459:  Auch Ciardi-Dupres KZ. 44, 122 Deutung von ai. crkSd-, av. varasa- m.
29066:gwallt ..Ilaar" (Pedersen KG. II 29). — Ai. vrana- .(Wunde                                                     •
30154:      Ai. vrka-m. ..Wolf     vrki „W6lfin“, av. vJhrka- „Wolf“ (geneuertes
30158: Fern. V9hrka); arm. (jail „Wolf (Hubschmann Arm. Gr. I 431, s. zum Laut-
41107:Haar" (Scheftelowitz BB. 28, 282, fur die Bed. ,,Haar‘ sich auf av. varasa-
```


## [2026-10-17T00:05:17.366Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29055,29075p incoming/WLD/WLD_Bd1_pages.txt; echo ----; sed -n 30148,30160p incoming/WLD/WLD_Bd1_pages.txt; echo; for n in 29066 30154 41107; do awk -v L=$n 'BEGIN{c=0} {if(NR==L){print \"leaf\",c; exit} n=gsub(/\\f/,\"&\"); c+=n}' incoming/WLD/WLD_Bd1_pages.txt; done; sed -n 41100,41110p incoming/WLD/WLD_Bd1_pages.txt; sed -n 5380,5400p SYN.txt | grep -i -o '.\\{150\\}varasa.\\{200\\}'"
}
```


### [2026-10-17T00:05:17.843Z] TOOL RESULT

```
44, 438), lat. vcllo, -ere, rclli und colsi ( vulsi ), rolsum ( vulsum ) ..rupfen,
zupfen, raufen; ausreiBen, ausrupfen, abzupfen" (iiber abweichende Deu-
tungen s. Yf. LE\Yb. 2 s. v ), volfur ..Geier" \*uel-tor ..ReiBer"; nicht etrusk.
nach Miiller-Deecke 2 I 455) got. icilwan „rauben‘f wuhai ..Raub" (nicht
                                            ;


als „sich beibiegen" zu *nd- ,.drehen‘‘, eiAvm ): Solmsen KZ. 32, 279 f. z. T.
nach Curtius 557).
   Cymr. giccllaif         ,
                               acorn,    guillihim         „Schere‘‘                  (Fick II 4 27 7 j       vielmehr von
gwallt ..Ilaar" (Pedersen KG. II 29). — Ai. vrana- .(Wunde                                                     •
                                                                                                                hat idg. r,
s. Yf. LEWb.
             2
               u. volnus, Persson Beitr. 277 f.                                       — Ganz zweifelhaft              ai.   liin-
thati ,,riihrt auf“, hotihuyati lothayati ,.raubt. pliindert"                                        (Johansson KZ. 32,
454, 471 zw. Uhlenbeck Ai. Wb. s. v.; In- aus ul-'i                                             i.   — tjber       lat.   veil us
und andere bedeutungsahnliche Worte s. *ud- „Haar".
   Im Germ, die Weiterbildungen mnd. wletr.     f. „Wunde, SchmiB”, mhd.
letzen ,,verletzen“' (idg.       Fick III 4 402; nicht nach Wood KZ. 45,
----
 doch gehoren beide lat. Worte eher zu reu-, rea-b- „aufreiBen“ (s. d.).

 ujqUos           „W olf   ‘    (daraus *luq20S in gr. Ivxog,                                 s.   Froehde BB.           14,    107;
                                                                                     1
         Siitterlin IF. 25, 6, 8, 75), iilq“I                          .,   Wolfin' .
                                               1
      Ai. vrka-m. ..Wolf     vrki „W6lfin“, av. vJhrka- „Wolf“ (geneuertes
                                                   ,


 Fern. V9hrka); arm. (jail „Wolf (Hubschmann Arm. Gr. I 431, s. zum Laut-
                                                             ‘
                                                                                        ;

leaf 313
leaf 324
leaf 439
Schwanz" (Bed.-Parallelen                   fur   „Stab-Schwanz" bei Scheftelowitz IF. 33,
    143); apr. kelian „Speer" mit westidg. k fur /.', Zupitza KZ. H7, 400; freilich
auch      (.„schneiden“ als „abgeschnittene Latte" beziehbar, wie schlieB-
            s)qel
lich auch   cad, celt air ); unsicherer arm. safari ,,belaubter Zweig, langes
                ir.

Haar" (Scheftelowitz BB. 28, 282, fur die Bed. ,,Haar‘ sich auf av. varasa-
.   Haar" ai. rale a- „Zweig“ berufend).
432                                                          kel-
```


## [2026-10-17T00:05:22.261Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i 'WOLF\\|GORG\\b\\|GURG' ARY_latin_index_pages.txt | head -5; grep -n 'گرگ' ARY_pages.txt | head -5; grep -n -i 'GORS\\|VARAS\\|VALANE' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:05:22.598Z] TOOL RESULT

```
12545:LOBO ASPANISH) libel GURG PAHLAVI) 5 349, at
12556:VK (BOHEMIAN) go WOLF (OLD FRISIAN) oS 52.9
12557:VLK SLOVAK) 51 jut WOLF (OLD HIGH GERMAN) AS gist
12558:VILKAS, VILKE LITHUANIAN) aly WOLF (GERMAN) git
12561:ULIPPAN HITTITE) <2» WOLF ENGLISH) 5-36
262:این اصل چنین است: زبانهای درو نگهواره و اطراف آن یشتر دستخوش نوآوری و دگرگونی
279:ویژه سکایی و سارماتی و اوستی)» برعکس لیتوانی و سلتی» دستخوش نو آوری و دگرگونی بیشتری
295:داشتند. واژه‌های همریشه‌ی «خرس» و «گرگث» و دقازه و «راش» (882614) و «غان» (81071) و
308:است و در زبانهای دیگر به گیاهان متفاوتی اطلاقی می‌شود. علت این دگرگونی آشکار است.
391:محسوب می‌شدند) به وجود آمدند. به همین دلیل این زبانها «پست» هستند و مرتباً دگرگون
3110:WILLA, WELLA VARASA, VARAYATI, VRTA, VRNATI
6580:KETYRE, CHETYRE CATVARAS, CATASRAS, CATVARI
7740:DRZWI (POLISH) tng! DVARAS SANSKRIT) ep Sunil
12404:GORSTU, GURTI (LITHUANIAN) gly GARAN _ HPAHLAYD 8 4,
12501:GLADU GORSNEH KURDISH) 52,5
```


## [2026-10-17T00:05:25.304Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'BEGIN{RS=\"\\f\"} /GURG PAHLAVI/ {print NR-1; print substr($0,1,300)}' ARY_latin_index_pages.txt | head -8; grep -n '\\[pdf page' ARY_latin_index_pages.txt | awk -F: '$1<12545' | tail -1; grep -n 'VEHRKA\\|VAHRKA\\|VARKANA\\|GURGAN' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-17T00:05:25.696Z] TOOL RESULT

```
429
[pdf page 430]
wh 1 SS |
(OLD CHURCH SLAVIC) pS 5%) GRIFTAN, APAHLAVD) 5 i,
GRABITI, GREBT GARAFTAN
GRABIC POLISH) lg) GIRTIN KURDISH) 52,5
GREBU AARUSSIAN) go GIRAG HBALUCHI) gr ge
HRABATI (CZECH) So GRABH., (SANSKRIT) 2 Snile
12521:[pdf page 430]
12544:LOUP FRENCH) sil VARKANA  :(OLD PERSIAN) surly gj),
```


## [2026-10-17T00:05:48.891Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 438 439 440 441 442; do awk -v L=$l 'BEGIN{RS=\"\\f\"} NR==L+1' KLN_1966.txt | grep -o -i '^[a-z-]*, [a-z]*\\.' | head -2 | tr '\\n' ' '; echo \" <leaf $l\"; done; for l in 885 886 887 888; do awk -v L=$l 'BEGIN{RS=\"\\f\"} NR==L+1' KLN_1966.txt | grep -o -i '^wol[a-z]*, \\|^wool[a-z]*, \\|^1750\\|^ *17[45][0-9] *$' | head -3 | tr '\\n' ' '; echo \" <leaf $l\"; done"
}
```


### [2026-10-17T00:05:49.688Z] TOOL RESULT

```
 <leaf 438
 <leaf 439
 <leaf 440
 <leaf 441
 <leaf 442
 <leaf 885
 <leaf 886
 <leaf 887
 <leaf 888
```


## [2026-10-17T00:05:52.420Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nprint(len(t))\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'^wolf, n',p,re.M) or re.search(r'^lanugo, n',p,re.M) or re.search(r'^lana',p,re.M): print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',p,re.M)[:3], p[:80].replace('\\n',' '))\nE"
}
```


### [2026-10-17T00:05:53.245Z] TOOL RESULT

```
903
464 ['864', '865'] ‘tongue;  language’.  Cp.  next  word  and  languet. langued,  adj.,  having  th
```


## [2026-10-17T00:05:58.102Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in (459,460):\n    p=t[i]; print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',p,re.M)[:3], re.findall(r'^([a-zA-Z-]+), (?:n|adj|v)',p,re.M)[:40])\nfor i in range(880,903):\n    if 'wolf' in t[i].lower() and 'vulture' not in t[i].lower(): \n        m=re.search(r'wolf, .{0,300}',t[i],re.S)\n        if m: print(i, re.findall(r'^\\s*(\\d{3,4})\\s*$',t[i],re.M)[:3], m.group(0)[:300].replace('\\n',' ')); break\nE"
}
```


### [2026-10-17T00:05:58.570Z] TOOL RESULT

```
459 ['852', '853', '1967'] []
460 ['857'] []
883 ['1666'] wolf,  Goth,  twalif.  These words  are  compounds  meaning  lit.  ‘two  left  after (ten)’,  ‘two  added  (to  ten)’.  For  the  first  element see  two.  The  second  element  is  cogn.  with  L.  lin- quere,  Gk.  Aeitteiv,  ‘to  leave  behind’ ;  see  loan, relinquish  and  ep.  eleven.  Outside
```


## [2026-10-17T00:06:02.386Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in range(880,903):\n    nums=re.findall(r'^\\s*(1[67]\\d\\d)\\s*$',t[i],re.M)\n    print(i,nums[:3], 'wulf' in t[i], 'vehrka' in t[i].lower() or 'hrka' in t[i])\nE"
}
```


### [2026-10-17T00:06:02.889Z] TOOL RESULT

```
880 ['1661', '1662'] False False
881 [] False False
882 [] False False
883 ['1666'] False False
884 [] False False
885 [] False False
886 [] False False
887 ['1675'] False False
888 ['1676'] False False
889 ['1679'] False False
890 ['1680'] False False
891 [] False False
892 [] False False
893 [] False False
894 [] False False
895 ['1691'] False False
896 ['1692'] False False
897 [] False False
898 ['1694', '1695'] False False
899 ['1696'] False False
900 [] False False
901 [] False False
902 [] False False
```


## [2026-10-17T00:06:07.242Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('KLN_1966.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nimport re\nfor i in (459,460):\n  for m in re.finditer(r'.{0,120}(wool|vars|hair|Avestic).{0,160}',t[i]): print(i, m.group(0).replace('\\n',' '))\nE"
}
```


### [2026-10-17T00:06:07.732Z] TOOL RESULT

```
460 Lachnanthes,  n.,  a  genus  of  plants,  the  redroot ( bol .)  —  ModL.,  compounded  of  Gk.  Xayvv), ‘woolly  hair’,  and  avffop,  ‘flower’.  The  first  ele¬ ment  prob.  stands  for  *fXxx-av- a,  fr.  I.-E. *wolk-o-,  whence  also  Avestic  varesa-,  ModPers. gurs,  OSl
460 av.  vlasu,  Russ,  volos,  ‘hair’;  for  the second  element  see  anther.  The  genus  was  so called  in  allusion  to  the  woolly  flowers, lachrymal,  also  lacrimal,  adj.,  1)  related 
460   dingua),  ‘tongue’,  L. levir  (for  I.-E.  *daiwer)  ‘husband’s  brother’.  Cp. also  L.  solium  (for  *sodium),  ‘chair  of  state, throne’,  which  is  rel.  to  sedere,  ‘to  sit’,  olere  (for *odere),  ‘to  smell',  which  is  rel.  to  odor,  ‘smell’, and  mdlus  (for  *maz
```


## [2026-10-17T00:06:15.292Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg540.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/540.png; cat > /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1794.vision.txt <<'E'\n[Read from BQT_v3_picofile.pdf pdf page 591 (= printed p. 1794; the cached 1794.txt/1796.txt OCR are mislabelled by two pages: pdf 594 = printed 1797)]\nگرس - بضم اول و سکون ثانی و سین بی‌نقطه، گرسنگی را گویند که در مقابل سیری است - و بمعنی چرک و ریم جامه و بدن هم آمده است - و موی پیچیده و موی پیچه را نیز گفته‌اند که موباف زنان باشد.\nfootnote (Mo'in): گرس = گرسنگی ... پهلوی gursak ... «اسشق ۹۰۷» ... پارسی باستان *vr̥sa- ... هوبشمان ۹۰۷ ... رک: اسشق - هوبشمان ۹۰۸ (Horn/Hübschmann no. 908 = gurs 'Lockenhaar').\nE\necho ok"
}
```


### [2026-10-17T00:06:15.544Z] TOOL RESULT

```
ok
```


## [2026-10-17T00:08:57.073Z] TOOL CALL #60: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-540.py <<'PYEOF'\nimport json\nW_VRANA=\"https://en.wiktionary.org/wiki/व्रण\"\nW_VULNUS=\"https://en.wiktionary.org/wiki/vulnus\"\nW_VULTUR=\"https://en.wiktionary.org/wiki/vultur\"\nW_GORG=\"https://en.wiktionary.org/wiki/گرگ\"\nW_WOLF=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wĺ̥kʷos\"\nW_WOOL=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wĺ̥h₁neh₂\"\nV_VARAS=\"https://vajehyab.com/moein/ورس\"\n\nPOK1144={\"src\":\"POK\",\"where\":\"pp. 1144-1145, 8. u̯el- (POK_full.txt l.~90697)\",\"stance\":\"supports\",\"note\":\"'uel-8 Meaning: to tear, wound ... hom. Attic οὐλή \\\"wound, scar\\\", np. vālāna, valāna \\\"wound\\\", Latin volnus \\\"wound\\\" (*ulsnos) ... Latin vello, -ere \\\"pluck, tear, rend\\\"'\"}\npok_wool={\"src\":\"POK\",\"where\":\"pp. 1139-1140, 4. u̯el- 'wool, hair' (POK_full.txt l.~90370-90395)\",\"stance\":\"supports\",\"note\":\"'Avestan varəsa-, npers. gurs = Old Church Slavic vlasъ, russ. volos \\\"hair\\\"' (B. guttural extensions *u̯olk̑-); A.: 'Gothic wulla, OHG wolla ... Latin lana'; 'Latin vellus \\\"fleece\\\" (villus \\\"das zottige Haar\\\")'\"}\nAHD_wel4={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wel-4 / wela-2 (AHD_watkins1985.txt l.1142)\",\"stance\":\"supports\",\"note\":\"'wel-4. To tear, pull. 1. *wel-do- in Latin vellere ... 2. *wel-no- in Latin villus, shaggy hair, wool: VELOURS, VELVET [Pok. 8. wel- 1144]'; 'wela-2. To strike, wound ... *welo-nes- in Latin vulnus (stem vulner-): VULNERABLE [In Pok. 8. wel- 1144]'\"}\nAHD_wool={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wela-1 'Wool' (AHD_watkins1985.txt l.1142)\",\"stance\":\"supports\",\"note\":\"'wela-1. Wool. Probably related to wel-4. 1. ... *wl-na- in a. Germanic *wullō in Old English wul(l), wool: WOOL; b. Latin lāna ... [Pok. 4. uel- 1139]'\"}\nAHD_wolf={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wlkwo- (AHD_watkins1985.txt l.1172)\",\"stance\":\"supports\",\"note\":\"'wlkwo-. Wolf. 1. Germanic *wulfaz in Old English wulf, wolf: WOLF ... [Pok. ulkwos 1178]'\"}\nKLN_wolf={\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.268019 s.v. wolf\",\"stance\":\"supports\",\"note\":\"'wolf ... fr. OE. wulf ... Goth. wulfs, fr. I.-E. *wḷqwos-, whence also OI. vṛkas, Avestic vəhrka- ... *wḷqwos- possibly derives fr. base *wel-, \\\"to tear\\\", and prop. denotes \\\"the tearing animal\\\"'\"}\nWLD_wolf={\"src\":\"WLD\",\"where\":\"Bd. I p. ~315-316 (WLD_Bd1_pages.txt leaf 324, l.30150)\",\"stance\":\"supports\",\"note\":\"'u̯ḷqʷos \\\"Wolf\\\" ... Ai. vṛka- m. \\\"Wolf\\\", vṛkī \\\"Wölfin\\\", av. vəhrka- \\\"Wolf\\\"; arm. gail'\"}\nSYN_wolf={\"src\":\"SYN\",\"where\":\"§3.71 WOLF (SYN.txt l.4946)\",\"stance\":\"supports\",\"note\":\"table lists 'Goth. wulfs ... OE wulf ... NE wolf ... Av. vəhrka-'\"}\nHRN910={\"src\":\"HRN\",\"where\":\"no. 910, pp. 202-203 (HRN.txt l.7887)\",\"stance\":\"supports\",\"note\":\"'910. gurg \\\"Wolf\\\". ... ap. Varkāna-; aw. vəhrka- \\\"Wolf\\\"; phlv. gurg; ai. vṛka-'\"}\nHUB_gurg={\"src\":\"HUB\",\"where\":\"§ on ap. r̥ > np. ur, HUB.txt l.5054\",\"stance\":\"supports\",\"note\":\"'gurg \\\"Wolf\\\" = zd. vehrka-; Gurgān \\\"ein Land\\\" = zd. vehrkāna-, ap. vrkāna-'\"}\nNYB_gurg={\"src\":\"NYB\",\"where\":\"Glossary s.v. gurg (NYB_vol2_glossary.txt l.1740)\",\"stance\":\"supports\",\"note\":\"'gurg [gwlg] wolf ... Av. (1418 sq.) vəhrka-; NP gurg'\"}\nPHD_gurg={\"src\":\"PHD\",\"where\":\"s.v. gurg (PHD_mackenzie.txt l.2627)\",\"stance\":\"supports\",\"note\":\"'gurg [gwlg] wolf.'\"}\nSOD_wolf={\"src\":\"SOD\",\"where\":\"no. 10432 wyrk- (SOD_pages.txt l.33880)\",\"stance\":\"supports\",\"note\":\"'10432 wyrk- B work, wirk ... <*wṛka; Av. vəhrka ... wolf'\"}\nARY_wolf={\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt [pdf page 430] (printed 431), wolf entry\",\"stance\":\"supports\",\"note\":\"index lists in the گرگ entry 'GURG (PAHLAVI)', 'VARKANA (OLD PERSIAN)', 'WOLF (ENGLISH)', 'LOBO (SPANISH)', 'VILKAS (LITHUANIAN)'\"}\nBQT1797={\"src\":\"BQT\",\"where\":\"p.1797 (BQT_v3 pdf 594, image read) s.v. گرگ\",\"stance\":\"supports\",\"note\":\"Mo'in fn. 6: 'پارسی باستان varkāna-، اوستایی vehrka (گرگ)، پهلوی gurg، هندی باستان vṛka-، ارمنی gail ... اسشق ۹۱۰'\"}\n\ndef node(i,lang,words,verdict,der,derfa,src,rc,cons,**kw):\n    d={\"id\":i,\"lang\":lang,\"words\":words,\"verdict\":verdict,\"derivation\":der,\"derivation_fa\":derfa,\"sources\":src,\"ref_check\":rc,\"consulted\":cons}\n    d.update(kw); return d\n\ne0=dict(entry=0,root=\"Wel 2\",verdict=\"confirmed\",modern_form=\"PIE *wel- (Pokorny 8. u̯el-) 'to tear, wound'; AHD splits it into *wel- 'tear, pull' (wel-4) and *welə- 'strike, wound' (wela-2)\",\n note=\"Pokorny pp. 1144-1145 '8. u̯el- to tear, wound' contains exactly Nourai's set: NP vālāna/valāna 'wound', Latin volnus, vellere. Root, label and gloss correct. But Pokorny does NOT put Sanskrit vraṇa- here (he lists it under *u̯er- 'tear, scratch', p. 1163-64), and Walde-Pokorny I 305 says explicitly 'ai. vraṇa- Wunde hat idg. r'. The chart's Sanskrit→Persian arrow follows Horn/Mo'in (BQT 2253), not the IE handbooks. In the book Welâ and Wlkwo are drawn as sub-roots of Wel 2 (Part 1).\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wel- «دریدن، کندن، زخم زدن» (پوکورنی ۱۱۴۴، ریشهٔ هشتم u̯el-) واقعی است و نام زبان و معنا درست آمده است. پوکورنی خود «والانه/ولانه»ی فارسی، volnus لاتینی و vellere را زیر همین ریشه آورده است. تنها اشکال، جای دادن vraṇa-ی سنسکریت در اینجاست که پوکورنی و والده-پوکورنی آن را از ریشهٔ *wer- (با r) می‌دانند. در مجموع ادعای نورایی دربارهٔ خود ریشه درست است.\",\n sources=[W_VULNUS],\n ref_check=[{\"ref\":\"POK:1144\",\"status\":\"supports\",\"note\":\"POK_full.txt l.90697ff: 'uel-8 Meaning: to tear, wound; to steal ... np. vālāna, valāna \\\"wound\\\", Latin volnus ... Latin vello, -ere \\\"pluck, tear\\\"' Page(s): 1144-1145.\"}],\n consulted=[{\"src\":\"AHD\",\"where\":\"Watkins 1985 wel-4, wela-2\",\"stance\":\"supports\",\"note\":\"'wel-4. To tear, pull ... [Pok. 8. wel- 1144]'; 'wela-2. To strike, wound ... [In Pok. 8. wel- 1144]'\"},\n            {\"src\":\"WLD\",\"where\":\"Bd. I 304-305 (WLD_Bd1_pages.txt leaf 313, l.29055-29066)\",\"stance\":\"partial\",\"note\":\"'lat. vello, -ere ... voltur \\\"Geier\\\" *uel-tor \\\"Reißer\\\"'; but 'Ai. vraṇa- \\\"Wunde\\\" hat idg. r'\"}],\n nodes=[\n node(1,\"Sanskrit\",\"vrana\",\"disputed\",\n  \"Skt. vraṇa- m./n. 'wound, sore, crack' is real, but modern and classical handbooks derive it from PIE *wer- 'to tear, scratch' (zero-grade *wr̥-no- / *wre-no-, cognate with OCS rana 'wound'), not from *wel-: Pokorny pp. 1163-64 lists 'Old Indic vraṇa- m. n. \\\"wound, crack\\\" besides *urā-na in OCS rana', and Walde-Pokorny I 305 says 'ai. vraṇa- \\\"Wunde\\\" hat idg. r'. Nourai's link follows Horn as quoted by Mo'in (BQT 2253), who compared it with NP vālāna; since Sanskrit r and l both continue PIE *l/*r this was possible in 19th-c. terms, but the Slavic cognate rana fixes the r.\",\n  \"«ورنه» (vraṇa-) در سنسکریت به معنای «زخم، شکاف» واژه‌ای واقعی است، اما پوکورنی (ص ۱۱۶۳) و والده-پوکورنی آن را از ریشهٔ *wer- «خراشیدن، دریدن» می‌دانند و هم‌ریشهٔ rana «زخم» در اسلاوی کلیسایی کهن را گواه می‌آورند؛ پس r آن اصلی است و از *wel- نیست. نورایی این پیوند را از حاشیهٔ معین بر برهان قاطع (به نقل از هرن) گرفته است. پژوهش امروزی (ویکی‌واژه هم) آن را از *wer- می‌داند، نه از ریشهٔ این نمودار.\",\n  [W_VRANA],\n  [{\"ref\":\"BQT:2253\",\"status\":\"supports\",\"note\":\"BQT vol.4 pdf 336 (printed 2253), Mo'in's footnote to والانه: '«سروری» «اسشق ... سانسکریت vraṇa- (زخم)» قس: لاتینی vulnus' — Mo'in (after Horn) does compare vraṇa; this is the source of the arrow, not an IE handbook.\"}],\n  [{\"src\":\"POK\",\"where\":\"pp. 1163-1164, u̯er- 'tear' B (POK_full.txt l.92178)\",\"stance\":\"contradicts\",\"note\":\"'ure-no-, uro-no- in Old Indie vraṇa- m. n. \\\"wound, crack\\\" besides urā-na in Old Church Slavic, russ. etc. rana \\\"wound\\\"' — under *wer-, not *wel-\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 305 (leaf 313, l.29066)\",\"stance\":\"contradicts\",\"note\":\"'Ai. vraṇa- \\\"Wunde\\\" hat idg. r'\"},\n   {\"src\":\"SKT\",\"where\":\"s.v. Vulnerable (SKT.txt l.21081)\",\"stance\":\"partial\",\"note\":\"Skeat (old view) 'L. vulnus ... Allied to vellere, to pluck, tear; Skt. vraṇa, a wound, fracture' — the older comparison Nourai follows\"}]),\n node(2,\"Persian\",\"vâlâneh, valâneh\",\"plausible\",\n  \"NP vālāna / valāna 'wound' (Sururi, Borhan-e Qate'; Mo'in: 'ولانه = والانه، جراحت') is a rare lexicographers' word with no attested Middle Persian ancestor. Pokorny p. 1145 does list 'np. vālāna, valāna \\\"wound\\\"' under *wel- 'tear, wound' beside Greek οὐλή and Latin volnus, and Hübschmann (quoted by Mo'in) reconstructs *varnā- < IE *welno-. So a *wel- origin is accepted in the handbooks, but the chart's arrow from Sanskrit vraṇa- is wrong twice: Persian does not descend from Sanskrit, and vraṇa- itself belongs to *wer- (see #1). Phonetically Iranian *warna- would give NP *gurn/*varn rather than vālāna, so the etymology stays uncertain.\",\n  \"«والانه» یا «ولانه» به معنای «زخم، جراحت» واژه‌ای کمیاب است که فرهنگ‌نویسان (سروری، برهان قاطع) آورده‌اند و صورت فارسی میانهٔ آن در دست نیست. پوکورنی (ص ۱۱۴۵) آن را زیر ریشهٔ *wel- «دریدن، زخم زدن» و هم‌ریشه با volnus لاتینی آورده و هوبشمان (به نقل معین) صورت *velno- را برایش بازسازی کرده است. اما پیکان نمودار از سنسکریت به فارسی نادرست است: فارسی از سنسکریت نمی‌آید و «ورنه» از ریشهٔ دیگری است. بنابراین پیوند با *wel- با احتیاط پذیرفتنی است.\",\n  [],\n  [{\"ref\":\"MON:4966\",\"status\":\"supports\",\"note\":\"MON_part2.txt l.87260: 'ولانه: (= والانه) (اِ.) جراحت' — meaning confirmed (Mo'in's own dictionary; no etymology given there).\"},\n   {\"ref\":\"POK:1145\",\"status\":\"supports\",\"note\":\"POK_full.txt l.~90722: 'hom. Attic οὐλή \\\"wound, scar\\\", np. vālāna, valāna \\\"wound\\\", Latin volnus' (Page(s) 1144-1145).\"}],\n  [{\"src\":\"BQT\",\"where\":\"p.2253 (vol.4 pdf 336), s.v. والانه fn.\",\"stance\":\"partial\",\"note\":\"'سانسکریت vraṇa- (زخم) قس: لاتینی vulnus ... هوبشمان ۱۷۵ گوید: vālāna از *varnā-، هندوژرمانی *velno-، لاتینی vulnus هندوژرمانی *velnes' — supports *wel-, cites Skt only as comparison\"},\n   {\"src\":\"HUB\",\"where\":\"p.175 (via Mo'in's quotation)\",\"stance\":\"supports\",\"note\":\"Hübschmann reconstructs *varnā- < IE *velno- (as quoted in BQT fn.)\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 304-305\",\"stance\":\"silent\",\"note\":\"np. vālāna not found in the OCR near vello/volnus\"}]),\n node(3,\"Latin\",\"vulmus; vellere\",\"transcription_suspect\",\n  \"The book prints 'vulmus', a misprint for Latin vulnus (older volnus), gen. vulneris 'wound', from Proto-Italic *welanos, PIE *wel(h)- 'tear, strike' (s-stem *welh-nes-); the extraction is faithful. vellere 'to pluck, tear' (vellō, vulsī, vulsum < *wel-d-/*wel-s-) is correct and confirmed by Pokorny 1145 and AHD wel-4.\",\n  \"صورت چاپ‌شده در کتاب «vulmus» است که خطای چاپی نورایی است و درست آن vulnus (کهن‌تر volnus) «زخم» است، از ایتالیک آغازین *welanos و ریشهٔ *wel- «دریدن، زدن». vellere «کندن، دریدن» درست آمده است. پس خطا در کتاب است، نه در خوانش اسکن؛ پیوند هر دو واژه با این ریشه را پوکورنی و واتکینز تأیید می‌کنند.\",\n  [W_VULNUS],\n  [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 l.1142: 'wela-2 ... *welo-nes- in Latin vulnus (stem vulner-), a wound'; 'wel-4 ... *wel-do- in Latin vellere, to tear, pull'.\"}],\n  [POK1144,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.264156 s.v. vulnerable\",\"stance\":\"supports\",\"note\":\"'L. vulnerāre \\\"to wound\\\", fr. volnus, vulnus \\\"a wound\\\" ... from I.-E. base *wel-, \\\"to tear\\\", whence also vellere \\\"to pluck, tear\\\"'\"},\n   {\"src\":\"LAT\",\"where\":\"not checked\",\"stance\":\"silent\",\"note\":\"not consulted; Klein+Pokorny+AHD agree\"}],\n  error_in=\"book\",book_prints=\"vulmus\",correct_form=\"vulnus\"),\n node(4,\"English\",\"vulnerable; vulture\",\"plausible\",\n  \"vulnerable (c.1600) < Late Latin vulnerābilis < vulnerāre 'to wound' < vulnus: confirmed. vulture (ME vultur < Anglo-Norman/OF voltour < Latin vultur, voltur): its connection with vellere 'tear' is an old guess ('the tearer', Walde-Pokorny *uel-tor) kept by Klein, but Wiktionary calls it 'perhaps ... the ending is unclear' and Watkins (AHD 1985) lists vultur under a separate root *gʷltur- (Pokorny 482). So vulture is only possibly from this root.\",\n  \"vulnerable «آسیب‌پذیر» از لاتینی متأخر vulnerabilis و vulnerare «زخمی کردن» از vulnus است و درست است. اما vulture «کرکس» از لاتینی vultur پیوندش با vellere «دریدن» (به معنای «درنده») تنها حدسی قدیمی است که کلاین و والده-پوکورنی پذیرفته‌اند؛ واتکینز آن را زیر ریشهٔ جداگانهٔ *gʷltur- آورده و ویکی‌واژه هم آن را نامطمئن می‌داند. پس این بخش با احتیاط پذیرفتنی است.\",\n  [W_VULTUR],\n  [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference\"}],\n  [{\"src\":\"AHD\",\"where\":\"Watkins 1985 l.553 and l.1142\",\"stance\":\"partial\",\"note\":\"VULNERABLE under wela-2; but 'gʷltur-. Vulture. Possible root. Latin vultur, vulture: VULTURE. [Pok. gʷltur(os) 482.]'\"},\n   {\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.264229 s.v. vulture\",\"stance\":\"supports\",\"note\":\"'L. voltur, vultur ... lit. meaning \\\"the tearing (bird)\\\", and in gradational relationship to vellere \\\"to tear\\\"'\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I 305 (l.29057)\",\"stance\":\"supports\",\"note\":\"'voltur \\\"Geier\\\" *uel-tor \\\"Reißer\\\"'\"},\n   {\"src\":\"SKT\",\"where\":\"s.v. Vulnerable (l.21081)\",\"stance\":\"supports\",\"note\":\"'L. vulner-, crude form of vulnus ... Allied to vellere, to pluck, tear'\"}]),\n ])\n\ne1=dict(entry=1,root=\"Welâ, Wlnâ, Wolko\",verdict=\"confirmed\",modern_form=\"PIE *h₂wĺ̥h₁neh₂ 'wool' (Pokorny 4. u̯el-, u̯elə- 'wool, hair', p. 1139) with the guttural extension *wolḱ-so- 'hair' (Av. varəsa-, OCS vlasъ)\",\n note=\"Pokorny pp. 1139-1140 (4. u̯el-) gives both the wool word (*u̯l̥nā: Goth. wulla, Lat. lāna) and the guttural-extended 'hair' words (Av. varəsa-, NP gurs, OCS vlasъ); AHD wela-1 'Wool. Probably related to wel-4' (tear). The chart's gloss 'plucked off (wool)' reflects that hypothesised link (wool as plucked before shearing); fine as a gloss. Modern notation *h₂wĺ̥h₁neh₂ (Wiktionary).\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *welə- / *wl̥nā «پشم» (امروزه *h₂wĺ̥h₁neh₂) در پوکورنی (ص ۱۱۳۹) ثبت است و پوکورنی گونهٔ گسترش‌یافتهٔ *wolk̑- «مو» را هم (اوستایی varəsa-، فارسی «گُرس»، اسلاوی vlasъ) کنار آن آورده است. معنای «کنده‌شده (پشم)» اشاره به پیوند احتمالی با ریشهٔ *wel- «کندن» است که واتکینز هم «محتمل» می‌شمارد. ادعای نورایی درست است.\",\n sources=[W_WOOL],\n ref_check=[{\"ref\":\"POK:1139\",\"status\":\"supports\",\"note\":\"POK_full.txt l.~90370ff (4. u̯el-, Page(s) 1139-1140): 'Gothic wulla, OHG wolla \\\"Wolle = wool\\\" ... Latin lana'; B. 'Avestan varəsa-, npers. gurs = OCS vlasъ, russ. volos \\\"hair\\\"'.\"}],\n consulted=[AHD_wool,{\"src\":\"WLD\",\"where\":\"Bd. I (leaf 439, l.41107)\",\"stance\":\"partial\",\"note\":\"cites 'av. varəsa- \\\"Haar\\\"' (Scheftelowitz) in a discussion of 'Haar' words; the main *u̯el- 'Wolle' article not located in OCR\"}],\n nodes=[\n node(1,\"Avestan\",\"varesa\",\"confirmed\",\n  \"Av. varəsa- m. 'hair' (of men and animals, usually head-hair: Vd. 7.57, Yt. 10.127), Bartholomae col. 1374; from Proto-Iranian *wársa- < PIE *wolḱ-so-/*wl̥ḱ-so- 'hair', the guttural extension of *wel- 'wool, hair' (Pokorny 1139-40), cognate with OCS vlasъ, Russ. volos 'hair'. Nourai's 'varesa' is the usual simplified spelling of varəsa-.\",\n  \"اوستایی varəsa- «مو (ی سر آدمی و جانوران)» در بارتولومه (ستون ۱۳۷۴) آمده و از ایرانی باستان *warsa- و هندواروپایی *wolk̑-so- «مو»، گونهٔ گسترش‌یافتهٔ ریشهٔ «پشم»، است؛ هم‌ریشه با vlasъ اسلاوی کلیسایی و volos روسی. پوکورنی همین را آورده است و ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"POK:1139\",\"status\":\"supports\",\"note\":\"POK_full.txt l.90393: 'Avestan varəsa-, npers. gurs = Old Church Slavic vlasъ, russ. volos \\\"hair\\\"' (Page(s) 1139-1140).\"}],\n  [{\"src\":\"BRT\",\"where\":\"col. 1374 s.v. varəsa- (BRT.txt l.22991)\",\"stance\":\"supports\",\"note\":\"'varəsa- m., n. \\\"Haar\\\" der Menschen und Tiere, meist Kopfhaar'\"},\n   {\"src\":\"SYN\",\"where\":\"§4.14 HAIR (SYN.txt l.5376)\",\"stance\":\"supports\",\"note\":\"table: 'Av. varəsa- (a)' beside 'ChSl. vlasŭ, Russ. volos'\"},\n   {\"src\":\"KLN\",\"where\":\"p.856 s.v. Lachnanthes (KLN_1966 leaf 460)\",\"stance\":\"supports\",\"note\":\"'I.-E. *wolk-o-, whence also Avestic varesa-, ModPers. gurs, OSlav. vlasŭ, Russ. volos \\\"hair\\\"'\"}]),\n node(2,\"Pahlavi\",\"vars\",\"confirmed\",\n  \"Pahlavi wars [wls] 'hair' (MacKenzie; Nyberg 'vars ... Av. varəsa-; Paz. vars; Arm. lw. vars-kʿ; NP gurs \\\"curled hair\\\"') continues Av./Old Iranian *warsa- with loss of the final vowel; Armenian borrowed it as vars. Nourai's gloss 'curly hair' is the NP meaning; MP wars means simply 'hair'.\",\n  \"پهلوی wars (نوشتهٔ wls) «مو» بازماندهٔ ایرانی باستان *warsa- (اوستایی varəsa-) با افتادن واکهٔ پایانی است و ارمنی هم آن را به صورت vars وام گرفته است. مکنزی و نیبرگ هر دو همین را آورده‌اند؛ نیبرگ «گرس» فارسی را دنبالهٔ آن می‌داند. معنای «موی مجعد» در اصل معنای فارسی نو است؛ در پهلوی تنها «مو» است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"HRN:202\",\"status\":\"supports\",\"note\":\"HRN.txt l.7891 (no. 908, p.202): '908. gurs \\\"Lockenhaar\\\" (unbelegt). aw. varəsa- \\\"Haar\\\"; phlv. vars, arm. LW. vars; ksl. vlasŭ'.\"}],\n  [{\"src\":\"PHD\",\"where\":\"s.v. wars (PHD_mackenzie.txt l.5216)\",\"stance\":\"supports\",\"note\":\"'wars [wls] hair.'\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. vars (NYB_vol2_glossary.txt l.3980)\",\"stance\":\"supports\",\"note\":\"'vars [wls] hair — Av. (1374) varəsa-; Paz. vars; Arm. lw. vars-kʿ (pl.); NP gurs \\\"curled hair\\\"'\"}]),\n node(3,\"Persian\",\"vares; gors 2\",\"plausible\",\n  \"gors (gurs) 'curly hair, hair-braid' (Borhan: 'موی پیچیده و موی پیچه ... موباف زنان') is the regular NP outcome of Old Iranian *warsa- via southwestern *vr̥sa- > gurs (initial *wr̥- > gur-, as in gurg), with a later form gars; Horn no. 908 (calling it unattested) and Hübschmann p. 92 ('gurs, besser gars ... = phl. vars, zd. varəsa-') confirm it. varas/varis 'cord' is Mo'in's 'a cord woven of cow-hair with which the barsom twigs are bound' — the Zoroastrian varas (hair-cord of a white bull) — a learned/Zoroastrian continuation of MP wars 'hair' with the specialised meaning 'hair-string'; semantically clear but Mo'in gives no etymology and the direct MP wars → varas descent (keeping v-, unlike gurs) marks it as a Zoroastrian technical term rather than an inherited one. gors confirmed; vares plausible.\",\n  \"«گُرس» به معنای «موی پیچیده، گیسوبافته» (برهان قاطع) دنبالهٔ بومی ایرانی باستان *warsa- است که در جنوب‌غربی با دگرگونی wr̥- به gur- (چنان‌که در «گرگ») به «گرس» رسیده؛ هرن (شمارهٔ ۹۰۸) و هوبشمان (ص ۹۲) آن را با پهلوی vars و اوستایی varəsa- یکی دانسته‌اند. «ورس / وریس» به گفتهٔ معین «ریسمانی که از موی گاو بافته می‌شود و شاخه‌های برسم را با آن به هم می‌پیوندند» است؛ این واژهٔ دینی زرتشتی از پهلوی wars «مو» با تحول معنایی «ریسمان مویین» آمده و چون v- آن به g- بدل نشده، واژه‌ای دینی و کتابی است نه بازماندهٔ عادی. بخش «گرس» درست و بخش «ورس» با احتیاط پذیرفتنی است.\",\n  [V_VARAS],\n  [{\"ref\":\"MON:5004\",\"status\":\"supports\",\"note\":\"vajehyab Mo'in s.v. ورس (archived): 'ریسمانی که از موی گاو بافته می‌شود و شاخه‌های برسم را با آن به هم می‌پیوندند' — meaning confirmed, no etymology.\"},\n   {\"ref\":\"SNS:285\",\"status\":\"partial\",\"note\":\"SNS index (SNS.txt l.30840) 'vars 280/13' and glossary l.15617 ':vars: ... (Bth.1374) varəsa-' — Tavoosi glosses Pahlavi vars < Av. varəsa-; page offset unknown, entry located by transliteration.\"},\n   {\"ref\":\"BQT:1794\",\"status\":\"supports\",\"note\":\"BQT vol.3 pdf 591 (= printed 1794; cached OCR file is labelled 1796) s.v. گرس: '... و موی پیچیده و موی پیچه را نیز گفته‌اند که موباف زنان باشد'; Mo'in fn. refers to 'اسشق - هوبشمان ۹۰۸'. Saved in ocr/BQT/1794.vision.txt.\"},\n   {\"ref\":\"KLN:856\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 460 (p.856) s.v. Lachnanthes: 'I.-E. *wolk-o-, whence also Avestic varesa-, ModPers. gurs, OSlav. vlasŭ'.\"}],\n  [{\"src\":\"HRN\",\"where\":\"no. 908, p.202\",\"stance\":\"supports\",\"note\":\"'908. gurs \\\"Lockenhaar\\\" (unbelegt). aw. varəsa-; phlv. vars'\"},\n   {\"src\":\"HUB\",\"where\":\"p.92 on Horn 908 (HUB.txt l.3266) and l.5537\",\"stance\":\"supports\",\"note\":\"'gurs, besser gars im älteren Neupersisch vorhanden gewesen ... neben älterem phl. paz. vars ... und arm. vars ... zu zd. varəsa-'; 'gurs \\\"Locken\\\" (unbelegt), besser gars = phl. gars, vars, zd. varəsa-'\"},\n   {\"src\":\"NYB\",\"where\":\"s.v. vars (l.3980)\",\"stance\":\"supports\",\"note\":\"'NP gurs \\\"curled hair\\\"'\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt l.3110\",\"stance\":\"silent\",\"note\":\"only 'VARASA' in a Sanskrit/Avestan cognate list; no separate gors/varas headword located\"}]),\n node(4,\"Sogdian\",\"wrs\",\"confirmed\",\n  \"Sogdian wrs /wars/ 'hair' (Gharib no. 10177: 'wrs B, S, C wars © Av. varəsa ... hair'; also wrs'k warsak) continues Old Iranian *warsa- directly, with v- kept as in eastern Iranian.\",\n  \"سغدی wrs (خوانش wars) «مو» در فرهنگ قریب (شمارهٔ ۱۰۱۷۷) با اوستایی varəsa- سنجیده شده و مستقیم از ایرانی باستان *warsa- آمده است؛ w- آغازی در زبان‌های ایرانی شرقی برجا مانده است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"SOD:412\",\"status\":\"supports\",\"note\":\"SOD_pages.txt l.33122: '10177 wrs B, S, C wars © Av. varəsa ... hair'.\"}],\n  [{\"src\":\"POK\",\"where\":\"p.1139-1140\",\"stance\":\"silent\",\"note\":\"lists Av. varəsa- and NP gurs, no Sogdian\"},\n   {\"src\":\"BRT\",\"where\":\"col. 1374\",\"stance\":\"silent\",\"note\":\"Avestan only\"}]),\n node(5,\"Germanic\",\"wullâ\",\"confirmed\",\n  \"Proto-Germanic *wullō (Nourai's 'wullâ'; Goth. wulla, OHG wolla, OE wull) < PIE *h₂wl̥h₁-neh₂ with assimilation -ln- > -ll-.\",\n  \"ژرمنی آغازین *wullō (گوتی wulla، آلمانی علیای کهن wolla) از هندواروپایی *h₂wl̥h₁-neh₂ با همگونی ln به ll پدید آمده است. ادعای نورایی درست است.\",\n  [W_WOOL],\n  [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 l.1142: 'Germanic *wullō in Old English wul(l), wool [Pok. 4. uel- 1139]'.\"}],\n  [pok_wool,{\"src\":\"WLD\",\"where\":\"Bd. I\",\"stance\":\"silent\",\"note\":\"main 'Wolle' article not located in the OCR\"}]),\n node(6,\"English\",\"wool\",\"confirmed\",\n  \"English wool < Middle English wolle < Old English wull < Proto-Germanic *wullō.\",\n  \"انگلیسی wool از انگلیسی میانه wolle و انگلیسی کهن wull و ژرمنی آغازین *wullō است. ادعای نورایی درست است.\",\n  [W_WOOL],\n  [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference\"}],\n  [AHD_wool,{\"src\":\"SKT\",\"where\":\"SKT.txt\",\"stance\":\"silent\",\"note\":\"WOOL headword not matched in OCR grep\"}]),\n node(7,\"Latin\",\"villus\",\"confirmed\",\n  \"Latin villus 'shaggy hair, tuft' is a collateral form of vellus 'fleece' (*wel-no-/*wol-no-), belonging to the wool/hair family (Pokorny 1139 'Latin vellus ... villus'; Wiktionary under *h₂wĺ̥h₁neh₂). Watkins files villus under wel-4 'tear, pull' instead, but notes wool is 'probably related' to that root, so the attribution differs only in sub-root.\",\n  \"لاتینی villus «موی پرپشت، دستهٔ مو» گونهٔ دیگر vellus «پشم گوسفند» است و از خانوادهٔ «پشم» (*wel-no-) است؛ پوکورنی و ویکی‌واژه آن را زیر همین ریشه آورده‌اند. واتکینز آن را زیر *wel- «کندن» گذاشته که خود به ریشهٔ «پشم» پیوسته است. ادعای نورایی درست است.\",\n  [W_WOOL],\n  [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 l.1142: 'wel-4. To tear, pull ... 2. *wel-no- in Latin villus, shaggy hair, wool: VELOURS, VELVET' — under 'tear, pull', which wela-1 'wool' is 'probably related to'.\"}],\n  [pok_wool,{\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.262165 s.v. villus\",\"stance\":\"supports\",\"note\":\"'L., \\\"shaggy hair, tuft of hair\\\", a collateral form of vellus \\\"fleece\\\"'\"}]),\n node(8,\"English\",\"velvet\",\"confirmed\",\n  \"velvet (c.1300) < Middle English veluet, velwet < Old French veluotte / Medieval Latin velluetum < Vulgar Latin *villūtus 'shaggy' < Latin villus 'shaggy hair'.\",\n  \"انگلیسی velvet «مخمل» از انگلیسی میانه veluet و فرانسوی کهن veluotte و لاتین عامیانه *villutus «پرزدار» از villus «موی پرپشت» آمده است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference\"}],\n  [{\"src\":\"KLN\",\"where\":\"KLN_1971.txt l.259982 s.v. velvet\",\"stance\":\"supports\",\"note\":\"'ME. veluet, velwet, fr. VL. velluetum, fr. *villutus \\\"shaggy\\\", fr. L. villus \\\"shaggy hair\\\"'\"},\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 index 'VELVET wel-4'\",\"stance\":\"supports\",\"note\":\"VELVET listed under wel-4 via Latin villus\"}]),\n ])\n\ne2=dict(entry=2,root=\"Wlkwo\",verdict=\"confirmed\",modern_form=\"PIE *wĺ̥kʷos 'wolf' (Pokorny u̯l̥kʷo-s 1178; AHD wlkwo-)\",\n note=\"The root is secure; the gloss 'tearing animals' is Klein's suggestion that *wl̥kʷos 'possibly derives fr. base *wel-, \\\"to tear\\\"' (Wiktionary also notes a possible derivation from *welh₂- 'tear'); it is a hypothesis, not the consensus, but the reconstruction and meaning 'wolf' are correct. The Iranian forms descend through Proto-Iranian *wŕ̥ka-; the chart's Avestan→Pahlavi→Persian line is a simplification (Persian continues the southwestern sister of Av. vəhrka-, OP *varka-).\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wĺ̥kʷos «گرگ» (پوکورنی ۱۱۷۸، واتکینز wlkwo-) قطعی است. معنای «جانور درنده» برگرفته از حدس کلاین است که آن را شاید از *wel- «دریدن» بداند؛ این تنها فرضیه است ولی خود ریشه و معنای «گرگ» درست است. در شاخهٔ ایرانی صورت ایرانی آغازین *wr̥ka- است و «گرگ» فارسی از گونهٔ جنوب‌غربی (پارسی باستان varka-) می‌آید نه مستقیم از اوستایی. ادعای نورایی درست است.\",\n sources=[W_WOLF],\n ref_check=[{\"ref\":\"KLN:1750\",\"status\":\"supports\",\"note\":\"Local KLN_1966 OCR stops c. p.1700, so read in KLN_1971.txt l.268019 s.v. wolf (same text): '*wḷqwos- possibly derives fr. base *wel-, \\\"to tear\\\", and prop. denotes \\\"the tearing animal\\\"'.\"}],\n consulted=[AHD_wolf,WLD_wolf,{\"src\":\"POK\",\"where\":\"p.1178 u̯l̥kʷo-s\",\"stance\":\"supports\",\"note\":\"AHD cross-ref '[Pok. ulkwos 1178]'; POK_full.txt OCR of the entry not matched by grep (noisy)\"}],\n nodes=[\n node(1,\"Avestan\",\"vherka, vehrka\",\"transcription_suspect\",\n  \"The Avestan word is vəhrka- 'wolf' (Bartholomae col. 1417-18), from Proto-Iranian *wŕ̥ka- < PIE *wĺ̥kʷos, with Avestan r̥ before k > ərə and the characteristic -hr- (r̥ > əhr before voiceless stops). The book prints 'vherka, vehrka': 'vehrka' is an acceptable simplified spelling (Horn/Hübschmann write vehrka-), but 'vherka' is not an Avestan form — Nourai's misprint (letters transposed); the extraction is faithful.\",\n  \"واژهٔ اوستایی vəhrka- «گرگ» است (بارتولومه، ستون ۱۴۱۷) از ایرانی آغازین *wr̥ka- و هندواروپایی *wĺ̥kʷos؛ در اوستایی r̥ هجایی پیش از k به əhr بدل شده است. کتاب «vherka, vehrka» چاپ کرده: vehrka نگارش ساده‌شدهٔ پذیرفتنی است، اما vherka صورتی نادرست و خطای چاپی کتاب (جابه‌جایی حروف) است، نه خطای خوانش اسکن.\",\n  [W_GORG],\n  [{\"ref\":\"KLN:1750\",\"status\":\"supports\",\"note\":\"KLN_1971 s.v. wolf: 'whence also OI. vṛkas, Avestic vəhrka-'.\"},\n   {\"ref\":\"SOD:423\",\"status\":\"supports\",\"note\":\"SOD no. 10432 wyrk-: '<*wṛka; Av. vəhrka'.\"}],\n  [{\"src\":\"BRT\",\"where\":\"col. 1417-1418 headword vəhrka- (BRT.txt l.23594)\",\"stance\":\"supports\",\"note\":\"column header 'vəhrka- 1418'; also Bartholomae on OP 'vargi-' vs 'vəhrka- \\\"Wolf\\\"' (l.28757)\"},\n   {\"src\":\"KNT\",\"where\":\"p.206 s.v. Varkāna- (KNT_full.txt l.28794)\",\"stance\":\"supports\",\"note\":\"'pIE *u̯l̥kʷo-, Av. vəhrka-, Skt. vṛ́ka-, Lith. vilkas, Gt. wulfs'\"},WLD_wolf],\n  error_in=\"book\",book_prints=\"vherka, vehrka\",correct_form=\"vəhrka-\"),\n node(2,\"Pahlavi\",\"gurg\",\"confirmed\",\n  \"Middle Persian gurg [gwlg] 'wolf' continues southwestern Old Iranian *wr̥ka- (OP *varka-, attested in Varkāna-): initial *wr̥- > MP gur- (as in gurs, gurda), final -a lost. It is a sister of, not a descendant of, Avestan vəhrka-.\",\n  \"پهلوی gurg (نوشتهٔ gwlg) «گرگ» از ایرانی باستان جنوب‌غربی *wr̥ka- (پارسی باستان varka- در نام Varkāna-) آمده است: wr̥- آغازی در فارسی میانه به gur- بدل شده (چنان‌که در «گرس» و «گرده»). این واژه هم‌ریشهٔ اوستایی vəhrka- است نه بازماندهٔ مستقیم آن. ادعای نورایی در اساس درست است.\",\n  [W_GORG],\n  [{\"ref\":\"HRN:202\",\"status\":\"supports\",\"note\":\"HRN.txt l.7887 (no. 910, pp.202-203): 'gurg \\\"Wolf\\\" ... ap. Varkāna-; aw. vəhrka- \\\"Wolf\\\"; phlv. gurg'.\"}],\n  [PHD_gurg,NYB_gurg,HUB_gurg]),\n node(3,\"Persian\",\"gorg\",\"confirmed\",\n  \"NP gorg/gurg 'wolf' = MP gurg unchanged (< OP *varka- < PIr. *wŕ̥ka-); dialects keep forms like Kashani varg, Mazandarani vurg, Kurdish varg, Baluchi gurk.\",\n  \"«گرگ» فارسی نو همان پهلوی gurg است، از پارسی باستان *varka- و ایرانی آغازین *wr̥ka-؛ گویش‌ها صورت‌هایی چون varg (کاشانی، کردی) و vurg (مازندرانی) را نگه داشته‌اند. هرن، هوبشمان، معین و ویکی‌واژه همین را می‌گویند. ادعای نورایی درست است.\",\n  [W_GORG],\n  [{\"ref\":\"BQT:1797\",\"status\":\"supports\",\"note\":\"BQT vol.3 pdf 594 (printed 1797), image read: Mo'in fn.6 'پارسی باستان varkāna-، اوستایی vehrka، پهلوی gurg، هندی باستان vṛka-، ارمنی gail ... کاشانی verg, varg، مازندرانی vurg، کردی varg ... بلوچی gurk ... اسشق ۹۱۰'.\"}],\n  [HRN910,HUB_gurg,ARY_wolf]),\n node(4,\"Old Persian\",\"varkana\",\"confirmed\",\n  \"OP Varkāna- 'Hyrcania' (DB 2.92), 'wolf-land', a -āna- derivative of OP *varka- 'wolf' (cf. Elamite mi-ir-qa-nu-ia-ip 'Hyrcanians', Greek Hyrkanía with Hy- for Iranian v-).\",\n  \"پارسی باستان Varkāna- «سرزمین گرگان، هیرکانی» (کتیبهٔ بیستون ۲.۹۲) از *varka- «گرگ» با پسوند -āna- ساخته شده و به معنای «سرزمین گرگ» است؛ یونانی آن را Hyrkania گفته‌اند. کنت همین را آورده است و ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"KNT:206\",\"status\":\"supports\",\"note\":\"KNT_full.txt l.28794: 'Varkāna- sb. \\\"Hyrcania\\\", a district southeast of the Caspian Sea: Elam. mi-ir-qa-nu-ja-ip \\\"the Hyrcanians\\\", Pht. and NPers. Gurgān, Gk. Hyrkania; \\\"Wolf-Land\\\", deriv. of pIE *u̯l̥kʷo-'.\"}],\n  [HRN910,NYB_gurg|{\"note\":\"'Gurgān [gwlg'n'] the province Gurgan — Av. vəhrkāna-, OP Vrkāna-; Gr. Hyrkania; Prth wrkn' (l.1741)\"}]),\n node(5,\"Pahlavi\",\"gorgân\",\"confirmed\",\n  \"MP Gurgān [gwlg'n'] 'the province of Gorgan' (Nyberg; MacKenzie gurgānīg 'of Gurgān') < OP Varkāna- with the same *wr̥-/var- > gur- development as gurg; Parthian kept wrkn.\",\n  \"پهلوی Gurgān (نوشتهٔ gwlg'n) «ایالت گرگان» از پارسی باستان Varkāna- با همان دگرگونی var-/wr̥- به gur- که در «گرگ» دیده می‌شود آمده است؛ پارتی صورت wrkn را نگه داشته است. نیبرگ و مکنزی گواه آن‌اند و ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"KNT:206\",\"status\":\"supports\",\"note\":\"KNT p.206 s.v. Varkāna-: 'Pht. and NPers. Gurgān'.\"}],\n  [{\"src\":\"NYB\",\"where\":\"Glossary s.v. Gurgān (l.1741)\",\"stance\":\"supports\",\"note\":\"'Gurgān [gwlg'n'] the province Gurgan — Av. vəhrkāna-, OP Vrkāna-; Gr. Hyrkania; Prth wrkn'\"},\n   {\"src\":\"PHD\",\"where\":\"s.v. gurgānīg (PHD_mackenzie.txt l.2628)\",\"stance\":\"supports\",\"note\":\"'gurgānīg ... of (the province) Gurgan'\"},\n   {\"src\":\"HUB\",\"where\":\"l.5055\",\"stance\":\"supports\",\"note\":\"'Gurgān \\\"ein Land\\\" = zd. vehrkāna-, ap. vrkāna-'\"}]),\n node(6,\"Persian\",\"Gorgân\",\"confirmed\",\n  \"NP Gorgān (Arabicised Jurjān), the region SE of the Caspian, = MP Gurgān < OP Varkāna- 'wolf-land'.\",\n  \"«گرگان» فارسی نو (معرّب آن «جرجان») همان پهلوی Gurgān از پارسی باستان Varkāna- «سرزمین گرگ» است و سرزمینی در جنوب‌شرقی دریای خزر را می‌نامد. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"KNT:206\",\"status\":\"supports\",\"note\":\"KNT p.206: 'Pht. and NPers. Gurgān ... \\\"Wolf-Land\\\"'.\"}],\n  [HUB_gurg,{\"src\":\"ARY\",\"where\":\"[pdf page 430]\",\"stance\":\"supports\",\"note\":\"wolf entry lists 'VARKANA (OLD PERSIAN)' beside GURG\"}]),\n node(7,\"Sogdian\",\"wyrk\",\"confirmed\",\n  \"Sogdian wyrk /wirk/ (also wyrq-) 'wolf' < Old Iranian *wr̥ka- (Gharib no. 10432 '<*wṛka; Av. vəhrka'); the syllabic r̥ developed to ir in Sogdian.\",\n  \"سغدی wyrk (خوانش wirk) «گرگ» از ایرانی باستان *wr̥ka- است و r̥ هجایی در سغدی به ir بدل شده؛ فرهنگ قریب (شمارهٔ ۱۰۴۳۲) آن را با اوستایی vəhrka- سنجیده است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"SOD:423\",\"status\":\"supports\",\"note\":\"SOD_pages.txt l.33880: '10432 wyrk- B work, wirk (wyrq-) <*wṛka; Av. vəhrka ... wolf'.\"}],\n  [SOD_wolf|{\"where\":\"Gharib grammar table (SOD_pages.txt l.3177)\",\"note\":\"'/wrk/ wyrk- wolf *vṛka-'\"},{\"src\":\"BRT\",\"where\":\"col. 1417-18\",\"stance\":\"silent\",\"note\":\"Avestan only\"}]),\n node(8,\"Germanic\",\"wulfaz\",\"confirmed\",\n  \"Proto-Germanic *wulfaz < PIE *wĺ̥kʷos, with *l̥ > ul and the irregular *kʷ > f (labial outcome, perhaps via *wulhwaz or taboo alteration).\",\n  \"ژرمنی آغازین *wulfaz از هندواروپایی *wĺ̥kʷos است: l̥ هجایی به ul و kʷ به گونه‌ای نابه‌قاعده به f بدل شده است. ادعای نورایی درست است.\",\n  [W_WOLF],\n  [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 l.1172: 'wlkwo-. Wolf. 1. Germanic *wulfaz in Old English wulf'.\"}],\n  [WLD_wolf,SYN_wolf]),\n node(9,\"English\",\"wolf\",\"confirmed\",\n  \"English wolf < Old English wulf < Proto-Germanic *wulfaz.\",\n  \"انگلیسی wolf از انگلیسی کهن wulf و ژرمنی آغازین *wulfaz است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference\"}],\n  [KLN_wolf,AHD_wolf]),\n ])\nout={\"pdf_page\":540,\"book_page\":510,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[e0,e1,e2]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-540.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-540.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-540.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 540"
}
```


### [2026-10-17T00:08:57.706Z] TOOL RESULT

```
nodes verified: 21/21
node verdicts: {'disputed': 1, 'plausible': 3, 'transcription_suspect': 2, 'confirmed': 15}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 20, 'not_checked': 4, 'partial': 2}
books consulted: {'contradicts': 2, 'partial': 3, 'supports': 41, 'silent': 8} | by book: {'WLD': 6, 'HUB': 6, 'KLN': 6, 'POK': 5, 'NYB': 5, 'AHD': 4, 'BRT': 4, 'SKT': 3, 'PHD': 3, 'HRN': 3, 'ARY': 3, 'SYN': 2, 'BQT': 1, 'LAT': 1, 'KNT': 1, 'SOD': 1}
```


## [2026-10-17T00:09:07.137Z] TOOL CALL #61: SubagentHandback

```json
{
 "message": "I wrote the page 540 file (book page 510). `verify_check.py 540` reports 0 PROBLEM lines and all 21 of 21 nodes are verified. The owner has no extraction errors to fix: the JSON matches the printed page.\n\n- **Roots:** all 3 confirmed (Wel 2, Welâ/Wlnâ/Wolko, Wlkwo).\n- **Nodes:** 15 confirmed, 3 plausible, 1 disputed, 2 transcription_suspect.\n\n**Disputed:**\n- **Wel 2 #1, Sanskrit vrana \"wound\":** Pokorny (pp. 1163–64) and Walde-Pokorny (I 305: \"ai. vraṇa- hat idg. r\") put it under PIE *wer- \"tear, scratch\", a cognate of Old Church Slavonic rana \"wound\", not under *wel-. Nourai's link comes from Mo'in's note quoting Horn (Borhan-e Qate' p. 2253).\n\n**Transcription suspect (both are misprints in the book; the extraction is faithful):**\n- **Wel 2 #3, Latin:** the book prints \"vulmus\", which should be vulnus (older volnus).\n- **Wlkwo #1, Avestan:** the book prints \"vherka, vehrka\". \"vherka\" is not a real form; it should be vəhrka-.\n\n**Plausible:**\n- **Wel 2 #2, Persian vâlâneh/valâneh:** Pokorny p. 1145 does list it under *wel-, but the arrow from Sanskrit is wrong.\n- **Wel 2 #4, English vulture:** Klein and Walde-Pokorny take it from *wel-, but Watkins (American Heritage) gives it a separate root *gʷltur-.\n- **Welâ #3, Persian vares:** Mo'in gives it as a cow-hair cord used to bind the barsom twigs, a meaning shift from Pahlavi wars \"hair\"; he gives no etymology. The other word in that node, gors \"curly hair\", is confirmed.\n\nFor the owner: the cached OCR files for Borhan-e Qate' vol. 3 are labelled about two pages off. PDF page 591 is printed p. 1794, but its cached OCR file is named 1796, and the 1797.txt OCR shows the running head as 1795. I saved a corrected reading of p. 1794 (gors) as `1794.vision.txt` in the same folder. `tools/ref_page.py --pdf-page` also seems to ignore its override and reuse the cache.\n\nFiles are in /home/sfmqrb/git/rishe-private/data/verification:\n- page-540.json\n- sources/refs/ocr/BOOK/540.png\n- sources/refs/ocr/BQT/1794.vision.txt"
}
```


### [2026-10-17T00:09:07.438Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
