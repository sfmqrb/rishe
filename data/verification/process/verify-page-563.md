# Verification process log — verify-page-563


## [2026-10-17T00:30:14.278Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 563 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-563.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-563.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-563.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 563` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.326Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:18.549Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:30:18.567Z] TOOL RESULT

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


## [2026-10-17T00:30:19.058Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-563.txt"
}
```


### [2026-10-17T00:30:19.096Z] TOOL RESULT

```
1	=== PDF page 563 (book page 533) ===
2	--- entry 0 ---
3	ROOT [Egyptian] Yb, Âbu, Elu, Elu-ephas : Yb, Âbu: elephant, ivory; Elu, Elu-ephas: elephant  (refs KLN:507,821; AHD:423)
4	#1 (parent #0) [Old Persian] refs=KNT:197; PLA:214 | piru : ivory
5	#2 (parent #0) [Aramaic] refs=MON:953 | p-ila, pŭla, pîlâ : elephant
6	  #3 (parent #2) [Persian] refs=PLA:214; BQT:446; MON:953; KLN:507 | pîl «پیل (فیل)» : elephant ; pîl-âs «پیلاس (پیلسته)» : "elephant's bone", ivory ☞Ost
7	#4 (parent #0) [Hebrew] refs=KLN:507 | el-eph : ox, elephant ; p-îl : elephant ; yěbh : elephant
8	#5 (parent #0) [Greek] refs=AHD:423. SYN:189 | el : Indian elephant ; elephas : elephant | NOTE: WEB & FSD suggest that these words may have been taken through Hebrew "eleph: ox"
9	  #6 (parent #5) [Latin] refs=KNT:507; AHD:423 | elephantus : elephant
10	    #7 (parent #6) [English] refs=AHD; KLN | elephant
11	    #8 (parent #6) [Latin] refs=KLN:507 | elepantum : ivory (principal) letters ; elementum : principal
12	      #9 (parent #8) [English] refs=AHD; KLN:507 | element
13	#10 (parent #0) [Latin] refs=AHD:697; KLN:821 | ebur : ivory ; eboreus : made of ivory
14	  #11 (parent #10) [Old French] refs=KLN:821 | ivurie
15	    #12 (parent #11) [English] refs=KLN:821 | ivory
16	--- entry 1 ---
17	ROOT Yě -> redirect to Ei
18	--- entry 2 ---
19	ROOT [Indo-European] Yekwer : liver  (refs POK:504)
20	#1 (parent #0) [Avestan] refs=POK:504 | yâkara : liver
21	  #2 (parent #1) [Pahlavi] refs=SNS:317 | jakar, jagar : liver
22	    #3 (parent #2) [Persian] refs=BQT:579; POK:504 | jegar «جگر» : liver ; jegar-band «جگربند» : a dear person, child
23	      #4 (parent #3) [Latin] refs=AHD | gigeria : bird's stomach
24	        #5 (parent #4) [English] refs=None | gizzard
25	#6 (parent #0) [Greek] refs=AHD | heepar : liver
26	  #7 (parent #6) [English] refs=None | heparin, hepatic
27	#8 (parent #0) [Latin] refs=AHD | jecur : liver
28	  #9 (parent #8) [English] refs=KLN:827 | jecoral
29	--- entry 3 ---
30	ROOT Yelek -> redirect to Ijlak
31	
```


## [2026-10-17T00:30:19.776Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-563.json"
}
```


### [2026-10-17T00:30:19.795Z] TOOL RESULT

```
1	{
2	  "pdf_page": 563,
3	  "book_page": 533,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Yb, Âbu, Elu, Elu-ephas",
8	        "lang": "Egyptian",
9	        "refs": "KLN:507,821; AHD:423",
10	        "gloss": "Yb, Âbu: elephant, ivory; Elu, Elu-ephas: elephant",
11	        "note": "These words had appeared in the Hamitic (old Egyptian) language"
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Old Persian",
18	          "refs": "KNT:197; PLA:214",
19	          "words": [
20	            {"translit": "piru", "gloss": "ivory", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 0,
28	          "lang": "Aramaic",
29	          "refs": "MON:953",
30	          "words": [
31	            {"translit": "p-ila, pŭla, pîlâ", "gloss": "elephant", "script": null}
32	          ],
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 2,
39	          "lang": "Persian",
40	          "refs": "PLA:214; BQT:446; MON:953; KLN:507",
41	          "words": [
42	            {"translit": "pîl", "gloss": "elephant", "script": "پیل (فیل)"},
43	            {"translit": "pîl-âs", "gloss": "\"elephant's bone\", ivory", "script": "پیلاس (پیلسته)", "see": ["Ost"]}
44	          ],
45	          "note": null,
46	          "quote": {"text": "چو شب تیره شد پهلوان سپاه - به پیلان آسوده بربست راه", "poet": "Ferdowsî"}
47	        },
48	        {
49	          "id": 4,
50	          "parent": 0,
51	          "lang": "Hebrew",
52	          "refs": "KLN:507",
53	          "words": [
54	            {"translit": "el-eph", "gloss": "ox, elephant", "script": null},
55	            {"translit": "p-îl", "gloss": "elephant", "script": null},
56	            {"translit": "yěbh", "gloss": "elephant", "script": null}
57	          ],
58	          "note": null,
59	          "quote": null
60	        },
61	        {
62	          "id": 5,
63	          "parent": 0,
64	          "lang": "Greek",
65	          "refs": "AHD:423. SYN:189",
66	          "words": [
67	            {"translit": "el", "gloss": "Indian elephant", "script": null},
68	            {"translit": "elephas", "gloss": "elephant", "script": null}
69	          ],
70	          "note": "WEB & FSD suggest that these words may have been taken through Hebrew \"eleph: ox\"",
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "Latin",
77	          "refs": "KNT:507; AHD:423",
78	          "words": [
79	            {"translit": "elephantus", "gloss": "elephant", "script": null}
80	          ],
81	          "note": null,
82	          "quote": null
83	        },
84	        {
85	          "id": 7,
86	          "parent": 6,
87	          "lang": "English",
88	          "refs": "AHD; KLN",
89	          "words": [
90	            {"translit": "elephant", "gloss": null, "script": null}
91	          ],
92	          "note": null,
93	          "quote": null
94	        },
95	        {
96	          "id": 8,
97	          "parent": 6,
98	          "lang": "Latin",
99	          "refs": "KLN:507",
100	          "words": [
101	            {"translit": "elepantum", "gloss": "ivory (principal) letters", "script": null},
102	            {"translit": "elementum", "gloss": "principal", "script": null}
103	          ],
104	          "note": null,
105	          "quote": null
106	        },
107	        {
108	          "id": 9,
109	          "parent": 8,
110	          "lang": "English",
111	          "refs": "AHD; KLN:507",
112	          "words": [
113	            {"translit": "element", "gloss": null, "script": null}
114	          ],
115	          "note": null,
116	          "quote": null
117	        },
118	        {
119	          "id": 10,
120	          "parent": 0,
121	          "lang": "Latin",
122	          "refs": "AHD:697; KLN:821",
123	          "words": [
124	            {"translit": "ebur", "gloss": "ivory", "script": null},
125	            {"translit": "eboreus", "gloss": "made of ivory", "script": null}
126	          ],
127	          "note": null,
128	          "quote": null
129	        },
130	        {
131	          "id": 11,
132	          "parent": 10,
133	          "lang": "Old French",
134	          "refs": "KLN:821",
135	          "words": [
136	            {"translit": "ivurie", "gloss": null, "script": null}
137	          ],
138	          "note": null,
139	          "quote": null
140	        },
141	        {
142	          "id": 12,
143	          "parent": 11,
144	          "lang": "English",
145	          "refs": "KLN:821",
146	          "words": [
147	            {"translit": "ivory", "gloss": null, "script": null}
148	          ],
149	          "note": null,
150	          "quote": null
151	        }
152	      ]
153	    },
154	    {
155	      "root": {
156	        "name": "Yě",
157	        "redirect": "Ei"
158	      },
159	      "nodes": []
160	    },
161	    {
162	      "root": {
163	        "name": "Yekwer",
164	        "lang": "Indo-European",
165	        "refs": "POK:504",
166	        "gloss": "liver"
167	      },
168	      "nodes": [
169	        {
170	          "id": 1,
171	          "parent": 0,
172	          "lang": "Avestan",
173	          "refs": "POK:504",
174	          "words": [
175	            {"translit": "yâkara", "gloss": "liver", "script": null}
176	          ],
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 2,
182	          "parent": 1,
183	          "lang": "Pahlavi",
184	          "refs": "SNS:317",
185	          "words": [
186	            {"translit": "jakar, jagar", "gloss": "liver", "script": null}
187	          ],
188	          "note": null,
189	          "quote": null
190	        },
191	        {
192	          "id": 3,
193	          "parent": 2,
194	          "lang": "Persian",
195	          "refs": "BQT:579; POK:504",
196	          "words": [
197	            {"translit": "jegar", "gloss": "liver", "script": "جگر"},
198	            {"translit": "jegar-band", "gloss": "a dear person, child", "script": "جگربند"}
199	          ],
200	          "note": null,
201	          "quote": {"text": "بیاید پس آنگاه فرزند من - ببسته میان را جگر بند من", "poet": "Ferdowsî"}
202	        },
203	        {
204	          "id": 4,
205	          "parent": 3,
206	          "lang": "Latin",
207	          "refs": "AHD",
208	          "words": [
209	            {"translit": "gigeria", "gloss": "bird's stomach", "script": null}
210	          ],
211	          "note": null,
212	          "quote": null
213	        },
214	        {
215	          "id": 5,
216	          "parent": 4,
217	          "lang": "English",
218	          "refs": null,
219	          "words": [
220	            {"translit": "gizzard", "gloss": null, "script": null}
221	          ],
222	          "note": null,
223	          "quote": null
224	        },
225	        {
226	          "id": 6,
227	          "parent": 0,
228	          "lang": "Greek",
229	          "refs": "AHD",
230	          "words": [
231	            {"translit": "heepar", "gloss": "liver", "script": null}
232	          ],
233	          "note": null,
234	          "quote": null
235	        },
236	        {
237	          "id": 7,
238	          "parent": 6,
239	          "lang": "English",
240	          "refs": null,
241	          "words": [
242	            {"translit": "heparin, hepatic", "gloss": null, "script": null}
243	          ],
244	          "note": null,
245	          "quote": null
246	        },
247	        {
248	          "id": 8,
249	          "parent": 0,
250	          "lang": "Latin",
251	          "refs": "AHD",
252	          "words": [
253	            {"translit": "jecur", "gloss": "liver", "script": null}
254	          ],
255	          "note": null,
256	          "quote": null
257	        },
258	        {
259	          "id": 9,
260	          "parent": 8,
261	          "lang": "English",
262	          "refs": "KLN:827",
263	          "words": [
264	            {"translit": "jecoral", "gloss": null, "script": null}
265	          ],
266	          "note": null,
267	          "quote": null
268	        }
269	      ]
270	    },
271	    {
272	      "root": {
273	        "name": "Yelek",
274	        "redirect": "Ijlak"
275	      },
276	      "nodes": []
277	    }
278	  ]
279	}
280	
```


## [2026-10-17T00:30:24.020Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','KNT','PLA','MON','BQT','SYN','POK','WLD','IEC','SNS','PHD','NYB','HRN','HUB','SKT','FSD','WEB','BRT','ARY','LKT','FVQ','AFM']:\n  v=d.get(k);print(k, v and {x:v.get(x) for x in ['local_file','page_offset','kind','lookup_hint']})\n\"; sed -n 1,80p tools/verify_check.py"
}
```


### [2026-10-17T00:30:24.599Z] TOOL RESULT

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
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'kind': 'archive_djvu+website+archive_restricted', 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
KNT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt', 'page_offset': 'leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations."}
PLA {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'], 'page_offset': '301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).', 'kind': 'archive_djvu', 'lookup_hint': 'HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)'}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'kind': 'website+archive_djvu', 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'kind': 'archive_djvu+local_scan_ocr', 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'kind': 'archive_djvu', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
SNS {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt'], 'page_offset': '242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image', 'kind': 'archive_djvu', 'lookup_hint': "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping."}
PHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB)."}
NYB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
HUB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number."}
SKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt', 'page_offset': 'leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags."}
FSD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt', 'page_offset': 'vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file."}
WEB {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt', 'page_offset': 'not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': 'Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.'}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'kind': 'local_scan_ocr', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
LKT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'kind': 'archive_djvu', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number."}
FVQ {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'kind': 'archive_djvu', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).'}
AFM {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt'], 'page_offset': "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", 'kind': 'archive_djvu', 'lookup_hint': "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."}
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


## [2026-10-17T00:30:28.676Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 80,200p tools/verify_check.py; command ls data/verification/ | tail -5; python3 -c \"\nimport json;v=json.load(open('data/verification/page-558.json'));n=v['entries'][0]['nodes'][0];print(json.dumps(n,ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-17T00:30:29.038Z] TOOL RESULT

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
page-97.json
page-98.json
page-99.json
process
sources
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
}
```


## [2026-10-17T00:31:01.172Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^(elephant|ivory|element|gizzard|jecoral|hepatic|heparin|ebur)' KLN_1966.txt | head; echo ---; grep -n -i -E '^pīru|^piru|pīru-' KNT_full.txt | head; echo; grep -n -E '^yekw|^ yekw|yek[wʷ]' AHD_watkins1985.txt | head; grep -n 'lemma: i̯ek' POK_full.txt | head"
}
```


### [2026-10-17T00:31:01.459Z] TOOL RESULT

```
4286:element  is  cogn.  with  Gk.  tpaystv,  ‘to  eat’;  see -phagous  and  cp.  baksheesh.  For  the  second  ele¬ ment  see  aumildar  and  cp.  words  there  referred  to. Bahaism,  n.,  the  teaching  of  the  religious  sect  of the  Bahaists.  —  Formed  with  suff.  -ism  fr.  Pers. baha,  ‘splendor’,  fr.  Arab,  bahd' ,  of  s.m. bahar,  n.,  a  weight.  - —  Arab,  hahdr,  a  weight  used in  India,  ultim.  fr.  OI.  bhdrah,  ‘load,  weight’, which  is  rel.  to  bhdrati,  bharate,  ‘carries’,  and cogn.  with  Gk.  qilpeiv,  L.  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,  and  cp.  words  there referred  to.
7600:element  in  isochronous,  anachronism,  metachro- nism,  parachronism.
12586:Eburna,  n,,  a  genus  of  marine  gastropods,  the ivory  shell.  —  ModL.,  fr.  L.  eburnus,  ‘of  ivory’, fr.  ebur,  ‘ivory’.  See  ivory, eburnated,  adj.,  hard  like  ivory  (med)  —  Formed with  suff.  -ed  fr.  L.  eburnus,  ‘of  ivory’.  See  prec. word.
12587:eburnation,  n.,  an  increase  in  the  density  of  bone, cartilage  or  tooth  (med.)  —  Formed  with  suff. -ation  fr.  L.  eburnus,  ‘of  ivory’.  See  Eburna. eburnean,  adj.,  pertaining  to,  made  of,  or  resem¬ bling,  ivory.  —  Formed  with  suff.  -an  fr.  L. eburneus,  ‘of  ivory’,  fr.  ebur,  ‘ivory’.  See  Eburna. eburnine,  adj.,  eburnean.  —  Formed  with  suff. -ine  fr.  L.  eburnus,  ‘of  ivory’.  See  Eburna. ec-,  pref.  meaning  ‘out  of’.  —  Gk.  ex-,  fr.  lx, ‘out  of’.  See  2nd  ex-,  and  cp.  ecto-. ecarte,  n.,  a  French  card  game  for  two  persons, played  with  32  cards.  —  F.,  lit.  ‘discarded’,  pp. of  ecarter,  ‘to  discard’,  fr.  e-  (fr.  L.  e,  ‘out  of’), and  carte,  ‘card’.  See  card  for  playing  and  cp. skat.
12801:elephantiac
12807:elephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font  (F.  elephant),  fr.  L.  elephantus ,  fr.  Gk. sXsT>a;  (gen.  -av-ro;).  The  first  element  of  Gk. iX-ltpat;  appears  also  in  Hamitic  eju,  ‘elephant’, whence  prob.  Pers.  p-il,  Arab,  ph-il,  Mishnaic Heb.  p-il,  of  s.m.  The  second  element  is  an Egyptian  loan  word.  Cp.  MEgypt.  yb,  ‘ele¬ phant’,  whence  Yebu  (Heb.  Yebh),  original name  of  the  island  Elephantine;  cp.  also  the second  element  in  Heb.  shen-habbim,  ‘ivory’, lit.  ‘tooth  of  the  elephant’,  and  OI.  tbhah,  ‘ele¬ phant’.  See  ivory  and  cp.  Ebuma.  Cp.  also element.
12809:elephantiasis
12811:elephantiasis,  n„  a  chronic  disease  of  the  skin characterized  by  the  thickening  of  certain  parts of  the  body,  esp.  the  legs.  —  L„  fr.  Gk.  4Xe- (pavuotcN! ;,  fr.  &i(pas,  gen.  -av-roc,  ‘elephant’. See  elephant  and  -iasis.  According  to  Aretaeus l\ stpavTiaati;  prop,  means  ‘disease  characterized by  a  skin  resembling  that  of  an  elephant’, elephantine,  adj.,  i)  of  an  elephant;  2)  like  an elephant,  clumsy.  —  L.  elephantinus,  ‘pertain¬ ing  to  the  elephant’,  fr.  elephantus,  ‘elephant’, cp.  Gk.  iXecpavrtvo 5,  ‘of  ivory’,  fr.  eX£q>ac,  gen. -av-roc,  ‘elephant’.  See  elephant  and  -ine  (re¬ presenting  Gk.  -Ivoc).
12812:Elephantopus,  n.,  a  genus  of  plants  (hot.)  — Modi-.,  lit.  ‘the  elephant’s  foot’,  compounded of  Gk,  &i<pac,  gen,  -avro?,  ‘elephant’,  and  roue, ‘foot’.  See  elephant  and  -pod.
16188:gizzard,  n.,  the  muscular  stomach  of  a  bird.
---

1597:HENCE ko- HENDECASYLLABIC sem-1 HENDIADYS dwo-, sem-1 HENOTHEISM sem-1 HEPARIN yekwr HEPATIC yekwr HEPATITIS yek"r HEPATO- yekwr _ HEPATOGENIC yekr HEPTA- septm HEPTAD septm HeEpPTaTEuCH dheugh- HER ko-
```


## [2026-10-17T00:31:17.102Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in '^ivory,' '^element,' '^gizzard,' '^jecoral' '^hepatic' '^heparin'; do grep -n -i \"$w\" KLN_1966.txt | head -2 | cut -c1-900; done; awk 'BEGIN{RS=\"\\f\"} /elephant,  n\\.  —  ME/{print NR-1}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} /^ivory,|\\nivory,/{print \"ivory leaf\", NR-1}' KLN_1966.txt"
}
```


### [2026-10-17T00:31:17.819Z] TOOL RESULT

```
20082:ivory,  n.  —  ME.  ivorie,  fr.  OF.  ivurie  (F.  ivoire), fr.  L.  eboreus,  ‘of  ivory’,  fr.  ebur,  ‘ivory’,  bor¬ rowed  fr.  Egyptian  ab,  abu,  ‘elephant,  ivory’, prob.  through  the  medium  of  the  Phoenicians. The  same  word  appears  in  the  second  element of  Heb.  shen-habbtm,  ‘ivory’  (lit.  ‘tooth  of  the elephant’),  whence  Yebu  (=  Heb.  Yebh),  ori¬ ginal  name  of  the  island  Elephantine;  cp.  also OI.  ibhah,  ‘elephant’,  and  the  second  element in  Gk.  £X-s<pa<;,  ‘elephant’.  Cp.  ebumine, elephant
16188:gizzard,  n.,  the  muscular  stomach  of  a  bird.
17580:Hepatica,  n.,  a  genus  of  plants,  the  liverleaf  (hot.)
17582:Hepaticae,  n.  pi.,  a  class  of  plants,  the  liverworts.
277
ivory leaf 444
```


