# Verification process log — verify-page-541


## [2026-10-17T00:00:15.249Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 541 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-541.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-541.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-541.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 541` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.302Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.343Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.448Z] TOOL RESULT

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


## [2026-10-17T00:00:18.849Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-541.txt"
}
```


### [2026-10-17T00:00:18.868Z] TOOL RESULT

```
1	=== PDF page 541 (book page 511) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wel 2 : to tear, pull, wound  (refs POK:1144)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:1179 | Wlp, Ulp, Lup : wolf, dog
5	  #2 (parent #1) [Avestan] refs=POK:1179 | urpa, urupis, lupis, raopias : dog ; taxma-urupa : (with) strong dogs ☞Tenk
6	    #3 (parent #2) [Persian] refs=BQT:968; MON5:405 | gorbeh «گربه (روباه)» : an animal that tears up ; Tahmŭres «تهمورث (طهمورث)» : (with) strong dogs
7	  #4 (parent #1) [Old High German] refs=KLN:27 | athal-wolf : noble wolf (Adolph) ☞Âtos
8	    #5 (parent #4) [English] refs=KLN; AHD | Adolph
9	--- entry 1 ---
10	ROOT [Indo-European] Wel 3 : to turn, roll  (refs POK:1140)
11	#1 (parent #0) [Avestan] refs=POK:1140 | var 3 : turn, time (as in one tine) ; varemi, varamiš : wave ; varanavaity : covered
12	  #2 (parent #1) [Persian] refs=POK:1140; SNS:98; MON:511; SOD:411 | bâr 2 «بار ۲ (چند بار)» : time (as in two times), it also refers to time of admission as in the following words: ; darbâr «دربار ( بارعام ، بارخدا )» : court ; barm «بَرم» : pool, pond, wave
13	#3 (parent #0) [Avestan] refs=POK:1140 | -var 4 : similar to, like ; var 5 : ceremony
14	  #4 (parent #3) [Pahlavi] refs=HRN:241; BQT:2373 | varišn : conduct, way of living
15	    #5 (parent #4) [Persian] refs=BQT:1137 | vâr 2 «-وار ۲» : like ; ham-vâr «هموار» : like each other, even ☞Sem 1 ; vâr 3 «وار ۳» : a custom or ceremony | extra: شلوار ، سزاوار ، شاهوار ، دیوانه وار
16	#6 (parent #0) [Germanic] refs=AHD | wel : willow tree (bending branches) ; welk : walk ; wall : rolling water, a cavity, wallet
17	  #7 (parent #6) [English] refs=None | willow ; walk ; well 2 : water well ; wallet
18	#8 (parent #0) [Latin] refs=AHD | volvere : to roll, make cavity ; vallĕs : valley
19	  #9 (parent #8) [English] refs=None | revolve, involve, evolution, valve, vault, volume, valley
20	#10 (parent #0) [Greek] refs=AHD | hel-ix
21	  #11 (parent #10) [English] refs=None | helix
22	
```


## [2026-10-17T00:00:19.318Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-541.json"
}
```


### [2026-10-17T00:00:19.532Z] TOOL RESULT

```
1	{
2	  "pdf_page": 541,
3	  "book_page": 511,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wel 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1144",
10	        "gloss": "to tear, pull, wound"
11	      },
12	      "part": 2,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Indo-European",
18	          "refs": "POK:1179",
19	          "words": [
20	            {"translit": "Wlp, Ulp, Lup", "gloss": "wolf, dog", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Avestan",
29	          "refs": "POK:1179",
30	          "words": [
31	            {"translit": "urpa, urupis, lupis, raopias", "gloss": "dog", "script": null},
32	            {"translit": "taxma-urupa", "gloss": "(with) strong dogs", "script": null, "see": ["Tenk"]}
33	          ],
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Persian",
41	          "refs": "BQT:968; MON5:405",
42	          "words": [
43	            {"translit": "gorbeh", "gloss": "an animal that tears up", "script": "گربه (روباه)"},
44	            {"translit": "Tahmŭres", "gloss": "(with) strong dogs", "script": "تهمورث (طهمورث)"}
45	          ],
46	          "note": null,
47	          "quote": {"text": "پسر بد مر او را یکی هوشمند - گرانمایه طهمورث هوشمند", "poet": "Ferdowsî"}
48	        },
49	        {
50	          "id": 4,
51	          "parent": 1,
52	          "lang": "Old High German",
53	          "refs": "KLN:27",
54	          "words": [
55	            {"translit": "athal-wolf", "gloss": "noble wolf (Adolph)", "script": null, "see": ["Âtos"]}
56	          ],
57	          "note": null,
58	          "quote": null
59	        },
60	        {
61	          "id": 5,
62	          "parent": 4,
63	          "lang": "English",
64	          "refs": "KLN; AHD",
65	          "words": [
66	            {"translit": "Adolph", "gloss": null, "script": null}
67	          ],
68	          "note": null,
69	          "quote": null
70	        }
71	      ]
72	    },
73	    {
74	      "root": {
75	        "name": "Wel 3",
76	        "lang": "Indo-European",
77	        "refs": "POK:1140",
78	        "gloss": "to turn, roll"
79	      },
80	      "nodes": [
81	        {
82	          "id": 1,
83	          "parent": 0,
84	          "lang": "Avestan",
85	          "refs": "POK:1140",
86	          "words": [
87	            {"translit": "var 3", "gloss": "turn, time (as in one tine)", "script": null},
88	            {"translit": "varemi, varamiš", "gloss": "wave", "script": null},
89	            {"translit": "varanavaity", "gloss": "covered", "script": null}
90	          ],
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 2,
96	          "parent": 1,
97	          "lang": "Persian",
98	          "refs": "POK:1140; SNS:98; MON:511; SOD:411",
99	          "words": [
100	            {"translit": "bâr 2", "gloss": "time (as in two times), it also refers to time of admission as in the following words:", "script": "بار ۲ (چند بار)"},
101	            {"translit": "darbâr", "gloss": "court", "script": "دربار ( بارعام ، بارخدا )"},
102	            {"translit": "barm", "gloss": "pool, pond, wave", "script": "بَرم"}
103	          ],
104	          "note": null,
105	          "quote": {"text": "عنان را بپیچید بر دست راست - بزد باردیگر بران سو که خواست", "poet": "Ferdowsî"}
106	        },
107	        {
108	          "id": 3,
109	          "parent": 0,
110	          "lang": "Avestan",
111	          "refs": "POK:1140",
112	          "words": [
113	            {"translit": "-var 4", "gloss": "similar to, like", "script": null},
114	            {"translit": "var 5", "gloss": "ceremony", "script": null}
115	          ],
116	          "note": null,
117	          "quote": null
118	        },
119	        {
120	          "id": 4,
121	          "parent": 3,
122	          "lang": "Pahlavi",
123	          "refs": "HRN:241; BQT:2373",
124	          "words": [
125	            {"translit": "varišn", "gloss": "conduct, way of living", "script": null}
126	          ],
127	          "note": null,
128	          "quote": null
129	        },
130	        {
131	          "id": 5,
132	          "parent": 4,
133	          "lang": "Persian",
134	          "refs": "BQT:1137",
135	          "words": [
136	            {"translit": "vâr 2", "gloss": "like", "script": "-وار ۲"},
137	            {"translit": "ham-vâr", "gloss": "like each other, even", "script": "هموار", "see": ["Sem 1"]},
138	            {"translit": "vâr 3", "gloss": "a custom or ceremony", "script": "وار ۳"}
139	          ],
140	          "script_extra": "شلوار ، سزاوار ، شاهوار ، دیوانه وار",
141	          "note": null,
142	          "quote": {"text": "وارآذر گذشت و شعلهٔ آن - شعلهٔ لاله را زمان آمد", "poet": "Rŭdakî"}
143	        },
144	        {
145	          "id": 6,
146	          "parent": 0,
147	          "lang": "Germanic",
148	          "refs": "AHD",
149	          "words": [
150	            {"translit": "wel", "gloss": "willow tree (bending branches)", "script": null},
151	            {"translit": "welk", "gloss": "walk", "script": null},
152	            {"translit": "wall", "gloss": "rolling water, a cavity, wallet", "script": null}
153	          ],
154	          "note": null,
155	          "quote": null
156	        },
157	        {
158	          "id": 7,
159	          "parent": 6,
160	          "lang": "English",
161	          "refs": null,
162	          "words": [
163	            {"translit": "willow", "gloss": null, "script": null},
164	            {"translit": "walk", "gloss": null, "script": null},
165	            {"translit": "well 2", "gloss": "water well", "script": null},
166	            {"translit": "wallet", "gloss": null, "script": null}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 8,
173	          "parent": 0,
174	          "lang": "Latin",
175	          "refs": "AHD",
176	          "words": [
177	            {"translit": "volvere", "gloss": "to roll, make cavity", "script": null},
178	            {"translit": "vallĕs", "gloss": "valley", "script": null}
179	          ],
180	          "note": null,
181	          "quote": null
182	        },
183	        {
184	          "id": 9,
185	          "parent": 8,
186	          "lang": "English",
187	          "refs": null,
188	          "words": [
189	            {"translit": "revolve, involve, evolution, valve, vault, volume, valley", "gloss": null, "script": null}
190	          ],
191	          "note": null,
192	          "quote": null
193	        },
194	        {
195	          "id": 10,
196	          "parent": 0,
197	          "lang": "Greek",
198	          "refs": "AHD",
199	          "words": [
200	            {"translit": "hel-ix", "gloss": null, "script": null}
201	          ],
202	          "note": null,
203	          "quote": null
204	        },
205	        {
206	          "id": 11,
207	          "parent": 10,
208	          "lang": "English",
209	          "refs": null,
210	          "words": [
211	            {"translit": "helix", "gloss": null, "script": null}
212	          ],
213	          "note": null,
214	          "quote": null
215	        }
216	      ]
217	    }
218	  ]
219	}
220	
```


## [2026-10-17T00:00:25.325Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; command ls data/verification/sources/refs/ | head -100; sed -n 1,200p tools/verify_check.py | head -150"
}
```


### [2026-10-17T00:00:25.654Z] TOOL RESULT

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


## [2026-10-17T00:00:29.629Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-53*.json page-54*.json 2>/dev/null; cat agent/charts/page-540.txt 2>/dev/null | head -30; python3 -c \"\nimport json;d=json.load(open('page-538.json'));e=d['entries'][0];print(json.dumps(e,ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-17T00:00:30.276Z] TOOL RESULT

```
page-530.json
page-531.json
page-532.json
page-533.json
page-534.json
page-535.json
page-536.json
page-537.json
page-538.json
page-53.json
page-54.json
=== PDF page 540 (book page 510) ===
--- entry 0 ---
ROOT [Indo-European] Wel 2 : to tear, pull, wound  (refs POK:1144)  PART 1
#1 (parent #0) [Sanskrit] refs=BQT:2253 | vrana : wound
  #2 (parent #1) [Persian] refs=MON:4966; POK:1145 | vâlâneh, valâneh «والانه ، ولانه» : wound
#3 (parent #0) [Latin] refs=AHD | vulmus : wound ; vellere : to tear
  #4 (parent #3) [English] refs=None | vulnerable ; vulture
--- entry 1 ---
ROOT [Indo-European] Welâ, Wlnâ, Wolko : plucked off (wool)  (refs POK:1139)
#1 (parent #0) [Avestan] refs=POK:1139 | varesa : hair
  #2 (parent #1) [Pahlavi] refs=HRN:202 | vars : curly hair
    #3 (parent #2) [Persian] refs=MON:5004; SNS:285; BQT:1794; KLN:856 | vares «وَرس (وریس)» : a string used in Zoroastrian ceremonies ; gors 2 «گُرس ۲» : curly hair
#4 (parent #0) [Sogdian] refs=SOD:412 | wrs : hair
#5 (parent #0) [Germanic] refs=AHD | wullâ : wool
  #6 (parent #5) [English] refs=None | wool
#7 (parent #0) [Latin] refs=AHD | villus : shaggy hair
  #8 (parent #7) [English] refs=None | velvet
--- entry 2 ---
ROOT [Indo-European] Wlkwo : tearing animals, wolf  (refs KLN:1750)
#1 (parent #0) [Avestan] refs=KLN:1750; SOD:423 | vherka, vehrka : wolf
  #2 (parent #1) [Pahlavi] refs=HRN:202 | gurg
    #3 (parent #2) [Persian] refs=BQT:1797 | gorg «گرگ» : wolf
#4 (parent #0) [Old Persian] refs=KNT:206 | varkana : wolf land
  #5 (parent #4) [Pahlavi] refs=KNT:206 | gorgân
    #6 (parent #5) [Persian] refs=KNT:206 | Gorgân «گرگان» : a district S.E. of the Caspian sea
#7 (parent #0) [Sogdian] refs=SOD:423 | wyrk : wolf
#8 (parent #0) [Germanic] refs=AHD | wulfaz : wolf
  #9 (parent #8) [English] refs=None | wolf
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
   "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.",
   "derivation_fa": "در اوستایی فعل vac- / vaoc
```


## [2026-10-17T00:01:02.370Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Page(s) 114[0-5]\\|Page(s) 117[89]\\|Page(s) 1178-1179\" POK_full.txt | head; grep -n \"Root / lemma: u̯el-\\|Root / lemma: uel-\\|Root / lemma: u̯ḷkʷos\\|Root / lemma: u̯ḷk\\|lemma: ulkuos\\|Root / lemma: uḷ\" POK_full.txt | head -30"
}
```


### [2026-10-17T00:01:02.914Z] TOOL RESULT

```
90239:Root / lemma: uel-1 
90264:Root / lemma: uel-2, ulei-, ule(i)- 
90323:Root / lemma: uel-3 
90432:Root / lemma: uel-5, uela- 
90462:Root / lemma: uel-7, uela-, ule-
```


## [2026-10-17T00:01:06.642Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90239,90500p POK_full.txt | cut -c1-600"
}
```


### [2026-10-17T00:01:07.034Z] TOOL RESULT

```
Root / lemma: uel-1 
Meaning: to see 

Material: Latin voltus, vultus, -usm. "Gesichtsausdruck, Miene, appearance, shape' {*vj-tu- 
) stellt sich to Irish fiTes gives', older Imper. *^e/e (compare French voicK), cymr. gweled 
"see', bret. guelet^\a vue'. Old Irish f/7/{Gen. filed, pre-lrish Ogam VELITAS) " seer, bard' 
{*uelets)\ the name the Germanic Seherin Veleda; in Germanic seems eine probably from 
*uel- abgeleitete root *uleid- {*ul-ei-d-): Gothic anda-wleiznu. (?) " front ', Old Icelandic ITta, 
Old English w/rtan'see, see, show'; zero grade Gothic m////s" front, shape'. Old Icelandic 
////-(Akk. PI. //tu) " appearance, paint, color'. Old Saxon i^////" radiance, appearance, 
shape'. Old Frisian iy//fe" front, appearance ', Old English wlite6s., also " radiance ', wlitu 
f. "form, kind of; ograde das causative Gothic wlaiton. Old Icelandic leita {*wlaitdn) "sich 



umsehen after, seek ' (wherefore as post-verbal leiti. "das Suchen', Wissmann Norn. 
Postverb. 1, 11), Old English wlatian6s.; 

also Germanic *wull=>u-xx\. "glory, magnificence' ("*prestige'): Gothic wu/Pus'g\orY, 
magnificence'. Old Icelandic Ullr{*wult^uz) " god's name ', Old English n/i/Zcyo/'" gloria', 
compare Gothic wult^rs^ value, worth ', M/i//fc'/7za"herrlicher'; further wult^ags ^ zybo^oc^ . 

References: WP. I 293, WH. II 831. 
Page(s): 1136-1137 

Root / lemma: uel-2, ulei-, ule(i)- 
Meaning: to wish; to choose 

Material: A. Old Indie unthemat. 3. Sg. Med. Aor. avrta. Opt. vunta, participle urana-, 
vrnTte, vrnnati, vrnoti, vrnute^ choose, vorziehen, love', vrta- "gewahit, desirable, worth 
having, welcome, wanted ', vara- m. "wish, Gegenstanddes Wunsches', vara- "vorzijglich, - 
st, better, best', varlyarhs- 'better', var/stha- 'best', i/5/ya-"wahlbar, vortrefflich, 
distinguished ', varana- n. "das Wahlen, WiJnschen', vara- m. "Kostbares, treasure, tribute' 
etc., vrtha' futile ', Avestan ap. var- " choose, want, desire, will' (3. PI. preterit Med. varata. 
Opt. vairfmaidfj, v9r9n[a]-{\. Sg. Med. versnS), v9rdnav-{3. Du. Med. varanvaite, 
participle Perf. Pass, varata-, va/rya-'tbe beste, delicious, worth '; also Avestan var- 
"believe'; 

Armenian gef pleasure, beauty' (presumably from *uel-no-, compare cymr. gwell 
"better'); Venetic PN Volti-xnos, Voltiomnus, lllyrian Voltius, Voltisa etc. (M. Lejeune BSL. 
49, 41 ff.) from *ulti-; 

gr. Asiu), Anw "will', after Schwyzer Gr. Gr. 1, 676 from *ule(i)mi, PI. * uleime {1); Latin 
void {* veld), vult{*velt), velle 'want, desire, will' (Opt. velim), voluntas, -at/si. "good 
volition' (previous participle *uolunt-tat-s); nolo, nevis, nevolt'\ will not' {*ne-vold); mald'\ 
pull vor', back formation after mavolt{magls volt); Umbrian e/7-i/e//^"jubeto', i/e//i/"deligito', 
e/7i/e/M/"decretum, edictum'; 

mcymr. corn. bret. guell'better', ncymr. gwell {*uel-no-'Vorzug , choice ', or to uer-2, 
see there); gall. VN VellavT, Catu-vellaunr{corc\pare den Ligurian PN Genava'GenV: raet. 
VN Genauni); 

Gothic wlljan. Old High German wlllu, will, wellan etc. "want, desire, will'; Gothic wllja. 
Old High German ulllo, wlllio etc. 'volition', Kaus. Iter. Gothic waljan. Old Icelandic veija. 



Old High German wellen^ choose ' (= Old Indie i/aAayaZ/'wahlt for sich', Old Church Slavic 
voliti); Old High German walai.. Old Icelandic i/a/n. 'choice '(: Old Indie vara- m.); 

Lithuanian pa-velmi, 3. Sg. pa-velt, Infin. pa-ve/t/" want, desire, will, allow', ablaut. v/7t/st 
"hope' {*ultis), K///^c»5 "hoffe'; Old Church Slavic veljg, ve/et/^\Nant, desire, will, order', 
ablaut, voljai. "volition', therefrom voljg, vo/ft/'want, desire, will, wish', in weiteren ablaut 
do-vbljQ, do-vbleti^ suffice \*Uole-)\ 

about Gothic wafia. Old High German wela, wolaeic. "probably' compare Feist^ 543. 

B. o^extension ((y-present): gr. £A5o|jai, hom. ££A5o|jai "sehne myself, demand after 
etwas', ££A5(ji)p n. "wish, desire'; 

Irish fled, cymr. ^MVeo'o'"Gastmahl, festival' {*ulda); gall. PN Vlido-rTx. 

C. yo-extension: hom. eAttu) "allow hoffen', EArrofjai, ££Ano|jai "hoffe', Perf. poet. £oAna; 
EATTiq, -i5o(;f. "hope', EAni^w "hoffe', hom. £Anu)pn "hope', zero grade *aAniaTO(;, Sup. to 
aArraAEOc;, dissim. apnaAsoq " desirable, worth having, welcome, wanted, charming', 
£naAnvo(; " desirable, worth having, welcome, wanted ' (///7-stem); Latin volup{e) Adv. 
"vergnijglich, gerne', CVcZ/O/-, *ulpi-), i/oA/p/as "pleasure'; 

doubtful hom. EiAairivn "festival', Aeolic EAAarriva (*£-FAaTT-iva?). 

References: WP. I 294 f., WH. II 828 f., Trautmann 348 f., Specht KZ 62, 59 f., Vasmer 1 , 
1 80, 224, Frisk 78, 455, 485, 502 f. 
Page(s): 1137-1138 

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
"Verdrangung from Besitzrechten' (*FoA-va); 

Lithuanian va//nas"\Na\\', i/a///7j7s"Tuchecke', Latvian va/n/s ' edge' , su-va/yt/"{ corn, 
grain) zusammenbringen, reap', Lithuanian /s-i/a/yZ/'heraus-, fortschaffen', va/yt/ ^c\ean'; 
Old Church Slavic *ve/b (: gr. ak\q) in velb-mi, -/77a "very, excessive', velb-leph 'very 
beautiful', velijb, i/e//]^b'big, large', *i/5/b'heap, bulk, mass' {*ud/os) in russ. va/om"\n bulk, 
mass', nava/'great heap', zai/a/'Verstopfung, Sperre', pr/va/ ^Lan6en' (*Andrangen), 
valbmja "haufenweise' etc.; 

5«-extension is probably Latin valgus, vulgus^6as people' (= 'big, giant bulk, mass of 
people', compare above russ. valom-b, valbmja) = Old Indie varga- m. 'dividing off, 
partitioning off, group'. Middle Breton ^M/5/c/7'UberfluR)', nbret. a-walc'h^ sufficient ' 
(compare oAk;), gwalc'ha^ satiate ', cymr. gwala'bu\k, mass, sufficient '; Tocharian B 
\/va Ike long' . 

References: WP. I 295 f., WH. II 826 f.. Frisk 71 f., 74, 117, 455 ff., Vasmer 180, 181; 
See also: original resemblance with *yel-Z'tum' is possible, da 'press, to press together ' 
originally 'zusammenwinden' sein kann. 
Page(s):1138 

Root / lemma: ueM, uele- 
Meaning: hair, wool; grass, forest 

Note: relationship to *uel-luxn' (' curly hair' ) or *uel-^ rend, pluck' is possible 
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

with voiced-aspirated Old Church Slavic vladb. Old Russian volodb^\\a\r\ 



D. Old Indie vala-, vara- m. " tail (haar), Haarsieb', ablaut. Lithuanian 1/5/arSchweifhaar 
of the horse'. 

References: WP. I 296 ff., WH. I 756, II 745, Trautmann 341, 359, Vasmer 1, 220 f. 
Page(s): 1139-1140 

Root / lemma: uel-5, uela- 
Meaning: to deceive 

Material: Lithuanian K////"cheat, deceive', Latvian K/7/ds., Old Prussian prawilts^ betray', 
Lithuanian kj7//^5 "deceit, artifice', zero grade Old Prussian po-wela^s\e verrieten', Latvian 
velts^ futile ', Lithuanian veltas^ useless'; (gr. ouAoc; = oKobo, above S. 777); Middle Irish 
/©//"deceit' (Middle Irish fall, newer /^///"Nachlassigkeif, cynnr.^M/a//"ds., lack', bret. gwall 
"evil, bad' are probably as eigene group for sich to place); after BGga Kalba ir sen. I 34 f. 
belong the Baltic words to uel-2. 

A extension from *uel- perhaps in: 

gr. sAscpaipofjai "cheat, deceive, swindle; betray, be disloyal; gull, fool, injure ' {*uel-dd^- 
), 6Ao(pu)iO(; "deceitful'; Lithuanian vllblnti {^ upd^-) " entice, affen, zum besten have'. 

References: WP. I 298; Frisk 493; different MiJhlenbach-Endzelin IV 534, 596. 
Page(s): 1140 

Root / lemma: uel^ 

Meaning: warm 

Material: Armenian p'c»/"heat', golanam^s\z\\ warmen'; Lithuanian vilditr lukewarm make'. 

References: WP. I 302; 

See also: perhaps to S. 1 142 under {uel-7). 

Page(s): 1140 

Root / lemma: uel-7, uela-, ule- 

Meaning: to turn, wind; round, etc.. 

Note: extended uel(e)u-, ul-ne-u-, u(e)lei- {6\ese also "umwinden, einwickein = einhijllen') 

Material: A. Old Indie valati, -/e"wendet sich, dreht sich' (?), Kaus. valayatr makes sich 

wenden, roll', valanam'das sich Wenden, sich Biegen, surge, Wogen', vala-m. 

"Bedeckung, cave' (or to *uer-7), vala-, valaka-m. perhaps "(round) balk, beam, shaft, 

pole', lengthened grade cakra-vala- n. " hoarfrost, ring, circle, bulk, mass', ala-vala- n. 



'immersion um die root eines Baumes' (compare Mayrliofer 1 , 79 f.), probably also vara- 
m. "(* turn) row, Folge, mal, Wochentag' = npers. bar'maV; 

from uf-m/-:0\6 Indie urm/- m. f. " surge, wave', Avestan varamis6s. 

from the ^basis: Old Indie vrnoti, z7/77d//"umhullt, bedeekt, umsehlieftt, umringt, hemmt, 
wehrt', Avestan varanavaiti ^be6ecVX hijllend' (eontain partly Indo Germanie *uer-5), das 
Avestan word also 'wendet (sieh)' as Old Indie valatr, compare S. 11 60; 

Old Indie varutra- (= gr. sAurpov) n. "Uberwurf, i.e. was man umlegt' (uncovered, ulva-, 
u/tia-m. n. "wrapping of embryo, womb, uterus' (compare Latin vo/va); 

from the /-basis: Old Indie va/aya-m. n. " circle, round Einfassung, bracelet ', va//ta- 
"gewendet, gebogen', va///-, Ka///"'Rankengewachs, Schlingpflanze', vallari-, valiant " 
tendril, Rankengewachs'; 

Armenian gelum{kox. gel!) 'turn, turn over; turn round, coil ', Med. " turn, coil ' (das 
present zur i/-basis, compare thematic Latin volvd), gelumn^ gyration, Umwindung' (= 
Latin volumen, z\K\j\^a'7), glem 'roWe, throw, cast low, base' {* gllem irom *uel- or *gulem 
from *udl-), gil{*uel-) 'round Wurfstein' (compare gr. 6K\xoq„ russ. 1/5/^/7 'round pebble'), 
presumably lamb{-i, -i\/) 'ring, circle ' from *^/-/77-bh/-(due to of /7-stem, compare 
Lithuanian vllnls. Old Church Slavic vltna. Old High German wella);
```


## [2026-10-17T00:01:15.357Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90500,90700p POK_full.txt | cut -c1-400 | grep -v \"^$\""
}
```


### [2026-10-17T00:01:15.882Z] TOOL RESULT