## [2026-10-17T00:31:23.543Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '16188,16190p;17580,17590p' KLN_1966.txt | cut -c1-700; grep -n -i -E '^element|^jecor|^hepar|^hepat' KLN_1966.txt | cut -c1-600 | head -20"
}
```


### [2026-10-17T00:31:23.922Z] TOOL RESULT

```
gizzard,  n.,  the  muscular  stomach  of  a  bird.
ME.  giser,  fr.  OF.  gezier,  giser,  gisier,  gusier (F.  gesier),  fr.  L.  gizeria,  ‘cooked  entrails  of poultry’,  which  is  prob.  a  Punic-Phoen.-Heb. loan  word.  Cp.  Heb.  glzdrfm,  construct  state gizrS,  ‘pieces  of  sacrificed  animals’,  pi.  of  gezer , ‘anything  cut,  a  piece’,  from  the  stem  of  gdzar, ‘he  cut,  divided’,  in  Mishnaic  Heb.  he  circum¬ cised;  he  decided,  decreed’,  rel.  to  Aram.-Syr. g‘zar,  ‘he  cut,  split,  circumcised;  he  decided,  de¬ creed’,  Arab,  jdzara,  Ethiop.  gazdra,  ‘he  cut, slaughtered’.  In  L.  gigeria,  a  collateral  form  of gizeria,  z  has  been  assimilated  to  the  preceding g.  The  final  d  in  gizzard  is  
glace,  adj.,  having  a  smooth  surface.  —  F.,  pp. of  glacer,  ‘to  freeze;  to  glaze’,  fr.  glace,  ‘ice’. See  next  word  and  cp.  glacier, glacial,  adj.,  pertaining  to  ice;  icy.  —  F.,  fr.  L. glacialis,  ‘icy’,  fr.  glades,  ‘ice’,  prob.  formed on  the  analogy  of  acies,  ‘sharp  edge,  point’,  fr. orig.  *gla-gies,  fr.  I.-E.  base  “gel-,  ‘to  freeze’, whence  also  L.  gelu,  ‘frost’.  See  gelid  and  adj. suff.  -al  and  cp.  glace,  glacier,  glacis, glacialist,  n.,  one  who  supports  the  glacial  theory. —  See  prec.  word  and  -ist. glaciate,  tr.  v.,  to  freeze.  —  L.  glaciatus,  pp.  of glaciare,  ‘to  turn  to  ice’,  fr.  glades.  See  gla
Hepatica,  n.,  a  genus  of  plants,  the  liverleaf  (hot.)
—  ML.  hepatica,  ‘liverwort’,  fr.  L.  hepatica, fem.  of  hepaticus,  ‘of  the  liver’,  fr.  Gk.  f]7raxix69, ‘of  the  liver’,  of  s.m.,  fr.  Jjrtap,  gen.  ipnxToi;, ‘liver’  (see  prec.  word);  so  called  because  the leaves  of  the  plant  resemble  the  liver.
Hepaticae,  n.  pi.,  a  class  of  plants,  the  liverworts.
—  ModL.,  prop.  pi.  of  prec.  word, hepatization,  n.,  consolidation  of  the  lung  owing
to  pneumonia  (med.)  —  Lit.  ‘appearance  of  a liver’ ;  coined  by  the  Italian  physician  Giovanni Battista  Morgagni  (1682-1771),  fr.  Gk.  -J)7ra- xi^eiv,  ‘to  be  like  a  liver’,  fr.  Jjicap,  gen.  •q7taxo9, ‘liver’.  See  hepatic  and  -ize. hepato-,  before  a  vowel  hepat-,  combining  form denoting  the  liver.  —  Gk.  Yjxaxo-,  fr.  )jxap,  gen. •ijixaxo?,  ‘liver’.  See  hepatic, hephaestic,  adj.,  pertaining  to  smiths;  —  hephaes- tic  cramp,  cramp  caused  by  the  excessive  use of  the  hammer.  —  See  next  word  and  -ic. Hephaestus,  n.,  the  god  of  fire  and  metal-working ; identified  later  with  Vulcan  ( Greek  mythol.)  — L.,  fr.  Gk.  "Htpatc
Hephzibah,  fem.  PN.  (Bible).  —  Heb.  Hephtzihdh, lit.  ‘my  delight  is  in  her’,  compounded  of hephtzf,  ‘my  delight’,  fr.  hiphetz,  ‘delight, pleasure,  desire’,  which  derives  fr.  haphitz,  ‘he delighted  in,  desired’,  and  of  bah,  ‘in  her’,  fr. b1-,  ‘in’,  with  the  fem.  suff.  of  the  3rd  person. See  hafiz.
Hepplewhite,  adj.,  relating  to  the  style  introduced in  England  by  the  cabinetmaker  George  Hepple¬ white  (died  in  1786). hept-,  form  of  hepta-  before  a  vowel, hepta-,  before  a  vowel  hept-,  combining  form meaning  ‘seven’.  —  Gk.  Erexa-,  Ettx-,  fr.  Exxa, ‘seven’,  which  stands  for  *septip  and  is  cogn. with  L.  septem,  Goth,  sibun ,  OE.  seofon,  ‘seven’. See  seven.
heptachord,  n.,  1)  a  seven-stringed  instrument; 2)  diatonic  system  of  seven  tones  (mus.)  —  Gk. Exxa/opSog,  ‘seven-stringed’;  compounded  of ETrra  (see  bepta-)  and  yopSf;,  ‘chord’.  See  chord and  cp.  words  there  referred  to. heptad,  n.,  a  group  of  seven  things.  —  Gk.  £71x04, gen.  e 77x0809,  ‘a  group  of  seven’,  formed  fr. £77x0,  ‘seven’,  with  suff.  -09,  gen.  -0804.  See bepta-  and  -ad.
heptagon,  n.,  a  plane  figure  with  seven  angles  and seven  sides  ( geom .)  —  Gk.  E7rraifojvo9,  ‘seven- cornered’,  compounded  of  Exxd  (see  hepta-)  and -yojvoc,  from  the  stem  of  y<ov(o,  ‘angle’.  See -gon.
Derivative:  heptagon-al,  adj.
heptahedron,  n.,  a  solid  figure  with  seven  plane faces  (geom.)  —  Compounded  of  hepta-  and Gk.  ESpd,  ‘seat;  base,  side,  face’.  See  -hedron. heptamerous,  adj.,  consisting  of  seven  parts.  — Compounded  of  hepta-  and  Gk.  pipo9,  ‘part’. See  -merous.
4286:element  is  cogn.  with  Gk.  tpaystv,  ‘to  eat’;  see -phagous  and  cp.  baksheesh.  For  the  second  ele¬ ment  see  aumildar  and  cp.  words  there  referred  to. Bahaism,  n.,  the  teaching  of  the  religious  sect  of the  Bahaists.  —  Formed  with  suff.  -ism  fr.  Pers. baha,  ‘splendor’,  fr.  Arab,  bahd' ,  of  s.m. bahar,  n.,  a  weight.  - —  Arab,  hahdr,  a  weight  used in  India,  ultim.  fr.  OI.  bhdrah,  ‘load,  weight’, which  is  rel.  to  bhdrati,  bharate,  ‘carries’,  and cogn.  with  Gk.  qilpeiv,  L.  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,
7600:element  in  isochronous,  anachronism,  metachro- nism,  parachronism.
17580:Hepatica,  n.,  a  genus  of  plants,  the  liverleaf  (hot.)
17582:Hepaticae,  n.  pi.,  a  class  of  plants,  the  liverworts.
40738:element  is  rel.  to  G.  laut,  ‘loud’ ;  see  loud  and  cp. ablaut,  anlaut,  auslaut.  As  a  technical  term  of grammar,  the  word  umlaut  was  introduced  by the  German  philologist  Jakob  Ludwig  Karl Grimm  (1785-1863).
```


## [2026-10-17T00:31:31.494Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '(^| )(element|jecoral|hepatic|heparin), +(n|adj)\\.[^—]*—.{0,600}' KLN_1966.txt | cut -c1-800 | head; echo ----; grep -n -B2 -A25 '^yekwr' AHD_watkins1985.txt | head -50"
}
```


### [2026-10-17T00:31:32.127Z] TOOL RESULT

```
12803: element,  n.  —  OF  (F.  element),  fr.  L.  elementum, ‘first  principle,  element’.  Of  the  many  etymo¬ logies  suggested,  the  most  probable  is  that which  derives  the  word  elementum  fr.  *elepan- tum,  ‘ivory  letter’,  an  ancient  Latin  loan  word fr.  Gk.  IXI9 avra,  acc.  of  IXl 9a?,  ‘elephant; ivory’.  The  change  of  *elepantum  to  elementum is  prob.  due  to  Etruscan  influence.  Sec  elephant. Derivatives:  element-al,  adj.  and  n.,  element-ary, adj.,  element-ari-Iy,  adv.,  element-ari-ness,  n. elemi,  n.,  a  fragrant  raisin.  —  Sp.  elemi,  fr.  VArab.
17575: heparin,  n.,  an  anticoagulant  obtained  from  the livers  of  animals  (pharm.)  —  Coined  by  the American  physiologist  William  Henry  Howell (1860-1945)  and  the  American  physician  Luther Emmett  Holt  Jr.  ( 1 895-  )  (see  the  article  “Two
17577: hepatic,  adj.,  pertaining  to  the  liver.  —  Gk.
20212: jecoral,  adj.,  pertaining  to  the  liver  (anal.)  — Formed  with  adj.  suff.  -al  fr.  L.  jecur,  gen.  je- coris,  ‘liver’,  which  is  cogn.  with  OI.  yak  ft ,  Gk. Jjmxp,  ‘liver’.  See  hepatic, jeep,  n.,  a  small  rugged  automobile.  —  Prob. contraction  of  gee  pee,  i.e.  GP,  the  initials  of General  Purpose  (Car).
----
```


## [2026-10-17T00:31:37.775Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '17575,17579p' KLN_1966.txt | cut -c1-900; grep -n -i -E 'yek.?w?r|GIZZARD|IVORY|ELEPHANT' AHD_watkins1985.txt | head -20; grep -n 'lemma: .*ek.*r' POK_full.txt | head"
}
```


### [2026-10-17T00:31:38.174Z] TOOL RESULT

```
Derivative:  heortolog-i-cal,  adj. hepar,  n.,  1)  the  liver ;  2)  a  liver-colored  substance. —  ML.,  fr.  Gk.  Ijrtap,  ‘liver’.  See  hepatic, heparin,  n.,  an  anticoagulant  obtained  from  the livers  of  animals  (pharm.)  —  Coined  by  the American  physiologist  William  Henry  Howell (1860-1945)  and  the  American  physician  Luther Emmett  Holt  Jr.  ( 1 895-  )  (see  the  article  “Two
new  factors  in  blood  coagulation  —  Heparin and  Pro-antithrombin"  in  American  Journal of  Physiology,  47,  3*8,  1918),  fr.  Gk.  Jjraxp (gen.  Y)7taTO<;),  ‘liver’  (see  hepatic),  and  chem. suff.  -in.  The  correct  form  would  have  been hepatin.
he  pat-,  form  of  hepato-  before  a  vowel, hepatic,  adj.,  pertaining  to  the  liver.  —  Gk.
721
Tj-aTixit;,  ‘of  the  liver’,  fr.  •SjTOxp,  gen.  TjmxToi;, ‘liver’,  fr.  I.-E.  base  *ylqw-r(t),  gen.  yeqw-nis, whence  also  OI.  ydkpt,  gen.  yaknah,  Avestic yakar1,  MPers.  jakar,  ModPers .jigar,  L.  jecur, OLith.  jeknos,  jekanas,  Lith.  jaknos  (pi.),  Lett. aknas,  aknis  (pi.),  ‘liver’.  Cp.  hepar,  heparin, jecoral.
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
1597:HENCE ko- HENDECASYLLABIC sem-1 HENDIADYS dwo-, sem-1 HENOTHEISM sem-1 HEPARIN yekwr HEPATIC yekwr HEPATITIS yek"r HEPATO- yekwr _ HEPATOGENIC yekr HEPTA- septm HEPTAD septm HeEpPTaTEuCH dheugh- HER ko-
1887:Root/ lemma: agro-{egro-?) {*hekrh3Uo) 
3776:From Root / lemma: aR-, oR- {* hek'^-): sharp; stone' derived Root/ lemma: aR-1, aRo- 
3858:It seems that Root/ lemma: alca- {more properly ak^i): ek"-: (water, river) derived from 
7813:Both Root/ lemma: auei- [auei-?) {*hek''ei-): bird, *water bird : Root/ lemma: ak^a- {* a/cra): 
10351:Root / lemma: b^arek*-or b^grek"- 
25053:from Root/ lemma: sAr"'^- (correct alcS). ek"- {* hek"^ : 'water, river' derived Root/ lemma: 
26523:Root / lemma: e-neuen, neup, enup {* henek'i-)'. nine' was created as a compound of Root 
27404:Root / lemma: erek-1 {erfejgh^ 
27414:Root / lemma: erek-1 {eije]gh^\ louse, tick, derived from a suffixed Root/ lemma: er-2, eri- 
27444:Root / lemma: er(e)k-2, rek-, rok-
```


## [2026-10-17T00:31:43.787Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'liver' AHD_watkins1985.txt | head; grep -n -i 'Page(s): 504' POK_full.txt; grep -n -i 'i̯ek\\|jek' POK_full.txt | grep -i lemma | head"
}
```


### [2026-10-17T00:31:44.119Z] TOOL RESULT

```
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
1111:[virére. To be green. Latin verb of unknown origin (> French verte, green). (FARTHINGALE), VERDANT, VIREO, VIRESCENT, VIRID; (BILIVERDIN), TERRE-VERTE.]
1155:wers-'. To confuse, mix up. Compare ers-'. I. Suffixed basic form. 1. Germanic *werz-a-, whence *werra- in: a. Old North French werre, war: WAR; b. Spanish gue- rra, war: GUERRILLA. 2. Germanic comparative *wers- izon- in Old English wyrsa, worse: WORSE. 3. Germanic superlative *wers-istaz in Old English wyrsta, worst: worst. II. Suffixed zero-grade form *wrs-ti- in Germanic *wursti- in Old High German wurst (> German Wurst), sausage (< “mixture”): WURST; (LIVERWURST). [Pok. uers- 1169.]
1189:yékwr. Liver. Greek hépar, liver: HEPATIC, HEPATO-;
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
40764:Page(s): 504-505 
42209:Page(s): 504 
42291:Page(s): 504
```


## [2026-10-17T00:31:52.138Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '1189,1190p' AHD_watkins1985.txt | cut -c1-400; for l in 40764 42209 42291; do sed -n \"$((l-25)),$((l))p\" POK_full.txt | tr '\\n' ' ' | cut -c1-1500; echo; echo ====; done"
}
```


### [2026-10-17T00:31:52.714Z] TOOL RESULT

```
Exit code 1
yékwr. Liver. Greek hépar, liver: HEPATIC, HEPATO-;
HEPARIN, (HEPATITIS), (HEPATOGENIC). [Pok. ieky-rt 504.]
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g^^-  Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc.   Gall, -iaio- " clearing ', often in PN, as Nanto-ialo-, French NanteuiVyaWey- clearing ', etc.;   cymr. iaii. " clearing ', PN /a/(J. Loth Mabinogion2 II 356); an-iaF waste land, wilderness ';   Note:   labialized laryngeal h2"a- > ya- > ia- Celtic   Latvian yie/s' unripe, uncultivated, raw, sore (from the skin)';   Note:   labialized laryngeal hre- > ye- > je- Baltic   Slavic j'a/band *jalo\n,\x\ xwss. jaiyjdx\^ jaiovyj^ infertile, uncultivated (of land)', serb.  Jalov^ infertile ', Czech Jalovy 6s., po\n.jafow/zna^ empty, waste place'.   Note:   labialized laryngeal h2"a- > ya- > ja- Slavic   References: Trautmann 107, Dottin Langue Gauloise 262.  Page(s): 504-505  

(eval):1: === not found
```


## [2026-10-17T00:31:56.646Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=42180 && NR<=42209' POK_full.txt | tr '\\n' ' ' | cut -c1-2500"
}
```


### [2026-10-17T00:31:57.021Z] TOOL RESULT

```
           Old Irish hicc{*iekko-) "healing, payment ', cymr. iach'iW, healthy', corn, yagh, bret. iac'h  ds. {*i9kko-), with unclear consonant doubling.     Note:   labialized laryngeal hre- > hye- > hi, h2"a- > ya-, ia- Celtic   Gr. QKOc; n. "remedy', OKEopai "heal", delph. scpaKeiaGai, aKearajp (as epithet of Apollos,  'physician, medicine man, savior, redeemer', aKsarrip 'healer, physician, medicine man'.  Epic -ionische Psilose), in Attic prose seldom used words;  Note:   labialized laryngeal hre- > 0e-, h2"a- > 0a- Greek   References: WP. I 195, WH. I 716, Schwyzer Gr. Gr. I 303;  See also: see above^eAr- 'speak'.  Page(s): 504
```


## [2026-10-17T00:32:00.498Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=42210 && NR<=42291' POK_full.txt | tr '\\n' ' ' | cut -c1-3000; echo; grep -n -i 'jecur\\|iecur' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -i 'jecur\\|iecur\\|ieq\\|jigar\\|jagar' IEC.txt | head; grep -n -i 'LIVER' SYN.txt | head"
}
```


### [2026-10-17T00:32:00.851Z] TOOL RESULT

```
 Root I temmaiJe/C-fff-J, Gen. Jek^-n-es   Meaning: liver   Material:   Note:   labialized laryngeal hre- > 0e-, h3"o- > hu-, h2"a- > ha- Hittite     labialized laryngeal PIE h"- > 0u-, 0u-, 0y-, 0i-    - West Germanic = y-, j- Old Indie = j- East    Germanic, Slavic, Old Latin, Old Albanian = w-.    f- Old Celtic = V- Old Slavic = g^-    Armenian, Celtic, lllyrian = z- Old Greek, Baltic,    Slavic = gj- Albanian Geg, gl- Albanian    Tosc.       Old \nd\c yakrt, Gen. y5/r/75/7 'liver'; pers. j7gar{*yakar-), afghan. yJna {ob\. *yaxna-)\   lengthened grade (?) Avestan yakard {aiter \N . Krause KZ. 56, 304 ff. perhaps also   Avestan *ha-yakana-, compare Old Norse litre xn. ' belonging to the same liver, brother ',   lifra\. ' sister ') =   Note:   labialized laryngeal h2"a- > ya- Old Indie   gr. nnap, -aroc; ( *-n-tos)\  Note:  labialized laryngeal hre- > 0e- Greek   Lat\njecur, -or/sand -/nor/s {proves previously *jecinis, amalgamation of A-and /7-stems);     Baltic *Jekna\. in Litliuaniany5/rA7c»s, o\6 j'eknos, jekanas, Latvian aknas, aknisi. PI. Old  Prussian iagno{y\s. lagno) f.   Note:   labialized laryngeal hre- > ye- > je- Latin, Baltic = h2"a- > ya- > ja- Baltic   After Pedersen KG. I 129 here Middle Irish i(u)chair{*ikuri-) f., Gen. i(u)chrach' roe,  eggs of a fish, eggs of various crustaceans ' and Church Slavic ikra, russ. ikra. Upper  Serbian jikro, jikno ds., that is further identical with Slavic ikra 'plaice' and ikra "calf (and of  that Baltic correspondences or rather leaning forms. Old Prussian yceroy, Latvian ikrs. Old  Lithuanian Gen. ikru) under a basic meaning 'clump, intumescence '. Also Indo Germanic  */e/r7f could be based on the same view.   It is difficult perhaps distorted taboo Armenian leard. Gen. Ierdi^\\yef (compare finally  Cuny Recherches 68 ff.). Whereas belong Old Norse iifri. 'liver'. Old English iifer, engl.  liver. Old High German libera, lebaraio gr. kxua^oo, 'fat' (see Root / lemma: leip-1\ to  smear, stick), so that the original epithet of the (fattened) liver also the old word for liver  was displaced, like LaWu jecur ficatumhas lead to Italian fegatoeic   A proto Indo Germanic basic form 7/e/r7Y appears to be risky.   References: WP. I 205 f., WH. I 673, Trautmann 103, 106, SchwyzerGr. Gr. I 518,  Benveniste Origines I 8f.  Page(s): 504  

18858:lat. jecur       ,
18892:wie jecur ficatnm zu ital. feyato usw. gefiilirt habe im Arm. ware die nach             :
18912:voe. 14S verwandte Annabme von Entlehnung des ir. Vortes aus lat jecur                                               .
6378:iequor (obl.: iequn-, iequnt-) ‘liver’. WP I, 205 Skt. yakrt, obl. yakán-; Per. jigar ($-); Oss. igár,
6387:pl. igártà, id.; Gk. &par, gs épatos; Lat. jecur, gs jecoris & jecinoris; Umb. iepru (queried: "ver": Li. jéknos, fpl. beside jáknos, id.; Latv. aknas, pl. id. (Oss. has also a form wrg, Dig. urg ‘kidney’
6388:(iequərə ‘roe’, see I-Supt: iqurà, and cf. iequər above. WP I, 206: Slav.)
2435:Rum. fd (mow used only in certain phrases), fr. Lat. fétus ‘offspring’. REW 3273. Hence fem. fatd ‘girl’ (so with Diez, Densusianu, and Pauli, op. cit. 71, more probably than as directly fr. Lat. féta ‘pregnant, newly delivered’, with shift of application to ‘one capable of childbearing’, as REW 3269, Puscariu 588, Tiktin s.v.).
5203:Liver
5275:There are a few instances (some of the words for ‘liver’, 4.45) in which the name of the organ was originally one applied to it only as an article of food, parallel to the case of ‘fish’ as an animal from ‘fish food’ (NG api, 3.65).
6475:4.45 LIVER
6479:» — higad OE lifer Boh. jdira Rum, feat i ae liver Pol. -watroba
6481:eral 0 ‘liver’ belon 0 an Inherited group. But the IE a:
6486:2. NG cuxari, dim. form of late Grk. cixwrdv, neut. of cixwrds (fr. oxo “fig’), in Frap cvxwrov, denoting the liver of ani- mals fed on dried figs, as explained in
6495:‘liver’ as an article of food (ef. Fr. foie gras). Walde-P. 1.205. Falk-Torp 639 (but with a less probable view of the semantic relation).
6496:5. Lith. kepenys, fr. kepti ‘bake, roast’, as (and prob. in imitation of) Russ. pecen’, pecenka fr. peé! ‘bake, roast’, orig:, of course, the cooked liver,
6569:ChSl. qiroba ‘belly’(?), ‘womb’ (much less frequent than éévo, Jagié, Entste- hungsgesch. 421; the examples are Where Grk. kotha is ‘womb’, but this may be accidental), SCr., Bulg., Russ, utroba ‘womb’ (in church language), Pol. wq- troba ‘liver’, all: ChSl. jetro ‘liver’, etc. (4.45).
```


## [2026-10-17T00:32:08.628Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '6475,6486p' SYN.txt | cut -c1-600; echo; grep -n -i 'ELEPHANT' SYN.txt | head; echo ---KNT; grep -n -i 'pīru\\|piru-\\|ivory' KNT_full.txt | head; echo ---PHD; grep -n -E '^(pīl|pil|jagar|jakar|ǰagar|jigar)' PHD.txt PHD_mackenzie.txt | head; grep -n -i 'elephant\\|liver' PHD.txt | head"
}
```


### [2026-10-17T00:32:08.970Z] TOOL RESULT

```
4.45 LIVER
ne rap Goth. . Lith. kepenys, jaknos (pl.) Lat se ie ON lifr Lett. aknas (pl.)
ie oat Dan. lever ChSl. jetro
! ac c Sw. lever SCr.  jetra
» — higad OE lifer Boh. jdira Rum, feat i ae liver Pol. -watroba
4 7 x, fe Yon! Nir 0a, trommchride Du. me ees, ae pecen W. oi OHG = libara ee yakara avy MHG leber(e) NHG leber
eral 0 ‘liver’ belon 0 an Inherited group. But the IE a:
pat Teplaced by others,
typical neuter r/n
alde-P 20 5 . = : 1D; 1.673, Tnout-M,
Grk. jap, gen. -aros; Lat. iecur (later qocur), gen. -oris, -inoris; Lith. jaknos (or jeknos, OLith. jekanas, all pl.), Lett. aknas (pl.); Skt. yakrt, gen. yaknas, Av. yakara, NPers. jigar.
2. NG cuxari, dim. form of late Grk. cixwrdv, neut. of cixwrds (fr. oxo “fig’), in Frap cvxwrov, denoting the liver of ani- mals fed on dried figs, as explained in

3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
3835:2. The sex of many domestic animals is shown by the use of different words, as NE oz—cow, horse—mare, ete. More generally it is shown by distinct gender forms either of the article or adjective (Grk. 6 trmos—} trros), or of the word itself (Lat. eyuus—equa), the latter in some languages so consistently (even for ‘cat’, ‘dog’, ‘elephant’, etc.) that there is only rarely occasion to use special words
3844:5. Words denoting the male or female of a particular animal may be prefixed to names of other animals, as NE buill- elephant, bull-whale, cow-elephant, and hen applied to the female of birds in gen- eral and sometimes even to the female fish (NED s.v.), Br. taro- ‘bull-’ in maout-taro ‘ram’, targaz (fr. taro-kaz) ‘tomeat’, ete.
3851:8. Skt. dhenu-.‘cow’, in cpds. ‘female’, as khadga-dhenu- ‘female rhinoceros’ (in Indic linguistic feeling prob. like NE cow-elephant, etc., above, 5, but here the general meaning is the more original), Av. daénu- used in apposition with names of ‘mule’, ‘elephant’, etc. : Skt. dhayati ‘sucks’, Grk. @4dus, Lat. fémina, etc. (2.24). Walde-P. 1.829 ff. Barth. 662.
4868:| etc.), but also to that of various large animals, as the moose, elephant, whale. Du. jonge hond, NHG junger hund, now the usual term for ‘puppy’ (in place of the old welp, welf), and so in general
5035:3.77 ELEPHANT
5039:" erégas 7 Dan. elefant is) eee ve elephantus, elephas Sw elefant Bes Bie Tt elefante OE elpend, ylp Co) slon rr Aéphant ME __ olifant, elefant Pol. ston Sp. elefante NE elephant Russ. lon. Rum. elefant Du. _ olifant Skt. hastin-, gaja-, etc. Ir. elefaint OHG  elafant, helfant Av. ge eieis NI. elephant aurfil MHG elefant, (h)elfant Ww.  aiffant, ¢ NHG  elefant Br. olifant
5041:3.77, 3.78. Nearly all the European words for ‘elephant’ and ‘camel’ are from Grk. é\epas or kayndos, which again are based upon Egyptian or Semitic words
5044:Hannibal, was subject to great distor- tion and some confusion in application with the camel in northern and north- eastern Europe, where both animals Were long known only by hearsay as strange beasts. Gre eAégas, -avros ‘ivory’ (Hom. cae elephant’ (Hdt. +), to be ana- an a dnidas; the second part, like eo 2 noe fr. Egypt. ab ‘elephant, i ae first part disputed. Schra- ? ex. 1.242. Ernout-M. 297 f.
5047:alde- ae ; a : 2. Grk. x&undos, ‘camel’, loanword fr. elephant, ae ie the Eur. words for | Semitic, Hebr. gamal, etc. Hence ence bles, ibs Balto-Slavic, through Lat. camélus (VLat. also -éllus,
---KNT
4867:from outside sources; such are piru- ‘ivory’, 
6847:to piruš ‘ivory’, cf. Lex. s.v. 
20138:brought. The ivory whieh was wrought here, was 
27521:thic for abl. after Ласа; either ‘Ivory River’, as 
27522:deriv. adj. to piru- ‘ivory’, or possibly plural ‘The 
27526:miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- 
---PHD
PHD.txt:550:pillagān 69 pušt
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:3126:pile up čīdan.
PHD.txt:3127:pillar stün(ag).
PHD.txt:3128:pillow balén, bāliš.
PHD.txt:4731:pil payray- fīlāsūfā payrāyag pērāmēn Payrāstan pīrīh péroz pérézih pérozgar
PHD_mackenzie.txt:4235:pil [pyt I M pyl, N --] elephant; (chess) bishop.
PHD_mackenzie.txt:4238:pillagan [plk)n I M pylg, N ......]steps, ladder.
PHD_mackenzie.txt:7284:pile up cidan.                             polo, ---stick caw(la)gan.
PHD_mackenzie.txt:7285:pillar stiin(ag).                          pomegranate anar.
412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
1748:elephant pil; —-driver pilban.
2648:liver jagar.
```


## [2026-10-17T00:32:13.498Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '5041,5047p' SYN.txt | cut -c1-1200; echo ---; sed -n '4860,4870p;6840,6850p;27515,27530p' KNT_full.txt; echo ---NYB; grep -n -E '^(pīl|pil|ǰakar|jakar|jagar|yakar)' NYB_vol2_glossary.txt | head; grep -n -i 'elephant' NYB_vol2_glossary.txt | head -3; grep -n -i 'liver' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-10-17T00:32:14.041Z] TOOL RESULT

```
3.77, 3.78. Nearly all the European words for ‘elephant’ and ‘camel’ are from Grk. é\epas or kayndos, which again are based upon Egyptian or Semitic words
olbanta, MHG olbente, olbende, and, through Gme. and in form influenced by velt- ‘great’, ChSI. velibadti, late
-blqdt, Boh. velbloud, Pol. wielbtad, respectively. But the name of the ele- | Russ. verbljud (> Lith. verbliudas). phant, known in southern Europe since | Feist 515. Stender-Petersen 358 fi.
Hannibal, was subject to great distor- tion and some confusion in application with the camel in northern and north- eastern Europe, where both animals Were long known only by hearsay as strange beasts. Gre eAégas, -avros ‘ivory’ (Hom. cae elephant’ (Hdt. +), to be ana- an a dnidas; the second part, like eo 2 noe fr. Egypt. ab ‘elephant, i ae first part disputed. Schra- ? ex. 1.242. Ernout-M. 297 f.
Brtickner 616. For the confusion note also that MIr. camall is used for ‘ele- phant’ in Book of Leinster (K. Meyer, Contrib. 311).
My colleague Gelb reports a Hitt. hieroglyph for ‘ox’, in this case prob. for some kind of wild ox, with accompany- ing cuneiform name wu-lu~pa-ta-sa, which may be normalized as ulupantas or ulpantas and seems to belong to the same group.
alde- ae ; a : 2. Grk. x&undos, ‘camel’, loanword fr. elephant, ae ie the Eur. words for | Semitic, Hebr. gamal, etc. Hence ence bles, ibs Balto-Slavic, through Lat. camélus (VLat. also -éllus,
---
OP abiS ‘with the waters’ (JAOS 62.269-70; 
$73.V, §130). For p in sp from pIE ky, $90; for 
b in zb from ghy, $01; for f from " in Vi"da- 
farnah-, §118.IV. 

V. OP p bf are in some instances not traceable 
to pIE forebears or are definitely borrowings 
from outside sources; such are piru- ‘ivory’, 
si"kabru- ‘carnelian’, naiba- ‘good’ (only in 
Iranian), and many place and personal names, 
such as Pirdva ‘Nile’, Putdya- ‘Libyan’, Babirus 
see $169. 

(2) In -u- stems: (Ar.) -au in loc. sg. dahyauv-à, 
-u- in loc. pl. dahyu-$uvà, -àu- in nom. sg. 
dahydu-§; see $180. Nom. sg. Dérayava*us 
and acc. -va'um with -u-, gen. -vahaus with 
(Ar.) -au-. Perhaps /Pirava, Nile’ with -àv-, 
to piruš ‘ivory’, cf. Lex. s.v. 


44 OLD PERSIAN 
pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; 
XPf 35, 38, 47. 


Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): 
Pirdva пзш. DZc 9, in naming phrase, anacolu- 
thic for abl. after Ласа; either ‘Ivory River’, as 
deriv. adj. to piru- ‘ivory’, or possibly plural ‘The 
Tusks’ (JAOS 51.209). 


miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- 
ru-§, Akk. pilu-, with cognates (or borrowings) 
in Eastern Asiatic languages (Przyluski, BSLP 


---NYB
3146:pil [pyl] elephant 2011. the rook,
3148:pilomand [~-’wmnd] big, ās as an elephant, of a bull 49°.
3149:pil-vàn [~-w’n'] elephant-keeper 20". — Probably: ‘elephant-tamier’ ‚from OPAv. (1350 spp.) van- ‘to subdue. NP pil-ban.
7331:pīl-bān: pil-van
3146:pil [pyl] elephant 2011. the rook,
3148:pilomand [~-’wmnd] big, ās as an elephant, of a bull 49°.
3149:pil-vàn [~-w’n'] elephant-keeper 20". — Probably: ‘elephant-tamier’ ‚from OPAv. (1350 spp.) van- ‘to subdue. NP pil-ban.
226:YHNSLWN-: Y'HANS' LUN, impf. 3d p. pl. of haf*el HANSEL to take away, to take back, to deliver (OAram), from "NSL
2755:nisäi [ns?y] the act of sending, conveying: ~ kartan to send off 10814; to convey 11923, -< OP *ni-cäya- from Av. (1638) ni-sray-, OP "ni-cay- 'to convey, to de- liver’.
3264:rastar one who escapes: ~ kartan to bring about an escape, to rescue, to deliver 1135-6, — NP rastär.
```


## [2026-10-17T00:32:18.775Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'jigar|ǰigar|jagar|cigar' HRN.txt HUB.txt NYB_vol2_glossary.txt | head; echo ---; grep -n -i -E '(^| )(\\d+\\. )?pīl|pil .Elefant|Elefant' HRN.txt HUB.txt | head; echo; grep -n -i 'yākar\\|yakar' BRT.txt | head -5"
}
```


### [2026-10-17T00:32:19.168Z] TOOL RESULT

```
HUB.txt:4473:ganger', skr. pafidti-; jigar *Leber, zd. yakare^ skr. yakri-;
HUB.txt:5291:yuga- ; Juft 'Genosse, Gatte* = zd. yuxta- ; jigar *Leber =
HUB.txt:8509:neben tak Xauf ' = zd. taka- ; jigar Xeber = zd. yakare,
HRN.txt:3960:\invA,jerk] afy. LW.jigar; oss. d. iger, t. igar (1»38);
HRN.txt:3961:bei. Jagar, n. ;ayar (173).
---

10187:Pü. ;  kär  varvlärlum,  Sü. :  kätyakariftantak.
```


## [2026-10-17T00:32:21.851Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '3950,3962p' HRN.txt; sed -n '4470,4474p;5289,5293p' HUB.txt; grep -n -i 'Elefant' HRN.txt HUB.txt | head; grep -n -i 'Leber' BRT.txt | head -5"
}
```


### [2026-10-17T00:32:22.387Z] TOOL RESULT

```
18, 205 und S. Bugge, KZ. 32, 8 folg.
424. Jvft ^Genosse, Gatte, Gattin; Paar ^).
aw. yu/ta-; phlv.Jw/^ (Bund.) 'Paar, arm. LW./*</^^rÄ-
*Paar'; ai. ynktä-,
kurd. öü/t (Socin), jöt (LW. aus,/w/i^); af/. j'w;^rgenau,
richtig, LWJifft 'Paar ; bei. Lw\ ju/f (116); syr. LW.
P5?1T in nnS?NP51T (de Lagarde, Ges. Abh. 42).
425. Jiger Xeber .
aw.yäkar- 'Leber; fhlv.jakar bezw. yakar (Bund.);
ai. ydkft^\ arm. leard 'Leber (H. No. 120) 2).
\invA,jerk] afy. LW.jigar; oss. d. iger, t. igar (1»38);
bei. Jagar, n. ;ayar (173).
426. Jen 'Richtung, Seite*.
des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
sassanid. Hormizd, arm. Ormizd^ ap. A(h)uramazdd; miyan
'Mitte* = paz. phi. miyan ^ zd. mai^yfina-; piyada 'Fuss-
ganger', skr. pafidti-; jigar *Leber, zd. yakare^ skr. yakri-;
paz. cihar Vier (np. cahar), zd. cadwaro; np. cihil Vierzig'
Jastan *springen, eilen' von einer Wzl. yas ? ; Jash 'Ungliick*,
zd. yaska-?; Jasn Test' = zd. yasna-; juy *Joch' = skr.
yuga- ; Juft 'Genosse, Gatte* = zd. yuxta- ; jigar *Leber =
zd. yakare ; Jau *6erste' = zd. yava- ; javan, juvan 'Jung-
ling' = skr. yuvan'\ jOsTdan *kochen, sieden', Wzl. Iran. yaus\
21530:•  j.  yäkar-  n.  'Leber':  'kan  F.Jg.
```


## [2026-10-17T00:32:28.904Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /425\\. Jiger/{print \"HRN leaf\",NR-1}' HRN.txt; awk 'BEGIN{RS=\"\\f\"} /yäkar-  n\\.  .Leber/{print \"BRT leaf\",NR-1; print substr($0,1,200)}' BRT.txt; awk 'BEGIN{RS=\"\\f\"} /jigar \\*Leber, zd/{print \"HUB leaf\",NR-1}' HUB.txt; awk 'BEGIN{RS=\"\\f\"} /pil \\[pyt I M pyl/{print \"PHDm leaf\",NR-1} /jagar \\[/{print \"PHDm jagar leaf\", NR-1}' PHD_mackenzie.txt; awk 'BEGIN{RS=\"\\f\"} /pil \\[pyl\\] elephant/{print \"NYB leaf\",NR-1}' NYB_vol2_glossary.txt;  awk 'BEGIN{RS=\"\\f\"} /piru- .ivory. \\(/{print \"KNT leaf\",NR-1}' KNT_full.txt"
}
```


### [2026-10-17T00:32:29.555Z] TOOL RESULT

```
HRN leaf 116
BRT leaf 707
Nebel  herangezogen"  YL1S33, Vgl. '<?>'-;  die  Formen  der  beiden  Basen  sind nicht  immer  sicher  lu  scheiden.    S.  auch  zn frayäi.  —    ai.  yäli  'er  geht".    —   Pii.  (lu  N.): ap^  ^
HUB leaf 138
PHDm leaf 89
NYB leaf 177
```


## [2026-10-17T00:32:36.499Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\ndef leaf(f,line):\n    t=open(f,errors='ignore').read().split('\\n')\n    return '\\n'.join(t[:line-1]).count('\\f')\nfor f,l in [('KNT_full.txt',27526),('PHD.txt',412),('PHD.txt',549),('BRT.txt',21530),('SYN.txt',5041),('SYN.txt',6475),('NYB_vol2_glossary.txt',3146),('AHD_watkins1985.txt',1189),('KLN_1966.txt',20212),('KLN_1966.txt',16188),('KLN_1966.txt',17577),('KLN_1966.txt',12807),('KLN_1966.txt',12803)]:\n    print(f,l,leaf(f,l))\nE\nawk 'BEGIN{RS=\"\\f\"} NR==708' BRT.txt | grep -o -E '^ *1[0-9]{3} *$|  12[0-9][0-9]  ' | head"
}
```


### [2026-10-17T00:32:37.286Z] TOOL RESULT

```
KNT_full.txt 27526 0
PHD.txt 412 70
PHD.txt 549 92
BRT.txt 21530 707
SYN.txt 5041 224
SYN.txt 6475 288
NYB_vol2_glossary.txt 3146 177
AHD_watkins1985.txt 1189 110
KLN_1966.txt 20212 446
KLN_1966.txt 16188 355
KLN_1966.txt 17577 388
KLN_1966.txt 12807 277
KLN_1966.txt 12803 276
```


## [2026-10-17T00:32:45.295Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==225' SYN.txt | head -5; awk 'BEGIN{RS=\"\\f\"} NR==278' KLN_1966.txt | head -3 | cut -c1-200; awk 'BEGIN{RS=\"\\f\"} /elephant,  n\\./{print \"1971 leaf\",NR-1}' KLN_1971.txt | head -2; grep -c . KLN_1971.txt"
}
```


### [2026-10-17T00:32:45.851Z] TOOL RESULT

```
 apa, OHG affo, etc., the general Gme. word, orig. unknown, perh. Celtic. Walde-P. 1.51 ff.
From Gme. come the Slavic forms, Boh. op, opice, SCr., ORuss. opica, etc. Stender-Petersen 361.
NE monkey, prob. fr. a MLG moneke (Moneke as name attested), dim. of the word that appears as Sp. mono, etc. (above, 2). NED s.v.
5. ChSl. (late) pitikd fr. Grk. riOnxos.
Boh. opice, etc. from Gme. (above, 4).
h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis.
elephant,  n.  —  ME.  elifaunt,  olifaunt,  fr.  OF.  oli- font  (F.  elephant),  fr.  L.  elephantus ,  fr.  Gk. sXsT>a;  (gen.  -av-ro;).  The  first  element  of  Gk. iX-ltpat;  appears  also  in 
Derivatives:  elephantiac  (q.v.),  elephantiasis (q.v.),  elephant-ic,  adj.,  elephantine  (q.v.),  ele- phant-oid,  elephant-ous,  adjs. elephantiac,  adj.,  one  who  has  elephantiasis.  —  L. el
221180
```


## [2026-10-17T00:32:51.002Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/563.* 2>/dev/null; pdftoppm -f 563 -l 563 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg563"
}
```


### [2026-10-17T00:32:51.755Z] TOOL RESULT

```
site/pages/563.jpg
```


## [2026-10-17T00:32:53.948Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg563.png"
}
```


### [2026-10-17T00:32:53.981Z] TOOL RESULT

```

```


## [2026-10-17T00:33:06.507Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'پیلسته' 'پیلاس' 'پیل ' ; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} index($0,w){print NR-1}' BQT_v1_pages.txt | head -20 | tr '\\n' ' '; echo; done; awk 'BEGIN{RS=\"\\f\"} index($0,\"جگر\"){print NR-1}' BQT_v2_pages.txt | head -30 | tr '\\n' ' '"
}
```


### [2026-10-17T00:33:07.373Z] TOOL RESULT

```
== پیلسته

== پیلاس

== پیل 
337 673 674 684 
36 37 38 62 86 293 332 370 463 469 526 570 648 674
```


## [2026-10-17T00:33:10.946Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==674||NR==675' BQT_v1_pages.txt | grep -n 'پیل\\|فیل\\|pil\\|pīl' | head -30"
}
```


### [2026-10-17T00:33:11.403Z] TOOL RESULT

```
9:۰ فیلبا - با بای فارسی بالف ۳
13:و آنرا معربی داءالفیل خوانئد وستونی را فز
27:چو در پیلیای فدح م یکنم
30:۷ - ركك : پیلگوش .
31:۸ - می خورکت باد نوش: برسمن وپیلگوش
32:پیل مرغ
36:پیلخوش"۷ - با غین نقطه دار بر وزن
42:ومعتی پیلفوش است که نوعی ازسوسن۸ -ورکل
48:پیل هرغ » مرغی است که از بالای
49:- از: پیل ۳- اسنه
50:باد هیبش چوخاست بشه‌شود پیلم.
54:پیل معلق در عوا
61:پیلو ار ۲ ت بسکون ثالث بروزن‌یشکاره
98:که جوهر فروش است ببا پیلمور ؟
```


## [2026-10-17T00:33:15.321Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:446 2>&1 | head -120"
}
```


### [2026-10-17T00:33:15.829Z] TOOL RESULT

```
no scan of BQT covers printed page 446 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:33:19.006Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 672 673; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -150; done"
}
```


### [2026-10-17T00:33:19.435Z] TOOL RESULT

```
=== leaf 672
بان. مقراضه
دو شاخ باشد
فیکانی » با کاف بر وزن شبطانی .
نوعی از لعل و فیرءزه باشد ۷ - و جنشی از
توشادر ح‌ هست که برشکل و هبات بان واقم
میئودو نها رالعل پیکانی‌وفيروزة پیکانی ونوشادر
پیکانی گویند .
لیگ ر ۴ - بروزن قیصرقالب وکالبدوجله
و صورت هرچبز را گونند ۲
پیکران در خشی» بکسر دون .
۱۳3 ی را گوشه ‏
ی 16
میان ملك وملکوت .
بیاث رد ایگان» کنابه ازماه است که
قمر باشد - و کنایه از سوداگر - و رامگذ.ی
هم هست- وباد صبارا نیز گویشد .
ی کردن امیك. کنابه از فاامیب
شدن باشد.
بیگرستاتن. ین را 9 وان
باجام از از آن جک محصوي مقداری ّ
وبارواح از آن حیثیت که‌نورانی است وآنرا عالم
مثال نفوی منطیمه وخیال منفصل و ارض حفیقی
خوانند ؟ .
2 44٩ --
پیگر گاو- کنابه از صراحیی باشد
ات کار
بیاك فلاث » کناب ازماه است که فمر
باشك , ۰
یی گم کردن « منم کان فارسی .
کنابه از کاری است که کسی بی‌بمطلب و مقصد
این کس نبرد .
پیکناد » بفتح کاف بروزن پیوند, ماضی_
پیوسن ودر سلك در آوردن باشد «عنی پیومست
و در سلك درا ورد وجمع نمود - و بکر اول
بروزن ربوند مقامی استاز توران زمین ۴ .
ایکندن - بر وژن و حعنی پیوستن
باشد- وبمعنی جمم کردن ودر سك کشیدن هم
همست ۵ .
فی کود کردن- کنابه از بی ندان
شدن امست
بل ای ی فا
جانوری. عمروف باشد -
و بممنی کیسه و خربطه
و گرهاید کته اند .
و ازین است که غدود را
دشتیبل گویند چه دذت
بمعتی زشت و بد و سل
بمعنیگره باشدیعنی گره
زشت و بد» چنانکه در
جای خود آمده است - یل
ز بهر دیدة خصم تو لمل پیکالی.
دحافنا شیرازی ص قکه».
۲ «اسثق ۰۳۹۱ .
۴ - رك : بیکند.
هرآنجه قارون آنرا بعمرها يکند.
رود کی سمرقندی. ۶ جهانگیری؟.
مشتق‌است ست «تفس» . رك: بان برتیا .
=== leaf 673
- ۷ -
پیالاد ۵ - بارای‌قرشت بروزن مینافام,
نام حصاری است ت عظیم‌و بز رگث.
بیل‌افکندن کنابه از عاجز کردن
باشد .
یل آهرو ۵ بامیم و رای بی ننطه
بر وزن قیراندود ؛ نوعی از امرود است و آن
صسوم‌ای باشد حعروف.
۰ فیلبا - با بای فارسی بالف ۳
نام حربه‌ایت ه بیشتر زنگان‌دارند - ونوعی
از قدح بزر کب شرامخواری باشد ۱ - و مرنی
است که بای ادمی ورم میکند و بز رکه میشود
و آنرا معربی داءالفیل خوانئد وستونی را فز
کویند که سفف برآن قرار کیرد .
یل لا لا- بابای ابد بروزن میرلالا »
توده وخرمن کرده وسیار را گویند - و کنابه از
ید 0 آمده است (۱).
یل با ‌‌ ستوتیرا گوین د که ا زگچ
2 بر بللای آن بابهای طاق
گذارند۴ ۰
کن ۲ یک از القاب رستم دستان گنت واسبرا
نیز کوبند .
شلسته بروزن سدسته, رخساره‌وروی‌را
گونند ‌ و یمعنی ساعذ دست‌هم مت وانگشت
(۱) چك: هم هست.
۱ - ر4 : بل بابه .
چو در پیلیای فدح م یکنم
:یلا .
(استخو ان) ۰ ستی
۷ - ركك : پیلگوش .
۸ - می خورکت باد نوش: برسمن وپیلگوش
پیل مرغ
دست رالیز گفته‌اند ض بهعتی عاج‌حم بظرآعده
ببران وسهاست واویردست رستم کته عیلا" 2
و بضم رابم سم سطبر وسخت راگویند. و کثابه
پیلخوش"۷ - با غین نقطه دار بر وزن
دیگه جوش .کلی است ازجنس سوسن‌وب ی کتار.
های‌آن خالهای سیاء و رخنهای کوچك باشد -
وگل نیلوفررا نیز کوبند- وچیزی هم هس تکه
خالك انداز گوبند .
یلگوش - با کاف فارسی » بر وزن
ومعتی پیلفوش است که نوعی ازسوسن۸ -ورکل
که ترا لوف گویند » را بمربی‌اصل‌اللوف
و کل ربواج دا نیز 27 و بعر بی 97
خوانند ۰
یل ما" با میم بر وزن‌ییرزال» کنابه
از پی‌سپر کردن وپایمال نءودن باشد.
پیل هرغ » مرغی است که از بالای
- از: پیل ۳- اسنه
باد هیبش چوخاست بشه‌شود پیلم.
خافانی شروالی. « جهانگیری».
روز رش ورام وجوش. روز خور وماه وباد ‏
+ متوچپری ۱۸ - باصحیح نارنده ۴
```