```
gr. siAsu) ' turn, twist, rotate, coil' (*F£A-v-£U)), lAAu) ds. (probably *Fi-FA-u), in addition 
\KKac, ' rope, band; close-packed, herding together, of cattle; ' \K\ac, = Troy, the Troad ', 
IKKoq ' squinting (the eye) ', Boeotian FiAAwv, lAAai auarpocpai, 5£a|Joi Hes.), Attic siAAu) 
ds. (*£-F£Aju)); from Aeolic eAAeoj (*F£Av£U)): zKKzbaydq 'rope, the band for binding corn- 
sheaves '), £iAiY^ and zik\\/\/oq 'whirl, turn, dizziness, giddiness; swindle ' (after zlktoj), 
zK\i\q, PI. £An£ic;, zK[}\yY^q, zK[}\yBz(;i. ' intestinal worm ', £uAn 'worm' (*£-FA-a), uaAr) 
GKcbAri^ Hes. (i.e. FaAri), £A£vr| ' plaited basket', 6AtJ0(; ' a round smooth stone (from which 
passage it was taken to signify the human trunk; any cylindrical or bowl-shaped body: 
mortar, kneadingtrough, hollow seat on which the Pythia prophesied, support, drinking- 
vessel, mouthpiece of a flute, stone used as a weight ', hom. ouAo(; ' frizzy, fleecy, woolly, 
woolen; of plants, twisted, curling; twisted, crooked ' (*F6Avo(;), redupl. ioukoq ' Milchhaar, 
Korngarbe, ein Insekt ', ouAoc; ' fascicle, sheaf ', ouAov 'the gums' (as ' torose, rounded '); 
from the /-basis: zhwoq " vine-layer, vine-tendril, the vine ', £Ai^ "winded', f. " bracelet ', 
therefrom zkiooo^, Attic eAIttu), and (after siAsu)) siAiaaoj ' curl, wind, turn; making it roll; 
turn round, to turn a chariot round the doubling-post; of any rapid motion, esp. of a circular 
kind; to roll or wind round, as the wool round the distaff; metaph. to turn in one's mind, 
revolve; to turn oneself round, turn quick round, turn to bay; of a serpent, to coil himself, of 
a missile, to spin through the air; to turn hither and thither, go about; to whirl in the dance ', 
ablaut. aAiv5u), Attic aAivSsu) " turn, twist, rotate, roll '; aAi^u) ds.; about 'HAig s. S. 1142; 
from the z/-basis: ep. eiAuu) " wrap, envelop, cover; to crawl or wriggle along, of a lame 
man ', Med. ' writhe, drag oneself along ' (*F£Avuu), compare KarasiAuov), compare 
participle siAucpooovTEc;; siAOcpa^siv 'whirl, turn, roll' (due to from *F£A-vu-q); £iAu6(;, £iAu0fj6(; 
"hiding place, nook, bolt-hole', zlkzoq (after siAsu)) ' intestinal obstruction, twisting of the 
bowels, cramp of the intestine, volvulus; lurking-place, den, hole; butcher's block; a kind of 
vine '; ablaut. *FoAoF6- " whirl, gyration ' in 6A(o)oi-Tpoxo(; " running in whirl ' = ' rolling 
stone '; FsAu- in Aor. Pass. sAuaGr) ' wurde geschleift, gewalzt ', sAuaGsiq ' wrapped ', 
Ionian Attic sAurpov (Hes. ysAouTpov) ' bow-case; sheath of a spear; mirror-case; case of 
a shield; sheath of the spinal cord, the shard of a beetle's wing; shell of a crab; of the eye- 
lids; of the umbilical cord; husk or capsule of seeds; the body, as being the case or shell of 
the soul; reservoir for water; tank for fish; container', £Aupo(; " case, quiver, a kind of 
Phrygian pipe, made of box-wood, with a horn tip and bend in the left pipe, millet; sheath ', 
£AuTr|<; "kind of pastry, perhaps pretzel ' (besides £iAuTa(;, zKK(jiaq); hom. slAap n. " a close 
covering, shelter, defence, fence, protection ' (*F£AFap, with prior dissimilation to *£AFap; 
compare £Aap por|9£ia Hes.; basic meaning probably " barrier or netting from winding 
branches '); *FAu- in n£AAuTpov " sock or bandage worn by runners on the ankle; foot- 
wrapper ', Perf. £'iAO|jai, £iAOfj£voc; " veiled '; secondary u: in Ei'Aupa ' sleeve, garment, 
wrapper, ' (Latin volumen, Armenian gelumn); 
in addition also eAiKri " willow ', DEAikwv "* mountain pasture, of osiers, of the willow- 
copse ' (FsAiKcbv of Korinna-Papyrus), like Old English welig, etc. ' willow ', different from 
Indo Germanic *salik- " willow '; 
after Frisk 36, 42, 80 here aisAoupoq m. f. " tomcat, cat ' or 'weasel', also aiAoupoc; (from 
a\bKoc, + oupa 'tail') and moKoo, 'quick, fast, movable, nimble, shimmering, varicolored; 
wriggling; changeful of hue, gleaming, glancing, of arms and armour; changeful, shifting, 
varied; shifty, wily, slippery ' from *(F)ai-F6A-0(;; aAuai(;f. ' chain, manacle' (*FaAu-Ti(;); 
Maybe /Kiokoc,, ou, 6, lord of the winds, properly the rapid or the changeable, Od. 
alb. vjer harvest; vomit ' {*uelud)\ valei. ' surge of kochenden water; wave, surge ' 
( *Uel9n§)\ 
Note: 
Wrong etymology, since alb. vJeiryoxwW derived from abbreviated Lithuanian i/e/77// "vomit', 
vemalaryovc\\\! > maybe truncated alb. {*vema/a/j y/e//\om'\t\ see Root / lemma: uem-, 
uema-: to spit, vomit. 
Latin vo/at " roundness, cavity the hand or the Fuftsohle' (compare Old Icelandic va/r' 
round ', Old Indie va/a- m. 'cave'); from the ^-basis 1/0/1/0, -ere, -/" vo/utum'roW, kollern, 
walzen, turn, whirl' {*ue/ud), vo/umen' pulley ', involucrum ^ s\eeye, wrapping, sheath ', 
involucre "Serviette', probably also 1/0/1/5, vulva " womb, uterus, Eihaut the Pilze'; 
reduced grade i/5//^5 'picket, pole, palisade, fence made from stakes; protective fence 
made from poles that are inserted into the ground ', wherefore as collective vallum 
"Pfahlwerk, Verschanzung' [out of it borrowed Old Saxon wal Old English weall Middle 
High German wal(l) 'Wall]; valles, vallls'yaWeY ('*incurvation ') = gr. *VaK\c, > ^HMq 
{*Uelnis), 1/5/1/50 "die TiJrflugel, DoppeltiJre', 1/5/1/0/50 'Schoten' (*t/e/^5); 
Old Irish fllllcl' bends' (previous /7-present), bret. goalenn' twig| sprout] stalk ' ("*flexible 
rod'); Old Irish felmae{= felmae) " hedge; fence, anything planted/erected to form 
surrunding barrier' (presumably '*wickerwork'); o-grade Middle Irish falm. "fence, paddock 
', cymr. gwawF wall, rampart, entrenchment'; 
doubtful Middle Irish fail, foil{Gen. falacli) "ring' {*Uelik-, ablaut, with sAi^?); 
Old Icelandic 1///PI., Gen. vilja' intestines, entrails ', Old English we(o)loc, weolc, uioloc 
"Trompeterschnecke', Dutchn/o/A, wulkds. from Germanic *weluka-, probably zur f/-basis, 
as certainly Gothic M/5/My5/7 "walzen', n/5/ty/sd/7 "wallow'. Old English M//0/14/5/7 "walzen, roll' 
{*walwjan), waiwianix. intr. "walzen, roll'; Old Icelandic vair' round ', Old English walui. 
"Strieme after a blow, knock' {*uolo-, -a, compare Latin 1/0/5), Middle Low German walen 
"turn, walzen, roll'. Old High German M/^/s/5f. 'bulge; bead; lip; torus; wreath; roll; bulb 
' Gothic M/5/C/5" staff. Old Icelandic i/p//'"round staff. Old Frisian M/5/i/-/?o/'5"Stabtrager', 
Old English i/y/'/-M/5/5 ("Wurzelstock'), Old High German wurzala '/"oo/'; /7-present Old High 
German M/0//5/7 "round, roll'. Old Saxon biwellan' blemish ' ("*in smut herumwalzen'). Old 
Frisian /7/M/i///o/7 participle "befleckf, wherefore Old High German wella' Welle= wave', 
compare with formants -mi- (as Old Indie urmf-, Avestan varsmi-) Old High German walm 
"Aufwallen, Sieden, heaf. Old English wielm, wylm' surge, Wallung, Sieden'; 
with the meaning "waves, billows throw' (compare Old High German weilaeic), " to 
bubble up, boil up, surge up' (from Ouellen and esp. from siedendem Wasser, from which 
partly also words for "vapor, heaf entsprangen) besides Old High German walm. Old 
English wielm a\so Old Icelandic vella, vail 'effervesce, simmer, seethe, boil, boil'. Old High 
German (etc.) wallan, w/e/'\Nogen, wallen, to bubble up, boil up, surge up, simmer, 
seethe, boil, cook', Kaus. Old Icelandic i/e//5'zum Sieden orSchmelzen bringen, 
zusammenschweiften'. Middle Low German Middle High German wellen6s.. Old Icelandic 
vellai. 'Sieden', Old Frisian walla. Old English wielli. 'wellspring, Sieden', zero grade 
Norwegian ollai. "wellspring', Gothic M/^/a/7 "simmer, seethe, boil'. Old Icelandic y//" 
"Warmedunsf, y^5"warm', olmr^ furious ': Old High German waloMN. "tepide', walT 
"tepor'; here uel-6S. 1140? 
lengthened grade Old English waelm. n. "whirlpool, pool', wselan {*wdljan) "walzen'. 
Middle Low German wdlen6s.. Old High German wuolen 'dig, aufwijhlen' (compare zum 
ablaut Old Church Slavic valltr\NdL\zev\\ and to meaning "aufwiJhlen' also Modern High 
German Wal, Wehle, ty^^/?/© "of Wasser ausgewaschene immersion'); 
Lithuanian vellu, veltl {heavy basis) "walken', i/a///s "thread, string, fishing net' (= russ. 
volofb " filament, fibre ' besides the intonation), Latvian i/e?/ "walzen, walken', Lithuanian 
apvalus, Latvian aphis' round ', Old Prussian M/5//S "Zugscheit am cart ', Lithuanian vole 
"wooden beetle, hammer', yoai/o/a/ "Walzen', Latvian valei. "Waschbleuel', vT-vala'\he 
Laufstock beim Garnwinden' (: vTvaluoV be exuberant '); Lithuanian i/e/e/i i/e/"against, 
noch einmal', Latvian i/e/"still, further' ("against' from " turn ') and with meaning- 
development "sich entwinden, sich winden = hesitate' perhaps Lithuanian velus, Latvian 
i/^/s"late', Lithuanian i/5/5/7o'5" while ' (out of it russ. i/5/5/7o'5"Saumseliger'); 
Slavic *i/5/b m. in Church Slavic 1/5/b "wave', russ. i/5/"wave, surge, Waize' (Balto 
Slavic *udla-), c»i6>i/5/"Erdrutsch', yC>/'(9i/5/"Einsturz'; Old Church Slavic i/5////s^"KuAi£a9ar, 
russ. i/5//?i. "walzen'. Iter. serb. valjafi, russ. i/5^a/i. "walzen, walken', ablaut. russ.-Church 
Slavic obbib " round ', russ. di6>/>y'"roundish' {*ob-vblb); about russ. volofb see above; 
Balto Slavic *ullna-{*ulna)i. "wave' in Lithuanian vllnis, vllnia, Latvian i////7a "wave'; 
Slavic *vblna\r\ Old Church Slavic vibna, russ. volna6s.; in addition Old Church Slavic 
vblatr\v\ Wallung bringen'. 
Tocharian A walylP\. " worms '. 
B. fltpresent (respectively o'-Erweiterg.): Old Icelandic velta, valt. Old High German 
walzan. Middle High German walzen, wielz' s\c\\ walzen'. Old High German also "volvere 
animo' (wgrm. 5-present to a Perf. with Indo Germanic o neologism with UnterstiJtzung of 
Iterativs:) Gothic waltJan'\Na\\o\N\ uswaltjan 'u{r\\Na\zen', Old Icelandic velfa. Old English 
wieltan. Old High German welzaniraus. 'walzen, roll, turn'. Old Norse valtr. Old English 
wealt'ro\\ev\6, walzbar, unbestandig'; Old English wlatlanuu'^ers. "nauseare', wiseta, 
wisettaxw. " disgust, repulsion, ioatliing ' {*wlatiPa), w/setan loedare', Middle Low German 
wlaten^ disgust ' {ule-d- : ula-d-)\ also besides Old High German wa/{ajgdn 'waWow , roll' 
stands Middle High German die meaning " disgust, repulsion, loathing feel', walgunge' 
seasickness ', also Norwegian dial. Ka/p'"widerlich, evil' (see below); 
o^Erweit. also in Latvian velde, ve/dre^das of rain niedergelegte (as gewalzte) corn, 
grain '; compare from the /-basis above gr. aAiv5w, aAiv5ew, aAi^w. 
C. further formation: 
ulei-s-, u//-s-\r\. Old Irish f/esc'rod' {*uliska), Gothic wlizjan^hW, chastise, castigate' (if 
derivative from a V//za-'rod'), Slavic *leska{*vloiska), russ. -Church Slavic /es/ro i/z> "from 
dem wood of Styraxbaumes gemacht', serb. lijeska^ hazel shrub ' etc.; about russ. les 
"wood, forest, wood ' {*lesh), /esa "fishing line, fence', which perhaps belong here, s. 
Vasmer 2, 33 f. and above S. 665. 
Maybe alb. //is "oak, oak forest' a Slavic loanword from Old Church Slavic: les-b "forest, 
wood(s)', Russian: /es "forest, wood(s)', Ukrainian: //s "forest, wood(s)'. 
ule-ro-, ulo-ro-, ula-ro-:qr. £uAr|pa, Doric auAripa PI. "rein', apAripa nvia Hes. (*£-, a- 
FAripo-), Latin lorum "strap', lorica " a leather cuirass, corselet of thongs; a defence, 
breastwork, parapet: pinnae ' , Armenian /a/'"rope, cord, bowstring, muscle ', compare 
above S. 1139. 
D. guttural extensions: 
uolg-\v\ Old Indie i/a/g5//"(*dreht sich), hijpft, springt', with sam-' places sich in rollende 
Bewegung', with abh/- "wallt auf, va/ga'br\6\e, rein, rein', Latin i/a/g^5"sabelbeinig'. Old 
English wealcan, weolc^roW (tr. and intr.), sich hin and her bewegen, volvere animo'. Old 
High German walkan. Middle High German walken, ty/e/c "trample, felt, thrash'. Middle 
High German also 'wallow'. Old Icelandic valku. "das Hinundhergeworfenwerden, esp. auf 
the sea'. Old English gewealcu. "das Rollen', wealcam. " surge '; *walkdn\v\ Old Icelandic 
i/a//ra"from place to place drive, push or Ziehen, plague, volvere animo'. Old English 
wealcian^roW (intr.), engl. walk^ wander ', Middle Low German walken^ drum, tumble, full, 
mill, flex, bend, knead'; Latvian Ka/g5"rope, cord'; 
nasalized Old Saxon ty/a/7/r"minxish, wanton, bold'. Old English i4'/a/7c"minxish, wanton, 
stout, proud, stately', if from the meaning " jumping ' (: Old Indie valgati) evolved. 
£/o/Ar-;in Middle Low German M/a/ge/7 "wrestle, struggle, fight, feeling of sickness', 
Norwegian olga^ be disgusted ', Old High German wa/{ajgdn ^waWow, roll', trans. " writhe, 
twist, be tormented (by pain), roll'. Middle High German unpers. m. Dat. " disgust, 
repulsion, loathing feel', wa/gunge' seasickness '. 
References: WP. I 298 f., WH. I 822, II 728 ff., 825, 832 ff., Trautmann 349, Vasmer 1, 165 
f., 234, Frisk 36, 42, 457 f., 461 f.; 
See also: compare ue/-3. 
Page(s): 1140-1144 
Root / lemma: ue/-8 
Meaning: to tear, wound; to steal
```


## [2026-10-17T00:01:19.380Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90700,90760p POK_full.txt | cut -c1-400 | grep -v \"^$\"; grep -n \"Meaning: wolf\" POK_full.txt"
}
```


### [2026-10-17T00:01:19.682Z] TOOL RESULT

```
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
93077:Meaning: wolf
```


## [2026-10-17T00:01:24.333Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 93070,93130p POK_full.txt | cut -c1-400 | grep -v \"^$\""
}
```


### [2026-10-17T00:01:24.669Z] TOOL RESULT

```
Tocharian AB {*vlek) /e/r 'shape, apparition'. 
References: WP. I 321, J. B. Hofmann Etymol. gr. Wb. 106, Frisk 629, Mayrhofer 1, 112. 
Page(s):1178 
Root/ lemma: y/k'^-os {* hau/k''-) 
Meaning: wolf 
Note: 
Root / lemma: yflc-os : "wolf derived from an extention of Root / lemma: uiek-, ijjk- : "to 
shine; fiery' [similarity of sparking beastly eyes in the dark] 
Material: Old Indie i/r/ra-m. "wolf, vrkTh' she-wolf, vrkat'h "ein Wolfischer', i/A/rayiz-'mad, 
wicked, evil, mordlustig '; Avestan i/a/7/'/ra- "wolf (geneuertes = renamed, has changed?^ 
Fem. vshrka); gr. Kukoc, (geneuertes = renamed, has changed?? Fem. AuKOiva); Latin 
lupus {sab\v\. loanword); Gothic wulfs. Old Icelandic ulfr. Old English Old Saxon wulf. Old 
High German wolF^oW, fem. Old High German wulpa. Middle High German wuipe. Old 
Icelandic y/g/'(from *wulgis, Indo Germanic *ulk% Lithuanian vilkas, Latvian vilks. Old 
Prussian wilkis. Old Church Slavic K/B/rbds.; fem. Lithuanian viike, Slavic Kb/c/-cain serb. 
vucica, russ. volcfca, 
with double zero grade (?): alb. {*wulku) u/k'woW, Ligurian MN U/kos, lllyrian PN 
Ulcudius, U/c/rus mons, PN OuAkIviov, Pannonian U/c/s/a castra; abrit. PN Ulcagnus, Proto 
Irish (Ogam) Gen. Ulccagni= Old Irish PN Olcan, also also Old Irish olc. Gen. i///c"mad, 
wicked, evil', as Subst. m. " Missetater ', n. "evil, harm, evil, wickedness ' (see307, 310); 
compare also paon. MN Aunrrsioq, Aukkeio^ could point to old Labiovelar; Szemerenyi 
(KZ. 71, 199 ff.) receives lllyrian ulk-irom *uulk-, Indo Germanic *ulk"-\ then Celtic ulko- 
must be looked as lllyrian loanword; conspicuous is Latin PN Vlp(ius) Lup/o{C\R 130); 
Note: 
Alb. {*ulcogna) ^//ro/T/e "she-wolf : abrit. PN Ulcagnus: Swedish varghona, varginna, 
vargbona, varghona, varginna, vargbona^ she-wolf, common alb. -kn- > -nj-. 
possible would be also, daft Latin lupusav\6 Germanic *wulfaz\N\Vc\ Indo Germanic yOto 
Old Indie lopasa-rw. "jackal, fox', Avestan raopi-. Middle Persian ropasetc. belongs, or 
mindestens from a derartigen root-influenced is (see above S. 690, where also Gall. PN 
AouEpvioq, abrit. Gen. Lovernii, cymr. Ilywarn, acorn, louuern, nbret. louarnlox\ Indo 
Germanic 7c»^pe/77c»-5 hinzufijgen is). 
References: WP. I 316 f., WH. II 836 f., Trautmann 359, Vasmer 1, 218, 223 f.; various 
distorted taboo; den Labiovelar leugnet W. Wissmann in D. Wb. 14, 2, 1242. 
Page(s): 1178-1179 
Root /lemma: ulp-, lup- {* haulk"-) 
Meaning: a kind of carnivore (fox, wolf) 
Note: 
Root / lemma: ulp- lup- {* haulk"-): "a kind of carnivore (fox, wolf)' derived from Root/ 
lemma: ullc-os {* haulk"^: 'wolf [common Latin /r"'- > p-]. 
Note: older ©-stem
```


## [2026-10-17T00:01:26.785Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 93130,93160p POK_full.txt | cut -c1-400 | grep -v \"^$\""
}
```


### [2026-10-17T00:01:27.207Z] TOOL RESULT

```
Material: Avestan urupi-sxx\. {*lupi-s) 'dog', raopi-s^iox, jackal'. Middle Persian ropas, 
npers. robah^ioyC = Old Indie /opasa-m. 'jackal, fox'; 
Maybe alb. lope'cow, (huge consuming animal; cow eaten by wolves)', //up'devour', //ape 
'tongue' : Lith. /apent/^to swallow food'. 
Armenian a/ues Gen. -esulox'; 
Maybe zero grade in poln. ( */ues) /is 'fox'. 
gr. (*FaAu)n6(;) aAcbnn^f., short form aAwno^; (common gr. F- = u-) 
Latin Ko/pes'fox', possibly also /upus'\No\V; 
Lithuanian /ape{*u/ope), Latvian /ap55 (syncopated from /apesa?\ndo Germanic 
*u/opeR^)\ compare Lithuanian v//p/sys^ wild cat ', it would be placed near Middle Persian 
gurpa/<u^ers. gurba^ house cat, domestic cat ', from Iran. *urpa-, Indo Germanic *u/pos, it 
concerns certainly various taboo adjustments. 
References: WP. I 316 f., WH. I 836 f., II 830, Frisk 83, Trautmann 149, Specht Indo 
Germanic Dekl. 36, Liden KZ. 56, 212 ff. 
Page(s):1179 
Root/ lemma: udo'^sa {* haudo^sS) 
Meaning: wasp
```


## [2026-10-17T00:01:43.789Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['BQT','MON','MON5','KLN','HRN','SNS','SOD','AHD']:\n  v=d.get(k); print(k, json.dumps(v,ensure_ascii=False)[:900] if v else None); print()\n\""
}
```


### [2026-10-17T00:01:44.286Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

MON5 None

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent;

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Ve

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins
```


## [2026-10-17T00:01:57.005Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -n -i \"^ *wel-\\|^wel-\\|wel- *[23]\\.\\|^ *wel-[0-9]\" data/verification/sources/refs/AHD_watkins1985.txt | head; timeout 300 python3 tools/ref_page.py BQT:968 2>&1 | head -60"
}
```


### [2026-10-17T00:01:57.412Z] TOOL RESULT

```
1139:wel-3
1141:wel-4
no scan of BQT covers printed page 968 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:01:59.895Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1125,1150p AHD_watkins1985.txt | cut -c1-300; grep -n \"^wel\\|wel-[0-9]\\|^ *wel\" AHD_watkins1985.txt | head -20"
}
```


### [2026-10-17T00:02:00.273Z] TOOL RESULT

```
wé-. To blow. Contracted from “*wea-; oldest basic form *gwé- (< *owea-). 1. Suffixed irregular shortened form *we-dhro- in Germanic *wedram, wind, weather, in Old English weder, weather, storm, wind: WEATHER. 2. Suf- fixed (participial) form *wé-nt-o-, blowing, in: a. Ger- manic *windaz in (i) Old 
webh-. To weave, also to move quickly. 1. Germanic *weban in Old English wefan, to weave: WEAVE, WOOF'. 2. Germanic *wefta- in Old English wefta, weft, cross thread: wert. 3. Suffixed o-grade form *wobh-yo- in Germanic *wabjam, fabric, web, in Old English webb), web: WEB, WEBSTER. 4. Suffixed German
wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, 
wed-2, To speak. 1. Possibly oldest root form *awed- becoming *awed- in reduplicated form *awe-ud- dissimi- lated to *aweid-, with suffixed o-grade form *awoid-o- respectively in Greek aeidein (Attic aidein), to sing, and aoidé (Attic didé), song, ode (but more likely a separate root *aweid- becomin
wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
weg-'. To weave a web. Related to wokso-. Suffixed
weg-?
form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-
74
weia-
Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, s
weik-'
derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffi
75
wel-3
for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bison
wel-4
HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 
wer-3
*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2;
wer-4
TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: W
wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germ
wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
77
wers-2
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
537:gva-. Also grem-. To go, come. 1. Germanic *kuman in: a. Old English cuman, to come: COME; b. Germanic *kumo6n-, he who comes, a guest, in compound *wil-ku- mon-, a desirable guest (*wil-, desirable; see wel-2), in Old English wilcuma, a welcome guest, and wilcume, the greeting of welcome: WELCOME; C. compound *bi-kuman, to arrive, come to be (*bi-, intensive prefix; see ambhi), in Old English becuman, to become: BECOME. 2. Suffixed form *g“(e)m-yo- in Latin venire, to come: VENIRE, VENUE; ADVENT, (ADVENTITIOUS), (ADVENTURE), (AVE- NUE), CIRCUMVENT, CONTRAVENE, CONVENE, (CONVEN- IENT), (CONVENT), (CONVENTICLE), (CONVENTION),
1044:s(w)eks. Six. I. Form *seks. 1. Germanic *seks in Old English s(iJex, six, six: sIx. 2. Latin sex (> Italian sei), six: SENARY, SEX-; SEICENTO, SEMESTER. 3. Suffixed form *seks-to- in Latin sextus, sixth: SESTET, SESTINA, SEXT, SEXTAN, SEXTANT, SEXTILE; SEXTODECIMO. II. Form *sweks in Greek hex, six: HEXA-, HEXAD. [Pok. sueks 1044.] swel-', To eat, drink. 1. Perhaps Germanic *swil- in Old English swilian, to wash out, gargle: swILL, 2. Extended form *swelk- in Germanic *swelgan, *swelhan in Old English swelgan, to swallow: SWALLOW!; GROUNDSEL!. 3. Iranian *khvdra- (attested in Avestan), to eat, in the probable source of Greek mantikhdras, manticore (see mer-?). [Pok. 1. suel(k)- 1045.] swel-2, To shine, burn. 1. Extended form *sweld- in Germanic *swiltan in Old English sweltan, to die, perish (perhaps < “be overcome with heat”): (SULTRY), SWEL- TER. 2. O-grade form *swol- in Germanic *swal- in Old Norse svalr, cool (< “lukewarm” < “hot”), akin to the Scandinavian source of Middle English swale, shade, shady place: SWALE. [Pok. 2. swel- 1045.]
1045:swel-3, Post, board. Germanic *suljé- in Old English sylXe), doorsill, threshold: stLL. [Pok. 2. sel-, swel- 898.] swem-. To move, stir, swim. Possibly an Indo-European root, but perhaps Germanic only. 1. Germanic *swimjan in Old English swimman, to swim: SWIM. 2. Suffixed zero-grade form *swum-to- in Germanic *sundam in: a. Old English sund, swimming, sea: SOUND’; b. Old French sonde, sounding line: SOUND‘; RADIOSONDE, ROCKETSONDE. [Pok. syem- 1046.]
1139:wel-3
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1141:wel-4
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1247:ANTA aneta ANTAGONIZE ag- ANTE ant- ANTEBELLUM duellum ANTECEDE ked- ANTEFIX dhig¥- ANTEPENDIUM (S)pen- ANTERIOR ant- ANTHELION sawel- ANTHELMINTIC wel-3 ANTHEM bha-2 ANTHEMION andh- ANTHER andh- ANTHESIS andh- ANTHO- andh- -ANTHOUS andh- ANTHROPIC ner-2 ANTHROPO- ner-2 ANTHURIUM ors- ANTI- ant-
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1293:BENEVOLENT deu-2, wel-2
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1382:COL kwel-1 COLANDER kagh- COLCANNON kaul-, weid- COLD gel-3
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
```


## [2026-10-17T00:02:05.639Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o \"WALLET [a-z0-9-]*\\|ADOLPH[^ ]* [a-z0-9-]*\\|WILLOW [a-z0-9-]*\\|HELIX [a-z0-9-]*\\|VALLEY [a-z0-9-]*\" AHD_watkins1985.txt|sort -u; grep -n -i \"^Adolph\\|^Adolf\" KLN_1966.txt | head; grep -n -i \"^wallet\\|^willow\\|^walk\\b\\|^helix\" KLN_1966.txt | head"
}
```


### [2026-10-17T00:02:06.066Z] TOOL RESULT

```
HELIX wel-3
VALLEY wel-3
1690:Adolph,  Adolphus,  masc.  PN.  —  L.  Adolphus,  of Teut.  origin.  The  name  lit  means  ‘noble  wolf’; cp.  OHG.  Athalwolf,  Athaulf,  Adulf,  Adolf  (G. Adolf),  fr.  athal,  ‘noble’,  and  wolf,  ‘wolf’.  For the  first  element  see  Adelaide  and  cp.  words  there referred  to.  For  the  second  element  see  wolf.
17497:helix,  n.,  spiral  line.  —  L.,  fr.  Gk.  tnZ,  (for ‘spiral,  coil’,  from  the  stem  of  gXlaaetv (for  *.FeXtxieiv),  ‘to  turn  about,  wind,  roll’, fr.  I.-E.  base  *wel-,  ‘to  bend,  turn,  twist,  roll’. See  volute  and  words  there  referred  to  and  cp. esp.  Helicon,  helminth.
```


## [2026-10-17T00:02:09.074Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^wallet,\\|^willow,\\|^walk,\\|^well,\\|^volve\\|^revolve,\\|^valley,\\|^valve,\\|^vault,\\|^volume,\\|^volute,\" KLN_1966.txt KLN_1971.txt | cut -c1-500 | head -30; grep -n -i \"^WALLET\\|^wallet\" SKT.txt | head"
}
```


### [2026-10-17T00:02:09.437Z] TOOL RESULT

```
KLN_1971.txt:69670:volvere , ‘to roll’. See volute and cp. envelop. 
KLN_1971.txt:82844:volve. — Formed fr. ist en- and AF. tail, ‘limit- 
KLN_1971.txt:165099:volvere, ‘to wrap’. See volute, 
KLN_1971.txt:177870:walk, go’. See amble and verbal suff. -ate. 
KLN_1971.txt:206377:volver e (pp. revolutus ), ‘to roll back, revolve’. 
KLN_1971.txt:206399:revolve, intr. and tr. v. — ME. revolven, fr. L. re- 
KLN_1971.txt:206400:volvere, ‘to roll back, revolve’, fr. re- and volvere , 
KLN_1971.txt:210897:well, sound’, which is rel. to salus , ‘sound con- 
KLN_1971.txt:251527:walk, go’. See grade, ‘step’, and cp. words there 
KLN_1971.txt:258941:valley, n. — OF. valee, vallee (F. vallee), fr. val, 
KLN_1971.txt:259019:valve, n. — L. valva, ‘leaf, fold or valve of a door’, 
KLN_1971.txt:259021:volvere, ‘to roll’. See volute and cp. bivalve. 
KLN_1971.txt:259644:vault, n., an arched roof. — ME. voute, vowte, fr. 
KLN_1971.txt:259654:vault, tr. v., to cover with a vault. — ME. vouten, 
KLN_1971.txt:259659:vault, intr. and tr. v., to leap. — ME. vauten , 
KLN_1971.txt:259663:vault, ‘arched roof’, and cp.volt, ‘a turning move- 
KLN_1971.txt:259666:vault, n., a leap. — MF. (= F.) volte, fr. It. volta , 
KLN_1971.txt:263670:vault, ‘to leap’, and cp. volte-face, volti, archivolt. 
KLN_1971.txt:263728:volume, n. — ME. volum, volume, fr. MF. (= F.) 
KLN_1971.txt:263729:volume, fr. OF., fr. L. volumen , ‘a roll; a book 
KLN_1971.txt:263804:volute, n., a spiral scroll forming the chief fea- 
KLN_1971.txt:263839:valve, vault, ‘roof’, vault, ‘to leap’, volar, volt, ‘a 
KLN_1971.txt:263854:volute, 
KLN_1971.txt:263856:volvelle, n., an old device serving to ascertain the 
KLN_1971.txt:264603:walk, intr. v., to move about on foot, go; tr. v., 
KLN_1971.txt:264624:walk, tr. v., to full (Brit.) — ME. walken , fr. 
KLN_1971.txt:264655:wallet, n., a bag. — ME. walet, prob. metathesis 
KLN_1971.txt:266038:well, n., a spring. — ME. welle, fr. OE. wella, 
KLN_1971.txt:266049:well, intr. v., to spring, rise. — ME. wellen, ‘to 
KLN_1971.txt:266058:well, adv. — ME. wel, fr. OE. wel, rel.’ to OS. 
21169:Wallet ;  see  Wattle.
```


## [2026-10-17T00:02:11.951Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for l in 264603 264655 266038 263804 258941; do sed -n \"${l},$((l+12))p\" KLN_1971.txt | tr '\\n' ' '; echo; echo ---; done; grep -n -i \"^willow\" KLN_1971.txt | head -3"
}
```


### [2026-10-17T00:02:12.466Z] TOOL RESULT

```
walk, intr. v., to move about on foot, go; tr. v.,  to go through or over. — ME. walken and  walkien , ‘to walk’ (prob. meaning orig. ‘to roll  along’), fr. OE. wealcan, ‘to roll, toss’ (tr. and  intr.), resp. wealcian, ‘to roll up, muffle up’  (intr.), rel. to ON. valka , ‘to drag about’, Dan.  valke, Swed. valka, ‘to full’, MDu. walken , ‘to  knead, press, full’, Du. walken , ‘to work or felt  (a hat)’, OHG. walchan , ‘to knead’ (whence  MHG. walken , ‘to knead, full’, G. walken , ‘to  full'), fr. I.-E. *walg-, whence also OI. valgati ,  ‘he jumps with joy', valga, ‘bridle, rein’, and  prob. also L. valgus, ‘bowlegged’; cp. valgus.  
---
wallet, n., a bag. — ME. walet, prob. metathesis  of ME. watel , ‘basket, bag’. See wattle,  walleye, n., eye with a whitish cornea. — Back  formation fr. walleyed.   walleyed, adj. — ME. wawil-eghed, fr. ON. vagl-  eygr, ‘walleyed’, lit. ‘having a beam in the eye’,  fr. vagi , ‘roost, beam; beam in the eye’ (name of  a disease), and eigr, ‘eyed, having eyes’, fr. auga,  ‘eye’. ON. vagi is rel. to ON. vaga, ‘to wag,  waddle’, vog, ‘lever’, vega, ‘to move, carry’, and    
---
well, n., a spring. — ME. welle, fr. OE. wella,  wiella, rel. to ON. vella, ‘boiling heat’, Du. wel ,  ‘spring, well, fountain’, OHG. wella, MHG., G.  welle, ‘wave’, from I.-E. base *wel-, ‘to turn,  roll’, whence also OI. urmih , Alb. vaVe (fr. I.-E.  *wl-na), ‘wave’, OSlav. vluna , Lith. vilnis, ‘wave’.  L. volvere, ‘to roll’. See volute and cp. words  there referred to. Cp. also next word. Cp. also  weld, ‘to unite’, and the second element in pot-  waller.   well, intr. v., to spring, rise. — ME. wellen, ‘to  boil’, fr. OE. wyllan , wiellan, rel. to OE .'weallan,  
---
volute, n., a spiral scroll forming the chief fea-  tures in Ionic and Corinthian capitals. — F., fr.  It. voluta, fr. L. voluta, ‘spiral scroll, volute’,  prop, subst. use of the fem. pp. of volvere, ‘to  roll, roll along, turn about’, which is cogn. with  Gk. ecXeiv (for *feXveiv ), ‘to roll, turn, twist’,  eiXtisiv (foe *J r eXvueiv or *!feX0siv ), ‘to roll  round, enfold, enwrap’, eXi jetv, ‘to roll’,  eXioaetv, Att. ^Xittciv, Ion. eDdoostv, (for  *feX(xteiv), ‘to wind, roll’, £Xi £ (for *feXt£),  ‘coil, spiral’, Arm. gelum, ‘I turn, twist’, glem,  ‘I roll’, OI. vfnoti, ugnoti, ‘covers, wraps’,  varutram, ‘wrapper’, vdlate, ‘turns’, Toch.  
---
valley, n. — OF. valee, vallee (F. vallee), fr. val,  ‘valley’, fr. L.- valles, later vallis. See vale, ‘val-  ley’. Cp. It., Sp., Port, valle, Prov. val, ‘valley’,  which are of the same origin as OF. val.  Vallisneria, n., a genus of plants, the tape grass  and the eel grass (hot.) — ModL., named after  the Italian botanist Antonio Vallisneri (1661-  1730). For the ending see 1st suff. -ia.  Vallisneriaceae, n. pi., a family of aquatic plants  {bot.) — ModL., formed from prec. word with  suff. -aceae.   vatlisneriaceous, adj. — See prec. word and  
---
211311:willow bark. 
262190:willows’, so called from the willow copse that 
267289:willow, n. — ME. wilghe , wilowe, fr. OE. welig,
```


## [2026-10-17T00:02:17.449Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 267289,267300p KLN_1971.txt | tr '\\n' ' '; echo; grep -n -i \"wallet\\|willow\" SKT.txt | head -5; grep -n \"^Wattle\\|^Willow\" SKT.txt"
}
```


### [2026-10-17T00:02:18.015Z] TOOL RESULT

```
willow, n. — ME. wilghe , wilowe, fr. OE. welig,  wilig, OS. wilgia , rel. to MLG., MDu. wilghe,  Du. wilg, and cogn. with Gk. £Xbaj (for *Fe-  Xlxtj), ‘willow’, SXi£, ‘coil, spiral’, from I.-E.  base *wel -, ‘to roll’, whence also L. volvere, ‘to  roll 5 ; see volute. OE. welig , etc., ‘willow’, prop  means ‘the tree with pliant branches’. Cp. E.  withy, which is cogn. with L. viere, ‘to bend,  twist’.   Derivatives: willow, tr. v., willo w-y, adj.  willy-nilly, adv. — Contraction of will I, nilll, or  
2201:tra^,  willow*bu»li.     IVob.
10928:mietreea.  a  lady  of  a  household.  (F.  • L.^     0.  F,  maistresse.  '  a  raiatress,  dame  ; ' Cot.  {F.mai/resse.)   Fcta.  of  O.V.maistre, a  master  ;  mtc  niaater  (above). AlagnoUa.    (K.)      A  genua  of  plants named  after  Pierre  jI/e^^w/,  of  MootpcUier, in  i- ranee;  died  a.i..  1715. Magpie,  a  bini.  (F.-L.-Gk. ;  a«</ F. —  L . )     A  Uo  ca  1 1  ed  Bnagpt-pU,  ^i^gg^^y  -/". Mag  is  short  for  Magoi  -  F.  Afargof,  a familiar  form  of  F.  Margverite,  alsu  used to   denote  a  magpie.      This  ii  from   L. Margarita^    fik.  fuxfrfapirrftf   a   pearl ;  cC Pers.    muruftirii/.  a   fiearl.     /W  ■»  F.  /i>, from  L.  fica,  a  magpie ;  see  Pie  (x). Mahogany,  a  trc«.   (W.  Indian.)    The native  S.  American  name  (Webster). Mahometan ;  see  Mohammedao. Maid.  Maiden:  see  May  {,i). Mail  (I),  »tccl  network;  sec  Maculate. Mail    (3),  a   letter-bag.    (F.-U.  H.  G.) M.  E.  mo/f.  — O.  F*.  ma/e  {¥.  ma/Ze),  a  bag. wallet  —  O.  H.  G.    malaho,    a    leatheni wallet. +Gae].  and  Iri:>h  jwo/a,  a  bag:  Gk. /i«A7'.'F,  hide,  skin.
12900:Osier.  (F.-Low  U-Gk.)  F.«*^i)J_ oiier,  red  withy,  water-willow  tree;' C| Allied  to  Low  L.  ontHa,  mtumwi^  M bcils   (9th    cent).  «  Gk.  tl^m, (VWl.)
16424:(E.)     M,  E.  sa/we-A  S    sral^, sea/M,    a  willow.     Name*!    from near  the  water;  cf.  Skt.  mA/i    t,i,^f»^ water,  jiJhruy'if,  a  loins.  4- siifg,  saSj.  Dan.  selje.  G.  / . Sttlnhti,  L.  raiix,  Gael  a  I
16425:sailea^h,    W.     iufyg    (pt.  . willow.    (VSAR.)
21241:Wattle,  a  flexible  rod,  hurdle ;  fleshy part  under  the  throat  of  a  cock  or  turkey. i^E.*)  The  orig^.  sen&e  was  something  twined or  woven  together;  hence  a  hurdle,  a  bag of  woven  stuff,  a  bag  on  a  cock's  neck. M.  E.  watel,  a  ba^ ;  A.  S.  tuafel,  watul,  a hurdle.  Base  WAT;  from  ^W A,  to  bind. wallet,  a  bag,  budget.  (E.)  M.  E. wa/et,  a  comiplion  of  M.  E.  wafeit  a  wat- tle, also  a  bag.  In  P.  Plowman,  C.  xi. 269,  where  some  MSS.  express  '  bag-full ' by  xoatel-ful,  others  have  waUt-ful.  Again, Saakespcare  has  ivaliets  for  bags  of  flesh upon  the  neck  (Temp.  iii.  5.  46),  which  is the  same  as  waffles.  Further,  cf.  O.  Da. wattsa^i,  G.  watiOik,  wnzdaaei,  a  wallet, where  tttf/-  ail  swers  lolhc  base  o(A.S,waf-e/.
21480:Willow.  lE)  ME.  wiloiv,  wihae  I A.  S.  welig.  -#-  Du.  wilg.  Low  G.  wilge, Wlmberry  ;  see  'Wine. Wimble  (i).  a  gimlet.  (Scand.^  M.E. u'/w^iV. — Dan.  vim/mi,  a  boring-tool:  of which  the  orig.  form  was  probably  vim/tl* or  ttnm/<l*,  as  it  seems  to  be  parallel  to Dan.  vindiit  as  seen  in  vindeltrappe^  a spiral  staircase.  Cf.  G.  wendtltrtpf^,  a spiral  staircase,  tvendilbohrtr,  a  wimble  or augur.  Prob.  allicii  lo  TWlnd  (a).  Cf. O.  Du.  w^melen,  '  to  pearce  or  bore  with  a wimble;'  Hexham.
```


## [2026-10-17T00:02:31.185Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"urupi\\|urupay\\|raopi\\|raopay\" BRT.txt | head -20; grep -n \"var[əa]mi\\|varamay\\|varənavai\\|varanavai\" BRT.txt | head"
}
```


### [2026-10-17T00:02:31.496Z] TOOL RESULT

```
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
12283:•  j.  tizi.daä-  Adj.  (mask.  'ta-)  'mit scharfem  Gebiss':   urupii  (sd.)   'iahe  V,
20781:—  ayä  ..yayH  kaantl  urvqnS  Y.jj.g;  — ahy/t  *Madahyä  .  .  yä  (ISm.)  karapanö urupayeintl yäcä  ..  duhxsa^rä  Y.4S.J0;
24751:para.iri^yeiti  V.  /j.  50;  —  yat  ahmi  spa- 1  mit  paiti  'mittelbar,  indirekt  in  Beriih- nas^'a  narasca  para.iri>inti  V.6.i;  —  i  rung  treten  mit  -,  Einfluss  üben  auf  -'*> sBnS  vä  para.iristahe  masyehe  vä  V.  G.  \  (Akk.):  cvai  alls  spä  yö  urupis  spmtahe 10,42,  7-24;  —  vJspanqm  ahmya  nmäne\tnaiHy3ui  dämanqm  hqm.rat%wayeiti  cvat fiabänazdisianam  para.iristanqm  ,  .  fravO' \paiti.ra€%wayeiti  "auf  wie  viele  von  den sayB  V.2Ö".7;  —  pasca  /ura./rij/a/r«' Geschöpfen  ..  erstreckt  der  Hund  .  .seinen ma^yeie  pasca  /rasaxtahe{^ä.)  masyehe  V, ;  Einfluss  direkt,  auf  wie  viele  indirekt?"  V, ir).2&;  —  ä  dirn  aoxta..pourvü{%^.iTi  u.)  J.  33.  a)  insbes,  von  ansteckender,  ver-
24960:•  j.  raopay-  ra.  Name  einer  Art  des Hundegeschlechts:  hnu  'pis  (statt  GS.) yaoni>.x''alaAe  hSu  vTspanam  .  .  spaa'hra- nqm  .  .  V./?.  16.
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
26822:paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa  va  na  va  iri^yai  V.Ä  4; '>  5-  39;  —  y^  asiim  upanhanzaiii  sBnS va  para.irittahe  maryehe  vä  y.6.  10;  12, 7.23; —  *näirikayä  hhrpa  ..sunü  kihrpa N.jp;  —  pasvamca  slaoranqmca  masya- nqmca  saiiamla  vayqmca  V.  2.  8; — pasca . .  nasäum  ava.kar>i>nti  spstum  vä  raoz»m va  v>hrk3m  va  V,  5.  5;  6.50;  —  yahöit dim  . .  avaxanan  süns  (NP.)  va  hnß.- ifardvayB  va  V.ö.^s;  46,7.29,  30;  — j/J vä..vay5vä  hn/sji^aroFr'W.li.  A)  mit Bezeichnung  der  besonderen  Art:  spä pasusJtaurvS^''  .  .  spä  vU.kaurvS''''  .  .  spa vohuna^B^^ ..spa  taurunö'''^..spa  sukurmd*''> . .  spa  jaiui^^ . .  spa  aiwinu/'''' . .  spa  vltus''^ ..spa  urupis"'^'  V.  5,  29-33;  —  späntm slidnm  urvUarsm  yim  vat»hapar>m^^  V. 13.3;  —  ys  aSa^qm  sünam  Jainti  yim pa^us.kaurvqmca  viLhaurvqmca  vohuna- sgqtnea  draxtS.hunaranqmia^^  V.  13. 8,  42 ;
7606:•  j.  spastinis  varamis  sispimnö  f»9mnÖ paoiris  iiöiyti'^  Yt. /^.ö?.  Vom  verstUm- j meltes  PPM.  in  der  Bedeutung  'veran- ' lassend',  NSm.  ,
22980:•  j.  varamay-  f.  'Welle':  *Aa^ma  . . sfialtinis  'mis  sispimnff  ^'..vnissMcheWeücn- (kämtne)  emportreibend"  Yt.  19. 67.
```


## [2026-10-17T00:02:37.569Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"urupay-\\|tizi.daä\" BRT.txt | head; sed -n 25520,25530p BRT.txt | cut -c1-500; grep -n \"var- *[0-9]\\|^• *[0-9]*\\. *var-\\|vär-\\|väram\\|vära-\" BRT.txt | head -30"
}
```


### [2026-10-17T00:02:37.962Z] TOOL RESULT

```
12283:•  j.  tizi.daä-  Adj.  (mask.  'ta-)  'mit scharfem  Gebiss':   urupii  (sd.)   'iahe  V,
25526:•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
AbleiL  aus  uru%may-').  —  P&.;  StSii!aSmani/. —  >>  Vgl.  zEild.  ai,  hrinya-  Adj.  'wogend'  ; ürmiy-  m.  "Woge'.
•  j.  umd'wan-,  'iwar-  n.  'Eingeweide, Bauch':  'wan  F._?g;  —  yB  gSus  'wart hqmpnfraiti  (sd.)  V.  4.48;  —  auch  Plur. : astila  gaonala  ^dimohaca  *''wqmca  pah- yasca  fraväxlas^a  YL  /_J.  1 1 ;  —  yB  nars aiaonB  kaca  "wqn  bt/asyät  "der  bei  einem Gläubigen  die  Eingeweide  kurirt"  V.  7. 44(?);  —  alte  äaxma  (sd.)  upanAanzalta an/aräj  naiMät  barp%ri/va  'WBJiva  "die Leicheostätten  soll  sie  (damit)  besprengen innen  im  Mutterleib,   im  Eingeweide"  V.
5. 5 1 .  a)  in  Ubertr.  Sinn  'Kern  (,  Quint- essenz)'": kai  asti  damayh  mazdayas^il ry  "was  ist  der  Kern  der  masd.  Keli- gion?"  V.^.30.
VgL  np.  rüda,  nbal.  rS%  'Eingeweide';  Bthl. IF.  5.  »28.  —  Pü.  (ru  F.):  itamb,  (in  V.  /): an  ddprn  ad,  (sonst):  tranaakr.—  '>S.  *»ra!rya-.
•  j.  umpay-  m.  (auch  mit  ^span-  m.) Name  einer  Art  des  Hundegeschlechts: hau  'pü  (statt  GS.)  HU.äatahe  . .  hau vispanam  .  .  spaci^ranqm  V.  13. 16;  — spä  •pii'V.S.ss'.
El?  FaIschFlCKVglWb.«.5s6.  — PD.:rpnk, nach  DsT.  ZA.  i.  77  für  rddpnk  (s.  lU  na- sujfafya-),  das  er  raipük  liest  und  mit  np. räsü  'WieEcl'  identiliilrt  Diese  Bedeutnng will  auch  GQ.
•  j.  urupay-m.EN.  des  zweiten  iranischen Königs,  eines  altem  Bruders  Yimas,  der ihm  nachfolgt"':  taxmO  °/a  (NS.)  asinavä Yt.75,11;  —  kavann  x'ar»nB  . .  yat  upa- nhaca^  taximm  'pi  (alsAS.)*'  azinavantam .  .  yat  barata  anrim  mainyBm  framittm (sd.)  aspahe  kihrpa  %risattm  aiwi^äma- nam  Yt.  jp.  28f.;  —  ^zainanuhanttm  .  . ya%a  taxmS  °pa  Az.  2.
Eig.  Bed.?  Falsch  DsT.  ZA.  2.  583,  FlCK  BB. 34.  314.  —  •)  Spälcr  Taxmürq/,  Tahtnüras  ge- nannt. —  ')  Man  verlangte  'pim,
•  g.  urüpa'ya-  den.  Praes.  31  '(Schein- bilder,  falsche  Vorstellungen  hervorrufen sva.)  täuschen,  betrügen' "':  *maäaAya  (sd.) yä  angrayä  karapanB  uropayäntl  yäiä xrata  äus»xsa%ra  dahyunqm  ". .  Rausch- Iranks  . .,  durch  den  böslich  die  Karapan und  durch  den  mit  Absicht  die  üblen Herrscher  der  Länder  betrügen"  \.48. 10.
*uripa-  n.  'Scheinbild' ;  ai.  rüpö-  n.  (woto Bgm.  Grdr.» /.  a6o),  räj^yaCj 'imiutur".  — Pü.: rätüitend  pinakXh,  erL :  pänakXh  i  liämän  tu kunind.  Mau  lerlegle  urü-^pay.  —  1)  Anders Gdn.  KZ.  30.  534,  bei  dessen  Fassang  ich jedoch  ein  Objekt  verlangte.
•  j.  urunya-  m,  'Gefäss';  i)  für  den Myazda,  'Schale,  Schüssel':  yailam  taya- nqm  aiaurune  . .  °ya  rai^wis.6ajina  , . V./4.8.  2)  Du.  die  beiden  Gefässe, 'Eimer'  od.  dgl.,  in  denen  den  Rossen Wasser  und  Futter  gereicht  wicd(?):  äpe urvaire  yazamaide  aourvatqm  •/w(AD.)" asavantm     asahe     ratum    yazamaide    G.
4294:PFP.  zum  V.  vär-;    eine  Kontamination 1  PFP.  auf  ania-  und  ya-,  %  20g.  12,   .
5183:Komp.!  *avära-+*nl/rT-,  eig.  'dcb  Kamelstuten -?-  sind';  *av5ra-  Adj,  -?-,  —  ')  Nach  der j'-Dekl-,  Tgl.  syih-asfiT-.
6991:dt'a:  /rasa  frayäi  (sd.)  vahi^jm  ä  ahUm ä  V.  J|V,  29;  —  avi  Um  spayat ..  UmS  äca va^ö  dia  acisUm  Sca  aküm  <J  V,_^.55*>;  — bufvm  ä  ¥.4^.  ß)  'bei,  an,  auP:  iatär^m ä  angrö  (sA)  vs  ,  .  Y,44-i2;  —  dasttum J  vs  gaonavats  (sd.)  N.  ffj;  —  yäka särim^a^''  varsanqm  (sd.)  iarämi  Yt.  5. 77.  b)  zeitlich,  a)  'in,  bei':  tä  yüioyai^S J  rapi'iwifum  ervänam  "die  beiden  kämpf- ten in  der  Mittagszeit"  Yt.ÄaS;  Y.5.11; —  kävanJm  ä  ratüm  Y.g.\;  —  ai  a ^waAmäi  ä^rl  rätqm  n>ma»ia  ..manyai Y. 4.3. 9; —  ä paitiMnitlm  N. 2 (?).  ß)  'bis zu  -'  (nurKompA.;  s.  axlüirjm).  c)  'nach, gemäss':  var^m^a  (s.  *vära-)  Yt.j.iso,  i-].  2, *Y.  10.  \\.  2)  mit  Lok.;  'in,  auf,  a)  auf
7231:3h-  fraiä  fi-ayäi  (sd.)  vahi^fm  ä  akUm a  V.  iS.ig;  —  avi  /pm  spayat ..  e>m3  äea vaisB  ii'a  aastim  äca  ahuin  ä  V,_J.35";  — burum  ö  F.  4  a.  ß)  'bei,  an,  auf:  kalärSm ä  arigrS  {s,A.)  Vil  ..  \.  44.12;  —  dattnsm ä  vä  gaonavats  (sd)  N.  Ö5;  —  ya%a sanm'a^^  varsanqm  (sd.)  barämt  Yt.  5. , 77.  b)  zeitlich,  a)  'in,  bei':  ta  yaiiyaärS S  rapi>win?m  zrvämm  "die  beiden  kämpf- ' ten  in  der  MitUgszeit"  Yt.ÄaS;  Y.9.11; —  häi'anTiii  3  ratüm  Y.  p.  i ;  —  at  3' ^waAmäi  äire  rätam  mmaiihS  ..manysi\ Y.  4J.  9 ;  —  3  paiti-bsTfitlm  N.  2  (?).  ß)  'bis  ! zu  —'  (nurKompA.;  s.  3xtairTm).  c)  'nach,  j gemäss';  vamn^a  (s. ^vära-)  YL 5.1 30,  77. 2,  \ ''Y.  /o.  14.  2)  mit  Lok.;  'in,  auTj  a)  anf
8253:dasin?m  'pa  karamm  aitiha  z^mS  Yt  10. 99;  —  dasin)m  hl  °pa  ars^sm  Vt  10, 100; 1 00';  —  dann?!»  'pa  sraxtim  N.  79 ;  7p';  — dasinqm  (sd.)  °pa  Yt.  13.6$.  7)  'in,  auf {auf  die  Frage  wo?):  a«/  .  .  rämyat  ioa •pa  imat  nmätani  Y.  iO.\;  —  yat  haosrava . .  *Om  kirpsim  (sd.)  'pa*^  tarn.  car?tqm  . . ¥1-/9.77.  b)  zeitlich,  a)  'bis  zu  -': danyimat  aipi  zrväram  "pa  särqm  */rasS.- kirntUn^    ^.62.%.  ß)    'beij    um':    ks
8261:ASn.  ans  *uf,i.äfa-  Adj.  'auf  dem  Wasser  be- findlich', Ableit.  la  upa+äp-,  —  S.  auch  upäpa-, —  pa. :  apar  an  vär-än  i  äp.
15619:•  ').  pairi.vära-  m.  i)  'Schutzwehr,  Wehr'; ta  hl  snaihis  ■vanhas^a  parHasea  *raiia vurntt  pairi . .  dru/aj  Yt  y.  7 1.  a)  'Um- wehrung,  Umwallung':  hahra  nmänä  ava- staya  .  .  /rashmb)mca  (sd.)  fravanmca °r?mla  V.  2.  a6.
15620:ti.  parivära-  m.  'Decke;  Umgebung';  aram. LW.  pareärä  'Vorstadt';  FrMÖllbR  WZKM. S.  97.  —  Pü, ;  pirämin  farvär.
16070:Brücke  des  Scheiders'  (beim  letzten  Ge- richt): Ayat  aüT^gpirun  yd^rä  ^vatJ  °tui "wenn  sie  dahin  kommen,  wo  die  Brücke des  Scheiders  ist"  Y.4Ö".  11;  —  frS  toii vispsis  cinvats  frafra  (Sp,  851  m.)  'tum \.46. 10;  —  tarS  änvats  °tSm  Y.  71. 16, V.  7p.  30;  Vr.  7.  i;  — yeiya  urvä  xraodaUl änvatJ  'tä(l£,.) aia(s��)Y.5i.i3.  a)dn. auch  ohne  cinvatB  'die  Brücke'  Kar'  i^,: hrlicit  (Sp.  591  m.)  tarS  'tümcit  la  urväram vahistfm  aÄsm  frapärayem  Y.  ig.  6.
16491:•  j.  baevarfl.vär-  m.,  Flur,  'zehntausend Regentropfen'(?):^(i>'i»'<i  äunma ..upa.apjm Aazanrö.varayö (sd.)  -värascii (NP.)  V. 21.%.
17853:ai,  pravära-  m,  "Decke';  np.  fars'är  'Veranda'.
23456:»vär-
23487:KompE.;  Ableit  —  Vgl.  'när-  md'väray.— ai,  vär-  r.  'Wasser",  np.  Sär-än  'Regen'.  — Pü. :  värän.  —   i)   Hds.  vate,  s.  aber  Pü.
23488:•  j.  "vär-  V.  'regnen',  persönL  und  unpers. Praes.  2  vSra-,  30  (Her.)  väraya-.  —  PFP, 'va/yrUya-.
23496:•  j.  ^vära-  m.  'Deckung,  Wehr". KompE.  —    Zum  V.  t-var:  —  ai.  'vära-  m., np.  bära  'Wall',  'vär;    %.  HBU.  AGr.  /.  226.
23497:'  j'i  K-  "vära-  n.  i)  'Willen,  Belieben': masäa  aia  xsmäk^m  'nm  xinaostmnS  (sd.) Y.4Ö'.  18;  —  yasia  hdi  'rat  rädat  (sd.) y.  5/.  6 ;  —  tsi  'rät  räthntJ  ahurahyä  taosi matdh  "die  erfüllen  den  Willen  des  AhM. zu  seinem  Wohlgefallen"  Y.^.  a;  —  AS. mit  °a  (vanma)  als  Adv.  sbes.  a)  'Aus- lese' (nur  vAbleiL).  (Y.  to.  14:  lies vär7ma.\
23504:D.i.  var)i?i(AS.aa*>vära-)+'a;  BtHL.  GlrPb. /.  122,  S  ^V  No.  —  Vgl,  aL  vdram  a.  —  Pü. : Ai.'narnm  mit  NpüErL:  Jil;  s.  Dst.  ZA.  /. 105  No.  42.
23513:•  j.  vära-gan- :  °jn-  m.  Name  eines Vogels'*:  afimäi  .  .  ajasa^  vazfmnS  v»r»- %rayne  .  .  niirr/ahe  kthrpa  •ynake'''  . . yS  vayam  aiti  asUtS  Yt.  i^l.  19;  —  lusai il'arynS  yimai  kaca  . .  mirriahe  kthrpa -ynahe''^  Vt /p.  35.
23514:Vgl.  värin-gan-.  —  Eig.  Bed.?  Man^  hat  den Vogel  Damen  mit  'flügelschlagend'  überaetit nnd  für  *3i'J/'-  auf  np.  fj/ 'Feder,  Flügel'  nnd ai.  J-äta-  m.  verwiesen;  5.  Sp.  Komm.  3.  1Ö4, Heu.  KZ.  27.  607.  Aber  ai.  vära-  bedeutet 'Schweifhaar',  bes.  des  Kosses  (wie  lit.  ialtd), und  np,  bäl  ist  vielmehr  gleich  ai.  barha-  [v') 'Schwan ife der"  lu  seWen,  Ander»  jetii  Richtir IF.  p.  185.  —  Npü.:  fehlt.  —  II  Welche»? Falsch  Dst.  ZA.  z.  566;  vgl.  Hbm.  PSi.  87. HoRN  GlrPh.  7  b.  56.  —  '}  Them.
24259:•  j.  vi.vära-  n.  'nach  allen  Seiten  strömen- der Regen':  vwannti  (sd.)  'rahu'^  V, 2/.  3.
24260:Zu  'vär-,  —  Fa.!  0/7  Aaf  an  värän.  —  t)  Nach der  J-DekL,  S  4'3.  3d.
25354:Zum  V.  rä%-.  —  Vgl.  rä%man-.  —  Pü. :  ioAr, SO.:  dänam,  dväram.  —  ')  Statt  'mSi,  weil  y' folgt.    Zwei  minderwertige  Hds.  bieten  wiilc-
26214:Eig.  'Kopfbedeckung' ;  *vära-  m.,  zum  V.  'vor-. —  mp.  sämär;  arm,  LW.  laiavarl,  TgL  Hbm. AGt.  I.  335.  —  Pü.:  iirvär,  erl, :  tarai,
```


## [2026-10-17T00:02:43.154Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"V\\.  *'umhüllen\\|'bedecken\\|'wählen\\|'glauben\\|'wenden\\|'drehen\\|Ordal\\|Gottesurteil\" BRT.txt | cut -c1-300 | head -30"
}
```


### [2026-10-17T00:02:43.415Z] TOOL RESULT

```
3646:Pü.:  dnddtdd.  —  0  Die  beiden  Stellen können  ursprunglich  nicht  den  gleichen  Wort- laut gehabt  haben.  An  der  1.  Stelle  wird  etwa gestanden  haben:  Wer  eines  Verbrechens  be- zichtigt wird  und  leugnet ,  soll  das  Ordal- wasser  trinken.  An  der  2.:  Wer  das  Ordal- was
7152:"^raoitS  (sd.)  V,  46. 7  •'.  a)  vom  Opfer- feuer: at  a  ^wahmäi  '%r!  ratam  iiima- t>hs  .,  asahyä  mä  ..  manyäi  (sd.)  Y.  47- 9.  b)   vom   eschatologischen   Ordal-
7927:*)  Die  Worte  beziehen  sich  auf  das  Wohl- gefühl des  Gerechten  und  die  Pein  der  Gott- losen beim  Durehschreiten  des  glühenden  Metall- stromes im  letzten  Gericht,  wovon  Bd.  jo.  19 eriihlt;  s.  aj-ai-  A  und  'ä/ar-  3  b.  Pii.  erl.: /äi-  am  fa  pasäxl  i/aiiiri  tu  ö
9157:—  yat  {mafiatum')  kjnniiun^^^  amtSa. spiiita  (ahc)yti ..  YLiO.  51;  —  hqmJaptibyS aiwyö  cäxrare'*'  (3PPfM.)  nfnbyö  "mit heissem  Wasser  stellen  sie  es  (das  Ordal) an  den  Männern  an"  V..;.  46.  5)  'Je- manden, etwas  (Akk.)  machen  zu  -' (Akk.):  II  hy^  durayaf'Ti^um  
9833:l'Q.i  hac  dtüin  afiar  vailat  (gescht.  i'')0  hae fiixai')  i  silTiar  "rechls  auf  dem  EückgtBl  0 beim  drillen  Wirbel" a).  Vorher  steht:  apar\ buland  fa  sar  i  kSf  "oben  auf  der  Spitze  des , Höckers",  —  >>  Zu  vaslan  'drehen',  rgl.  lat. virUbra.  —  ")  Eig.  'Knote
14131:(Sp.  251  u.):  asaonS  ahmi  'vatö  nöit  ahmt Y. /O.  16;  —  fradahäi  vTspayä  alaonS stöis  hamistSe  vupayh  'vatö  j/Si'/ Y.52.4; Ä  8.  10)  von  ajidem  Schöpfungen  der dafiAschta  Welt  'glaubensfeindlich,  ruch- los'; pairi  'valal  mahrkäl  pairi  °vatai a^mät  pairi  drvafhyö^''
19204:*mvaila>ka-  Adj.,  Ableit  aus  'ni-vaila-  Adj-, PPfP.;  VgL  mp.  vaJian,  np.  gajtan  'drehen'; s.  dazu  Bthl.  IF.  4.  i^i,  Hbm.  PSt.  197,  —
19731:tSm  Vi  ala  mjAmaiäl  *htiJtaxaim  (sd.)  Y. 4lS-  ij;  —  sptutjm  ai  %wa  maxdä  nOngkl oAwa  hyat  . .  "als  den  Heiligen  erkannte ich  dich  da,  o  AfAi^  als  . ."  Y.4j.  5; —  atfmcti  akyä  masda  ^wam  mfAAr foMtrDim  vaBi»m{sA.)  Y.2g.  10;  —  matdä yasmmla  vakm^mcä  vafditi
22756:ai.  vfmlt  >er  wählt',  vpfuli,  varal,  avj-la,  vu- rila;    np,  giravTJan^);    oosi.  wmin  'glauben'.
22809:•  j.  'varah-  n.  'Probe,  Prüfung,  Ordal'*': urvdhqmcit  (sd.)  zbayem  avi  imai  TS uzdatTm  aviätnmca  bargsmäca  avipfnnqtn vjyzarayeintTm  avi  raoynyqm  varauhsm (sd.)  aeui/rmca  urvaranqm  ".  .  zu  dem hier  angestellten  Ordal,  zu  dem  Feuer  und Bansman,  zu  der  Uberfliesse
22810:♦)  Vgl.  DsT.  ZA.  2.  492-  liber  die  Ordale handelte  nach  Dk.  S.  42  ein  besonderer  Ab- schnitt des  iS.  Naiia  des  Awesta,  das  Varaslän. Über  die  verschiedenen  in  mp-  Schriften  ge- nannten Ordalarten  s.  SBE.  5,  iS,  57  im  Index unter  'Ordeal'.
22811:KompE.  —  Eig.  'Beglaubigung,  Erhärtung' des  Rechts,  der  Unschuld;  lum  V.  'var-,  — Vgl.   yvaroA:    —    mp.  (Pü.)   z«ir  'Ordal'.    —
22813:Ordals  gemeint.
22814:•  j.  ^varah-  Adj.  (auch  fem.)  'beim  Ordal verwendet,Ordal-';  urva%qmäti.%d^ zbayemi avi  imatvarS{%A.^uzd3t>m.. avi  raoynyqm 'ranhim  (AS£)  ". .  zu  der  Ordalbutter" Yt  12.  z*\
24136:•  j.  vi^Savant-  Adj.  (fem,  'vaiti-)  'die  Er- mittlung der  Schuld  bewirkend',  vom  Ordal- wasser:  äpfm  saoknUavaitltn  taranyävaiilm ..  a/>3ihis  isd.)  ..  V.4.54-
25828:np.  saagand  (mit  auffälligem  a«)')  xurdan 'den  Eid  leisten',  eig.  'das  5cliwefel(wasser) trinken,  d.i.  sich  dem  Ordal  unterziehen';  s. dazu  GlrPh.  a.  1^4.  —  Pü.:  göiirl{'=-  np. gaugird^maitd.  —  i)  S.  dazu  Hbm.  PSt  77, HoKN  GlrPh.  I  b.  39.
```


## [2026-10-17T00:02:59.684Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:2373 BQT:1137 BQT:1797; do echo \"=== $r\"; timeout 300 python3 tools/ref_page.py $r --image 2>&1 | head -80; done"
}
```


### [2026-10-17T00:03:16.111Z] TOOL RESULT

```
=== BQT:2373
(no exact page map; using offset -1917 -> pdf page 456; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2373.png
REF: BQT:2373  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 456  OCR-lang: fas

-۳ پوس همیان
آبند کان مخلوقات وخوجودات هم همت . همو ‌آره؟ - با واو بر وزن انگاره :
همو ای؟ - باواو بالف کشیده و برای | بمعنی پیوسته وهمیشه ومدام باشد.#
قرشت زده ؛ مغروف است که بمعنی‌براپر وبيك ٍ همیان* با بای حطی بروزن اببان؛
طریق ومساوی باشد - وبمعنی همیشه ودایم هم | کینه‌ای باشد طولانی که بر کمربندند و بغربی
۱ - هم شین تو ازتو به پاید تا آر! عقل و دین بیفزاید.
« امتال وحکم دهغدا » .
۴ هاموار* همواره ۳ هامواره » پهلوی 1877۷2۲ * منای ۲۷۹ ۰ « اوئوالا
۱ 19» کردی ع 861۵۷۵۴ (مساوی, متحد). ۴ - هموارکردن, تحمل کردن:
این درد " نه دردیست که بیرون رود از دل این داغ نه داغی اآسمت که هموار نوان کرد.
صالب تبریزی « فرهنگه نظام » ۰
۴ هموار* هاموار * هامواره :
کرهمی خواهی که با معشوق درهودج بوی با عدو و خصم او همواره در محمل مباش.
«سنائی غزلوی؛ دیوان ص ۰۹۵۸
8 «هامیان ۳ امیان ۳ آمیان, درعربی « همیان, بالکر , ازاربند و کیبه ای که در
آن درم لهند. پارسی است ومعرب.» «منتهی‌الارب»» ورك: دزی جاص ۰۷۹۵ کردی هعنذصه‌ط
(همیانی که درآن پوزنهند) » ژابا اصل اوستایی آنترا 818188128 داند * ژاباس۱ 40 و اسشق
ازاوستایی -1 9۵۳3-۳2 (کمربستن). فس. اوستابی2 81۷۷9200188 ( کمربند) « اسشق
۵ هوبشمان این‌وجه اشتقاق‌را قطمی نمیداند «هویشمان ۰.۱۱۶۵ :
0 همه - بفتح‌اول ودوم(درنلفظ کنونی بکسردوم)؛ ابرانی باستان 012810868 دنیب رکه
س۹۳ -87۳8 (خمه ‏ تمام) » هندی باستان - 82826 » پپلوی 1187808۳ «اسشق ۰۶۱۱۶۳
6 (هر, همه. تمام) «ثیب رک ایسا» «هوبشمان ۱۱*۳ «منای ۹۲:۲۷۵ » 12126 «منای
۹ ۶ نأوادیا ص ‎0٩‏ بند ۷۲ متن و حاشیه » و دراه : اس ۱ .۰ ۳۱۱ 40 پازند ۳872
«هوبشمان‌ایضاً ». بلوچی 88008, 880086 ۰82706 امشق ایضاً *. کردی 16000 «اسشق
ایا ۰ ژابا ص 240۱ ؛ تدام » جمیح افراد : «اسماعیل بن‌موسی که ملجاً همه خوارج بو دکه از
عرب آمده بودند پایعقوب حر بکرد. » «تاریخ سیستان: ص۲۱۳ کل يك‌فرد» سراسر: « وهمةٌ
شب نماز میکردند ( مصطفی ص وباران ) عرچند که واجب بربشان نيمه شب بود با مه يك و با
دوسه يك بر تخییر...» «میبدی. کشف‌الاسرار ج۱ص4۸>. راجع بقواعد استعمال همه. ر4: اضافه
0 همی - بفتح اول وباه مجپول 11276 (درتافظ کنونی 201 5) پیشوندفعل» پهلوی
3822 , پازید132206 ۰ اسشق- هوبشمان ۱۱۰۶؛ اين‌پیشوند. برسرفعل ماضی, امضارع وامن
درآ ید: همی‌رقت» همی‌رود. همیرو . برسرفعل ماضی معنی استمرار دهد :
زخارا گهر جست يك رو زکار (جمشید) همی کرد زو روشنی خواستار .
فردوسی طوسی «شاهنامةٌ بخ جاص ۰۲۵
ور: ص‌لد آزد‌يباچهٌ موْلف. گاه رورت شعر پس ازفعل آید :
بری جوی مولیان آید همی باد ار مهربان‌آید اهمی .
رود کی سمرقندی «چهارمقاله: طبح دوم نگاریده یو

=== BQT:1137
no scan of BQT covers printed page 1137 (see 'scans' in refs_online.json)
=== BQT:1797
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1797.png
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


## [2026-10-17T00:03:25.077Z] TOOL CALL #23: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2373.png"
}
```


### [2026-10-17T00:03:25.609Z] TOOL RESULT

```

```


## [2026-10-17T00:03:25.606Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:03:32.447Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; cat > ocr/BQT/2373.vision.txt <<'EOF'\n[BQT printed p. 2373 (vol. 4, picofile pdf p. 456), read from the page image]\nهموار ۲ - باواو بالف کشیده و برای قرشت زده، معروف است که بمعنی برابر و بیک طریق و مساوی باشد - و بمعنی همیشه و دایم هم هست ۳.\nهمواره ۴ - با واو بر وزن انگاره، بمعنی پیوسته و همیشه و مدام باشد.\nFootnote 2: هاموار = همواره = هامواره، پهلوی hamvâr «مناس ۲۷۶»، «اونوالا ۳۰۱ bis»، کردی hemvar (مساوی، متحد). ۳ - هموار کردن، تحمل کردن ...\nFootnote 4: همواره = هاموار = هامواره ...\nEOF\nfor f in incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt; do echo \"== $f\"; grep -n \"گربه\\|طهمورث\\|تهمورث\\|^ *وار \\|دربار\\|بَرم\\|برم -\" $f | head -12; done"
}
```


### [2026-10-17T00:03:33.394Z] TOOL RESULT

```
== incoming/BQT/BQT_v3_pages.txt
407:که از حیوان شبیه بگربه حاصل میشود و ‎OT‏
457:و دراز 6 - و گربه کردن بسیار باشد.
3135:شتر گربه کوبند که در غابت بلندی و بستی
7242:Jie ‏کلك اوبخندد‎ tas, ‏زگربه‎ - ۴
8740:فارسی در آمده است ‎«٩‏ نفيسي . دربارء ‎ute‏ لفت فارسی ۰ ‎Galak‏ پوردارد جاص ۲۲۹.حدی
11564:طهمورث ۴ ‎ie‏ پادشاهی بود از
11755:ودمیدن ضی صورت گیرد . دربارة ابدال اين حرف » ‎By‏ : لخت نامه.
14278:‎she‏ خرخربرا گوبند که بمب گربه کردن با
14281:حزین وآواز ترمی باشد که درحالت گربه کردن
15132:‏مکن غلمج مرا از بهر خنده که چشم از ‎oe‏ تو درگربه دارم .
21664:« رشیدی » درعربی فنك بنوعی ببار کوچك از روباء . ببزرگی گربه , اطلاق شود وآن‌درنواحی
23304:‏دربارة اين‌کلمه حدسهای مختلف زده‌اند . مار گلیوت ‎D.S- Margoliouth‏ درپاسخ
== incoming/BQT/BQT_v4_pages.txt
92:ادب دوستان مخصوصا دربارة لغات مربوط بلهجه ها محلی
288:دربارهٌ مطالب مجلدات چپارگانة برهان قاطع مستقیماً به عنوان نگارنده
531:قرشت » کنایه ا زگربه کنندة بسوز است پمنی مادده ؟ - بکر ثاك و فتح رابع,نام
826:فی‌بادی باشد که موش در وقتی که گربه را بیند ماس - بروزن طای » مخق فآمای‌است
1643:وار ( پوند بت و اتصاف ) ۳ ماهواره « رشیدی > . فی : ماهیانه .
2969:۷-۹ .۰ م.م. ‎ )‏ دربارة نوع قبر (کور ) مفهوم ا زکلمه ؛ استاد هنینگه پس ازیحثی » بهترین
5379:بعربی قاره میگوبند ۱ - وبا تانی‌مجپول» گربه موشگر ‎٩‏ (۱) - با نی مجهول وکاف
5383:معدوله‌پروزن هوشیارء, لت ناه َ اد تا زنان دیگر آنرا شنیده بگربه و موبه
5570:* رشیدی > . ‎٩‏ - پهلوی ۵46181 ( ناله وزاری » شکایت » گربه ) ۰ ابرانی باستان
5897:مهر ) از : مهر(.م.) ۳ گان ( پوند بت .که درباره جشنها نیز بکار میرفته » فی:آبانگان,
5946:پدربار شاهنشاه هخامنشی هدیه می‌فرستاد . اردشیر پابکان و خسرو انوشروان درین روز جامهٌ
6835:که از مقر عیش و اعشرت ملاطین بغراطی - که در دربار شروان ظاهراً شهرت داشته است -
== BQT_v1_pages.txt
242:که زرتشت بدربار شهریار آنجا گشتاسب پناه برد و دینش نخست در
557:استاد بو نیست اصلاه‌ادی‌است ؛ چه دربارسی باستان میبایست بصورت «بره
1042:مدائن است و کساننکه در دربار شاه بودند بدان ستن میگفتند ۰ س آین
1057:٩‏ الفهرست. چاپ‌قاهره‌ی٩۱.  *‏ دربارة «فارسیه» اول‌وهفارسيه "دوم‌بحث‌خواهيم کرد.
1093:سربانی ولغت درباری که ازآن بدری تعبیر هیکنند » اکتفا کرده‌اند . » وفرهنگه نوسان نیز از
1130:وری منسوب است‌به «در> بمعنی‌دربار » چنانکه ابن‌المقفع وحمزه
2781:سلیمانی رفته واو نیز دربار جپانگیر را درك کرده است ۰
2801:د - سخنی چند دربارة برهان قاطع ۱
2812:عظیم کنب شمر ودیوانهای اساتید نظم در دربارا کپر وشاه‌جهان وجهانگر
2996:اول»در گاه و آمتانةٌ خانه را گویند» آمده وآن صحیح‌امت وذ کر ختح‌اول برای آنست که دربارء
3029:۱- بفاعد قَل الفاظ بونانی حرف اول‌آنرا نالعم مبتوان نوشت- (فیجی. دربارة چند
3149:خود که دربار انواع طعامها وغذاها برسییل طیبت سروده , فرهنگی برای‌اغذیه ترقیب داده است
== BQT_v2_pages.txt
34:‫دربارة لغات مربوط بلهجه‌های محلی وشاهدهای شان ونادر مرفوم‌دارند‪ .‬چندتن دعوت‌وبرا‬
63: ‫کرده‌اند‪ .‬تقدیم میکند وازخوانند کان درخواست دارد که اطلاعات خود را دربار؛ مطالب‬
344:                            ‫بلوچی ‪ 2۰‬کیلکی ‪ [882‬؛ بجای ‪ ....‬بمعنی درحق ‪ ...‬درباره ‪...‬‬
3455:    ‫‪ - ۴‬بهر دومعنی » حانظ دربارٌ امیر مبارزالدیین محمد ومیل کشیدن چشمان وی بامر‬
4251:                            ‫وچاته زدن بمعنی گفتگو با فروشنده دربار؛ بای چیزی‌است‪.‬‬
7473:      ‫ببلطنت برسید اورا بدرباراحضار کرد و وعدة مقامات ارجمندداد » اما ار پپذبرفت » خسروبجنث‬
9168:  ‫وی بدربار خاقان اکبر منوچهربن فربدون شروانشاه اختصاص داشت و نخلص او از عنوان همین‬
11594:     ‫‪ ),‬چك ‪ ۰‬چش‪ :‬خرلجای ‪.‬‬                  ‫(ه) چك » چش‪ :‬بگربه ‪.‬‬                   ‫(‪ )4‬چش‪ :‬هاله ایست‪.‬‬
11675:‫باگربه باشد‪ -‬وبانگه بی گربه رایز کویند؟ ‪۶#‬‬                             ‫نیزگوبند که فر دهن فرح زنان میباشد و آبرا‬
13886:      ‫(فیسی ‪ :‬دربارة چند لفت فارسی‪ .‬بادنامةٌ پورداود ج ‪ ۱‬ص ‪ )۰۳-۱۳‬و ممکن است ( خاریشت)‬
14972:                          ‫آرا تصرف کند ‪.۴‬‬          ‫اشزبآان بازجایی دیگربهم نمیرسد » چه گویند‬
15033:‫خون دل ناخن آوردلست که کنانه از گربه‬                          ‫خون‌جبال ‪ -‬کنابه از لعل ‪ -‬و‬
```


## [2026-10-17T00:03:36.347Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11550,11600p incoming/BQT/BQT_v3_pages.txt; grep -n \"pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<11564' | tail -1"
}
```


### [2026-10-17T00:03:36.813Z] TOOL RESULT

```
‎Lg a ۱‏ دراوستا ‎LG ( Tumaspa‏ در اوستا * فروردین بشت بند ۱۳۱ ‎dL‏
‏شده ) مر کب از ‎Cuma‏ ( زورمند) ۳- اسپ(اسب), جمعاً دارند اسب زورمنه با اسب فربه . ناه
‎by‏ طاء درین بام پاید نم تلفظ شود و علت آنکه آنرا بت خوانند نظر بتاء در نامهای تهمتن
و رستهم ( ‎cer‏ ) و کتهم است . اما نهم درین سه بام از ‎CAR‏ آمده که بمعنی دلیر
ویهلواست. ‎Ne?‏ ص ۲۲۸».