## [2026-10-17T00:33:27.414Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'جگر' incoming/ARY/ARY_pages.txt | head -5; grep -n -i 'JIGAR\\|JEGAR\\|PIL\\b' incoming/ARY/ARY_latin_index_pages.txt | head -5; grep -n 'پیلسته\\|پیلاس' MON_part1.txt MON_part2.txt | head -5; grep -n '^جگر\\|جگر بند\\|جگربند' MON_part1.txt | head -5"
}
```


### [2026-10-17T00:33:27.777Z] TOOL RESULT

```
423:BEL) 9 ee SL Oe are alt Sassy» PIL ry Jedas SUT sey
6136:IKRA JIGAR, DZIGAR
MON_part1.txt:35569:پیلس: هام [- پیلسته - بیلاس] (امر.) 
MON_part1.txt:35572:پیلسته: (و)هادداآم [ییل + استه (- است 
MON_part1.txt:35573:<استخوان >) - پیلاس - پیلس - فیلسته| 
28081:جگر پارة تن. جگر گوشه. پارةٌ ر: قراضه. 
48066:جگر 1 کند (آگند): (ه«معهممرج 1‏ 
48075:جگرک: (-.ع2-21»)16عج[ (ا.مصف.) جکر 
48078:جگرگوشه: (0-)2کناع-.1 (امر.) باره‌ای از 
48079:جگر. (کد.) فرزند؛ ج. جگرگوشگان.
```


## [2026-10-17T00:33:32.682Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '35565,35580p' MON_part1.txt; grep -n 'جگر' MON_part1.txt | sed -n '1,40p' | grep -n 'په\\|(ا' | head; awk 'NR<=6136 && /\\[pdf page/{p=$0} NR==6136{print p}' incoming/ARY/ARY_latin_index_pages.txt; sed -n '6125,6140p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-10-17T00:33:33.061Z] TOOL RESULT

```
پیلتن: ممد-اآم [- فیلتن ] (ص‌مر.) دارای 
اندامی چون پیل» بزرگ جثه. عظیم‌الجثه» 
سیار زورمند (چون فیل). (اخ.) لف رستم 
ین زال. (استعاره) اسبی که بیل پیکر باشد. 
پیلس: هام [- پیلسته - بیلاس] (امر.) 
پبلسته» عاج. 

پیلسته: (و)هادداآم [ییل + استه (- است 
<استخوان >) - پیلاس - پیلس - فیلسته| 
(امر.) استخوان فىل» دندان فیل» عاج. (محد.) 
انگشت دست» اصبع. (مج.) ساعد (دست.) 
رح روی» رخساره. 

پیلسم: .2 [- - فیلسم | (امر.) سم ستبر و 
درشت و سخت. (ص‌مر.) اسبی دارای تیم 
ضحم و گران. (مج.) اسب قوی و زورآور. 
15:48071:چگر بند: 0-.[. (امر .) مجموع جگر و 
16:48075:جگرک: (-.ع2-21»)16عج[ (ا.مصف.) جکر 
17:48078:جگرگوشه: (0-)2کناع-.1 (امر.) باره‌ای از 
[pdf page 212]
SKEAT: (EVER) 201-202 EL (OLD SCANDINAVIAN) 5 5the!
ofr igbi say :(OLD HIGH GERMAN) 6S gall
10, EO, EWA
Jeadhoal
ASG BLS Hey Secle y3 ly gal oe
HEPAR, HEPATOS — (GREEK) iy TAKARE AAVESTAN): gah |
JECUR, JECORIS (LATIN) 5s JAGAR, JIKAR 3} eantLavy 34
FOIE FRENCH) 413 IGAR, IGER HOSSETIC) goa 3) |
HIGADO (SPANISH) gli JERK (KURDISH) 53,5 !
FEGATO A(TALIAN) gldly\ JAGAR ABALUCHD) ge se
OLD CHURCH SLAVIC) 4S 5s! AFGHAN) (4) glait
IKRA JIGAR, DZIGAR
IKRA (RUSSIAN) gay y YAKRT, YAKNAS:(SANSKRIT) <4 Sails
[pdf page 213]
|
(ae glo JS) ye [TAF |
```


## [2026-10-17T00:33:37.062Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '48060,48077p' MON_part1.txt; grep -n '^پیل:' MON_part1.txt | head -3"
}
```


### [2026-10-17T00:33:37.398Z] TOOL RESULT

```
(جاذ. بز.)» (تد. .عم.) عزیز» عزیز دلم (به 
فرزندان و پسران و دختران گرامی اطلاق 
۳۵ غم. غصه ر نج محنت. انتظار. 
وسط هر چیزء میانه. شفقت» مرحمت. 
شحاعت» دلبری. 

جگر 1 کند (آگند): (ه«معهممرج 1‏ 
بچکرا کنلاه با غتا | زا اشاه وه 
گوسفند که آن را با گوشت و مصالح پر 
کرده باشند؛ عصیب؛ چرغند. 

چگر بند: 0-.[. (امر .) مجموع جگر و 
شش و دل (در انسان و حیوان). فرزند. هر 
چیز لاغر و زبون. 

جگرک: (-.ع2-21»)16عج[ (ا.مصف.) جکر 
گوسفند. خوراکی که از گر گوسفند 
سازند و با روغن و پیاز در تابه تف دهند. 
35526:پیل: اآ« [آشوری» معر. فیل] (ا.) (جان.) 
35540:پیل: اآ« |- بیل] (.) گره» غده: دشپیل.
```


## [2026-10-17T00:33:42.139Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'jagar\\|jakar\\|yakar' SNS_pages.txt SNS.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==37' BQT_v2_pages.txt | grep -n -A3 'جگر\\|jag\\|yak' | head -40"
}
```


### [2026-10-17T00:33:42.597Z] TOOL RESULT

```
SNS.txt:17179:.jSV:jagar; ia> 
SNS.txt:29226:yakar- 317/ 7 
SNS.txt:32447:jagar 317/6 
SNS_pages.txt:12397:                                                                    .jSV:jagar;              ia>                                                                                           W>
SNS_pages.txt:15132:buray- 110/12              raS    39/16                            yakar- 317/      7           vayu- 263/22
SNS_pages.txt:16083:hist 205/18                                                    jagar 317/6               kahisn 208/5
48:       ‫جگره بروزن شکر ‪ ۰‬کرد و خاك را‬
49-       ‫گویند‪ -‬ویزبان‌علمی‌هند نیزهمین‌معنی دارد ‪٩‬‏‬                      ‫جکاشه ‪ -‬بنتح اول بروزن خلاشه »‬
50-
51-
```


## [2026-10-17T00:33:47.380Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '17170,17185p' SNS.txt; for n in 35 36 37 38; do echo \"== $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -n 'جگر' | head -8; done"
}
```


### [2026-10-17T00:33:47.981Z] TOOL RESULT

```
• TY/U^ 

* 

.^:yak: 3j 

.*/Yl^ .,/«( :yak-5: -»-»3l> (*^.i)A-*/Y^ (**<***>) 
.*,/•<)£ {^h f> -^)^*-:3 yak: -*£_>" 

.jSV:jagar; ia> 
£kto.l282)yakrt : ^j^- ySkara -/ySkar- : fc- 

-.oibjl^^t^l :5stad: yK^MNN-^t : >•: V^"^ 1 ^ 

■YA/16^ -»«/A^ .^ 

== 35
== 36
48:       ‫جگره بروزن شکر ‪ ۰‬کرد و خاك را‬
== 37
9: ‫جگر بنك ‪ -‬بابای‌ابجد بروزن‌خردمند»‬                                                           ‫گویند ‪.‬‬
10:‫مجموع جگر و شش و دل را کوبند خواه از‬                ‫جگتیبو فستن؟ ‪ -‬بافوقانی و نحتالی‬
14:‫کنابه ازعا قشق باشد ‪-‬‬    ‫جگر فته‬                    ‫چگره بکر اول و فتح انی و سکون‬
20:‫جمعی باشنفد از‬    ‫خواره ‪-‬‬           ‫جگر‬                                    ‫مشت‌هم آمده ا ت‬
38:           ‫یاجگر بندپیش زاغ بنه‪.‬‬                      ‫ببتاشوش وغصه راضی شو‬
45:  ‫زنی بوده سخت‬    ‫پردل ‪ .‬دلاور‪ « :‬مادرحسنك‬       ‫بکی اول و فتح واو“‬      ‫‪-‬‬   ‫جگر آور‬     ‫*‬
== 38
4: ‫(‪ )۱‬بمعنی زدن‬        ‫پپلوشکن » بافت زپندازوند‬          ‫بسکون‬         ‫جگر گر به خوردن ‪-‬‬
11:‫وکاف فارسی بتحتانی کشیده » لففلی است که در‬               ‫جگر گو شه = باره‌ای ازجگر باشد‬
15: ‫کوبند » زوان بهنگام لذت مباشرت بزربان‬                   ‫جگر نهس بروزن درمنه » مرفی امت‬
24:                                          ‫وا‬             ‫جگرو نتن ‪ ۳‬بداتای فرشت بر وزن‬
40:  ‫رك ‪ :‬جگربند ‪ - ۳ .‬هز » ‪ [020(1)06۲(4)82‬و نظایرآن " بهلوی ‪ , 020202۵‬زدن ‪.‬‬                               ‫‪۱‬‬
```


## [2026-10-17T00:33:51.645Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==37' BQT_v2_pages.txt | sed -n '1,60p' | grep -v '^\\s*$' | cut -c1-250 | head -70"
}
```


### [2026-10-17T00:33:52.092Z] TOOL RESULT

```
        ‫‪۸۷0‬‬                                                                                                 ‫جفت کاو‬
       ‫باهم‪ -‬و کنابه از جماع و مباثرت هم‌هست ‪.‬‬                         ‫کاتویراند ‪۱‬‬
                                                                                 ‫جفت گاو سکاو زر‬
                                                                                                    ‫ویعربی فدان خوانند‪.‬‬
                                                                       ‫از طاق ابوان‬         ‫به‬
                                                                                             ‫نسامس‬
                                                                                                 ‫جفت مکقو‬
                                         ‫و مباشرت باشد ‪.‬‬
                                                                                                           ‫وعمارت باشد ‪.‬‬
       ‫قرشت بر‬     ‫وای‬
                     ‫جفر سته ‪ -‬بفتح اول ر‬
                                                                       ‫جفته = بفتح اول بروزن هفته » خمیده‬
       ‫وزن سربسته » ربسمان خامی باشد که در وقت‬                          ‫و کج باشد ‪ -‬و چوب‌بندی‌تا انگور ‪ ۴‬وسقف‬
       ‫رشتن پنبه بردوكپیچیده‌شود ‪ ۴‬؛ وبا جیم‌فارسی‬                     ‫خانه را گونند ‪ -‬و طاق ابوان را همگفته انب‬
                                          ‫‪:‬‬   ‫است‬    ‫هم امده‬
                                                                        ‫وم اول‌سرین و کفل مردم و اسب و شتروغیره‬
   ‫‪ ۰‬شخصی را‬                ‫ری‬
                             ‫ضوزن‬
                                ‫جقر ی ‪-‬خبر‬                              ‫وتر‬
                                                                          ‫باشد ‪ -‬و لگدیرا نیزگویند که اپ ش‬
                                                                       ‫آندازند ‪ - ۴‬و کره رسمان را هم‬
                                                                                                   ‫ومثال ا‬
                                                                                                         ‫ا‬
                                                                                                                 ‫‪۹۳‬‬
       ‫گونند که علم حفر دائد و آن علمی است مشهور‪-‬‬
       ‫و معرب کفری‌هم‌هست که پوست بهار خرمای‬
                                                 ‫‪۰‬‬   ‫ماده باشد‬          ‫جفتی ردن‪ .‬جفت شدن‌حوانات‌باشد‬
                                                       ‫بیان سیز دهم‬
                              ‫در جیم ابجد باکاف تازی مشتمل برچهار لغت‬
   ‫خاریشت بزرکه را کوبند که خارهای خود را‬                               ‫جث ‏ بنتح‌اول وسکون ثانی‪,‬جنبانیدن‬
   ‫ماتند تبربجاب خصم اندازد و او را روباه ترکی‬                          ‫ا مکه‬       ‫باشد درمشکی تاسویی‬      ‫ماست وحغرات‬
                                              ‫نمییزگویند ‪.‬‬             ‫و کر آن‌از دوغ جداشود سویمعئی برات‌هم آمده‬
       ‫جکاك ‏ باکاف و حرکت غیر علوم ‪,‬‬                                   ‫‪۵۵‬‬    ‫است و بان معنی ا جیم فارسی‌هم گفته اند‬
                       ‫انگور زبون وضایع را گوبند ‪.‬‬                      ‫شب پانزدهم ماه شعبان را نگیوزبند چه شب‬
                                                                                                      ‫جك شب برات‌است‪.‬‬
       ‫جگره بروزن شکر ‪ ۰‬کرد و خاك را‬
       ‫گویند‪ -‬ویزبان‌علمی‌هند نیزهمین‌معنی دارد ‪٩‬‏‬                      ‫جکاشه ‪ -‬بنتح اول بروزن خلاشه »‬
  ‫‪0‬‬
         ‫دراصطلاح روستائان» مقدار زمینی‌را که بك زارع ا دو گاو ممتواند زراعت کند «جفت کاو»‬                         ‫سح‬   ‫‏‪١‬‬
‫شم‬
 ‫هه‬
  ‫امروزجفتك بضم اول وفتح سوم گویند و‬
```


## [2026-10-17T00:33:56.284Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==38' BQT_v2_pages.txt | grep -v '^\\s*$' | cut -c1-260 | sed -n '1,12p;40,80p'"
}
```


### [2026-10-17T00:33:56.679Z] TOOL RESULT

```
                                     ‫بیان چهار دهم‬
            ‫سبزده لغت و کنات‬               ‫درجم أجد با کاف فارسی ‪۹7‬‬
‫جگارن ‪ = ۱‬بفتح اول بر وزن هزاره» || که آنرا باکوشت و مصالح پر کرده باشند »‬
                 ‫® ‪0‬‬     ‫اش‬
                          ‫اىرفص‬
                              ‫وان و زوفهای کلف ‪۱ ۱:‬وت‬
                                                    ‫زانیا و تسه ز‬
 ‫جگر بنك ‪ -‬بابای‌ابجد بروزن‌خردمند»‬                                                           ‫گویند ‪.‬‬
‫مجموع جگر و شش و دل را کوبند خواه از‬                ‫جگتیبو فستن؟ ‪ -‬بافوقانی و نحتالی‬
‫و بای ابجد وواو و نون وسین‌سعفص وتای‌قرشت | انان باشد و خواه ازحیوانات‌دیگر ‪ » ۱‬وبعربی‬
 ‫بروزن منزل پرسیدن ‪ ۰‬بلغت زند و پازند (‪ | )۱‬سوادالبطن خوالند‪ -‬کونابه‌ازفرزند همهت ‪۷‬‬
      ‫و هر چیز که آن لاغر و زیون باشد ‪.‬‬                                           ‫بمعنی نوشتن باشد ‪.‬‬
  ‫زنی بوده سخت‬    ‫پردل ‪ .‬دلاور‪ « :‬مادرحسنك‬       ‫بکی اول و فتح واو“‬      ‫‪-‬‬   ‫جگر آور‬     ‫*‬
                                                                  ‫گر آور» هریخ بت ‪۹۸۱‬‬
```


## [2026-10-17T00:34:02.178Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -40"
}
```


### [2026-10-17T00:34:02.514Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

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


## [2026-10-17T00:34:11.286Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; for u in \\\n\"https://www.etymonline.com/word/elephant|page 563, root Yb, elephant chain\" \\\n\"https://www.etymonline.com/word/ivory|page 563, root Yb, ebur/ivory chain\" \\\n\"https://www.etymonline.com/word/element|page 563, root Yb, elementum theories\" \\\n\"https://www.etymonline.com/word/gizzard|page 563, root Yekwer, gigeria\" \\\n\"https://www.etymonline.com/word/hepatic|page 563, root Yekwer, hepatic\" \\\n\"https://www.etymonline.com/word/heparin|page 563, root Yekwer, heparin\" \\\n\"https://en.wiktionary.org/wiki/پیل|page 563, root Yb, Persian pil\" \\\n\"https://en.wiktionary.org/wiki/پیلسته|page 563, root Yb, pilasta ivory\" \\\n\"https://en.wiktionary.org/wiki/ἐλέφας|page 563, root Yb, Greek elephas\" \\\n\"https://en.wiktionary.org/wiki/ebur|page 563, root Yb, Latin ebur\" \\\n\"https://en.wiktionary.org/wiki/elementum|page 563, root Yb, Latin elementum\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yékʷr̥|page 563, root Yekwer\" \\\n\"https://en.wiktionary.org/wiki/جگر|page 563, root Yekwer, Persian jegar\" \\\n\"https://en.wiktionary.org/wiki/gigeria|page 563, root Yekwer, Latin gigeria\" \\\n\"https://en.wiktionary.org/wiki/jecoral|page 563, root Yekwer, jecoral\" \\\n\"https://en.wiktionary.org/wiki/אלף|page 563, root Yb, Hebrew eleph\" \\\n\"https://en.wiktionary.org/wiki/𐎱𐎡𐎽𐎢|page 563, root Yb, OP piru\" \\\n\"https://en.wiktionary.org/wiki/elephantus|page 563, root Yb, Latin elephantus\" \\\n; do python3 $F \"${u%%|*}\" --note \"${u#*|}\"; done 2>&1 | tail -20"
}
```


### [2026-10-17T00:34:22.358Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5468486d2ec3ed5a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bdc765c96d2d9a22.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/495155cff8cf7766.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a0b46bf88c83da37.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eabeaa838bdd6dae.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f8d06ba4a71eddd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e610310eb2ed378b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c6944c394dc921f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0f0f849a705387b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/db3253e6819fddea.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4181206801b6058f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60fb8485f26300fd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dcf45eff21724805.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4bfee2b9b3cbe92f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0376ad6d430138dc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7ce84ee457a57755.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2e5c34bfc9e185e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/909fd0a06ea30338.txt
```


## [2026-10-17T00:34:25.481Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -18 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['status'],d['bytes'],d['url'][:70],d['file'])\""
}
```


### [2026-10-17T00:34:25.903Z] TOOL RESULT

```
-1 39 https://www.etymonline.com/word/elephant data/verification/sources/web/5468486d2ec3ed5a.txt
-1 39 https://www.etymonline.com/word/ivory data/verification/sources/web/bdc765c96d2d9a22.txt
-1 39 https://www.etymonline.com/word/element data/verification/sources/web/495155cff8cf7766.txt
-1 39 https://www.etymonline.com/word/gizzard data/verification/sources/web/a0b46bf88c83da37.txt
-1 39 https://www.etymonline.com/word/hepatic data/verification/sources/web/eabeaa838bdd6dae.txt
-1 39 https://www.etymonline.com/word/heparin data/verification/sources/web/8f8d06ba4a71eddd.txt
200 10561 https://en.wiktionary.org/wiki/پیل data/verification/sources/web/e610310eb2ed378b.txt
-1 39 https://en.wiktionary.org/wiki/پیلسته data/verification/sources/web/4c6944c394dc921f.txt
200 7281 https://en.wiktionary.org/wiki/ἐλέφας data/verification/sources/web/c0f0f849a705387b.txt
200 7501 https://en.wiktionary.org/wiki/ebur data/verification/sources/web/db3253e6819fddea.txt
200 7226 https://en.wiktionary.org/wiki/elementum data/verification/sources/web/4181206801b6058f.txt
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yékʷ data/verification/sources/web/60fb8485f26300fd.txt
200 7535 https://en.wiktionary.org/wiki/جگر data/verification/sources/web/dcf45eff21724805.txt
200 3745 https://en.wiktionary.org/wiki/gigeria data/verification/sources/web/4bfee2b9b3cbe92f.txt
200 2053 https://en.wiktionary.org/wiki/jecoral data/verification/sources/web/0376ad6d430138dc.txt
200 6941 https://en.wiktionary.org/wiki/אלף data/verification/sources/web/7ce84ee457a57755.txt
-1 39 https://en.wiktionary.org/wiki/𐎱𐎡𐎽𐎢 data/verification/sources/web/b2e5c34bfc9e185e.txt
200 4166 https://en.wiktionary.org/wiki/elephantus data/verification/sources/web/909fd0a06ea30338.txt
```