‎. le #4) - ‏طهرای‎ *

[pdf page 156]
2۱۳۹۱۳

بخشید و پنجاء سال پادشاهی کرد ۷ .

طهمورث ۴ ‎ie‏ پادشاهی بود از
بیرهای هوشنکه . کوبند ابلیس را م کوب

ob

ساخته ‎oy‏ و سوار ميشد و مدت پادشاهی او را

بسنی سی‌سال و بسضی هزار سال لوشته‌اند.

بیان دوازدهم

در طای بی ‎Labs‏ بای حطی

‎Lb‏ = بنتم ‎Jo!‏ بر وزن ‎Le‏ » بلفت
پونالی نوشادر پیکالبرا گریند , و ‎OT‏ چیزست

‏طیاره ۴ - بروزن ‎ale‏ کنتی‌وجهاز
تیزرو را کویند .

‏طیاف « بکراول‌بروزن غلافسنگینی
وکرانیی‌را کویند که‌درخواب برمردم افتدوبعربی
کابوی خوانند ۴ .

‎olb‏ © بفتح اول,بروزن خزان , باسمن
صحراییر اکوبند وآن مانند لبلاب بر یکدییگر

‏مشتمل برهیجده لغت ‏ و کنایت

‏پیجد ‎py‏ شاخهای ‎OT‏ خار میباشد ‎OF Nestle‏
‎yl‏ بعربی عشبة النار خوالاد.

‏طیره * - یک اول بر وزن خیره »
خجلت و خجالت- وخجل را گوبند - و بمعنی
آزردکی هم آمده است - و در عربی بمعنی‌فال
بد باشد - و بفتح‌اول هم درعر بی بمعنی‌قهروخشم
باشد ۷ .

11559:[pdf page 156]
```


## [2026-10-17T00:03:39.178Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 11600,11640p incoming/BQT/BQT_v3_pages.txt | grep -v \"^$\""
}
```


### [2026-10-17T00:03:41.296Z] TOOL RESULT

```
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
‏میکرد ...» « چپار ‎peat Gone lie‏ ۰۹۹ .
‎toe ‏بدرجهای شید که هره-اعت‎ Gat
‎Age) ‏طیسفون » < پسفون‎ « mee. ۷
[pdf page 157]
طیسه = پنتح اول وسین بی‌شطه » بستر
و بالين را گویشد .
‎Olan‏ - با ‎oth‏ حطی تالی بر وزن
‎OOS‏ » بلفت سریالی ‎SUAS‏ صحراییرا کوشد
وحربی ‎oy AS‏ خوانند ‎٩‏ .
- طیطاو ۲ - با ای حطی بروزن ‎ied‏
‎ey‏ از مرغابی باشد؛ وطیتو ‎ps‏ کنته‌اند کسلای
دوم ای فرشت ‎ath‏
```


## [2026-10-17T00:03:44.136Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"تهمورث\\|Taxma\\|taxma\\|urupi\" BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:03:44.470Z] TOOL RESULT

```
32031:که او وا تهمورث دیو ند می خوانند؟ ت ورنفی
32059:۵ تهمورث - رك : نهمورسی .
```


## [2026-10-17T00:03:46.316Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"pdf page\" BQT_v1_pages.txt | awk -F: '$1<32031' | tail -1; sed -n 32020,32075p BQT_v1_pages.txt | grep -v \"^$\""
}
```


### [2026-10-17T00:03:46.636Z] TOOL RESULT

```
فردوسی طوسی» گفتار رستم باسفندیار .
و کوبروارمفرب بقزوین وساوهطول آن ازهشرق‌بمغزب (غر قآ باد تا فدروژ کوه) ۲۹۰ وعرض‌ازشمال
بجنوب (ا زگردنة کندوان تا درباچهُ ق) *۱۲ کیلومتر و صساحت آن فربب ۳۱۰۰۰ کیلو متر
مربع است. شهرتهران پابئخت ابران دربن ابالت است. درفدیم نهران عکیاز فربه‌ه‌ای کوچكری
بوده» اصطخری وابن‌حوفل ومسمودی نام‌تهران را در کتب خود ذ کر کرده‌اند. «جقرافای سیاسی .
کیهان ۳۱۱- ۳۹۹. درسال ۱۲۱۰ آغا محمدخال قاجار آنرا باشخت ابران فرارداد . جمیت
نپران قوب ۱۰۰۰۰۰۰ نن است. راجم‌بوجه اشتفاق نهران وسور مختلف تلفظ و کتابت آن» رك:
بقبه درصفحةٌ ۰۳۹تهمك - بر وزن لك لك , مصفر تهم
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
دوم شمارء 4۰۷۰۱قی ۱ ع یکسر اول و سکون ثالی :
مخفف تهی است که خالی باشد .
تیان اف قون مان دگتن کل
بز رک راگوند ؟ » چه تبانچه دبگ سر کشاده
کوچك باشد .
لیس باثانی مجهول» بر وزن ومعنی
سیب است که عرب تفاح کف 2 و دمعتی
سر کشته ومدهوش و بی‌فرار وشتاب زده همآحده
ات
تییا؟ پر وزن زببا » بزبان زند
و بازد(۱) آهو را گویند » وبتازی ظبی‌خوانند.
لیباش » بسکون شین فرشت ۰ نزه
```


## [2026-10-17T00:03:51.507Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py"
}
```


### [2026-10-17T00:03:52.020Z] TOOL RESULT

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


## [2026-10-17T00:03:53.286Z] AGENT

Fetch and archive the web sources, then read the relevant etymology sections.


## [2026-10-17T00:03:58.265Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 541: $2\" 2>&1 | tail -1; }\nf 'https://en.wiktionary.org/wiki/گربه' 'Wel 2, gorbeh etymology'\nf 'https://en.wiktionary.org/wiki/تهمورث' 'Wel 2, Tahmuras'\nf 'https://en.wiktionary.org/wiki/روباه' 'Wel 2, rubah < raopi-'\nf 'https://en.wiktionary.org/wiki/بار' 'Wel 3, bar time/court'\nf 'https://en.wiktionary.org/wiki/-وار' 'Wel 3, -var suffix'\nf 'https://en.wiktionary.org/wiki/هموار' 'Wel 3, hamvar'\nf 'https://en.wiktionary.org/wiki/دربار' 'Wel 3, darbar'\nf 'https://www.etymonline.com/word/wallet' 'Wel 3, wallet'\nf 'https://www.etymonline.com/word/willow' 'Wel 3, willow'\nf 'https://www.etymonline.com/word/walk' 'Wel 3, walk'\nf 'https://www.etymonline.com/word/well' 'Wel 3, well n.'\nf 'https://www.etymonline.com/word/Adolph' 'Wel 2, Adolph'\nf 'https://www.etymonline.com/word/helix' 'Wel 3, helix'\nf 'https://www.etymonline.com/word/valley' 'Wel 3, valley'\nf 'https://www.etymonline.com/word/revolve' 'Wel 3, revolve'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wel-' 'Wel 3 root'\nf 'https://en.wiktionary.org/wiki/Adolf' 'Wel 2, Adolf'"
}
```


### [2026-10-17T00:04:03.901Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/41c12e9add3278f9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ff869a5c1356b51d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3dcdc6992a175401.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/49747c621585df37.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44253677b535d01d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e4e8a6f28a70487.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b0a7e91b51bc0362.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ef5d2fcf9ba38425.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1f6aaf2799bc2f3a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d09e83b8d8b02ef6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6f9c8a679c9b2b0d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bc31844728c8313a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3a580c1ff13e26bf.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ee2a8513ad872b82.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cf713de84bfed466.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3670be14f5c84a56.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a4e7fabbff16daed.txt
```


## [2026-10-17T00:04:06.263Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for h in 41c12e9add3278f9 ff869a5c1356b51d 3dcdc6992a175401 49747c621585df37 44253677b535d01d 3e4e8a6f28a70487 b0a7e91b51bc0362; do echo \"=== $h\"; grep -n -A6 \"^ *Etymology\" $h.txt | head -40 | cut -c1-500; done"
}
```


### [2026-10-17T00:04:06.863Z] TOOL RESULT

```
=== 41c12e9add3278f9
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
187: Etymology
188- [ edit ] 
189-
190- From Middle Persian [script needed] ( gwlbk' /⁠gurbag⁠/ , “ cat ” ) , from Proto-Iranian *wr̥pa-ka- , [ 1 ] ultimately from Proto-Indo-European *h₂wl̥pís . [ 2 ] [ 3 ] Compare Lithuanian vilpišys ( “ wildcat ” ) , Latin vulpes ( “ fox ” ) . Perhaps anciently related to روباه ( rubâh , “ fox ” ) ; see there for more.
191-
192- Pronunciation
193- [ edit ] 
=== ff869a5c1356b51d
=== 3dcdc6992a175401
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
175: Etymology
176- [ edit ] 
177-
178- From Middle Persian [Book Pahlavi needed] ( lwpʾh /⁠rōbāh⁠/ , “ fox ” ) , from Old Persian *raupāθah ( “ fox ” ) , from Proto-Iranian *Hrawpācáh . Cognate with Baluchi روپاسک ( ròpàsk ) .
179-
180- Pronunciation
181- [ edit ] 
=== 49747c621585df37
62: Etymology 1 
63-
64- 1.1.1 
65- Verb 
66-
67- 1.1.1.1 
68- Conjugation 
--
71: Etymology 2 
72-
73- 1.2.1 
74- Noun 
75-
76- 1.2.1.1 
77- Declension 
--
80: Etymology 3 
81-
82- 1.3.1 
83- Adjective 
84-
85- 1.3.1.1 
86- Declension 
--
89: Etymology 4 
90-
91- 1.4.1 
92- Verb 
93-
94- 2 
95- Gulf Arabic 
--
100: Etymology 
101-
102- 2.2 
103- Pronunciation 
104-
105- 2.3 
106- Noun 
--
=== 44253677b535d01d
=== 3e4e8a6f28a70487
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
--
148: Etymology
149- [ edit ] 
150-
151- Inherited from Middle Persian [script needed] ( hamwar , “ level , abreast ” ) [ 1 ] , Northern Luri هومار ( homar ) .
152-
153- Pronunciation
154- [ edit ] 
=== b0a7e91b51bc0362
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
79: Etymology 
80-
81- 2.2 
82- Pronunciation 
83-
84- 2.3 
85- Noun 
--
158: Etymology
159- [ edit ] 
160-
161- From در ( dar ) + بار ( bâr ) .
162-
163- Pronunciation
164- [ edit ] 
--
245: Etymology
246- [ edit ] 
247-
248: Etymology tree
249-
250- Classical Persian در ( dar ) 
251-
252- Classical Persian بار ( bâr ) 
253-
254- Classical Persian دَرْبَار ( darbār ) bor.
```


## [2026-10-17T00:04:09.961Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n \"Persian\\|time\\|Etymology\" 49747c621585df37.txt | sed -n 1,200p | grep -i -n \"persian\" | head -5; awk '/^ *Persian *$/,0' 49747c621585df37.txt | grep -v \"^\\s*$\" | grep -i -B2 -A4 \"etymology\" | head -60 | cut -c1-400; echo ====; head -c 3000 ff869a5c1356b51d.txt | tail -c 1200; head -c 2500 44253677b535d01d.txt | tail -c 800"
}
```


### [2026-10-17T00:04:10.299Z] TOOL RESULT

```
Exit code 1
8:148: Persian 
9:150: Toggle Persian subsection 
30:1343: Borrowed from Classical Persian بار .
31:1367: Persian
32:1370: Persian Wikipedia has an article on: بار 
 Pronunciation 
 6.2 
 Etymology 1 
 6.2.1 
 Verb 
 6.2.1.1 
 Derived terms 
 6.3 
 Etymology 2 
 6.3.1 
 Noun 
 6.3.1.1 
 Synonyms 
--
 Descendants 
 6.4 
 Etymology 3 
 6.4.1 
 Noun 
 6.4.1.1 
 Derived terms 
 6.5 
 Etymology 4 
 6.5.1 
 Noun 
 6.5.1.1 
 Derived terms 
 6.6 
 Etymology 5 
 6.6.1 
 Noun 
 6.7 
 Etymology 6 
 6.7.1 
 Noun 
 6.8 
 Etymology 7 
 6.8.1 
 Noun 
 6.9 
 Etymology 8 
 6.9.1 
 Noun 
 6.10 
 References 
--
 Toggle Uyghur subsection 
 9.1 
 Etymology 
 9.2 
 Pronunciation 
 9.3 
 Adverb 
--
 Arabic
 [ edit ] 
 Etymology 1
 [ edit ] 
 Root 
 ب و ر ( b w r ) 
(eval):1: === not found
```


## [2026-10-17T00:04:12.007Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n '1367,1700p' 49747c621585df37.txt | grep -v \"^\\s*$\" | grep -v \"edit \\]\" | cut -c1-350 | head -90"
}
```


### [2026-10-17T00:04:12.349Z] TOOL RESULT

```
 Persian
 Persian Wikipedia has an article on: بار 
 Wikipedia fa 
 Dari
 بار 
 Iranian Persian
 Tajik
 бор 
 Pronunciation
 ( Classical Persian ) IPA ( key ) : /ˈbaːr/ 
 ( Dari, formal ) IPA ( key ) : [bɑːɾ] 
 ( Dari, formal ) IPA ( key ) : [bɑːɾ] 
 ( Kabuli ) IPA ( key ) : [bɑːɾ] 
 ( Hazaragi ) IPA ( key ) : [bɔːɾ] 
 ( Iran, formal ) IPA ( key ) : [bɒːɹ] 
 ( Tajik, formal ) IPA ( key ) : [bɔɾ] 
 Rhymes: -aːr 
 Readings
 Classical reading ? 
 bār
 Dari reading ? 
 bār
 Iranian reading ? 
 bâr
 Tajik reading ? 
 bor
 Audio ( Iran ) : ( file ) 
 Etymology 1
 See below.
 Verb
 بار • ( bâr ) 
 present stem form of باریدن ( bâridan , “ to rain ” ) 
 Derived terms
 آتشبار ( âtaš-bâr ) 
 اشکبار ( ašk-bâr ) 
 خون بار ( xun-bâr ) 
 گهربار ( gohar-bâr ) 
 بارش ( bâreš ) 
 Etymology 2
 From Middle Persian bʾl ( bār , “ load, burden; duty; fruit ” ) , from Proto-Iranian *bāra- ( “ load ” ) , from Proto-Indo-European *bʰer- ( “ to bear, carry ” ) . [ 1 ] 
 Noun
 بار • ( bār / bâr ) ( Tajik spelling бор ) 
 burden , load , charge 
 پربار ( por-bâr ) 
 سبکبار ( sabok-bâr ) 
 کوله بار ( kule-bâr ) 
 pack , bale 
 baggage , luggage 
 بار بستن ( bâr bastan ) 
 responsibility , duty 
 سربار ( sar-bâr ) 
 زیر بار رفتن ( zir-e bâr raftan ) 
 بار بر دوش گرفتن ( bâr bar duš gereftan , “ to take responsibility of a task ” ) 
 ( archaic ) sorrow , grief 
 بار دل ( bâr-e del ) 
 ( archaic ) sin , fault 
 ( archaic ) fetus 
 باردار ( bâr-dâr ) 
 fruit 
 Synonyms: بر ( bar ) , میوه ( mive ) 
 بار دادن ( bâr dâdan ) 
 بار آوردن ( bâr âvardan ) 
 adulteration 
 ( agriculture ) manure , fertilizer 
 cargo 
 electric charge 
 ( computing ) load 
 Synonyms
 ( baggage ) : وسیله ( vasile ) , اثاث ( asâs ) , بار و بندیل ( bâr-o-bandil ) ( colloquial ) , بار و بنه ( bâr-o-bone ) ( colloquial ) 
 Derived terms
 تره‌بار ( tare-bâr ) 
 بار کردن ( bâr kardan ) 
 Related terms
 خواربار ( xvârbâr ) 
 Descendants
 → Armenian: բար ( bar ) 
 Etymology 3
 From Middle Persian bʾl ( bār , “ time, occasion ” ) .
 This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