## [2026-10-17T00:34:31.989Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; cat 5468486d2ec3ed5a.txt; for f in e610310eb2ed378b c0f0f849a705387b db3253e6819fddea 4181206801b6058f dcf45eff21724805 4bfee2b9b3cbe92f 0376ad6d430138dc 909fd0a06ea30338; do echo \"=== $f\"; grep -i -A6 'Etymology' $f.txt | head -24 | cut -c1-700; done"
}
```


### [2026-10-17T00:34:32.502Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/elephant
FETCHED: 2026-10-17T00:34:11Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden=== e610310eb2ed378b
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 
--
 Etymology 

 3.2 
 Noun 

 4 
 Ottoman Turkish 
--
 Etymology 

 4.2 
 Noun 

 4.2.1 
 Derived terms 
--
=== c0f0f849a705387b
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 
--
 Etymology
 [ edit ] 

Earlier form: Mycenaean Greek 𐀁𐀩𐀞 ( e-re-pa /⁠elephās⁠/ ) . Probably borrowed from Egyptian ꜣbw 

 (reconstructed as earlier /ˈʀuːbaw/, later /ˈjuːbə/). [ 1 ] . Cognate with Latin ebur ( “ ivory ” ) and Sanskrit इभ ( íbha ) . For the first half compare Hittite 𒆷𒄴𒉺𒀸 ( laḫpaš , “ ivory ” ) , Proto-Berber *eləw , Hebrew פיל , possibly also Ancient Greek ἔλαφος ( élaphos , “ deer ” ) .

 ( Can this ( + ) etymology be sourced ? Particularly: “Sources for the first half”) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /e.lé.pʰaːs/ → /eˈle.ɸas/ → /eˈle.fas/ 

=== db3253e6819fddea
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 
--
 Etymology 

 2.2 
 Noun 

 3 
 Old High German 
--
 Etymology 

 3.3 
 Noun 

 3.3.1 
 Declension 
--
=== 4181206801b6058f
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 
--
 Etymology
 [ edit ] 

 Uncertain. Perhaps ultimately from L M N , first three letters of the second half of the Canaanite alphabet, recited by ancient scribes when learning it (in sense compare English ABC(s) ( “ fundamentals ” ) ). This idea has been criticized though due to the absence of any evidence for use of a half-split in the Latin alphabet itself and the lack of evidence for the use of "el", "em", and "en" as letter names in early Latin. [ 1 ] An alternative related idea is that elementum was borrowed into Latin from a Semitic term (probably via Egyptian ) halaḥama , which derives from the old South Semitic initial character sequence, h-l-ḥ-m..., though this presents some difficulties as well.

 Alternatively could be a neologism to translate the equivalent Greek term στοιχεῖον ( stoikheîon , “ element, letter ” ) (introduced in the sense of "element" by Plato), which, like the Latin elementum , has the dual meaning of "element" and "letter". This neologism would be modelled on and alluding to alimentum ( “ nourishment ” ) , modified to be a mnemonic for the sequence of letters "L M N"; this would make it related to alere ( “ to nourish ” ) , olēscere ( “ to grow ” ) , both from Proto-Indo-European *h₂el- . [ 2 ] 

=== dcf45eff21724805
 Etymology 

 3.3 
 Pronunciation 

 3.4 
 Noun 
--
 Etymology 

 4.2 
 Noun 

 4.3 
 References 
--
 Etymology 

 5.2 
 Pronunciation 

 5.3 
 Noun 
--
=== 4bfee2b9b3cbe92f
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 
--
 Etymology
 [ edit ] 

 Uncertain; possibly from Middle Persian (compare Persian جگر ( jegar ) ), or from a cognate in another language, which would ultimately be from Proto-Indo-European *Hyékʷr̥ ( “ liver ” ) , whence the inherited iecur .

 Pronunciation
 [ edit ] 
--
 Douglas Harper ( 2001–2026 ), “ gizzard ”, in Online Etymology Dictionary . 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=gigeria&oldid=88856961 "

 Categories : English non-lemma forms 
 English noun forms 
 English plurals in -a with singular in -um 
=== 0376ad6d430138dc
 Etymology 

 1.2 
 Adjective 

 Toggle the table of contents 

--
 Etymology
 [ edit ] 

 From Latin jecoris , from jecur ( alternative form of iecur ).

 Adjective
 [ edit ] 
=== 909fd0a06ea30338
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 
--
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Afroasiatic *leb- 
 Egyptian ꜣbw bor. ? 
 Ancient Greek ἐλέφας ( eléphas ) bor. 
 Latin elephantus 

--
 Pages with etymology trees 
 Latin entries with etymology trees 
 Latin entries with etymology texts 
 Pages using etymon with no ID 
 Pages with entries
```


## [2026-10-17T00:34:36.604Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in e610310eb2ed378b db3253e6819fddea dcf45eff21724805 7ce84ee457a57755; do echo \"=== $f\"; grep -A4 'Etymology$' $f.txt | grep -v '^\\s*$' | grep -v 'edit \\]' | head -20 | cut -c1-700; grep -i -E 'from |borrow' $f.txt | head -8 | cut -c1-500; done"
}
```


### [2026-10-17T00:34:37.077Z] TOOL RESULT

```
=== e610310eb2ed378b
 Etymology
 From Persian پول ( pul ) .
--
 Etymology
 Borrowed from Sanskrit पेशी ( peśī ) .
--
 Etymology
 Borrowed from Persian پیل ( pil , “ elephant ” ) , from Middle Persian pyl ( /⁠pīl⁠/ ) , ultimately from Akkadian 𒄠𒋛 ( /⁠pīru⁠/ ) . Doublet of فیل ( fil , “ elephant ” ) .
--
 Etymology
 Borrowed from Classical Persian پیل ( pīl ) .
--
 Etymology
 Borrowed from Classical Persian پیل ( pīl ) . Cognate with Pashto پيل ( pil ) .
 From Wiktionary, the free dictionary
 From Persian پول ( pul ) .
 Borrowed from Sanskrit पेशी ( peśī ) .
 Borrowed from Persian پیل ( pil , “ elephant ” ) , from Middle Persian pyl ( /⁠pīl⁠/ ) , ultimately from Akkadian 𒄠𒋛 ( /⁠pīru⁠/ ) . Doublet of فیل ( fil , “ elephant ” ) .
 elephant , a mammal of the order Proboscidea , having a trunk , and two large ivory tusks jutting from the upper jaw 
 ( chess ) bishop , the chess piece which moves along diagonal lines and developed from the shatranj alfil ("elephant")
 Borrowed from Classical Persian پیل ( pīl ) .
 From Middle Persian pyl ( /⁠pīl⁠/ ) , from Akkadian 𒄠𒋛 ( pīru ) .
=== db3253e6819fddea
 Etymology
 Etymology tree
--
 Etymology
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
--
 Etymology
 From Proto-West Germanic *ebur . Cognates include Old English eofor , Old Norse jǫfurr .
 From Wiktionary, the free dictionary
 Loan word, probably from Demotic Egyptian yb ( “ ivory, Elephantine ” ) , from Egyptian 
 R. E. Latham , D. R. Howlett, & R. K. Ashdowne, editors ( 1975–2013 ), “ ebur ”, in Dictionary of Medieval Latin from British Sources ‎ [1] , London: Oxford University Press for the British Academy , →ISBN , →OCLC 
 From Proto-West Germanic *ebur . Cognates include Old English eofor , Old Norse jǫfurr .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ebur&oldid=92064532 "
 Latin terms derived from Demotic Egyptian 
 Latin terms derived from Egyptian 
 Latin terms derived from Proto-Afroasiatic 
=== dcf45eff21724805
 Etymology
 Inherited from Middle Persian ( ykl /⁠jagar⁠/ ) , from Old Persian , from Proto-Iranian *yákr̥ , from Proto-Indo-Iranian *Hyákr̥ , from Proto-Indo-European *Hyékʷr̥ ( “ liver ” ) .
--
 Etymology
 Borrowed from Classical Persian جِگَر ( jigar ) .
--
 Etymology
 Borrowed from Classical Persian جِگَر ( jigar ) .
--
 Etymology
 From Urdu جِگَر ( jigar ) .
 From Wiktionary, the free dictionary
 Inherited from Middle Persian ( ykl /⁠jagar⁠/ ) , from Old Persian , from Proto-Iranian *yákr̥ , from Proto-Indo-Iranian *Hyákr̥ , from Proto-Indo-European *Hyékʷr̥ ( “ liver ” ) .
 Borrowed from Classical Persian جِگَر ( jigar ) .
 Borrowed from Classical Persian جِگَر ( jigar ) .
 From Urdu جِگَر ( jigar ) .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=جگر&oldid=92378756 "
 Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
=== 7ce84ee457a57755
 From Wiktionary, the free dictionary
 From Proto-Semitic *ʔalp- ( “ thousand; cattle ” ) . Cognate with Arabic ألف ( ʔalf ) .
 Tanach , Exodus 12:37 , with translation of the Jewish Publication Society The value tsrc=JPS is ambiguous and deprecated. After checking the translation, please replace it with JPS1917 , JPS1985 , or JPS2023 . See the documentation . : וַיִּסְעוּ בְנֵי־יִשְׂרָאֵל מֵ רַעְמְסֵס סֻכֹּתָ ה כְּ שֵׁשׁ ־ מֵאוֹת אֶלֶף רַגְלִי הַ גְּבָרִים לְבַד מִ טָּף ׃ vayis'ú v'né yisra'él mera'msés sukóta k'shésh me'ót élef raglí hagvarím l'vád mitáf And the children of Israel journeyed from Rameses to Succoth, ab
 From Hebrew אלף .
 Retrieved from " https://en.wiktionary.org/w/index.php?title=אלף&oldid=91299625 "
 Hebrew terms inherited from Proto-Semitic 
 Hebrew terms derived from Proto-Semitic 
 Yiddish terms borrowed from Hebrew
```


## [2026-10-17T00:34:44.516Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/Hyékʷr̥|page 563, root Yekwer PIE\" \"https://en.wiktionary.org/wiki/פיל|page 563, root Yb, Hebrew pil\" \"https://en.wiktionary.org/wiki/elephant|page 563, root Yb, English elephant\" \"https://en.wiktionary.org/wiki/gizzard|page 563, root Yekwer, gizzard\"; do python3 tools/fetch_source.py \"${u%%|*}\" --note \"${u#*|}\"; done; cd data/verification/sources/web; tail -4 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['status'],d['bytes'],d['file'])\""
}
```


### [2026-10-17T00:34:46.700Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/470def05a816107a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ac90eb860ccc1058.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b516e5fdf7297354.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/64fdf883c7ea70ec.txt
200 2956 data/verification/sources/web/ac90eb860ccc1058.txt
200 5117 data/verification/sources/web/8ceb2a7077107674.txt
200 37036 data/verification/sources/web/b516e5fdf7297354.txt
200 8486 data/verification/sources/web/64fdf883c7ea70ec.txt
```


## [2026-10-17T00:34:50.557Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -5 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['status'],d['bytes'],d['url'],d['file'])\"; for f in 470def05a816107a ac90eb860ccc1058 8ceb2a7077107674 64fdf883c7ea70ec b516e5fdf7297354; do echo \"== $f\"; grep -i -E 'from |borrow|derived' $f.txt 2>/dev/null| head -6 | cut -c1-500; done"
}
```


### [2026-10-17T00:34:50.984Z] TOOL RESULT

```
200 6739 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/Hyékʷr̥ data/verification/sources/web/470def05a816107a.txt
200 2956 https://en.wiktionary.org/wiki/פיל data/verification/sources/web/ac90eb860ccc1058.txt
200 5117 https://en.wiktionary.org/wiki/iuvencus data/verification/sources/web/8ceb2a7077107674.txt
200 37036 https://en.wiktionary.org/wiki/elephant data/verification/sources/web/b516e5fdf7297354.txt
200 8486 https://en.wiktionary.org/wiki/gizzard data/verification/sources/web/64fdf883c7ea70ec.txt
== 470def05a816107a
 Derived terms 
 From Wiktionary, the free dictionary
 (Redirected from Reconstruction:Proto-Indo-European/Hyékʷr̥ ) 
 From *(H)yekʷ- ( “ liver ” ) +‎ *-r̥ ( r/n-stem suffix ) .
 Derived terms
 ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [2] , 1st edition, Oxford: University Press, →ISBN , pages 13 and 45 
== ac90eb860ccc1058
 From Wiktionary, the free dictionary
 Retrieved from " https://en.wiktionary.org/w/index.php?title=פיל&oldid=83636774 "
== 8ceb2a7077107674
 Derived terms 
 From Wiktionary, the free dictionary
 From Proto-Italic *juwenkos , from Proto-Indo-European *h₂yuHn̥ḱós , equivalent to iuvenis +‎ -cus . De Vaan suggests that Latin -enc- instead of -inc- is explainable either as a Sabellicism or as the result of analogical remodeling after iuvenis or iuventus . [ 1 ] 
 Derived terms
 Retrieved from " https://en.wiktionary.org/w/index.php?title=iuvencus&oldid=91480602 "
 Categories : Latin terms derived from Proto-Indo-European 
== 64fdf883c7ea70ec
 Derived terms 
 From Wiktionary, the free dictionary
 From Middle English gyser , geser , from Old French gesier , giser et al. (French gésier ), from Latin gigēria .
 2016 , Justin O. Schmidt, The Sting of the Wild , Johns Hopkins University Press,, →ISBN , page 29 : As fortune has it, kingbirds, like owls, lack a grinding gizzard and regurgitate hard fragments from their meals. 
 Derived terms
 Latin: ingluviēs   f ( the same word also for the craw or crop ) , gigēria   n   pl [from 2 nd century AD] 
== b516e5fdf7297354
 Derived terms 
 From Wiktionary, the free dictionary
 From Middle English elefant , elefaunt , from Old French elefant , elefan , olifant , re-latinized in Middle French as elephant , from Latin elephantus , from Ancient Greek ἐλέφᾱς ( eléphās ) (gen. ἐλέφαντος ( eléphantos ) ). Believed to be derived from an Afroasiatic form such as Proto-Berber *eḷu ( “ elephant ” ) (compare Tamahaq êlu , Tamasheq alu ) or Egyptian ꜣbw ( “ elephant; ivory ” ) . More at ivory . Replaced Middle English olifant (from the aforementioned Old French form, from Vulgar 
 Derived terms
 Retrieved from " https://en.wiktionary.org/w/index.php?title=elephant&oldid=92768218 "
 Categories : English terms inherited from Middle English
```


## [2026-10-17T00:35:12.490Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in ELEPHANT IVORY ELEMENT GIZZARD HEPATIC; do grep -n \"^$w\" SKT.txt | head -2 | cut -c1-500; done; command ls FSD* WEB*"
}
```


### [2026-10-17T00:35:12.817Z] TOOL RESULT

```
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
WEB_vol1.txt
```


## [2026-10-17T00:35:16.590Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^ *(elephant|ivory|element|gizzard|hepatic)\\b' SKT.txt | head -10 | cut -c1-400; echo ---WEB; grep -n -i -E '^el.e.phant\\b|^el.e.ment\\b|^i.vo.ry\\b|^giz.zard\\b' WEB_vol1.txt | head | cut -c1-200"
}
```


### [2026-10-17T00:35:17.077Z] TOOL RESULT

```
5746:Element.  (F.-U)  O.  F.  c/mmm/.-L. tUmentum,  a  first  principle.
5747:Elephant.  (F.-L.-Gk.-Heb)  M.£. elifaunt.  •  O.  F.  plifant^  eUphamt.  —  L. eU'phanUm,  ace.  of  tUpkai.'mQV.  \kk^m^ an  elephant  — Heb.  aUph,  ileph,  an  01,
8578:Hepatic,  relating  to  ihe  liver. -Gk.)  O.  F.  hepatiqui.^V.  ke^ Gk.  i5»aTi«tJ«,  belonging  to  the  1j ^voTi-,  crude  form  of  ^r>a^,  Ihe  Ii iecur,  'SiVk.  yakxit,  the  liver.  Der. liver-wort,  a  flower.
9392:Ivory.  (F.  -  L.)  M.  E.  iwrU  ( -  ivcne). —  O.  F.  ivuru,  later  ivoire,  —  L.  tbomts, adj.,  made  of  ivory.  — L.  «ivr-,  stem  of  ;^ur, trory.  Perhaps  allied  to  Skt  idha,  an  ele- phant.
---WEB
101501:i/vO-ry black, a fine black pigment prepared from burnt ivory.
101520:i’vo-ry palm (päm), the tree that produces the ivory nut.
101521:I/vo-ry shell, a univalve shell of a species of Eburna.
```


## [2026-10-17T00:35:21.260Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '5747,5750p' SKT.txt | cut -c1-600; grep -n -i 'gizzard' SKT.txt | head -3 | cut -c1-300; grep -n -i -E '^e.?l.?e.?p.?h.?a.?n.?t[ ,(]' WEB_vol1.txt FSD_vol1.txt | head -5 | cut -c1-200; grep -n -i 'eleph' WEB_vol1.txt | grep -i 'heb\\|ox\\b' | head -5 | cut -c1-400"
}
```


### [2026-10-17T00:35:21.717Z] TOOL RESULT

```
Elephant.  (F.-L.-Gk.-Heb)  M.£. elifaunt.  •  O.  F.  plifant^  eUphamt.  —  L. eU'phanUm,  ace.  of  tUpkai.'mQV.  \kk^m^ an  elephant  — Heb.  aUph,  ileph,  an  01,
Elevate ;  see  Iievity.
Eleven.  (£.)  }A.%,  tnleutn.  A.S.  m^> lufon.  +  Du  *//,  Icel.  elliju,  DaJi.  tllet»u Swed.  tlfva,  Goth-  ainliu  G.  tij.  p.  The best  form  is  the  Goth.  ain'tif\  where  ain» one;  and  -/i/- Litbuan.  -lika  (in  vmdiUm, eleven).     Liih.  iika  meao*  '  rcmatning,*
Elf.  (E.)  M.E.  *;/  A.S.  tf//.+Icel.a^. Dan.  Swed.  alf,  G.  4i/.  Der.  elf-in,  adj.. for  eif-en  *.
28987:ý casting ; c : 2. the Castilian form of Spanish, now the 2. [C-] a genus of rodents characterized bi ar SEP apunt coats drn Dalan a i a pee bince to the beaver. SEIO LREN adv. accidentally; f st/ing, n. 1. the act of throwing, as a line in . a hat made of the f thout design; by chance, ' 7 tuit fishing or dice in gambling. a 3 rabbit. ur of the beaver or cap aäl ness, n. secidenttaest h ee 
62822:eVēphănt, 7%. [L. elephantus or elephas, ele- phantis; Gr. Se uae epruno an elephant, ivory; perhaps from Heb. eleph, an ox.) _
103282:h, n. (Heb.] the eleventh letter of the He- ogy, chromatin, the stainable substance of kec¢’kling, n. in nauti ENDE EEN corresponding to English K, k. the cell nucleus: also spelled caryotin. fer Sea pee bee’ materi kā’pok, n. [Malay ka oq.] the silky fibers Käş’bäh, x. the native quarter of Algiers:also kec’klish, a. sick at thee les, al used around the seeds of the tropical silk-cotton sp
108248:lin’dō, x. [Sp., Port., and ; fine, elegant.] a bright cole genus Euphonia. line, n. (ME. lin; AS. lin linum, flax.] y Hoen x . thelong and fine fiber [Obs. in both senses.] oii line, v.l. ; lined, pt., pp.; linin: 5 to cover on the meee prob lite ta ME linen, ioen from line; AS. lin, linen.) over with . to cover on the inside; as i ment with fur; to line a box Site i 2. to put in the insid
```


## [2026-10-17T00:35:29.416Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\ndef leaf(f,line):\n    t=open(f,errors='ignore').read().split('\\n')\n    return '\\n'.join(t[:line-1]).count('\\f')\nprint(leaf('incoming/WLD/WLD_Bd1_pages.txt',18858), leaf('IEC.txt',6378), leaf('HRN.txt',3957), leaf('incoming/ARY/ARY_latin_index_pages.txt',6136))\nE\nsed -n '18850,18862p' incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200; grep -n -i 'jecur\\|iecur\\|jigar\\|yakar' WLD_band3.txt | head -5"
}
```


### [2026-10-17T00:35:29.875Z] TOOL RESULT

```
213 255 116 211


ley!!-      „Leber‘\         rjn- St.    Kom. *icq'i-r{t), gen. *icq'in—es.
     Ai. ydkrt, Gen. yakndh „Leber‘, av. ydkaro ds.                                   = gr. yrtao. -mo; i-n-tos     .




lat. jecur       ,
                   und -inoris ds. iSehwund der Labialisation im Nom. Acc.
                     -oris
sg. vielleiclit auch in Formen wie *jecnis      -inoris Yerquickung des r- und
                                                                      ;
742:MI. Lateiniath Adrés — fopis: 7% hérés 05, 543. ~dre 22°. ira 4, 107. hen 664. int, (100) 135, irrifo, -dre 140. hernia GM. ia, wd 97, hestermus Gi ratutn, -tom, -fud 742 Aibermus 547 Tialia 251. Adem O47 iter, iio 102. Aillag (OM. terum 43, 100 hilum (O76). ifo, -dire 108. hinnus 113. juba, jubar 204. hippie ito, -are 880. wbilim 210. ] . are um 210. Air, tr 605. fides T76. hire O04, jigerum 202 Airews 610 pugo, ere 210 Anm, | Airrio, -ire Fugbsieed 201 hirsitus 610 Fugu 201. hirtus 610. juncus 206 hieco, -ere S40. j yungo, -ere 202. hivpidus 610. indiimentum 109. jinodus 200. ema G63. induo, -ere 10M. jiniperus 208, hontia 583. indusium 109, jini 20M). horefus alat. 859. indiitiag TOS. J | hordeum 611. induvire 109. Suppiter T73 , iri SOL. tafensus 680. jurgo 203 Aornwe }06, safernua 325, jara, -dr horres, -Ere G10. inferws 323, jita »Sateung™ 200. Aertor, -~bri G01. infeatne BO4. jm ,.Brithe” 100 a infrd 323. : hospes O40, TT", rifula 207. juvenia 200). hostia 40, iagena (258"). jure, ire 201. hoslis G40, ingluvigs 62. ; qe 202. | liirvinus O83. mngrup, re (M7, (685 binm, laben 384", miles  Anm, 1). litho, <ire 431° Aunws 662 ing I faber, -iria 432° jaceo, -fre 190. iniiwm 102, idérum: 441". jacio, «ere LO). imope 175. ldjrusca S85", 432°. jon 101. injuam 475*. fturiwm 355". jrnitricds 205, inquittnus 615. lac 66D. dana 104. inguing, -ire 460. lacea 421" Jénus 104. indegue, insece 475". lancer 410° Hea (185, 1918) 4, inacliscere 505 lace 419° imatcuro, -dre GOE*. lacerta 421*. Sot, feds BR. inafigo, -dire 613%. lecertua 421°. ictus 8, inatingwo, -tre G13". fooinia 410". idem (770) imewla 452°. lan, Inceseo 421° jecundauen 205. 1 _ sere 420" lacdnar 35%)*. jecur infer 126, lacus 350°. Segius O07, interduo, -duim S15. igedo, -orn FTO". igitur (8 Anm. 2). inferficin, -ere B27. lovtus (26, 379°. rus G6). tmlerien U7. laceus 37S* i 3 323 {nterocrea 34. lalie, «dre 370* fia 163. infertrigo 729, lima 386%, ile 34, intra, oird 126. lombo, -ere 384". imdgo 102. infro, -dre T33, TS4. limenine 376". imifrilive 1O4*, 110*, infue 137. lomia, laminm 434". inter TST. inulens 3, 108. ismmina 355*. imbractum 282", firmus 3, 1048. line 2M), imitirwe S58. inrilus 475, lances 92". dmiter. «iri 102. siaveap oO. longqueo, -fre TI2*. imminss T33%. lone, -dre (44%) imminis 240*. Sree? F alnd: 20g. limtige 296. impedio, -ire 24* ioreafid alut. 203. lonx 158.
```