Particularly: “Does this word derive from Proto-Indo-European *bʰer- ( “ to bear, carry ” ) (and is thus a semantic extension of Etymology 2)? Or is it from another root like *bʰreyH- ( “ to cut ” ) ? Note also Sanskrit वार ( vā́ra , “ moment, occasion ” ) .”
 Noun
 بار • ( bār / bâr ) ( Tajik spelling бор ) 
 time , turn , occasion 
 Synonym: دفعه ( daf'e ) 
 آدم عاقل از یک سوراخ دو بار گزیده نمی شود. ( proverb ) âdam-e 'âqel az yek surâx do bâr gazide ne-mi-šavad. A wise person is not bitten twice through the same hole. 
 c. 1260 , Rumi , “ 5:3780 ”, in The Masnavi : نود بار آمدم تن برهنه بوک زخمی آیدم. navad bâr âmadam tan-berahne bu ke zaxmi âyadam. Ninety times I came [into battle] unarmed, that perchance I might be [mortally] wounded. ( Reynold A. Nicholson translation) 
 ( archaic ) permission to visit a ruler, king, etc.
 ( archaic ) court 
 ( archaic ) curtain at the door of a pavilion 
 Derived terms
```


## [2026-10-17T00:04:16.913Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c ff869a5c1356b51d.txt 44253677b535d01d.txt; grep -n -i -A3 \"etymology\" 44253677b535d01d.txt | head -20; grep -i -m3 \"does not have\\|not found\" ff869a5c1356b51d.txt; for h in ef5d2fcf9ba38425 1f6aaf2799bc2f3a d09e83b8d8b02ef6 6f9c8a679c9b2b0d bc31844728c8313a 3a580c1ff13e26bf ee2a8513ad872b82; do echo \"== $h\"; grep -m2 -i \"origin\\|from\\|uncertain\" $h.txt | cut -c1-700; done"
}
```


### [2026-10-17T00:04:17.447Z] TOOL RESULT

```
138 ff869a5c1356b51d.txt
133 44253677b535d01d.txt
271 total
FETCH FAILED: HTTP Error 404: Not Found
== ef5d2fcf9ba38425
== 1f6aaf2799bc2f3a
== d09e83b8d8b02ef6
== 6f9c8a679c9b2b0d
== bc31844728c8313a
== 3a580c1ff13e26bf
== ee2a8513ad872b82
```


## [2026-10-17T00:04:19.457Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c ef5d2fcf9ba38425.txt 1f6aaf2799bc2f3a.txt cf713de84bfed466.txt 3670be14f5c84a56.txt a4e7fabbff16daed.txt; head -c 400 ef5d2fcf9ba38425.txt"
}
```


### [2026-10-17T00:04:20.009Z] TOOL RESULT

```
  133 ef5d2fcf9ba38425.txt
  133 1f6aaf2799bc2f3a.txt
  134 cf713de84bfed466.txt
 4547 3670be14f5c84a56.txt
14207 a4e7fabbff16daed.txt
19154 total
URL: https://www.etymonline.com/word/wallet
FETCHED: 2026-10-17T00:04:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-17T00:04:25.499Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 541: $2\" 2>&1 | tail -1; }\nf 'https://en.wiktionary.org/wiki/wallet' 'Wel 3, wallet'\nf 'https://en.wiktionary.org/wiki/willow' 'Wel 3, willow'\nf 'https://en.wiktionary.org/wiki/walk' 'Wel 3, walk'\nf 'https://en.wiktionary.org/wiki/well' 'Wel 3, well'\nf 'https://en.wiktionary.org/wiki/helix' 'Wel 3, helix'\nf 'https://en.wiktionary.org/wiki/وار' 'Wel 3, -var'\nf 'https://en.wiktionary.org/wiki/طهمورث' 'Wel 2, Tahmuras'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wl̥kʷos' 'Wel 2 wolf'\nf 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wl̥pis' 'Wel 2 fox'\ncd data/verification/sources/web; head -c 1500 3670be14f5c84a56.txt | tail -c 1000"
}
```


### [2026-10-17T00:04:31.095Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e7ae71a820e712bb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ba981c61ac2938e4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/34fd3b7ece3f3b8d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/40ccbebf92997351.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02e7cae9249b4969.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0589be4d70321f0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/abcf747a3264a4ba.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/075658e5d38a64fc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2b226dab4912204.txt
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
 Descendants 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ wel- 

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

 See also: Reconstruction:Proto-Indo-European/welH- , Reconstruction:Proto-Indo-European/welh₁- , and Reconstruction:Proto-Indo-European/welh₃- 

 This Proto-Indo-European entr
```


## [2026-10-17T00:04:34.257Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -c 2500 3670be14f5c84a56.txt | head -c 1500; echo; for h in e7ae71a820e712bb ba981c61ac2938e4 34fd3b7ece3f3b8d 40ccbebf92997351 02e7cae9249b4969 c0589be4d70321f0 abcf747a3264a4ba 075658e5d38a64fc c2b226dab4912204; do echo \"== $h $(wc -c <$h.txt)\"; grep -n -A3 \"^ *Etymology\" $h.txt | grep -v \"^\\S*-\\s*$\\|edit \\]\" | grep -i \"from\\|origin\\|uncertain\\|compare\" | head -3 | cut -c1-600; done"
}
```


### [2026-10-17T00:04:34.855Z] TOOL RESULT

```
~ *-etos ) ( see there for further descendants )

 *wḗl-s-t ~ *wél-s-n̥t ( s-aorist ) 
 Proto-Tocharian: *yels- 
 Tocharian B: yel- ( “ to investigate ” ) 

 *wléy-ti ( ey-aktionsart ) 
 ⇒ *wley- ( reanalysed root ) 
 ⇒ *wléy-de-ti ( de-present ) [ 2 ] 
 > ? Proto-Germanic: *wlītaną ( “ to see, look ” ) ( perhaps more likely from a contaminated *weyd- ( “ to see ” ) [ 1 ] ) ( see there for further descendants )
 ⇒ Proto-Germanic: *wlaitōną ( “ to search ” ) ( see there for further descendants )

 *wél-ti-s ~ *wl̥-téy-s 
 Proto-Germanic: *wlitiz ( “ sight, appearance, face ” ) ( see there for further descendants )

 *wél-tu-s ~ *wl̥-téw-s [ 2 ] [ 1 ] 
 Proto-Germanic: *wulþuz ( “ glory ” ) ( see there for further descendants )

 Proto-Italic: *woltus 
 Latin: voltus , vultus ( “ (facial) expression ” ) 

 Unsorted formations 

 Proto-Armenian: 
 Old Armenian: գեղ ( geł , “ beauty; (beautiful) appearance, look ” ) 

 Proto-Germanic: *wuldrą ( “ glory ” ) ( see there for further descendants )

 References
 [ edit ] 

 ↑ 1.0 1.1 1.2 1.3 Rix, Helmut , editor ( 2001 ), “ 3. *u̯el- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 675 

 ↑ 2.0 2.1 2.2 Pokorny, Julius ( 1959 ), “ 1. u̯el- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, 
== e7ae71a820e712bb 18105
212- From Middle English walet ( “ a bag, knapsack ” ) , of uncertain origin. Possibly from an assumed Old Northern French *walet ( “ a roll; bag; a knapsack ” ) , from Proto-Germanic *wal- ( “ to roll ” ) . More at walk , well , wallow .
== ba981c61ac2938e4 23347
205- From Middle English wilwe , welew , variant of wilghe , from Old English weliġ , from Proto-West Germanic *wilig , from Proto-Germanic *wiligaz , from Proto-Indo-European *welik- (compare (Arcadian) Ancient Greek ἑλίκη ( helíkē ) , Hittite 𒌑𒂖𒆪 ( welku , “ grass ” ) ), from *wel- ( “ twist, turn ” ) . Cognate to West Frisian wylch and more distantly (via Proto-West Germanic *wilgijā ) to Dutch wilg and German Wilge .
== 34fd3b7ece3f3b8d 58290
360- From Middle English walk , walke , walken , walkyn , wolken ( “ to roll, toss, or turn; to walk; to move; to be living; to beat or full; to perform ” ) , a conflation of Old English wealcan ( “ to move around; to revolve; to roll; to fluctuate; to discuss ” ) ( ġewealcan ( “ to go, traverse; to roll ” ) ) and Old English wealcian ( “ to curl, roll up, twist; to wrinkle ” ) ; both from Proto-West Germanic *walkan , from Proto-Germanic *walkaną ( “ to roll, toss, turn, wind; to walk, wander, wend; to full, trample ” ) , *walkōną ( “ to roll about; to full ” ) , from Proto-Indo-European *wal
1374- From Middle English walc , walk , walke , from Old English *wealc (as in Old English wealcspinl ) and ġewealc ( “ rolling, turning; motion, surging ” ) , from Proto-Germanic *walką .
1862- Borrowed from English waulk .
== 40ccbebf92997351 75927
2429- From Middle English wellen , from a merger of Old English weallan (intransitive) and wiellan (transitive), both meaning “to boil.” Further from Proto-Germanic *wallaną and *wallijaną . Doublet of wall .
2538- From the accusative of Middle High German wīle , from Old High German wīla , from Proto-West Germanic *hwīlu . Cognate with German weil .
2724- From Middle High German welich , from Old High German welih . Compare German welch .
== 02e7cae9249b4969 11938
238- From Latin helix , from Ancient Greek ἕλιξ ( hélix , “ something twisted or spiral ” ) .
424- Borrowed from Latin helix , from Ancient Greek ἕλιξ ( hélix ) .
557- Borrowed from French hélix .
== c0589be4d70321f0 11146
286- Inherited from Proto-Turkic *bār .
438- Inherited from Prakrit 𑀯𑀸𑀭 ( vāra ) , from Sanskrit वार ( vāra ) . Compare Urdu بار ( bār ) .
472- Inherited from Sanskrit वाल ( vāla ) .
== abcf747a3264a4ba 3977
== 075658e5d38a64fc 170
== c2b226dab4912204 172
```


## [2026-10-17T00:04:39.259Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/welH-' --note 'page 541: Wel 3 root turn' | tail -1; cd data/verification/sources/web; sed -n 360,362p 34fd3b7ece3f3b8d.txt | cut -c590-900; grep -n \"wella\\|wielle\" 40ccbebf92997351.txt | head -3 | cut -c1-500; awk '/^ *Persian *$/,0' c0589be4d70321f0.txt | grep -v \"^\\s*$\\|edit \\]\" | head -40 | cut -c1-300"
}
```


### [2026-10-17T00:04:40.066Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/426e7541dbfe340d.txt
an *walg- ( “ to twist, turn, move ” ) .


1702: From Middle English welle , from Old English wielle ( “ well ” ) , from Proto-West Germanic *wallijā , from Proto-Germanic *wallijǭ ( “ well, swirl, wave ” ) , from Proto-Indo-European *welH- ( “ to turn; wind; roll ” ) .
2666: wellas 
2672: wellas 
 Persian 
 Toggle Persian subsection 
 4.1 
 Noun 
 4.1.1 
 Derived terms 
 5 
 Punjabi 
 Toggle Punjabi subsection 
 5.1 
 Alternative forms 
 5.2 
 Etymology 
 5.3 
 Pronunciation 
 5.4 
 Noun 
 5.4.1 
 Derived terms 
 5.5 
 References 
 6 
 Sindhi 
 Toggle Sindhi subsection 
 6.1 
 Etymology 
 6.2 
 Noun 
 6.3 
 References 
 7 
 Urdu 
 Toggle Urdu subsection 
 7.1 
 Pronunciation 
 7.2 
 Etymology 1 
 7.2.1 
 Noun 
 7.3
```


## [2026-10-17T00:04:43.361Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n \"^ *Persian *$\" c0589be4d70321f0.txt; awk 'f&&/Punjabi/{exit} /^ *Persian *$/{c++} c==2{f=1} f' c0589be4d70321f0.txt | grep -v \"^\\s*$\\|edit \\]\" | head -25 | cut -c1-300; echo ====; grep -v \"^\\s*$\" 426e7541dbfe340d.txt | grep -n -i \"Iranian\\|Avestan\\|Sanskrit\\|ūrmí\\|Latin: volv\\|vallis\\|varəm\\|Persian\" | head -30 | cut -c1-300"
}
```


### [2026-10-17T00:04:43.922Z] TOOL RESULT

```
Exit code 1
123: Persian 
412: Persian
 Persian
 Noun
 وار • ( vâr ) 
 ( rare ) flame 
 Derived terms
 وار زدن ( vâr zadan ) 
(eval):1: === not found
```


## [2026-10-17T00:04:49.301Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; wc -c data/verification/sources/web/426e7541dbfe340d.txt; f(){ python3 tools/fetch_source.py \"$1\" --note \"page 541: $2\" 2>&1 | tail -1; }\nf 'https://vajehyab.com/moein/وار' 'Wel 3, Moin s.v. var'\nf 'https://vajehyab.com/dehkhoda/وار' 'Wel 3, Dehkhoda s.v. var (Rudaki verse)'\nf 'https://vajehyab.com/moein/گربه' 'Wel 2, Moin s.v. gorbe'\nf 'https://vajehyab.com/moein/طهمورث' 'Wel 2, Moin s.v. Tahmuras'\nf 'https://vajehyab.com/moein/برم' 'Wel 3, Moin s.v. barm'\nf 'https://vajehyab.com/moein/بار' 'Wel 3, Moin s.v. bar'"
}
```


### [2026-10-17T00:04:51.959Z] TOOL RESULT

```
7075 data/verification/sources/web/426e7541dbfe340d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3026dde260368b16.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2d076bcb869e93d2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/aa42594a7763cf2c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b37ef613812b7974.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/825c874f0e98eb27.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1cf78020775ad63c.txt
```


## [2026-10-17T00:04:54.800Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for h in 3026dde260368b16 2d076bcb869e93d2 aa42594a7763cf2c b37ef613812b7974 825c874f0e98eb27 1cf78020775ad63c; do echo \"== $h $(wc -c <$h.txt)\"; grep -v \"^\\s*$\" $h.txt | sed -n 5,60p | grep -v \"^ *[A-Za-z ]*$\" | head -14 | cut -c1-400; done; grep -v \"^\\s*$\" 426e7541dbfe340d.txt | tail -60 | head -50 | cut -c1-200"
}
```


### [2026-10-17T00:04:55.445Z] TOOL RESULT

```
== 3026dde260368b16 1519
معنی وار | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 وار
 فرهنگ انتشارات معین
 (پس .) 1 - نشانة دارندگی ، عیالوار. 2 - به معنی نظیر و مانند: دیوانه وار. 3 - (اِ.) دفعه ، مرتبه . 4 - به معنی بار، حمل : خروار،شتروار. 5 - دال بر لیاقت : شاهوار، گوشوار. 6 - آنچه مدت معین ظاهر شود: هفته وار (مجله هفتگی ).
 وار در فرهنگ‌های دیگر
 معنی وار در لغت‌نامه دهخدا 
 معنی وار در فرهنگ فارسی عمید / قربان‌زاده 
 معنی وار در گویش بختیاری 
 معنی وار در گویش مازنی 
 معنی وار در فرهنگ مترادف و متضاد 
 معنی وار در واژه‌نامه آزاد 
== 2d076bcb869e93d2 1696
معنی وار | لغت‌نامه دهخدا | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 وار
 لغت‌نامه دهخدا
 وار. (اِ) رسم و عادت . (برهان ) (جهانگیری ) : 
فرخ آنکس که وار خود بشناخت 
کار خود را به وار خود پرداخت .
 جامی (از جهانگیری ).
 || طرز و روش . (غیاث ). || نوبت . (جهانگیری ) (آنندراج ). زمان . دور. واره : 
وار آذر گذشت و شعلهٔ آن 
شعلهٔ لاله را زمان آمد.
 رودکی .
== aa42594a7763cf2c 1812
معنی گربه | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 گربه
 فرهنگ انتشارات معین
 (گُ بِ) [ په . ] (اِ.) حیوانی است پستان دار و گوشت خوار از تیرة گربه سانان ، دارای جثه ای نسبتاً کوچک ، سرِ گرد، سبیل های حساس ، گوش های راست و متحرک و پنجه ها و دندان هایی تیز. این حیوان به بی صفتی و نمک نشناسی معروف است . ؛ ~را دم حجله کشتن کنایه از: ترساندن ، زهرچشم گرفتن .
 گربه در فرهنگ‌های دیگر
 معنی گربه در لغت‌نامه دهخدا 
 معنی گربه در فرهنگ فارسی عمید / قربان‌زاده 
 معنی گربه در دیکشنری فارسی به عربی 
 معنی گربه در دیکشنری فارسی به انگلیسی 
 معنی گربه در دیکشنری فارسی به ترکی 
 معنی گربه در گویش اصفهانی 
== b37ef613812b7974 134
FETCH FAILED: HTTP Error 404: Not Found
== 825c874f0e98eb27 1509
معنی برم | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 برم
 فرهنگ انتشارات معین
 (بَ رَ) (اِ.) 1 - چوبی که پارچه ای ملون بر بالای آن بندند و در میدان نصب کنند برای آگاه کردن مردم از کشتی پهلوانان . 2 - چوب بندی را گویند که تاک انگور و بیارة کدو و خیار و غیره را بالای آن گذارند؛ داربست .
 برم در فرهنگ‌های دیگر
 معنی برم در لغت‌نامه دهخدا 
 معنی برم در فرهنگ فارسی عمید / قربان‌زاده 
 معنی برم در دیکشنری فارسی به انگلیسی 
 معنی برم در گویش مازنی 
 معنی برم در فرهنگ مترادف و متضاد 
 معنی برم در واژه‌نامه آزاد 
== 1cf78020775ad63c 1646
معنی بار | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 بار
 فرهنگ انتشارات معین
 ( اِ.) 1 - اجازه ، رخصت . 2 - اجازة حضور نزد شاه یا امیر. 3 - دفعه ، مرتبه . 
 بار در فرهنگ‌های دیگر
 معنی بار در لغت‌نامه دهخدا 
 معنی بار در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بار در گویش بختیاری 
 معنی بار در دیکشنری فارسی به عربی 
 معنی بار در دیکشنری فارسی به انگلیسی 
 معنی بار در دیکشنری فارسی به ترکی 
 Latvian: vēl ( “ yet, still ” ) 
 Lithuanian: vėl ( “ again ” ) 
 Samogitian: viel 
 Slavic:
 Russian: вал ( val , “ billow ” ) 
 Proto-Celtic: *walensnā [ 3 ] 
 Proto-Brythonic: *gwalenn 
 Middle Breton: goalenn ( “ green twig ” ) 
 Breton: gwalenn 
 Proto-Celtic: *welnīti 
 Old Irish: fillid ( “ to bend ” ) Middle Irish: fillid Irish: fill , pill 
 Manx: filley 
 Scottish Gaelic: fill 
 Middle Irish: tillid ( as if prefixed with to- ) Irish: till 
 Scottish Gaelic: till 
 Proto-Germanic: *wiligaz ( “ willow ” ) , *walkaną ( “ to turn, walk ” ) , *walkōną ( “ to roll, to full ” ) , *walgōną ( “ to roll ” ) , *wallijǭ ( “ well; wave ” ) ( see there for further descendan
 Hellenic:
 Ancient Greek: ᾱ̔λής ( hālḗs ) (< *sm̥wl̥ēs), ᾱ̔λίᾱ ( hālíā ) , ᾱ̔λίζω ( hālízō ) , ἀολλέες ( aollées ) (< *sm̥wolnēs), εἰλεός ( eileós ) , εἰλύω ( eilúō ) , εἴλω ( eílō ) , ἕλιξ ( hélix ) , ἑλίσσω (
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: उल्ब ( úlba ) , उल्व ( úlva ) 
 Sanskrit: वलय ( valaya , “ coil ” ) 
 Sanskrit: वलयति ( valayati , “ to cause to turn ” ) 
 Sanskrit: वल्लि ( valli , “ creeper; winding plant ” ) 
 Proto-Italic: *wolwumen , *wolgos , *wolwā 
 Latin: valgus , valva , volumen , vulgus , vulva ( see there for further descendants )
 References
 [ edit ] 
 ↑ 1.0 1.1 1.2 1.3 1.4 Rix, Helmut , editor ( 2001 ), “ 2. *u̯elH- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert
 ^ Kroonen, Guus ( 2013 ), “*walwjan-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 572 
 ^ Matasović, Ranko ( 2009 ), “*wel-n-o-”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN 
 Further reading
 [ edit ] 
 Pokorny, Julius ( 1959 ), Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 1140ff 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/welH-&oldid=92422285 "
 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European ReRH-shaped roots 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 
 This page was last edited on 31 August 2026, at 15:22.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct
```