## [2026-10-17T00:35:37.119Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -c 'elephas\\|ἐλέφας' POK_full.txt; grep -n -i 'ebur\\b' POK_full.txt | head -3 | cut -c1-200; grep -n -i 'elephas\\|ebur ' WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt | head -3 | cut -c1-200; grep -n -i 'ELEPHANT\\|IVORY\\|ELEMENT' AHD_watkins1985.txt | head -5 | cut -c1-200; grep -n -i 'ebur\\|elephant' IEC.txt | head -3 | cut -c1-200; grep -n -i -E '^(ebur|elementum)' LAT.txt LEW_1910.txt | head | cut -c1-500"
}
```


### [2026-10-17T00:35:37.479Z] TOOL RESULT

```
0
13980:(Vogel-)Bauer, whereof Old High German nahgibur. Old English neahgebur. Modern High 
13982:gebur(e), then bur. Modern High German Bauer^ farmer, peasant '; 
27178:"boar'). Old English eoforru. "boar', mndd. ever. Old High German ebur. Modern High 
101:An important technique of word formation in Indo-European was composition, the com- bining of two separate words or notions into a single word. Such forms were and continue to be built on underlyi
112:The second element of the name of the chief god, *dyeu-pater-, is the general Indo- European word for FATHER, used not in the sense of father as parent, but with the mean- ing of the adult male wh
274:aiw-. Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, 
275:ak-. Sharp. 1. Suffixed form *ak-yd- in: a. Germanic *akjo in Old English ecg, sharp side: EDGE; b. Germanic *akjan in Old Norse eggja, to incite, goad: EGG?. 2. Suf- fixed form *ak-u- in: a. Germ
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old Fr
2470:dromblio- (dromb-) *tread, tramp'. Cf. WP I, 797 & I, 876 MLG & LG trampeln; Li. dramblys ‘elephant’; cf. Sw. trampa, v., and tramp, s. ‘treadle’. (Sole instance of e-gde in Go. -trimpan ‘tread’)
3103:*potbelly; elephant
3110:dhrombhos, ios (dhromb-) ‘hump, lump’. WP I, 734 & 876 Av. cf. dramno (queried: ‘dense’, of a forest); Gk. cf. (variant) thrómbos; MIr. druimm, Ir. druim, gs droma ‘hil’; drom ‘back’; ON dramb ‘a
LAT.txt:18215:ebur, -oris n. : ivoire, objet d'ivoire. - Ancien (Pl.), usuel.
LAT.txt:18506:elementum, -I n.(surtout au pl. elementa, -orum) : i° principes,
LAT.txt:18512:Elementum recouvre dans tous ses eaplois le gr. CTTOixeiov qu'il
LAT.txt:18519:Elementum. Cette siailitude absolue de sens entre crmiyeia et elementa
LAT.txt:18528:elementum, v. en dernier lien V. Vollgraff, Mneaos., 1949, p.89 et s.,
LAT.txt:78657:eburx.h. a., 67.
```


## [2026-10-17T00:35:40.709Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '18215,18225p;18506,18535p' LAT.txt | cut -c1-300; grep -n -i -E '^(elephantus|elephas|gigeria|iecur)' LAT.txt | head; "
}
```


### [2026-10-17T00:35:41.111Z] TOOL RESULT

```
ebur, -oris n. : ivoire, objet d'ivoire. - Ancien (Pl.), usuel.
Iri. eabur.
Adjectifa dlrivds: eburnus; eburneus; eburneolus (cf. corneolus);
eboreus: d' ivoire. La deraier adj. a pass6 dans les langues roaanes339
ecce
o 4 il a pris la place de ebur: fr .ivoire, M.L.3817, d'o 4 angi.ivory,
etc .-, eburatus: orn 4 d'ivoire (d 4 j 4 daas Plaute; cf.owrdtus); eborarius:
ouvrier ea ivoire.
Sbur eat neutre coaae lea noas de aatifere: aurum, argentum, marmor,
lignum , etc. Sa d 4 clinaison eat aana doute calqu 4 e snr celle de robur
et de aaraor. II eat Arident «lue lea Latina ont connu 1 'ivoire avant
elementum, -I n.(surtout au pl. elementa, -orum) : i° principes,
4 l 4 aents; a° connaissances 414 aentaires, rudiaent; 3 0 lettres de l'al-
phabet, alphabet. - Usuel et classique. De IX, ga.ll.elf en " 4 l 4 aent"
bret. e Ivenn "dtincelle".
D 4 riy 4 s: elementarius, elementicius (tous deux d' 4 poq. iap.), coe le-
mentatus (Tert.).
Elementum recouvre dans tous ses eaplois le gr. CTTOixeiov qu'il
traduit, cf. Cic.Acad.i,y,36 illa initia, et ut e Graeco uertam, elementa
(= orot^eTcx) dicuntur. Or crroixe^ov signifie d'abord "rang, rang 4 e,
s 4 rie" (cf. oreC/co, oroixoc), puis rang 4 e de lettres, toc cpto tx^Tct; par
extension, le aot d 4 signe les lettres en taat qu' 414 aents de la syllabe
et du aot, puis d'une aanibre plus g 4 n 4 rale, les 414 aents ou principes
des choses, des Sciences, etc., coaae l'a aontr 4 en d 4 tail Diels,
Elementum. Cette siailitude absolue de sens entre crmiyeia et elementa
a aaen 4 k supposer que elementum serait d 4 riv 4 de IKN, seconde s 4 rie
de 1 'alphabet latin. Mais on voit aal pourquoi le noa de ces lettres
aurait 4 t 4 adopt 4 . L'explication par *elepantum "lettre d'ivoire"
(de eXeqxxc) propos 4 e par Diels (arec une dissiailation d'origine 4 trus-
que coaae dans Melerpanta, de BeXXepoqx>VTr)C?) «at ind 4 aontrable et
peu Traiseablable. La conserration de e devant le (oi l 4 tait y 4 laire)
n'est pas favorable k une origine propreaent latine et d 4 nonce plutot
un eaprunt. Adaptation d'un aot 4 trusque? Sur le sens et 1 'origine de
elementum, v. en dernier lien V. Vollgraff, Mneaos., 1949, p.89 et s.,
qui reprend l' 4 tyaologie de Diels, et donne coaae sens preaier k ele¬
menta celui de "grains de colliers d^yoire".
elemosina (e lee-), -ae f.: auaone. Eaprunt fait parlal.de l' 4 gl.
(Tert. Ital.) au gr. eXer|(ioai)vr]; latinis 4 . D'oA elemosinarius : qui fait
1 'auaone, charitable (tardif). Eoaan. M.L.4839 *alem 6 syna, *alemos(na345
ellychnium
(d'aprfes olo?), v.h.a. aloauoson; iri. almsan-, britt. a lusen.
6954:Elephas est un mot africain.
12125:elephas ( fr.olifant), de adamas, etc.
18536:elephantus, -i (puis elephas, et elephans,-antis) a.: i° 4 l 4 phant j
26170:gigeria (gizeria), -orum n.pl.: entrailles de volaille, g^sier.
29174:Iecur n'a pas pass 4 dans les 1 . romanes ou il a ete remplac^ par
57905:iecur diffluxisse . On a propos^ de lire sacenaris , de sacena.
```


## [2026-10-17T00:35:45.729Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '18225,18232p;18536,18545p;26170,26176p' LAT.txt | cut -c1-300"
}
```


### [2026-10-17T00:35:46.072Z] TOOL RESULT

```
et de aaraor. II eat Arident «lue lea Latina ont connu 1 'ivoire avant
l' 414 phant; auasi ont-ila deux aota pour designer lea deux choaes,
aais elephantus, elephas ae ddnonce coaae un eaprunt rdcent, qu'on
peut dater; v. plua ba8 a.u. Le grec dit eXecpaC pour ddsigner 4 la
fois l' 4 l 4 phant et 1 'ivoire. L'eaploi de elephas, elephantus, au aena
de "ivoire" en latin n'eat qu'une iaitation litt 4 raire de 1'uaage grec
(Vg.G.3,**6; Ae.3,464; 6,895).
tivideaaent eaprunt 4 , coaae eX—ecpaC (dont le preaier 414 aent eat
elephantus, -i (puis elephas, et elephans,-antis) a.: i° 4 l 4 phant j
3°"ivoire", et aussi " 4 l 4 phantiasis"j 3 0 no» d'un poisson de «er on
d'un c 4 tac 4 , et d'un crustac 4 (hoaard?). - Attestd depnis Plaute et
Ennius. Elephantus est sans doute une forae popnlaire b&tie sur le
gdnitif eXeqxxvTOC de gr. eXecpac (cf. abacus). L'eaprnnt a du se faire
pendant la gnerre contre ^rrrhus; les Latina, faute d 1 en connaitre
le no», avaient d'abord reconm ponr ddsigner 1 ' 414 phant X la p 4 ri-
phrase LGca bSs, cf. Varr. L.L.y,39. Le »ot qui d'abord servait uniqueaent
X d 4 signer 1'animal, a eaprunt 4 dans la suite tous les sena du aot
grec. C'est ainsi qu'il a 4 t 4 eaployd concurreaaent ayec ebur (v. ce
gigeria (gizeria), -orum n.pl.: entrailles de volaille, g^sier.
Terne de cnisine attest^ senlement au pluriel, quoique le fr. gdsier
remonte a gigerium, M.L.3760. Les mss. de Nonius, p.119,18, attribuent
X Lucilius une forne gizerini (lire g izerianit), mais le texte est
peu sur, et, serait-il exact, on ne pourrait d 4 cider si la forme
remonte k Lucilius, ou repr^sente une prononciation contenporaine
de Nonius, ou du copiste. Sur gizeriator, v. gingrid.
```


## [2026-10-17T00:35:53.276Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=gizzard\" --note \"page 563, root Yekwer, AHD gizzard etymology\"; python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=elephant\" --note \"page 563, root Yb, AHD elephant etymology\"; python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=ivory\" --note \"page 563, root Yb, AHD ivory etymology\"; cd data/verification/sources/web; tail -3 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['status'],d['bytes'],d['file'])\""
}
```


### [2026-10-17T00:35:54.848Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e7a1e3d0306f710.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6d253c3f435c0c5e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f7277ad3a39d45c.txt
200 4624 data/verification/sources/web/3e7a1e3d0306f710.txt
200 5068 data/verification/sources/web/6d253c3f435c0c5e.txt
200 4794 data/verification/sources/web/8f7277ad3a39d45c.txt
```


## [2026-10-17T00:35:59.306Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 3e7a1e3d0306f710 6d253c3f435c0c5e 8f7277ad3a39d45c; do grep -E '^\\s*\\[|from|Latin' $f.txt | head -5 | cut -c1-600; echo ==; done"
}
```


### [2026-10-17T00:35:59.747Z] TOOL RESULT

```
Exit code 1
 The articles in our blog examine new words, revised definitions, interesting images from the fifth edition, discussions of usage, and more.
 --> See word lists from the best-selling 100 Words Series!
 [Alteration of Middle English giser , from Old French, from Vulgar Latin * gicērium , from Latin gigēria , cooked entrails of poultry, probably of Iranian origin; akin to Persian jigar , liver; see yk w  in the Appendix of Indo-European roots.] 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .
(eval):1: = not found
```


## [2026-10-17T00:36:02.734Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -h '\\[' 6d253c3f435c0c5e.txt 8f7277ad3a39d45c.txt | cut -c1-700"
}
```


### [2026-10-17T00:36:03.041Z] TOOL RESULT

```
 [Middle English ivorie , from Old French ivoire, ivurie , from Latin eboreus , of ivory, from ebur , ebor- , ivory, from Egyptian 3bw , elephant, ivory; see ELEPHANT .] 
 [Middle English elefaunt , from Old French elefant , from Latin elephantus , from Greek eleph ā s , elephant- , ivory, elephant, probably of Afro-Asiatic origin; akin to Tawllemet (Berber language of Mali) el ə w and Mokilko (Chadic language of central Chad) 'êlbi , elephant, and possibly also to Egyptian 3bw , elephant, ivory, and Oromo arba , elephant.]
```


## [2026-10-17T00:36:07.251Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA; awk 'BEGIN{RS=\"\\f\"} NR==229' PLA_pages.txt | grep -n -i -B2 -A6 'fil\\|pil\\|ivory\\|elephant' | head -60"
}
```


### [2026-10-17T00:36:07.568Z] TOOL RESULT

```
8-
9-
10:J>-        fil:        "Elefant" <                 pers. „ pil 2 mp. yo pil,                                    aram.     Lw.   pila 3,
11:       mand.            pila, hebr.               »*».
12:       "ap.        piru          "ivory"          akk.        pllu      borrowings           in       many      Asiatic       langs"    4
13-       "the        word          seems       to    be        of   Iranian         origin"         >
14:       "Whence              in    mod.       pers.           it   is JPpil,         paz.        pil,       representing          an    old
15-       Form,           which          was    borrowed             on    one      hand     into        Sanskrit          and   Armenisch      and
16:       on     the       other          hand       into        Akkadisch           piru,      pilu"         6,
17-
18-
19:a“ - fil?:              "der          Läufer        im Schach".
20-
21- Fr    B           -                                                                       Pd         .
22:obs         - Filfüf:                 "Cypern          Galen'" pers.                    ls        filgü$,         aram.       auge T,
23-
24-
25:Gr           - filzahraf:                    "Lycium,             Saft      u.    Extrakt         v.      Berberitzen"          aus    pers.
26-            un                               8
27:           Eye   filzahre                      .
28-
29-
30:Se - filag:                  "Seidenwurm"                    pers.          ol, pile         9 5.         bäla.
31-
32-
33:als- fila:                  "weibl.          Elefant"             s. fl.
34-
35-ss         - fiman:              "Vertrag"        pers. ol. peymän < mp. wspo patmän < Bati                                                    +
36-       aw.        / ap. may                 "messen" -
37-
38-&= - £iyüf: PL. v.sfiß.
39-
```


## [2026-10-17T00:36:15.869Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\bpil\\b|\\bpīl\\b|pll ' HUB.txt HRN.txt | head -5 | cut -c1-300; grep -n -i 'pil\\b.*Elef\\|Elefant' HUB.txt | head"
}
```


## [2026-10-17T00:36:16.460Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '85,90p' HRN.txt | cut -c1-400"
}
```


### [2026-10-17T00:36:16.820Z] TOOL RESULT

```
sie zu protestiren, was öfter notwendig schien, wenn sich
dieselben in viel benutzten Büchern vorfanden. Die Namen
der Urheber der einzelnen Etymologieen sind nur in wich-
tigeren Fällen und soweit sie neueren Datums sind ge-
nannt*). Eine grosse Anzahl ist längst zum Gemeingut
geworden; es wäre höchst zeitraubend und zum Teil ge-
```


### [2026-10-17T00:36:16.836Z] TOOL RESULT

```
HRN.txt:5923:*) Sputer mit Angleichiing an zhnle Mebondig* zhifle pil go-
HRN.txt:17256:: zandpll 670.
```


## [2026-10-17T00:36:21.968Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==708' BRT.txt | grep -n -E '^ *[0-9]{4} *$|^ *[0-9]{4}  ' | head; awk 'BEGIN{RS=\"\\f\"} NR==708' BRT.txt | grep -n -A3 'yäkar-  n' | cut -c1-300"
}
```


### [2026-10-17T00:36:22.446Z] TOOL RESULT

```
9:•  j.  yäkar-  n.  'Leber':  'kan  F.Jg.
10-Vgl.  ai.  yäirl;  mp,  (Pü.)  jakar,  np.  ßfort). Weiteres  bei  Hau.  AGr.  r.  452.  —  ')  j.  yä- kar) :  np.  jig-at  =  j.  sävar/  (sd.)  :  np.  sA" ;  vgl.
11-I      auch  Bthl.  BB,  //.  125.
12-I  •  j.  "gycS  yagara"  V.  5. 48  RiZ.
```


## [2026-10-17T00:39:22.552Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-563.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nAHDq=\"https://ahdictionary.com/word/search.html?q=\"\nKLN_EL={\"src\":\"KLN\",\"where\":\"KLN_1966 leaf 277 s.v. elephant\",\"stance\":\"supports\",\"note\":\"'The first element of Gk. el-ephas appears also in Hamitic elu, ‘elephant’, whence prob. Pers. p-il, Arab. ph-il, Mishnaic Heb. p-il ... The second element is an Egyptian loan word. Cp. MEgypt. yb, ‘elephant’, whence Yebu (Heb. Yebh), original name of the island Elephantine'\"}\nKLN_IV={\"src\":\"KLN\",\"where\":\"KLN_1966 leaf 444 s.v. ivory\",\"stance\":\"supports\",\"note\":\"'ME. ivorie, fr. OF. ivurie (F. ivoire), fr. L. eboreus, ‘of ivory’, fr. ebur, ‘ivory’, borrowed fr. Egyptian ab, abu, ‘elephant, ivory’, prob. through the medium of the Phoenicians'\"}\nSYN_EL={\"src\":\"SYN\",\"where\":\"§3.77 ELEPHANT (SYN leaf 224)\",\"stance\":\"partial\",\"note\":\"'Grk. elephas, -antos ‘ivory’ (Hom.), ‘elephant’ (Hdt.+) ... the second part, like Lat. ebur, fr. Egypt. ab ‘elephant, ivory’; first part disputed.'\"}\nAHD_EL={\"src\":\"AHD\",\"where\":\"ahdictionary.com s.v. elephant (online 5th ed.)\",\"stance\":\"partial\",\"note\":\"'from Greek elephās, elephant-, ivory, elephant, probably of Afro-Asiatic origin; akin to Tawllemet (Berber) eləw ... and possibly also to Egyptian 3bw, elephant, ivory'\"}\nAHD_IV={\"src\":\"AHD\",\"where\":\"ahdictionary.com s.v. ivory\",\"stance\":\"supports\",\"note\":\"'from Old French ivoire, ivurie, from Latin eboreus, of ivory, from ebur, ebor-, ivory, from Egyptian 3bw, elephant, ivory'\"}\nLAT_EL={\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. elementum (LAT.txt l.18506-18530)\",\"stance\":\"contradicts\",\"note\":\"'L'explication par *elepantum \\\"lettre d'ivoire\\\" (de elephas) proposée par Diels ... est indémontrable et peu vraisemblable' — prefers an Etruscan adaptation or the L-M-N idea as unproven.\"}\nPOK_none={\"src\":\"POK\",\"where\":\"POK_full.txt grep 'elephas', 'ebur'\",\"stance\":\"silent\",\"note\":\"no entry — non-IE (Afroasiatic) loanword.\"}\nWLD_none={\"src\":\"WLD\",\"where\":\"WLD Bd1/Band3 grep 'elephas','ebur '\",\"stance\":\"silent\",\"note\":\"not treated (non-IE).\"}\nPLA214={\"ref\":\"PLA:214\",\"status\":\"partial\",\"note\":\"Asbaghi p.214 (PLA_pages leaf 229) s.v. fīl: 'pers. pīl, mp. pīl, aram. Lw. pīlā, mand. pīlā, hebr. ...; ap. piru \\\"ivory\\\", akk. pīlu \\\"borrowings in many Asiatic langs\\\"; \\\"the word seems to be of Iranian origin\\\"' — links the Persian/Aramaic/OP/Akkadian words but gives no Egyptian source.\"}\nMON_pil={\"src\":\"MON\",\"where\":\"MON_part1.txt l.35526 s.v. پیل\",\"stance\":\"contradicts\",\"note\":\"'پیل: [آشوری، معر. فیل] (ا.) (جان.)' — Mo'in labels the word Assyrian (Akkadian), not Egyptian/Hamitic.\"}\n\ne0nodes=[\n dict(id=1,lang=\"Old Persian\",words=\"piru\",verdict=\"disputed\",\n  derivation=\"OP pīru- 'ivory' is attested once, in Darius's Susa foundation charter (DSf), where ivory is said to come from Kush, India and Arachosia; the related Pirāva 'Nile' may be 'Ivory River'. Kent counts it among OP words 'not traceable to pIE forebears or ... definitely borrowings from outside sources' and compares Elamite piruš and Akkadian pīru/pīlu 'elephant'. The word and its meaning are confirmed. Deriving it from the Egyptian/Hamitic box (yb/ꜣbw, elu) is not supported. Modern sources (Kent, Wiktionary) trace OP pīru- to the Mesopotamian word pīru/pīlu, whose ultimate origin is unknown (Indian and African sources have both been proposed). The r of pīru- matches the Akkadian variant pīru.\",\n  derivation_fa=\"پارسی باستان pīru- «عاج» تنها در کتیبهٔ داریوش در شوش (DSf) آمده است، آنجا که عاج از کوش و هند و رُخَج آورده می‌شود. کنت آن را از واژه‌های بیگانهٔ پارسی باستان می‌شمارد و با ایلامی piruš و اکدی pīru/pīlu «فیل» می‌سنجد. خود واژه و معنایش درست است، ولی پیوند آن با ریشهٔ مصری ꜣbw یا «elu» حامی را پژوهش امروزی نمی‌پذیرد. خاستگاه نهایی واژهٔ میان‌رودانی pīru ناروشن است.\",\n  sources=[W+\"پیل\"],\n  ref_check=[{\"ref\":\"KNT:197\",\"status\":\"partial\",\"note\":\"Kent lexicon s.v. piru- (KNT_full.txt l.27526): 'piru- sb. ‘ivory’ (§75.V, §153.I): Elam. piruš, Akk. pīlu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski ...)'; §75.V: 'borrowings from outside sources; such are piru- ‘ivory’'. Supports word and gloss; no Egyptian origin.\"},PLA214],\n  consulted=[{\"src\":\"KNT\",\"where\":\"Grammar §75.V (KNT_full.txt l.4861-4868)\",\"stance\":\"partial\",\"note\":\"'OP p b f are in some instances not traceable to pIE forebears or are definitely borrowings from outside sources; such are piru- ‘ivory’'\"},\n             {\"src\":\"BRT\",\"where\":\"BRT.txt grep 'pīru|piru'\",\"stance\":\"silent\",\"note\":\"Bartholomae has no entry (word found only in DSf, published after 1904).\"}]),\n dict(id=2,lang=\"Aramaic\",words=\"p-ila, pŭla, pîlâ\",verdict=\"disputed\",\n  derivation=\"Jewish Babylonian Aramaic and Syriac pīlā 'elephant' (Mandaic pīla) are real. The hyphen in 'p-ila' reflects Klein's analysis of the word as a prefixed p- plus Hamitic elu. The other form, 'pŭla', is unclear. It may be a vocalization variant; no source we checked has it. Modern scholarship derives Aramaic pīlā from Akkadian pīlu/pīru 'elephant' (Mo'in's 'آشوری'; Wiktionary; Asbaghi lists 'aram. Lw. pīlā'). The analysis as an Egyptian article p3 'the' + Berber elu mixes two languages and is not accepted today. So the word is real, but the arrow from the Egyptian/Hamitic root is disputed.\",\n  derivation_fa=\"آرامی (یهودی‌بابلی و سریانی) pīlā «فیل» واژه‌ای واقعی است. خط تیرهٔ «p-ila» برگرفته از تحلیل کلاین است که آن را پیشوند p- و «elu» حامی می‌داند. پژوهش امروزی (معین با برچسب «آشوری»، اصبغی، ویکی‌واژه) آرامی pīlā را از اکدی pīlu/pīru می‌داند، نه از مصری. پس واژه درست است، ولی پیوندش با ریشهٔ مصری پذیرفته نیست.\",\n  sources=[W+\"پیل\"],\n  ref_check=[{\"ref\":\"MON:953\",\"status\":\"partial\",\"note\":\"6-vol page not mappable online; the 2-vol Mo'in (MON_part1.txt l.35526) s.v. پیل: '[آشوری، معر. فیل]' — gives a Mesopotamian (Assyrian) origin, no Egyptian link.\"}],\n  consulted=[KLN_EL, {\"src\":\"PLA\",\"where\":\"p.214 s.v. fīl (PLA_pages leaf 229)\",\"stance\":\"partial\",\"note\":\"'aram. Lw. pīlā, mand. pīlā ... akk. pīlu' — Aramaic word confirmed; it is from Akkadian, not from Egyptian.\"}]),\n dict(id=3,lang=\"Persian\",words=\"pîl; pîl-âs\",verdict=\"plausible\",\n  derivation=\"NP pīl 'elephant' < MP pīl (pyl; MacKenzie, Nyberg), also Pāzand pīl. Arabic fīl was borrowed from it (p → f) and came back into Persian as فیل. MP pīl, with l, more likely reflects Aramaic pīlā / Akkadian pīlu than OP pīru-. Mo'in tags it 'آشوری'. So the edge Aramaic → Persian (or a shared Mesopotamian source) is plausible, while the ultimate Egyptian origin of the root box is not supported. pīlasta / pīlās 'ivory' = pīl + asta 'bone' (MP ast, Av. ast-, see root Ost). Mo'in gives 'پیلسته [پیل + استه (= است «استخوان») = پیلاس = پیلس = فیلسته] استخوان فیل، عاج', and BQT has the same analysis. The Ferdowsi verse with پیلان is genuine usage.\",\n  derivation_fa=\"«پیل» از فارسی میانه pīl (پهلوی pyl) است و عربی «فیل» از آن گرفته شده (با ابدال پ به ف) و دوباره به فارسی بازگشته است. لام پایانی نشان می‌دهد که واژه از آرامی pīlā یا اکدی pīlu آمده است، نه از پارسی باستان pīru-، و معین نیز آن را «آشوری» می‌داند. «پیلسته/پیلاس» به معنای «عاج» از «پیل» و «استه/اَست» (استخوان) ساخته شده است، و معین و برهان قاطع همین را می‌گویند. پیوند آرامی ← فارسی پذیرفتنی است، ولی خاستگاه مصری ریشه ثابت نشده است.\",\n  sources=[W+\"پیل\"],\n  ref_check=[PLA214,\n             {\"ref\":\"BQT:446\",\"status\":\"supports\",\"note\":\"BQT vol 1 leaves 672-673 (pp. ~444-446): پیل 'جانوری معروف باشد'; پیلسته '... بمعنی عاج هم بنظر آمده', Mo'in's footnote 'از: پیل + استه (استخوان)'.\"},\n             {\"ref\":\"MON:953\",\"status\":\"supports\",\"note\":\"2-vol Mo'in (MON_part1.txt l.35569-35575): 'پیلسته: [پیل + استه (= است <استخوان>) = پیلاس = پیلس = فیلسته] استخوان فیل، دندان فیل، عاج' — confirms pīlās and its analysis.\"},\n             {\"ref\":\"KLN:507\",\"status\":\"partial\",\"note\":\"KLN_1966 leaf 277 s.v. elephant: 'Hamitic elu, ‘elephant’, whence prob. Pers. p-il' — Klein's (dated) derivation.\"}],\n  consulted=[{\"src\":\"PHD\",\"where\":\"p.~69 (PHD.txt l.549)\",\"stance\":\"supports\",\"note\":\"'pīl [pyl | M pyl, N ~] elephant; (chess) bishop. ~bān elephant-driver.'\"},\n             {\"src\":\"NYB\",\"where\":\"Glossary leaf 177 (NYB_vol2 l.3146)\",\"stance\":\"supports\",\"note\":\"'pīl [pyl] elephant ... pīl-vān elephant-keeper ... NP pīl-bān'\"},\n             MON_pil,\n             {\"src\":\"HRN\",\"where\":\"HRN.txt grep 'pīl|pil'\",\"stance\":\"silent\",\"note\":\"Horn does not treat pīl (non-IE word).\"},\n             {\"src\":\"HUB\",\"where\":\"HUB.txt grep 'pīl|Elefant'\",\"stance\":\"silent\",\"note\":\"not treated.\"},\n             {\"src\":\"BQT\",\"where\":\"vol 1 leaf 673\",\"stance\":\"supports\",\"note\":\"پیلسته footnote 'از: پیل + استه (استخوان)'.\"}]),\n dict(id=4,lang=\"Hebrew\",words=\"el-eph; p-îl; yěbh\",verdict=\"disputed\",\n  derivation=\"Hebrew ʾelef (אלף) exists and means 'thousand' and, in the plural ʾălāfîm, 'cattle, oxen' (Proto-Semitic *ʔalp-). It never means 'elephant'. Its link with Greek elephas is an old guess (Skeat, Webster) that modern sources have dropped. Mishnaic Hebrew pīl 'elephant' is real but is a loan from Aramaic pīlā (see #2). Klein's hyphen 'p-îl' again reflects his p- + elu analysis. Yěbh (Yēḇ) is the Hebrew name of the island Elephantine (Egyptian ꜣbw), not a common noun 'elephant' (Klein: 'Yebu (Heb. Yebh), original name of the island Elephantine'). Biblical Hebrew for ivory is šenhabbîm 'elephant's tooth', whose second part may continue Egyptian ꜣb. So two of the three glosses are wrong and the derivations from the root box are disputed.\",\n  derivation_fa=\"عبری ʾelef (אלף) به معنای «هزار» و در جمع «گاوان، چارپایان» است و هرگز «فیل» معنا نمی‌دهد. پیوند آن با یونانی elephas گمانی کهنه است (اسکیت، وبستر). عبری میشنایی pīl «فیل» واقعی است، ولی از آرامی pīlā وام گرفته شده است. «یِب» (Yēḇ) نام جزیرهٔ الفانتین در مصر است، نه واژه‌ای به معنای «فیل». پس معنای «فیل» برای ʾelef و yěbh نادرست است و این اشتقاق‌ها را پژوهش امروزی رد می‌کند.\",\n  sources=[W+\"אלף\"],\n  ref_check=[{\"ref\":\"KLN:507\",\"status\":\"partial\",\"note\":\"KLN_1966 leaf 277 s.v. elephant: 'Mishnaic Heb. p-il ... Cp. MEgypt. yb, ‘elephant’, whence Yebu (Heb. Yebh), original name of the island Elephantine; cp. also ... Heb. shen-habbim, ‘ivory’' — Klein gives yěbh as a place name, not 'elephant', and does not mention eleph 'ox'.\"}],\n  consulted=[KLN_IV,\n             {\"src\":\"SKT\",\"where\":\"s.v. Elephant (SKT.txt l.5747)\",\"stance\":\"partial\",\"note\":\"'Elephant. (F.-L.-Gk.-Heb.) ... Gk. elephas ... — Heb. aleph, eleph, an ox' — the old ox theory, now abandoned.\"},\n             {\"src\":\"WEB\",\"where\":\"WEB_vol1 l.62822 s.v. elephant\",\"stance\":\"partial\",\"note\":\"'Gr. elephas, an elephant, ivory; perhaps from Heb. eleph, an ox.'\"}]),\n dict(id=5,lang=\"Greek\",words=\"el; elephas\",verdict=\"disputed\",\n  derivation=\"Greek elephas, gen. elephantos, means 'ivory' in Homer and 'elephant' from Herodotus on. Mycenaean has e-re-pa 'ivory'. It is generally held to be an Afroasiatic loan whose second part matches Egyptian ꜣbw 'elephant, ivory' (also the source of Latin ebur). The first part is disputed: it has been compared with Berber *eləw / Tuareg êlu 'elephant' and with Hittite laḫpa- 'ivory'. That part is credible. 'el' glossed 'Indian elephant' is not a Greek word. The book isolates it from Klein's analysis 'el-ephas'; no source gives Greek 'el' or the sense 'Indian elephant'. On the chart's NOTE: Skeat and Webster (WEB) do derive elephas from Hebrew ʾelef 'ox'. Modern references (AHD, Wiktionary, Buck) do not; they prefer Berber eləw + Egyptian ꜣbw, and ʾelef means 'cattle/thousand', not 'elephant'.\",\n  derivation_fa=\"یونانی elephas (اضافی elephantos) در هومر به معنای «عاج» و از هرودوت به بعد به معنای «فیل» است و در یونانی میسنی e-re-pa «عاج» آمده است. بخش دوم آن با مصری ꜣbw «فیل، عاج» یکی دانسته می‌شود و بخش نخست را با بربری *eləw «فیل» می‌سنجند. این تحلیل پذیرفتنی است. اما «el» به معنای «فیل هندی» واژه‌ای یونانی نیست و تنها پاره‌ای از تحلیل کلاین است. نظر وبستر و فانک‌اند‌واگنالز دربارهٔ عبری «eleph: گاو» را پژوهش امروزی کنار گذاشته است.\",\n  sources=[W+\"ἐλέφας\",W+\"elephant\",AHDq+\"elephant\"],\n  ref_check=[{\"ref\":\"AHD:423\",\"status\":\"partial\",\"note\":\"1976 AHD main-dictionary page not online; the current AHD s.v. elephant: 'from Greek elephās ... probably of Afro-Asiatic origin; akin to Tawllemet (Berber) eləw ... and possibly also to Egyptian 3bw' — supports elephas from the Afroasiatic words, gives no Greek 'el'.\"},\n             {\"ref\":\"SYN:189\",\"status\":\"partial\",\"note\":\"Buck §3.77 ELEPHANT (local leaf 224): 'the second part, like Lat. ebur, fr. Egypt. ab ‘elephant, ivory’; first part disputed.'\"}],\n  consulted=[KLN_EL, SYN_EL, POK_none, WLD_none,\n             {\"src\":\"WEB\",\"where\":\"WEB_vol1 l.62822\",\"stance\":\"partial\",\"note\":\"'perhaps from Heb. eleph, an ox' — confirms the NOTE's attribution to WEB.\"}]),\n dict(id=6,lang=\"Latin\",words=\"elephantus\",verdict=\"confirmed\",\n  derivation=\"Latin elephantus (Plautus, Ennius), later also elephas/elephans, was built on the Greek genitive elephantos. Ernout-Meillet date the borrowing to the war against Pyrrhus (280-275 BCE), before which the Romans called the elephant 'Luca bos'. It meant 'elephant' and, imitating Greek, 'ivory'. The book prints the ref as 'KNT:507', evidently a misprint for KLN:507.\",\n  derivation_fa=\"لاتین elephantus (از پلاوتوس و انیوس) از حالت اضافی یونانی elephantos ساخته شده است. ارنو و میه زمان وام‌گیری را جنگ با پیروس (۲۸۰ تا ۲۷۵ پ.م.) می‌دانند. پیش از آن رومیان فیل را «گاو لوکانیا» (Luca bos) می‌نامیدند. ادعای نورایی درست است. ارجاع «KNT:507» در کتاب خطای چاپی به جای KLN:507 است.\",\n  sources=[W+\"elephantus\"],\n  ref_check=[{\"ref\":\"KNT:507\",\"status\":\"not_found\",\"note\":\"Kent's Old Persian ends at p. ~215; printed 'KNT:507' is a misprint for KLN:507 (Klein s.v. elephant: 'fr. L. elephantus, fr. Gk. elephas (gen. -antos)').\"},\n             {\"ref\":\"AHD:423\",\"status\":\"supports\",\"note\":\"current AHD s.v. elephant: 'from Latin elephantus, from Greek elephās, elephant-'.\"}],\n  consulted=[{\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. elephantus (LAT.txt l.18536)\",\"stance\":\"supports\",\"note\":\"'Elephantus est sans doute une forme populaire bâtie sur le génitif elephantos de gr. elephas ... L'emprunt a dû se faire pendant la guerre contre Pyrrhus'\"},\n             KLN_EL]),\n dict(id=7,lang=\"English\",words=\"elephant\",verdict=\"confirmed\",\n  derivation=\"ME olifaunt, elifaunt < OF olifant, elefant (re-Latinized in Middle French as éléphant) < Latin elephantus. The spelling elephant was restored after the Latin in the 14th-16th centuries, replacing olifant.\",\n  derivation_fa=\"انگلیسی elephant از انگلیسی میانه olifaunt/elifaunt، از فرانسوی کهن olifant/elefant، از لاتین elephantus است. املای امروزی در سده‌های ۱۴ تا ۱۶ به پیروی از لاتین بازسازی شد. ادعای نورایی درست است.\",\n  sources=[W+\"elephant\",AHDq+\"elephant\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD s.v. elephant: 'Middle English elefaunt, from Old French elefant, from Latin elephantus'.\"},\n             {\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 277: 'elephant, n. — ME. elifaunt, olifaunt, fr. OF. olifont (F. éléphant), fr. L. elephantus'.\"}],\n  consulted=[KLN_EL,{\"src\":\"SKT\",\"where\":\"SKT.txt l.5747\",\"stance\":\"supports\",\"note\":\"'M.E. elifaunt. — O.F. olifant, elephant. — L. elephantum, acc. of elephas'\"}]),\n dict(id=8,lang=\"Latin\",words=\"elepantum; elementum\",verdict=\"disputed\",\n  derivation=\"Latin elementum 'first principle; letter of the alphabet' is real. It renders Greek stoikheion. '*elepantum' 'ivory letter' is not attested. It is Diels's hypothesis, adopted by Klein ('the most probable') and Vollgraff, that elementum comes from *elepantum (< Greek elephanta) through Etruscan dissimilation. Ernout-Meillet call it 'indémontrable et peu vraisemblable'. Wiktionary calls the origin uncertain and lists the L-M-N idea, a Semitic h-l-ḥ-m source, and a calque modelled on alimentum. So the arrow from elephantus is a minority hypothesis, and the form elepantum should be starred.\",\n  derivation_fa=\"لاتین elementum «اصل نخستین، حرف الفبا» واژه‌ای واقعی و برگردان یونانی stoikheion است. صورت *elepantum «حرف عاجی» در هیچ متنی گواهی نشده است. این فرضیهٔ دیلس است که کلاین آن را «محتمل‌ترین» نظر خوانده، ولی ارنو و میه آن را «اثبات‌ناپذیر و نامحتمل» می‌دانند. ویکی‌واژه خاستگاه را ناروشن می‌داند. پس پیوند elementum با «فیل/عاج» فرضیه‌ای اقلیتی و مورد مناقشه است.\",\n  sources=[W+\"elementum\"],\n  ref_check=[{\"ref\":\"KLN:507\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 276 s.v. element: 'the most probable is that which derives the word elementum fr. *elepantum, ‘ivory letter’, an ancient Latin loan word fr. Gk. elephanta, acc. of elephas ... The change of *elepantum to elementum is prob. due to Etruscan influence.'\"}],\n  consulted=[LAT_EL,{\"src\":\"SKT\",\"where\":\"SKT.txt l.5746\",\"stance\":\"silent\",\"note\":\"'Element. (F.-L.) O.F. element. — L. elementum, a first principle.' — no origin given.\"}]),\n dict(id=9,lang=\"English\",words=\"element\",verdict=\"confirmed\",\n  derivation=\"ME element < OF element < Latin elementum 'first principle, rudiment, letter'. This last edge is secure; only the deeper origin of elementum (see #8) is disputed.\",\n  derivation_fa=\"انگلیسی element از فرانسوی کهن element و از لاتین elementum «اصل نخستین» است. این پیوند قطعی است و تنها خاستگاه دورتر elementum (گره ۸) محل اختلاف است.\",\n  sources=[W+\"elementum\"],\n  ref_check=[{\"ref\":\"KLN:507\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 276: 'element, n. — OF (F. élément), fr. L. elementum, ‘first principle, element’'.\"},\n             {\"ref\":\"AHD\",\"status\":\"not_checked\",\"note\":\"AHD element page not fetched; Klein suffices for this chain.\"}],\n  consulted=[{\"src\":\"SKT\",\"where\":\"SKT.txt l.5746\",\"stance\":\"supports\",\"note\":\"'Element. (F.-L.) O.F. element. — L. elementum'\"},\n             LAT_EL]),\n dict(id=10,lang=\"Latin\",words=\"ebur; eboreus\",verdict=\"confirmed\",\n  derivation=\"Latin ebur, eboris n. 'ivory' (Plautus+) and the adjective eboreus 'of ivory' are real. Ernout-Meillet note that the Romans knew ivory before the elephant, hence two words. ebur is held to be a loan from Egyptian ꜣbw 'elephant, ivory' (Demotic yb), probably through Phoenician traders (Klein, AHD, Wiktionary). It is cognate in the loan sense with the second part of Greek el-ephas.\",\n  derivation_fa=\"لاتین ebur «عاج» و صفت eboreus «عاجی» واژه‌هایی واقعی‌اند. ارنو و میه یادآور می‌شوند که رومیان عاج را پیش از فیل می‌شناختند. ebur را وامی از مصری ꜣbw «فیل، عاج» می‌دانند که احتمالاً بازرگانان فنیقی آن را رساندند. کلاین، فرهنگ امریکن هریتیج و ویکی‌واژه همین را می‌گویند. ادعای نورایی درست است.\",\n  sources=[W+\"ebur\",AHDq+\"ivory\"],\n  ref_check=[{\"ref\":\"KLN:821\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 444 s.v. ivory: 'L. eboreus ... fr. ebur, ‘ivory’, borrowed fr. Egyptian ab, abu, ‘elephant, ivory’, prob. through the medium of the Phoenicians'.\"},\n             {\"ref\":\"AHD:697\",\"status\":\"supports\",\"note\":\"current AHD s.v. ivory: 'Latin eboreus, of ivory, from ebur, ebor-, ivory, from Egyptian 3bw, elephant, ivory'.\"}],\n  consulted=[{\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. ebur (LAT.txt l.18215)\",\"stance\":\"supports\",\"note\":\"'ebur, -oris n.: ivoire ... eboreus: d'ivoire. Le dernier adj. a passé dans les langues romanes ... fr. ivoire, d'où angl. ivory'; 'évidemment emprunté, comme el-ephas'\"},\n             {\"src\":\"SKT\",\"where\":\"SKT.txt l.9392 s.v. Ivory\",\"stance\":\"partial\",\"note\":\"'L. eboreus ... ebur, ivory. Perhaps allied to Skt. ibha, an elephant.'\"},\n             POK_none]),\n dict(id=11,lang=\"Old French\",words=\"ivurie\",verdict=\"confirmed\",\n  derivation=\"Old French (Anglo-Norman) ivurie, yvoire < Latin eboreus 'of ivory' (via Vulgar Latin *eborium). Stressed ŏ > uo/o, intervocalic b > v, and initial e > i. Later French has ivoire.\",\n  derivation_fa=\"فرانسوی کهن ivurie/yvoire از لاتین eboreus «عاجی» آمده است، با تبدیل b میان دو واکه به v و e آغازین به i. فرانسوی امروز آن را ivoire می‌گوید. ادعای نورایی درست است.\",\n  sources=[AHDq+\"ivory\"],\n  ref_check=[{\"ref\":\"KLN:821\",\"status\":\"supports\",\"note\":\"KLN s.v. ivory: 'fr. OF. ivurie (F. ivoire), fr. L. eboreus'.\"}],\n  consulted=[{\"src\":\"SKT\",\"where\":\"SKT.txt l.9392\",\"stance\":\"supports\",\"note\":\"'O.F. ivurie, later ivoire, — L. eboreus'\"},\n             {\"src\":\"LAT\",\"where\":\"LAT.txt l.18218\",\"stance\":\"supports\",\"note\":\"eboreus 'a passé dans les langues romanes ... fr. ivoire'\"}]),\n dict(id=12,lang=\"English\",words=\"ivory\",verdict=\"confirmed\",\n  derivation=\"ME ivorie, yvoire (c.1300) < OF ivurie.\",\n  derivation_fa=\"انگلیسی ivory از انگلیسی میانه ivorie (حدود ۱۳۰۰ م.) و آن از فرانسوی کهن ivurie است. ادعای نورایی درست است.\",\n  sources=[AHDq+\"ivory\"],\n  ref_check=[{\"ref\":\"KLN:821\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 444: 'ivory, n. — ME. ivorie, fr. OF. ivurie'.\"}],\n  consulted=[{\"src\":\"SKT\",\"where\":\"SKT.txt l.9392\",\"stance\":\"supports\",\"note\":\"'Ivory. (F.-L.) M.E. ivorie'\"},AHD_IV]),\n]\n\ne2nodes=[\n dict(id=1,lang=\"Avestan\",words=\"yâkara\",verdict=\"confirmed\",\n  derivation=\"Avestan yākarə n. 'liver' (Vd.) < Proto-Iranian *yákr̥ < PIE *(H)yékʷr̥. Its long ā is a lengthened grade or an Avestan peculiarity; Pokorny marks it 'lengthened grade (?)'. Avestan is a sister of, not the direct ancestor of, Middle Persian. The arrow to Pahlavi stands for the common Old Iranian form, as is usual on the chart.\",\n  derivation_fa=\"اوستایی yākarə «جگر» از ایرانی آغازین *yákr̥ و هندواروپایی *yékʷr̥ است. پوکورنی آن را با درجهٔ بالانده (؟) و آ کشیده می‌آورد. اوستایی نیای مستقیم فارسی میانه نیست و نمایندهٔ صورت ایرانی باستان است. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/Hyékʷr̥\"],\n  ref_check=[{\"ref\":\"POK:504\",\"status\":\"supports\",\"note\":\"POK_full.txt s.v. yekʷ-r̥(t) (Page(s): 504): 'Old Indic yakr̥t, Gen. yaknas ‘liver’; pers. jigar (*yakar-) ... lengthened grade (?) Avestan yākarə'.\"}],\n  consulted=[{\"src\":\"BRT\",\"where\":\"BRT leaf 707 s.v. yākar-\",\"stance\":\"supports\",\"note\":\"'j. yākar- n. ‘Leber’ ... Vgl. ai. yákr̥t; mp. (Pü.) jakar, np. jigar'\"},\n             {\"src\":\"WLD\",\"where\":\"Bd. I p.205 (WLD_Bd1_pages leaf 213)\",\"stance\":\"supports\",\"note\":\"'Ai. yákr̥t, Gen. yaknáh „Leber“, av. yākarə ds. = gr. hēpar ... lat. jecur'\"},\n             {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. yékwr̥ (leaf 110)\",\"stance\":\"partial\",\"note\":\"'yékwr̥. Liver. Greek hēpar ... [Pok. iekʷ-r̥t 504.]' — lists only Greek derivatives.\"},\n             {\"src\":\"IEC\",\"where\":\"s.v. iequor (IEC leaf 255)\",\"stance\":\"supports\",\"note\":\"'iequor ‘liver’. WP I, 205 Skt. yakr̥t ... Per. jigar; Oss. igár ... Gk. hēpar ... Lat. jecur'\"}]),\n dict(id=2,lang=\"Pahlavi\",words=\"jakar, jagar\",verdict=\"confirmed\",\n  derivation=\"MP jagar 'liver', written ykl, also read jakar; Manichaean and Pāzand forms likewise. It comes from Old Iranian *yakar- with initial y- > j-, the regular SW Iranian development seen in jaw < yava- and juft < yuxta-, and k > g after a vowel. Both readings jakar/jagar reflect the ambiguity of Pahlavi k.\",\n  derivation_fa=\"فارسی میانه jagar «جگر» (به خط پهلوی ykl، که jakar هم خوانده می‌شود) از ایرانی باستان *yakar- است. y آغازین طبق قاعده به j بدل شده، چنان‌که در jaw «جو» از yava- و juft «جفت» از yuxta-، و k پس از واکه نرم شده و g شده است. مکنزی و توسی (واژه‌نامهٔ شایست نشایست) آن را تأیید می‌کنند.\",\n  sources=[W+\"جگر\"],\n  ref_check=[{\"ref\":\"SNS:317\",\"status\":\"supports\",\"note\":\"SNS index (SNS.txt l.32447, l.29226): 'jagar 317/6', 'yakar- 317/7'; glossary text (l.17179): '.jagar; ... yakr̥t ... yākarə/yākar-' — p.317 lists jagar with the Avestan/Skt. cognates.\"}],\n  consulted=[{\"src\":\"PHD\",\"where\":\"p.~49 (PHD.txt l.412)\",\"stance\":\"supports\",\"note\":\"'jagar [ykl | N jigar] liver.'\"},\n             {\"src\":\"NYB\",\"where\":\"NYB_vol2 grep 'jagar|jakar|yakar'\",\"stance\":\"silent\",\"note\":\"no entry found in the glossary OCR.\"},\n             {\"src\":\"HRN\",\"where\":\"no. 425, p.95 (HRN leaf 116)\",\"stance\":\"supports\",\"note\":\"'phlv. jakar bezw. yakar (Bund.)'\"}]),\n dict(id=3,lang=\"Persian\",words=\"jegar; jegar-band\",verdict=\"confirmed\",\n  derivation=\"NP jegar/jigar 'liver' < MP jagar < OIr. *yakar-, cognate with Skt. yakr̥t, Greek hēpar and Latin iecur. Its figurative senses are 'courage' and 'dearest one'. jegar-band 'liver, lungs and heart together' (Mo'in: 'مجموع جگر و شش و دل'), then figuratively 'child, darling', is a compound with band 'bond'. The Ferdowsi verse '... ببسته میان را جگربند من' uses it of a son.\",\n  derivation_fa=\"«جگر» از فارسی میانه jagar و ایرانی باستان *yakar- است و با سنسکریت yakr̥t، یونانی hēpar و لاتین iecur هم‌ریشه است. «جگربند» در اصل «مجموع جگر و شش و دل» است و به استعاره «فرزند» معنا می‌دهد. برهان قاطع و معین همین را آورده‌اند و فردوسی آن را برای فرزند به کار برده است. ادعای نورایی درست است.\",\n  sources=[W+\"جگر\"],\n  ref_check=[{\"ref\":\"BQT:579\",\"status\":\"supports\",\"note\":\"BQT vol 2 leaf 37 (p.579): 'جگربند ... مجموع جگر و شش و دل را گویند خواه از انسان باشد و خواه از حیوانات دیگر ... کنایه از فرزند هم هست'.\"},\n             {\"ref\":\"POK:504\",\"status\":\"supports\",\"note\":\"'pers. jigar (*yakar-)'.\"}],\n  consulted=[{\"src\":\"HRN\",\"where\":\"no. 425 'jiger ‘Leber’', p.95\",\"stance\":\"supports\",\"note\":\"'aw. yākar- ‘Leber’; phlv. jakar ...; ai. yákr̥t'\"},\n             {\"src\":\"HUB\",\"where\":\"p.128 (HUB leaf 138, l.4473)\",\"stance\":\"supports\",\"note\":\"'jigar ‘Leber’, zd. yākarə, skr. yakr̥t' (example of y > j).\"},\n             {\"src\":\"MON\",\"where\":\"MON_part1.txt l.48071\",\"stance\":\"supports\",\"note\":\"'جگربند: (امر.) مجموع جگر و شش و دل (در انسان و حیوان). فرزند.'\"},\n             {\"src\":\"ARY\",\"where\":\"pdf page 212 (printed 213), entry جگر\",\"stance\":\"supports\",\"note\":\"latin index: 'HEPAR, HEPATOS (GREEK) ... YAKARE (AVESTAN) ... JECUR, JECORIS (LATIN) ... JAGAR, JIKAR ... IGAR, IGER (OSSETIC) ... JIGAR, DZIGAR ... YAKRT, YAKNAS (SANSKRIT)'\"},\n             {\"src\":\"BQT\",\"where\":\"vol 2 leaf 37\",\"stance\":\"supports\",\"note\":\"جگربند entry as above.\"}]),\n dict(id=4,lang=\"Latin\",words=\"gigeria\",verdict=\"plausible\",\n  derivation=\"Latin gigeria (also gizeria), n. pl., 'cooked entrails of poultry', is a cookery term from the 2nd century CE. AHD calls it 'probably of Iranian origin; akin to Persian jigar, liver', and Wiktionary says 'possibly from Middle Persian'. Klein instead derives it from a Punic/Hebrew word (gizrê 'pieces of sacrificed animals', from g-z-r 'cut'), with gigeria from gizeria by assimilation. Ernout-Meillet give no origin. The Iranian etymology is one of two competing proposals.\",\n  derivation_fa=\"لاتین gigeria (یا gizeria) «دل و جگر پختهٔ مرغ» اصطلاحی آشپزی از سدهٔ دوم میلادی است. فرهنگ امریکن هریتیج آن را «احتمالاً ایرانی، هم‌ریشه با فارسی جگر» می‌داند و ویکی‌واژه نیز وام از فارسی میانه را ممکن می‌شمارد. کلاین آن را از واژه‌ای فنیقی/عبری gizrê «تکه‌های قربانی» (از ریشهٔ g-z-r «بریدن») می‌داند. پس نظر نورایی پذیرفتنی است، ولی قطعی نیست.\",\n  sources=[W+\"gigeria\",AHDq+\"gizzard\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD s.v. gizzard: 'from Latin gigēria, cooked entrails of poultry, probably of Iranian origin; akin to Persian jigar, liver; see yekwr̥ in the Appendix'.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1966 leaf 355 s.v. gizzard\",\"stance\":\"contradicts\",\"note\":\"'fr. L. gizeria, ‘cooked entrails of poultry’, which is prob. a Punic-Phoen.-Heb. loan word. Cp. Heb. gizrē ... ‘pieces of sacrificed animals’ ... In L. gigeria, a collateral form of gizeria, z has been assimilated to the preceding g.'\"},\n             {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. gigeria (LAT.txt l.26170)\",\"stance\":\"silent\",\"note\":\"'gigeria (gizeria): entrailles de volaille, gésier. Terme de cuisine' — no etymology.\"}]),\n dict(id=5,lang=\"English\",words=\"gizzard\",verdict=\"confirmed\",\n  derivation=\"English gizzard < ME giser, gyser < OF gisier, gezier (F. gésier) < Vulgar Latin *gicerium < Latin gigeria. The final -d is excrescent, added from the 16th century.\",\n  derivation_fa=\"انگلیسی gizzard «سنگدان» از انگلیسی میانه giser، از فرانسوی کهن gisier (فرانسوی امروز gésier)، از لاتین gigeria است. d پایانی در سدهٔ شانزدهم افزوده شده است. این پیوند قطعی است.\",\n  sources=[W+\"gizzard\",AHDq+\"gizzard\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference printed on the chart.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"leaf 355\",\"stance\":\"supports\",\"note\":\"'ME. giser, fr. OF. gezier, giser ... (F. gésier), fr. L. gizeria ... The final d in gizzard is ...'\"},\n             {\"src\":\"AHD\",\"where\":\"online s.v. gizzard\",\"stance\":\"supports\",\"note\":\"'Alteration of Middle English giser, from Old French, from Vulgar Latin *gicērium, from Latin gigēria'\"}]),\n dict(id=6,lang=\"Greek\",words=\"heepar\",verdict=\"confirmed\",\n  derivation=\"Greek hēpar, gen. hēpatos (< *-n̥tos), 'liver', written 'heepar' with ee for ē, < PIE *yékʷr̥. Initial *y- > h- (as in hos < *yos), *kʷ > p before e, and the r/n heteroclite stem shows in the genitive hēpatos. Pokorny, WLD, AHD and Mann agree.\",\n  derivation_fa=\"یونانی hēpar (اضافی hēpatos) «جگر» از هندواروپایی *yékʷr̥ است. y آغازین در یونانی به h بدل شده و kʷ پیش از e به p. ستاک دوگانهٔ r/n در حالت اضافی hēpatos پیداست. پوکورنی و دیگران این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/Hyékʷr̥\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 (leaf 110): 'yékwr̥. Liver. Greek hēpar, liver: HEPATIC, HEPATO-; HEPARIN ... [Pok. iekʷ-r̥t 504.]'\"}],\n  consulted=[{\"src\":\"POK\",\"where\":\"p.504\",\"stance\":\"supports\",\"note\":\"'gr. hēpar, -atos (*-n̥-tos)'\"},\n             {\"src\":\"WLD\",\"where\":\"Bd. I p.205\",\"stance\":\"supports\",\"note\":\"'= gr. hēpar, -atos'\"},\n             {\"src\":\"IEC\",\"where\":\"s.v. iequor\",\"stance\":\"supports\",\"note\":\"'Gk. hēpar, gs hēpatos'\"},\n             {\"src\":\"SYN\",\"where\":\"§4.45 LIVER (leaf 288)\",\"stance\":\"supports\",\"note\":\"'Grk. hēpar, gen. -atos; Lat. iecur ... Skt. yakr̥t ... Av. yākarə, NPers. jigar.'\"}]),\n dict(id=7,lang=\"English\",words=\"heparin, hepatic\",verdict=\"confirmed\",\n  derivation=\"hepatic (15th c.) < Latin hepaticus < Greek hēpatikos 'of the liver' < hēpar, hēpat-. heparin was coined in 1918 by W. H. Howell and L. E. Holt from Greek hēpar + chemical suffix -in, because it was first extracted from liver. Klein notes the 'correct' form would be hepatin.\",\n  derivation_fa=\"hepatic از لاتین hepaticus و یونانی hēpatikos «جگری» است. heparin را هاول و هولت در ۱۹۱۸ از یونانی hēpar و پسوند شیمیایی -in ساختند، زیرا نخست از جگر به دست آمد. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/Hyékʷr̥\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference printed on the chart.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"leaf 388 s.v. heparin, hepatic\",\"stance\":\"supports\",\"note\":\"heparin: 'Coined by ... William Henry Howell ... and Luther Emmett Holt Jr. (1918), fr. Gk. hēpar (gen. hēpatos) ... and chem. suff. -in'; hepatic: 'Gk. hēpatikos, fr. hēpar, gen. hēpatos, ‘liver’, fr. I.-E. base *yēqʷ-r(t)'\"},\n             {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. yékwr̥\",\"stance\":\"supports\",\"note\":\"lists HEPATIC, HEPARIN.\"},\n             {\"src\":\"SKT\",\"where\":\"SKT.txt l.8578 s.v. Hepatic\",\"stance\":\"supports\",\"note\":\"'Hepatic ... (L.-Gk.) ... Gk. hēpatikos ... Gk. hēpar, the liver'\"}]),\n dict(id=8,lang=\"Latin\",words=\"jecur\",verdict=\"confirmed\",\n  derivation=\"Latin iecur (jecur), gen. iecoris / iecinoris, 'liver' < PIE *yékʷr̥, *yekʷn-. The two genitives continue the r/n heteroclite. Initial *y- is kept in Latin, and *kʷ > c before the following consonant/vowel by delabialization. It was replaced in Romance by ficatum 'fig-fed liver' (It. fegato, F. foie).\",\n  derivation_fa=\"لاتین iecur (اضافی iecoris/iecinoris) «جگر» از هندواروپایی *yékʷr̥ است. دو صورت اضافی آن بازماندهٔ ستاک دوگانهٔ r/n است. در زبان‌های رومی، ficatum «جگرِ پروارشده با انجیر» جای آن را گرفت. ادعای نورایی درست است.\",\n  sources=[W+\"Reconstruction:Proto-Indo-European/Hyékʷr̥\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 yékwr̥ lists only Greek derivatives; Latin jecur not in the 1985 text (JECORAL not listed).\"}],\n  consulted=[{\"src\":\"POK\",\"where\":\"p.504\",\"stance\":\"supports\",\"note\":\"'Lat. jecur, -oris and -inoris (proves previously *jecinis, amalgamation of r- and n-stems)'\"},\n             {\"src\":\"WLD\",\"where\":\"Bd. I p.205\",\"stance\":\"supports\",\"note\":\"'lat. jecur, -oris und -inoris ds.'\"},\n             {\"src\":\"IEC\",\"where\":\"s.v. iequor\",\"stance\":\"supports\",\"note\":\"'Lat. jecur, gs jecoris & jecinoris'\"}]),\n dict(id=9,lang=\"English\",words=\"jecoral\",verdict=\"confirmed\",\n  derivation=\"English jecoral 'pertaining to the liver', a rare anatomical adjective, is formed with the suffix -al on Latin iecur, gen. iecoris.\",\n  derivation_fa=\"انگلیسی jecoral «مربوط به جگر» صفتی نادر در کالبدشناسی است که با پسوند -al از لاتین iecur (اضافی iecoris) ساخته شده است. ادعای نورایی درست است.\",\n  sources=[W+\"jecoral\"],\n  ref_check=[{\"ref\":\"KLN:827\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 446: 'jecoral, adj., pertaining to the liver (anat.) — Formed with adj. suff. -al fr. L. jecur, gen. jecoris, ‘liver’, which is cogn. with OI. yakr̥t, Gk. hēpar'.\"}],\n  consulted=[{\"src\":\"KLN\",\"where\":\"leaf 446\",\"stance\":\"supports\",\"note\":\"as above.\"},\n             {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'jecoral'\",\"stance\":\"silent\",\"note\":\"not in Skeat.\"}]),\n]\n\nout={\"pdf_page\":563,\"book_page\":533,\"verified_by\":\"claude-opus-5-5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Yb, Âbu, Elu, Elu-ephas\",\"verdict\":\"plausible\",\n  \"modern_form\":\"Egyptian ꜣbw (Demotic yb) 'elephant, ivory'; Berber *eləw / Tuareg êlu 'elephant'\",\n  \"note\":\"Egyptian ꜣbw 'elephant, ivory' (also the name of Elephantine, Heb. Yēḇ) is real and is the accepted source of Latin ebur and the second part of Greek elephas. 'Elu' is Berber (Tuareg êlu, Tawllemet eləw), not Egyptian; Klein calls it 'Hamitic' and the box note says so. 'Elu-ephas' is not an attested form anywhere; it is Nourai's hybrid reconstruction of Greek el-ephas. The Semitic/Iranian pīl/pīru group under this root is traced today to Akkadian pīru/pīlu, not to Egyptian or Berber (Klein's 'p-il' analysis is dated). Printed ref 'KNT:507' on the Latin elephantus box is a misprint for KLN:507. The extraction matches the printed page.\",\n  \"note_fa\":\"مصری ꜣbw «فیل، عاج» (نام جزیرهٔ الفانتین نیز از آن است) واقعی است و خاستگاه پذیرفتهٔ لاتین ebur و بخش دوم یونانی elephas به شمار می‌رود. «elu» واژه‌ای بربری (حامی) است، نه مصری، و «Elu-ephas» در هیچ زبانی گواهی نشده و ساختهٔ خود نورایی از تحلیل el-ephas است. گروه پیل/پیرو/پیلا امروز به اکدی pīru/pīlu بازگردانده می‌شود، نه به مصری. پس ریشهٔ کلی با احتیاط پذیرفتنی است، ولی بخشی از شاخه‌ها نادرست‌اند.\",\n  \"sources\":[W+\"ἐλέφας\",W+\"ebur\",W+\"elephant\",AHDq+\"elephant\",AHDq+\"ivory\"],\n  \"ref_check\":[{\"ref\":\"KLN:507\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 277 s.v. elephant: 'Hamitic elu, ‘elephant’ ... The second element is an Egyptian loan word. Cp. MEgypt. yb, ‘elephant’'.\"},\n               {\"ref\":\"KLN:821\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 444 s.v. ivory: 'borrowed fr. Egyptian ab, abu, ‘elephant, ivory’'.\"},\n               {\"ref\":\"AHD:423\",\"status\":\"partial\",\"note\":\"current AHD s.v. elephant: 'probably of Afro-Asiatic origin; akin to Tawllemet (Berber) eləw ... and possibly also to Egyptian 3bw' (1976 page itself not online).\"}],\n  \"consulted\":[SYN_EL, AHD_EL, POK_none],\n  \"nodes\":e0nodes},\n {\"entry\":2,\"root\":\"Yekwer\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *(H)yékʷr̥, gen. *(H)yekʷn̥-és 'liver'\",\n  \"note\":\"Pokorny 504 iekʷ-r̥(t); AHD yékwr̥; WP I 205. Root, language label and gloss correct. Only Latin gigeria (→ gizzard) is uncertain: AHD and Wiktionary allow an Iranian source (Persian jigar), Klein prefers a Punic/Hebrew one.\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *yékʷr̥ «جگر» (پوکورنی ۵۰۴) درست است. سنسکریت yakr̥t، اوستایی yākarə، فارسی میانه jagar، فارسی «جگر»، یونانی hēpar و لاتین iecur همه از آن‌اند. تنها وام بودن لاتین gigeria از فارسی جگر قطعی نیست و کلاین خاستگاهی سامی برای آن پیشنهاد می‌کند.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/Hyékʷr̥\"],\n  \"ref_check\":[{\"ref\":\"POK:504\",\"status\":\"supports\",\"note\":\"POK_full.txt (Page(s): 504): 'Meaning: liver ... Old Indic yakr̥t ... pers. jigar (*yakar-) ... Avestan yākarə ... gr. hēpar ... Lat. jecur'.\"}],\n  \"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I p.205\",\"stance\":\"supports\",\"note\":\"'„Leber“ ... Ai. yákr̥t ... av. yākarə ... gr. hēpar ... lat. jecur'\"},\n               {\"src\":\"AHD\",\"where\":\"Watkins 1985 leaf 110\",\"stance\":\"supports\",\"note\":\"'yékwr̥. Liver.'\"},\n               {\"src\":\"IEC\",\"where\":\"leaf 255\",\"stance\":\"supports\",\"note\":\"'iequor ‘liver’. WP I, 205'\"},\n               {\"src\":\"SYN\",\"where\":\"§4.45\",\"stance\":\"supports\",\"note\":\"inherited group yakr̥t / hēpar / iecur / yākarə / jigar.\"}],\n  \"nodes\":e2nodes}]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-563.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-563.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-563.json >/dev/null && python3 tools/verify_check.py 563"
}
```