## [2026-10-17T00:05:00.154Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"gurbag\" \"rōbāh\\|robah\\|rōpās\" \"tahm[oō]r\\|taxm[oō]r\" \"^ *bār \\|^bār \" \"hamwār\\|hamvar\\|hamwar\" \"^ *war \\|^war \\|warišn\\|warrōy\" \"^ *-wār\\|wār \" \"warm \"; do echo \"### $p\"; grep -n -i \"$p\" PHD.txt | head -6 | cut -c1-250; done"
}
```


### [2026-10-17T00:05:00.543Z] TOOL RESULT

```
### gurbag
1172:cat gurbag.
5446:gon gonag dowom drustih drust gowizar gozénag gugay gugay gugayih gugayih gugan- gokanig gokan doganag gugar- gugārīdan gugārdan dēk gēūgirdūmand gogird даг, рог, gul dol gurbag
### rōbāh\|robah\|rōpās
### tahm[oō]r\|taxm[oō]r
### ^ *bār \|^bār 
### hamwār\|hamvar\|hamwar
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwh
702:abreast hamwar.
2609:level hāmēn, hamwar.
### ^ *war \|^war \|warišn\|warrōy
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE <
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [w
698:abode šāwarišn,  bunag, nišēmag; (daevic) dwārišn.
967:behaviour barišn, rawišnīh, warišn.
1365:consumption xwarišnīh,
1696:drink xwarišn; alcoholic — hur.
### ^ *-wār\|wār 
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw
130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE <
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; c
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-k
### warm 
378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [w
2584:learn hammóxtan; ~ by heart warm kardan.
2778:memorize warm kardan.
4264:warm garm(6g); ~ region garmsér,
5165:narm, -*warm O yt
```


## [2026-10-17T00:05:03.227Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 607p PHD.txt | grep -o \"wany(b).\\{0,1500\\}\" | cut -c1-1600; grep -n -o \"bār \\[.\\{0,250\\}\" PHD.txt | head -5; grep -n -o \"gurbag \\[.\\{0,120\\}\\|rōbāh.\\{0,100\\}\\|ròbāh.\\{0,100\\}\" PHD.txt | head; grep -n -o \"hamwār.\\{0,150\\}\\|hamwar \\[.\\{0,150\\}\" PHD.txt | head -3"
}
```


### [2026-10-17T00:05:03.756Z] TOOL RESULT

```
wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
252:bār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignati
376:bār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker.
390:bār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] fo
663:bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' 
392:hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P
```


## [2026-10-17T00:05:08.831Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"varišn\\|warišn\" \"hamvār\\|hamwār\" \"gurpak\\|gurbak\\|gurpag\" \"taxm\\|tahm\" \"^ *bār\\b\\|bār m\\.\" \"varm\\b\\|warm\\b\" \"rōpās\\|rōpāh\\|rōbāh\"; do echo \"### $p\"; grep -n -i \"$p\" NYB_vol2_glossary.txt | head -5 | cut -c1-300; done"
}
```


### [2026-10-17T00:05:09.292Z] TOOL RESULT

```
### varišn\|warišn
1420:dvaristan [dwb'lstn'], dvaritan [dwb'lytn'] to run, to rush, of enemies and demoniac beings 2518 ete. passim; — andar ~. to rush, to come dashing (6 into the presence of) 7526; to make an onslaught, of Ahri- man and the demons at the beginning of the world 933.13, 9519, 10318; to make an assaul
3131:pēš [pyš; L'YN!, inser. and Ps. L'YNY] l. adv. before, earlier 97°; first, opp. pas, in a sequence 5718; ~ hac before: 912, 1274, 382, 392, 493, 652°, with a v. n. or an inf. instead of a temporal clause 4618, 5423; ~ ki 81. 1317, ~ hac han-tčit [ZK *D] ka 98% conj. before; dvārtšn 6 ~ to run 
3973:varišn [wlšn'] conduct, way of living: ~ névak 90%, —--ē (sg. cas. obl.) frarön 9024 righteous as to his conduct. — Per- haps to be derived from Av. (1362 sq.) 3yar- ‘to turn’. Arm. lw. var-k* (pl., stem varu-) ‘conduct, habits’, adj. varun ‘beat- n (track)’.
5670:nydfwrd, nydf’r-: nihvarišn
### hamvār\|hamwār
1862:ham-vàr [hmw?l] always, continually 1”. 135. 1211". — Paz. ham(a)vär, hamjür. A synonym of hambär (q. v.) with which it is generally regarded to be identical (OP *hama-bāra- > hamvār and then remod- elled after the simple bdr); but perhaps better connected with Skr vära- ‘turn, time’, cf Av. (1
### gurpak\|gurbak\|gurpag
1739:gung [gwng, gng] dumb 11°. 127. 652°. — = NP. gurbak [gwlbk'] cat 101. — NP gurbah.
7172:gurbah: gurbak
### taxm\|tahm
1129:eihr [cyhl; inscr. ctly] seed, origin HajB 2-4. SPrs: 5.7.13. P1:2.4; essence, innate quality 55°. — Av. (587) ?c?0ra-, OP *cica- in n. pr. Cicantaxma (Trosapéevng < * Cica-farnah-) ; MPrs cyhr essence, shape, origin, face = MPrth cyhrg; cyhr’wynd ‘beautiful’, Sogd. 35.37, cf hu-cihr; Paz. ciha
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1;
1459:šton [ytwn'; HKYN 467] thus, in this way, passim; such 6215; han ~ 345, e(t) ~ 6920-21 such as that, as this; hàn i ~ such things 5817; — before an adj.: so 1225, 3724 ete. before an adv. 5611-12, 1192; — governed by a vb. of saying, thinking, perceiving etc., it anticipates a clause with kū ‘t
1781:11814-15; — unfulfilled condition: past pt. + hé, or hà(h), or hat, pl. hand (v. h-): ~ citak city (HWH =) he, adak ... but (HWH =) kē if a cairn (v. s. v. citäk) had been erected, it would have been . HajB:9-10; —-am...n&özathäh,as...be apasthénit hah if I had not killed him he would have dest
3349:Rötastahm [lwtsthm] n. pr. 1162. — NP Rustam; Old Sogd rwstmy, Reichelt, Sogd. Handschr.- R. II, 63.
### ^ *bār\|bār m\.
### varm\|warm
563:apa-zón [’pzwn'] increase, addition 11217; tan pat-~ kunéh increase thy physical well being 21%, cf s. v. ?pat (11); increase of spiritual blessings 50%. — MPrs ’bzwn (A-H IT); Paz. awazün; NP afzün ‘more, greater’; < *abi-Zavana-, in which api- was substituted for abi-, v.s. v. apa-; from apa-z
1636:garm [glm], garmök [glmwk'] hot, warm 1420, 41?9, 10122. — Av. (515) garoma-, (516) garomu- ‘heat; MPrs grm’g ‘heat’ (A-H I); NP garm. l
3041:patiš [pts] adv. 1. before (= pēš), with hac: ~ hac zāyišn i ... before the birth of ... 365. — 2. used instead of pat if it refers back to an encl. pron. in the be- ginning of the sentence: cē-m anākēh vas ~ kunēnd (BYDWN-x;) for they will do much harm to me 954; i ka-t anākēh ~ kuném for we s
### rōpās\|rōpāh\|rōbāh
```


## [2026-10-17T00:05:12.099Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1862,1866p NYB_vol2_glossary.txt; grep -n \"bār \\[\\|^bār\\|^ *bar \\[b'l\\]\\|b'l\\]\" NYB_vol2_glossary.txt | head -5 | cut -c1-400"
}
```


### [2026-10-17T00:05:12.565Z] TOOL RESULT

```
ham-vàr [hmw?l] always, continually 1”. 135. 1211". — Paz. ham(a)vär, hamjür. A synonym of hambär (q. v.) with which it is generally regarded to be identical (OP *hama-bāra- > hamvār and then remod- elled after the simple bdr); but perhaps better connected with Skr vära- ‘turn, time’, cf Av. (1362sq.) ?var- ‘to turn’.
ham-x'ari$néh [hmhwlänyh] the act of drinking together: api-§ mad pat ~ 6
ham z'art 6118; as to the construction v.s.v. pat.
hàn [ZK], with emphasizing particle hän-ic [ZK-c; on ZK-p, ZK-py 5113-15 v.s. v.-p], dem. pron., sg. and pl., refer- ring to what is distant from the speaker, or already mentioned; independent, or adj. placed before its headw. (exception: viyük han HajB: 9); the adj. han may be replaced by hàn t, properly ‘that which is’: hàn + "sih that *splendour 125-26; han i Vidrafš + yātūk 25%; han à yamak 571%; esp. if -c is added to it: hün-ic i dar-band 241; hān-ic i Hutēs
2422; — determinative: han i ..., hàm
918:ībār [b?]] burden 1188. — = NP.
1678:Göbär [gwb'l] one of the districts of Ispahan 8??, - Yagut 2,138 Jūbār, v. also EI? s.v. Isfahän. Antià reads Dūbāl, which he identifies with the town called Duvan. |
```


## [2026-10-17T00:05:17.059Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^• *[0-9]*\\.\\? *var-\\|^•  *j\\. *[0-9]var-\\|•  [0-9]\\.  var-\\|^• *[0-9] *var-\\|V\\.  *'var-\" BRT.txt | head; grep -n \"'wenden'\\|'umwenden\\|'sich wenden\\|'drehen'\" BRT.txt | head | cut -c1-200"
}
```


## [2026-10-17T00:05:18.020Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"var- *V\\.\\|var-  V\\.\\|'var-  V\\|var-  v\\.\" BRT.txt | head -20 | cut -c1-250"
}
```


### [2026-10-17T00:05:18.320Z] TOOL RESULT

```
13975:•  j-,  g.  'dvar-  V.  'gehen',  uzw.  von ifoA^chen  Wesen".  Praes.  2  dvara-, 4  äväru:
22730:•  g.  vayü.bar^t- Adj.'wehe!,  Wehgeschrei anhebend':  'bmdubyS  dui^'ara-hsm  nasal  \  •  '}■>  &.  P-  'var-  V.  'irählen  (usw.)'.  Praes.
22733:•  'var-  V,  'hüllend  bedecken';    nur  mit Praev.     Praes.  10  varmav-  :  vamv-,     it
22760:•  j,  3var-  V.  '(se)  vertere',  nur  mit  Praev. Praes.  10  v>r>nav-  :  virpnv-,  aj  (Pass.) vsirya-,  30  (Kaus.)  vsraya-.
```


### [2026-10-17T00:05:18.438Z] TOOL RESULT

```
17525:Aus  3X.  *pra-fff-t;    zum  V.  'var-,    %  368.  41;
22811:KompE.  —  Eig.  'Beglaubigung,  Erhärtung' des  Rechts,  der  Unschuld;  lum  V.  'var-,  — Vgl.   yvaroA:    —    mp.  (Pü.)   z«ir  'Ordal'.    —
23498:vAbieit.  —  Zum  V.  'var-.  —  Vgl.  matdä.vara-. —  Pü. :  (pa)  iämai.
9833:l'Q.i  hac  dtüin  afiar  vailat  (gescht.  i'')0  hae fiixai')  i  silTiar  "rechls  auf  dem  EückgtBl  0 beim  drillen  Wirbel" a).  Vorher  steht:  apar\ buland  fa  sar  i  kSf  "oben  auf  
19204:*mvaila>ka-  Adj.,  Ableit  aus  'ni-vaila-  Adj-, PPfP.;  VgL  mp.  vaJian,  np.  gajtan  'drehen'; s.  dazu  Bthl.  IF.  4.  i^i,  Hbm.  PSt.  197,  —
25554:i)  'sich  drehen,  kreisen':  lainm  (sd.) Aaraihyä  . .  yat  ml  aiwitS  urvis)nti^^  sta- rasiam  äsca  Avanca  Ytja.as,  2)'sich wenden,  umkehren':  in/a  mi  urvisyatim "zurüclc  wendeten
```


## [2026-10-17T00:05:19.757Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22730,22770p BRT.txt | cut -c1-600"
}
```


### [2026-10-17T00:05:20.073Z] TOOL RESULT

```
•  g.  vayü.bar^t- Adj.'wehe!,  Wehgeschrei anhebend':  'bmdubyS  dui^'ara-hsm  nasal  \  •  '}■>  &.  P-  'var-  V.  'irählen  (usw.)'.  Praes.
Zum  Perf.  de»  V.  via;  -
•  j,  "vavCata'*  F.  i/. PQ.i  nndeullich. —  ■)  Unter  den  Wörtern  mit anlant.  m.    Zweimal  mit  Anlauls-c  geschr.
•  'var-  V,  'hüllend  bedecken';    nur  mit Praev.     Praes.  10  varmav-  :  vamv-,     it
mit  aiwi  'überdecken,  verbergen':  mqna- yptt  bä  . .  ya%a  masyayh  vana  kasyarihqm vanqm  aiwi.vfr^ttvaiti'^  ".  .  wie  ein grösserer  Baum  kleinere  Bäume  verbirgt" V.5-24-
mit  avi  und  kam  'in  etwas  (Lok.)  hinein bergen':  fl  mqnt  ava'ha  vinrunte  (sd., Sp.  1363  m.)  yä^a  anyascU  ariänö  avi x/udrä    x/ährisva    Aam.v^tynavainti'''    V.
mit  h4im  'zudecken,  bedecken':  aitaaa altaÄe  äste  (Sp.  340  m.)  stairisca  bar?nua hqm.v?r»nante  V.5. 59.
ai.  v^nSli,  vfnase. —  Pü.  (1UV.5J:  HÜu/iati't, (zu  V.'  /j):  äfiuiltan').  —  ')  Them.  —  ")  VgL
jr^jäfSM  dngvSui>byd  djfit.antaiibyl>  "den wehe!  rufenden  wird  Üble  Speise  (vorge- setzt)", das  Paradies  (aber)  geht  ihnen verloren,  denZ^n^enossen,  die  das  Recht missachten"  Y.5?.  6.
'vayü  Interj.  'wehe !'.  —  Vgl.  vayöi.  —  Pü. : S  an')daAiiri  tarind  ruvätt  i  »■«.  —  ')  Die Zusammenstellung  Weheruf  und  Qble  Speise als  das,  was  des  Z'rti^anhängers  wartet,  auch Y.  31.  20  und  H.  2.  34,  36.    —    =)    Vgl.    zu
•  j.ya'^a  para  "vayto  nmänamca  vlsimca zatäSuica  datahJuÜa  iii.S:  —  ?  — .
Pü.:    vai  elSii    kac  öi  afi  failäkih  hend  haf
7  väur-'^,  10  v>rmav-,  vamav-''' :  v»rfnv-,  11  v>r>n-  [,25  v?rfnaitä\.  — PPfP.  'vanta-,  PFP.  vairya-;  Inf.  urväm, virmdyäi.
1)  'etwas  (Akk.)  wählen,  sich  auswählen, sich  entscheiden  für  — ,  sich  überzeugen von  — ,  glauben,  ■n^i^eii%ai' ;  Med.^':  hyat Ti  a.d^aoma  (sd.)  .  .  upa.Jasat  hyat  vir^ natil  (3P.)  acistim  manS  ",  .  so  dass  sie sich  das  schlechteste  Denken  ausenrähl- ten"  Y,^.  6;  —  aya  *niainivS  varata (aPPrM.)  yi  drsgva  aältä  vtryxyS  aitm mainyus  spSnistB  .  .  yascä  .  .  "unter  diesen beiden    Geistern    wählten    sich    der    zur
dby  Google
13^1  'var-i  a
Z>ru^  haltende  das  Tun  des  Schlechtesten aus,  das  A/a  aber  der  heiligste  Geist  .  . und  die,  welche  . ."  Y.^0, 5;  —  /am (istim  tßjämäspS  .  .  ii'idil  ifanns  (sd.)  . . iwwfWÄ  (3SPM.)  Y.5;.  18;  ~  at  ahurä kvB  mainyüm  zarahustrB  vtrynll  mazda yasK  äicä  spsnilto  "aber,  o  Ah.,  er,  Zar,, erwählt  sich  jeden  deiner  heiligsten  Geister, o  Mr  Y.  4j.  16;  —  spintam  vS  ärmaitim vaauhjtn  varimaids {xYYi'A^  hä  riS anhat "für  eure  heilige  gute  Frommergebenheit haben  wir  uns  entschieden;  sie  soll  unser sein!"  Y.  _y2.  a;  —  sp>niqm  ärmaillm 
sein,  vertrauen',  mit  Akk.  und  Inf.:  maibyd %via  sastrai  (sd.)  vtnne  ahura  Y.  46.  j 3.  b)  'lieber  wollen  als  -,  vorziehen vor— '{Abl.):^(7i/V''^'*'"'^(sd-)  asäl  varatä (3PPrM.)  karapa  .  .  Y.J2.  iz.  a)  mit  1
kaus.  BedeuL  'überzeugen,  ■aitisiv',  Med.  I J  MäfyJ' .  .paruv  *%aäayä* . .  nailim  vama- 1 vätaiy  duruxtain  (sd.)  *maniyätaiy  Bh.  4- S;  —  tya^  manu  kartam  varnavatam  1 "^uvam  mJ/yJ*  *draujTyähy  {^A.)  Bh.  4.  6; — . .  nüram  %uväm  vamavaiSm  ty<^  mann  \ kartam  ai'a3ij(sd.)..Bh.4. 10.'!  a)gAw.  | insbes.  vom  Überzeugen  auf  religiösem  1 Gebiet,  sva.  'zum  Glauben  bringen,  be- kehren'; nur  Int.,  Med:  tat  nS  ..  vaolä^ kisvS .  .y3  jvantd  vispSng  väuraya  ( 1 SOM.) ". .  auf  dass  ich  alle  Lebenden  überzeugen  , kann"  Y.jr.  3;  —  >43  (näml,  
unter  nl.]
mit  /rä  Med.  i)  'Jemanden  (Akk.)  fUr sich  (Dat.)  auswählen  ab  — '  (Akk.):  at At  ayh  fravar»lä  västrim  ahyai  ßuyantim ahunm    alavamm   .  .  fsSnghJm  (sd.)    "da
^var-  mit  avi  136a
hat  sie  unter  den  beiden  den  viehzUch- tenden  Bauer  Air  sich  als  den  gerechten Herrn  auserwählt.."  Y.j/.  10.  a)  als
religiöser  Teim.  techn.  a)  'den  Glauben (einer  Religion)  bekennen,  sich  bekennen zu  (einer  Religion)',  mit  Akk.  oderlnstr.: dainqm  mätdayasnTm  fraonnaita  s'  (3SPr.) "Z.  bekannte  sich  zur  mazd.  Religion"  V. /p.  2;  —  aya  damaya  fraonnta^  (3S.) ahurS  maidä  frä^  .  ,  Y.j?.  24;  —  aya äagnaya  fraonnta  ^  ahura  mazdh  frä^  . . fra  hi  (als  AS.)  amisa  spsnta  b>nja  (sd.) viranta  (3S.,  statt  Plur.)  dalHayäi  Yt.  10. 91;  — /rä  le  v>rme  ahe  damaya  ..  ahura .  .  maidayamS  zara^ustrÜ  "ich  bekenne mich  dir,  zu  dieser  (unserer)  Religion  .  .
GlaubensgelUbde  ablegen,  sich  zum  Glau- ben bekennen',  absol.:  masdayasnB  zara- "k  ustril  fravarSnl  astBtasifS  fravarftascä "als  J/atiÄT)'.,  als  Zun  will  ich  das  Glaubens- gelübde ablegen,  der  sich  dem  Glauben angelobt,  zum  Glauben  bekannt  hat"  Y, /2. 8;  i;  —  yS  paoiryl!  ../raonrtalai^S.yi'''^ mazdayasnS  zardhustri! '^X.  13.  Z^\  —  s. noch  Inf.
mit  nl  dnwS.  2  a:  tjm  zT  v3  *spfrtdil ^m'varanV  ya  .  .  "die  hier  will  ich  mit Eifer  zum  Glauben  bekehren,  dass  sie  .." Y.5i.4.
ai.  vfmlt  >er  wählt',  vpfuli,  varal,  avj-la,  vu- rila;    np,  giravTJan^);    oosi.  wmin  'glauben'.
—  Pu.  1)  zum  einf.  V.:  diiüan,  (iuY-iS.  la): dösatlar,  (10  V.  35-  f>-  ■iä""^  dalan,  (sonst): vamvilait^l ,  varavenilan,  varaviin  dälan; a)  zum  komp.  V.,  a)  mit  «1:  döiUaa,  b)  mit /Vä:  /raitä/tanm.  (lU  Vr.  J.  3):  Jräc  varm,f. lau.  Sü.  ist  auffällig  unEleich.  —  ■)  S.  dazu S  310  Na.   [.  —  ')  Slets  them.  tiektirl.    InL-
i      Red.  zeigt  auch  mp.  vävar,    np.  bävat  (wozu Hbm.  AGr,  /.  100,  Salemann  GlrPh.  /.  269).
—  J)  Allein  ausgenommen  viriHoval  F.  S, dessen  Überseiiung  mit  däiil  darum  wahr- scheinlich auf  einem  Miss  Verständnis  beruhen wird.  —  0  Vgl.  KZ.  2g.  385  f.  —  S  S  368. 41.  —  6)  Them.  —  n  So  die  Lesart  von PI  4,  J  2.  NA,  sfiridäni  varätii.  —  <)  Vgl. GIrPh.  /  b.  laS;  dazu  noch  KL.  3.  85.  — 9)  Zu  V.  ig.  2  mit  der  Erl. :  kus  fravatänc  iarl.
•  j,  3var-  V.  '(se)  vertere',  nur  mit  Praev. Praes.  10  v>r>nav-  :  virpnv-,  aj  (Pass.) vsirya-,  30  (Kaus.)  vsraya-.
mit  avi  und  pairi  'sich  Uberbreitend herzukommen  zu  — '  (Akk.):  v^rt'ätrayne  avi imat  nmätum  gaosuräbys  ifarirtS  patri.- Virfftavaiti''''  ya%a  ..    "K  kommt  herzu
dby  Google
1363  3var-  mit/mVi  —  'varay-  1364
und  breitet  sich  über  dieses  Haus,  das  ^tm  (sd.)  ..  V.2.30;  38;  —  auch  Rur.: durch  seinen  Rindeneichtum  henüche{}),'  aäagsiia  '^•rxfsva'^.Y'i  yö  yimS  kinnaot wie  .  ."  YL/4.41-  "in    der  Burg,    die    Y.  erbaute"  V,2.39;
niVi  paiti    'umstürzen,   zu  Grunde  rieh-;  —  visptm  a  ahmäl  yal  alte  narB  "'rt/^iHt ten,  vernichten';    mi^rtm  ..yd    doi^Afus .(LP.)''  anh^n  V.2.28. raxryaihyS  paiti  s^armä  värayäti  "..der       Zum  V.  "for-.    —    ai.  vgl.  vata-  m.  'Raum';
die  Heirlichkeiten  des  Landes  vernichtet"  "P"  <^"-'  "%  '^""''  ("="■''■  T  ,!'  ,^e'-  ""
,,                                                                                  I  Sage   vom  Var  (mp.  var  1  yamkart)   Ijndnkb
^^lO.iT.  Fesigr.  Roth   313.    —    »)   SlaU   faf^iwi,   wie
mit  fairi  'pervertcre'**;  a)  '(Ohren)  ab-  utsächlich  L  4  a  zu  V.  3.  39,  41  biet«.  Die
drehen,    abreissen'J*;    aisam  . .  pairi  uH  Veneming  des  Woits  ist  offenbar  duicli  V.
```


## [2026-10-17T00:05:28.485Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'E'\nimport json,glob\nfor f in ['page-538.json','page-537.json','page-536.json','page-535.json','page-534.json']:\n  d=json.load(open(f))\n  for e in d['entries']:\n    for n in e['nodes']:\n      if 'barm' in n.get('words','') or 'gorbe' in n.get('words','').lower():\n        print(f,e['root'],n['id'],n['words'],n['verdict']); print(n['derivation'][:1500]); print()\nE\ngrep -l \"barm\\|Tahm\" page-5*.json page-4*.json | head"
}
```


### [2026-10-17T00:05:29.040Z] TOOL RESULT

```
page-503.json
page-507.json
page-522.json
page-533.json
```


## [2026-10-17T00:05:31.307Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'E'\nimport json\nfor f in ['page-533.json','page-522.json','page-503.json']:\n  d=json.load(open(f))\n  for e in d['entries']:\n    for n in e['nodes']:\n      s=json.dumps(n,ensure_ascii=False)\n      if 'barm' in n.get('words','') or 'Tahm' in n.get('words',''):\n        print(f,e['root'],n['id'],n['words'],n['verdict']); print(n['derivation'][:1200]); print()\nE"
}
```


### [2026-10-17T00:05:31.751Z] TOOL RESULT

```
page-522.json Var 2 barm confirmed
NP barm 'pool, pond, reservoir' (Borhan: 'تالاب و استخر و چشمهٔ آب'; Shahid Balkhi, Farrokhi) < MP warm with the regular initial w- > b-. Mo'in tags it [په.] (Pahlavi). It must be kept apart from barm 'memory' (< 1warm) and borm 'pole, trellis'.

page-503.json Tenk 2 tang; tanjîdan; tahamtan; Tahmŭras; Rostam plausible
tang 'narrow, tight' < MP tang [tng] (MacKenzie 'narrow, tight') < OIr. *tanka-/*tanč- (Cheung *tanč) < PIE *tenk-; Horn 398 and Hübschmann 398 put it beside Av. tančišta-, so confirmed. tanjīdan 'to squeeze, contract, pull tight' (with variant taranjīdan) is from the same *tanč- (Cheung; Wiktionary: borrowed from a NW-Iranian cognate of Manichaean MP tnz- 'to strain, press'); Horn 394 had linked it to Av. θanj- 'to pull', which Cheung explicitly rejects. tahamtan 'strong-bodied', Rostam's epithet, = tahm/taham 'strong' (MP tahm 'strong, brave' < Av. taxma-, -xm- > -hm-) + tan 'body' (Av. tanū-): confirmed. Tahmūras/Tahmūrath < MP Tahmōraf < Av. Taxma Urupi; the Arabic-script ث reflects an Arabicised spelling; the gloss 'with strong dogs' is speculative. Rostam < MP Rōdastahm/Rōtastahm, usually analysed as rōd/raod- 'growth, stature' (or 'river', per Wiktionary) + stahm 'strength, force' < *staxma- (cf. Av. staxra-); Hübschmann already compared tahm, but the attested -stahm makes Nourai's 'raodha-taxma' only an approximation.
```


## [2026-10-17T00:05:36.735Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"gurba\\b\\|gurbah\\|gurbe\" \"^ *[0-9]*\\. *bär\\|^ *[0-9]*\\. *bâr\\|^ *[0-9]*\\. *bār\" \"hamvär\\|hamvâr\\|hamvār\\|hamwär\" \"rübäh\\|rōbāh\\|rubāh\\|rübah\" \"tahmür\\|Tahmür\\|tahmūr\" \"vär 'Art\\|-vär\\|-vâr\\|-vār\"; do echo \"### $p\"; grep -n -i \"$p\" HRN.txt | head -5 | cut -c1-300; echo \"-- HUB\"; grep -n -i \"$p\" HUB.txt | head -4 | cut -c1-300; done"
}
```


### [2026-10-17T00:05:37.261Z] TOOL RESULT

```
### gurba\|gurbah\|gurbe
-- HUB
### ^ *[0-9]*\. *bär\|^ *[0-9]*\. *bâr\|^ *[0-9]*\. *bār
1767:159. bärän *Regen', bartden regnen', baris, bärgln,
-- HUB
### hamvär\|hamvâr\|hamvār\|hamwär
-- HUB
### rübäh\|rōbāh\|rubāh\|rübah
-- HUB
### tahmür\|Tahmür\|tahmūr
-- HUB
### vär 'Art\|-vär\|-vâr\|-vār
1768:g. he-väre 'es regnet'; mäz. väris; Käs. vörün etc.
11641:et-väre 80,
-- HUB
```


## [2026-10-17T00:05:40.352Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==263' HRN.txt | head -80 | cut -c1-200; echo =====; grep -n \"Katze\" HRN.txt HUB.txt | head; grep -n \"Fuchs\" HRN.txt | head -5"
}
```


### [2026-10-17T00:05:40.920Z] TOOL RESULT

```
Exit code 1
— 241 -
Nicht hierher gehören die Suffixe -var in seriär
löwenhaft' (Sahn. I, 253 Vers 166) oder in selvär
(No. 789) u. a. m.
Das Suffix -awer (z. B. np. jengäwer) ist erst neu-
persisch.
1074. wäriin unglücklich, elend, schlecht*, tcärilne^).
phlv. apärün, aparumh.
Zusammengesetzt aus apa und phlv. rün (das 'Seite,
Richtung zu bedeuten scheint), also eigentlich 'ab-
seits ; vergl. phlv. frarün.
1075. valäne, velane (so im Gazophylacium S. 389)
'Wunde*.
skr. rrand' Wunde* , wozu doch gewiss auch lat.
volmts^) gehört.
1076. veyiMür^ vu/sür 'Prophet' ).
phlv. va/sivar (Denkart); de Lagarde, Ges. Abh.
164 nimmt als Grundform aw. "^va/sahara- an (vergl.
va/sem möi asqsatj vd. 19, 15).
1077. vefif 'Grösse, Würde'.
aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
reich, prangend*; phlv. varc bezw. varj, varcömamJ
bezw. varjömand (vergl. Salemann, Mel. asiat. IX,
235 Note 35); ai. vdrcas- 'Glanz.
Den von Salemann a. a. 0. citirten FirdüsT-Vers
konnte mir Herr Dr. Landauer nicht nachweisen.
H Häufig mit wazün in den Handschriften verwechselt. Dieses,
sowie wäzüue ist sicher aus bäzyüne (Öähn. I, 197 Vers 1220) ent-
standen, rergl. cün etc. s. v. yün (No. 946).
2) tJber dieses Wort vergl. 0. Hoffmann, BB. XVIir, 291,292.
') In unserem Texte des äähnSme ist in den im FJ angeführten,
von de Lagarde erwähnten Versen ve-^mr durch peiyewber ersetzt
(I, 6 Vers 95); in der Strassburger Handschrift des Ferheng stehen
sie auf Fol. 162 und lauten folgendermassen :
hegnftär-l re/sür-t /ud räh^jöl
d%l ez ieregihä hedln Wf söi
Aus Firdüsl's jQsuf und Zulei;^ä wird ebendaselbst die folgende
Strophe citirt:
bt(/ö ei ;(%reilmend ez in der sü/un
qtyäse zt ve/8ür-i dädär^ hm.
Auch SF hat einen Belcgvors für das Wort.
Uorn, UruDdrUs d. neup. Etyniolugfie. 1(>
(eval):1: ==== not found
```


## [2026-10-17T00:05:42.595Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==262' HRN.txt | tail -40 | cut -c1-200"
}
```


### [2026-10-17T00:05:42.928Z] TOOL RESULT

```
240 —
V, w.
1071. if, ü (§ähn. I, 25 Vers 37) und*.
ap. tää auch, und'; aw. uta; phlv. u (päz. ?/).
Bei diesem vielgebrauchten Worte ist die nicht
lautgesetzliche starke Verkürzung durchaus erklärlich.
Die Aussprache ve (die wohl AM. noch nicht hat,
vergl. z. B. S. 82, Zeile 3 v. u.) ist Nachahmung des
arab. va und* oder dieses ist selbst entlehnt worden.
Oder gehört np. ü und' zu gr. av, got. auk etc.
(vergl. Kluge, Wörterbuch s.v. auch)? Man sollte
aber doch wohl eine Anknüpfung der Partikel im
iranischen Gebiete erwarten können.
wä *offen', siehe baz (No. 163).
1072. väj 'sprich', vergl. vat 'Wort, Rede' (dialektisch^),
guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
g. vätrnun 'sprechen' (vergl. Justi, ZDM6. 36,
403, 404) ; Käs. Q. K. vöj^ 7j, vaz (s. v. f^eda kerden),
Käs. V. bivötdn, Impt. böj, Q. vötin, bavöten, Praes.
avöjün, K. vötmün^ Impt. hSvöJtd^ Z. bSvöt, Praes. vözön
'sprechen' (s. v. giiften).
aw. {/"vac-y vaocat 'sprechen' ; phlv. väöak 'Stimme',
väc (päz. väz) *Gebet'; ai. l/vac-^ vivakti, vdc- *Wort\
kurd. vdtin, vergl. bezium 'ich sage, spreche' etc.
(Justi, No. 408.)
Das in den Dialekten noch heute allein gebräuch-
liche Verbum ist schon im PehlevT fast verschwunden.
1073. "WäTj -wäre, tver (ür)^), Suffix 'tragend, versehen
mit'.
ap. -bara- in taka]bara' 'tragend'; aw. gada^vara-;
phlv. 'bar in datbar (neben datwar), dastbar, m(i)zdbar,
'tvar, war in nmetwär, öjwar^ ranjfwar; arm. -ber^
z. B. Insaber, -avor^ z. B. lusavor.
M Belegt durch einen Vers des Mir NezmI.
V
*J In mizdür Sahn. (M oh 1) VI, 152 Vers 330, genjür^ renjür u. a. m.
```


## [2026-10-17T00:06:16.335Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"gurba\\|gurbak\" SYN.txt | head -3 | cut -c1-300; grep -n -i \"Adolph\" SKT.txt FSD_vol1.txt WEB_vol1.txt | head -3 | cut -c1-200; grep -n -i \"^ *ulpo\\|lupos\\|ulpēs\\|uḷpē\\|urupi\" IEC.txt | head -5 | cut -c1-300; grep -n \"urupi\\|gurba\" incoming/WLD/WLD_Bd1_pages.txt | head -5 | cut -c1-300"
}
```


### [2026-10-17T00:06:16.686Z] TOOL RESULT

```
15683:9.76 BASKET Grk. Kégtvos, x&Xafos, etc. Goth. tainjo, snorjo Lith. gurbas NG Kanébt, xopive ON — laupr, teina Lett. kurvis, gruozs Lat. _corbis, calathus, ete. Dan. kurv ChSl.  kodt, krabtjt It. cesta, canestra, pa- Sw. korg SCr. ko, kotarica (korpa) niere, corba OE  t@nel, windel, wilige Boh.
15710:2. Lat. corbis (> It. corba; late dim. corbicula > Fr. corbeille), orig. dub., pos- sibly with notion of plaiting from bend- ing : Russ. korobit’ ‘bend’, ON herpask ‘contract’, ete.; or may be a loanword fr. some Mediterranean source. Lat. cor- bis is the source of the Gmc. words, Dan. kurv, S
15733:5. Lith. gurbas, Lett. kurvis, above 2 under Lat. corbis.
WEB_vol1.txt:99786:In-ter-na/tion-dle (or Fr. an-ter-na-sy6-nal’), n. a revolutionary socialist hymn written in 1871 by Eugène Pottier, with music by Adolphe Degeyter.
FSD_vol1.txt:9550:ag'a-plilte,  1   ag'e-fait;  2   Hg'a-flt,  «.  A   variety  of Persian  turquoise.  [   <   Agaphi,  a   naturalist.] a'gari,  n.  Same  as  agar-agar.— hydrocele  agar,  a   sub- 
FSD_vol1.txt:37267:Ltitzen,  Prus.:  Nov.  16,  1632:  Swedes  led  by  Gustavus Adolphus  def.  Wallenstein  and  Imperialists;  Swedish king  fell.  lists  and  destroyed  city.
19287:tulupos, å “lump, ball, mass, crowd’ Per. turb (‘radish’; LW in Tk. turp, id.); Gk. tolüpe, f. ‘ball of thread’; Alb. tulup, m. (‘col- lop of meat, spg. infl. by tul ‘lean meat, see tul- (4) beside tullupan, adj. ‘bald’); OCS tlüpa, R tolpà, Cz. tlupa “crowd, gang’; ambig. Ir. tola, gs. id., f
30197:   Av. urupi-s m. (frupi-s) „eine Art Hund", raopi-s ebenso („Fuchs,
```


## [2026-10-17T00:06:19.650Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30185,30215p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-250; grep -n \"pdf page\\|^\\[leaf\\|Seite\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<30197' | tail -1; grep -n \"„drehen, winden\\|uel- „drehen\\|ṷel- „drehen\\|„wälzen\" incoming/WLD/WLD_Bd1_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:06:20.023Z] TOOL RESULT

```
die Zuruckfiihrung von * wulfs usw. auf *ulpos durch Zupitza Gutt. 16);
lit.   vilkas     lett.   vilks,       apr.   wilkis           „Wolf“, lit. vilke „Wolfin“ (lett. ulks,
vulks „Wolf“ aus dem Russ.,                       s.       Endzelin KZ. 44, 61); abg. vhkh, russ. volkz
.Wolf".
   Curtius 161, Osthoff aaO. m. Lit., Vf. LEWb. 2 u. lupus.  Yielleicht als
„reiBendes Tier" eine Ableitung von uel- „rei6en“ (s. d.) in lat. vello, vol-
tur usw., was gleicherweise fur ul-p- (s. d.) in Betracht kommt.


uJP- 1«P- in Raubtierbezeichnungen, bes. aus dem Hundegeschlecht (Fuchs,
    Schakal, Wolf).
      Lat. volpes „Fuchs", valpe-cula,                         lit.       vilpikys „wilde Katze“.
   Av. urupi-s m. (frupi-s) „eine Art Hund", raopi-s ebenso („Fuchs,
Schakal"), mpers. ropds, np. robah Fuchs" = ai. lopagd- (auch lopdka-) m.
                                                               ,,


„ Schakal, Fuchs"; arm. alues „Fuchs‘   gr. aktbm]£, -xog ds. (s. u.);
                                                                      £

                                                                          ;

   lat. lupus „Wolf“ (kaum wahrscheinlicher zu *ulq u os, s. d.); abret.
                                                                         acorn.
louuern „Fuchs“, nbret. louarn ds., gall. Aovegvio; MN., acymr. Cruc Leuyrn
ON., ncymr. Llywernog ON. *lup-erno s. Pedersen KG. I 92, II
                              (                                     53);
  lit. Idpe Fuchs", lett. lapsa „Fuchs“ (synk. etwa aus *lapesa, -isa).
  Ygl. Spiegel KZ. 13, 366, Bersu Gutt 143, Zupitza Gutt. 16, Hiibsch-
mann KZ. 26, 603; Fick I 4 556, II 4 256, Yf. LEWb. 2 u. lupus, volpes, und
nun bes. Schulze KZ. 45, 287 f.
29768:m. Lit.);        mit derselben Bed. „all“’ aus „nach alien Seiten auseinander-
22473: liegen (s. sue>~; aber auch in der Bed. „drehen, winden" z. B. anord. sveipr
24477:1. uendh- „drehen, winden, wenden, flechten                                              .
25654:s. *ualg- unter *uel- „drehen").    Unter der Yorstellung des unwilligen
27665:seits Zugehorigkeit zu *uerg- „drehen, winden                    ,
28185:544 f. Urspriingliche Gleickheit mit *uel- „drehen” (^so Sommer Gr. Ltst. 112,
```


## [2026-10-17T00:06:23.947Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 incoming/WLD/WLD_Bd1_pages.txt; grep -n \"^\\[\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<30200' | tail -2; grep -n \"uel- „drehen\\|1\\. *uel-\\|uel- „wälzen\\|uel- „rollen\" incoming/WLD/WLD_Bd1_pages.txt | head"
}
```


### [2026-10-17T00:06:24.277Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                                DER


     INDOGERM ANISCHEN SPRACHEN

                HERAUSGEGEBEN UND BEARBEITET
                                VON

                     JULIUS POKORNY


                           I.   BAND


VM   /




                   BERLIN UND LEIPZIG 1930

              WALTER DE GRUYTER & CO.
  23635:[*udri-s „ * Wasserschlauch", vgl. gr. vdota Thurneysen KZ. 32, 563), Ultra             :
28811:[ulE-d-    ulo-d-; Fick III
25654:s. *ualg- unter *uel- „drehen").    Unter der Yorstellung des unwilligen
27848:1.   uel- „seken".
28185:544 f. Urspriingliche Gleickheit mit *uel- „drehen” (^so Sommer Gr. Ltst. 112,
28208:        zu *uel- „drehen“ („Kraushaar a u. dgl.) ist fiir mebrere der hier (ob
28253:     Uber gr. ovlog „kraus"' s. u. uel- „drehen“.
28289:8. unter *uel- „drehen“), lit. vdltis „Haferrispe, Haferspelte“ (aucb „Garn,
28290:Fischernetz <£ s. *uel- „drehen“; auch „Kahn mit flachem Boden“, in welcber
28376:7.      uel- „drehen, winden, walzen". vollere Basenformen '*uelv-, *vcl(e u-,
```


## [2026-10-17T00:06:27.148Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28376,28420p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200 | grep -v \"^\\s*$\""
}
```


### [2026-10-17T00:06:27.456Z] TOOL RESULT

```
7.      uel- „drehen, winden, walzen". vollere Basenformen '*uelv-, *vcl(e u-,
          *u'e)lei- fdiese auch „umwinden, einwickeln = einhiillen").
       Ai.      vrihiti,          -te    ,,wendet      sich,   dreht         sich",     kaus.    vdlmjati          ..macht       sich
wenden, rollen", vnlanam „das Sichwenden, Sichbiegen, wallen, wogen"',
vala- m. „Bedeckung, Holile" (oder zu *ucr-l), vain-, vnlahi- m. etwa
..(runder) Balken, Stange" (Johansson IF. 3, 247), dehnstufig rakra-viVa- n.
,,Reif, Ring, Kreis, Menge", dla-vnln- n. ,,Yertiefung um die Wurzel eines
Baumes, in die das fur ihn bestimmte Wasser gegossen wird (zum I. Glied                                   •'
eine Yermutung bei Uhlenbeck Ai. Wb. 22        wohl auch vara- m.    * Wen-         ,
dung) Reihe, Folge, mal, Wochentag" s. Persson Beitr. 542 m. Lit. Yf.         >
LEWb. 2 u. hornu s, sc-tneh = np. btlr ,,mal"; vain- m. ficus indica" (,.sich
windend", von den Luftwurzeln des Baumes), vgta- m., vail f. Strick" (un-                                      ,
belegt), vala-, vatnha- m. „KloBchen“, vatl, raided „Kiigelchen, Pille";
va nd- m., raid „Rohr, Rohrstab" (s. auch u. lat. valli/s).
   Von der set-Basis ai. fir mi- m. f. „Woge, Welle", av. varomi ds.
        Unrichtig scheint mir der Vergleich der halt. Sippe (tc el- ml-, wozu util- sekun-
       *)                                                                                         :
diir)  mit anord vela „bestricken“ von ril f. . konst, Kniff, Werkzeug‘ (mi-, in- mit For-
mans -lo-) dureh Trautmann Grm. Lautges. 35, Apr. <09, Fick 111*413, Falk-Torp u.
i'0le.  Petersson Fort Regel 26.                       —
                                     Ob ai. rrthd T umsonst, vergebens, veikehrt", altcst
.leicht, ohne Miihe* mit lit. reltui usw. verwandt sei (Fick II * 275), ist sehr unsieher
keinesfalls ist nach Uhlenbeck Ai. Wb. 29 mit rrthe nur reltui zu vergleichen und letz-
                                                                  1
teres von ap-filti usw. zu trennen, um diese auf eine i- Wz. beziehen zu konnen.
                                                        uel-                                                  299
```


## [2026-10-17T00:06:31.383Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30140,30260p incoming/WLD/WLD_Bd1_pages.txt | grep -n \"  3[01][0-9]\\s*$\\|^ *3[01][0-9] \" | head; grep -n \"ARY\\|gorbe\\|GORBE\\|GURBAK\\|TAHMURAS\\|TAXMA\" incoming/ARY/ARY_latin_index_pages.txt | grep -i \"gurb\\|gorb\\|taxm\\|tahm\\|urupi\" | head"
}
```


### [2026-10-17T00:06:31.725Z] TOOL RESULT

```
26:                                                                      iu P-                                              317
5522:(SANSKRIT) 2 Sails TAXMA HAVESTAN) gle)
5842:TANK -(TOKHARIAN B) B 5 5 ‘TAXMA, TANGCISHTA
```


## [2026-10-17T00:06:34.848Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n \"گربه\\|هموار\\|روباه\\|طهمورث\\|تهمورث\" ARY_pages.txt | head -8 | cut -c1-200; grep -n -i \"URUPI\\|RAOPI\\|GURBAK\\|VAREMI\\|VARAMI\\|ROBAH\\|HAMVAR\" ARY_latin_index_pages.txt | head | cut -c1-250"
}
```


### [2026-10-17T00:06:35.116Z] TOOL RESULT

```
15588:۶ ا۱ هامون, هامن (به چم *دشت هموار»)
2900:VAREMIS AVESTAN) plurs\ :
8909:REV (NORWEGIAN) «5335 URUPI, RAOPL HAVESTAN) gem 3)
8910:LAPE, > (LITHUANIAN) gl) ROPAS, ROBAH =— (PAHLAVI) «5,4
12426:POKORNY. —=~SO*~*~S~S~*~«a URUPIS SANSKRIT) 2 Sila
```


## [2026-10-17T00:06:37.207Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; for l in 2900 8909 12426; do grep -n \"pdf page\" ARY_latin_index_pages.txt | awk -F: -v L=$l '$1<L' | tail -1; sed -n \"$((l-12)),$((l+8))p\" ARY_latin_index_pages.txt | cut -c1-150; echo ----; done"
}
```


### [2026-10-17T00:06:37.794Z] TOOL RESULT

```
2883:[pdf page 102]
HOLD CHURCH) of 53%
‘REFERENCES beth VETRU, VEJO, VEJATI
POKORNY: ——SOS*~*~*~S*S*S«S WIATR POLISH) long!
BARNHART: (WIND) 1238 VETER (RUSSIAN) guy
DELAMARRE: (VENT) 192 vITR (CZECH) Soy
MACKENZIE: (WIND) 140 VITR (BOHEMIAN) aay
ONIONS: 67, 683 (WIND) 1007 VIETOR (SLOVAR) hel
BUCK: 61, 683 VEJAS LITHUANIAN) gp)
SKEAT: (WIND) 717 VEISH LATVIAN) (3) 9)
red ebb dbp WINS {OLD PRUSSIAN) oS e+.
FETH HOLD IRISH) eyS' 52432)
|
VAREMIS AVESTAN) plurs\ :
BAR PAHLAVI) 5 34g |
"REFERENCES bey SANSKRIT) <n, Sule i
POKORNY. = SSS*S*~*~«d VALATI, VALA, VARA |
MACKENZIE: 7 OLD HIGH GERMAN) ff gist
ri sabi oly WALLON, wal 3
woe 4A
BER, BAR (KURDISH) 3,5 BAR, BERETI, AAVESTAN) gli!
(SANSKRIT) oy Site BaRgTISH
----
8897:[pdf page 308]
[pdf page 308]
ra] SS) |
|
REZO, REHMA, GREEK) gli RANG (PAHLAVI) 6 shy
RAHEUS RENG, RENK (KURDISH) 52,5
RANG ABALUCHI) sh
‘REFERENCES beth RANG AFGHAN) (4) sli)
POKORNY, —=—SSs=~<CS~*~“CS*~*« RAJVATI, RAGA, (SANSKRIT) cy Site
MALLORY & ADAMS: REG- RAJYATE, RANJAYATI, RANGA
ad seb day ERANG ARMENIAN) ga
|
|
REV (NORWEGIAN) «5335 URUPI, RAOPL HAVESTAN) gem 3)
LAPE, > (LITHUANIAN) gl) ROPAS, ROBAH =— (PAHLAVI) «5,4
VILPISHYS ROWE KURDISH) 53,5
LAPSA, RUADH (LATVIAN) (53) 39) ROPASK HBALUCHI) jh
RUADH (OLD IRISH) gS 5) p\ LOPASA (SANSKRIT) a Sudo
LOUARN HBRETON) 52 LOPAKA, LOPASAS
ALUES + JARMENIAN) 5!
‘REFERENCES beth ALOPEKS GREEK) gli,
POKORNY = SSSOS*~«*CTS VOLPES MATIN) ga 4
----
12418:[pdf page 426]
ONIONS: (GRAVE) 411 GREU RUMANIAN) «gay,
SKEAT: (GRAVE) 248 GRAVE (PORTUGUESE) Js x
AMINDAROV: (HEAVY) 235 KAGRUS GOTHIC) SF
YVAN L eu oly :(OLD SCANDINAVIAN) 48 44!
[pdf page 426]
mies
detlasl
Bish gh Tiga call 2 03s ol
Obi 2 039 gh gle) 32 059 onl
feet re |
*URPA (OLD PERSIAN) ky eo
‘REFERENCES bch GURPAK, GURBAG  :(PAHLAVI) 5 hy |
POKORNY. —=~SO*~*~S~S~*~«a URUPIS SANSKRIT) 2 Sila
war | sbi Oey GADOU ARMENIAN) 31
icetlook
HGSGATO pile) CHAT gests y CATUS oS yKATZE gliT 5 CAT poJ63i laejly lt
hts Lead Uy i pST Sly gel el tiie Lalita, ly et ly LA eel A rly coe
(BARNHART: 149)
GARDER GaRgDHO AVESTAN) poe 3b
HOLD SAXON) 5 gip-Sle *  SKRTA (OLD PERSIAN) ileal, gs
GARD, GARDO KART | APAHLAVD) 5 34
----
```


## [2026-10-17T00:06:42.511Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *41[01][0-9] \\|time, occasion\\|\\btimes\\b\" SOD_pages.txt | head -8 | cut -c1-200; grep -n -i \"wʾr\\|w'r \" SOD_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:06:42.958Z] TOOL RESULT

```
2001:                                                           separate work, times permitting.
2056:indefinite at times in connection with recognising the        endings as well as gender and number indicators
2242:times. Politically, h>wever, they were probably              Chinese silk to go westward and for Buddhism and
2378:           The materials mentioned above show the extent                 the materials belong to different times.
15398:                                                             4110 Ymp- C => Ymb-
15406:                                                            4112 Ympnbry C                     ^^aiJ^c^^}^/
15417:4100 Y$nyw -* Y^n'yw
15418:4101 Y«wk    S                (<Sjj£ :J^-O^      *j^h^      4114 Ympwn S, C =» YnP>wnn
7649:      wool-stuffed saddle ?                                         1358 'ptyw'r B                                      Jy~^/
24606:7266 prwV      B => prw'r                                       parwick ? ©<OP paruva-
35364:                                                               10912 y'tyw'r =» y'tywVk                          J* /
```


## [2026-10-17T00:06:50.477Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -i -m3 \"Athal\\|Adalwolf\\|Old High German\" a4e7fabbff16daed.txt | cut -c1-300; grep -v \"^\\s*$\" abcf747a3264a4ba.txt | tail -15 | cut -c1-200"
}
```


### [2026-10-17T00:06:50.811Z] TOOL RESULT

```
 From Old High German adal ( “ noble ” ) + wulf ( “ wolf ” ) . Doublet of Ethelwolf from Old English Æþelwulf .
 From Old High German adal ( “ noble ” ) + wolf ( “ wolf ” ) .
 a male given name from Old High German, equivalent to English Adolph 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct 
 Developers 
 Statistics 
 Cookie statement 
 Mobile view 
 Search 
 Search 
 Toggle the table of contents 
 طهمورث 
 5 languages 
 Add topic
```


## [2026-10-17T00:09:48.775Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-541.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nV=\"https://vajehyab.com/\"\nPOK1144={\"ref\":\"POK:1144\",\"status\":\"supports\",\"note\":\"POK_full.txt l.90699ff. 'Root / lemma: uel-8 / Meaning: to tear, wound; to steal ... np. valana, valāna \\\"wound\\\", Latin volnus ... Latin vello, -ere ... pluck, tear, rend ... References: WP. I 304 f. ... Page(s): 1144-1145'. Root, gloss and number match Nourai's box.\"}\nPOK1179={\"ref\":\"POK:1179\",\"status\":\"partial\",\"note\":\"POK_full.txt l.93126ff. 'Root / lemma: ulp-, lup- ... Meaning: a kind of carnivore (fox, wolf) ... Avestan urupi-s (*lupi-s) \\\"dog\\\", raopi-s \\\"fox, jackal\\\". Middle Persian rōpās, npers. rōbāh ... Middle Persian gurpak, npers. gurba \\\"house cat\\\", from Iran. *urpa-, Indo Germanic *ulpos, it concerns certainly various taboo adjustments. Page(s):1179'. The forms are there; Pokorny does NOT attach them to uel-8 'tear' (he treats them as taboo variants beside *ulkʷos 1178).\"}\nPOK1140={\"ref\":\"POK:1140\",\"status\":\"supports\",\"note\":\"POK_full.txt l.90462ff. 'Root / lemma: uel-7 ... Meaning: to turn, wind; round ... vāra- m. \\\"(* turn) row, Folge, mal, Wochentag\\\" = npers. bār \\\"mal\\\"; from ul-mi-: Old Indic ūrmi- \\\"surge, wave\\\", Avestan varəmiš ds.; ... Avestan varənavaiti \\\"bedeckt, hüllend\\\" (contain partly Indo Germanic *uer-5), das Avestan word also \\\"wendet (sich)\\\" ... Page(s): 1140-1144'.\"}\nWLD298={\"src\":\"WLD\",\"where\":\"Bd. I 298-299 (WLD_Bd1_pages.txt l.28376ff.)\",\"stance\":\"supports\",\"note\":\"'7. uel- „drehen, winden, wälzen“ ... ai. ... vāra- m. „Wendung, Reihe, Folge, mal, Wochentag“ ... = np. bār „mal“ ... Von der set-Basis ai. ūrmi- m. f. „Woge, Welle“, av. varəmi ds.'\"}\nWLD316={\"src\":\"WLD\",\"where\":\"Bd. I 316-317 (WLD_Bd1_pages.txt l.30188-30215)\",\"stance\":\"supports\",\"note\":\"s.v. *ulqʷos 'Wolf': 'Vielleicht als „reißendes Tier“ eine Ableitung von uel- „reißen“ (s. d.) in lat. vello, voltur usw., was gleicherweise für ul-p- (s. d.) in Betracht kommt.' Then 'ul-p-, lup- in Raubtierbezeichnungen, bes. aus dem Hundegeschlecht ... Av. urupi-s m. „eine Art Hund“, raopi-s ebenso („Fuchs, Schakal“), mpers. rōpās, np. rōbāh'. This is the scholarly basis of Nourai's arrow from 'tear' to the wolf/fox words.\"}\nAHDwel3={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wel-3\",\"stance\":\"supports\",\"note\":\"AHD_watkins1985.txt l.1140: 'wel-3. To turn, roll ... 3. Perhaps Germanic *wel- in Old English welig, willow (with flexible twigs): WILLOW. 4. Perhaps Germanic *welk- in Old English wealcan, to roll, toss ...: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< \\\"rolling or bubbling water,\\\" \\\"spring\\\"): WELL ... 7. ... b. Latin volvere, to roll: VAULT, ... VOLUME, ... INVOLVE, ... REVOLVE ... d. ... Latin valva, leaf of a door: VALVE ... 9. Perhaps variant *wall- in Latin vallēs, vallis, valley: VALLEY ... 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. [Pok. 7. wel- 1140.]' No WALLET.\"}\nnodes0=[\n {\"id\":1,\"lang\":\"Indo-European\",\"words\":\"Wlp, Ulp, Lup\",\"verdict\":\"plausible\",\n  \"derivation\":\"Pokorny 1179 sets up *ulp-, lup- 'a kind of carnivore (fox, wolf)' (Lat. volpēs, lupus; Av. urupi-, raopi-; Lith. lapė; Gk. alṓpēx) and treats them as taboo deformations parallel to *wl̥kʷos 'wolf' (1178); Watkins has *wlp-ē- 'fox' [Pok. 1179]. Modern work (Wiktionary *h₂wl̥pis) keeps these as a fox/wildcat word separate from *wl̥kʷos. Nourai hangs them under *wel- 'to tear', i.e. 'the tearing animal'. Walde-Pokorny I 316-317 explicitly offer this ('vielleicht als „reißendes Tier“ eine Ableitung von uel- „reißen“ ... gleicherweise für ul-p-'), but Pokorny's 1959 IEW leaves it out, so the attachment is a possible old proposal and not established. The gloss 'dog' comes only from Av. urupi-.\",\n  \"derivation_fa\":\"پوکورنی (ص ۱۱۷۹) برای نام‌های جانوران درنده‌ای چون روباه و گرگ ریشهٔ *ulp-/lup- را می‌آورد (لاتینی volpēs و lupus، اوستایی urupi- و raopi-) و آن‌ها را دگرگونی‌های تابویی در کنار *wl̥kʷos «گرگ» می‌داند. والده و پوکورنی (ج ۱، ص ۳۱۶-۳۱۷) با «شاید» پیشنهاد کرده‌اند که این نام‌ها به معنای «جانور درنده» از ریشهٔ *wel- «دریدن» باشند، ولی پوکورنی در فرهنگ ۱۹۵۹ این پیوند را نیاورده است. پس صورت‌ها درست‌اند، اما بستن آن‌ها به ریشهٔ «دریدن» تنها با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"گربه\",W+\"روباه\"],\n  \"ref_check\":[POK1179],\n  \"consulted\":[WLD316,\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wlp-ē-\",\"stance\":\"partial\",\"note\":\"AHD_watkins1985.txt l.1172: 'wlp-ē-. Fox. 1. Latin vulpēs, fox: VULPINE. 2. Taboo variant *alōpek- in Greek alōpēx [Pok. ulp-, lup- 1179.]' and 'wlkwo-. Wolf ... 2. Taboo variant *lupo- in Latin lupus' -- listed as separate roots, no link to wel-4 'to tear, pull'.\"},\n   {\"src\":\"POK\",\"where\":\"1178 s.v. ulkʷos\",\"stance\":\"partial\",\"note\":\"Pokorny derives *ulkʷos rather from *u̯lek- 'to shine' ('similarity of sparking beastly eyes in the dark') and notes Latin lupus, Avestan raopi- may belong together 'or at least be influenced by such a root' -- no mention of uel-8.\"}]},\n {\"id\":2,\"lang\":\"Avestan\",\"words\":\"urpa, urupis, lupis, raopias; taxma-urupa\",\"verdict\":\"plausible\",\n  \"derivation\":\"Avestan urupi- (nom. urupiš) is 'a kind of dog' (Vd. 5.33 spā urupiš; Bartholomae 'Name einer Art des Hundegeschlechts') and raopi- (Vd. 13.16) is another canine, 'fox, jackal' (= Skt. lopāśá-). Both are real and both are Pokorny's *ulp-/lup- words, with Iranian *rūp-/*urup- from *(H)wl̥p-. But 'urpa' is only a reconstructed Iranian *urpa- (Pokorny, behind MP gurbag), 'lupis' is Pokorny's bracketed pre-form *lupi-s, not an Avestan word, and 'raopias' is a garbled raopiš. Taxma Urupi (nom. taxmō urupa, Yt. 15.11, 19.28) is the name of the second Pishdadian king, taxma- 'strong, brave' + urupi-. Bartholomae leaves the meaning open ('Eig. Bed.?'), so the gloss 'with strong dogs' is only one possible reading.\",\n  \"derivation_fa\":\"در اوستا urupi- (نهادی urupiš) نام گونه‌ای سگ است (وندیداد ۵.۳۳) و raopi- نام جانوری از تیرهٔ سگان، روباه یا شغال (هم‌ریشه با سنسکریت lopāśá-). هر دو واژه در اوستا آمده‌اند. ولی urpa تنها صورتی بازسازی‌شده در ایرانی باستان است و lupis صورت فرضی پوکورنی است که در اوستا نیامده است. «تخمه اوروپی» (taxmō urupa) نام دومین پادشاه پیشدادی است، از taxma- «دلیر، نیرومند» و urupi-. بارتولومه معنای دقیق این نام را روشن نمی‌داند، پس معنای «دارندهٔ سگان نیرومند» تنها یک برداشت است.\",\n  \"sources\":[W+\"روباه\"],\n  \"ref_check\":[POK1179],\n  \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"col. 1534 (urupay- 1 and 2), col. 1489 raopay- (BRT.txt l.25520-25526, 24960)\",\"stance\":\"supports\",\"note\":\"'urupay- m. (auch mit span- m.) Name einer Art des Hundegeschlechts: ... V.13.16; spā °piš V.5.33'; 'urupay- m. EN. des zweiten iranischen Königs, eines ältern Bruders Yimas ...: taxmō °pa (NS.) azinavā Yt.15.11 ... Eig. Bed.? ... Später Taxmūraf, Tahmūras genannt'; 'raopay- m. Name einer Art des Hundegeschlechts'.\"},\n   WLD316,\n   {\"src\":\"ARY\",\"where\":\"pdf p. 308 (ARY_latin_index_pages.txt l.8909)\",\"stance\":\"supports\",\"note\":\"s.v. روباه: 'URUPI, RAOPI (AVESTAN) ... ROPAS, ROBAH (PAHLAVI) ... LOPASA (SANSKRIT) ... VOLPES (LATIN) ... REFERENCES POKORNY'.\"}]},\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"gorbeh; Tahmŭres\",\"verdict\":\"plausible\",\n  \"derivation\":\"gorbe 'cat' < MP gurbag (MacKenzie 'cat gurbag'; Nyberg 'gurbak cat ... NP gurbah') < Proto-Iranian *wr̥pa-ka- (Wiktionary), i.e. the Iranian *urpa- that Pokorny 1179 and Aryanpur put beside Av. urupi-. Initial *w- before the syllabic r gives MP gu-, as in gurg < *wr̥ka-. So gorbe is a cognate formation of urupi- and does not come from the attested Avestan word itself. Nourai's gloss 'an animal that tears up' is his own reading of the root, not a recorded meaning. The bracketed روباه rubāh is right: MP rōbāh/rōpās < *raupāsa-, cognate with Av. raopi- and Skt. lopāśá-. Tahmūras/Tahmūrath (طهمورث، تهمورث) < MP Taxmōrup/Tahmōraf < Av. Taxma Urupi. The ث/س ending reflects Arabic-script renderings of the final -f/-p, and ط is an Arabicising spelling of ت. The gloss 'with strong dogs' is speculative.\",\n  \"derivation_fa\":\"«گربه» از فارسی میانهٔ gurbag (مکنزی، نیبرگ) و آن از ایرانی باستان *wr̥pa-ka- است. w پیش از r هجایی در فارسی میانه گُ شده است، چنان‌که در «گرگ» از *wr̥ka-. پوکورنی و آریان‌پور این واژه را در کنار اوستایی urupi- می‌آورند. پس «گربه» با urupi- هم‌ریشه است، ولی از خود آن واژهٔ اوستایی برنیامده است. معنای «جانور درنده» برداشت خود نورایی است. «روباه» از فارسی میانهٔ rōbāh و هم‌ریشه با اوستایی raopi- است. «تهمورث / طهمورث» از فارسی میانه Taxmōrup و اوستایی Taxma Urupi است. ث و ط در این نام نشانهٔ نگارش عربی است. ادعای نورایی در کلیات پذیرفتنی است.\",\n  \"sources\":[W+\"گربه\",W+\"روباه\",V+\"moein/گربه\"],\n  \"ref_check\":[\n   {\"ref\":\"BQT:968\",\"status\":\"not_checked\",\"note\":\"tools/ref_page.py: 'no scan of BQT covers printed page 968'. Printed 968 falls in vol. 2 (ج–خ), where neither گربه (vol. 3, گ) nor تهمورث (vol. 1, ت) stand. In BQT_v3_pages.txt l.11564 (pdf 156) 'طهمورث ... پادشاهی بود از ... هوشنگ' with footnote 'تهمورث'; BQT_v1_pages.txt l.32059 'تهمورث - رك: تهمورس'.\"},\n   {\"ref\":\"MON5:405\",\"status\":\"not_checked\",\"note\":\"Mo'in vol. 5 (proper names) is not online; vajehyab has no Mo'in entry for طهمورث (HTTP 404).\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"English index, 'cat'\",\"stance\":\"supports\",\"note\":\"PHD.txt l.1172 'cat gurbag.'\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. gung (NYB_vol2_glossary.txt l.1739)\",\"stance\":\"supports\",\"note\":\"'— = NP. gurbak [gwlbk'] cat 101. — NP gurbah.'\"},\n   {\"src\":\"ARY\",\"where\":\"pdf p. 426 (ARY_latin_index_pages.txt l.12420-12426)\",\"stance\":\"supports\",\"note\":\"s.v. گربه: '*URPA (OLD PERSIAN) ... GURPAK, GURBAG (PAHLAVI) ... URUPIS ... REFERENCES POKORNY'.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. گربه\",\"stance\":\"partial\",\"note\":\"'(گُ بِ) [په.] (اِ.) حیوانی است پستان دار و گوشت خوار ...' -- Pahlavi origin, no further etymology.\"},\n   {\"src\":\"HRN\",\"where\":\"grep gurba/gurbe/Katze\",\"stance\":\"silent\",\"note\":\"no entry found in the OCR.\"}]},\n {\"id\":4,\"lang\":\"Old High German\",\"words\":\"athal-wolf\",\"verdict\":\"confirmed\",\n  \"derivation\":\"OHG Athalwolf, Athaulf, Adulf, Adolf is a Germanic dithematic name: athal/adal 'noble lineage' + wolf 'wolf' (< PGmc *wulfaz < PIE *wl̥kʷos). The second element is the wolf word itself, so it belongs here only through the wolf/'tearing animal' idea. The compound and gloss are standard (Klein; Wiktionary Adolf).\",\n  \"derivation_fa\":\"نام آلمانی کهن Athalwolf / Adolf از دو جزء ساخته شده است: athal / adal «نژاده، اصیل» و wolf «گرگ» (از ژرمنی آغازین *wulfaz و هندواروپایی *wl̥kʷos). معنای «گرگ نژاده» درست است و کلاین و ویکی‌واژه هم همین را می‌گویند. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Adolf\"],\n  \"ref_check\":[{\"ref\":\"KLN:27\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l.1690: 'Adolph, Adolphus, masc. PN. — L. Adolphus, of Teut. origin. The name lit. means \\\"noble wolf\\\"; cp. OHG. Athalwolf, Athaulf, Adulf, Adolf (G. Adolf), fr. athal, \\\"noble\\\", and wolf, \\\"wolf\\\".'\"}],\n  \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wlkwo-\",\"stance\":\"supports\",\"note\":\"'wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf ... c. Old High German wolf' -- second element.\"},\n   {\"src\":\"SKT\",\"where\":\"grep Adolph\",\"stance\":\"silent\",\"note\":\"no entry (Skeat does not treat personal names).\"}]},\n {\"id\":5,\"lang\":\"English\",\"words\":\"Adolph\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English Adolph(us) comes from the Latinised Adolphus, the medieval Latin form of Frankish/OHG Adolf (< Athalwolf). The Latin -ph- spelling stands for the Germanic -f. It reached English as a learned and royal name (e.g. Gustavus Adolphus).\",\n  \"derivation_fa\":\"نام انگلیسی Adolph از صورت لاتینی‌شدهٔ Adolphus آمده است و آن از آلمانی کهن Adolf (Athalwolf) است. ph در این نام نگارش لاتینی f ژرمنی است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"Adolf\"],\n  \"ref_check\":[{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l.1690 'Adolph, Adolphus ... L. Adolphus, of Teut. origin ... \\\"noble wolf\\\"'.\"},\n               {\"ref\":\"AHD\",\"status\":\"not_found\",\"note\":\"Watkins' appendix has no personal-name entry; ADOLPH not in the index.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"p. 27 s.v. Adolph\",\"stance\":\"supports\",\"note\":\"'L. Adolphus, of Teut. origin. The name lit. means \\\"noble wolf\\\"'.\"},\n   {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt l.37267\",\"stance\":\"silent\",\"note\":\"only 'Gustavus Adolphus' in a historical note; no etymology.\"},\n   {\"src\":\"WEB\",\"where\":\"grep Adolph\",\"stance\":\"silent\",\"note\":\"only 'Adolphe Degeyter' in another entry.\"}]}]\nnodes1=[\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"var 3; varemi, varamiš; varanavaity\",\"verdict\":\"plausible\",\n  \"derivation\":\"Bartholomae col. 1362f. has 3var- '(se) vertere', with a nu-present vərənav- and only with preverbs (pairi.vərənvaiti 'comes spreading over'). This is the Avestan reflex of *welH- 'to turn', so 'var 3: turn' is right. The sense 'time (one time)' is not Avestan: it is Sanskrit vā́ra- 'turn, time', which Pokorny 1140 and WP I 299 set equal to NP bār. varəmi- f. 'wave' (Yt. 19.67, nom. pl. varəmiš) = Skt. ūrmí- is a certain derivative (Bartholomae 'Welle'; Pokorny). Pokorny glosses varənavaiti- as 'bedeckt, hüllend'. He notes that it partly belongs to *wer- 'to cover' (Bartholomae 2var- 'hüllend bedecken'), so 'covered' only partly belongs to this root.\",\n  \"derivation_fa\":\"در اوستا فعل 3var- به معنای «گشتن، برگشتن» آمده است (بارتولومه، ستون ۱۳۶۲) و بازماندهٔ ریشهٔ هندواروپایی *welH- «پیچیدن، گرداندن» است. پس معنای «گشتن» درست است. ولی معنای «بار، دفعه» در اوستا گواهی ندارد و از سنسکریت vā́ra- گرفته شده است. اوستایی varəmi- «موج» هم‌ریشه با سنسکریت ūrmí- بی‌گمان از همین ریشه است. پوکورنی varənavaiti- «پوشیده» را تا اندازه‌ای از ریشهٔ دیگری (*wer- «پوشاندن») می‌داند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/welH-\"],\n  \"ref_check\":[POK1140],\n  \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"col. 1362-1363 s.v. 3var-; col. 1385 varəmay- (BRT.txt l.22760, 22980)\",\"stance\":\"supports\",\"note\":\"'3var- V. \\\"(se) vertere\\\", nur mit Praev. Praes. 10 vərənav- ...'; 'varəmay- f. \\\"Welle\\\": ... °mis sispimnō ... \\\"wogende Wellen emportreibend\\\" Yt.19.67'; 2var- (l.22733) is a separate verb, 'hüllend bedecken'.\"},\n   WLD298,\n   {\"src\":\"ARY\",\"where\":\"pdf p. 102 (ARY_latin_index_pages.txt l.2900)\",\"stance\":\"supports\",\"note\":\"s.v. بار 'time': 'VAREMIS (AVESTAN) ... BAR (PAHLAVI) ... VALATI, VALA, VARA (SANSKRIT) ... WALLON (OHG) ... REFERENCES POKORNY'.\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"bâr 2; darbâr; barm\",\"verdict\":\"plausible\",\n  \"derivation\":\"bār 'time, turn' (do bār 'twice') < MP bār [bʾl] 'time, occasion' (MacKenzie). Pokorny 1140 and WP I 299 set it equal to Skt. vā́ra- 'turn, time', so the reflex is *wāra- with the regular w- > b-. Wiktionary keeps the origin open, debating *bʰer- 'carry' against this. The old sense 'audience, admission to the king' is listed under the same lemma (Mo'in: 'اجازهٔ حضور نزد شاه'; Wiktionary: 'permission to visit a ruler; court'). From it comes darbār 'court' = dar 'door' + bār 'admission' (Wiktionary: from در + بار), and also bār-e ʿām, bār-xodā. barm 'pool, pond' < MP warm 'pool, reservoir' (MacKenzie), again with w- > b-. Linking it to Av. varəmi- 'wave' fits the form, but neither Pokorny nor MacKenzie states the link.\",\n  \"derivation_fa\":\"«بار» به معنای «دفعه» از فارسی میانهٔ bār «دفعه، نوبت» آمده است. پوکورنی و والده آن را با سنسکریت vā́ra- «نوبت، دفعه» یکی می‌دانند، با دگرگونی w آغازین به b. ویکی‌واژه ریشهٔ آن را هنوز قطعی نمی‌داند. معنای کهن «اجازهٔ حضور نزد شاه» هم زیر همین واژه است، و «دربار» از «در» + «بار» به همین معناست. «بَرم» به معنای «آبگیر، استخر» از فارسی میانهٔ warm «آبگیر» است (مکنزی). پیوند آن با اوستایی varəmi- «موج» از نظر آوایی ممکن است، ولی در منابع نیامده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"بار\",W+\"دربار\",V+\"moein/بار\",V+\"moein/برم\"],\n  \"ref_check\":[POK1140,\n   {\"ref\":\"SNS:98\",\"status\":\"not_checked\",\"note\":\"SNS OCR is too poor to locate p. 98 (no page offset).\"},\n   {\"ref\":\"MON:511\",\"status\":\"partial\",\"note\":\"Mo'in via vajehyab s.v. بار: '1 - اجازه، رخصت. 2 - اجازة حضور نزد شاه یا امیر. 3 - دفعه، مرتبه' -- senses confirmed, no etymology online; page 511 not mappable.\"},\n   {\"ref\":\"SOD:411\",\"status\":\"not_checked\",\"note\":\"SOD OCR is too poor to locate entry/page 411.\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"s.v. bār; s.v. warm (PHD.txt l.252, 607)\",\"stance\":\"supports\",\"note\":\"'bār [bʾl | N ~] time, occasion.'; '*warm [wlm | N barm] pool, reservoir.'\"},\n   WLD298,\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. برم\",\"stance\":\"silent\",\"note\":\"Mo'in online gives only barm 'pole on which a coloured cloth is hung; trellis' (the other barm), not the 'pool' sense.\"},\n   {\"src\":\"ARY\",\"where\":\"pdf p. 102\",\"stance\":\"supports\",\"note\":\"بار 'time' with Avestan VAREMIS, Pahlavi BAR, Sanskrit VARA; ref. Pokorny.\"},\n   {\"src\":\"HRN\",\"where\":\"no. 159 (HRN.txt l.1767)\",\"stance\":\"silent\",\"note\":\"Horn has only 'bārān Regen, bārīden regnen'; no bār 'mal'.\"}]},\n {\"id\":3,\"lang\":\"Avestan\",\"words\":\"-var 4; var 5\",\"verdict\":\"plausible\",\n  \"derivation\":\"Bartholomae has no Avestan suffix '-var' meaning 'like', and no 'var' meaning 'ceremony'. The nearest real words are varah- 'test, ordeal' (BRT col. 1371, MP war 'ordeal'), which belongs to 1var- 'to choose, believe' (*welh₁-, Pokorny 1137), and the Avestan suffix -bara-/-vara- 'bearing' (Horn 1073), which is from *bʰer-. So as written both items are Nourai's own constructs. What supports the chain is Nyberg: he derives Pahlavi varišn 'conduct' and hamvār 'always' 'perhaps' from Av. 3var- 'to turn' (BRT 1362). The idea 'turn > way, manner > like' is therefore a scholarly suggestion, but these Avestan forms are not attested.\",\n  \"derivation_fa\":\"در اوستا پسوندی به شکل -var به معنای «مانند» و واژهٔ var به معنای «آیین» در فرهنگ بارتولومه یافت نشد. نزدیک‌ترین واژه varah- «آزمون، ور» است که از فعل دیگری (var- «برگزیدن، باور داشتن») ساخته شده است. پسوند -bara- / -vara- «دارنده» هم از ریشهٔ «بردن» است. با این همه، نیبرگ پهلوی varišn «رفتار» و hamvār «همیشه» را «شاید» از اوستایی 3var- «گشتن» می‌داند، پس پیوند معنایی «گشتن > روش > مانند» پیشنهادی است که پژوهشگران هم داده‌اند. صورت‌های اوستایی که نورایی آورده ساختهٔ خود اوست، ولی اندیشهٔ کلی پذیرفتنی است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"POK:1140\",\"status\":\"partial\",\"note\":\"POK_full.txt l.90462ff. uel-7 lists Avestan varəmi-, varənavaiti but no '-var \\\"like\\\"' or 'var \\\"ceremony\\\"'.\"}],\n  \"consulted\":[\n   {\"src\":\"BRT\",\"where\":\"col. 1360-1363, 1371 (BRT.txt l.22730-22811)\",\"stance\":\"contradicts\",\"note\":\"Only 1var- 'wählen ... glauben', 2var- 'hüllend bedecken', 3var- '(se) vertere'; 'varah- n. \\\"Probe, Prüfung, Ordal\\\" ... zum V. 1var- ... mp. (Pü.) war \\\"Ordal\\\"'. No suffix -var 'like', no 'ceremony'.\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. varišn, ham-vār (l.3973, 1862)\",\"stance\":\"partial\",\"note\":\"'varišn ... conduct, way of living ... Perhaps to be derived from Av. (1362 sq.) 3var- \\\"to turn\\\"'; 'ham-vār ... perhaps better connected with Skr vāra- \\\"turn, time\\\", cf Av. (1362sq.) 3var- \\\"to turn\\\"'.\"},\n   {\"src\":\"HRN\",\"where\":\"p. 240-241 no. 1073\",\"stance\":\"partial\",\"note\":\"'-wār, -wāre ... Suffix \\\"tragend, versehen mit\\\". ap. -bara- ...; aw. gada-vara-; ... Nicht hierher gehören die Suffixe -vār in šērvār \\\"löwenhaft\\\" ... oder in šalvār (No. 789)'. Horn separates -vār 'like' from the 'bearing' suffix but gives it no Avestan source.\"}]},\n {\"id\":4,\"lang\":\"Pahlavi\",\"words\":\"varišn\",\"verdict\":\"plausible\",\n  \"derivation\":\"Pahlavi warišn [wlšn'] 'conduct, behaviour' is attested (MacKenzie; Nyberg 'conduct, way of living', the very gloss Nourai uses). It is an -išn verbal noun. Nyberg suggests 'perhaps' deriving it from Av. 3var- 'to turn' ('the way one turns' > 'conduct'), and he compares the Armenian loan vark' 'conduct, habits'. The derivation is therefore a cautious scholarly proposal, not a certainty.\",\n  \"derivation_fa\":\"واژهٔ پهلوی warišn «رفتار، روش زندگی» در فرهنگ مکنزی و نیبرگ آمده است، با همان معنایی که نورایی آورده. این واژه نام‌واژه‌ای با پسوند -išn است. نیبرگ با «شاید» آن را از اوستایی 3var- «گشتن» می‌داند و واژهٔ قرضی ارمنی vark' «رفتار، عادات» را با آن مقایسه می‌کند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[],\n  \"ref_check\":[\n   {\"ref\":\"HRN:241\",\"status\":\"partial\",\"note\":\"HRN.txt leaf 263 = p. 241: end of no. 1073 '-wār ... Nicht hierher gehören die Suffixe -vār in šērvār \\\"löwenhaft\\\" ... oder in šalvār (No. 789)' -- the page treats the suffix -vār, not varišn.\"},\n   {\"ref\":\"BQT:2373\",\"status\":\"partial\",\"note\":\"Read from the page image ocr/BQT/2373.png (vol. 4, pdf 456; printed number confirmed): 'هموار ... بمعنی برابر و بیک طریق و مساوی باشد - و بمعنی همیشه و دایم'; Mo'in fn.: 'پهلوی hamvâr «مناس ۲۷۶»، کردی hemvar (مساوی، متحد)'. Covers hamvār, not varišn. Saved to ocr/BQT/2373.vision.txt.\"}],\n  \"consulted\":[\n   {\"src\":\"PHD\",\"where\":\"s.v. warišn (PHD.txt l.607)\",\"stance\":\"supports\",\"note\":\"'warišn [wlšn'] conduct, behaviour.'\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. varišn (l.3973)\",\"stance\":\"supports\",\"note\":\"'varišn [wlšn'] conduct, way of living ... Perhaps to be derived from Av. (1362 sq.) 3var- \\\"to turn\\\". Arm. lw. var-k' \\\"conduct, habits\\\"'.\"}]},\n {\"id\":5,\"lang\":\"Persian\",\"words\":\"vâr 2; ham-vâr; vâr 3\",\"verdict\":\"plausible\",\n  \"derivation\":\"The suffix -vār 'like' (dīvāne-vār 'like a madman', šāhvār 'kingly') is real (Mo'in: 'به معنی نظیر و مانند'). Horn separates it from the -vār 'bearing' suffix (< *-bara-) but gives it no etymology. Deriving it from *wāra- 'turn, manner' is possible but unproven. hamvār 'even, level; always' < MP hamwār [hmwʾl] 'level, abreast', hamwār(ag) 'always' (MacKenzie; Borhan/Mo'in p. 2373; Kurdish hemvar). Nyberg notes that it is usually taken as = hambār < *hama-bāra-, but 'perhaps better' from Skt. vāra- 'turn' / Av. 3var-. vār 3 'custom' is Borhan's 'رسم و عادت' (Dehkhoda). However, Dehkhoda cites the Rudaki line Nourai quotes ('وار آذر گذشت و شعلهٔ آن') under the sense 'turn, time, period' (نوبت، زمان، دور، واره), and Wiktionary even glosses vār as 'flame'. So the verse does not illustrate 'custom'. Of the extra words, sezāvār and šāhvār are 'befitting'; Horn 789 separates šalvār, whose -vār is not this suffix.\",\n  \"derivation_fa\":\"پسوند «-وار» به معنای «مانند» (دیوانه‌وار، شاهوار) در فرهنگ معین آمده است. هرن آن را از پسوند «-وار» به معنای «دارنده» (از *-bara-) جدا می‌کند ولی ریشه‌ای برایش نمی‌دهد. «هموار» از فارسی میانهٔ hamwār «هم‌سطح، برابر؛ همیشه» است (مکنزی، معین در حاشیهٔ برهان، ص ۲۳۷۳). نیبرگ می‌گوید معمولاً آن را همان hambār می‌دانند، ولی «شاید» بهتر است آن را با سنسکریت vāra- «نوبت» و اوستایی 3var- «گشتن» بسنجیم. «وار» به معنای «رسم و عادت» در برهان آمده است، ولی دهخدا بیت رودکی (وار آذر گذشت...) را زیر معنای «نوبت، زمان، دور» آورده است. پس آن بیت گواه معنای «آیین» نیست. در «شلوار» هم، به گفتهٔ هرن، «-وار» این پسوند نیست. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"هموار\",W+\"وار\",V+\"moein/وار\",V+\"dehkhoda/وار\"],\n  \"ref_check\":[{\"ref\":\"BQT:1137\",\"status\":\"not_checked\",\"note\":\"tools/ref_page.py: 'no scan of BQT covers printed page 1137' (vol. 2, ج–خ; وار would be in vol. 4).\"}],\n  \"consulted\":[\n   {\"src\":\"BQT\",\"where\":\"p. 2373 (vol. 4 pdf 456, image read)\",\"stance\":\"supports\",\"note\":\"'هموار ... بمعنی برابر و بیک طریق و مساوی باشد - و بمعنی همیشه و دایم هم هست'; fn. 'پهلوی hamvâr «مناس ۲۷۶»، کردی hemvar (مساوی، متحد)'.\"},\n   {\"src\":\"PHD\",\"where\":\"s.v. hamwar (PHD.txt l.392)\",\"stance\":\"supports\",\"note\":\"'hamwar [hmwl | N hamwār] level, abreast. hamwār(ag) [...| N hamwāra] always.'\"},\n   {\"src\":\"NYB\",\"where\":\"Glossary s.v. ham-vār (l.1862)\",\"stance\":\"partial\",\"note\":\"'A synonym of hambār ... generally regarded to be identical (OP *hama-bāra- > hamvār ...); but perhaps better connected with Skr vāra- \\\"turn, time\\\", cf Av. 3var- \\\"to turn\\\".'\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. وار\",\"stance\":\"partial\",\"note\":\"'(پس.) 1 - نشانهٔ دارندگی ... 2 - به معنی نظیر و مانند: دیوانه وار. 3 - (اِ.) دفعه، مرتبه ...' -- senses, no etymology.\"},\n   {\"src\":\"HRN\",\"where\":\"p. 240-241 no. 1073\",\"stance\":\"partial\",\"note\":\"separates -vār in šērvār/šalvār from the 'bearing' suffix -wār < -bara-.\"}]},\n {\"id\":6,\"lang\":\"Germanic\",\"words\":\"wel; welk; wall\",\"verdict\":\"plausible\",\n  \"derivation\":\"These are Watkins' Germanic forms under wel-3: *wel- in OE welig 'willow (with flexible twigs)' ('perhaps'), *welk- in OE wealcan 'to roll, toss' ('perhaps'), and o-grade *wall- in OE wiella/wella 'well' ('rolling or bubbling water'). Pokorny 1140ff. and Wiktionary *welH- give the same set (*wiligaz, *walkaną, *wallijǭ). Two caveats apply. Kroonen/Wiktionary trace *walkaną to an extended *walg-, and Klein to *walg- 'to twist'. And the gloss 'wallet' for *wall- has no support in AHD (see node 7).\",\n  \"derivation_fa\":\"این صورت‌ها همان صورت‌های ژرمنی‌اند که واتکینز زیر ریشهٔ wel-3 «گرداندن، غلتاندن» آورده است: *wel- در «بید» (willow)، *welk- در walk «راه رفتن» (در اصل «غلتیدن») و *wall- در well «چاه، چشمه» (در اصل «آب جوشان»). پوکورنی و ویکی‌واژه هم همین‌ها را دارند، ولی دو مورد نخست را با «شاید» آورده‌اند. معنای «کیف» (wallet) برای *wall- در هیچ منبعی نیامده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/welH-\",W+\"willow\",W+\"walk\",W+\"well\"],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt l.1140 wel-3 items 3 (willow), 4 (walk), 5 (well); WALLET absent.\"}],\n  \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"1140-1144 uel-7\",\"stance\":\"supports\",\"note\":\"POK_full.txt: 'Old English welig ... willow'; 'Old English wealcan ... engl. walk'; 'Old English wielle f. \\\"wellspring\\\"'; 'Latin vallus ... out of it borrowed Old English weall'.\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. walk, well (KLN_1971.txt l.264603, 266038)\",\"stance\":\"partial\",\"note\":\"walk: 'fr. OE. wealcan, \\\"to roll, toss\\\" ... fr. I.-E. *walg-'; well: 'fr. OE. wella ... from I.-E. base *wel-, \\\"to turn, roll\\\"'.\"},\n   WLD298]},\n {\"id\":7,\"lang\":\"English\",\"words\":\"willow; walk; well 2; wallet\",\"verdict\":\"plausible\",\n  \"derivation\":\"willow < ME wilwe < OE welig < PGmc *wiligaz < *welik-, cognate with Gk. helíkē 'willow', 'the tree with pliant branches' (Klein, Wiktionary, Pokorny); confirmed. walk < ME walken < OE wealcan 'to roll, toss' + wealcian; the sense moved from 'roll about' to 'go on foot'. Wiktionary and Klein take it from an extended *walg- 'to twist, turn', and AHD and Pokorny put it under *wel-; plausible. well (n.) < OE wiella/wella < PGmc *wallijǭ 'well, swirl, wave' < *welH- (Wiktionary, Klein); confirmed. wallet is disputed: Klein ('prob. metathesis of ME. watel \\\"basket, bag\\\". See wattle') and Skeat (from watel) derive it from wattle. Only Wiktionary's hedged 'possibly from an assumed Old Northern French *walet ... from PGmc *wal- \\\"to roll\\\"' links it to this root.\",\n  \"derivation_fa\":\"willow «بید» از انگلیسی کهن welig و ژرمنی *wiligaz است، هم‌ریشه با یونانی helíkē «بید»، یعنی «درخت شاخه‌نرم»، و این پیوند درست است. walk از انگلیسی کهن wealcan «غلتیدن، تکان خوردن» است و معنایش به «راه رفتن» گشته است. برخی آن را از صورت گسترش‌یافتهٔ *walg- می‌دانند، پس این پیوند پذیرفتنی است. well «چاه» از انگلیسی کهن wella و ژرمنی *wallijǭ «گرداب، موج» از همین ریشه است و درست است. ولی wallet «کیف» را کلاین و اسکیت از watel / wattle «سبد» می‌دانند. تنها ویکی‌واژه با «شاید» آن را به *wal- «غلتاندن» می‌رساند. پس این یکی محل بحث است.\",\n  \"sources\":[W+\"willow\",W+\"walk\",W+\"well\",W+\"wallet\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node has no reference of its own; AHD wel-3 (l.1140) covers WILLOW, WALK, WELL but not WALLET.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.v. willow, wallet (KLN_1971.txt l.267289, 264655)\",\"stance\":\"partial\",\"note\":\"willow: 'fr. OE. welig ... cogn. with Gk. helíkē \\\"willow\\\" ... from I.-E. base *wel-, \\\"to roll\\\"'; wallet: 'ME. walet, prob. metathesis of ME. watel, \\\"basket, bag\\\". See wattle' (contradicts for wallet).\"},\n   {\"src\":\"SKT\",\"where\":\"s.v. Wattle (SKT.txt l.21241); Willow (l.21480)\",\"stance\":\"partial\",\"note\":\"'wallet, a bag, budget. (E.) M.E. walet, a corruption of M.E. watel, a wattle, also a bag'; willow: 'M.E. wilow ... A.S. welig'.\"},\n   AHDwel3]},\n {\"id\":8,\"lang\":\"Latin\",\"words\":\"volvere; vallĕs\",\"verdict\":\"plausible\",\n  \"derivation\":\"Latin volvō, volvere 'to roll, turn' < *welw-e/o- (the u-extension of *welH-), cognate with Gk. eilúō and Arm. gelum; certain (Pokorny, Watkins, Klein). Nourai's 'make cavity' is not a sense of volvere. It reflects Pokorny's derived nouns (volva/vulva 'womb, covering', vola 'hollow of the hand'). vallēs/vallis 'valley' is put here by Pokorny (*wl̥-nis 'curvature') and by Watkins only with 'perhaps' ('that which is surrounded by hills'); de Vaan regards the origin as uncertain. Hence plausible.\",\n  \"derivation_fa\":\"لاتینی volvere «غلتاندن، گرداندن» بی‌گمان از *welw- است، صورت گسترش‌یافتهٔ ریشهٔ *welH-، و با یونانی eilúō هم‌ریشه است. معنای «گودی ساختن» که نورایی آورده معنای این فعل نیست و از نام‌واژه‌های هم‌ریشه مانند volva «پوشش، زهدان» گرفته شده است. vallēs / vallis «دره» را پوکورنی از همین ریشه می‌داند، ولی واتکینز آن را با «شاید» آورده است. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/welH-\"],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"wel-3 item 7b 'Latin volvere, to roll: VAULT ... VOLUME ... INVOLVE ... REVOLVE'; item 9 'Perhaps variant *wall- in Latin vallēs, vallis, valley'.\"}],\n  \"consulted\":[\n   {\"src\":\"POK\",\"where\":\"1140-1144 uel-7\",\"stance\":\"supports\",\"note\":\"'Latin ... volvo, -ere, -ī, volūtum \\\"roll, kollern, wälzen, turn, whirl\\\" (*uelu̯ō), volūmen ... valvae \\\"die Türflügel\\\" ... valles, vallis \\\"valley\\\" (\\\"*incurvation\\\")'.\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. volute, valley (KLN_1971.txt l.263804, 258941)\",\"stance\":\"supports\",\"note\":\"volvere 'cogn. with Gk. eilein (for *welnein), \\\"to roll, turn, twist\\\" ... Arm. gelum'; valley 'fr. OF. valee ... fr. L. valles, later vallis'.\"},\n   {\"src\":\"LAT\",\"where\":\"not located\",\"stance\":\"silent\",\"note\":\"not grepped successfully in Ernout-Meillet OCR; relied on Pokorny/Watkins/Klein.\"}]},\n {\"id\":9,\"lang\":\"English\",\"words\":\"revolve, involve, evolution, valve, vault, volume, valley\",\"verdict\":\"confirmed\",\n  \"derivation\":\"All of these came into English from Latin. revolve < L. revolvere 'roll back' (ME revolven), involve < involvere, and evolution < ēvolūtiō 'unrolling (of a book)', from ēvolvere. valve < L. valva 'leaf of a folding door' (a derivative of volvere). vault 'arched roof' < OF voute < VL *volvita, *volta from volvere. volume < OF volume < L. volūmen 'a roll (of writing)'. valley < OF valee, from val < L. vallis. Each Latin > (French) > English step is standard (Klein, Watkins).\",\n  \"derivation_fa\":\"این واژه‌ها همه از لاتینی به انگلیسی رسیده‌اند. revolve از revolvere «بازگرداندن»، involve از involvere، evolution از ēvolūtiō «باز کردن طومار»، valve از valva «لنگهٔ در»، vault از فرانسوی کهن voute از *volvita، volume از volūmen «طومار»، و valley از فرانسوی کهن valee و لاتینی vallis آمده است. همهٔ این گذرها در منابع آمده‌اند و ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given; AHD wel-3 lists VAULT, VOLUME, INVOLVE, EVOLVE, REVOLVE, VALVE, VALLEY.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.v. revolve, valve, vault, volume, valley (KLN_1971.txt l.206399, 259019, 259644, 263728, 258941)\",\"stance\":\"supports\",\"note\":\"'revolve ... ME. revolven, fr. L. revolvere'; 'valve ... L. valva, \\\"leaf, fold or valve of a door\\\" ... rel. to volvere'; 'vault ... ME. voute ...'; 'volume ... fr. L. volumen, \\\"a roll\\\"'; 'valley ... fr. L. valles'.\"},\n   AHDwel3]},\n {\"id\":10,\"lang\":\"Greek\",\"words\":\"hel-ix\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Greek hélix (gen. hélikos) 'anything spiral, coil; tendril' < *welik-, with initial *w- lost (digamma) and replaced by the rough breathing. It belongs to helíssō 'to turn, roll' (< *welik-yō) and to helíkē 'willow', which matches OE welig. Watkins lists 'Suffixed form *wel-ik- in Greek helix'; Pokorny and Klein agree.\",\n  \"derivation_fa\":\"یونانی hélix «پیچ، مارپیچ» از *welik- است. w آغازین (دیگاما) در یونانی افتاده و جای آن دم‌آوای h آمده است. این واژه با فعل helíssō «پیچاندن» و helíkē «بید» هم‌خانواده است. واتکینز و پوکورنی و کلاین همین را می‌گویند و ادعای نورایی درست است.\",\n  \"sources\":[W+\"helix\"],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"wel-3 item 11 'Suffixed form *wel-ik- in Greek helix, spiral object: HELIX'.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.v. helix (KLN_1966.txt l.17497)\",\"stance\":\"supports\",\"note\":\"'helix ... L., fr. Gk. hélix, \\\"spiral, coil\\\", from the stem of helíssein (for *welikyein), \\\"to turn about, wind, roll\\\", fr. I.-E. base *wel-'.\"},\n   {\"src\":\"POK\",\"where\":\"1140-1144 uel-7\",\"stance\":\"supports\",\"note\":\"'from the i-basis: ... hélix \\\"winded\\\", f. \\\"bracelet\\\", therefrom helíssō ... in addition also helíkē \\\"willow\\\"'.\"}]},\n {\"id\":11,\"lang\":\"English\",\"words\":\"helix\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English helix (16th c.) is a learned borrowing of Latin helix 'spiral, volute', which is from Greek hélix. It was used first in architecture (the volute of a capital) and later in geometry and anatomy.\",\n  \"derivation_fa\":\"انگلیسی helix وام‌واژه‌ای دانشورانه از لاتینی helix است و آن از یونانی hélix گرفته شده است. نخست در معماری (پیچک سرستون) و سپس در هندسه و کالبدشناسی به کار رفته است. ادعای نورایی درست است.\",\n  \"sources\":[W+\"helix\"],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"no reference given; KLN s.v. helix supports.\"}],\n  \"consulted\":[\n   {\"src\":\"KLN\",\"where\":\"s.v. helix\",\"stance\":\"supports\",\"note\":\"'helix, n., spiral line. — L., fr. Gk. hélix'.\"},\n   AHDwel3]}]\nout={\"pdf_page\":541,\"book_page\":511,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Wel 2\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *wel- 'to tear, pull, wound' (Pokorny 8. u̯el- 1144-1145; Watkins wel-4 'to tear, pull')\",\n  \"note\":\"Root, label and gloss are correct: Pokorny 1144 uel-8 'to tear, wound' (Lat. vellere, volnus, NP vālāne 'wound'); Watkins wel-4 'To tear, pull' [Pok. 8. wel- 1144]. This is PART 2 of the chart (part 1, on p. 540, has vālāne and vulnerable). The branch here (wolf/fox/dog words) rests on the old suggestion in Walde-Pokorny I 316-317 that *ulkʷos and *ulp- are 'the tearing animal' from uel- 'reißen'. Pokorny's 1959 IEW and Watkins treat *wl̥kʷos and *wlp-ē- as separate (taboo-deformed) roots, so the attachment is only possible. Within the branch, gorbe < MP gurbag < *wr̥pa-ka- and Tahmūras < Av. Taxma Urupi are sound. The Avestan node mixes real words (urupi-, raopi-) with reconstructions ('urpa', 'lupis').\",\n  \"note_fa\":\"ریشهٔ هندواروپایی *wel- به معنای «دریدن، کندن، زخمی کردن» در پوکورنی (ص ۱۱۴۴) و واتکینز آمده است، با بازمانده‌هایی چون لاتینی vellere و vulnus و فارسی «والانه» به معنای زخم. پس ریشه و معنایی که نورایی داده درست است. ولی بستن نام‌های گرگ و روباه و سگ به این ریشه، به معنای «جانور درنده»، تنها پیشنهاد والده و پوکورنی (ج ۱) است. پوکورنی در فرهنگ ۱۹۵۹ آن را نیاورده و پژوهش امروزی این نام‌ها را ریشه‌های جداگانه می‌داند. در این شاخه، «گربه» از پهلوی gurbag و «تهمورث» از اوستایی Taxma Urupi درست‌اند.\",\n  \"sources\":[W+\"گربه\",W+\"روباه\",W+\"Adolf\"],\n  \"ref_check\":[POK1144],\n  \"consulted\":[\n   {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wel-4\",\"stance\":\"supports\",\"note\":\"AHD_watkins1985.txt l.1141: 'wel-4. To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE ... 2. Suffixed form *wel-no- in Latin villus, shaggy hair ... [Pok. 8. wel- 1144.]'\"},\n   WLD316],\n  \"nodes\":nodes0},\n {\"entry\":1,\"root\":\"Wel 3\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *welH- 'to turn, roll' (Pokorny 7. u̯el- 1140-1144; LIV² 2. *u̯elH-; Watkins wel-3)\",\n  \"note\":\"Root, label and gloss are correct: Pokorny 1140 uel-7 'to turn, wind; round' (WP I 298f.), Watkins wel-3 'To turn, roll', Wiktionary *welH-. Pokorny himself gives the key Iranian items Nourai uses: Skt. vāra- 'turn, time' = NP bār 'mal', Av. varəmi- 'wave' = Skt. ūrmí-, and Av. varənavaiti- (partly *wer- 'cover'). The Western branches (willow, walk, well, volvere, valva, vallis, helix) are Watkins' own list, with 'perhaps' for willow, walk and valley. Weak points: (1) the Avestan '-var 4: like' and 'var 5: ceremony' are not attested (Bartholomae has only varah- 'ordeal' from 1var- 'choose'). The Pahlavi varišn/hamvār link to 3var- 'turn' is only Nyberg's 'perhaps'. (2) Klein and Skeat derive wallet from wattle, so it does not belong here securely. (3) The Rudaki verse quoted for vār 'custom' is cited by Dehkhoda for vār 'turn, time'. No transcription problems: the chart forms match the extraction.\",\n  \"note_fa\":\"ریشهٔ هندواروپایی *welH- به معنای «گرداندن، غلتاندن» در پوکورنی (ص ۱۱۴۰)، واتکینز و ویکی‌واژه آمده است. پوکورنی خود سنسکریت vāra- «نوبت» را با «بار» فارسی (به معنای دفعه) یکی می‌داند و اوستایی varəmi- «موج» را هم از همین ریشه می‌شمارد. پس ریشه و معنا درست است. شاخه‌های غربی (willow، walk، well، volvere، helix) را هم واتکینز آورده است. با این همه، صورت‌های اوستایی -var «مانند» و var «آیین» در بارتولومه نیامده‌اند، و پیوند «ورِشن» و «هموار» با این ریشه تنها پیشنهاد نیبرگ است. wallet را هم کلاین و اسکیت از wattle می‌دانند.\",\n  \"sources\":[W+\"Reconstruction:Proto-Indo-European/welH-\",W+\"بار\"],\n  \"ref_check\":[POK1140],\n  \"consulted\":[WLD298,AHDwel3,\n   {\"src\":\"KLN\",\"where\":\"s.v. volute (KLN_1971.txt l.263804)\",\"stance\":\"supports\",\"note\":\"volvere 'cogn. with Gk. eilein ... OI. vṛṇoti ... valate, \\\"turns\\\"'.\"}],\n  \"nodes\":nodes1}]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-541.json','w'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-541.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-541.json >/dev/null && python3 tools/verify_check.py 541"
}
```


### [2026-10-17T00:09:49.508Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 11, 'confirmed': 5}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 6, 'not_checked': 8, 'supports': 7, 'not_found': 1}
books consulted: {'supports': 30, 'partial': 11, 'silent': 7, 'contradicts': 1} | by book: {'KLN': 7, 'WLD': 5, 'AHD': 5, 'POK': 4, 'ARY': 4, 'PHD': 4, 'NYB': 4, 'HRN': 4, 'BRT': 3, 'MON': 3, 'SKT': 2, 'FSD': 1, 'WEB': 1, 'BQT': 1, 'LAT': 1}
```


## [2026-10-17T00:10:01.428Z] TOOL CALL #64: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-541.json` for PDF page 541 (book page 511). It parses as JSON, and `verify_check.py 541` reports 16/16 nodes verified with 0 PROBLEM lines.\n\n- **Roots:** 2 confirmed. Wel 2 \"to tear, pull, wound\" matches Pokorny 1144. Wel 3 \"to turn, roll\" matches Pokorny 1140 and Watkins wel-3.\n- **Nodes:** 5 confirmed, 11 plausible, 0 disputed, 0 transcription_suspect.\n\nThe main things behind the \"plausible\" verdicts:\n- **Wel 2, wolf/fox/dog branch:** linking these words to *wel- \"tear\" rests only on Walde-Pokorny I 316-317 (\"vielleicht als 'reißendes Tier'\"). Pokorny 1959 and Watkins treat *wl̥kʷos and *ulp-/lup- as separate roots. The Avestan node mixes real words (urupi-, raopi-, Taxma Urupi) with reconstructions: \"urpa\" is a reconstructed form and \"lupis\" is Pokorny's pre-form, not Avestan.\n- **Wel 2, gorbeh and Tahmuras:** gorbeh < MP gurbag < *wr̥pa-ka- and Tahmuras < Av. Taxma Urupi are sound. The glosses \"an animal that tears up\" and \"(with) strong dogs\" are Nourai's own readings.\n- **Wel 3, Avestan \"-var 4: like\" and \"var 5: ceremony\":** Bartholomae has neither. The nearest real word is varah- \"ordeal\", which comes from the different verb var- \"choose\". Linking Pahlavi varišn and hamvār to 3var- \"turn\" is only Nyberg's \"perhaps\".\n- **Wel 3, wallet:** Klein and Skeat derive it from wattle. Only Wiktionary's hedged \"possibly\" ties it to *wal- \"roll\".\n- **Wel 3, the Rudaki verse quoted for vâr 3 \"custom\":** Dehkhoda cites this verse for vâr \"turn, time\", not \"custom\".\n- **Wel 3, other weak links:** valley (< vallis) is only \"perhaps\" in Watkins. barm comes from MP warm \"pool\", but no source states its link to Av. varəmi- \"wave\".\n\n**Extraction errors:** I did not check the printed page, because no node was flagged transcription_suspect. I found no sign of an extraction error.\n\n**Nourai's references:**\n- **Mismatches:** BQT:968 and BQT:1137 don't match where these headwords stand in Borhan, and those pages have no scan.\n- **Could not check:** SNS:98, SOD:411 and MON5:405 (OCR too poor, or not online).\n- **Page saved:** I read BQT:2373 (hamvâr) from the page image and saved the text to `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2373.vision.txt`.\n- **Etymonline:** it returned 403, so I used and cited the Wiktionary pages instead."
}
```


### [2026-10-17T00:10:02.118Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