### [2026-10-17T00:39:23.221Z] TOOL RESULT

```
nodes verified: 21/21
node verdicts: {'disputed': 5, 'plausible': 2, 'confirmed': 14}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 9, 'supports': 18, 'not_found': 1, 'not_checked': 3}
books consulted: {'partial': 8, 'silent': 10, 'supports': 39, 'contradicts': 4} | by book: {'KLN': 9, 'SKT': 9, 'LAT': 6, 'POK': 4, 'WLD': 4, 'AHD': 4, 'HRN': 3, 'IEC': 3, 'BRT': 2, 'PHD': 2, 'NYB': 2, 'MON': 2, 'HUB': 2, 'BQT': 2, 'WEB': 2, 'SYN': 2, 'KNT': 1, 'PLA': 1, 'ARY': 1}
```


## [2026-10-17T00:39:34.325Z] TOOL CALL #57: SubagentHandback

```json
{
 "message": "I wrote the verification for page 563 (book page 533) to /home/sfmqrb/git/rishe-private/data/verification/page-563.json. `verify_check.py 563` shows all 21 nodes verified and 0 PROBLEM lines.\n\n**Verdicts:**\n- **Roots:** Yb/Âbu (entry 0) is plausible; Yekwer (entry 2) is confirmed.\n- **Nodes:** 14 confirmed, 2 plausible, 5 disputed, 0 transcription_suspect.\n\n**Disputed (all in entry 0, Yb/Âbu/Elu):**\n- **#1 Old Persian piru 'ivory':** the word is real, but Kent and modern sources trace it to Akkadian pīru/pīlu, not to Egyptian ꜣbw or Berber elu.\n- **#2 Aramaic p-ila/pīlā:** this is a loan from Akkadian pīlu. Klein's reading of it as a p- prefix plus Hamitic elu is dated.\n- **#4 Hebrew el-eph / p-îl / yěbh:** ʾelef means 'thousand; cattle', never 'elephant'. Mishnaic pīl is from Aramaic. Yēḇ is the Hebrew name of the island Elephantine, not a word for 'elephant'.\n- **#5 Greek el / elephas:** 'el' glossed 'Indian elephant' is not a Greek word; it is Nourai's fragment of Klein's analysis 'el-ephas'. Elephas itself as an Afroasiatic loan is fine. The chart's NOTE (WEB & FSD: from Hebrew 'eleph: ox') is accurate for WEB and Skeat, but modern scholarship has dropped that idea.\n- **#8 Latin elepantum → elementum:** *elepantum ('ivory letter') is Diels's unattested reconstruction. Klein favours it, but Ernout-Meillet call it \"indémontrable et peu vraisemblable\".\n\n**Plausible:**\n- **#3 Persian pīl / pīlās:** the Aramaic → Persian link is fine. pīlasta/pīlās = pīl + asta 'bone' is confirmed by Mo'in and the Borhan-e Qate' (BQT).\n- **Entry 2 #4 Latin gigeria:** AHD says \"probably of Iranian origin; akin to Persian jigar\", but Klein derives it from Punic/Hebrew.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Book misprint:** the ref on the Latin elephantus box (entry 0 #6) is printed \"KNT:507\" but should be KLN:507. It is recorded as `not_found` in that node's `ref_check`.\n\nEtymonline returned HTTP 403 for every page I tried, so it is not cited."
}
```


### [2026-10-17T00:39:34.611Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
