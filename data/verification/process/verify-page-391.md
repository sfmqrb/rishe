# Verification process log — verify-page-391


## [2026-09-14T00:49:32.891Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 391 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-391.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-391.json. Write /home/sfmqrb/git/rishe/data/verification/page-391.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 391` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:33.975Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:34.804Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:34.822Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T00:49:35.309Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-391.txt"
}
```


### [2026-09-14T00:49:35.332Z] TOOL RESULT

```
1	=== PDF page 391 (book page 361) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pele, Pelt, Paita : to spread, make flat  (refs POK:805; IEC:918; CEL2:3)
4	#1 (parent #0) [Iranian] refs=IEC:918 | partaka : flap of cloth, curtain
5	  #2 (parent #1) [Persian] refs=LAT:853 | pardeh «پرده» : curtain | extra: پرده دار ، سراپرده ، پردگی | NOTE: LKT:131 claims this has reached Europe through Arabic.
6	  #3 (parent #1) [Pahlavi] refs=PHD:64 | pardag : curtain, veil
7	    #4 (parent #3) [Hindustani] refs=HJB:744; AID:242 | pardah : curtain, veil
8	      #5 (parent #4) [English] refs=AHD:1061; KLN:1273; FWE:233 | pardah, purdah : veil
9	  #6 (parent #1) [Sanskrit] refs=IEC:918 | patah : cloth, screen garment, canvas
10	  #7 (parent #1) [Sogdian] refs=SOD:284 | prd`nk, prd`nkh, prthynq : curtain
11	#8 (parent #0) [Greek] refs=AHD:1533; IEC:918 | plan-asthai : to wander around ; plas-sein : to spread out in a mold
12	  #9 (parent #8) [French] refs=VOP:120 | plasma ; plastique
13	    #10 (parent #9) [Persian] refs=VOP:120 | plâsmâ «پلاسما» : plasma ; plâstîk «پلاستیک» : plastic
14	  #11 (parent #8) [English] refs=AHD | planet, plasma, plaster, airplane, plastic
15	#12 (parent #0) [Germanic] refs=POK:805 | fel-thus : flat land ; flô-ruz : floor
16	  #13 (parent #12) [English] refs=AHD | field ; floor
17	#14 (parent #0) [Latin] refs=AHD:1533 | plâ-nus : flat ; pal-ma : palm of hand
18	  #15 (parent #14) [English] refs=AHD | plane, plain, plan, explain ; palm
19	#16 (parent #0) [Indo-European] refs=POK:833 | Plat : to spread
20	  #17 (parent #16) [Avestan] refs=POK:833; KLN:1192 | frathah : wide
21	    #18 (parent #17) [Persian] refs=BQT:1444; HRN:180 | farâx «فراخ» : wide, large
22	  #19 (parent #16) [Germanic] refs=AHD | flataz : flat
23	    #20 (parent #19) [English] refs=None | flat
24	  #21 (parent #16) [Greek] refs=AHD | platus : flat
25	    #22 (parent #21) [Latin] refs=AHD:1004 | plattus
26	      #23 (parent #22) [French] refs=VOP:120 | platine : platinum
27	        #24 (parent #23) [Persian] refs=VOP:120 | pelâtîn «پلاتین» : platinum
28	      #25 (parent #22) [English] refs=AHD | plate, place, plaza, plateau, platinum
29	--- entry 1 ---
30	ROOT Pelt -> redirect to Pele
31	--- entry 2 ---
32	ROOT Pelu -> redirect to Pel 1
33	--- entry 3 ---
34	ROOT Pen -> redirect to Spen
35	
```


## [2026-09-14T00:49:37.901Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-391.json | head -200",
 "description": "Read source JSON for page 391"
}
```


## [2026-09-14T00:49:38.673Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T00:49:39.003Z] TOOL RESULT

```
{
    "pdf_page": 391,
    "book_page": 361,
    "entries": [
        {
            "root": {
                "name": "Pele, Pelt, Paita",
                "lang": "Indo-European",
                "refs": "POK:805; IEC:918; CEL2:3",
                "gloss": "to spread, make flat"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Iranian",
                    "refs": "IEC:918",
                    "words": [
                        {
                            "translit": "partaka",
                            "gloss": "flap of cloth, curtain",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "LAT:853",
                    "words": [
                        {
                            "translit": "pardeh",
                            "gloss": "curtain",
                            "script": "\u067e\u0631\u062f\u0647"
                        }
                    ],
                    "script_extra": "\u067e\u0631\u062f\u0647 \u062f\u0627\u0631 \u060c \u0633\u0631\u0627\u067e\u0631\u062f\u0647 \u060c \u067e\u0631\u062f\u06af\u06cc",
                    "note": "LKT:131 claims this has reached Europe through Arabic.",
                    "quote": {
                        "text": "\u0637\u0644\u0627\u06cc\u0647 \u0632 \u0647\u0631 \u0633\u0648 \u0628\u0631\u0648\u0646 \u062a\u0627\u062e\u062a\u0646\u062f - \u0628\u0647 \u0647\u0631 \u067e\u0631\u062f\u0647 \u0627\u06cc \u067e\u0627\u0633\u0628\u0627\u0646 \u0633\u0627\u062e\u062a\u0646\u062f",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "PHD:64",
                    "words": [
                        {
                            "translit": "pardag",
                            "gloss": "curtain, veil",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Hindustani",
                    "refs": "HJB:744; AID:242",
                    "words": [
                        {
                            "translit": "pardah",
                            "gloss": "curtain, veil",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "English",
                    "refs": "AHD:1061; KLN:1273; FWE:233",
                    "words": [
                        {
                            "translit": "pardah, purdah",
                            "gloss": "veil",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 1,
                    "lang": "Sanskrit",
                    "refs": "IEC:918",
                    "words": [
                        {
                            "translit": "patah",
                            "gloss": "cloth, screen garment, canvas",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:284",
                    "words": [
                        {
                            "translit": "prd`nk, prd`nkh, prthynq",
                            "gloss": "curtain",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "AHD:1533; IEC:918",
                    "words": [
                        {
                            "translit": "plan-asthai",
                            "gloss": "to wander around",
                            "script": null
                        },
                        {
                            "translit": "plas-sein",
                            "gloss": "to spread out in a mold",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "French",
                    "refs": "VOP:120",
                    "words": [
                        {
                            "translit": "plasma",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "plastique",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "Persian",
                    "refs": "VOP:120",
                    "words": [
                        {
                            "translit": "pl\u00e2sm\u00e2",
                            "gloss": "plasma",
                            "script": "\u067e\u0644\u0627\u0633\u0645\u0627"
                        },
                        {
                            "translit": "pl\u00e2st\u00eek",
                            "gloss": "plastic",
                            "script": "\u067e\u0644\u0627\u0633\u062a\u06cc\u06a9"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 8,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "planet, plasma, plaster, airplane, plastic",
                            "gloss": null,
                            "script": null
```


### [2026-09-14T00:49:39.046Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-14T00:49:49.005Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-391.json | sed -n '200,500p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T00:49:50.169Z] TOOL RESULT

```
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "POK:805",
                    "words": [
                        {
                            "translit": "fel-thus",
                            "gloss": "flat land",
                            "script": null
                        },
                        {
                            "translit": "fl\u00f4-ruz",
                            "gloss": "floor",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "field",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "floor",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD:1533",
                    "words": [
                        {
                            "translit": "pl\u00e2-nus",
                            "gloss": "flat",
                            "script": null
                        },
                        {
                            "translit": "pal-ma",
                            "gloss": "palm of hand",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "plane, plain, plan, explain",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "palm",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 0,
                    "lang": "Indo-European",
                    "refs": "POK:833",
                    "words": [
                        {
                            "translit": "Plat",
                            "gloss": "to spread",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "Avestan",
                    "refs": "POK:833; KLN:1192",
                    "words": [
                        {
                            "translit": "frathah",
                            "gloss": "wide",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 18,
                    "parent": 17,
                    "lang": "Persian",
                    "refs": "BQT:1444; HRN:180",
                    "words": [
                        {
                            "translit": "far\u00e2x",
                            "gloss": "wide, large",
                            "script": "\u0641\u0631\u0627\u062e"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 19,
                    "parent": 16,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "flataz",
                            "gloss": "flat",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 20,
                    "parent": 19,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "flat",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 21,
                    "parent": 16,
                    "lang": "Greek",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "platus",
                            "gloss": "flat",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 22,
                    "parent": 21,
                    "lang": "Latin",
                    "refs": "AHD:1004",
                    "words": [
                        {
                            "translit": "plattus",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 23,
                    "parent": 22,
                    "lang": "French",
                    "refs": "VOP:120",
                    "words": [
                        {
                            "translit": "platine",
                            "gloss": "platinum",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 24,
                    "parent": 23,
                    "lang": "Persian",
                    "refs": "VOP:120",
                    "words": [
                        {
                            "translit": "pel\u00e2t\u00een",
                            "gloss": "platinum",
                            "script": "\u067e\u0644\u0627\u062a\u06cc\u0646"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 25,
                    "parent": 22,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "plate, place, plaza, plateau, platinum",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Pelt",
                "redirect": "Pele"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Pelu",
                "redirect": "Pel 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Pen",
                "redirect": "Spen"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-14T00:49:50.270Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"plā-\" POK_full.txt | head -40; echo \"=== POK page marker check\"; ls",
 "description": "Grep Pokorny"
}
```


### [2026-09-14T00:49:50.369Z] TOOL RESULT

```
=== POK page marker check
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


## [2026-09-14T00:49:55.503Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','CEL2','LAT','PHD','HJB','AID','AHD','KLN','FWE','SOD','VOP','HRN','BQT','LKT','FSD','WEB','SKT','MON','ARY','SYN','WLD','BRT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-14T00:49:56.445Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

CEL2 null

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

FWE {"title": "A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, 1966", "edition_found": "1966 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/dictionaryoffore00blis (+8 other lending copies)", "identifier": "dictionaryoffore00blis (also dictionaryoffore0000alan, dictionaryoffore0000ajbl)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 2026-09: borrowable only."}

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-14T00:50:01.719Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---IEC'); print(d['IEC']['page_offset']); print(d['IEC'].get('lookup_hint'))\nprint('---KLN'); print(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('---SOD'); print(d['SOD'].get('page_offset'))\nprint('---LAT'); print(d['LAT']['page_offset'])\nprint('---HJB'); print(d['HJB']['page_offset'])\nprint('---BQT'); print(d['BQT'].get('page_offset'));print(d['BQT'].get('lookup_hint'))\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-14T00:50:03.315Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---IEC
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
---KLN
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---SOD
printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
---LAT
leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---HJB
leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---BQT
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-14T00:50:06.402Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 805\" POK_full.txt | head; echo \"=== 833\"; grep -n \"Page(s): 83[23]\" POK_full.txt | head",
 "description": "Find Pokorny pages 805, 833"
}
```


### [2026-09-14T00:50:06.486Z] TOOL RESULT

```
65651:Page(s): 805-807 
66142:Page(s): 805 
=== 833
68162:Page(s): 832-833 
68235:Page(s): 833-834
```


## [2026-09-14T00:50:09.376Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '65600,65660p' POK_full.txt; echo \"#### 66100\"; sed -n '66110,66145p' POK_full.txt",
 "description": "Read POK 805 entries"
}
```


### [2026-09-14T00:50:09.451Z] TOOL RESULT

```
as d^-present probably here gr. nAaaaw (*nAa9i(jo, phonetically adapted to the present 
from guttural stems), Aor. STiAaaa, snAaaGnv "shape from soft mass form ', Kara-, z\^- 
nAaaaw " spread ', nAaa|ja n. " thing ', nAaaTr|<; m. "molder', spnAaarpov n. > Latin 
emplastrum> Modern High German Pflaster^ plaster '; in addition nAa9avo(; m., nAa9avr| 
f. " cake board ', nr|Ao-TTAa9oc; "clay formend, a worker in clay, potter '; nominales d^ in 
naAaGri "flat Fruchtkuchen'; 

with formants -/70-; Latin y0/5/7^5"platt, even, flat' (Indo Germanic *pla-no-s) = gall. 
Med/o-/anum actuaWy "mitten in the Ebene?', Lithuanian p/dnas't\r\\n', Latvian p/ansl\at, 
even, thin', yO/a'/75 "threshing floor'. Old Prussian p/on/s{0\6 Lithuanian planas) "threshing 
floor': 

Slavic *pol-no-\x\ Upper Serbian pioh^ plain ', kir. pc»/c»/7y/7a"Hochebene', Czech plauy^ 
infertile, field-, wood, forest-', plan^ plain, Prarie', sloven, plan, f. p/analree from 
Baumwuchs', p/anja 'oiiene, free surface, plain, area', Serbo-Croatian planfna^ mountain 
forest ' etc.; 

here - perhaps of ziellosen sich Ausbreiten weidender Herden - gr. ttAqvoc; "irrend, 
wandering ', nAavo(; m., nAavr) f. "irrender run, flow', nAavav "of rechten way abfiJhren', - 
aoGai " wander', TTAavr|<;, -r|TOc;f. " wandering ', Old Icelandic /7a/7a"umherfahren', French 
(from dem Germanic) flaner^sich auf the road umhertreiben'; 

with />formants: gr. -nzKavoc, "flat Opferkuchen, flat coin'; 

with /77-or />forms, meaning esp. "flat hand': *pjama{pjm§). gr. naAapn f- fat hand'; 

maybe alb. ( *pel9ma) pe//emt>a ^ pa\fr\' [common alb. m- > mt)-]. 

Latin pa/mal\at hand; also Gansefuft, Geweihschaufel of Damhirsches, shovel of Ruders, 
Palme', pa/mus'd\e Hand as measurement of length, span', palmes, -///s"RebenschoR)', 
Old Irish lam, acorn, lof, cymr. //aM/"hand' (if in addition Old Irish fo-laumur^\NaQe'l); Old 
High German /b//77a"hand'. Old English /b//77"flat hand'; other ablaut in Old \v\6\c panf-vn. 
"hand' (Middle Indie from * parni-), Avestan p9r9na^\\o\\\Q hand'; 



with Aformants: Old Icelandic florrxw. " floorboard of Viehstalles; cattle shed', Old 
English flor^ floorboard ', Middle Low German vlor^ floorboard, meadow'. Middle High 
German i/A/o/"" bottom, meadow, sown field ', Modern High German Flur, Old Irish lar, 
cymr. etc. Ilawr {*pla-ro-) "solum, pavimentum'; 

with dentalem forms *pel-tosv\., *pel-tu-src\., *yO/-/a "surface, plain, area': Old High 
German Old Saxon feldu. "field, bottom, plain ', Old English feld {u-sierw) ds.; Old 
Icelandic foldi. "earth, land', also "Fjord' and FIN, Old English folde. Old Saxon folda 
"earth' (Old \v\6\c prthivl). Old High German FIN Fu/d-aha'Fu\6a'; Finnish yOe//c» "farmland' 
from dem Germanic; above examples belong actually to extension p/et- 

Maybe alb. {*fulsa) fusha " field '. 

References: WP. II 61 ff., WH. II 237, 240 f., Trautmann 204, 222; 
See also: extensions under plak-, plet- 
Page(s): 805-807 

Root / lemma: peli-s- pel-s- 

Meaning: rock 

Material: Old \x\A\c pasana-m., pasya-n. " stone ', (from *pars- = Indo Germanic *pels-)\ 

gr. nsAAa K\Qoc, Hes. (*n£Aaa); Pashto pa/'sa Middle Irish allu. {*plso-) "cliff (s-inflection 

#### 66100
U\h\}av\\av\pele-ju, -ti" mildew ', pelesiaiP\. " mildew ' and in ab\a\}\. plek-stu, -ti" mildew, 
modern'; in ablaut Lithuanian pilkas'^raY, /Oe//re"Moorbruch', a\so palsas, Latvian paiss 
"sallow, paled' ( *polRos) as well as Old Prussian poa//s'doye' {*pdlis); Slavic *plesnb in 
russ.-Church Slavic plesnt. Old Czech plesen' mildew ' and Church Slavic /0e/e5"pullus', 
russ. pe/esjy" mottled, speckled, *tabby, varicolored'; das forms Indo Germanic -so- or -ko- 



References: WP. II 53 f., WH. II 239 f., 242, 386, Trautmann 205, 212; 
See also: see above S. 799 C {pel-1). 
Page(s): 804-805 

Root / lemma: {pel-9), pol- pie- plo- 

Meaning: to burn, be warm 

Note: also with -£/o- extended; perhaps = (s)p(h)el-'q\eavc\, shimmer' 

Material: Old Icelandic flor {*fld-wa-) "lukewarm, warm'; Dutch f/ouwla\nt, languid, 

lukewarm'. Modern High German flau {*ple-uo-); Old Church Slavic yoo^ip, /7C»/e//"burn' intr., 

causative pa//t/"burn' tr., vbs-p/anetb sg "KaTacpAsynasTai', plamy, plamenb m. "flame' 

( *polmen-); whether here Lithuanian plenys above S. 802? 

in addition probably cymr. ^c»-/ei/ "light', bret. gou-louds. {*plo-uo-); different Lewis- 
Pedersen 29 (to GN Lugus), compare above S. 690. 



References: WP. II 59 f., Trautmann 212 f., J. Loth RC. 36, 157. 
Page(s): 805 

Root / lemma: pelpo- or polpo-
```


## [2026-09-14T00:50:10.185Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68120,68240p' POK_full.txt",
 "description": "Read POK 833 entries"
}
```


### [2026-09-14T00:50:10.252Z] TOOL RESULT

```
nisi, flokirw.. Old English flocm. "Flunder', engl. /7c»c»/r-/fc»c»/eo'"plattfuR)ig'; Old High 
German flah{-hh-), Dutch flak, flach^ smooth ', Old Saxon flakai. "Fuftsohle', Norwegian 
flaku. " disc, floe, floating mass of ice'. Old Icelandic flaki, flekixw. "Bretterverschlag', Tirol- 
karnt. f/ecken 'board, plank, balk'. 

References: WP. II 90 f., WH. II 314 ff., Trautmann 222 f.; Vasmer 2, 365 f., 367. 



Page(s): 831-832 



Root / lemma: plak-2, plag- , also p/ek-, pleg- 
Meaning: to hit 

Material: Gr. nAnaau) {*plakid), nAnvvufji 'hit', nAnYH- Doric TTAava "blow, knock', TTAf|KTpov 
'beetle, hammer etc.'; nasalized TrAa^oj (*nAaYYJw) 'hit, verschlage' (nAay^u), snAaYxQnv); 
Latin p/aga'b\o\N, knock, wound', plango, -ere^hW: die Hand auf die Brust hit, loud grieve '; 
Middle Irish len. Gen. /eo//7 'affliction, wound' {*plakno-), /essa//?? 'schlage violent' {*plang- 
sd)\ Gothic faiflokun ^ZKOJ^-ioy-io, betrauerten'. Old English f/dcan^Be\ia\\ klatschen'. Old 
Saxon flocan 'verwijnschen, curse ' (at first from 'loud die Brust hit'). Old High German 
fluohhon6s., fluoh^ curse'. Old Icelandic /7o/r/ "gestampfter Filz'; from dem Germanic here 
probably also words for 'Anprall, gust of wind' and 'with den Flijgeln hit, flutter, flicker': Old 
Icelandic /75^5 'sudden attack ', Middle Low German Middle High German vlage^ shove, 
attack, storm', engl. /7ai4^ 'gust of wind, crack'; Old Icelandic flggra^i\\}\.\.er\ Old High 
German /7a^a/io/7'umherfliegen'; with Germanic /r.Old Icelandic figkra {flakuron) 
'umherschweifen'. Middle High German vlackern, Dutch iz/a/r/re/'e/? 'flicker'. Old English 
/7ac"o/''fliegend', /7/ico/7a/7 'flicker'. Old Icelandic figkta {*flakutdn) 'umherstreifen, flutter', 
expressive Old Icelandic flakka 'flutter, umherschweifen', old Dutch vlacken ' twitch '; 
nasalized Middle Low German v/unke{' \N\ng'); Old Icelandic f/engja ^thrasW (engl. f//ng 
'throw' from dem Old Icelandic), wherefore (?) Latin /ancea^d\e originally spanische lance ' 
(Celtic word); 

Lithuanian plaku, plakti^hW, chastise, castigate', plokisxw. 'Rutenstreich'; Old Church 
Slavic placg, plakati sg 'sich an die Brust hit, weep, cry, wail '; 

besides plak/g- siauds p/ek/g-:La\.\r\ plecto, -e/ie 'punish, curse, chastise, castigate', 
Lithuanian pifek-iu, -//'hit, thrash, chastise, castigate', dial, p/e^a 'cudgel, ZiJchtigung'. 

References: WP. II 91 ff., WH. II 315 f., 321 f., Trautmann 222 f.; Vasmer2, 364 f.; 
See also: probably to pels-: pla-S. 805, also originally 'breit hit'. 
Page(s): 832-833 

Root / lemma: plat-{plad^, plet- plot-, plat- 

Meaning: wide, flat 

Note: extension to pels- : p/a-ds., see there; to Vokalverhaltnis compare p/ak- : p/ek-ds. 

and p/ak- : p/ek- : p/ek- 'hit' 

Material: Aryan *p/et/i-:0\d Indie /O/a/^aZ/'breitet from', -/e'dehnt sich from, verbreitet 

sich', prtfia- m. 'flat hand', prat/ias-v\. = Avestan fra^a/i-n. ' Breite', Old \nd\c prt/iu-, 



Avestan p9rd^u-'\N'\de, breit, capacious ', fern. Old Indie prthvT, Avestan p9r9^wT{a\so as 
Subst. " surface '), besides from *pjt(h)9u- : prthivTi. "earth' ('Erdoberflache') = gr. nAaraia, 
gall. GN LitavTi., gall. -Latin Letavia, leg. *Litavia, ncymr. Llydaw^6\e Bretagne', Middle Irish 
LethadiS.; 

Armenian /a//7 'breit' {*pleta-no-). 

gr. nAoTuq 'platt, breit' (= Old Indie prth'u-), nAaroq n. 'Breite' (reshuffling from *nA£Toq = 
Old Indie /Ora/^as- after nAaTU(;), nAarn "Ruderschaufel', cbpo-nAaTri f. 'scapula', irAaTavoc; 
'sycamore' ('breitastig'); nAaraiJcbv ' each flat body' (: Old \n6\c prath/man-m. 'Breite, 
Ausdehnung'); nAarayn 'das Klatschen'; formal nicht right clear, bright are naAaarn 'flat 
hand', TTAaoTiy^ 'flat bowl'; 

Latin p/anfat 'Fuftsohle' {*pla-n-ta)\ p/anfa ^ Setzre'\s' is back-formation to *p/antare'6en 
Boden ebnen'; 

cymr. //ed, corn, /es, bret. /et, ledxw. 'Breite' (from dem n. *pletos= Old Indie /7/'a//755-), 
cymr. Iledu, bret. ledaff' outspread ', Old Irish lethaim^Aehue from, erweitere' (probably 
also Old Irish lethu. 'side, flank ' etc.), Kompar. cymr. //ed'\N\de, further' {*plet-is). Old Irish 
/etha'wde', Positive */0//e/7c»- in Old Irish lethan, cymr. Ilydan, bret. corn. ledan^breW!, gall. 
Litana {silva), Litano-briga; Middle Irish /e///7e 'shoulder' {*pletia). Middle Irish lethech^ 
flounder, flatfish '; Old Irish less, cymr. //ys 'castle' {*pJt-to-l)\ 

Maybe alb. {*pletia) flete' (wide) wing, side, flank, (flat) leaf, /7e-' lie, sleep' : Old Irish 
/e//7n. 'side, flank ', Middle Irish /e///7e 'shoulder'; also alb. leth, ledh^muA, alluvium; wall, 
flat earth, mound, river mouth, balk' : Old Irish less, cymr. Ilys 'castle' ( *pJt-to-l) : gall. -Latin 
Letavia, \Q^.*Litavia, ncymr. Llydaw, Middle Irish Letha . 

in Germanic with ablaut, a: 6: Middle High German i/A/oofe/'' Plunder', nasalized Middle 
High German Low German flunder^s.. Middle Low German vlundereAs., Dutch vionder 
'thin board'. Old Icelandic flydrai. ' deadwood ', Swedish flundra6s., Norwegian also 
'small platter stone '; Germanic *flat^dn\v\ Old High German /750'c' 'Opferkuchen', Middle 
High German vlade'\N\6e, thin cake'. Modern High German Fladen, Kuh-fladen, 
Norwegian fladerw. 'small plain, flat field'; Middle Low German vladder^Vc\\v\ Torfschicht'; 

Lithuanian plotytl 'outspread ', p/d/as 'Platte', p/o//s 'Breite', Latvian platft, plest, thin 
aufstreichen'; Old Church Slavic *plast-b 'tortum', russ. plasf layer ' (root form * plat-); 
Lithuanian spleclu, splestr bre\ten, breitlegen' (doubtful because of ani. s-, das in our 
family otherwise nirgends), plati/s^breW {a= o, different from nAarug, prthu-), plantu, plasti 



'wide become', Old Pruss\anp/asmenoi. "Vorderhalfte the Fuftsohle'; from the root form 
p/et-: Lithuanian p/etot/" s\c\r\ ausbreiten', Old Church Slavic yO/es/7a"FuR)Sohle' {*plet-s-na, 
to e5-stem Old Indie prathas-); but Slavic *pl§sati^ dance ' because of Lithuanian p/^st/not 
here {*plenR-); 

Old Church Slavic yO/es/e "shoulder", russ. piece 6s. (russ. belo-plekij^\Ne\{i>sc\\u\\x\o^' , 
neologism Xo plece= Old Bulgarian pleste, compare above Middle Irish leithe). 

With final sound voiced-nonaspirated: Old Icelandic flatr. Old High German flaz^ even, 
flat'. Old Saxon /75/"flat, untief (full grade Middle Low German iz/d/ds.). Old Icelandic-Old 
English flettu.. Old Saxon flet, fleW floor in Haus', Old High German flazzi, flezzi 
"geebneter bottom, threshing floor, Hausflur, Vorhalle' (Modern High German F/o/z'ebene 
Bergschicht'); Old High German /7azza "palm'; Latvian plandn^breW. make'. 

References: WP. II 99 f., WH. II 316 ff., 319 f., Trautmann 222 f., 225 f. 
Page(s): 833-834 

Root / lemma: pleR- 
Meaning: to plait, weave 

Note: presumably further formations from pel- "falten'
```


## [2026-09-14T00:50:18.258Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '65560,65600p' POK_full.txt",
 "description": "POK 805 lemma header"
}
```


### [2026-09-14T00:50:18.323Z] TOOL RESULT

```
mushroom ' : Romanian cuptor'oven', ciuperca ' mushroom ' similar to Slavic formation 

Bulgarian pecburka ' a small stove, mushroom ' : Polish p/eczara ' cave' : Old Church 

Slavic yoes/e/'a 'cave, oven' > Polish p/eczarka' mushroom '. 

without metathesis Old Prussian pectis ' stove shovel ' = Old Church Slavic pestb 'oven, 

jHohle '; Lithuanian pe/r/as 'roasted'. Old Church Slavic *pekg, *pestr bake ' in serb. 

pecem, pec/ds., etc.; Old Church Slavic pekb'heaV, potb 'Schweift' ( *pokto-), pestb 

'oven', pestera^cave, oven' etc.; 

Tocharian AB pak- 'zum Reifen bringen, cook', participle Pass. B pepaksu, A pukal, B 

pikuryear' (= ' ripeness'), common Old Indie -g"h- > -ks- : Tocharian -g'^b- > -ks- 

References: WP. II 17 f., WH. I 270 f., Trautmann 21 1 f. 

Page(s): 798 



Root / lemma: pe/a- pla- 

Meaning: wide and flat 

Material: Armenian /70/ 'earth, dust, powder, bottom, land'; Latin palam^ open, publicly ', 

Akk. as clam, from a *pela-ox pola-, alb. sh-pal, shpair reveal, proclaim '; Old Irish latharv\. 



'plan, place, position ' {*pla-tro-), to cymr. Ilawdr' britches ', acorn, loder^ canga ', bret. 
loer^ bas, chaussure ' (originally "base'); Latvian ploti^ breitschlagen ', Latvian plat^ thinly 
spread '; russ. polyj^ openly, freely, uncovered, stamped out (of the water) ', Old Church 
Slavic polje "field' ("stretched out surface, plain, area', hence the land of Polen Poland); 
Old Swedish-New Swedish falai. " plain, moor, heath, moorland '; Hittite palhi- " broad '; 

as d^-present probably here gr. nAaaaw (*nAa9i(jo, phonetically adapted to the present
```


## [2026-09-14T00:50:32.684Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 472 473 474 475 476; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | head -60; done",
 "description": "IEC leaves around p.918"
}
```


### [2026-09-14T00:50:33.772Z] TOOL RESULT

```
=== leaf 472
neggen, id. cf. E to nag, and nac- heit ‘craftiness’, Sw. nagga “bite, sting’, all with a possible IE initial *kn-)
nik- (1) “rise, excel'. Cf. WP II, 335 Per. nik, nīkū ‘excellent’; Hitt. nikmi, redup: ninik- (rise, be raised’; redup: ‘raise, gather up); Gk. nikos, n., nike, f. ‘victory’; nikáo,
845
v. denom. ‘prevail’; OCS (and com. S1.) -nika- ti, nikno, -noti ‘rise’; Cz. “be outstanding, stand out
nik- (2) ‘thrust, force, penetrate’. Cf. niks- (1) Skt. cf. nicah, m. ‘a perfume’; Lat. cf. for-nix, gs: -nicis, m. Catch, doorway’ fr. *dhuer-?); W nig, pl. -ion, m. ‘squeeze, strait’; nigio, inf. denom. ‘squeeze’; OCS nico, nicati (sic) “bud, sprout’; Srb. ničem and nicim, niknem, inf. nicati, id.; Cz. cf. v-niknout, inf. *pene- trate’; Li. cf. ninku, nikti, v. ‘tackle’; Latv. cf. nikns, adj. ‘evil’. (Isophone in Li. nykis, gs: io, m. *whim'). Cf. Lat. per-nix, gs: -nicis *per- sistent?’
nik- (3) “low; down; fall’. Cf. ni-, ni- Skt. nicah “low, base’; nicyami “lie low, be servile'; Per. cf. nigün adj. “bent downward', LW in Arm. nkun ‘abased; base’; OCS nif, OCz. nice ‘prone’; Srb. nik, m. ‘fall, lowering’; R niknuť, inf. ‘stoop’; Ukr. cf. nyknuty, inf. ‘disappear’; Cz. cf. zá-nik ‘downfall, eclipse’; Li. nykstu, nýkti, v. ‘disappear, perish’; nykùs, adj. ‘grim, awful’, cf. also nykulys, gs: -io, m. ‘decline’; Latv. nikstu, nikt, v. ‘languish, per- ish’; Big. nica se, v. ‘crouch’
niks- (1) “press, force, pierce, penetrate’. Cf. nik- (2) Skt. níksami, v. ‘pierce’; Lat. nixus, gs: -üs, m. “effort; trend"; Li. cf. ninku, nikti, v. ‘tackle’. (Isophones: Skt. niksanam *stirring-rod'; Li. niksas ‘thimble’, nikstas ‘dislocation, crack in bones”, nykštys, 10, m. ‘thumb; big toe’). Cf. also Lat. per-nix, -nicis ‘persistent
niks- (2) (nisk-, nesk-?) Arm. nex, o-st. (decay, pus; W nych, m. ‘languishing state’; nychu, v. inf. ‘pine’; Br. nech, m. ‘worry’; cf. Gael. neasg, Ir. neasc- óid, m. ‘furuncle, boil
nisdos (nizdos) “seat, nest’. WP II, 485 Skt. nidáh, am. m. n. ‘abode, nest; Arm. nist, gs nsti, i-st. ‘seat’; Lat. nidus, gs -i, m. ‘nest; Mir net, n., Ir. nead, gs: nid, mf, id.; Br. neiz, pl: neisiu, m. id.; W nyth, pl: -au, -0d, f. id.; Cor. nyth, pl. -ow, m. id.; OHG, OE, Du. nest, n. id.; Sw. näste, id. (The ini- tial of Li. lizdas, Latv. lizds, m. id. unex- plained)
nik- — nnk- (nnkió, nonkio)
10
20
25
30
35
40
45
846
nit- (1) “conflict, hostility'. WP II, 336 Lat. cf. nitor, nixus sum, v. 'strive; thrust'; Olr. nith, f. beside Mod. Ir. neith, f. *battle, conflict; nioth, m. id. (and 'death-blow"); niata, adj. (fierce, brave”, fr. *neit-); Go. neip, n. ‘envy’; OHG nid, m. ‘fray, horror, hate’; MHG nit, gs. -des, m. 'hostility'; nide, wf. ‘jealousy’; OS nith, m. ‘rivalry, hostility’; OE nip, m. “effort, hostility’; ON níð, m. ‘mockery, insult
nit- (2) 'threader; thread'. Cf. neià OCS (and com. Sl.) niti, f. ‘thread’; Li. nyty . pl. *healds'; nytis, gs; -ies, f. ‘warp’; Lai nits, gs id. ‘weavers bodkin’; cf. om. » "thread; Skt. cf. netih, f. (thread worn through the nose', fr. *neit-)
ni-teros, -tomos 'further down, nether; at the bottom, below, lowest". Cf. ni WP II, 325 Skt. cf. nitarám, adv. *below, lower'; Av. nito- ma- (lowest; OE nióer(e), neoóan, niðan, adv. ‘below, lowest? beside nip, n. ‘abyss’; MHG oder, niden ‘below’
nitios (aphetic form of eni + -itios) "own, native, kin’
Skt. (Vedic) nítyah ‘own, native’; Go. nibjis, m. ‘kinsman’. (Isophonic: Skt. nityah ‘sea’; nityā ‘plowshare’; Icel. nið, n. ‘climb’; niður, m. ‘babbling, ripple', niða, v. ‘babble, ripple’; Li. nitas ‘solder’, of uncertain connexions) nm, nmi (nom, an affirmative particle 'in- deed”, lit. take" (?)) Gk. cf. naí, naí-khi “indeed, yes’; Lat. cf. e- nim beside nam
nm-tos (nm-nós), pp. “bent, curved, in-
dented; depression, valley” Skt. natáh, pp. ‘bent’; natih, f. “bend, curve’; cf. nimnáh ‘hollow’; nimn
=== leaf 473
ám, n. ‘hollow, depression’; Gaul, nanto- ‘valley; W nant, pl. nentydd & nannau, m. id.; Cor. nans, pl. -0W, m. id.; Br. nant, pl. -ed, m. ‘brook’ For the form *nm-nós ‘low’, cf. Gk. nànos (dwarf. LW in Lat. nanus) and (uncertainly) Br. W. nam ‘blemish, fault’, cf. namn- above
nnk- (nnkió, nonkio) ‘press, force, squeeze, thrust, stab'. Cf. nnt-
Gk. násso, adj: naktós (press, cram, pile up, trampte'. The adj. nastós, also linked w. nássó, derives from a parallel form *npt-, q. v.); cf.
847 nnt-, (nntið also pí-naks, -nakos, m. “writing-tablef”; dó- naks, -nakos, m. ('two-thrust, hence “split quill, reed, arrow’); trí-naks, m. ‘trident’; cf. bo-nassos “wild bull’, fr. *guou-nnkios) and perhaps wá-naks, gs: -naktos 'ruler' and aga- naktéo (‘be incited’. Cf. ngnt- for px.); Pol. nekac, inf. ‘oppress’; Cz. v-nukat, v. ‘impress’, from *nonk-
nnt-, (nntio, nontio) *press, press on, force, squeeze’. Variant of nnk-, q.v. Cf. WP II, 317 Gk. násso, adj: nastós, as above (pf. pass. né- nasmai here; nénagmai to *nnk- above); Olr. cf. néit, f. ‘fight’; Ir. néid, f. id. (and *wound"), beside Ir. néata ‘fierce, violent’, both forms contaminated with neith, nioth, given under wt- (1); cf. also Olr. nét ‘Mars’; Go. ana- nanpjan ‘dare’; OHG nenden, id. (beside (e- gde) nindan, sv. 3 ‘grapple with"); nand, s. ‘daring’; OS naóian ‘strive’; OFris. netha ‘dare’; néth, s. ‘daring’; OE nop ‘daring; booty’; ON nenna ‘intend’; Pol. ngcic, inf. ‘allure’; Cz. nutit, inf. ‘force’; cf. (?) Hitt. nannahi, v. “drive; march" & OCS notrjo se, notriti se ‘penetrate; instil
(nó, aphetic form of type ang, q.v. in Li. nuo, Latv. no, prp. & px. “from; down- cf. Gk. nõton ‘back, top")
nó (nõu, noi) "we two’ Skt. cf. nau, id.; Gk. n6j, nói, id.; OCS (acc. & dat.) na, id.; Blg, na, nas (acc. pl. *us?) be- side enclitic ni, acc. & dat. pl. id.; Li. dial. nuo-du, id.
nobh- ‘nave, navel, hub, centre’. WP I, 130 Skt. nábhyam, n. id.; Av. nabis, f. ‘navel’; Per. naf ‘navel, middle; Oss. Dig. naffä ‘navel; OHG naba, f. “hub, nave’; OE nafu, d. ON nof, f. id. OHG cf. nabalo, wm. ‘navel’; OE nafela, wm. id. beside nafeóa, wm. ‘thub’; Latv. LW naba ‘nave’; Finn. LW napa ‘navel, hub’. (Latv. naba also = ‘navel; axle- tree, crossbar of plow’)
nobhesos (nebhos, -es-?) ‘centre-bit of drill (9). Cf. nobh- above ON nafarr, ds: nafri, m. *gimlet'; Cz. nebozez, id.
nóbhrios ‘fine, acute, astute’. Cf. ono (nö), bhrio (3) Arm. nurb, gs nrbi, i-st. “thin, fine'; Bayr.
, nontió) — nö-
20
25
30
35
40
45
848
(alleged) nuober ‘able’; MLG (alleged) nofer, id. (Holthausen); ON noefr “clever”
nódos, is, io ‘knot, tie’. WP II, 328 Alb. (LW or « *nodio) nye, gs: neni, m. & nye, def: nyja, f. id.; Lat. nodus, gs: -i, m. ‘knot, noose, knot in wood: MLG nuot, sf. “joint, fitting; LG opt nüte, f. ‘wood joint, dovetail, mortice'; Du. Fris. neut, f. ‘tenon, bolt, nut’; Icel. nóti, m. “match, equal" beside nót, f. pl. nætr "large net’; Norw. not, pl. noter, Sw. not, pl. -ar, f. 'fishing-net; Ukr. cf. pry-nada ‘lure, charm’; Cz. cf. v-nadidlo, n. ‘bait’
nogudos, nogutos (noguito-) ‘naked’. Variant: nogumnos (nogunos, nongu-). WP II, 339 First form in Lat. nūdus; MIr. nocht, Ir. nocht; W noeth; Br. nôaz; Cor. nōth; Go. naqabs; OE nacod; MHG nacket & nackent, (G dial. nackend); ON noktr & nokirðr, id. beside mod. nekt, f. ‘nudity’. Second form in Skt. nagnáh; Hind. Sind. nanga, Romani nango; Av. mayno (sic), id.; Arm. cf. t-nank, gs: -1, ab.s: -av “poor” beside s-nank, i, av ‘bankrupt’; MHG nacken; ON nakinn; Sw. naken “naked. (The antecedents of Per. nang, Kurd. neng ‘shameful; shame’ and of Gk. gumnós ‘naked’, < *p-gum-? are obscure). Cpd. in Oss. bá$- näg “naked? and perh. in Gk. kín-nabos 'sculp- tor's model, if for *-nogu-?). A long-gde form arises in OCS and com. SI. nagü “naked; 
=== leaf 474
cf. R naglyj ^barefaced, impudent; Blg. naglo, adv. ‘impudently’; Li. nuogas *naked'; An e- gde form arises in Hitt. nekumanc ‘naked’, fr. *ne-gum- ‘uncomely’?
(noguhos, à, variant of type onugh-, q.v. in Icel. naggur, m. ‘peg’; Li. nagas, naga ‘nail, claw, hoof; Latv. nags, m. id.)
nóg- (1) ^whim, triviality, fancy, dalliance, teasing, mockery'
Per. nàz ‘flirtation, flattery’; cf. nazuk ‘flashy’; nàzidan, inf. ‘flirt’; Gk. cf. nógala, npl. ‘snacks’ (if not < *no, eno, and *&olok?); OLat. nogae, cpds. naug-, Class. nügae 'trifles'; Fris. noekje “darling, favourite" beside noekerje, v. ‘cajole, coax’; (but G Nucke, Nücke, f. *whim' is fr. MLG nucke, id., and Du. nuk, f. id. is appa- rently fr. LG); R cf. za-nóza, f. ‘irritant; irri- table person' (?); Li. (?) nuoZ-mas, -mus, adj.
849
“grim”
nóg- (2) Q) Per. nàZu 'fir, juniper'; Oss. naz, nazu, id. beside näzí ‘Scotch fir; LW in Arm. noč, noci ‘cypress and in Georgian nadzvi “fir
noid- ‘hate’. Cf. ne-, n-, uoid- (?). WP II, 322 Skt. cf. à-nedyah ‘blameless’; Go. ga-naitjan, v. ‘denigrate’; MHG neis, s. ‘torture’; neisen, v. id.; OE nætan, v. “hurt, harm'; ON neita, v. “deny, refuse'; Latv. naids, m. “hate, hosti- lty’; cf. (z-gde) nidu, inf. nist, v. ‘hate’. (For Gk. ón-eidos, n. “shame, blame”, cf. uon- “lack? and ueidos 'face")
noigos, à “gentle, fair; gentility, fairness, beauty” OCS něga, f. ‘delight’; R ‘effeminacy’; Srb. ‘cherishing’; Cz. něha ‘gentility, fondness’; Latv. naigs, adj. (3) ‘beautiful
noigh- OE nægan, v. ‘accost, attack’; ge-nāg (hapax) ‘dashing’; Latv. naigs, adj. (1) ‘quick’
noik- ‘force, impetus’. Cf. neik-, nik- (2) Lat. cf. per-nix, -nicis, adj. (quick; persistent". Vocalism ambig.); Latv. naiki, adv. ‘violently, excessively’; (Li. isophone: naikùs 'perish- able’). E-gde in Gk. neikos, n. ‘strife’; z-gde in Gk. nike ‘victory and in Li. i-nikti, pr. -ninku ‘strive; tackle, grapple with’; i-nykis, gs -io, m. ‘gusto’ Å
noit- (nit-) (1) “inflame, kindle; be inflamed, burn brightly”. Lat. niteo, ere, v. ‘shine’; cf. nitidus, adj. ‘bright’; o-gde in OCz. nietiti, Pol. niecic, Slovene netiti, inf. (inflame, kindle’. Not re- lated to the OCS type gnétiti ‘inflame, arouse’)
noit- (2), o-gde variant of type *neit-, see nit- (1) Lat. cf. (vowel ambig.) nitor, sup. nisus & nixus (of two separate origins but here in the sense of “strive*); Cz. cf. pod-nét 'enter- prise’; pod-nítit, inf. ‘undertake’. (For sup. nixus, cf. niks- (1) above)
(nói, nou, forms of the dual number "we two’. See no. WP II, 320)
(noios ‘turn, bent, aptitude’, see neio (2) ‘turn’. O-gde only in Gk. noüs and nóos “mind”, cf. Eng. sense of bent ‘aptitude’, and
nóg- — noktiór (noktor)
10
15
20
25
30
35
40
45
850
G Gewandt-heit. Isophonic in Skt. nayah “lead, conduct’, but this relates to neio (1))
nokterinos ‘nightly’. See noktis & nokts. WP II, 317 Gk. cf. nukterinós ‘nocturnal’; Lat. cf. noctur- nus, id.; OE nihterne, id.
noktím ‘by night, at night, yesterday night. Cf. nokts, noktis Skt. náktam id.; Tokh. A noktin “in the even- ing; MHG nehten “last night; OPr. naktin ‘by night; Li. nákti, id.
noktis, nokts ‘night (ultimately *noqutis, *noquís (?) in view of the vocalism of Gk. nux and Li. nakvóti, v. ‘spend the night, with an echo in Hitt. nekuc “evening, night- fall’, e-gde indicating the approach to night, as also in Tokh. B nekciye “in the evening, For a possible u-affection in Gk. cf. püksis under poks- below, and híppos (?); -u- and -i- for *-o- & *-e-. The i-stem seems to denote ‘night when counted; the consonantal form a familiar entity, as in Lat. vox, dux, lex, sol ‘the voice’ etc. I-stem in Skt. (Vedic) náktih, f.; Ober naktin, acc. sg.; Tokh. noktin and niktin ‘toward evening’; Lat. nox, gp noctium, but OLat. nox ‘by night; Ir. a nocht, in nocht 'to- ni
=== leaf 475
ght; W nôs, Br. noz, pl. nosiu, f.; Cor. nos; OCS oos Cz. noc, npl. noci; Latv. nakts, gp: nakéu. Cons.stem in Vedic nak, m.; Gk. nux; Alb. natë, pl: net; cf. nádje “in the morn- ing; Go. nahts £.; OHG naht, npl. id., gp: nahto; OE niht (fr. *nekt- or *nequt-); ON. nátt, nótt; Cz. veliko-noce, pl. (great nights? = *Easter); Li. naktis, gp naktü. Cf. also Go.
` nakts ‘by night’: OLat. nox, id. and Italo-Alb.
nesé (*tomorrow', fr. *noktjo ?). Vedic nak- tam, n. ‘night unexplained, except as an ar- chaic adverb > noun, see noktím
noktiom, -noktiom, adv. & collective of type nokt-, see above Gk. cf. meso-nüktion; Lat. tri-, aequi-noc- tium; MHG ein-nehte; ON javn-nsetti; cf. also OCz. noci “by night’; Blg. noščė, wd: Li. nakcià beside nákti, id.
noktiór (noktór) “by night, the evening be- fore; next night Per. cf. nahar ‘breakfast’; Gk. cf. nüktor “by
851
night; Alb. nesër, dial. nestër ‘tomorrow’; Lat. cf. noctur-nus ‘nocturnal; W neithiwr and neithwyr “last night’; Br. neizcer, neizür, neichur, id.; Cor. nyhewer, id.
nokeio ‘injure, kil. See neK- (1) Skt. na$áyami ‘destroy’; OPer. cf. -na0ayatiy, 3s. ‘injures’; Lat. noceo, -ere, v. ‘harm’; Li. cf. nasle, f. ‘widow’
noKus ‘bearing, burden, weight; weighing, oppressive’. Cf. neK- (2) Hitt. nakkus & nakkis “heavy, difficult, impor- tant; W (?) nog, m. ‘stoppage’; OCS (and com. Sl.) -nosü (vü-nosü, iz-nosü) (convey- ance’; Li. oaëus adj. ‘productive’; cf. našta, f. burden, weight, produce’; Latv. nasta, f. id.
nóm-, long o-gde form of nem- (2). WP II, 330. Cf. nomos (1) below Per. nàme "book epistle’; Gk. cf. nómáo (1) ‘share’; Li. náoma, f. rent beside nàomoju, oti “let, hire out; Latv. noma, f., nomåju, at, as Li.
nõmn-, nómen- (form of ono-mnm, q.v.) “name”. Aphetic in Skt. naman, n.; OPer. nàman-; Per. nàm; Oss. nom, pl. námtà, Dig. non, pl. nändtä; Du. cf. noemen, v. ‘to name’; Fris. neame, id. (A type *nomo(n) is represented in Go. (and general Gmc.) namo, etc. Cf. ang, ono). WP I, 132
nomos (1) “part, share, division, decision. Cf. nem- (2) Vedic námah ‘pasture’; Per. cf. name "book epistle’; Gk. nomós, nomé, m.f. ‘pasture; abode; district; nómos, m. “law, custom": Lat. cf. numerus, 1, m. ‘number’; Li. namai, mpl. ‘house’; Latv. nams, m. id. (and 'scullery). WP II, 330
nomos, is (2) 'turn, bend'. Cf. nemo and nemos (1) Skt. cf. namráh ‘crooked’; Gk. nomeis, pl. ‘ribs of ship’
nondh- (nndh-) “press, swell, drive’. Cf. WP II, 316 and nnt- (nont-) Per. cf. (z-gde?) nad “increase, abundance"; Hitt. cf. nannahi, v. ‘drive, march’; OCS noZdo, noditi, v. ‘thrust, force’; Pol. cf. nedza, Cz. nouze, R nuždà ‘misery, need'; cf. also
nokeió — noruos, à
10
15
20
25
30
35
40
45
852
(if w. *-n-) Vedic nàdhamanah ‘importunate’; nadhitáh ‘oppressed, needy’. (For OHG nen- den “dare”, ge-nindan, sv. “be eager”, and ON nenna "be keen on, woo', see nnt-)
(noqu-, ultimate theme of type *noktis, *nokts, q. v. and cf. nqu-, nqut- Cf. Hitt. nekuc-; Gk. nukheüo “watch through the night; nukhth-émeron, n. "a day and a night', and the vocalism of nüx 'night'; Li. nakvinti, inf. “put up for the night; nakvyne *night's lodging")
nor- (1) “penetration; inside; interior; depth’. Cf. nið, enor-, ner- (2), nerteros. WP IT, 333 OCS norü, m. “den, hole, cave, nest’; nora, norja, f. id.; R norà, f. ‘burrow’; Ukr. norà, f. “hole; source, spring’; Li. náras *diver-bird', cf. naroms, adv. “under water; narüs, adj. “Table to sink”
nor- (2) “join, joint Per. narà ‘partition wall (?); Sw. nara, f. 'car- penter's nail; Li. narys, gs: -io, m. “joint, link, member’; Latv. naris ‘fetter on horse's leg; fetlock'; nàrs (with syntactical length), m. 'vice, clamp'
nor- (3) (?) “narrow, close’. Gmc. fr. *nor- quos in view of Finn. LW, but see noruos (2) below Oss. cf. nárág ‘narrow’; OS naru, OE nearu “narrow, close, strict; OE nearu, gs. we, s. ‘danger’; Finn. (LW) narka, adj. ‘narrow’; Li. (?) narávas, m. (archa
=== leaf 476
ic) ‘power; force; tyrant; (mod.) ‘obstinacy’
(nōr-. See Supt: N)
noruos, å (1) ‘incision, groove, burrow, cut, mark, impression; character, habit'. Cf. en-, rouið, rouos, rüió OHG narwa, f. ‘scar; MHG narwe, nar, w. & sf, id.; LG nor, wf. id.; G Narbe, f. d EMSw. narf, Sw. narv, m. 'pockmark, pitted skin’; OCS nravü, m. ‘manner; OCz. nrav ‘custom’; Slovene nráv ‘nature’; R nòrov ‘habit, man- nerism'; Ukr. norov ‘temper’; cf. also Cz. po- nrava ‘larva’; Li. nařvas, narvà, m. f. “cell of honeycomb; cage’; cf. also (?) narávas, m. (*obstinacy'. See nor- (3) above). (For Hes. norbá ‘incision’: Go. at-snarpjan: Du. sner- pen; ON snerpa, see snorb- Supt)
853
noruos, à (2) (?) “narrow; strait'. See nor- (3)
nos “we, us’. Cf. menes, mnés, ns, mes (“me and yow as against ‘me and mine’, hence the varied phonology). Cf. WP II, 320 Skt. nas, acc.gen.dat. ‘us’; Hitt. -nas, acc. & dat. id.; Av. cf. na, adj. our: Alb. na, ne(ve) ‘us’; Lat. nos, prn. ‘we, us’; OCz. ny, nas, prn. ‘us’; OCS ny, nasü, as OCz.
-nos, -nom, -nā (theme of medio-passive participle. Cf. -tós, -tóm, -tà, theme of pas- sive part. with an implied agent). Cf. -men. Skt. cf. dináh, stirnáh ‘given, strewn' as against ditáh, strtáh, id.; sannáh 'seated" as against sattáh, id.; Gk. rhignós ‘perished w. cold”; sparnós ‘rare’ as against spartós 'scat- tered'; Lat. plenus “fulP as against com-pleétus; G ver-dorben as against ver-derbt; E shaven, rotten, molten as against shaved, rotted, melt- ed, etc.
(noseió, frequentative of type nes- (2) ‘turn’, in Gk. noéó ‘turn over in mind, consider, know’, etc.)
nósít- (prob. for *onóo-sth-) “application, addiction, emphasis'. Celtic forms ambig. Cf. Ir. nós, m. ‘custom, habit (phon. uncertain); W naws, pl. au f. ‘nature’, cf. nawd, f. id., adj. “kind, soft’; Br. ncez, f. “way, shape, look, pretence’ beside (LW fr. W?) naóz, id.; Du. noest, adj. ‘hard-working’; Latv. nost, adv. “gone, away, dead? beside nostāja, f. (fr. no + stāja 'attitude")
nót-, os (1) (notis) (prob. for *onót-, see ono:
Gk. áno “above on top”, etc.) Oss. nag (queried: ‘top, surface, cover, back"); Arm. nuk, acc: nus, s. ‘back’; Gk. nótos, m. “surface, ridge, back, backside’; Lat. cf. (vari- ant) nátis, usu. pl. nátes ‘backside’; MIr. nát, s. ‘buttock’; Cz. nat, f. gs: -i “part of a plant above ground; radish- or turnip-top'. Cf. WP II, 340 e
nót- (2) (notiom, io) (?). Cf. nost-, snadh-
(2). (Celtic initial uncertain) W nawd, f. ‘nature’; adv. ‘easily’; Fris. noed (care; responsibility; risk. Phonol. ambig. *notós?); Icel. cf. naeói, if for *noeói, n. “lei- sure, rest’. (Equations uncertain)
noruos, à — nii, nün, nünai
10
15
20
25
30
35
40
45
854
notis ‘wetness; wet’. (Phonol. ambig. snot-?) Arm. naj, gs. -i, Lët ‘wet, moist’; s. "liquid"; Gk. notis, f. “moisture? beside nótios “wet, rainy'; noterós, id. (The parallel form indi- cated by G nass ‘wet; netzen, v. id. and Go. ga-natjan, id. suggests the initial *no-)
noudos, à, om ‘stand-by, useful object, trea- sure, object of wealth, good companion'. WP II, 325. Cf. nud- MHG n03, sn. ‘farm animal’; G Noss, n. “head of cattle’; OE neat, m. “follower, companion, tenant-farmer'; n. ‘ox; cf. also OHG gi-noso, gi-n07 w. & s. m. ‘companion’; ON nautr, m., obi. naut-, m. *partaker; donor; gift; n. ‘cattle’; Finn. LW nauta ‘head of cattle’; OCS po-nuda, f. ‘gift, food-offering'; Li. naudà, f. “property; benefit; Latv. nauda, f. ‘money’. (Isophone in Ukr. nudkyj 'sweetish'. Here?)
noudheið ‘urge, force’. See next. WP II, 316 Go. naubpjan, v. ‘force’, beside naudi- in naudi- bandi, n. ‘fetter’; OCS nuZdo, nuditi and com. SL, id. (not related to noZdo, noditi, see nondh-); MHG noeten, id.; OE néadian, v. id.; (alleged naudei, ds ‘to force given by SF as OPr., misspelt nautei)
noudhos, à, is, io ‘urge, force, nee
```


## [2026-09-14T00:50:42.337Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'(?m)^\\s*91[789]\\s*$', l):\n        print('LEAF',i, [m for m in re.findall(r'(?m)^\\s*(9\\d\\d)\\s*$',l)])\nEOF",
 "description": "Locate IEC page 918"
}
```


### [2026-09-14T00:50:43.352Z] TOOL RESULT

```
LEAF 509 ['916', '917']
LEAF 510 ['918', '919']
```


## [2026-09-14T00:50:46.227Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(leaves[510])\nEOF",
 "description": "Print IEC leaf 510 (pp.918-919)"
}
```


### [2026-09-14T00:50:47.345Z] TOOL RESULT

```
 ‘film’
peln- (2), pelnos, å ‘yield, produce, earnings, plenty’. Cf. WP II, 51 & 61 Skt. panah, m. ‘pledge, bet; pay, goods; busi- ness, wealth’; Oss. farn, s. (peace; plenty, fortune’. Vowel w. secondary length); Arm. cf. holonem, v. ‘gather’; Gk. cf. pélanos, m. ‘sacri- ficial food, libation’; Alb. pjellë, f. “yield, pro- duce, offspring’; Olr. ell, f. ‘advantage’; Ir. eall, s. ‘flock beside eall-ach, s. ‘belongings, cattle, sheep’; OCS plënŭ, m. ‘booty’; R plën, m. ‘captivity’; plénit, v. “capture; captivate’; Pol. cf. plenny, adj. ‘fertile’; plenic se, v. *mul- tiply?; Li. pelnas, m. ‘profit, advantage’; Late pelna, f. “earnings”; cf. no-pelns ‘merit
(peln- (3), see pel- (2). In Latv. pelni, mpl. *ashes'; cf. Li. pelenai, id.)
pelo “strike”, etc. see pel- (1)
pelos ‘chaff, straw’. Cf. pel- (2), pal- (2) Skt. palah, m. ‘straw’; Li. pelai, mpl. ‘chaff; pélas, m. ‘awn’; Latv. cf. pelus, pelavas, pl. ‘chaff; OE cf. fileóe, filióe, n. “hay?
pels- (extn. of type pel- (1), q.v.) “strike; abuse'. Cf WP II, 57 Gk. cf. a-péllo, a-peiléo, v. “round up; threa- ten; boast; swear’; Lat. pello, ére, pf: pepuli, v. ‘strike, beat, knock, drive’; cf. pul-mentum, n. ‘porridge’; Umb. pels-, v. a-st. ‘mince, pulp, mash’; pelmner, gs. ‘of porridge’; Cz. cf. plis- nit, v. (abuse, fr. *pelsnijó); Latv. cf. pelsans ‘loose, friable’
pelsmn- (pelsn-) (1) ‘sole, base’. WP II, 58 Gk. pélma, n. ‘sole; slipper; pediceľ; OCS plesna (for *plěsna? ‘sole, base’)
pelsmn- (pelsn-) (2) ‘powder, dandruff, mil- dew, hoarfrost'. Cf. pel- (2), pelm- (1) Arm. eyeamn, gs: eyeman 'drizzle; hoarfrost'; Alb. cf. plehén, pl. plehna 'sweepings, rub- bish, manure’; OCS plësni, f. (^mildew', and com. S1); Li. cf. (variant) pelesiai, mpl. id.
pelt- (1) ‘wrap, cloak, cover, screen. (Indo-
peln- — pendo, ëið
20
25
30
35
40
45
918
Iran. ambig. Cf. prtos) Skt. patah, m. “cloth, garment, screen, can- vas? beside patalam, n. “cover, basket, hive, cataract on the eye’; Per. parde ‘veil, curtain’; ON feldr, pl. feldir, m. ‘cloak, coat. See next
pelt- (2) (Same as (1)?) ‘space, patch, flat surface’ Gk. (ambig.) pélte ‘shield’; (LW in Lat. pelta, id.); MHG vëlt, gs. -des, sn. (and com. Gmc.) ‘field, plain; field on shield, chessboard square, face of dice’; OE feld, m. (“'plain', etc.); (LW in Finn. pelto ‘field’)
pelu ‘much, many’. Cf. polu, poluos, peluð, peln-. WP II, 65 Arm. cf. h-olov, i-st. adj. (much, many”, fr. *en-peleu-); Lat. cf. polleo, ere, v. (“be strong’, fr. *pelu- or *polu-, q.v.); OIr. il ‘many’ be- side s. ealbh, m. ‘flock’; W elw, pl. -oedd, m. ‘gain, profit, goods’; Alb. cf. pjellë, f. *pro- duce' (ambig. cf. peln-); Go. OHG. OS filu ‘much, many’; OE fela, Du. veel, id.; ON fjol-, cpds. id.
pelu-, see peluos & pélouos
peluà (a tree: ‘sallow’ or ‘alder’) Oss. fürwe ‘alder; OHG félawa, f., MHG vëlwe, s. & wf. ‘willow’; G. cf. Felber ‘white willow’
peluis (“basin”, etc.) see pelouis
peluo (1) “yield, produce’. Variant of type peln- (2), q. v. See next Arm. cf. h-olov, gs: -i, ab. s: -iv ‘much, many (fr. *en-peleui-); Alb. piell, aor: polla, v. *pro- duce, bear’; pjellë, f. “produce, offspring’; Ir. ealbh, pl. -aidhe, m. ‘flock’; W elw, pl. -oedd, m. ‘gain, profit, goods";
peluo (2) “fill”. Cf. pelu, polua, pluos, pinos Skt. parvàmi, v. id.
peluos ‘dust, specks, chaff. Variant pelouos, q. v. Cf. pelsmn- (2) Oss. cf. fárwakà, färakä ‘bran’; Skt. cf. palavam, n. ‘chaff, husks’; Lat. (e-, o- or z-gde) pulvis, gs: pulveris, m. ‘dust, powder’; ON. fol, f. ‘thin blanket of snow; R. Ukr. polóva, f. ‘chaff beside Ukr. pliva, f. ‘film’; Cz. pleva, f. ‘chaff ; Latv. cf. pelavas, pelus, id. (pl.); LW in Finn. pelu ‘chopped straw, chaff
(pēmn-, see Supt: P)
pendo, eio (1) “hang limp’
919
Lat. pendo, Gre v. “weigh: pay, be fined"; pendeo, ere “hang, linger, hover, stoop’; Li. pendZiu, pendeti, v. ‘languish, fall ill
(pendó (2), see
```


## [2026-09-14T00:50:59.783Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD grep pardag\"; grep -n \"pardag\\|pardag\\b\\|pltk\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD leaf 85\"; awk 'BEGIN{RS=\"\\f\"} NR==86' PHD.txt | head -60",
 "description": "MacKenzie pardag"
}
```


### [2026-09-14T00:51:00.868Z] TOOL RESULT

```
=== PHD grep pardag
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:1470:curtain pardag.
PHD.txt:4198:veil čādur, pardag.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
PHD_mackenzie.txt:4022:pardag [pith I N parda] veil, curtain.
PHD_mackenzie.txt:6338: curtain pardag.                           deceived freftar.
PHD_mackenzie.txt:7894:veil eadur, pardag.
PHD_mackenzie.txt:8596:paseminih         -"'"U t""6\)U Q)      pardag                      \~~Q)
=== PHD leaf 85
[nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
nizārīh 61 0$
—jh: weakness. nizārīh- [nz?lyh-] become weak. nē [ТА < A t£? | М пол, N nuh] nine. nóg [nek! | М mwg, N naw] new, recent. ~erz [-hvc | N nawróz] New Year's day. ---zád(ag) [-z't(k)! | N nawzàád] new-born. nohom [nhwm | = M, N ~] ninth. nózdah [nwzdh | № ~] nineteen. nin [KON < A k‘n | M, J поп] now.
O
6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -man
```


## [2026-09-14T00:51:02.037Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN farāx\"; grep -n -i \"far\\[aâā\\]x\\|farâh\\|fara<u>h\\|fraθah\\|frathah\" HRN.txt | head -20; echo \"=== HRN leaf 201 (p180)\"; awk 'BEGIN{RS=\"\\f\"} NR==202' HRN.txt | head -60",
 "description": "Horn farāx"
}
```


### [2026-09-14T00:51:03.165Z] TOOL RESULT

```
=== HRN farāx
=== HRN leaf 201 (p180)
— 180 —
ap. ^\^, fra\ plilv. fra bezw. /ar, arm. LW. ]ira-\
ai. ]prd,
kurd. AiZ-, hol-,
808. /<9ri* 'Glanz, Majestät*, ferre^ yurve % vergl. /eveme
(arab. /avarnaq).
ap. N. pr. Vi(fi)da]fa7'na' ; aw. /^'arenah- *61anz';
phlv. N. pr, Farn[hag^ N(a)pl\farnai (Gemme, Hörn,
Mitteilungen, Heft IV, 24), arm. LW. par[lc, päz.
yj'areh,
np. ferrux 'glücklieh', phlv. farraxü, farraxülh
('Glück*) sind durch «(-Epenthese entstanden; vergl.
auch ferytinde.
Vergl. 0f()o/di'7]g' ro d^oroitia rrjv tov uaylaXQov
aii'av rfi QUif.iaYy,ri ivariJ,ialvBvai yXidrrrj (Theoph. Simoc.
IV, 2), Ferru/än, Ferruhän (Nöldeke, Tab.-Übs. 292,
Anm. 2). Hohe Würdenträger führen auf Gemmen
den Beinamen farra/ß (Hörn, a. a. O., 39).
809. ferä, Praefix, 'auf, zu, in' z. B. in fera/m\ auch
selbständig, z. B. ferä restden, yiriften,
aw. frä' in fra\keresta', frä[cidra' etc., ai. prü-
z. B. in präkära-,
810. feräji weit, breit', feräxh \S'r>X-lS (Is. 15, 3).
aw. fradah' Breite'; phlv. /räA bezw. /röA[e] 2),
fräh[(f\T.h^ fräh[e\Jmtan^ frah[e\kart (aw. Vourukasa-),
fr äh[e]raftar (Himd.), fr{ä)hgöyöt {av^woiiru.gaoi/aoUi');
ai. präthas'.
kurd. LW. (?) fereh 'weit'; bei. LW. präh^ präh
weit, breit' (303).
*) Nicht *Teil, Provinz' in Ardeslr ^urre (wie bei Vullers s. v.
xurre)^ vergl. Nöldeke, Tab.-Übs. 11. — Bezzenberger^s Ver-
wendung des päz. ^^'arehy -^'^arehmand bei Fick *, Seite 341 ist falsch.
2) Oft ein Strich zu viel, z. B. vd. 14 (23) Gl.; ich halte die
Form /m/i, frähih etc. aUein für richtig, vergl. /räfi[varst (vd. 18
(128)). Man könnte natürlich auch schon im Pehlevl ffäx lesen, doch
sclM'iiit OS besser, «lor Päzondausspraclie, welche h hat, zu folgen.
```


## [2026-09-14T00:51:19.200Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leafpage(fn, pat, ctx=0):\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    leaves=txt.split('\\f')\n    for i,l in enumerate(leaves):\n        if re.search(pat,l,re.I):\n            print(f'--- {fn} leaf {i}')\n            print(l[:3000])\n            print()\nleafpage('LKT.txt', r'parde|pardah|purdah')\nEOF",
 "description": "Lokotsch parde"
}
```


### [2026-09-14T00:51:20.289Z] TOOL RESULT

```
--- LKT.txt leaf 159
b232.
1629.  Pers.  pärcäm: 'Haarlocke',  ebenso  tk.  periem  'Haar- locke auf  der  Stirne';  hieraus  bulg. percem,  peröiti,  serb.  per  ein;  rum.  per- ciun  'Schläfenlocke  der  Juden,  Peies', perciunat  'Jude'.  [Löbel  EITAP  75. Mikl  SlEtWb  241a.
1630.  I'ers.  pärdä:
'Vorhang',  tk.  ebenso  perde;  hieraus bulg.  perde  'Schleier;  Geländer',  serb. perde  'Bettvorhang';  lum.  perdea  'Vor- hang, Gardine',  perdelufä.  Hieraus wurde  auch  ar.  barda'a,  s.  hier  Nr.  228. [Löbel  EITAP  75.    Mikl  SlEtWb  241  b.
1631.  Hebr.  pardes:
'Paradies'  ['Wonnegarten'  aus  altpers. pairidaeza  'Umzäunung,  Garten'],  gr. irapdbeiooq,  lat.  paradisum;  hieraus  frz. paradis,  sp.  paraiso,  it.  paradiso,  rum. paradis;  engl,  paradise,  dtsch.  Paradies. Lautgesetzlich  entwickelt  mit  volks- etymologischer Umgestaltung  trz.  parvis 'Vorhof  der  Kirche'.  Nfrz.  paradis  war bei  den  Mysterien bühnen  im  Gegensatz zur  im  Vordergrunde  gelegenen  Hölle ein  Platz  auf  einer  Anhöhe  des  Hinter- grundes, jetzt  der  oberste  Teil  des  Zu- schauerraums auf  der  Galerie  [sonst  frz. poulailler;  vgl.  dtsch.  'Himmelreich, engl,  up  among  the  Gods].  Vgl.  Otto Driesen,  Der  Ursprung  des  Harlekin. Berlin  1904.  (Forschungen  zur  neueren Literaturgeschichte,  herausgegeben  von Muncker.  XXV.)  S.  83, 163iJ.  Fers,  pärgal: 'Leichtes  Linnen  oder  Kleidungsstück daraus';  hieraus  sp.  percal  [Dicc  Gast 1531  c]  'Baumwollstoff',  weiß  oder  bunt, mehr  oder  weniger  fein,  percalina  'ein- farbiges percal',  frz.  percal,  perkal,  per- caline  'weifses  Baumwollenzeug';  dtsch. Perkal.
1633.  Hind.  pargana:
'Bezirk'  [vom  sskr.  pragari  'abrechnen', vgl.  pers.  pärgänä  'Provinz,  Distrikt' Horn  NpEt  S.  67,  Nr.  302];  hieraus angloind.  engl,  pergunnah  'Unterbezirk', der  mehrere  Dörfer  umfaßt.  [Hobson- Jobson  698.
1634.  Pers.  pari:
'Guter  Genius'  [Horn  NpEt  S.  69,  Nr.  310 im  Gegensatz  zu  dlw,  s.  hier  Nr.  509; vielleicht  Weiterbildung  von  pers.  pärr 'Flügel'  ebenda  S.  65,  Nr.  293,  also  etwa 'geflügelt'];  hieraus  sp.  peri,  frz.  piri; engl,  peri  [womit  natürlich  trotz  der gleichen  Bedeutung  fairy  <^  frz.  feerie <  lat.  fatum  nichts  zu  tun  hat],  dtsch. Peri  'gute  Fee'.  [Eguilaz  470.  Devic DEt  185/186.
1635.  Pers.  pärkär:
'Zirkel'  [aus  fers,  pär-  'herum'  und  k&r, s.  hier  Nr.  1069],  tk.  perkjar,  vulg.  mit Dissimilation  pergel  [Kdekian  Kämüs 319b]  'Zirkel';  hieraus  rum.  perghel 'Zirkel,  Gewölbe';  hn\^. pierigel  'Zirkel'.
1636.  Tk.  parmak:
'Finger'  [vom  Stamme  bar,  var  'vor- wärts gehen'  Vämbery  TktEtWb  S.  200, Nr.  210] ;  hieraus  rum.  palmac  'Daumen', als  Maß  o  cm;  i^ormac  'Pfahl,  Pfosten', parmacUc  'Geländer';  bulg.  parmakhk 'Geländer'  [wie  schon  türk.  parmaklyk 'dass.].
1637.  Pers».  pärtüw:
'Glanz'  [Horn  NpEt  S.  66,  Nr.  296],  tk. ebenso  pertew  [Kelekian  Kämüs  318a]; hieraus  rum

--- LKT.txt leaf 234
  120
ört'«;  145 bähal  180 Äa^wr  180 hajib  145 hakbük  187 Järwx  256 iarze/  259 iätoÄ  267 bdtü"}!,  267 heheinä  283 6eZi  287
1461a ftg.tgw  293 böhü  2085
tZäßär  514 rf«/  468 dallü^  468 Z)a!<j»b  503 dibb§r  514
^sgr  127 esöß  566
öfäß»»  716 ^äw«ß  659 ge  705 gezera  713 ^f/wg^  721 <7öi  728 i^öqpgr  727 göräl  731 gulgöl^b  743 Aäßar  764
j^ße/-  764
AäTaT  77V
haxäm  788
Äa/äZ  793 I  hatta'  845 I  ^ßra  857 j  Miele  858 I  ÄösTa  87i:
I  H^ri  12 >'a;  287 jaklfir  928 iäwaÄ  932 jäSa  872 jößei  959
kabbäla  977 fcab  988 A-a/f  990 kähäl  1000 Ä;a«ä  1035 kammön  1046 i^nas  1050 Ä;äq)ar  992 kappära  1068 i^saß  1107 Ä-äse?"  1112 ]  käsln  1113 I  Äräöaß  1168 fcäfön  1126 I  käza?  1059 j  fcgbgm  1149 kelatp  1154 I  ierwß  1165 I  kesil  1166 !  Äreöißä  1168 i  kippfr  1068 I  kisse  1190 fco/  1194 köcper  992 ÄJorMn  1208 i^«  1264
läSön  788 ;  /eß  1312 I  le^önä  1331 Zew«»  1315 lücjäQän  1325
mab  1490
mäfal  1479 I  maggäl  1479 I  »i«M-fßfö  1375 i  mamzer  1388 j  ma«ä  1398 j  wä'ös  1402 j  mai-'e  1412 I  massa  1441 j  mazol  1920 !  mazzäl  1455 ^  we'is  1402 j  rng/gx  1379
mifdal  1461a
mö'cf  Uli
mötal  1479 »nüö  1524 «erd  1548 Mfö^r  1567
pardes  1631 p(Ss<ife  1641 pelefä  1643 p^sah  1652 pjigTgä  203
räßrtÄ  1677
ratö  1678
ra^säkeh  1679
rahmänl  1687
räkarrt  1694 I  sa'aqp  1734 j  saötoa  1742 I  *'äT«T  1757 '  sähar  1763 I  safc  1781 !  ^äkal  1880
söfcar  1788 i  Mxar  1787 !  sä/fca«  1789
M/aq?  1804
sdma/  1811
sämar  1813
sdqpaZ  1761
sapptr  l83i) I  sän/cp  1885
säö«  iy27
sätän  1867
sgfcfZ  1880
semlra  1813 1  IfwiM^ä  1884 !  secper  1830 I  serä9m  1885
sibhöl^b  1891 I  strfrfäx  18'32 '  söcpe/  1751 i  söq)er  1830 i  sölan  1958 I  sö<e  1927 !  süs  1776
«(SÄad  1984
<äiö  2002
iä^ias  1978
ießd  1975 I  tef^illa  2068 ;  Jere(pä  2070
<öß  208 i :  iöÄft  2085 i  3!?ßf/  -'210.
Italienisch  (einschl.  Dia- lekten, sizilianisch  u.  sar- disch). dial.  =  dialektisch sard.  =  sardisch siz.  =  sizilianisch abadessa  1
Italienisch.  I
204
(ibate  1
ar^^rtHM  siz.  49J
beduino  1 64
abhadia  1
assaccari  siz.  1783
belgioina  1 332
abbate  1
assaccu(ni)  siz.  1783
belgiui  1332
uboifino  1471
assammarari  siz.  1816
belzebu  145
accanzari  siz.  lOöl'
assagsinar  839
betzuar  1605
acciaccarc  1785
assassino  839
belzuino  1332
ncciacco  17^5
asMft  1897
benzoino  1332
acciaffari  siz.  1734
afaöa^/o  1971
bergamotta  282
affarari  siz.  585
attaciatu  siz.  122
bernusso  365
attaciu  siz.  

--- LKT.txt leaf 237
z.  878 1  fustagno  621 j  fustanella  621
i  gabbano  971
!  i?aftf//f/.  974
I  gabelloto  .siz.  974
I  f/ff/fa  siz.  sard.  994
i  p^a^To  1734
I  gaglioffo  659
I  ^a«/««  siz.  1006
j  ^rt?«  864
I  galanga  765
j  galante  864
galantnomo  864 '  gnliggi  siz.  799 I  828 j  galöfano  siz.  1085 i  galufn  dial.  659 j  gammara  siz.  1741 I  gancio  1056 1  gnnzirri  siz.  817 '  garheUara  673 j  garbellafura.  673 i  garbino  674 I  garbula  siz.  673 i  garifu  siz.  827 j  garitta  siz.  828 I  garofano  1085 i  garrusu  siz.  III I  gassina  siz.  836 I  gassira  siz.  8.36 I  gazzarra  700 [  gazzella  699 I  gazzettn  1059 i  gazzo  2205
gazzurrv  700 1  gebbia  siz.  630.  736 '  gellamina  1149 I  gelsomino  942 i  gengiovo  1930 j  (;er/"a  siz.  676 ;  ge^minu  942 I  p'esso  716
f/ÄeWo  1222
ghiazzerino  697
ghimberluccu  dial.  924
ghingano  722
^taco  929
giamberlucco  924
gianetto  2192
gianfutre  dial.  424
giannetta  2192 !  giannettu  siz.  2192
giannizzero  954
^riara  688
giarda  670
Italienisch.)
206
giarra  siz.  688 </iaurro  632 giberna  641 gilt  9öl ginnetfo  2192 ffiraffa  2234 gitibba  737 giub,-tta  737 giucca  dial.  739 giucco  dial.  siz.  739 gittdio  949 (7«tt/"a  dial.  739 giulebbe  742 giulebbo  742 giulecco  951 giuleppo  742 giunca  753 yiunco  753 yiuppa  737 ffiitppone  737 gnacchero  1546 gomena  750 granturco  2114c guajassa  siz.  171 guappa  dial.  1002 guingano  722 gumina  750 guttaperca  712
indaco  9  9 hüarsia(re)  1706 islamismo  915
Jamberluccii  dial.  924 jippimi  siz.  737
labarda  823 /rtc-c«  1295 /accÄe  2130 /a/ia  siz.  24 lambiccare  79 lambiccio  79 lanibicco  79 /an/"«  1535 laparderi  siz.  823 laparduni  siz.  823 /a^is  lazzuli  1311 larice  114 lazzaretto  1310 lazzarone  1310 lazzeruola  2ii06 lazzuli(lapis)  1311 Ze/ffli  siz.  1313 libeccio  1313 i?7ac  1319 Hmbiccio  79 limone  1322 limuni  siz.  1322 Usciardo  1581 K«rfo  2127 «M<o  2127 1329
inoaseMK  siz.  1362
macadaru  siz.  1353
macaluba  1376 ,  macalubi  siz.  1376 '  maciilucco  siz.  1357
maccabh  dial.  1375
maccit  siz.  1358
macra  dial.  1349
rnadd(i)H  siz.  1342 :  tuafjia  1355
majfioso  1855
»»a/5a  siz.  1355 I  mafiuftu  siz.  1355 j  magasenu  siz.  1362 i  magasinu  sard.  1362
magazzino  1362 :  maimone  1365 i  malase(nu)  siz.  1362 !  malco  di
```


## [2026-09-14T00:51:20.967Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB purdah\"; grep -n -i \"PURDAH\\|PURDA\\b\" HJB.txt | head -10; echo \"=== AID pardah\"; grep -n -i \"pardah\\|parda\\b\" AID.txt | head -10",
 "description": "Hobson-Jobson and Whitworth purdah"
}
```


### [2026-09-14T00:51:21.043Z] TOOL RESULT

```
=== HJB purdah
10500:G08HA,  adj.  Used  in  some  parts,  as an  Anglo-Indian  technicality,  to  indi- cate that  a  woman  was  secluded,  and  can- not appear  in  public.  It  is  short  for  P. gosha-nishmy  *  sitting  in  a  comer ' ;  and is  much  the  same  as  pcMrda-nishln  (see PURDAH).
12046:[1832.—"  Besides  the  purdahs,  the  open- ings between  the  pillars  nave  blinds  neatly made  of  bamboo  strips,  wove  together  with coloured  cords :  these  are  called  JhllbniaiB or  cheeks"  (see  CHICK,  a).— Ifw.  Meer Hassan  Ali,  Observations,  i  906.]
18284:1809.— "On  the  fourth  (side)  a  purdah was  stretched  acron."— Z^.  Vaientia,  i.  100.
18285:1810.— "If  the  disorder  be  obstinate,  the doctor  is  permitted  to  approach  the  purdah (i.e.  curtain,  or  screen)  and  to  put  tMe  ka^d through  a  small  aperture  ...  in  order  to feel  the  patient's  pmse." —  WilliamsoH,  V.  21. i.  130.
18287:1878. — "  Native  ladies  look  upon  the  coo- finement  behind  the  purdah  as  a  badge  of rank,  and  also  as  a  sign  of  chastity,  and are  exceedingly  proud  of  it."— A/;>  ij»  tke MofussiI,i.m.
18288:[1900.—"  Charitable  aid  is  needed  for  the purdah  women." — Pioneer  Mail ^  Jan.  21.]
=== AID pardah
2592:Goshanashin.  [Hindustani,  from  go- ska ,   a   corner,  and  nashin,  who  sits.] A   Muhammadan  ascetic.  The  term is  also  sometimes  used  for  parda- nashin.
5309:Pardah.  [Persian.]  A   veil,  a   screen, a   curtain,  especially  one  used  to  ex- clude women  from  public  view.
5310:Pardahnishin.  [Persian  njfhin ,   who sits.]  A   woman  who  observes  the practice  of  seclusion.
```


## [2026-09-14T00:51:36.239Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (155,156,157,158,159):\n    nums=re.findall(r'(?m)^\\s*(1[0-9][0-9])\\s*$', leaves[i])\n    print(i, nums[:5], leaves[i][:120].replace('\\n',' '))\n# find entry 228\nfor i,l in enumerate(leaves[:80]):\n    if re.search(r'228\\.\\s', l) or 'barda' in l:\n        print('--- leaf',i); print(l[:1500])\nEOF",
 "description": "LKT page numbers and entry 228"
}
```


### [2026-09-14T00:51:37.644Z] TOOL RESULT

```
155 ['128'] rs.  iiuhüd: 'Kichererbse,  Cicer  arietinum',  ebenso tk.  nohut;  hieraus  rum.  näut,  nähut, nohot  'dass.'. 1578.  
156 ['129'] -ütan,  also  wörtlich  'Waldmensch' [genau  dass.  wie  frz.  sauvage,  engl,  sa- vage  <^  lat.  silvaticus  sc.  hom
157 ['130'] arre,  belzuar;  engl,  be- zonr,  ndl.  bezoar  'Ziegenstein  im  Magen der  Wiederkäuer',  dtsch.£f2;oar'Gemsen- kugel
158 ['131'] k  'Baumwolle'  und  gr.  udiußaE, ■iraiißdKiov  'dass.';  hieraus  rum.  bumbac, buig.  bubak,  serb.  panmk  'Baumwoll
159 ['132'] b232. 1629.  Pers.  pärcäm: 'Haarlocke',  ebenso  tk.  periem  'Haar- locke auf  der  Stirne';  hieraus  bulg. percem,  
--- leaf 46
11/12.
220.  Syr.  Bar-abba:
N.  pr.  Nach  den  Evangelien  Mt  27  u. Mc  15  ein  jüdischer  Verbrecher,  den die  Juden  am  Passahfeste  an  Jesu  Stelle losbaten  [aus  syr.  bar  'Sohn'  und  abba 'Vater',  s.  hier  Nr.  1,  also  'Sohn  des Vaters';  dagegen  scheint  die  Deutung bar  rabbän  'Sohn  ihres  Herrn  oder  Leh- rers' kaum  wahrscheinlich];  gr.  Bapaß- ßa?,  lat.  Barabhas ;  hieraus  triest.  baraba 'Taugenichts',  genues.  barbau,  prov. barban,  barbau  'Schreckgespenst  für Kinder'.    [ML  940.
221.  Pers.  bärk:
'Blatt'  [Horn  NpEt  S.  47,  Nr.  203] ;  hier- aus über  die  kaukasischen  Sprachen russ.  burka  'runder,  kurzer  Filzmantel', wie  er  bei  den  Kosaken  und  Kaukasiern üblich  ist.    Poln.  burka.   [Gorjajew  34.
222.  Ar.  baraka:
'Segen  (nämlich  Gottes)',  ebenso  tk. bereket  'dass.,  Fruchtbarkeit';  hieraus rum.  berechet  'Fülle,  Fruchtbarkeit'; bulg.  bereket  'Überfluß',  serb.  bericet 'Glück,  Überfluß'.  [Sain  47.  Bern SlEtWb  49.
223.  Sskr.  baranda:
[Vielleicht  selbst  vom  pers.  bär-äniädä 'heraufgekommen,  d.  h.  mit  einem  Dach versehen'],  neuindisch  varanda  'ein  be- deckter, nach  vorne  offener  Vorraum, Altan';  hieraus  pg.  varanda,  sp.  baranda, harandilla,  kat.  barana,  frz.  veranda, it.  Veranda;  dtsch.  Veranda,  engl,  veran- dah  [jedoch  amerikanische  Schreibung Veranda  Herrigs  Archiv  CXLI.  195], schwed.  Veranda.  [Hobson-Jobson  964  u. 965.    ML  9151.
224.  Ar.  baras:
'We
--- leaf 47
ifa-Sandale,  Hausschuh'  [das  Wort ist  selbst  durch  romanische  Vermittelung aus  dem  Baskischen  zu  den  Arabern gekommen  ZDMG  LI,  311;  vgl.  sp. aharca,  mlat.  abärca  'Bauernschuli'] ; hieraus  mit  dem  ar.  Art.  pg.  alparca, murcianisch  alborga,  albolya  ;  aus  dem ar.  plr.  al-bargät  wurde  sp.  pg.  alpar- gata  'Spartoschuh'.  [ZfromPh  XXXII, 43.    ML  904.
244.  Pers.  barglr:
[Aus  pers.  bar  'Last'  Horn  NpEt  S.  36, Nr.  156  und  gtr  s.  hier  Nr.  158]  'Last- pferd'. Hieraus  bind,  und  daraus  anglo- ind.  bargeer  'Soldat  der  irregulären Kavallerie,  der  nicht  Eigentümer  seines Pferdes  und  seiner  Waffen  ist,  welche vielmehr  der  Regierung  gehören'.  — Im  vulg.  tk.  verderbt  zu  bejgir  oder begir  'Lastpferd',  hieraus  rum.  beghir 'Pferd'.    [Hobson-Jobson  69.
245.  Pers.  bäri:
'Wenigstens'  [aus  pers.  bär  'Mal'  Horn NpEt  S.  36,  Nr.  157  und  i  der  Einheit, also:  'ein  Mal'],  ebenso  tk.  barg  und bar  gm;  hieraus  rum.  barem,  barim  'we- nigstens', bulg.  serb.  bare  'wenigstens, dennoch'.  [Mikl  SlEtWb  7.  Bern  SlEt- Wb 44.
246.  Hiud.  bari-bibi:
[Aus  bind,  ban,  fem.  zu  barä  'groß', und  hlbl  'Frau,  Dame']  'große  Dame'; im  angloind.  ist  das  Wort  zur  Bezeich- nung der  Dame  geworden,  die  bei  einer Gesellschaft  den  Vorsitz  verlangt:  hirra- beebee.  [Hobson-Jobson
247.  Ar.  barkfik:
[Aus  dem  lat.  praecocium  'das  F'rühreife' über  gr.  rrpaiKÖKKiov,  irpaiKÖKia,  up
--- leaf 50
' [aus  gr.  rapixiov  mit  vorgesetztem altäg.  oder  kopt.  Art.  p;  ZDMG  L,  654]; hieraus  it.  bottarga,  siz.  buttaraca,  vut- taraca  'Kaviar  aus  den  Eiern  der  Meer- äsche', frz.  boutargue,  botargue,  pmitar- gue  'Speise  aus  Eiern  der  Seebarbe,  die gesalzen  und  an  der  Sonne  getrocknet oder  geräuchert  werden'.
275.  Tk.  batrak:
[Nicht  osm.,  sondern  tat.]  'Arbeiter': hieraus  russ.  batrak,  batraöka  'Arbeiter, Knecht;  Arbeiterin, Magd'.  [Gorjajew  13.
276.  Ar.  batta: Einheitsnomen  zu  baft  'Enten'  [aus  pers. bat  'Ente'  Horn  NpEt  S.  51,  Nr.  226] ; hieraus  sp.  pg.  pato,  pata  'Ente',  pg. patinho  'junge  Gans';  pg.  pato  'leicht zu  betrügender  Mensch'  [Constancio Dicc  752  b;  schon  npers.  här-bäf  'Idiot' Horn  a.  a.  0.].
277.  Ar.  bazaga:
'Sich  rühmen'.  Von  diesem  Stamme, vielleicht  von  einem  ar.  Adj.  *bazgän, kommt  siz.  baggianu  'eitel,  dünkelhaft' und  it.  albagia  'Eigendünkel',  Adj.  al- bagioso.    [GrSVociSic  228.
'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort
--- leaf 53
iea 'Märzveilchen'.  —  Ob  vom  pers.  Grund- wort russ.  wenisa  'Granate  (Stein)'  her- kommt, wie  Gorjajew  43  will,  scheint nicht  ganz  sicher,  wenn  auch  möglich.
311.  Tk.  bir:
'Eins',  birlik  'Einheit';  hieraus  rum. berlic  'As  beim  Kartenspiel'.  Wohl  auch russ.  birka  'Kerbstock'  [wohl  kaum  aus bir  iki  'eins,  zwei'  Gorjajew  17 ;  XXXVHI mit  ?].
312.  Ar.  birka:
'Teich';  hieraus  mit  ar.  Art.  sp.  alberca, pg.  alverca  'dass.'.    [DE  71.
313.  Pers.  birün:
Auch  berün  'außen,  heraus'  [Horn NpEt  S.  58,  Nr.  252] ;  hieraus  ein  Adj. mit  ar.  Endung  blrünl  'draußen  woh- nend', mit  ar.  Art.  al-blrünl  'der  Vor- städter'. Diesen  Beinamen  erhielt,  weil in  einer  Vorstadt  von  Huärizm  [s.  hier Nr.  890]  geboren,  der  berühmte  Poly- histor und  fruchtbare  Schriftsteller  Aba Raihän  Muhammad  ihn  Ahmad  al-Bi- runi,  ein  Zeitgenosse  Avicennas  [973  bis 1048,  vgl.  C.  Brockelmann,  Geschichte der  ar.  Literatur.  Leipzig  1901.  S.  166  u. 167,  wo  allerdings  die  überragende  Be- deutung des  Mannes  m.  E.  nicht  genü- gend gewürdigt  ist;  Alexander  Baum- gartner, Geschichte  der  Weltliteratur. Freiburg  1901.  I,  384].  Nach  der  an- sprechenden Vermutung  DEVICS  ist hieraus  frz.  alihoron  zur  Bezeichnung eines  fast  wunderbaren  Gelehrten  und Propheten,  einer  ganz  hervorragenden Persönlichkeit  geworden;  schließlich  er- hielt frz.  aliboron  die  Bedeutung  'Esel'. [Devic  DEt  20/22.
```


## [2026-09-14T00:51:47.888Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"barda\" LKT.txt | head -20; echo \"=== tail leaf158\"; python3 -c \"\ntxt=open('LKT.txt',encoding='utf-8',errors='replace').read(); l=txt.split('\\f')\nprint(l[158][-1500:])\"",
 "description": "LKT barda'a and leaf 158 tail"
}
```


### [2026-09-14T00:51:49.193Z] TOOL RESULT

```
733:228.  Ar.  barda'a:
734:[Nach  I.  I.  Hess  aus  pers.  pärdä  'Tep- pich' mit  infigiertem  'Ain  ZfSein  H,  221. Allerdings  kann  das  ar.  Wort  auch  tk. Ursprungs  sein,  da  wenigstens  im  Dia- lekte von  Adärbaigän  die  Satteldecke ähnlich  heißt:  burunduk  von  der  Wurzel bur,  bör  'verhüllen,  verdecken'  Vämbery TktEtWb  S.  211,  Nr.  228;  vgl.  ZDMG XXIII,  270]  'Satteldecke,  Sattelunterlage, Piicksaltel'.  Hieraus  viele  romanischen Formen  mit  manchem  Bedeutungs- wechsel: it.  barda  'Lederdecke  für  Brust, Hals  und  Flanken  des  Pferdes',  siz. tarda,  frz.  barde  'Reitkissen',  sp.  pg. barda  'Pferdeharnisch;  Hecke',  sp.  pg. albarda  'SaumsatteP;  sp.  bardo,  frz. 6ar(?eaM 'Dachschindel',  frz.  &arrfo< 'Maul- tier'.   [DE  66.   Devic  DEt  62.   ML  955.
735:229.  Ar.  bardag-:
736:'Erbeutete,  gefangene  Griechenmädchen, weiße  Sklavinnen'  [KREMER  in  SBKAW Wien  phil.  bist.  Gl.  CHI  (1883),  195/196; nach  VÖLLERS  in  ZDMG  L,  628  noch jetzt  im  Namen  Hös  Barda',  dem  Sklaven- hof von  Kairo,  erhalten] ;  sie  wurden meist  zu  unzüchtigen  Zwecken  gehalten, daher  it.  bardascia  'Knabe,  der  zur  Un- zucht gebraucht  wird,  Lotterbube'  [aber logud.  mail.  piem.  'Knabe'  schlechthin], afrz.  hardaclie,  sp.  bardaja,  bardaje 'Schandbube'.    [Eguilaz  340.    ML  956.
737:230.  Tk.  bardak:
738:'Glas,  Becher':  hieraus  rum.  bardac, bardacä  'Krug,  Tintengefäß',  Ableitung bärdäcufä.  Bulg.  serb.  bardak  'dass.'. [Mikl  SlEtWb  7.    Bern  SlEtWb  44.
1992:'Lanze',  aber  auch  die  'eiserne  Lanzen- spitze' an  der  etwa  4  m  langen  Be- duinenlanze mizrak  [s.  hier  Nr.  1476; vgl.  FISCHER  in  MSOS  II,  233];  hier- aus mit  ar.  Art.  it.  labarda,  alabarda, frz.  hallebarde,  sp.  pg.  alabardo  'Helle- barde', pg.  hallabarda,  mhd.  mit  Volks- etymologie helmbarte.  Dazu  siz.  lapar- deri  'Gauner,  Erpresser,  Betrüger',  la- parduni  'Drohne'  [man  war  der  Mei- nung, die  Hellebardiere  lebten  vom  er- preßten Gute  anderer].  Mit  vorgesetztem mu  des  Partizips  ergibt  sich  ar.  *muharba, hieraus  sp.  moharra  'Lanzenspitze'. Über  das  Tk.  wurde  rum.  arbiu  'Lade- stock'.   [DE  316     ML  4040.
3728:'Vorhang',  tk.  ebenso  perde;  hieraus bulg.  perde  'Schleier;  Geländer',  serb. perde  'Bettvorhang';  lum.  perdea  'Vor- hang, Gardine',  perdelufä.  Hieraus wurde  auch  ar.  barda'a,  s.  hier  Nr.  228. [Löbel  EITAP  75.    Mikl  SlEtWb  241  b.
5139:bardag  229
6352:baragouin  256 I  barbacane  197 I  bardache  afz.  229 ]  barde(au)  228 i  ftarc^of  228 ,  baroque  364 I  barque  2148 i  barracan  250 I  basane(r)  afz.  316 ^  basane  316 I  basanier  316 !  basiUqtie  (vemej  262
6880:(ilabarda  82'i
6990:barda  22^
6993:barda<cia  229
7097:labarda  823 /rtc-c«  1295 /accÄe  2130 /a/ia  siz.  24 lambiccare  79 lambiccio  79 lanibicco  79 /an/"«  1535 laparderi  siz.  823 laparduni  siz.  823 /a^is  lazzuli  1311 larice  114 lazzaretto  1310 lazzarone  1310 lazzeruola  2ii06 lazzuli(lapis)  1311 Ze/ffli  siz.  1313 libeccio  1313 i?7ac  1319 Hmbiccio  79 limone  1322 limuni  siz.  1322 Usciardo  1581 K«rfo  2127 «M<o  2127 1329
7915:alabarda  823
7960:albarda  228
8237:hallabarda  823
8690:baba(cä)  146 babaie  146 babalic  146 fca6a|(  201 i^acaZ  189 baclava  191 fcacpg  178 fca^ra  168 bageacä  167 ftaÄmei  128 bairac(dar)  182 bairani  183 bajacä  167 balama(le)  173 balamut  199 6«?6rtj  201 balcäz  203 balctz  203 feaZcon  197 bttlgiü  201 bali(e)mez  201 baisam  293 bam(b)ä  210 bamie  210 bananä  211 baraban(ä)  1607 bardac(ä)  230 barem  245 barim  245 iasar  278 6«se«  280 basma  264 tejCcU  260 ha^ca  263 bapbnzuc  266 öff^/w  260 öazar  278
9796:arfor  501 adraja  485 aduana  526 aduar  502 adufa  538 adufe  537 agengibre  1930 oguajaque  2168 aguanafa  1535 ahorrar  886 ajarafe  1840 «;e&e  1735 ajedrea  1872 ajedrez(atama)  1871 ajimenez  1815 ajimiz  1816 ajonjoU  744 ajorca  1951 ajovar  1959 ajuar  1959 alabarda  823 alabega  761 alacena  871 alacran  4:1 alafia  24 alahilca  904 alamar  67 alambar  78 alambique  79 alambre  78 alameda  1364 alamud  72 alancel  1428 alaqueca  45 alarbe  89 alarde  94 aZaWf^o  59  d.  100 I  alarife  99 alatar  134 alazan(o)  870 albacea  2158 albaheca  761 «Zöate  226 albanilear  216 albanal  204 nlbanar  204 albani(r)  216 albanil(esco)  216 alhaqida  188 albaran  226 albarazo  224 ffife«r(/a  228 albardän  241 a/fcarrfi  dial.  242 albardin  242 albaricoque  247 albarrada  249 albarrän  251 albarrana  251 albarraz  762 albayaldar  6 albayalde  6
10036:babuche  1625 iadrt  152 badana  316 badea  319 badian(a)  162 bagasa  171 daA«H  177 baladi  196 balaja  151 balajo  151 6aZc(5n  197 fcflWa  271 (de,en)  balde  271 baldequhi  170 fea/rfio  271 balsamo  293 bambu  209 banana  211 bandujo  273 bandullo  273 bango  213 barahunda  256 baraja(do)  225 barajar  225 baranda  223 barbacana  197 fcarca  2148 fcarrfa  228 bar da ja  229 bardaje  229 ftarrfo  228 barragän  250 barroco  364 6a<a  273
=== tail leaf158
che, (dial.  Schlesien)  Paputschen.  [DE  231, Eguilaz  328.  ML  858  und  6216  (gehören natürlich  zusammen).    GrSVociSic  227.
1626.  Pers.  pärä:
'Stück,  Teil'  [Horn  Np  EtS.  62,  Nr.  271], ebenso  tk.  para  'Stück,  Geldstück,  '/^<> tk.  Piaster';  hieraus  bulg.  para  'der Para',  serb.  pari  'Geld',  besparicen  'un- entgeltlich'; rum.  para  'Geldstück,  Para'; vom  Adj.  paralij  'reich'  kommt  rum. paraleü  'reich'  [Gi^ä  POP  hat  in  seinem Wörterbuch  S.  325  paraleü  'mächtiger Löwe'];  A&m.pärälu^ä  'Gänseblümchen'. [Löbel  EITAP  74,    Mikl  SIEtWb  232.
1627.  Tain,  panai:
'Große  Trommel',  die  bei  gewissen  Fest- lichkeiten geschlagen  wird ,  die  erblichen Trommelschläger  heißen  pasaiyan.  plr, paRaiijar  'Trommler'.  Hieraus  ist  anglo- ind. parriar,  pariah  zur  Bezeichnung einer  niederen  Hindukaste  in  Südindien geworden,  die  stellenweise  die  zahl- reichste Bevölkerung  ausmacht.  Jetzt ist  das  Wort  in  den  europäischen Sprachen  mit  'ausgestoßen,  verachtet*^ synonym  geworden:  engl,  pariah,  frz. paria,  dtsch.  Paria.  —  [Die  Seiler  DKiL IV,  371  angegebene  Erklärung  tarn. rajan,  bind,  paharija  'Gebirgsbewohner' gibt  also  erst  die  sekundäre  Bedeutung wieder.]    [Hobson  Jobson  678/680.
1628.  Pers.  pärcä:
'Stückchen'  [von  pärä,  s.  hier  Nr.  1626], tk.  ebenso  paria;  hieraus  bulg.  parca,
131
[Fers.  päiSäm.
russ.  paria  'Brokat,  Stoß',  serb.  paröe 'Stück'.  [Gorjajew  249.  MiklSlEtW
```


## [2026-09-14T00:52:00.603Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD pela\"; grep -n -i \"^pel.-2\\|pel.-2\\.\\|plat-\\|pletə\\|plāno\" AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins roots"
}
```


### [2026-09-14T00:52:00.653Z] TOOL RESULT

```
=== AHD pela
198:kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds.
829:pela-2
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
848:plat-
858:plak-'. Also plak-. To be flat. Extension of pele-2. 1. Germanic *fléh6 in Old Norse fl6, layer, coating: FLOE. 2. Variant form *pldg- in: a. Germanic *flék- in Old English fléc, flatfish: FLUKE!; b. Germanic *flakaz in Norwegian flak, flat piece, flake, probably akin to the Scandinavian source of Middle English flake, flake: FLAKE}; c. Germanic *flak- in Old Norse flaki, fleki, hurdle: FLAKE?. 3. Extended form *plakd in Germanic *flag6 in Old Norse flaga, layer of stone: FLAG, FLAW}. 4. Possibly suffixed (stative) form *plak-é-, to be calm (as of the flat sea), in Latin placére, to please, be agreeable: PLACEBO, PLACID, PLEA, (PLEAD), PLEASANT, PLEASE; COMPLACENT. 5. Lengthened suffixed form *plak-G- in Latin placdre, to calm (causative of placére): PLACABLE, PLACATE. 6. Nasalized form *pla-n-k- in Latin plancus, flat, flat-footed, whence planca, board: PLANCHET, PLANK, PLANK-SHEER. 7. Variant form *plag- in: a. perhaps Latin plaga, net (? < “something ex- tended”): PLAGIARY; b. Greek plagos, side: PLAGAL, PLAGIO-, PLAYA. 8. Root form *plak- in Greek plax, flat, flat land, surface: PLACENTA, PLACOID. 9. Variant form *pelag- in Greek pelagos, sea: PELAGIC; ARCHIPELAGO. [Pok. 1. pla-k- 831.]
860:plat-. To spread. Extension of pele-?. 1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: rLAT!; b. Old French flater, to flatter: FLATTER!. 2. Suffixed variant form *plad-yo- in Germanic *flatjam in Old English flei(t), floor, dwelling: FLAT?. 3. Basic form *plat- in Germanic *flathd(n), flat cake, in Late Latin
862:flad6, flat cake, pancake: FLAN. 4. Germanic nasalized suffixed form *flu-n-th-r-j6- in Old Swedish flundra, flatfish, flounder, probably akin to the Scandinavian source of Middle English flounder, flounder: FLOUNDER?. 5. Nasalized form *pla-n-t- in Latin planta, sole of the foot, and denominative plantdre, to drive in with the sole of the foot, plant, whence planta, a plant: CLAN, PLAN, PLANT, PLANTAIN!, PLANTAR; PLANTIGRADE, SUPPLANT. 6. Suffixed form “plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE‘, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY?), PLATY-, (PLAZA). [Pok. plat- 833.] [plegan. To pledge for, stake, risk, exercise oneself. West Germanic verb. 1. Old English plegian, to exercise one- self, play: PLAY. 2. Late Latin plevium (> Old French plevir, to pledge), pledge, guarantee: PLEDGE; REPLEVIN. 3. Germanic derivative noun *plehti- in Old English pliht, danger, peril: PLIGHT?.] plek-. To plait. Extension of pel-*. 1. Suffixed o-grade form *plok-so- in Germanic *flahsam, flax, in Old Eng- lish fleax, flax: FLAX. 2. Full-grade form *plek- in Latin -plex, -fold (in compounds such as duplex, twofold; and supplex, “with legs folded under one,” kneeling, entreat- ing; see dwo-, upo): MULTIPLEX, QUINTUPLE, SUPPLE. 3. Latin plicdre, to fold (also in compounds used as denominatives of words in -plex, genitive -plicis): PLAIT, PLIANT, PLICA, PLICATE, PLIGHT!, PLISSE, PLY!; APPLY, COMPLICATE, COMPLICE, DEPLOY, DISPLAY, EMPLOY, EXPLICATE, IMPLICATE, REPLICATE, SUPPLICATE. 4. Suf- fixed forms “plek-to- and *plek-t-to- in Latin plectere (past participle plexus), to weave, plait, entwine: PLEACH, PLEXUS; AMPLEXICAUL, COMPLECT, (COMPLEX), PERPLEX. 5. Greek plekein, to plait, twine, and plektos, twisted: PLECOPTERAN, PLECTOGNATH. [Pok. plek- 834.] plék-. Also pleik-. To tear. 1. Zero-grade form *pbk- becoming *plak- in Germanic *flahan in Old English fléan, to strip the skin from: FLAY. 2. Suffixed o-grade form “ploik-sk- perhaps in Germanic “flaiskjan, piece of flesh torn off, in Old English flésc, flesh: FLESH. 3. Zero-grade form *plik- in Germanic *flikkja in: a. Old English flicce, side of a hog: FLITCH; b. Germanic ablaut form *flekkja in Old Norse flekkr, piece of skin or flesh, spot, stain: FLECK. [Pok. plék- 835.] pleu-. To flow. I. Basic form “pleu-. 1. Latin pluere, to rain: (PLOVER), (PLUVIAL), PLUVIOUS. 2. Greek pleusis, sailing: PLEUSTON. 3. Suffixed zero-grade form *plu-elos dissimilated into Greek puelos, trough, basin: PYELITIS. 4. Suffixed form *pl/(e)u-mon-, ‘‘floater,” lung(s), in: a. Latin pulmé (< *plumonés), lung(s): PULMONARY; b. Greek pleumén, pneumon, lung: PNEUMONIA, PNEU- MONIC. 5. Suffixed o-grade form *plou-to- in Greek plou- tos, wealth, riches (< ‘‘overflowing’’): PLUTO; PLUTOCRACY. 6. Lengthened o-grade form *pl6(u)- in: a. Germanic *fléwan, to flow, in (i) Old English flowan, to flow: FLOW (ii) perhaps Middle Dutch vluwe, fishnet: FLUE?; b. suffixed form *pld-tu- in Germanic *fléduz, flowing water, deluge, in Old English fléd, flood: FLOOD. II. Extended form *pleuk-. 1. Germanic *fleugan, to fly, in Old English fléogan, to fly: FLY!. 2. Germanic *fleu- gon-, flying insect, fly, in Old English fléoge, a fly: FLY?. 3. Probably Germanic *fleuhan, to run away, in Old English fléon, to flee: FLEE. 4. Germanic causative *flauhjan in Old English flygan, flégan, to put to flight: FLEY. 5. Germanic suffixed form *fleug-ika in Old French fleche, arrow: FLECHE, FLETCHER. 6. Zero-grade form *pluk- in: a. Germanic *flugja-, feather, in Old English -flycge, with feathers (only in unfligge, featherless): FLEDGE; b. suffixed form *flug-ti- in Old English flyht, act of flying, and *flyht, act of fleeing, escape: FLIGHT, FLIGHT?; Cc. possibly (but unlikely) suffixed form *flug- laz, dissimilated into *fuglaz, bird, in Old English fugol, bird: FowL; d. Germanic suffixed form *flug-ila in Mid- dle High German viiigel (> Germanic Fliigel), wing: FLUGELHORN, FUGLEMAN. III. Extended form *pleud-.
1370:CLAN plat- CLANDESTINE kel-2 CLANG kleg- CLASMATOCYTE kel-1 cLass kele-2 CLAST kel-1 CLasTIC kel-1 CLATHRATE kleu-3 CLATTER gal-2 CLAUSE kleu-3 CLAVATE kleu-3 CLAVICHORD kleu-3 CLAVICLE kleu-3 CLAVICORN ker-1, kleu-3 CLAVIER kleu-3 CLAVIFORM kleu-3 CLAW gel-1
1516:FIx dhigw- FIXATE dhig¥- FIXITY dhigw- FIXTURE dhigw- FIZGIG peis-2 FIZZLE pezd- FJELD pelis- FJORD per-2 FLABELLUM bhié-2 FLAG! = plak-1 FLAGELLATE bhiag- FLAGELLUM _bhiag- FLAGITIOUS bhlag- FLAGRANT bhel-1 FLAIL  bhlag- FLAIR bhrag- FLAKE! plak-1 FLAKE? plak-1 FLAMBE bhel-1 FLAMBEAU bhel-1 FLAMBOYANT bhel-1 FLAME bhel-1 FLAMEN bhilad- FLAMINGO bhel-1 FLAMMABLE bhel-1 FLAN plat- FLANEUR pele-2 FLANK kleng- FLANNEL wele-1 FLAP plab-
1517:FLAT!  plat- FLAT? plat- FLATTER! plat- FLATUS bhié-2 FLAVESCENT bhel-1 FLAVIN bhel-1 FLAVO- bhel-1 FLAVONE bhel-1 FLAVOPROTEIN bhel-1 FLAVOR bhié-2
1521:FLORAL bhel-3 FLORIATED bhel-3 FLORID bhel-3 FLORIGEN bhel-3 FLORIN  bhel-3 FLORIST bhel-3 -FLOROUS  bhel-3 FLOSCULUS bhel-3 FLOTILLA pleu- FLOTSAM pleu- FLOUNCE! sker-3 FLOUNDER? plat- FLOUR bhel-3 FLOURISH bhel-3 FLOW pleu- FLOWER bhel-3 FLUCTUATE _bhleu- FLUENT bhieu- FLUERIC bhleu- FLUE? pleu- FLUGELHORN ker-1, pleu- FLUID bhleu- FLUKE! plak-1 FLUME bhlieu- FLUOR bhlieu- FLUORIDE bhleu- FLUORO- bhieu- FLUSH? bhleu- FLUSTER pleu- FLUTTER pleu- FLUVIAL bhleu- FLUVIOMARINE bhieu- FLUX bhieu- FLY! pleu-
2087:PHYLACTERY phulax PHYLAXIS phulax PHYLE bheue- PHYLETIC bheue- -PHYLL bhel-3 PHYLLO- bhel-3 PHYLLOCLADE kel-1 -PHYLLOUS bhel-3 PHYLLOXERA ksero- PHYLOGENY bheua- PHYLUM bheue- PHYSIC bheue- PHYSIO- bheue- PHYSIOGNOMY gn6- PHYSIQUE bheue-_ PHYSOSTIGMINE pu-1 PHYSOSTOMOUS_ pu-! -PHYTE bheue- PHYTO- bheue- PHYTON bheue- PIACULAR pius PIANO? pele-2 PIANOFORTE bhergh-2 PIAZZA plat- PIBROCH pipp- PICA2 (s)peik- PICARO (s)peik- PICE ped-1 PICEOUS_ pik- PICKET (s)peik- PICOLINE pik- PICRO- peig-1 PICTOGRAPH peig-1 PICTOR peig-! PICTURE peig-1 PICTURESQUE peig-', (s)peik- PIE? (s)peik-
2099:PIU pele-1 PLACABLE plak-! PLACATE plak-1 PLACE plat- PLACEBO pilak-1 PLACENTA plak-1 PLACID plak-1 PLACOID plak-1 PLAGAL plak-1 PLAGIARY plak-1 PLAGIO- plak-1 PLAGIOCLASE kel-1 PLAGUE plak-2 PLAICE plat- PLAIN pela-? PLAINT plak-2 PLAIT plek-
2100:PLAN plat- PLANARIAN pele-2 PLANCHET plak-1 PLANE! pele-2 PLANE? pelo-2 PLANES pele-2 PLANE‘ plat- PLANET pele-2 PLANE TREE plat- PLANGENT plak-2 PLANISH pele-2 PLANK plak-1 PLANK-SHEER plak-1 PLANKTON plak-2 PLANO- pelo-2 PLANT plat- PLANTAIN! plat- PLANTAR plat- PLANTIGRADE ghredh-, plat- PLANULA pele-2 -PLASIA pele-2 PLASMA pele-2 PLASMODESMA dé- -PLAST pele-2 PLASTER pele-2 PLASTIC pele-2 PLASTID pele-2 -PLASTY pele-2 PLATE plat- PLATEAU plat- PLATITUDE plat- PLATTDEUTSCH teuta- PLATY2 plat- PLATY- plat- PLATYHELMINTH wel-3 PLATYPUS ped-1 PLAY plegan PLAYA plak-1 PLAZA plat-
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
```


## [2026-09-14T00:52:02.134Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN purdah\"; grep -n \"^purdah\\|purdah,\" KLN_1966.txt KLN_1971.txt | head; echo \"=== KLN plat\"; grep -n \"^plat-\\|^platy\\|^plate,\" KLN_1966.txt | head",
 "description": "Klein purdah, plate"
}
```


### [2026-09-14T00:52:02.202Z] TOOL RESULT

```
=== KLN purdah
KLN_1971.txt:196057:purdah, n., curtain guarding women from public 
KLN_1966.txt:31049:purdah,  n.,  curtain  guarding  women  from  public view  in  India.  —  Hind,  and  Pers.  pardah,  ‘veil’, pure,  adj.  —  ME. pur, pure,  fr.  OF.  (=  F.)  pur,  fr. L.  purus,  ‘pure,  clean’,  which  is  rel.  to  putus , ‘clear,  pure', putare,  'to  cleanse, clean’,  and  cogn. with  OI.  pdvate,  punati,  ‘purifies,  cleanses’, putah ,  ‘pure’,  putih,  ‘purification’,  pavitar-,  ‘pu¬ rifier’,  MIr.  «r,  ‘fresh,  new’,  OHG.  fowen,  ‘to sift’.  See  putative  and  cp.  purblind,  puree,  pur¬ gatory,  purge,  purify,  depurate,  expurgate.  Cp. also  pious  and  words  there  referred  to. Derivatives:  pure,  adv.,  pure-,  pref.  meaning ‘purely’,  pure-ness,  n.
=== KLN plat
29103:platypus,  n.,  the  duckbill.  —  Lit.  ‘flatfooted’,  fr. platy-  and  Gk.  7E065,  gen.  710865,  ‘foot’.  See
29105:platyrrhine,  adj.,  having  a  broad  nose.  —  Com¬ pounded  of  platy-  and  Gk.  pti,  gen.  ptv6?, ‘nose’.  See  rhino-.
29106:platysma,  n.,  a  broad  muscle  on  each  side  of  the neck  ( anat .)  —  Medical  L.,  fr.  Gk.  7tXaTU<J[xa, ‘a  flat  object;  widening,  dilation’,  fr.  ieXcct-ji;, ‘flat,  wide,  broad’;  see  platy-  and  -ma.  In  its anatomical  sense  the  word  platysma  was  intro¬ duced  by  Oribasius,  physician  of  Emperor Julian.
```


## [2026-09-14T00:52:19.620Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\n# locate purdah leaf\nfor i,l in enumerate(leaves):\n    if re.search(r'purdah,\\s+n\\.,\\s+curtain', l):\n        print('purdah leaf', i, 'est page', i*2-24, i*2-23)\n    if re.search(r'^platy-', l, re.M):\n        print('platy- leaf', i)\n        m=re.search(r'platy-.{0,900}', l, re.S)\n        print(m.group(0))\nEOF",
 "description": "Klein leaves for purdah and platy-"
}
```


### [2026-09-14T00:52:20.740Z] TOOL RESULT

```
purdah leaf 678 est page 1332 1333
```


## [2026-09-14T00:52:21.044Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '825,835p' AHD_watkins1985.txt | cut -c1-3000; echo \"=== FIELD index\"; grep -n \"FIELD \" AHD_watkins1985.txt | head -3",
 "description": "AHD pele-2 full entry"
}
```


### [2026-09-14T00:52:21.106Z] TOOL RESULT

```
peig-?. Also peik-. Evil-minded, hostile. 1. Suffixed zero-grade form *pig-olo- in Germanic *fikala- in Old
English ficol, treacherous, false: FICKLE. 2. Suffixed o-grade form *poik-os in Germanic *gafaihaz (*ga-, collective prefix; see kom), in Old English gefah, enemy: FOE. 3. Suffixed o-grade form *poik-yos in Germanic *faigjaz in Old English fege, fated to die: FEY. 4. Suf-
peis-'
fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. zero-grade. form *pkt-en- in Greek kteis (genitive ktenos < *pktenos), a comb: CTENIDIUM; CTENOID, CTENOPHORE. [Pok. 2. pek- 797.] peku-. Wealth, movable property. 1. Germanic *fehu- in: a. Old Norse fé, property, cattle: FELLOW; b. Old French fie, fief: FEE; c. Medieval Latin feudum, feudal estate: FEUD?; INFEUDATION. 2. Suffixed form “peku-n- in Latin peciinia, property, wealth: PECUNIARY; IMPECUNIOUS. 3. Suffixed form *peku-l- in Latin peciilium, riches in cattle, private property: PECULATE, PECULIAR. [In Pok. 2. pek- 797.] pekv-. To cook, ripen. 1. Assimilated form (in Italic and Celtic) *kvekw- in Latin coquere, to cook: COOK, CUISINE, (CULINARY), KILN, KITCHEN, QUITTOR; APRICOT, BISCUIT, CONCOCT, DECOCT, PRECOCIOUS, RICOTTA. 2. Greek pe- pon, ripe: PEPO. 3. Greek peptein, to cook, ripen, digest (> peptos, cooked): PEPTIC; DRUPE, EUPEPTIC, PEPSIN, PEPTONE, PUMPKIN. 4. Greek -pepsia, digestion: DYSPEP- sia. 5. Sanskrit pakva-, ripe: PUKKA. [Pok. peky- 798.] pel-1. Dust, flour. 1. Latin pollen, fine flour, dust: PoL- LEN. 2. Latin pulvis, dust: POWDER, PULVERIZE. 3. Latin palea, chaff: PAILLASSE, PALEA. 4. Greek palunein, to sprinkle flour: PALYNOLOGY. 5. Greek poltos, porridge (made from flour), probably borrowed via Etruscan into Latin as puls, pottage: POULTICE, PULSE?. [Pok. 2 b. pel- 802.] pel-2. Pale. 1. Suffixed variant form *pal-wo- in: a. Ger- manic *falwaz in Old English fealu, fealo, reddish yellow: FALLOW DEER; b. Latin pallére, to be pale: PALE, PAL- LID, PALLOR; APPALL; C. Latin palumbés (influenced in form by Latin columbus, dove), ringdove, “gray bird”: PALOMINO. 2. Suffi
pela-2
d. Germanic combining form *-falthaz, *-faldaz in Old English -feald, -fald, -fold: -roLD. 2. Combining form *.plo- in: a. Latin -plus, -fold (as in triplus, threefold): DECUPLE, MULTIPLE, OCTUPLE, QUADRUPLE, SEPTUPLE, (SEXTUPLE), TRIPLE; TRIPLOBLASTIC; b. Greek -plos, -ploos, -fold (as in haploos, haplous, single): -PLOID; (DIPLOID), HAPLOID. [Pok. 3. a. pel- 802.]
pel-4. Skin, hide. 1. Suffixed form *pel-no- in Germanic *felnam in Old English fell, skin, hide: FELL, 2. Ger- manic suffixed form *fel-men- in Old English filmen, membrane: FILM. 3. Suffixed form *pel-ni- in Latin pellis, skin: PELISSE, PELLICLE, (PELT!), PELTRY, PIL- LION; PELLAGRA, SURPLICE. 4. Greek -pelas, skin: ERY- SIPELAS. 5. Suffixed form *pel-to- in Greek pelté, a shield (made of hide): PELTATE. [Pok. 3 b. pel- 803.]
pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *
pela-*
*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old 
49
=== FIELD index
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
```


## [2026-09-14T00:52:33.260Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (677,678,679):\n    nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', leaves[i])\n    print(i, nums[:6], leaves[i][:100].replace('\\n',' '))\n# find platy-/plate entries and their leaf\nfor i,l in enumerate(leaves):\n    if re.search(r'plate,\\s+n\\.', l) or re.search(r'platy-,\\s', l):\n        nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', l)\n        print('PLATE/PLATY leaf',i,nums[:6])\nEOF",
 "description": "Klein page numbers"
}
```


### [2026-09-14T00:52:34.410Z] TOOL RESULT

```
677 [] ‘to  swim,  float’,  for  which  see flow  and  pluvial.  Pulmones,  etc.,  orig.  meant  ‘the float
678 ['1273']   attentive  to  punctilios.  —  Form¬ ed  fr.  prec.  word  on  analogy  of  It.  puntiglioso, Sp. 
679 ['1274', '1275'] eansing,  puri¬ fying’,  fr.  purgatus,  pp.  of  piirgdre.  See  purge  and -ation. purgative,  adj
PLATE/PLATY leaf 579 ['1082', '1083']
PLATE/PLATY leaf 636 []
PLATE/PLATY leaf 638 []
PLATE/PLATY leaf 639 ['1198', '1199']
PLATE/PLATY leaf 895 ['1691']
```


## [2026-09-14T00:52:41.083Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (635,636,637):\n    print('=== leaf',i)\n    print(leaves[i][:3500])\nEOF",
 "description": "Klein leaves near p.1192"
}
```


### [2026-09-14T00:52:42.221Z] TOOL RESULT

```
=== leaf 635
’,  and  F.  girouette, ‘weathercock’.
pirouette,  intr.  v.,  to  whirl  about  on  tiptoe.  —  F. pirouetter,  fr.  pirouette.  See  pirouette,  n. Derivatives:  pirouett-er,  ti.,  pirouett-ist,  n. pirssonite,  n.,  a  hydrous  calcium  sodium  carbon¬ ate  (mineral.)  —  Named  after  the  American geologist  Louis  Valentine  Pirsson  (1860-1919). For  the  ending  see  subst.  suff.  -ite. pis  aller,  last  resource.  —  F.,  lit.  ‘to  go  worse’,  fr. pis,  ‘worse’  (fr.  L.  pejus,  neut.  of  pejor,  ‘worse’), and  alter,  ‘to  go'.  See  pejorative  and  alley, pisanite,  n.,  a  hydrous  iron  copper  sulfate  (min¬ eral.)  —  Named  after  the  French  chemist  and mineralogist  F61ix  Pisani  (1831-1920),  who  ana¬ lyzed  it.  For  the  ending  see  subst.  suff.  -ite. piscary,  n.,  the  right  of  fishing  (law).  —  ML. pisedria,  prop.  neut.  pi.  of  the  L.  adj.  piscarius, ‘pertaining  to  fishing’,  fr.  piscis,  ‘fish’.  See Pisces  and  adj.  suff.  -ary.
piscatology
1190
piscatology,  n.,  the  science  of  fishing.  A  hybrid
coined  fr.  L.  piscatus,  pp.  of  piscari,  ‘to  fish’,  fr. piscis,  ‘fish’,  and  Gk.  -Xoyla,  fr.  -Xoyo?,  ‘one who  speaks  (in  a  certain  manner) ;  one  w ho  deals (with  a  certain  topic)’.  See  Pisces  and  -logy, piscator,  n.,  a  fisherman.  —  L.  piscator ,  fr.  pisca- tus,  pp.  of  piscari,  ‘to  fish’.  See  next  word, piscatory,  adj.,  pertaining  to  fishing.  —  L.  pisca- torius,  ‘of  fishermen’,  fr.  piscator,  ‘fisherman’, fr.  piscatus,  pp.  of  piscari,  ‘to  fish’,  fr.  piscis, ‘fish’.  See  next  word  and  adj.  suflf.  -ory. Derivatives:  piscatory,  n .,  piscatori-al,  adj.
Pisces,  n.  pi.,  the  twelfth  sign  of  the  zodiac.  —  L., pi.  of  piscis,  ‘fish’,  cogn.  with  Goth  .fisks,  OHG., OE.  fisc,  ‘fish’.  See  fish,  ‘an  aquatic  animal’,  and cp.  words  there  referred  to. pisci-,  combining  form  meaning  fish.  —  L.  pisci-, fr.  piscis,  ‘fish’.  See  prec.  word, pisciculture,  n.,  fish  culture.  —  Compounded  of pisci-  and  L.  cultura,  ‘culture’.  See  culture. Derivatives: piscicultur-al,  adj ., piscicultur-al-ly, adv.,  piscicultur-ist,  n.
piscina,  n.,  1)  fish  pond ;  2)  stone  basin  in  the  wall of  a  church.  —  L.  piscina,  ‘fishpond,  pond  for bathing,  cistern,  tank,  reservoir’,  fr.  piscis,  ‘fish’. See  Pisces  and  -ine  (representing  L.  -ina). Derivative:  piscin-al,  adj. piscine,  n.,  bathing  pool.  —  See  prec.  word, piscine,  adj.,  pertaining  to  fish.  —  Formed  with suff.  -ine  (representing  L.  -inns)  fr.  L.  piscis,  ‘fish  . See  Pisces.
piscivorous,  adj.,  fish-eating.  —  Compounded  of pisci-  and  L.  -vorus,  ‘devouring’.  See  -vorous. pise,  n.,  puddled  clay.  —  F.,  pp.  of  piser,  ‘to pound’,  fr.  L.  pinsere ,  ‘to  beat,  pound,  crush', whence  pistillum ,  ‘pestle’.  See  pestle.
Pisgah,  n.,  name  of  a  mountain  in  Moab,  from which  Moses  saw  the  Promised  Land.  —  Heb. Pisgdh,  lit.  ‘cleft’.  Cp.  the  phrase  Pisgah  sight  (in allusion  to  Deut  3  :  27). pish,  interj.,  v.  and  n.  —  Imitative, pishogue,  n.,  witchcraft,  sorcery.  —  Ir.  piseug, ‘sorcery’.
pish-pash,  n.,  rice  soup  containing  small  pieces  of meat  ( Anglo-Ind .)  — -  Pers.  pish-pash,  ‘broken  to pieces’,  fr.  pashidan,  ‘to  break  to  pieces’. Pisidium,  n.,  a  genus  of  freshwater  bivalves  (zool.) —  ModL..  dimin.  of  L.  pisum,  ‘pea’.
=== leaf 636
e  earthen  winejar  (Greek  archeol.) —  Gk.  nt&oq,  which  is  dissimilated  fr.  *<pl&op and  is  cogn.  with  L.  fidetia,  ‘clay  vessel’  (orig. ‘anything  tied  up  together’),  fiscus,  ‘woven  bas¬ ket,  purse;  treasury’.  See  fisc, pitiable,  adj.  —  ME.  piteable,  fr.  OF.  piteable  (F. pitovahle),  fr.  pile  (F.  pitie).  See  pity  and  -able. Derivatives:  pitiable-ness,  n.,  pitiabl-y,  adv. piton,  n.,  a  peak.  —  F.,  ‘peak  of  a  mountain; eyebolt’.  Cp.  Sp.  piton,  ‘protuberance,  promi¬ nence’.
pittacal,  n.,  eupittonic  acid  ( chem .)  —  G .  Pittacal, Pittakal,  coined  by  the  German  natural  philos¬ opher  and  industrialist  Baron  Karl  von  Reichen- bach  (1788-1869)  in  1835  fr.  Gk.  nixxa,  rJ.aax, ‘pitch’,  and  xxXoc,  ‘beautiful’.  The  first  element is  cogn.  with  L.  pix,  gen.  picis,  ‘pitch’ ;  see  pitch, ‘resinous  substance’.  For  the  second  element  see calo-,  for  the  ending  see  adj.  suff.  -al. pittance,  n.,  a  dole.  —  ME.  pitance,  fr.  OF.  pi- tance,  ‘pity’  (whence  F.  pitance,  ‘allowance  of food,  pious  dole’),  formed,  with  change  of suffix,  fr.  OF.  pitie  (F.  pitie).  See  piety,  pity,  and -ance.
pittite,  n.,  an  auditor  in  the  pit  of  a  theater  (col- loq.)  —  Formed  fr.  pit  with  subst.  suff.  -ite. pituitary,  adj.,  1)  pertaining  to  or  secreting  mu¬ cus;  2)  of  the  pituitary  gland.  —  L.  pituitarius.
pituitous
‘pertaining  to  phlegm",  fr.  pituxta ,  ‘slime;  vis¬ cous  moisture,  phlegm’,  fr.  I.-E.  base  *pi-,  ‘sap, juice’,  whence  also  L.pinus,  ‘pine’.  See  pine,  the tree,  and  cp.  Hypopitys.  For  the  ending  see adj.  suff.  -ary.
Derivative:  pituitary,  n.
pituitous,  adj.,  pituitary.  —  L.  pituitosus,  ‘full  of phlegm,  pituitous’,  fr.  pituita.  See  prec.  word and  -ous.
Derivative:  pituitous-ness,  n. pity,  n.  —  ME.  pite,  fr.  OF.  pile,  pitet  (F.  pitie), fr.  L.  pietatem,  acc.  of  pietds.  See  piety  and  cp. piteous.
Derivatives:  pity,  tr.  and  intr.  v.,  piti-ful,  adj., piti-ful-ly,  adv.,  piti-ful-ness,  n.,  piti-less,  adj., piti-less-ly,  adv.,  piti-less-ness,  n.,  pity-ing,  adj., pity-ing-ly,  adv.
pityriasis,  n.,  a  skin  disease  (tried.)  —  Medical  L., fr.  Gk.  mTupiaoig,  ‘scurf,  dandruff’,  lit.  ‘bran¬ like  eruption  of  the  skin’,  fr.  mrupov,  ‘bran’, which  is  cogn.  with  Mir.  caith,  ‘dandruff’.  For the  ending  see  suff.  -iasis. piu,  adv.,  more  (used  in  musical  terms).  —  It.,  fr.
L.  plus,  ‘more’.  See  plus.
Pius,  masc.  PN.  —  L.  plus,  ‘dutiful,  pious’.  See pious.
pivot,  n.,  a  point  or  pin,  etc.,  on  which  something turns.  —  F.  pivot,  of  uncertain  origin. Derivatives:  pirot-al,  adj.,  pivot-al-ly,  adv., pivot-er,  n.
pivot,  intr.  v,,  to  turn  about  on  a  pivot;  tr.  v.,  to cause  to  pivot.  —  F.  pivoter,  fr.  pivot.  See  pivot, n.
pixie,  n.  —  A  var.  of  pyxie. pixy,  pixie,  n.,  fairy,  elf.  —  Fr.  earlier  pisky, which  is  rel.  to  Swed.  pysk,  ‘a  little  fairy';  of uncertain  origin, pixy,  n.  —  A  var.  of  pyxie. piyyut,also  spelled  piyut,n., a  religious  poem  added to  the  liturgy  of  the  Jewish  festivals  and  spe¬ cial  Sabbaths.  —  Talmudic  Heb.  piyyut,  ‘poem, hymn’,  in  Medieval  Heb.  Titurgic  poem,  liturgic poetry’,  verbal  noun  of piyyet,  ‘he  wrote  poetry’, in  Medieval  Heb.  ‘he  wrote  liturgic  poetry’, which  is  prob.  a  back 
=== leaf 637
bal  adj.  of  xXav,  ‘to  break’. See  clastic  and  cp.  prec.  word, plague,  n.  —  ME.  plage,  fr.  MF.  plague,  fr.  L. plaga,  ‘stroke,  blow,  wound,  pestilence’,  fr.  I.-E. base  *plaq-,  *plag~,  ‘to  strike",  whence  also  Gk. 7rXr,oCT£iv,  irXqyviivai,  ‘to  strike’,1  7rXqyq,  Dor. txXaya,  ‘stroke,  blow’,  L.  plangere,  ‘to  strike, to  beat  the  breast’,  ‘to  lament  loudly’  (orig.  ‘to lament  while  beating  the  breast’),  OE.  flocan,  ‘to strike,  beat',  Goth.,  OS.flokan.'to  bewail',  OHG. fluohhan,  fluohbon,  MHG.  vluochen,  G.  flue  hen, OFris.  fldka,  Du.  vloeken,  ‘to  curse’  (orig.  ‘to lament  while  beating  the  breast’).  —  According to  some  philologists  L.  plaga  is  a  loan  word  fr. Dor.  -Xaya.  —  It.  piaga,  F.  plaie,  ‘wound, sore,  plague’,  Sp.  plaga,  ‘plague,  scourge,  calam¬ ity’,  llaga,  ‘wound,  sore',  OIr.  plag  (gen. plaige),  ‘plague,  pestilence’,  derive  fr.  L.  plaga. Cp.  plain,  ‘to  mourn',  plaint,  plangent,  plankton, plectrum,  Plegadis,  plessor,  plexor,  Aplectrum, apoplexy,  complain,  monoplegia,  dyplegia,  para¬ plegia,  Symplegades.  Cp.  also  flaw,  ‘gust  of wind’.
Derivatives:  plague,  tr.  v.,  plagu-ed,  adj.,  plagu- er,  n.,  plague-some,  adj ,,plagu-y,  adj. plaice,  n.,  a  European  edible  flatfish.  —  ME. plais,  plaice,  fr.  OF.  plaise,  plaiz  (F.  plie),  fr. Late  L,  platessa,  ‘plaice,  flatfish’,  which  prob. derives  fr.  Gk.  TxXaxu;,  ‘flat’.  See  place, plaid,  n.  —  Gael,  plaid,  ‘blanket’,  prob.  contract¬ ed  fr.  peallaid,  ‘sheep  skin',  fr.  peall,  ‘skin’,  fr. L.  pellis,  ‘skin,  hide’.  See  fell,  ‘hide’,  and  cp. pillion.
plain,  adj.,  flat;  clear,  distinct.  —  ME.,  fr.  OF. (  =  F.)  plain,  fr.  L.  planus,  ‘even,  level,  flat,  clear, distinct’,  fr.  I.-E.  base  *p(e)la-,  ‘broad,  flat, spread  out’,  whence  also  Lith.  plonas,  ‘thin', Lett  .plans,  ‘flat,  thin’,  OPruss.  plonis,  ‘threshing floor’,  Gk.  Tt£Xavo<;,  ‘sacrificial  cake’.  Hitt. palhi,  ‘broad’.  Cp.  plain,  ‘level  country’,  plane, ‘even,  level’,  plane,  the  tree,  plane,  ‘tool  for smoothing’,  piano,  llano,  esplanade,  explain,  ex-
planation;  cp.  also  Pole.  Cp.  I.-E.  base  *pla-ro [=  -r-enlargement  of  base  *p(e)ld-],  which  ap¬ pears  in  OIr.  tar  (gen.  lair),  ‘ground,  floor’,  OE. flor ,  ‘floor’,  MHG.  vluor,  G.  Flur,  ‘meadow, plain’;  see  floor.  For  a  dental  enlargement  of base  *p(e)la-  see  field.  Two  other  enlargements of  base  *p(e)la-  are  *p(e)lag-  and  *p(e)!aq-.  The former  appears  in  Gk.  TtX&yoz,  ‘side’,  nXivtoe, ‘placed  sideways,  oblique,  slanting’,  7reXayoi;, ‘the  open  sea’ ;  cp.  flake,  ‘a  thin  flat  piece’,  flake. Tack  for  storing  goods’,  flask,  ‘plate  of  the  trail of  a  gun  carriage’,  flaw,  ‘crack’,  flay,  fleck.  For derivatives  of  base  *p(e)Iaq-  see  please, plain,  n.,  level  country.  —  ME.  plein,  playn,  fr. OF.  plain,  fr.  L.  planum,  ‘level  ground,  plain’, prop,  neut.  of  the  adj.  planus,  ‘level,  flat’,  used as  a  noun.  See  plain,  adj.  F.  plaine,  ‘level  coun¬ try,  plain’,  is  formed  fr.  the  fern,  of  the  adj. plain,  "even,  level’  (fr.  L.  planus). plain,  intr.  v.,  to  complain,  lament.  —  ME. pleinen,  playnen,  fr.  OF.  (==  F.)  plaindre,  ‘to mourn’,  fr.  L.  plangere,  ‘to  strike,  to  beat  the breast’,  ‘to  lament  loudly’  (orig.  ‘to  lament  while beating
```


## [2026-09-14T00:52:52.521Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"frathah\\|fra&ah\\|fra9ah\\|frathanh\\|Avestic  perethu\\|perethu\\|pere&u\" KLN_1966.txt KLN_1971.txt | head -20; echo \"=== place entry\"; grep -n \"^place,  n\\.\\|place,  n\\., \" KLN_1966.txt | head",
 "description": "Klein Avestan wide forms"
}
```


### [2026-09-14T00:52:52.616Z] TOOL RESULT

```
=== place entry
28981:place,  n.  —  ME.,  fr.  OF.  (=  F.),  fr.  VL.  *plattea (whence  also  It.  piazza,  OProvenq.  plasa,  Catal. plassa,  Sp.  plaza.  Port,  pra(a),  fr.  L.  platea, ‘open  space,  street’,  fr.  Gk.  -XaTEta  (686; ), ‘street’,  lit.  ‘broad  way’,  fern,  of  -XaTuq,  ‘flat, wide,  broad’,  which  is  cogn.  with  OI.  prathati, ‘spreads  out’,  prthith,  ‘broad,  wide,  spacious’, Avestic  plrepush,  of  s.m.,  Arm.  lain,  ‘broad’,  L. planta,  ‘sole  of  the  foot’,  OSlav.  plesno,  of  s.m., Lith.  platiis,  ’broad’,  pletoti,  ‘to  spread  out', plotyti,  ‘to  fold’,  MDu.  vlade,  Du.  via,  vlade, ‘cake’,  OHG.  flado,  ‘offering  cake’,  MHG. vlade,  ‘flat  cake,  honeycomb’.  G.  Fladen,  ‘flat cake’,  Swed.,  Norw.  fiundra,  MHG.  vluoder, G.  Flunder,  ‘flounder’,  OIr.  lethan,  Co.  ledan, ‘broad’.  All  these  words  are  derivatives  of  I.-E. base  *pldt-,  *plet-,  *plet-,  *plot-,  ‘spread  out, broad,  flat’.  Cp.  piazza  and  plaza,  which  are doublets  of  place.  Cp.  also  flat,  ‘level’,  flat, ‘floor’,  flawn,  ‘a  kind  of  pie',  flounder,  ‘a  fish’, placer,  placeta,  plaice,  plantain,  plant  of  the genus  Plantago’,  plane,  the  tree,  plant,  plantar, plat,  ‘piece  of  ground’,  plat,  ‘course  of  meal’, plateasm,  plateau,  plate,  platinum,  Platon,  plat¬ ter,  platy-,  plot,  ‘piece  of  ground',  and  the  first element  in  Plattdeutsch.
```


## [2026-09-14T00:53:06.415Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'place,  n.  —  ME.,  fr.  OF.' in l:\n        nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', l)\n        print('place leaf',i,nums[:6])\n        # print neighbors\n        for j in (i-1,i,i+1):\n            print(j, re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$', leaves[j])[:4])\nEOF",
 "description": "Klein place leaf/page"
}
```


### [2026-09-14T00:53:07.694Z] TOOL RESULT

```
place leaf 636 []
635 ['1190']
636 []
637 []
```


## [2026-09-14T00:53:08.176Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT frathah\"; grep -n \"fra&ah\\|fraθah\\|fra\\^ah\\|fra9ah\\|frathah\" BRT.txt | head -10; echo \"=== BRT search Breite\"; grep -n \"Breite\" BRT.txt | head -20",
 "description": "Bartholomae fraθah"
}
```


### [2026-09-14T00:53:08.278Z] TOOL RESULT

```
=== BRT frathah
21355:yavö.fra&ah-
21359:•  j.  *yavö.fra^ah'ya-''  n.  'Breite  eines Yava:  bar?sma  antarät  naetnäj  *ais$.drä-
=== BRT search Breite
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
11428:Y.  5t.  13;  —  iya/  aibl.ggmm  ya%rll  'i f?ntus{si.)  Y.46.  11;  —  /rlf  täii'  vufäis 'vatS  frafrä  (sd.)  pirsiBm  "^.46. 10;  — JrapSrayätihe  unian^m  tarS  'vatS  f?r3tBm Y.7/,16;  —  tarS  'vatS pgntüpt  vfinlra- yeiti  haltB  mainytmanqm  yazatanam  V.  ig. 30;  —  'vatS  piniüm  yazamaide  garö nmämm  .  .  vahishm  ahüm  Vr.  7.  i ;  — tarS  p3iüm  daraisrBtim  yim  "vatS  Vyt.42. *)  Die  Richterbrücke,  bei  der  die  Scheidung der  Guten  and  Bösen  erfolgt.  Sie  echt  nach mp.  Büchern  vom  Nocdfuss  des  Hathurz  zu dessen  Südkunm  ;  unter  der  Mitte,  die  äuf  dem rt*J//'<iü//a('Gericht5bere')ruht,  liegt  die  Hölle. Für  den  Gerechten  erscheint  sie  in  der  Breite von  9  Speeren  oder  27  Pfeilen,  für  den  Gott- losen so  schmal  wie  die  Schärfe  eines  Messers, so  diss  er  in  die  Hölle  sturit.  Vgl.  Bd.  ly.  7, 30.  33,  Dd.  21.  I  f.,  35.  6,  34.  4,  Mi.  2.  115, Dk.  9.  10.  3.  Av.  3.  \,  SJ.  3  f.,  sowie  die  von Modi  JRASBombay  7502  mitgeteilte  Stelle  des CrBd.
14097:gieich    an  pahtäk  'Breite'  gegenüber  np.  di-
16335:•  }.  p^sto.fra^aDham  Adv.  'in  der  Breite
17244:[Höhe  und  Breite  als  die  Erde;  und  es  ist I  die  Erde   so   gross  an  Höhe  (Tiefe)  wie
17250:an  Breite"  Y.ig-T, —  ovaiH  '«ff  V.  2.19 PuZ.
17648:•  j,  fra^h-  n.  'Breite':  avavaitya  batasca (sd.)  ■•'has&  . .  ya^a  fm  za;  astica  Im  sa avaiti  bazsl^^  yavaitt  ''kaicit  Y.ig."}.
18894:•  3.  nävaya-  Adj.  (fem.  °ya-)  'schiffbar',  Be- zeichnung fli essenden  Wassers  von  grösserer Breite  und  Tiefe:  airysJayatam  ..yahmya apö  'y&  p^n%wi/  XiaoiartAa  %waxi?nU Yt  10. 14;  —  . .  'hraotS.siacS  apa  taänä 'yä  Yt/J.  ro;  — pxavS /raoirisyBti  tarasca apB  'ya  (APf.)  V.  14. 16;  7<y.  74;  —  tyaäa *nä  buyat . ,  hupirihwe  a/s*'ya''>  Yt.i6.y,
21356:•  J.  yavö.fraSah-  Adj.  (auch  fem.)  'von der  Breite  eines  Yava'*'':  bansma  aisS.- dräjS  »äJ  N.  70;  V.  /^.  19;  —  äat  upama aiiS.drajaf)ha  (sd.)  '%at)ha  (NPf,  näral. urvarayä  atfhn)  N.go.
21359:•  j.  *yavö.fra^ah'ya-''  n.  'Breite  eines Yava:  bar?sma  antarät  naetnäj  *ais$.drä-
22994:•  j.  varasö.stavah-  Adj.  (auch  fem.)  'von der  Breite,  Dicke  eines  Haars':    °vanA?m
26934:•  j.  spä.fraB-ah-  Adj.  (auch  fem.)  'in der  Breite  eines  Hunds':  cnaj  yavat vai^Tml . .  spnMnzim  (sd.)  °fra%)m  (ASf.)*' V.J4. 12.
28122:•  j.  zsm.fraStih-  Adj.  'von  der  Breite  der Erde,  so  breit  wie  die  Erde':  mi^nm  .  . yj  '%S  aiwyäiti  Yt/0.95;  —  °%S  niaf- ha/am  Yt  10.  44;  —  aisi/  badaza  . . '^aaAa  (APn.)"  dänu.drajar)ha  hvan.- bartzanha  "der  Aiay  Heilmittel . .,  die  so breit  wie  die  Erde,  so  lang  wie  die  Russe, so  hoch  wie  die  Sonne  sind"  Y.  60. 4.
```


## [2026-09-14T00:53:18.555Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD prd\"; grep -n \"prd'nk\\|prd\\`nk\\|prdynk\\|prthynq\\|prd’nk\\|curtain\" SOD.txt | head -20",
 "description": "Gharib Sogdian curtain"
}
```


### [2026-09-14T00:53:19.599Z] TOOL RESULT

```
=== SOD prd
55341:curtain 
56507:curtain 
88559:curtain    7084,  7254
```


## [2026-09-14T00:53:20.255Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB farax\"; grep -n -i \"farâx\\|ferāx\\|feräx\\|farax\\|frāh\\|frathah\" HUB.txt | head -20",
 "description": "Hübschmann farāx"
}
```


### [2026-09-14T00:53:20.475Z] TOOL RESULT

```
=== HUB farax
2951:810. ^"p. farax = phi. /r^au, geschrieben fraxv scheint ein
```


## [2026-09-14T00:53:22.650Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2940,2975p' HUB.txt",
 "description": "Hübschmann entry 810 context"
}
```


### [2026-09-14T00:53:22.732Z] TOOL RESULT

```
auf ein phi. *farnak, sondern, wie np. farrihl *Herr-
liehkeit* zeigt, auf ein phi. ^farreh (vgl. syr. B^l^niB
Farrahanns N. pr. bei Hoffmann, Ausziige p. 72) =
ap.*/arwaAa- (oder ein ahnlich erweitertes farnah-) zu-
riiek, vgl. np. xurrah = paz. x^areh Min. Gl. {x^arehe
Shk. 255) = zd. x^arenaflha- (oder ein sLhnlich er-
weitertes x^arenailh').
*) YgL zd. ac^arenahha nom. sg., afarenafihvanta instr. sg.,
x'arenanhuniem = x^arenahhentem ace. sg.
6*— 84 —
809. Np. fara = skr. prak Vorn, vor etc.
810. ^"p. farax = phi. /r^au, geschrieben fraxv scheint ein
ap. *fra(k)uva" vorauszusetzen. Ebenso Fr. Miiller,
WZKM. 7, 378.
812. Zu der vorgeschlagenen Etym. passt das o von phi.
psiz. framos, farmos (Min. 61. 75, Shk. 244), np. fara-
moS nicht. Doch ware np. faramnst = skr. ^pramrsta-,
*pramrsti-. Dames hat nh, sa-musay^ sa^musay (mitw,
u) *to forget'.
813. Gegensatz von zd. frapi^wa- gut genahrt, gedeihend'
= np. farbih pinguis, robustus, florens, copiosus' ist
zd. tardpt&wa- vd. 13, 20 = *sehleeht genS-hrt*. Np.
farbt JRAS. 1894, p. 477 = phi. frapfh = zd. *fra-
p^d^wa-? Zur jiid. pers. Form vgl. paz. pad = phi.
pit ^fat' Shk. 261.
Nach 816 ware nach Salemann np. farasp = phi. frasp
(Gl. and Ind. 98) = zd. fraspaU zu erwahnen. Die
Bedeutung des letzteren ist nicht sicher, Darmesteter
vermuthet *Teppich\
818. 6r. 6 naQaadyyriq; arm. LW. hrasax.
819. Lies zd. ^frasta- = ar. *pra8th'ta-f vgl. die Nach-
trage bei Horn p. 259. Dazu stimmt freilich der Vokal
von np. ftriMta 'Bote* nicht, der durch paz. frista =
phi. fnstak oder frestak *Bote' (Shk. 245) alt bezeugt
wird. Hat Anlehnung .an firista, alter fireSta JRAS.
1894, 478 'Bote, Engel' = phi. /rgs^afe = ap. */raisf a-
```


## [2026-09-14T00:53:23.701Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '55320,55360p' SOD.txt; echo \"#####\"; sed -n '56490,56520p' SOD.txt",
 "description": "SOD curtain entries"
}
```


### [2026-09-14T00:53:23.794Z] TOOL RESULT

```
7081  prS'yt-   B  jjLiT^^ 
arOayd   ©<*parifa-  6axta  ©pt.  st.  =^pr8>ync- 
0o)spread,  (r<?)pull 

GMS  600;  AVS  123 

7082  prSVkU)   B  •julT^^J* 
pa9aydak(u),  parGayde  ©pp. 

spread,  pulled 
VJ862 

7083  pre^tch   B  +x^£  myJ? 
parOaxtc  ©f.  pp. 

spread,  pulled 
VJ  19\  346 

7084  prS'nkOi)  B 
parGang  ^prS'ync-,  pr8ynq 
curtain 
TSP  3.159,  156 

7085  prS'w  S(M) 
parS/0aw   ©Khot.  padav 
flame 

BBB  bl5;  Benv.  Notesiv  518;  GMS  573;  Prolexis. 
154;Sund.  MHC  36.8  R6 

7086  prS'ync-   B  &jj 


*>j\ 


yj>rA 


parOenc  ©<*pari/a-6anjaya-  ©inf.  -h 
#####

7253  pr8ync-   C  0^ 
parOenj  ©impf.  pryOync  =*pr5}ync- 


*>j% 


o->j^~**f 


Go  )st  retch 

BSTii  875.19:  C2,  66V19 

7254  prBynq   C 
parGing  ©pi.  -t  ^pr6Jnk(h) 
curtain 

BSTii  90421;  STSC  106;  C2,  57R21 

7255  prw1  (o>>  >^  ^)>>  ^ ,  ^k 
paru,  parew   ©<*upari-avam   ^pr'w1,  *prw2,  pr 

to  it,  to  the,  for,  in,  on 
GMS  1432,  prwwt  KG  2358 

7256  prw3  M  j^li^^^ij^ 
paru   ©<*aparam   ^'prw1,  ^pr'w 

the  last,  latter,  then
```


## [2026-09-14T00:53:35.572Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(len(leaves))\nfor i,l in enumerate(leaves):\n    if '7084' in l and 'curtain' in l:\n        print('leaf',i,'printed ~',i-66)\n        print(l[:300])\nEOF",
 "description": "SOD page for entry 7084"
}
```


## [2026-09-14T00:53:36.427Z] TOOL CALL #36: Bash

```json
{
 "command": "ls tools/ | head -30; echo; python3 -c \"print()\"",
 "description": "List tools"
}
```


### [2026-09-14T00:53:36.680Z] TOOL RESULT

```
645
leaf 350 printed ~ 284
                                                                                                                284



prbyrdV

7075 prbyrd'r   C =» prbyrt-                                     parOenc ©<*pari/a-6anjaya- ©inf. -h
                                                                   =»pr
leaf 549 printed ~ 483
  483                                                                                                     defectivness


    8742, 8746                            curative     3048                      daughters      3688
 creator    3402, 8733, 8743
```


### [2026-09-14T00:53:37.583Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-14T00:53:43.049Z] TOOL CALL #37: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T00:53:43.053Z] TOOL RESULT

```


```


## [2026-09-14T00:53:47.035Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%D9%87",
 "prompt": "Give the full Persian etymology section for پرده (parde): Middle Persian form, Proto-Iranian reconstruction, PIE root, cognates, and any cited sources (Hasandust, Cheung, MacKenzie). Also note derived/borrowed terms."
}
```


## [2026-09-14T00:53:48.098Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/purdah",
 "prompt": "Give the full etymology of purdah, including Urdu/Hindi and Persian forms and dates of first English attestation."
}
```


### [2026-09-14T00:53:52.759Z] TOOL RESULT

```
# Etymology of Purdah

**First English Attestation:** 1800

**Etymology Chain:**
The word entered English from "Urdu and Persian _pardah_" meaning "veil, curtain." This Persian term derives from Old Persian components: _pari_ ("around, over") combined with _da-_ ("to place").

**Language Origins:**
- **Urdu/Persian:** _pardah_
- **Old Persian:** _pari_ + _da-_

**Proto-Indo-European Roots:**
The constituent elements trace back further to PIE: _*per-_ (1) meaning "forward" (hence "in front of, against, around") and _*dhe-_ meaning "to set, put."

The combined meaning reflects the practical function: something positioned to screen or separate, literally "to place around/over."
```


### [2026-09-14T00:53:53.245Z] TOOL RESULT

```
# Persian Etymology of پرده (parde)

## Middle Persian Origin
The word derives from Middle Persian *pltk'* (pardag), representing a continuation of an ancient term for cloth or covering material.

## Proto-Indo-European Root
The ultimate source is PIE *\*pel-* ("to cover, wrap; hide, cloth"), demonstrating the word's deep ancestry in Indo-European language families.

## Cognates
The entry lists several related terms across language families:
- Sanskrit पट (paṭa, "piece of cloth")
- Northern Kurdish perî, pelhe ("curtain; bridal curtain")
- Central Kurdish پەردوو (perdû, "roofing material, such as leaves, barks, etc.")
- Old Armenian պարտակ (partak)
- Classical Syriac ܦܪܕܩܐ (pardəqā)

## Cited Sources
The references section mentions MacKenzie's *Concise Pahlavi Dictionary* (1971) for the Middle Persian form, though specific etymological commentary from Hasandust or Cheung is not included in this Wiktionary entry's visible content.

The entry notes that Armenian and Syriac forms represent "Iranian borrowings," indicating the term's historical significance across the broader region.
```


## [2026-09-14T00:54:07.534Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN perde\"; grep -n -i \"perde\\|parda\\|pardag\" HRN.txt | head -20; echo \"=== HUB parda\"; grep -n -i \"perde\\|parda\" HUB.txt | head -20",
 "description": "Horn/Hübschmann parde"
}
```


### [2026-09-14T00:54:07.590Z] TOOL RESULT

```
=== HRN perde
219:eza-), während das dialektische *espäl — ap. ^sparda- die
2884:phlv. parda/tan (AV.).
6149:701. seperden, siperden auf etwas treten*.
8108:'Hofhund'j, nazule 'Kätzchen*, perdele 'Häutchen', segle 'Hündchen*,
18659:bergj. perdele 929 Anm.
=== HUB parda
196:avdr> Dann ware audi paz. apardan, apurdan^) 'to
1295:297. Np. pardaxtan hat bei Vullers 12 Bedeutungen,
1299:(vgl. afgh. LW. pardaxt performance, relinquishment,
1305:lassen . Phi. pardaxt verbraucht' Arta-Vlraf Cap. 89,
5819:307; Pahlav 'Parthien' --=^ ap. Pardava-; fadarv Tasan' H.
6292:sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
7930:auch aspal (in Klammern) an, das = ap. ^sparda-lw&TQ, Aber in echt
```


## [2026-09-14T00:54:13.687Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nhits=[i for i,l in enumerate(leaves) if re.search(r'پرده', l)]\nprint('hits',hits[:40])\nEOF",
 "description": "Borhan vol1 پرده"
}
```


### [2026-09-14T00:54:14.939Z] TOOL RESULT

```
hits [66, 104, 118, 120, 171, 255, 266, 312, 335, 391, 397, 401, 427, 434, 469, 503, 548, 605, 606, 607, 648, 709, 730, 734, 735, 739, 753, 773]
```


## [2026-09-14T00:54:15.638Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('n',len(leaves))\nfor i in range(230,242):\n    l=leaves[i]\n    print('=== pdfleaf',i, 'est printed', i+1209, repr(l[:200]))\nEOF",
 "description": "Borhan vol3 around p.1444"
}
```


### [2026-09-14T00:54:16.813Z] TOOL RESULT

```
n 721
=== pdfleaf 230 est printed 1439 '[pdf page 231]\naus\n\nو۳ اه\n\nربمعنی حو کوچك هم هست \u200eV\u200f - ومکفف\u200cزفانه\nهم هست که زبالٌ آتش ۴ و زيانة چوب و امثال\nآن\u200cباشد» وزبانٌ ترازو را یز گوبند .\n\n. \u200fحطی بروزن (۱)جاوید»\u200e st \u200fبا\u200e - AGU\n\nممرب \u200edh\u200f است ۴'
=== pdfleaf 231 est printed 1440 '[pdf page 232]\nوا\n\nفتالیدن ۱ © بفتح\u200cاول\u200cبروزن\u200cطراوبدن»\nبمعنی ریختن_ودردنوشکافتن_ویربشان\u200cوی را کنده\nکردن ۴ - و کندن\u200cوازهم\u200cجدا کردن وکستن ۴\nباشد ؛ \u200eGy\u200f اول هم گفته\u200cاند .\n\nفتح باب ۴ - کنابه از در باز \u200eOS'
=== pdfleaf 232 est printed 1441 '[pdf page 233]\n\u200ea\u200f را کمر کگشادن وا\nقتی = \u200eoth\u200f ول و \u200egl\u200f و سکون واو .\nبمعنی عربده جوی وغره و حفرور باشد ؛ وبجای\nحرف انی تون\u200cهم آمده است اشاعل ۳ .*\n\n\u200fبهرام او را و \u200ethu\u200f قصی پردن او کاو را مشهور "\nاست'
=== pdfleaf 233 est printed 1442 '[pdf page 234]\n\u200eoly\u200f چهازم\n\n\u200fدرحرف فا با خای \u200elabs\u200f مشتمل بر دوازده \u200ecal\u200f\n\n\u200fجح ۱ \u200ecr\u200f اول و سکون ثالی:بمنی\n\n\u200fتله باشد \u200eSe AT oF,\u200f بدان جالو رگیرید \u200e -\u200f\n\n\u200fو بممتی شکار وشکارگاه نیز آمده است .\n\n\u200eCS\u200f = ب'
=== pdfleaf 234 est printed 1443 '[pdf page 235]\nwee)\n\nآورد .#\n\nخمیده \u200ego)\u200f وزن فهمیده,پنبه را\nکوبند که پنبهدانة آنرا جدا کرده وبرآورده\u200cباشند\nوهتوز حلاجی نکرده باشند .\n\n\u200eupd\u200f بفتح اول و سکون الی ولون»\n\n\u200f۱44۲\n\u200eOle\u200f و درون باغ راکوبند -'
=== pdfleaf 235 est printed 1444 '[pdf page 236]\noN Efe\n\nودبوث هم حست - و بزبان \u200eblk\u200f خوردلی\nو طمامی باشد که در دستمال (۱) بسته از جایی\nبجایی برند - و بیعنی دستور هم بنظر آمده\n\nاست .\n\nقدرو نك \u200ebw\u200f رای قرشت (۲) \u200eogy\u200f\n\u200fبروزن(۳)زتبورلك س'
=== pdfleaf 236 est printed 1445 '[pdf page 237]\nفرابرز\nهست - وبمعنی بر و در \u200eee\u200f علی\u200cوفی\u200cخوانند\n- وبمعنی مه\u200cومجموع- وزیادت - و اخذ کردن\nو ستایدن آهده است - و با تشدید \u200e«gt\u200f\n\u200fبلفت\u200cعربی بمعن ی کر بختنو کربزان شدن\u200cباشد ۷.\n\nفرا برد \u200ecae\u200f'
=== pdfleaf 237 est printed 1446 '[pdf page 238]\nسووعوت\nقراخ \u200egi\u200f - کنابه ازبتتابوسبیل\nرفتن باشد .\n\u200eO18\u200f و ۱ - بنتهرایبی قطه,تمجیل\nو شتاب رونده را گویند - و کنایه از کی است\nکه ازحد خود بیرون رود- ومسرف وعرزه\u200cخرج\n\n,\\ نیز گویند ۳ - وم ر'
=== pdfleaf 238 est printed 1447 '[pdf page 239]\nفراز\nفلاطرن , کسیرا و چیزیر! کویند که نه بطریق\n\u200eHe THe\u200f پس رود. یمنی روز به نباشد وروزبروز\nپي رود .\n\n\u200eILS\u200f ۷ - بروزن نماز . چندممنی\u200cدارد:\n۱- پهن شده و پخش کردیده باشد . ۲ - بسته\nو کشاده'
=== pdfleaf 239 est printed 1448 '[pdf page 240]\n~\\tty—\n\nفراسیون ۱ = بفتح اول وکس رابع\nبر \u200eoir\u200f حواربون .گندنای کوهی باشد و \u200eWT\u200f\n\u200fبتازی \u200eMinto\u200f وصوف\u200cالارش و سندبان\u200cالارش\nخوانند . چون با نمك برگزند کیک دیوانه\nماد کنند \u200egil\u200f باشد ؛ وآن '
=== pdfleaf 240 est printed 1449 '[pdf page 241]\nay\n\u200fاول وسکون آخ رکه کاف\u200e ails\n\u200fبلشد » بمعنی پشت است که در مقابل رو است\u200e\n\nو جربی ظهر خوانند - و در بعضی حیز ومخنث\nرا کفته\u200cاند - وپلید و پلشت (۱) و زبون را ح\u200c\n\nمیگویند .\n\n\u200eSUS\u200f ۱ - بح او'
=== pdfleaf 241 est printed 1450 '[pdf page 242]\n—\\tta—\n\nقراود \u200etote\u200f بروزن \u200ehe ele\u200f\nموضعی \u200ecol\u200f در خراسان و در آلجا چشمه\u200cایت\nکه چون درآن چشممغوطه خورند \u200ebent\u200f\n\u200fکند .\n\nفراو فك ۲ » بر وزن دماوند + چوب\n\u200eGlen”\u200f باش دکه\u200cدرپس در کوچه نهند '
```


## [2026-09-14T00:54:26.770Z] TOOL CALL #43: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1444 --image 2>&1 | tail -40",
 "description": "Render Borhan page 1444"
}
```


### [2026-09-14T00:54:34.449Z] TOOL RESULT

```
فراپرز نله
هست - وبمعنی بر و درکه‌بمربی علی‌وفی‌خوانند قراخ - بفتح‌اول وئانی بالف کشیدمویهای
- ویمع - وزبادت - و آخذ کردن
ی ی خذ کردن نقطه‌دار زده ‏ بیعنی کشاد است ۴ - و بععنی
: نّ ست.- تشدید تانی. ‌
۳ نما 6 فا بسیار هم‌آمده است ؛ وبکس اول در عربی جمع
بلفت‌عربی بممن ی کر بختن و کربزان شدن‌باشد :| فرخ امت که جوجه مرغ خانگی باشد.
فارز ند ۱ ت 3 جوم ب
فر برد نو اول وضم بای ایجد(۱) فراخا ۴ + قح اول وثانی ورابع بالف
و سکون رای قرشت (۲) و زای هوز )۳( نلم کشده . بمع فراخ وکشادگی باشد ومحل
پهلوانی بوده ابرائی از سپه داران و رای زنان فراخی وکشادگی را نی ز گوبند بعنی چیزی که
دارا ۰ او مردی بود که پیوسته دارا در کارها فراخی وکنادگی قام باوست ۱
باو معورت کردی و او را بجنگه اسکندر رخصت اوه
نداد . قراخ ) سین - کنابه از جوان مرد
و ۱ 1 وصاحب: اهمت و کریم و بخشنده باشد 8 .
قراله - بم اول وافتح تای قرشت . وا ۹ :
آب انگور اس ت که نشاسته و آرد کندم در آن فر خن - فح اول بروزن نواختن.
ربزند و چندان بجوشانند که بقوام آید وسنمت | بمعنی افراختن است که بلند ساختن وبالا بردن
شود وآنرا بررشته‌ای که مغز بادام پا مغز جوز | باشد :
کشیده باشد مانندشمع پر یز ندوآ نرادرآذربایجان فراخ دست - بفتح اول ودال ابجد .
پاسدق کوبند پم دال ابجد : بمعنی فراخآستین امت که جوان مرد و صاحب
قراقین ؟ - باتای قرشت‌بروزنملاطین. | اهمت وبخشنده وکریم باشد ۷ .
آسمانی زبان است بلفت زند واستا . ونوادزبان | از بسیارکو و پوچ گو و هرزه چانه و بد زبان
راگوبند بفتح نون . است .
(۱) چك : وضم با - (۷) چك : وسکون را . (۳) چك : وزا .
۹ - (عر) فر ( بفتح اول و تشدید دوم) وفرار ( بفتح وکسر وضم اول )بمعنی گربختن
است. رلد: شرح قاموی, منتهی آلارب.
۲ - برساخته دساتینر « فرهنگك دساتیر ۲۵۹ »« فاب ۱ص 4۷ >
۴ - اوستا - ۲۲۵188۳ ( عرض » پهنا ) . بهلوی دلق)؟ فقس : |8]طة3)] .
]۲۲2۵ هندی باستان - ۳45( »کردی ع 0( (کناد) : بلوچی 0/5
( کعاد » عررض ) « اسشق ۸۱۰ . درپهلوی ۲۳3 که ۲۳31۷ نوشته شود » از پارسی باستان
-1۳2)(۷۵* مأخون است « هوبشمان ۸۱۰ > پازند ۳28] , 0672 « نیب رکه ۷۱.
۴ - از : فراخ ۹ ( پسوند ساختن‌اسم ازصفت ) لقن : درازا » ژرفا .رك: اسم‌مصدر
بغلم نگارنده ص۱۱۸ ] * فراخی ۳ فراخنا ؛ درکردی « فراوا > بمعنی عرض « ژابا صس ۲۹۰ >:
شادیت باد چندانك آندر جهان فراخا تو با نشاط وراحت با رنج ودرد اعدا .
دقیقی‌طوسی « لغت فری ۰۲۹۱۶
8 -فی : فراخ دست. ۹ - مخغف « افراختن > (ه.م.) ور4: افراشتن .
۷ - قس : قراخ آستن ۰
```


## [2026-09-14T00:55:08.344Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor fn,pat,off in [('HJB.txt', r'PURDAH', 43), ('AID.txt', r'Pardah\\.\\s+\\[Persian', 18)]:\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    leaves=txt.split('\\f')\n    for i,l in enumerate(leaves):\n        if re.search(pat,l):\n            print(fn,'leaf',i,'est printed',i-off)\n            print(l[:1800])\n            print('-----')\nEOF",
 "description": "HJB/AID purdah leaves"
}
```


### [2026-09-14T00:55:09.514Z] TOOL RESULT

```
HJB.txt leaf 442 est printed 399
ons'  (lit.  *Lord  of  cows'),  i,e, one  who  is  supnosed  to  have  subdued his  passions  and  renounced  the  world. Applied  in  various  parts  of  India  to dinerent  kinds  of  persons  not  neces- sarily celibates,  but  professing  a  life  of religious  menaicancy,  and  including some  who  dwell  together  in  convents under  a  superior,  and  others  who  en- cage in  trade  and  hardly  pretend  to ^d*a  religious  life.
1774. — "My  hopes  of  seeing  Teshu  Lama were  chiefly  founded  on  the  Qosain."— Bogle,  in  Markham's  Tibet,  46.
c.  1781. — "It  was  at  this  time  in  the bands  of  a  Qosine^  or  Hindoo  Religious." — Hodgei,  112.  (The  use  of  this  barmuism  by Hodges  is  remarkable,  common  as  it  has become  of  late  years.)
[1818.— "  Unlike  the  eeneralit^  of  Hindoos, theee  CtoMdngs  do  not  burn  their  dead  ..."
FwheB,  Or.  Mem,  2nd  ed.  i.  812-3 ;  in  i. 544  he  writes  Oosaimeo.]
1826. — "I  found  a  lonely  cottage  with  a light  in  the  window,  and  being  attired  in the  habit  of  a  ^^OBsein,  I  did  not  hesitate  to request  a  lodging  for  the  night." — Pandu- rang  Sari,  399 ;  [ed.  1873,  ii.  276].
GOSBECE,  GOSBEAGUE,  s.     A
coin  spoken  of  in  Persia  (at  Gombroon and  elsewhere).  From  the  quotation from  Fryer  it  appears  that  there  was a  Go8s  and  a  Gosbegty  corresponding  to Herbert's  double  and  single  Cozbeg^ Mr.  Wollaston  in  his  English-Persian Did.  App.  p.  436,  among  "Moneys now  current  m  Persia,"  gives  "  5  dindr =  1  gh&z ;  also  a  nominal  money." The  ghdZy  then,  is  the  name  of  a  coin (though  a  coin  no  longer),  and  gh&z- beg!  was  that  worth  10  dindrs. Marsden  mentions  a  copper  coin, called  kaabegi^fiO  (nominal)  d
-----
AID.txt leaf 261 est printed 243
Parbhus  were  em- ployed as  clerks  by  the  Portuguese and  English  before  the  Brdhmans accepted  such  service,  and  the  latter have  been  unable  to  oust  them.
Farbutty.  See  Pdrwati.
Farcherry.  *   [Perhaps  the  same  word as  pat  cherry,  or  from  para,  other, foreign.]  The  outskirts  of  a   town, the  quarter  where  the  Paraiyans usually  live.
Pardah.  [Persian.]  A   veil,  a   screen, a   curtain,  especially  one  used  to  ex- clude women  from  public  view.
Pardahnishin.  [Persian  njfhin ,   who sits.]  A   woman  who  observes  the practice  of  seclusion.
Pardedi.  [Hindi,  from  the  Sanskrit para ,   other,  and  de/a,  country.]  A foreigner;  but  particularly,  in  the Bombay  presidency,  a   Rdjput  from Hindustan.
P&rdhi.  [Mardthi,  from pdradk ,   hunt- ing.] The  name  of  a   caste,  whose profession  is  hunting  and  scaring wild  animals.  Many  of  .them,  es- pecially those  called  Langofi  and Phdnsi  Pdrdhis,  are  professional thieves,  and  are  said  to  be  a   branch of  the  Bdori  tribe.  Compare  Pdradhi.
Pardl.  [Mardfhi.]  A   small  pateh  of
FARG
*43
PARS
-   ground  surrounding  or  adjoining  a house,  and  usually  free  of  assess- ment. When  unduly  large  a   limit is  sometimes  fixed,  and  pardi  lands in  excess  of  it  are  assessed.
Fargand,  or  Parghnah.  [Hindi.]  A district,  a   province,  but  especially  a subdivision  of  a   zillah  ;   a   tdluk.
Parheyd.  An  aboriginal  tribe  living in  the  hill  ranges  of  Lohdrdagd;  they may  be  a   branch  of  the  Mun<Jds,  but have  adopted  Hindi  speech,  and their  marriage  and  funeral  cere- monies are  according  to  Hindu :   custom.
Fari.  [Persian.]  A   fabulous  winged monster  with  the  body  of  a   horse .■  and  a   
-----
```


## [2026-09-14T00:55:17.347Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if '1809.— \"On  the  fourth' in l or re.search(r'PURDA\\b|PURDAH,\\s+s', l):\n        print('leaf',i)\n        print(l[:2500]); print('----')\nEOF",
 "description": "Hobson-Jobson purdah entry"
}
```


### [2026-09-14T00:55:18.493Z] TOOL RESULT

```
leaf 790
  Williamson  mentions  that  punkahs "  were  suspended  in  most  dining  halls." — Vade  Mecum,  i.  281.
1823.— "Punkas,  large  frames  of  li^ht wood  covered  with  white  cotton,  and  looking not  unlike  enormous  fire-boards,  hung  from the  ceilings  of  the  principal  apartments." — Heber,  ed.  1844,  i.  28.
1852.— "  Holy  stones  with  scrubs  and  slaps
(Our  Christmas  waits  !)  prelude  the  day  ;
For  holly  and  festoons  of  bay
Swing  feeble  punkas, — or  perhaps
A  windsail  dangles  in  collapse."
Christmas  on  board  a  P.  and  0.,  near the  Kquatw.
PUNSAREE.
744
PUTCHOCK.
1875. — "The  punkah  flapped  to  and  fro lazily  overhawi.  — ChesMy,  The  DUemmAf ch.  xxxviii.
Mr.  Biisteed  observes  :  "  It  is  curious that  in  none  of  the  lists  of  servants and  their  duties  which  are  scattered through  the  old  records  in  the  last century  (18thX  is  there  any  mention of  the  pimka,  nor  in  any  narratives referring  to  domestic  life  in  India then,  that  have  come  under  our  notice, do  we  remember  any  allusion  to  its use.  .  .  .  The  swinging  pimka,  as we  see  it  to-day,  was,  as  every  one knows,  an  innovation  of  a  later  period. .  .  .  This  dates  from  an  early  year  in the  present  century." — Echoes  of  Old Calcutta^  p.  115.  He  does  not  seem, however,  to  have  found  any  positive evidence  of  the  date  of  its  introduction. ["Hanging  punkahs  are  said  by  one authority  to  have  originated  in  Cal- cutta by  accident  towards  the  close  of the  last  (18th )  century.  It  is  reported that  a  clerk  in  a  Government  office susjjended  the  leaf  of  a  table,  which w^as  accidentally  waved  to  and  fro  by a  visitor.  A  breath  of  cool  air  followed the  movement,  and  suggested  the  idea which  was  worked  out  and  resulted  in the  present  machine  "  (CVirey,  Good  Old Days  of  John  Company,  i.  81).  Mr. Douglas  savs  that  pimkahs  were  little used  by  Europeans  in  Bombay  till 1810.  They  were  not  in  use  at Nuncomar's  trial  in  Calcutta  (1775), Bovibay  and  W,  India,  ii.  253.]
PUNSABEE,  s.  A  native  .drug- .seller  ;  Hind,  pansdrh  We  place  the word  here  partly  because  C.  r.  Brown says  *it  is  certainly  a  foreign  word,' and  assigns  it  to  a  corruption  of  dis- pensarium;  which  is  much  t^  be doubted.  [The  word  is  really  derived from  ^kt.  pa?iyaJdla,  'a  market,  ware-
----
```


## [2026-09-14T00:55:23.386Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('HJB.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nl=leaves[790]\ni=l.find('PUNSABEE')\nprint(l[i:i+3000])\nEOF",
 "description": "HJB p.744 PURDAH entry"
}
```


### [2026-09-14T00:55:24.476Z] TOOL RESULT

```
PUNSABEE,  s.  A  native  .drug- .seller  ;  Hind,  pansdrh  We  place  the word  here  partly  because  C.  r.  Brown says  *it  is  certainly  a  foreign  word,' and  assigns  it  to  a  corruption  of  dis- pensarium;  which  is  much  t^  be doubted.  [The  word  is  really  derived from  ^kt.  pa?iyaJdla,  'a  market,  ware- house.']
[1830. — "Beside  this,  I  purchased  from  a IMUisaree  some  application  for  relieving  the pain  of  a  bruise.  — Frazer,  Tfie  Persian Adventurer,  iii.  23.]
PIJBDAH,  s.  Hind,  from  Pers. parda,  '  a  curtain ' ;  a  portih-e ;  and especially  a  curtain  screening  women from  the  sight  of  men  ;  whence  a woman  of  position  who  observes  such rules  of  seclusion  is  termed  parda- nishln,  *one  who  sits  behind  a  curtain,' (See  GOSHA.)
1809.— "On  the  fourth  (side)  a  purdah was  stretched  acron."— Z^.  Vaientia,  i.  100.
1810.— "If  the  disorder  be  obstinate,  the doctor  is  permitted  to  approach  the  purdah (i.e.  curtain,  or  screen)  and  to  put  tMe  ka^d through  a  small  aperture  ...  in  order  to feel  the  patient's  pmse." —  WilliamsoH,  V.  21. i.  130.
[1813. — "My  travelling  palankeen fonned my  bed,  itsjpnrdoe  or  chintz  ooTering  mj curtains." — Forbes,  Or*  Mem,  2nd  ed.  ii.  109.]
1878. — "  Native  ladies  look  upon  the  coo- finement  behind  the  purdah  as  a  badge  of rank,  and  also  as  a  sign  of  chastity,  and are  exceedingly  proud  of  it."— A/;>  ij»  tke MofussiI,i.m.
[1900.—"  Charitable  aid  is  needed  for  the purdah  women." — Pioneer  Mail ^  Jan.  21.]
PIJBDESEE,  s.  Hind,  paradesl usually  written  pardesi,  'one  from  a foreign  country.'  In  the  Boml^ay  army the  term  is  universally  appliei  to  a sepoy  from  N.  India.  [In  the  N.W.P. the  name  is  applied  to  a  wandering tribe  of  swindlers  and  coiners.]
PUBWANNA,  PEBWAUHA,  sl
Hind,  from  Pers.  partpdna^  *  an  order  ; a  grant  or  letter  under  royal  seal  ;  a letter  of  authority  from  an  official  to his  su))ordinate  ;  a  license  or  pass.'
1682.—"  .  .  .  we  being  obliged  at  the  end of  two  months  to  pay  Custom  for  the  s«id goods,  if  in  that  time  we  did  not  procure  a Pherwanna  for  the  Duan  of  Decca  to  ezcn^ us  from  it." — Hedges,  Diary,  Oct.  10  ;  [Hak. Soc.  i.  34].
1698. — " .  .  .  Egmore  and  Pursewaukum were  lately  granted  us  by  the  Nalwb's  por- waanaB."— Wheeler,  i.  281.
1759.— "  Perwanna,  under  the  Coochnck (or  the  small  seal)  of  the  Nabob  Vizier  Uhna Maleck,  Nizam  ul  Muluck  Bahadour,  to Mr.  John  Spenser." — In  Cambridge's  Acri.  of tiie  War,  280.  (See  also  quotation  under HOSBOLHOOKUH.)
1774. — "  As  the  peace  has  been  ao  lately concluded,  it  would  be  a  satisfaction  to  the Rajah  to  receive  your  parwaxma  to  this purpose  before  the  departure  of  the  caravan." — Bogle's  Diary,  in  Mariham't  Tibd,  p.  50. But  Mr.
```


## [2026-09-14T00:55:31.720Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index parde/farax\"; grep -n -i \"PARDE\\|PARDA\\|FARAX\\|FARĀX\\|FARAKH\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur index"
}
```


### [2026-09-14T00:55:31.775Z] TOOL RESULT

```
=== ARY latin index parde/farax
4261:SKEAT: PARDE (FRENCH) «i
4585:HOLD CHURCH SLAVIC) 4S 5 s%| PARDAZISHN, PARDAXTAN
4604:Se aly el oo pe pa Gala platy "gut aT” py 4 PARDAXTAN 3!) ly O45 22 ot
4605:64: MACKENZIE tg £4) col 29 "g Sey" 4"21jT" py 4 PARDAZISHN
```


## [2026-09-14T00:55:33.943Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor fn in ['MON_part1.txt','MON_part2.txt']:\n    txt=open(fn,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'پرده', txt):\n        s=max(0,m.start()-150); print(fn, repr(txt[s:m.start()+200])); break\n    print(fn, 'count', txt.count('پرده'))\nEOF",
 "description": "Mo'in parde"
}
```


### [2026-09-14T00:55:34.943Z] TOOL RESULT

```
MON_part1.txt 'شکك شده و رنگ\u200cهای آمیخته \nبا آب و مواد چسبنده» که به وسیلةٌ قلم موی \nمخصوص به روی کاغذ یا پارچة ابریشمی \nکشند» آب رنک؛ مق مارت 3 رون \nسیاه\u200cقلم. (نق.) پرده\u200cای که با آب و رنگ \nنقاشی شده باشد؟ آب رنگ. سصدی و \nسرخی جهره» رونق و جلای صورت: \nخوش آب و رنگه» بد آب و رنگ. رنگ \n2 رو. \n\nآب\u200cوگل: اه-30-0 (امر.) سنا ساختمان. \nزمین» ملکث. آب و گل در جایی داشتن: \n'
MON_part1.txt count 118
MON_part2.txt 'لی» » غشاء مخی عظام (ل.)؛ ج. اغشبه. \nغشاء: (ع. ف. غشا] (.) (بز.) ردو \nپوششی حول و درون برخی اندام\u200cهای \nدرونی و قسمت سطحی سیتوپلاسم \nسلول\u200cهای حیوانی و پردهٌ سلولری حول \nسلول\u200cهای گیاهی. غشاء جنب: (پز.) شامة \nشش را گویند که از خارج هر یک از شش\u200cها \nرا پوشانده است و عبارت از یکك برده دو \nلایه است که در بين این دو لایه ممکن است \nکاهی ترشحات و سروزیته جمع'
MON_part2.txt count 76
```


## [2026-09-14T00:55:43.774Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pel-",
 "prompt": "List the distinct PIE roots spelled *pel- on this page and their meanings, especially any meaning \"to cover, wrap, hide, cloth\" and any meaning \"flat / to spread\". For the \"cover, wrap\" root list the descendants including Proto-Iranian and Persian forms."
}
```


## [2026-09-14T00:55:45.931Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%B7",
 "prompt": "Is there a Sanskrit entry पट (paṭa) 'woven cloth'? Give its etymology and what Mayrhofer or other sources say about its origin (Indo-Aryan vs Dravidian/non-IE)."
}
```


### [2026-09-14T00:55:47.584Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T00:55:52.241Z] TOOL RESULT

```
# Proto-Indo-European Root *pel-

## Distinct Roots and Meanings

The page documents **five distinct homonymic roots** spelled *pel-:

1. **"to cover, wrap"** - with related meanings of skin, hide, cloth
2. **"to fold"**
3. **"to beat, push, drive"**
4. **"flour, dust"** (possibly from beating)
5. **Alternative reconstruction** of *pelH- (pale, gray)

## Root: "Cover, Wrap, Hide, Cloth"

The first root is defined as: *"to cover, to wrap"* and *"skin, hide, cloth."* This root produced extensive descendants across Indo-European languages.

### Key Descendants

**Proto-Iranian and Persian forms:**
- Proto-Iranian: *\*frakah* (via extension *\*pl-okos*)
- Classical Persian: *پر* (-pirr)
- Iranian Persian: *پر* (-per(r)), *پل* (-pel, "-fold")

**Other notable descendants include:**
- Proto-Germanic: *\*fellą* (skin, hide)
- Latin: *pellis* (skin)
- Ancient Greek: *πέλμα* (pélma, sole of foot)

The root demonstrates widespread attestation across ancient and modern language families, illustrating its foundational role in Proto-Indo-European vocabulary.
```


## [2026-09-14T00:55:55.808Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%9F",
 "prompt": "Sanskrit पट (paṭa): give the meanings and the full etymology section, including any statement about non-Indo-Aryan / Dravidian / Munda origin, and any link to PIE *pel- 'cover'."
}
```


## [2026-09-14T00:55:56.989Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/platinum",
 "prompt": "Give the etymology of platinum, including Spanish platina, plata, and any Greek platys link; also mention French platine if present."
}
```


### [2026-09-14T00:56:02.545Z] TOOL RESULT

```
# Sanskrit पट (paṭa)

## Meanings

The Sanskrit noun paṭa (masculine a-stem) means "garment" or "piece of cloth."

## Etymology

The entry notes the origin is "uncertain." It presents two main theories:

**Indo-European Theory:** "Usually derived from Proto-Indo-Aryan *paḷṭas, undergoing Fortunatov's law from Proto-Indo-Iranian *paltas...from Proto-Indo-European *pol-to-s, from *pel- ('to cover, wrap; hide, cloth')." This would make it cognate with Proto-Slavic *poltьno and Ancient Greek péltē (small leather shield).

**Alternative Origin:** The entry acknowledges an alternative possibility: "Alternatively, borrowed from a presumably Southeast Asian substrate."

The etymology tree illustrates the Indo-European connection, linking the term through PIE *pel- to the concept of covering or concealment, which connects to the cloth/garment meaning.
```


### [2026-09-14T00:56:02.892Z] TOOL RESULT

```
# Etymology of Platinum

The word "platinum" originates from Modern Latin (1812), derived from Spanish *platina*, which is a diminutive of *plata* meaning "silver." The Spanish term traces back to Old French *plate* or Old Provençal *plata*, both meaning "sheet of metal."

## Language Connections

**Spanish origins:** Spanish *plata* ultimately comes from Romance language sources describing metal sheets, and interestingly, "the cognate in Spanish...has become the usual word for 'silver.'"

**Greek connection:** The ultimate root connects to Greek *platys*, meaning "flat, broad," which derives from the Proto-Indo-European root *\*plat-* meaning "to spread."

**French:** While the content traces the word through Old French *plate* as an intermediary source, it does not mention a separate French term *platine*.

## Historical Context

The metal was "first obtained from Spanish colonies in Mexico and Colombia, brought to Europe in 1735, and identified as an element 1741." Spanish discoverers initially mistook it for inferior silver, hence the diminutive name. The modern English form with the *-ium* element ending was adopted in 1812 during systematic standardization of element names.
```


## [2026-09-14T00:56:08.171Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AE",
 "prompt": "Persian فراخ (farâx): give the etymology — Middle Persian form, Old Iranian/Avestan antecedent, and any cited authorities."
}
```


## [2026-09-14T00:56:09.404Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/plastic",
 "prompt": "Give the etymology of plastic (and plasma if mentioned): Greek plastikos / plassein, Latin plasticus, French plastique, and PIE root cited."
}
```


### [2026-09-14T00:56:12.774Z] TOOL RESULT

```
# Etymology of Persian فراخ (farâx)

**Middle Persian form:** The word derives from Middle Persian plʾhw' (/⁠frāx⁠/), meaning "large, wide, spacious, ample, prosperous."

**Old Iranian antecedent:** It traces back to Proto-Iranian *fráθah, which ultimately comes from Proto-Indo-Iranian *prátʰas and Proto-Indo-European *pléth₂os.

**Cited authority:** The dictionary references "Hayyim, Sulayman (1934), New Persian–English dictionary, Teheran: Librairie-imprimerie Béroukhim" as a source for this lexical entry.

The etymological chain shows this Persian adjective (meaning wide, spacious, or plentiful) has ancient roots extending back through multiple language family stages.
```


### [2026-09-14T00:56:15.135Z] TOOL RESULT

```
# Etymology of Plastic and Plasma

## Plastic

**Adjective (1630s):** From Latin *plasticus*, derived from Greek *plastikos* meaning "fit for molding, capable of being molded into various forms." The Greek term stems from *plastos* (molded, formed) and *plassein* (to mold).

**Noun (1905):** Originally referred to "solid substance that can be molded," particularly dental molds. The modern sense of synthetic petroleum-based material emerged by 1909.

## Plasma

From Late Latin *plasma*, rooted in Greek *plasma* meaning "something molded or created." The Greek term derives from *plassein* (to mold), which ultimately traces to the Proto-Indo-European root *\*plath-yein*, itself descended from *\*pele-* meaning "flat; to spread."

The medical sense—"the liquid part of blood"—appeared in 1845, while the physics definition ("ionized gas") emerged by 1928.

## PIE Root Connection

Both terms share connection to *\*pele-* (2), the foundational Indo-European root denoting flatness and the action of spreading or molding material.
```


## [2026-09-14T00:56:23.018Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%D9%87\" \\\n \"https://www.etymonline.com/word/purdah\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pel-\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%9F\" \\\n \"https://www.etymonline.com/word/platinum\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AE\" \\\n \"https://www.etymonline.com/word/plastic\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 391, root Pele/Plat: pardeh, purdah, farāx, plastic/platinum chains\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T00:56:26.823Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c87c917d4a0483db.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4296901ec66746d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec57e984b5fefcdd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aaa6764933066cc4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3de1334c17a4a6e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06fc06c3b29ac3a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4495a5b32de3089f.txt
```


## [2026-09-14T00:56:43.446Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### NYB pardag\"; grep -n \"pardag\\|pltk\" NYB_vol2_glossary.txt | head -5; echo \"### PHD frax\"; grep -n \"frāx\\|fr’x\\|plʾhw\" PHD.txt PHD_mackenzie.txt | head -5; echo \"### SKT flat/plate\"; grep -n \"^flat (1)\\|^flat,\\|^plate,\\|^plain,\" SKT.txt | head -8; echo \"### LEW planus palma plattus\"; grep -n \"plattus\\|^planus\\|^palma\" LEW_1910.txt | head -8",
 "description": "Batch local greps 1"
}
```


### [2026-09-14T00:56:43.545Z] TOOL RESULT

```
### NYB pardag
2743:nipartak [npltk'] brave, excellent 316, 16", — NP nabardah ‘warlike, brave’, navard ‘worthy, excellent’.
### PHD frax
PHD.txt:343:~ih: plenty, prosperity. e frāxēnīdan, früxén- [pP hwyn-ytn!] enlarge, make prosper.
PHD.txt:3261:prosper walidan; make ~ frāxēnīdan, padéxénidan.
PHD.txt:3262:prosperity ābād(ān)īh, bahrómandih, drod, frāxīh, padéxih.
PHD.txt:4697:frahang fraxih frixén- frāxēnīdan frahangestān frāx parahém frahanj- frayad- frayadidan frayad
### SKT flat/plate
### LEW planus palma plattus
```


## [2026-09-14T00:56:46.393Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD band3 index\"; grep -n \"pelə\\|plat-\\|plā-\" WLD_band3.txt | head -10; echo \"### RCH parda\"; grep -n \"pardah\\|parda,\" RCH.txt | head -5; echo \"### PLA barda\"; grep -n -i \"barda\\|برده\\|پرده\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10; echo \"### AFM parda\"; grep -n \"پرده\\|برذعة\\|بردعة\" AFM.txt | head -10",
 "description": "Batch local greps 2"
}
```


### [2026-09-14T00:56:46.552Z] TOOL RESULT

```
### WLD band3 index
### RCH parda
18584:p   btpardahj  Without  a   veil  or  curtain  ;   open,  exposed, p   bt  parted^  Without  fear,  scruple,  or  reflection.  Intre- pid. To  be  bold,  to  have  no  fear  or  hesitation.
19759:*"  pttfduh,  A   veil,  curtain,  tapestry,  cawl,  film,  inenibratie. A   partition  between  two  rooms.  A   fence  or  wall  for  dividing fields.  A   plait,  a   fold.  A   musical  tone  or  sound,  a   note.  The key  of  an  organ,  harpicliord,  or  similar  instrument.  Frets,  or divisions  upon  the  neck  or  finger-board  of  a   guitar  or  lute.  The walls  of  a   tent.  Modesty.  parda-i  iihan,  The  firma- ment. pardah  burdan,  'I'o  seize.  To  ravish.  iJy
19767:Sfftlhdn^  and  Jjltx  parda^i  ^Hshshdk^  Names  of'ihree  sorts of*  musical  airs,  pardah  khdkl  kardan^  To  dis- close, to  reveal,  parda-i  khurram^  A   note  in  music*
19775:o/Atf’  g/V^vy,  The  fourth  Jieaveii.  pardah  kamarl^
19780:1.^  ubV  kdrdn-pardah,  A   raiii-miibrella,  a   parapluic. iiijJ  divcar-purdtth,  The  veil  or  membrane  of  the  wall,  tapestry. 4.^  JA.  maghz-pardtth,  The  pia  mater.  Purdah,  An  enigma.
### PLA barda
6649:»Le- Yarädig: Pl. v. Syp Bardaq s. Sardag. 
6650:Le - Zarädig: Pl. v. 3y>%fardag s. Bardaq. 
6763:I2.- Bardagq: dünner Kuchen" aus dem pers. oJ garde <Imp. d» gird 
6764:a3> - $ardaga: nom. un. v. Bardaqg q. v. 
6769:&ye- Sardaqg = Bardag s. Bardag. 
10687:zabardag 141 zarbi 
10690:&2+, - zabardaß = zabarfad a. v. 
### AFM parda
```


## [2026-09-14T00:56:55.470Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^field,  n\\.\" \"^floor,  n\\.\" \"^flat,  adj\\.\" \"^palm,  n\\.\" \"^plate,  n\\.\" \"^plasma,\" \"^platinum,\" \"^planet,\" ; do echo \"### $w\"; grep -n \"$w\" KLN_1966.txt | head -2 | cut -c1-900; done",
 "description": "Klein entries batch"
}
```


### [2026-09-14T00:56:56.634Z] TOOL RESULT

```
### ^field,  n\.
### ^floor,  n\.
14968:floor,  n.  —  ME.  flor,  fr.  OE.  flor,  rel.  to  MDu., Du.  vloer,  ON.  flor ,  ftorr,  Norw.  flor,  ‘floor  of a  cow  stall’,  MHG.  vluor,  G.  Flur,  ‘field,  mead¬ ow,  plain,  floor’,  fr.  I.-E.  base  *pldros,  *pldra , whence  also  OIr.  lar  (for  *plar),  W.  llawr,  Bret. leur,  ‘ground,  floor  .  This  base  is  an  enlarge¬ ment  of  base  *p(e)la-,  ‘spread  out,  broad,  fiat’, whence  L.  planus,  ‘level,  flat’.  See  plain,  adj., and  cp.  words  there  referred  to.
### ^flat,  adj\.
### ^palm,  n\.
27036:palm,  n.,  a  tropical  tree.  —  ME.  palme,  fr.  OE. palm,  fr.  L.  palma,  ‘palm  tree’,  orig.  identical with  palma,  ‘palm  of  the  hand’ ;  so  called  from the  flatness  of  its  leaves.  See  prec.  word  and  cp. palmetto,  palmitic.
### ^plate,  n\.
### ^plasma,
29057:plasma,  also  plasm,  n.,  1)  the  liquid  part  of  blood; 2)  the  protoplasm.  —  Late  L.,  fr.  Gk.  irXaaiAX, ‘something  molded',  fr.  TiXdcaastv,  ‘to  mold, form,  model’.  Cp.  -XocOavov,  ‘mold  in  which bread  or  cakes  are  baked',  and  the  second  ele¬ ment  in  v.opuTtXxfl o',  ‘modeller  of  small  fig¬ ures'.  Cp.  also  plasson,  plaster,  plastic,  plastid, plastron.
### ^platinum,
29088:platinum,  n.  —  ModL.,  fr.  earlier  platina,  fr.  Sp. platina  in  platina  del  Pinto,  i.e.  ‘little  silver  of  the River  Pinto’;  so  called  because  of  its  silver- white  color  and  because  it  was  first  found  near the  River  Pinto.  Sp.  plata  comes  either  fr. OProvenc.  plata  or  fr.  OF.  plate,  which  mean ‘sheet  of  metal’,  and  ult.  derive  fr.  Gk.  rcXaxuc, ‘flat,  wide,  broad’.  See  plate  and  cp.  platina.  Cp. also  plateresque.
### ^planet,
```


## [2026-09-14T00:57:02.402Z] TOOL CALL #59: Bash

```json
{
 "command": "pdftoppm -f 391 -l 391 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391.png",
 "description": "Render PDF page 391"
}
```


### [2026-09-14T00:57:04.193Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81140 Sep 13 20:57 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391.png
```


## [2026-09-14T00:57:05.923Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391.png"
}
```


### [2026-09-14T00:57:06.370Z] TOOL RESULT

```

```


## [2026-09-14T00:57:06.364Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:57:27.544Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 391 -l 391 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg391big && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg391big.png'); print(im.size)\nim.crop((700,550,2500,1100)).save('pg391crop.png')\n\"",
 "description": "Crop the pardeh region"
}
```


### [2026-09-14T00:57:30.531Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-14T00:57:32.863Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391crop.png"
}
```


### [2026-09-14T00:57:32.886Z] TOOL RESULT

```

```


## [2026-09-14T00:58:00.816Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg391big.png')\nim.crop((700,400,1750,570)).resize((2100,340)).save('pg391root.png')\nim.crop((880,1180,1620,1340)).resize((1480,320)).save('pg391sog.png')\n\"",
 "description": "Crop root and Sogdian boxes"
}
```


### [2026-09-14T00:58:02.272Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:04.686Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391root.png"
}
```


### [2026-09-14T00:58:04.805Z] TOOL RESULT

```

```


## [2026-09-14T00:58:04.800Z] INPUT

[Image: original 2100x340, displayed at 2000x324. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-14T00:58:13.519Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^paita\\|paita\\b\\|paitā\" IEC.txt | head -10; echo \"=== CEL abbrev in Nourai?\"; grep -rn \"\\\"CEL\" /home/sfmqrb/git/rishe/data/verification/sources/refs_online.json | head -5",
 "description": "Search IEC paita and CEL2"
}
```


### [2026-09-14T00:58:13.590Z] TOOL RESULT

```
=== CEL abbrev in Nourai?
/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json:837: "CEL": {
```


## [2026-09-14T00:58:16.385Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['CEL'],ensure_ascii=False)[:900])\"",
 "description": "CEL reference info"
}
```


### [2026-09-14T00:58:17.658Z] TOOL RESULT

```
{"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Haus printing is not digitised anywhere found. HathiTrust full-text search (search-only volumes) can confirm whether a word occurs, via a browser."}
```


## [2026-09-14T00:58:17.943Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391sog.png"
}
```


### [2026-09-14T00:58:17.966Z] TOOL RESULT

```

```


## [2026-09-14T00:58:27.241Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nfor i in range(860,880):\n    nums=re.findall(r'(?m)^\\s*(8[0-9]{2})\\s*$', leaves[i])\n    print(i,nums[:3], leaves[i][:90].replace('\\n',' '))\nEOF",
 "description": "Ernout-Meillet p.853"
}
```


### [2026-09-14T00:58:28.354Z] TOOL RESULT

```
leaves 1409
860 [] pala 843 - Bati sur castrensis, pacensis , apparait en baa latin un adj. pagens is (Greg.,
861 [] - 043 “ Pales "Pfingstvogel" merle dore); tout ceci, tres incertain. palasea (plasea) : no
862 [] palla 844 - palla, — ae f.: grande mantille de femme, formae d*une piece d'4toffe oblongue
863 [] - 845 “ palpebrae bras. - Ancien (Pl.), usuel, class. Panroman. M.L.6170,6171. Celt.: iri.
864 [] palpor - O4.fi - palpor, -aris (et palpo, -as) , -ari: toucher legerement de la main, tapo
865 [] - 047 " pando cf. Vc 5 g.Mil. 1,11 : depsis, -Ss: d^limiter avec des pieux (tardif), et in
866 ['848'] pangB 848 Derives et composes en pand- et en pass-i pandus, -a, -um (est a pandt), comme -
867 [] -049 pannus ornamenta quae antis adpinguntur, i. e. adfiguntur', compingo (et dans les glo
868 [] pansus - 850 - Nom techuique et familier, sana correspondant net. V.sl . opona "rideau" n'
869 [] - 8 S i - pSr Tenne expressif sans itymologie claire. papilla: v. papula. pappa, -ae: mot 
870 [] parabola - 85» - par est - aequom est. Ancien, usuel. Panroman, sauf roumain. M.L. 0 %ig, 
871 [] - 853 “ p*re 8 Sid.). Peut-etre celti que. Senble sana rapport ayec 1 'iranien *partaka- "
872 [] pardus - 854 - ^galement lea compoaea de aena divergenti dont la langue ne recon naissait 
873 [] - 855 ~ pari es visible (sens physique et moral); apparet "il est visible [que] "j *' sens
874 [] Parilia - 856 - Cf. aussi *pariet 5 na, M.L.6343. Aucun rapprochement net. II est tentant 
875 [] - 857 - pare indo-europ4en; le groupe de gignO, nascor a. un caractbre juridicae et aocial
876 [] parochia - 858 disparSsca (Claud., Mam.), britt. disperod-, impera (v. ce mot); praeparo- 
877 [] - 859 ~ paruus populaire, partes populares, par opposition a factio , la caste noble. Usit
878 ['860'] pasceolus 860 du subst. derive paruitas qui semble bien cree d'apres p,UJtpoxriC. — Attest
879 [] - 86i pataracina d* engraisser, de nourrir".Les deux fora ea *p5- de pOscG, pOul, pabulum,
```


## [2026-09-14T00:58:35.178Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt=open('LAT.txt',encoding='utf-8',errors='replace').read(); l=txt.split('\\f')\nprint(l[870][-1200:]); print('=========871========='); print(l[871][:3000])\"",
 "description": "Read Ernout-Meillet p.852-853"
}
```


### [2026-09-14T00:58:36.290Z] TOOL RESULT

```
oque imperiale (Val.
FIacc., Stace, Prud,, So 1. ), avec le sens de dispar, est une forme
reconstruire sur sSparo, rattache faussement k par. Cf. encore M.L.
S 39 apparium.
Sur aequipero, aequipar, v. aequus, sub fin.
fitymologie inconnue. Il n'y a pas de terme indo-europeen connu
pour "egal". On songe k la famille de pario (v. ce mot), paro, pars.
Mais le sens reste a expliquer. L'ombrien a pars est "par erit".
parabola, ae f. : - 7ictpapoXr|. D*abord simplement transerit du
grec sons la forme parabole, puis emprunte par la langue de la rhe¬
torique dans le sens de "comparaison" (Quint., sen.), apparalt dans
lal.de l ? figlise avec le sens de "parabole", "proverbe", et, dans
la Vulgate, avec celui de "parole", assumpta parabola "ayant pris
la parole" (e.g. Num.33,7), qui est demeure dans les 1. romanes, ou
(sauf en roumain) parabola a supplante uerbum, grace k la frequence
et a 1'importance de son emploi dans la langue religieuse, et aussi
k cause du sens de uerbum dans cette meme langue. Cf.M.L. 62331 et
62%% parabolare. Iri. parabail (mot savant).
D4riv<?s: parabolice-, parabolo,-Us (- lor ); -bolarius, tardifs.
parada, -ae f. : rideau, tente d'un vaisseau. Rare et tardif (Aus.,
=========871=========
- 853 “ p*re 8
Sid.). Peut-etre celti que. Senble sana rapport ayec 1 'iranien *partaka-
"rideau", pera .parda, eaprunt 4 par 1 'ara 4 nien ( partak) et le syriaque
dans lequel le Sena de "rideau" doit fctre le rdaUltat d'une sp 4 cia-
liaation secondaire, le sena preaier devant etre "diyision".
paradisus, -ia.: pare. Eaprunt de la 1. de 1' igl.au gr. 7capa6eioo£
(aot d'origine iranienne), vulgaris 4 par lal.de 1 'Sglise, et pass 4
par li dans lea 1 . roaanea, M.L.6aaa. Celt.s iri. pardus, britt .para-
dwys . D 4 riv 4 s et compos 4 s: paradisiacus, paradlsicola.
paragauda (et paragaudis),- ae f.: bordure de v£teaent d'or ou
de aoie dor 4 e; paragaude, yfeteaent orn 4 de cette bordure. Baa latin;
aot 4 tranger; perae, ▼. Hubschaann, Arn. Gramm ., p.ae 7 , n* 530, renu en
latin par le grec. D 4 riv 4 s: paragaudius, -diStUs.
paramus, -I a.: plateau (CE 1536 C3). Mot 4 tranger, sana do ut e
eapagnol. M.L.Caa8.
parasitus, -I a.: parasite. Mot de la coa 4 die, eaprunt 4 au gr.
TOXpoim toC; lati ni s 4 . Dlriy 4 s: parasita f. (Hor., Plin.), parasitor, -Sris
(Viante), parasiticus) parasitaster (T 4 r.). ,
paratragoedfi, -Ss: prendre dea airs tragi quos. Cr 4 ation de Plaute,
d* aprbs le gr.TcapaxpaYpSao.
paraueredus: y. ue rSdus . ✓
Parca (usit 4 aurtout au pl. Parcae), -ae f.: la Parque, nou g 4 n 4 -
rique dea d 4 eaaea eharg 4 es de filer la destinae de chaque aortel (leura
noaa particuliers aont M 5 na, Decuma, Horta, correspondant aux noaa
des d 4 esses grecques ClUthU, Lachesis et Atropos ).
Rattach 4 par Varron k pariS, cf. Geli.3,16,ysqq,, 4 tyaologie g 4 n 4 -
raleaent adaise par lea aodernes.
parcC, -Is, peperci (claas., Cic., C 4 a.j fora es secondaires parsi,
notaaaent arec pr 4 yerbe, comparsit chez T 4 rence, et' parcui, Naey.,
d r aprbs arcui), parsum et parcltum (pcp.fut. par surus T.L. parciturus
S*-J 4 r. j et aeae k basse 4 poque pepertuu, pepercitum), parcere: aena
preaier "retenir, contenir" (trans.) encore attest 4 dans 1 'expression
rituelle conaeryde par P.F.a49,i, parcito linguam in sacrificiis
dicebatur, i.e, coerceto, contineto, taceto) cf. Plaute Hi.xaao parce
uocem et Poe.1035 linguam compescas . Sp 4 cialis 4 dans le sene absolu
de "se contenir, ae retenir", parce pias scelerare manus Vg., Xe.3,49)
puis "se contenir (en faveur de quelqu'un ou de quelque cbose), 4 par-
gner, a 4 nager" (sui vi du datif, p. alicui et k basse 4 poque, p.db,
d'aprbs abstinere ab). Usit 4 de tout teaps. Conserv 4 sCui eaent en
proyenyal. M.L.6a3ia.
D 4 rir 4 s etcompos 4 s: parcus : a 4 nager, 4 conome; et lea coapoa 4 s ex—
pressifs deparcus (Su 4 t.), praeparcus (Pl.), perparce (T 4 r.); parsi¬
monia, -mSnium (parci-), et k 1 ' 4 poque irip 4 riale parcitds) imparcenter
(tardifs) parciloquium (Apul.), parciprornus (Pl.); parcitor, parcitUdd
(tardifa); parsiS (d.).
compercS,-is (compar-)) cf.P.F. $9,36, comparsit Terentius (Ph.44)
pro compescuit posuit : a'abstenir de, 4 pargner; impercS (Plaute)j
reparcS (rare).
A la a£ae racine, mais ayec u
```


## [2026-09-14T00:59:32.141Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T00:59:32.178Z] TOOL RESULT

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


## [2026-09-14T00:59:40.003Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg391.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/391.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/391.png",
 "description": "Save page PNG for audit"
}
```


### [2026-09-14T00:59:40.067Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81140 Sep 13 20:59 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/391.png
```


## [2026-09-14T01:11:57.175Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-391.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nWIKT_PARDE = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AF%D9%87\"\nWIKT_PEL = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pel-\"\nWIKT_PATA = \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%9F\"\nWIKT_FARAX = \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D8%AE\"\nETY_PURDAH = \"https://www.etymonline.com/word/purdah\"\nETY_PLATINUM = \"https://www.etymonline.com/word/platinum\"\nETY_PLASTIC = \"https://www.etymonline.com/word/plastic\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Iranian\", \"words\": \"partaka\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Old/Middle Iranian *partaka- 'curtain' is real and well attested indirectly: Ernout-Meillet, the very page Nourai cites for the Persian box (LAT p.853 s.v. parada), writes \\\"l'iranien *partaka- 'rideau', pers. parda, emprunté par l'arménien (partak) et le syriaque\\\" — i.e. Iran. *partaka- gave NP parda and was borrowed into Armenian partak and Syriac pardəqā. What is disputed is the parent drawn here. Nourai hangs *partaka- on PIE *pelə-/*plā- 'wide and flat' (Pokorny 805). Modern handbooks do not: Wiktionary derives MP pardag < PIE *pel- 'to cover, wrap; hide, cloth' (Pokorny's pel- 3b, p.803 = AHD pel-4 'skin, hide'), a homonymous but distinct root; Etymonline instead analyses the word as Old Persian *pari-dā- 'to place around' (*per- + *dheh1-); and Ernout-Meillet say outright that the primary sense of the Iranian word \\\"devant être 'division'\\\", not 'flat surface'. Nourai's authority is Mann (IEC 918), who files Skt paṭaḥ and Per. parde under *pelt- (1) 'wrap, cloak, cover, screen' and then asks, of his *pelt- (2) 'flat surface', \\\"(Same as (1)?)\\\" — a query Nourai has silently turned into an identity. The form itself: *part-aka-, a -ka- derivative, gives MP pardag by the regular Middle Iranian voicing of intervocalic/post-r *-t- > -d- and of *-ka > -ag.\",\n \"derivation_fa\": \"صورت ایرانی باستان/میانهٔ *partaka- «پرده» خود واقعی است؛ ارنوـمیـه در همان صفحهٔ ۸۵۳ که نورایی ارجاع داده، می‌نویسد «ایرانی *partaka- به معنی پرده، فارسی parda، وام‌گرفته در ارمنی partak و سریانی». اما انتساب آن به ریشهٔ هندواروپایی آغازین *pelə-/*plā- «پهن و صاف» (پوکورنی ۸۰۵) پذیرفته نیست: ویکی‌واژه آن را از ریشهٔ هم‌آوای دیگری *pel- «پوشاندن، پیچیدن؛ پوست، پارچه» (پوکورنی ۸۰۳) می‌گیرد و اتیمون‌لاین آن را مرکب پارسی باستان *pari-dā- «پیرامون نهادن» می‌داند؛ ارنو-میه نیز معنای نخستین آن را «جداسازی/بخش‌کردن» می‌داند نه «پهنی». مأخذ خود نورایی (من، ص ۹۱۸) پرده را ذیل *pelt- «پوشش، پرده» آورده و یکی بودن آن را با *pelt- «سطح صاف» فقط با علامت پرسش مطرح کرده است. از نظر آوایی، *part-aka- با نرم‌شدن t پس از r و تبدیل *-ka > -ag به فارسی میانهٔ pardag می‌رسد.\",\n \"sources\": [WIKT_PARDE, WIKT_PEL, ETY_PURDAH],\n \"ref_check\": [\n   {\"ref\": \"IEC:918\", \"status\": \"partial\", \"note\": \"Mann, IEC p.918 (leaf 510 of IEC.txt): 'pelt- (1) „wrap, cloak, cover, screen“. (Indo-Iran. ambig. Cf. prtos) Skt. paṭaḥ, m. „cloth, garment, screen, canvas“ ...; Per. parde „veil, curtain“; ON feldr ... See next' — followed by 'pelt- (2) (Same as (1)?) „space, patch, flat surface“'. Mann has the word, but under a 'cover/screen' root and with the identification with the 'flat' root marked as a question. He gives no Iranian *partaka- form.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"p.853 s.v. parada (LAT.txt leaf 871)\", \"stance\": \"supports\", \"note\": \"'Semble sans rapport avec l'iranien *partaka- „rideau“, pers. parda, emprunté par l'arménien (partak) et le syriaque, dans lequel le sens de „rideau“ doit être le résultat d'une spécialisation secondaire, le sens premier devant être „division“.' — confirms the Iranian form *partaka- and the Armenian/Syriac loans, but assigns it a 'division' not a 'flat/spread' semantics.\"},\n   {\"src\": \"POK\", \"where\": \"pp.805-807 pelə-, plā- (POK_full.txt 'Page(s): 805-807')\", \"stance\": \"silent\", \"note\": \"Pokorny's pelə-/plā- 'wide and flat' lists Armenian hol, Lat. palam, Gk. plāssō, Germanic feld/flōr, Slavic polje — no Iranian 'curtain' word at all; *partaka- is absent from the entry Nourai cites for the root.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss, no entry\", \"stance\": \"silent\", \"note\": \"grep 'parda|perde' in HRN.txt returns only bergj. perdele 'Häutchen' (no. 929 Anm.); Horn has no headword for parda.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"pardeh «پرده»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP پرده pardeh 'curtain, veil, screen' continues MP pardag [pltk'] without complication: MP final -ag > NP -a/-e (pardag > parda > mod. Tehrani parde), exactly as خانه < xānag. The word is Ferdowsi-old (the chart's own شاهنامه line طلایه ز هر سو برون تاختند / به هر پرده‌ای پاسبان ساختند) and productive: the extras پرده‌دار 'chamberlain', سراپرده 'royal pavilion', پردگی 'one behind the curtain, harem woman' are regular Persian compounds/derivatives. The chart's NOTE ('LKT:131 claims this has reached Europe through Arabic') is a fair, if compressed, summary of Lokotsch: his no. 1630 routes Pers. pärdä into Europe through Turkish perde (Bulg. perde, Serb. perde, Rum. perdea) and then adds 'Hieraus wurde auch ar. barda'a', and his no. 228 takes Ar. bardaʿa 'saddle-cloth' (after I. I. Hess, from Pers. pärdä with infixed ʿayn) into It. barda, Fr. barde, Sp./Pg. albarda. So the Arabic route is real but delivers barde/albarda, not purdah; the Balkan perde came via Turkish; and Lokotsch himself allows that the Arabic word may instead be Turkic (Azeri burunduk). Caution: the printed chart connects this box by a plain line to the Pahlavi box, i.e. NP pardeh < MP pardag; the JSON records parent #1 (Iranian).\",\n \"derivation_fa\": \"«پرده» در فارسی نو دنبالهٔ بی‌واسطهٔ فارسی میانهٔ pardag [pltk'] است؛ پسوند پایانی -ag فارسی میانه در فارسی نو به -ه بدل می‌شود (مانند xānag > خانه). واژه از روزگار فردوسی گواهی دارد و مشتقات آن (پرده‌دار، سراپرده، پردگی) ساخت‌های قاعده‌مند فارسی‌اند. دربارهٔ یادداشت کتاب («لوکوچ می‌گوید از راه عربی به اروپا رسیده»): لوکوچ در شمارهٔ ۱۶۳۰ راه اصلی را از طریق ترکی perde به زبان‌های بالکان می‌داند و تنها می‌افزاید که عربی bardaʿa «زیرانداز زین» نیز از همین واژه است (شمارهٔ ۲۲۸) که ایتالیایی barda و اسپانیایی albarda از آن برآمده‌اند. پس راه عربی وجود دارد اما به صورت barde/albarda و نه purdah. ادعای نورایی دربارهٔ خود واژه درست است.\",\n \"sources\": [WIKT_PARDE, ETY_PURDAH],\n \"ref_check\": [\n   {\"ref\": \"LAT:853\", \"status\": \"supports\", \"note\": \"Ernout-Meillet p.853, s.v. parada 'rideau, tente d'un vaisseau': '... Semble sans rapport avec l'iranien *partaka- „rideau“, pers. parda, emprunté par l'arménien (partak) et le syriaque ...' — the page does carry Pers. parda and its Iranian etymon, exactly as Nourai's citation implies (the Latin word parada itself is ruled out as a relative).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1630 (printed p.132, LKT.txt leaf 159) and no. 228 (leaf 46)\", \"stance\": \"partial\", \"note\": \"1630: 'Pers. pärdä: „Vorhang“, tk. ebenso perde; hieraus bulg. perde ..., serb. perde ..., rum. perdea ... Hieraus wurde auch ar. barda'a, s. hier Nr. 228.' 228: 'Ar. barda'a: [Nach I. I. Hess aus pers. pärdä „Teppich“ mit infigiertem 'Ain] ... hieraus ... it. barda ..., frz. barde ..., sp. pg. albarda.' Lokotsch's European route is via Turkish; the Arabic route yields barda/albarda only, and he concedes the Arabic word may be Turkic instead. Printed p.131 (leaf 158) ends with no. 1628, so Nourai's 'LKT:131' is one page early.\"},\n   {\"src\": \"RCH\", \"where\": \"Richardson-Johnson s.v. pardah\", \"stance\": \"supports\", \"note\": \"'pardah, A veil, curtain, tapestry, cawl, film, membrane. A partition between two rooms. ... A musical tone or sound ... Modesty.' — the full classical range of the Persian word, incl. the 'partition/division' sense Ernout-Meillet call primary.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, no entry\", \"stance\": \"silent\", \"note\": \"grep 'parda|perde' in HUB.txt gives only no. 297 pardaxtan and Pahlav/Pardava-; Hübschmann does not treat parda.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep 'barda|پرده' in PLA_asbaghi_1988_ia_djvu.txt returns only bardaq/بردق (< pers. garde) and zabardag — Asbaghi has no entry deriving an Arabic word from پرده, so Lokotsch's bardaʿa is not corroborated there.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"pardag\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary p.64 has exactly 'pardag [pltk' | N parda] veil, curtain' — Book Pahlavi spelling pltk', reading pardag, with the New Persian continuation explicitly given. The form is the expected Middle Iranian reflex of *part-aka-: post-consonantal *-t- voiced to -d- after r, and the productive adjective/noun suffix *-aka > -ag. Its antiquity outside Persian is guaranteed by the Middle Iranian loans into Armenian (partak) and Syriac (pardəqā) recorded by Ernout-Meillet and Wiktionary, which preserve the -t-.\",\n \"derivation_fa\": \"مکنزی در فرهنگ کوچک پهلوی، ص ۶۴، عیناً می‌آورد: pardag [pltk' | N parda] «پرده، حجاب». این صورت بازتاب قاعده‌مند ایرانی باستان *part-aka- است: ت پس از ر نرم شده و پسوند *-aka به -ag بدل شده است. وام‌واژه‌های ارمنی partak و سریانی pardəqā که ت را نگاه داشته‌اند، کهنگی صورت ایرانی میانه را تأیید می‌کنند. ادعای نورایی درست است.\",\n \"sources\": [WIKT_PARDE],\n \"ref_check\": [\n   {\"ref\": \"PHD:64\", \"status\": \"supports\", \"note\": \"MacKenzie 1971 p.64: 'pardag [pltk' | N parda] veil, curtain' (PHD.txt line 540; PHD_mackenzie.txt line 4022 'pardag [pltk I N parda] veil, curtain'). The page also has the neighbouring pardaštan/pardāxtan entries, so p.64 is right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep 'pardag|pltk' in NYB_vol2_glossary.txt yields only nipartak [npltk'] 'brave, excellent'; Nyberg's glossary (limited to his selected texts) has no pardag entry, so it neither confirms nor contradicts.\"},\n   {\"src\": \"LAT\", \"where\": \"p.853 s.v. parada\", \"stance\": \"supports\", \"note\": \"'pers. parda, emprunté par l'arménien (partak) et le syriaque' — independent evidence for a Middle Iranian *partak/pardag already in the Sasanian period.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Hindustani\", \"words\": \"pardah\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Hindustani/Urdu पर्दा ٹردہ pardā 'curtain, veil; the seclusion of women' is certainly the Persian word, but it is a New Persian loan of the Delhi-Sultanate/Mughal period, not an inheritance from Pahlavi as the chart's arrow (parent #3) shows. Hobson-Jobson p.744 states it flatly: 'PURDAH, s. Hind. from Pers. parda, „a curtain“; ... whence a woman of position who observes such rules of seclusion is termed parda-nishīn'; Whitworth p.242 likewise tags 'Pardah. [Persian.]'. Persian -a was taken over as Hindi -ā, and the institution (parda-nishīn, gosha-nishīn) is a Persianate court usage carried into India. So: right word, right donor language, wrong stage — read #3 → #2 → #4.\",\n \"derivation_fa\": \"«پرده» در اردو/هندوستانی (pardā) وام‌واژه‌ای از فارسی نو است که در دوران سلاطین دهلی و گورکانیان وارد شده، نه مستقیماً از فارسی میانه چنان‌که نمودار کتاب نشان می‌دهد. هابسن-جابسن (ص ۷۴۴) می‌نویسد: «PURDAH, هندی از فارسی parda» و ویتوورث (ص ۲۴۲) نیز آن را «[فارسی]» برچسب می‌زند. هٔ پایانی فارسی در هندی به آی بلند بدل شده است. پس ادعای نورایی دربارهٔ زبان وام‌دهنده درست است ولی مرحلهٔ زبانی را یک پله بالاتر گرفته است.\",\n \"sources\": [ETY_PURDAH],\n \"ref_check\": [\n   {\"ref\": \"HJB:744\", \"status\": \"partial\", \"note\": \"Hobson-Jobson p.744 (HJB.txt leaf 790, running head 'PUNSAREE. 744 PUTCHOCK.'): 'PURDAH, s. Hind. from Pers. parda, „a curtain“; a portière; and especially a curtain screening women from the sight of men; whence ... parda-nishīn' — supports the word but derives it from New Persian, not from Pahlavi.\"},\n   {\"ref\": \"AID:242\", \"status\": \"partial\", \"note\": \"Whitworth, Anglo-Indian Dictionary p.242 (AID.txt leaf 261, running head 'PARG *43 PARS'): 'Pardah. [Persian.] A veil, a screen, a curtain, especially one used to exclude women from public view.' plus 'Pardahnishin. [Persian nīshīn, who sits.]' — same: Persian, not Pahlavi.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"p.744 s.v. PURDAH, and p.399 s.v. GOSHA\", \"stance\": \"supports\", \"note\": \"GOSHA: 'much the same as parda-nishīn (see PURDAH)' — the Indian institution is described throughout as Persian-derived court usage.\"},\n   {\"src\": \"AID\", \"where\": \"p.242\", \"stance\": \"supports\", \"note\": \"'Pardah. [Persian.]' — Whitworth's square-bracket tag is his source-language label.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"pardah, purdah\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English purdah (also spelt pardah, purda) 'curtain screening women; the system of female seclusion' is an Anglo-Indian borrowing of Hindustani pardā, first recorded 1800 (Etymonline; Hobson-Jobson's earliest quotation is Valentia 1809, 'On the fourth (side) a purdah was stretched across'). Klein p.1273: 'purdah, n., curtain guarding women from public view in India. — Hind. and Pers. pardah, „veil“.' The u-spelling reflects the Anglo-Indian rendering of the short a of Hindi pardā (cf. punkah, pundit); the sense generalised from the physical curtain to the social institution during the 19th c.\",\n \"derivation_fa\": \"انگلیسی purdah وام‌واژه‌ای آنگلوهندی از هندوستانی pardā است که نخستین کاربرد آن به سال ۱۸۰۰ میلادی بازمی‌گردد. کلاین (ص ۱۲۷۳) می‌نویسد: «purdah — هندی و فارسی pardah پرده». نوشتن u به جای a شیوهٔ معمول انگلیسی‌هندی است (قیاس کنید punkah، pundit) و معنا در سدهٔ نوزدهم از «پردهٔ مادی» به «نهاد پرده‌نشینی» گسترش یافته است. ادعای نورایی درست است.\",\n \"sources\": [ETY_PURDAH],\n \"ref_check\": [\n   {\"ref\": \"KLN:1273\", \"status\": \"supports\", \"note\": \"Klein 1966 p.1273 (KLN_1966.txt leaf 678, which carries the running number 1273): 'purdah, n., curtain guarding women from public view in India. — Hind. and Pers. pardah, „veil“.'\"},\n   {\"ref\": \"AHD:1061\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition main-dictionary page; only the Watkins IE-roots appendix (pp.1505-1550) is available locally/openly, the A-Z pages are on lending-only scans.\"},\n   {\"ref\": \"FWE:233\", \"status\": \"not_checked\", \"note\": \"Bliss, A Dictionary of Foreign Words and Phrases in Current English (1966) — refs_online records it as borrowable-only on archive.org, no open copy.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.1273 s.v. purdah\", \"stance\": \"supports\", \"note\": \"'Hind. and Pers. pardah, „veil“'.\"},\n   {\"src\": \"HJB\", \"where\": \"p.744 s.v. PURDAH\", \"stance\": \"supports\", \"note\": \"Quotations 1809 (Ld. Valentia i.100), 1810 (Williamson), 1813 (Forbes 'its purdoe or chintz covering'), 1878, 1900 — documents the English currency of the word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Sanskrit\", \"words\": \"patah\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Sanskrit पट paṭa- m. 'woven cloth, garment, screen, canvas' is real (the chart's 'patah' is the nominative paṭaḥ), but it is NOT a descendant of Iranian *partaka- as the arrow draws it. No handbook derives an Old Indic word from an Old Iranian one here: at most the two are collateral. Mann himself (IEC 918), Nourai's own reference, lists Skt paṭaḥ and Per. parde side by side as co-descendants of *pelt-, flagging 'Indo-Iran. ambig.' Wiktionary's current view: paṭa- is of uncertain origin, 'usually derived from Proto-Indo-Aryan *paḷtas, undergoing Fortunatov's law (*-lt- > retroflex -ṭ-) from Proto-Indo-Iranian *paltas, from PIE *pol-to-s, from *pel- „to cover, wrap; hide, cloth“' — again the 'cover' root, not the 'flat' root — 'alternatively, borrowed from a presumably Southeast Asian substrate'. The retroflex -ṭ- is in fact the strongest argument against a loan from Iranian, where the cluster stayed -rt-/-rd-.\",\n \"derivation_fa\": \"سنسکریت paṭa- «پارچه، جامه، پرده» واژه‌ای واقعی است، اما برخلاف نمودار کتاب برگرفته از ایرانی *partaka- نیست؛ هیچ مرجعی وام‌گیری هندی باستان از ایرانی باستان را در این‌جا نمی‌پذیرد. خود من (مأخذ نورایی) این دو را هم‌ردیف و هم‌ریشه می‌آورد نه پدر و فرزند. ویکی‌واژه ریشهٔ آن را نامطمئن می‌داند: یا از هندوآریایی آغازین *paḷtas با قانون فورتوناتوف (تبدیل lt- به طـ جزری) از ریشهٔ *pel- «پوشاندن»، یا وام‌واژه‌ای از لایهٔ زیرین غیرهندواروپایی. همان طـی جزری بهترین دلیل علیه وام‌گیری از ایرانی است. پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [WIKT_PATA, WIKT_PEL],\n \"ref_check\": [\n   {\"ref\": \"IEC:918\", \"status\": \"partial\", \"note\": \"Mann p.918 s.v. pelt- (1): 'Skt. paṭah, m. „cloth, garment, screen, canvas“ beside paṭalam, n. „cover, basket, hive, cataract on the eye“; Per. parde „veil, curtain“; ON feldr ...' — the two are coordinate members of one root family, and Mann marks the Indo-Iranian evidence 'ambig.'; he nowhere derives the Sanskrit word from Iranian.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pelə-, plā- pp.805-807; pel- 3b p.803\", \"stance\": \"silent\", \"note\": \"The pelə-/plā- entry has no Old Indic 'cloth' word; Pokorny keeps the 'Haut, Fell, decken' family at p.803 separate.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dict. of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"grep for paṭa/pata in SYN.txt does not turn up a discussion of the Sanskrit cloth word under 'cloth' (6.21); no support for an Iranian source.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Sogdian\", \"words\": \"prd`nk, prd`nkh, prthynq\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are copied correctly from Gharib: SOD p.284 = entry 7084 'prδ'nk(h) B, parδang, cf. prδ'ync-, prδynq, „curtain“ (TSP 3.159, 156)' and entry 7254 'prδynq C, parδing, pl. -t, cf. prδynk(h), „curtain“'; Nourai renders Gharib's δ once as 'd' and once as 'th', which is why his third form looks unlike the first two. The Sogdian word is certainly the same lexical family as Persian parda (Sogd. -δ- is the regular post-vocalic/post-r outcome of Old Iranian *-d-/-θ-). But Gharib does not attach it to *partaka-: she cross-refers the nouns to the verb prδ'ync- 'to stretch, spread' (entry 7086), which she derives '< *pari/θa-θanjaya-', i.e. *pari-θanj- 'to draw around'. So the Sogdian evidence is compatible with, but does not prove, the Iranian preform Nourai draws — and if Gharib is right it points to a *pari- compound, which is the analysis Etymonline gives for parda too.\",\n \"derivation_fa\": \"صورت‌های سغدی درست از قریب نقل شده‌اند: ص ۲۸۴، مدخل ۷۰۸۴ prδ'nk(h) = parδang «پرده» و مدخل ۷۲۵۴ prδynq = parδing. نورایی دال توک‌دار (δ) را یک‌جا d و جای دیگر th آورده و از همین رو فهرست ناهماهنگ می‌نماید. واژهٔ سغدی بی‌گمان هم‌خانوادهٔ «پرده» است، اما قریب آن را به فعل prδ'ync- «گستردن، کشیدن» از *pari-θanjaya- بازمی‌گرداند نه به *partaka-. پس این پیکان با احتیاط پذیرفتنی است.\",\n \"sources\": [WIKT_PARDE],\n \"ref_check\": [\n   {\"ref\": \"SOD:284\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, printed p.284 = SOD_pages.txt leaf 350 (leaf − 66), where entry 7084 'prδ'nk(u) B / parδang / ⇒prδ'ync-, prδynq / curtain / TSP 3.159, 156' stands; the companion entry 7254 'prδynq C / parδing / pl. -t / curtain' is p.483. All three forms Nourai prints are on or keyed to p.284.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 7084, 7086, 7254\", \"stance\": \"partial\", \"note\": \"7086 'prδ'ync- B parδenc ©<*pari/θa-θanjaya- ©inf.' — Gharib's own etymology for the family is a *pari- compound of θanj- 'draw', not *part-aka-.\"},\n   {\"src\": \"LAT\", \"where\": \"p.853 s.v. parada\", \"stance\": \"partial\", \"note\": \"Ernout-Meillet give only Iranian *partaka- with Armenian/Syriac loans; the Sogdian branch is not discussed there.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"plan-asthai; plas-sein\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Greek verbs are standard members of PIE *pelə-2/*plā- 'flat; to spread'. Watkins (AHD appendix, the 'AHD:1533' Nourai cites): '5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< „to spread out“): PLANET; APLANATIC ... 6. Suffixed zero-grade form *pl̥-dh- in Greek plassein (< *plath-yein), to mold, „spread out“: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY.' Pokorny 805-807 has the same two: 'πλάσσω (*πλαθιω) ... „shape from soft mass, spread“' as a dh-present, and 'πλάνος „irrend, wandering“ ... perhaps of the aimless spreading of grazing herds'. planāsthai is the middle of planáō; plássein is Attic for *plath-yein with the regular -θj- > -σσ-.\",\n \"derivation_fa\": \"هر دو فعل یونانی از اعضای پذیرفته‌شدهٔ ریشهٔ هندواروپایی *pelə-/*plā- «پهن؛ گستردن»‌اند. واتکینز (پیوست‌نامهٔ AHD) می‌نویسد: «گونهٔ گستردهٔ *plan- در یونانی planasthai «سرگردان شدن» (< گستردن) ← planet» و «صورت درجهٔ صفر *pl̥-dh- در plassein (< *plath-yein) «قالب زدن» ← plasma, plastic». پوکورنی (ص ۸۰۵–۸۰۷) نیز همین دو را ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [ETY_PLASTIC],\n \"ref_check\": [\n   {\"ref\": \"AHD:1533\", \"status\": \"supports\", \"note\": \"The Watkins appendix entry pelə-2 (AHD_watkins1985.txt lines 829-834, reprint of the same list that occupies AHD New College pp.1505-1550) has both planasthai (§5a) and plassein (§6) — p.1533 falls inside the appendix at 'pel-'.\"},\n   {\"ref\": \"IEC:918\", \"status\": \"not_found\", \"note\": \"IEC p.918 (leaf 510) runs peln- ... peluos / pendo and contains no Greek plan-/plass- material; Mann's Greek forms for this root are elsewhere in the volume.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pelə-, plā- pp.805-807\", \"stance\": \"supports\", \"note\": \"'as dʰ-present probably here gr. πλάσσω (*πλαθιω) ... „shape from soft mass, form“ ... πλάσμα n. „thing“ ... ἐμπλαστρον > Latin emplastrum'; and 'here - perhaps of ziellosen sich Ausbreiten weidender Herden - gr. πλάνος „irrend, wandering“'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. s.v. plasma\", \"stance\": \"supports\", \"note\": \"'plasma ... Late L., fr. Gk. πλάσμα, „something molded“, fr. πλάσσειν, „to mold, form, model“.'\"},\n   {\"src\": \"AHD\", \"where\": \"index, PLANET/PLASMA/PLASTER/PLASTIC → pelə-2\", \"stance\": \"supports\", \"note\": \"Watkins index lines 2099-2100: 'PLANET pele-2 ... PLASMA pele-2 ... PLASTER pele-2 PLASTIC pele-2'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"French\", \"words\": \"plasma; plastique\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French plasma and plastique are learned formations on the Greek stem, taken in through Latin rather than straight from Greek: plastique (adj. 1548, subst. f. 'art of modelling', then 20th-c. 'synthetic mouldable material') < Latin plasticus < Gk plastikós 'fit for moulding', from plastós, verbal adjective of plássein; plasma (1846 in the blood sense, 1928 in the physics sense) < Late Latin plasma < Gk plásma 'something moulded'. The chart's Greek → French arrow is therefore right in substance, with Latin as the unnamed relay.\",\n \"derivation_fa\": \"فرانسه‌ی plasma و plastique واژه‌هایی عالمانه‌اند که از راه لاتین از یونانی گرفته شده‌اند: plastique < لاتین plasticus < یونانی plastikós «قابل قالب‌گیری»، و plasma < لاتین متأخر plasma < یونانی plásma «چیز قالب‌زده». پس پیکان یونانی ← فرانسه درست است، فقط حلقهٔ لاتین نام‌برده نشده است.\",\n \"sources\": [ETY_PLASTIC],\n \"ref_check\": [\n   {\"ref\": \"VOP:120\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vâžehâ-ye Orupâyi dar Fârsi (1371/1992) — refs_online.json records 'kind: none': no scan or ebook found anywhere (archive.org, ketabnak, noorlib), purchase second-hand only.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. plasma; plastic\", \"stance\": \"supports\", \"note\": \"'plasma ... Late L., fr. Gk. πλάσμα ... fr. πλάσσειν' — Klein routes both through Latin, as French does.\"},\n   {\"src\": \"AHD\", \"where\": \"appendix pelə-2 §6\", \"stance\": \"supports\", \"note\": \"'Greek plassein ... : -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"plâsmâ «پلاسما»; plâstîk «پلاستیک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both are 20th-century European loans in Persian. پلاستیک plâstîk reproduces French plastique (the final -یک = Fr. -ique, not English -ic which would have given *پلاستیک with short i; the long ī and the stress pattern point to French, the usual channel for Iranian technical vocabulary before 1941). پلاسما plâsmâ with final آ likewise renders French plasma [plasma] rather than English [ˈplæzmə]. Neither is a native Persian formation; they enter medicine and industry in Iran from the Dar al-Fonun / Franco-Persian scientific tradition. The chart's French → Persian arrow is thus correct; the ultimate Greek ancestry it displays is a genuine, if very long, chain.\",\n \"derivation_fa\": \"«پلاستیک» و «پلاسما» هر دو وام‌واژهٔ سدهٔ چهاردهم هجری از فرانسه‌اند. پایانهٔ «–یک» در پلاستیک برگردان –ique فرانسه است و «آ» پایانی پلاسما نیز تلفظ فرانسوی را بازمی‌تاباند نه انگلیسی را. این واژه‌ها از راه سنت علمی فرانسه‌زبان دارالفنون وارد فارسی شده‌اند. ادعای نورایی درست است.\",\n \"sources\": [ETY_PLASTIC],\n \"ref_check\": [\n   {\"ref\": \"VOP:120\", \"status\": \"not_checked\", \"note\": \"Moshiri 1992 has no digital copy (refs_online.json 'kind': 'none'); this is Nourai's only reference for the modern European loans on this page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi, vol. 4 (foreign compounds)\", \"stance\": \"silent\", \"note\": \"The local OCR files MON_part1/part2.txt do not contain the پلاستیک / پلاسما headwords (grep of the Persian script returns only unrelated running text), so Mo'in could not be quoted here.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. plastic, plasma\", \"stance\": \"supports\", \"note\": \"Klein confirms the Greek>Latin>modern-European chain that the Persian loans sit at the end of.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"planet, plasma, plaster, airplane, plastic\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Four of the five are correct as drawn. Watkins files PLANET under Gk planasthai and PLASMA, PLASTER, PLASTIC under Gk plassein (AHD index: 'PLANET pele-2 ... PLASMA pele-2 PLASTER pele-2 PLASTIC pele-2'); planet is Gk planḗtēs (astḗr) 'wandering star' > L planeta > OF planete > ME planete, and plaster is Gk émplastron > L emplastrum > OE plaster. AIRPLANE, however, is not Greek: Watkins puts it under the Latin branch of the same root (*plā-no- > Latin planus), 'LLANO, PIANO, PLAIN ... PLANO-, PLANULA; AIRPLANE, EXPLAIN' — English airplane is a reshaping of French aéroplane, whose second element is Latin planus 'flat (surface)'. So the node belongs partly in box #14/#15, not here.\",\n \"derivation_fa\": \"چهار واژه از پنج واژه درست است: planet از یونانی planḗtēs «ستارهٔ سرگردان»، و plasma، plaster، plastic از plassein. اما airplane یونانی نیست: واتکینز آن را ذیل شاخهٔ لاتین همین ریشه (planus) می‌آورد؛ این واژه بازساختهٔ فرانسه‌ی aéroplane است که جزء دومش لاتین planus «صاف» است. پس این یک واژه جابه‌جا افتاده و باید در جعبهٔ لاتین می‌آمد.\",\n \"sources\": [ETY_PLASTIC],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins index (AHD_watkins1985.txt lines 2099-2100 and the pelə-2 entry): PLANET, PLASMA, PLASTER, PLASTIC all → pelə-2 via Greek; but AIRPLANE is listed in the entry under the Latin planus branch, not the Greek one.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"appendix pelə-2 §3b, §5a, §6\", \"stance\": \"partial\", \"note\": \"'*plā-no- in Latin planus ...: LLANO, PIANO, PLAIN ...; AIRPLANE, EXPLAIN' vs '*plan- in Greek planasthai ...: PLANET' and '*pl̥-dh- in Greek plassein ...: PLASMA, PLASTER, PLASTIC'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. plasma\", \"stance\": \"supports\", \"note\": \"'plasma ... fr. Gk. πλάσμα ... Cp. also plasson, plaster, plastic, plastid, plastron.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Germanic\", \"words\": \"fel-thus; flô-ruz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *felþuz/*felþa- 'field, flat land' and *flōruz 'floor' are both in Pokorny's pelə-/plā- entry, the page Nourai cites: 'with r-formants: Old Icelandic flórr m. „floorboard of cattle shed“, Old English flōr, Middle Low German vlor, MHG vluor, NHG Flur, Old Irish lár, Welsh llawr (*plā-ro-) „solum, pavimentum“' and 'with dental forms *pel-tos n., *pel-tu- m., *pel-tā „surface, plain“: OHG/OS feld n., OE feld (u-stem), ON fold f. „earth, land“, OE folde, OS folda'. Germanic *p- > *f- by Grimm's law; *-t- of *pel-tu- stays voiceless after the stressed root syllable (no Verner voicing). Pokorny does add that the feld-words 'belong actually to extension plet-', which is only a question of which sub-root you file them under.\",\n \"derivation_fa\": \"ژرمنی آغازین *felþuz «دشت، کشتزار» و *flōruz «کف، زمین» هر دو در همان مدخل پوکورنی (ص ۸۰۵–۸۰۷) آمده‌اند: «با پسوند r: ایسلندی کهن flórr، انگلیسی کهن flōr ... (*plā-ro-)» و «با پسوند دندانی *pel-tos/*pel-tu- «سطح، دشت»: آلمانی علیای کهن feld، انگلیسی کهن feld». پ‌ی هندواروپایی برپایهٔ قانون گریم در ژرمنی به f بدل شده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:805\", \"status\": \"supports\", \"note\": \"POK_full.txt block 'Root / lemma: pelə- plā- / Meaning: wide and flat / ... Page(s): 805-807': 'with r-formants: Old Icelandic flórr m. „floorboard of cattle shed“, Old English flōr ...' and 'with dentalem forms *pel-tos n., *pel-tu- m., *pel-tā „surface, plain, area“: Old High German Old Saxon feld n. „field, bottom, plain“, Old English feld (u-stem) ds.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"index FIELD → pelə-2; entry §3a *plā-ru- > Gmc *flōruz\", \"stance\": \"supports\", \"note\": \"'FIELD pele-2' (index line 1509) and '*plā-ru- in Germanic *flōruz, floor, in Old English flōr, floor: FLOOR'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. floor\", \"stance\": \"supports\", \"note\": \"'floor, n. — ME. flor, fr. OE. flōr, rel. to MDu. vloer, ON. flór ... fr. I.-E. base *plāros, *plārā ... This base is an enlargement of base *p(e)lā-, „spread out, broad, flat“, whence L. planus.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"field; floor\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English field < OE feld (u-stem) < PGmc *felþuz, and floor < OE flōr < PGmc *flōruz; both are inherited, not borrowed, and both are placed under this root by Watkins ('FIELD pele-2', and '*plā-ru- in Germanic *flōruz ... in Old English flōr, floor: FLOOR'). The OE ēo/e of feld is regular for West Germanic *e before l + consonant; OE flōr keeps the inherited long ō (< *ā), whence ME flor > NE floor.\",\n \"derivation_fa\": \"انگلیسی field از انگلیسی کهن feld و floor از انگلیسی کهن flōr است؛ هر دو میراثی‌اند نه وام‌واژه، و واتکینز هر دو را ذیل همین ریشه می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index line 1509 'FIELD pele-2'; index line 1521 'FLOOR' under the same root via the entry's §3a; neither is assigned elsewhere.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.805-807\", \"stance\": \"supports\", \"note\": \"'Old English feld (u-stem) ds.'; 'Old English flōr „floorboard“'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. floor\", \"stance\": \"supports\", \"note\": \"'For a dental enlargement of base *p(e)lā- see field.' — Klein cross-refers floor and field to the same base.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"plâ-nus; pal-ma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin plānus 'flat, level' is *plā-no-s, the suffixed full grade of the root (Pokorny: 'Latin plānus „platt, even, flat“ (Indo Germanic *plā-no-s) = gall. Mediolanum ... Lithuanian plónas „thin“, Latvian plāns, Old Prussian plonis „threshing floor“'). Latin palma 'palm of the hand' is the zero-grade *pḷ-ma < *palama (Watkins '§4. Suffixed zero-grade form *pl̥-mā in Latin palma (< *palama), palm of the hand'), with the same 'flat surface' semantics; Pokorny sets it beside Gk palámē, OIr. lám, OHG folma, OE folm and Av. pərənā 'hollow hand'. Both are exactly where Nourai puts them.\",\n \"derivation_fa\": \"لاتین plānus «صاف، هموار» از *plā-no-s است (پوکورنی ص ۸۰۵)، و palma «کف دست» از درجهٔ صفر *pḷ-mā (< *palama) که هم‌ریشهٔ یونانی palámē، ایرلندی کهن lám و اوستایی pərənā «کف دست» است. هر دو دقیقاً همان‌جایی اند که نورایی نشانده است. ادعا درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:1533\", \"status\": \"supports\", \"note\": \"Watkins pelə-2: '§3b. suffixed form *plā-no- in Latin planus, flat, level, even, plain, clear' and '§4. Suffixed zero-grade form *pl̥-mā in Latin palma (< *palama), palm of the hand: PALM1, PALM2'. The appendix occupies AHD New College pp.1505-1550, so p.1533 is inside it at 'pel-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.805-807\", \"stance\": \"supports\", \"note\": \"'Latin plānus „platt, even, flat“ (Indo Germanic *plā-no-s)'; 'Latin palma „flat hand ...“, palmus, palmes'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. plain, adj.; palm, n.\", \"stance\": \"supports\", \"note\": \"'plain, adj. ... fr. L. planus ... fr. I.-E. base *p(e)lā-, „broad, flat, spread out“'; 'palm ... fr. L. palma, „palm tree“, orig. identical with palma, „palm of the hand“; so called from the flatness of its leaves.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"plane, plain, plan, explain; palm\",\n \"verdict\": \"plausible\",\n \"derivation\": \"plain (ME, fr. OF plain < L plānus), plane (in all its senses, via OF/L plānus, plānum, plāna), explain (L explānāre 'to flatten out, make clear') and palm (OE palm, ME paume, fr. L palma) are all correctly filed under the Latin box. The odd one out is plan: Watkins assigns PLAN not to plānus but to plat- — English plan < French plan 'ground-plan', from Latin planta 'sole of the foot' (plat- §5 'Nasalized form *pla-n-t- in Latin planta ... CLAN, PLAN, PLANT, PLANTAIN, PLANTAR'), with later contamination from plan 'flat' (< plānus). So four of the five English words are confirmed, one belongs under the Plat sub-root drawn lower on the same chart.\",\n \"derivation_fa\": \"plain، plane، explain و palm همگی به درستی از لاتین plānus/palma آمده‌اند. اما plan را واتکینز ذیل ریشهٔ plat- می‌آورد: از فرانسه plan «نقشهٔ زمین» از لاتین planta «کف پا» (با آمیزش معنایی بعدی با plan «صاف»). پس چهار واژه از پنج واژه درست‌اند و یکی باید به شاخهٔ Plat منتقل شود.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins index line 2099-2100: 'PLAIN pelə-2 ... PLANE1 pelə-2 PLANE2 pelə-2 PLANE3 pelə-2 PLANE4 plat- ... PLAN plat-'; PALM1/PALM2 and EXPLAIN are under pelə-2. So PLAN (and PLANE4 'plane tree') sit under plat-, not under Latin plānus.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. plain, adj.\", \"stance\": \"supports\", \"note\": \"'plain, adj., flat; clear, distinct. — ME., fr. OF. (= F.) plain, fr. L. planus ... Cp. plain „level country“, plane „even, level“, plane, the tree, plane „tool for smoothing“, piano, llano, esplanade, explain, explanation.'\"},\n   {\"src\": \"AHD\", \"where\": \"appendix pelə-2 §3b\", \"stance\": \"partial\", \"note\": \"'LLANO, PIANO, PLAIN, PLANARIAN, PLANE1, PLANE2, PLANE3, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN' — no PLAN.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Indo-European\", \"words\": \"Plat\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pokorny's page 833 is exactly 'plat- (plad-), plet-, plot-, plət-, Meaning: wide, flat', with the note 'extension to pelə- : plā- ds.' — i.e. Pokorny himself makes *plat- an extension of the *pelə-/*plā- of p.805, which is precisely the relation Nourai's chart draws (Plat hanging off Pele). Watkins says the same in one line: 'plat-. To spread. Extension of pelə-2 ... [Pok. plat- 833.]'. Nourai's gloss 'to spread' is Watkins's; Pokorny's is 'wide, flat'; they are the same root.\",\n \"derivation_fa\": \"صفحهٔ ۸۳۳ پوکورنی دقیقاً مدخل plat-/plet-/plot-/plət- «پهن، صاف» است با این یادداشت که «گسترشی از pelə-/plā-» است — همان رابطه‌ای که نمودار نورایی نشان می‌دهد. واتکینز نیز می‌نویسد: «plat- «گستردن». گسترشی از pelə-2». ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:833\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: plat- (plad-), plet- plot-, plət- / Meaning: wide, flat / Note: extension to pelə- : plā- ds., see there ... References: WP. II 99 f., WH. II 316 ff. ... Page(s): 833-834'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"appendix s.v. plat-\", \"stance\": \"supports\", \"note\": \"'plat-. To spread. Extension of pelə-2. ... [Pok. plat- 833.]'\"},\n   {\"src\": \"KLN\", \"where\": \"p.1192 s.v. place\", \"stance\": \"supports\", \"note\": \"'All these words are derivatives of I.-E. base *plāt-, *plət-, *plet-, *plot-, „spread out, broad, flat“.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Avestan\", \"words\": \"frathah\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan fraθah- is genuine: Bartholomae, Altiranisches Wörterbuch, has 'j. fraθah- n. „Breite“' (attested Y. 19.7, of the earth's extent). It is the Iranian reflex of the s-stem *pl̥th2-es- (PII *prátʰas), matching Old Indic práthas- n. 'breadth' exactly — PIE *pl̥- > Indo-Iranian *pr̥- > Av. fra- with the regular Avestan *p > f before r, and the aspirate *tʰ > θ. One caveat on the gloss: fraθah- is a neuter noun 'breadth, width', not the adjective 'wide'; the Avestan adjective is pərəθu- (= Skt pṛthú-, Gk platús), which is the form Klein cites on the page Nourai gives.\",\n \"derivation_fa\": \"اوستایی fraθah- واقعی است: بارتولومه در فرهنگ ایرانی باستان می‌آورد: «fraθah- خنثی «پهنا»» (یسنا ۱۹،۷). این صورت بازتاب ستاک s‌دار *pl̥tʰ-es- است که دقیقاً با سنسکریت práthas- «پهنا» برابر است؛ پ ایرانی پیش از r به f بدل شده است. تنها نکته: fraθah- اسم است («پهنا») نه صفت («پهن»)؛ صفت اوستایی pərəθu- است که کلاین در همان صفحهٔ ۱۱۹۲ ذکر کرده است.\",\n \"sources\": [WIKT_FARAX],\n \"ref_check\": [\n   {\"ref\": \"POK:833\", \"status\": \"supports\", \"note\": \"POK p.833 s.v. plat-: 'Aryan *pleth-: Old Indic práthati „breitet aus“ ... práthas- n. = Avestan fraθah- n. „Breite“, Old Indic pṛthú-, Avestan pərəθu- „wide, breit“.'\"},\n   {\"ref\": \"KLN:1192\", \"status\": \"partial\", \"note\": \"Klein 1966 p.1192 (leaf 636, the leaf after the one carrying '1190') s.v. place: Gk. πλατύς 'is cogn. with OI. prathati „spreads out“, pṛthúḥ „broad, wide, spacious“, Avestic pərəθuš, of s.m. ... All these words are derivatives of I.-E. base *plāt-, *plət-, *plet-, *plot-'. Klein gives the root correctly but the Avestan form he prints is the adjective pərəθu-, not fraθah-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch s.v. fraθah- (BRT.txt line 17648)\", \"stance\": \"supports\", \"note\": \"'j. fraθah- n. „Breite“: avavaḟitya ... Y.19.7.' Bartholomae also has the compounds yavō.fraθah- 'of a barleycorn's breadth', spā.fraθah- 'of a dog's breadth', zəm.fraθah- 'as broad as the earth' — an entirely regular s-stem.\"},\n   {\"src\": \"POK\", \"where\": \"p.833\", \"stance\": \"supports\", \"note\": \"as above; the Avestan word is quoted by Pokorny in the very entry Nourai cites.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"farâx «فراخ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP فراخ farāx 'wide, spacious, ample' goes back to MP frāx [plʾh(w)], and behind that to the Old Iranian s-stem/u-stem of this root. Horn, Grundriss no. 810 (p.180), the page Nourai cites, has it verbatim: 'ferāx „weit, breit“, ferāxī ... aw. fraθah- „Breite“; phlv. frāh bezw. frāh[ē] ... ai. práthas-; kurd. LW (?) fereh „weit“; bel. LW prāh „weit, breit“'. Hübschmann no. 810 adds the alternative that NP farāx reflects a u-stem, 'np. farax = phl. frāxv, geschrieben fraxv scheint ein ap. *fra(k)uva- vorauszusetzen', i.e. *fraθu-/*fraxu- rather than the s-stem; Mo'in's footnote in Borhan-e Qate' p.1444 reports both. Wiktionary's current entry has MP plʾhũ /frāx/ < Proto-Iranian *fráθah < PII *prátʰas < PIE *pléth₂os — the same chain Nourai draws. The x of farāx is the Middle Persian outcome of the cluster *θu/*θw (whence also the Pāzand doublet frāh).\",\n \"derivation_fa\": \"«فراخ» از فارسی میانهٔ frāx است و آن از ایرانی باستان *fráθah (اوستایی fraθah- «پهنا»). هرن در شمارهٔ ۸۱۰ (ص ۱۸۰) همین را می‌آورد؛ هوبشمان در همان شماره صورت پارسی باستان *fra(θ)uva- را پیشنهاد می‌کند؛ و معین در حاشیهٔ برهان قاطع (ص ۱۴۴۴) هر دو را نقل کرده است. خـی فارسی حاصل خوشهٔ *θw است (در برابر گونهٔ پازند frāh). ادعای نورایی درست است.\",\n \"sources\": [WIKT_FARAX],\n \"ref_check\": [\n   {\"ref\": \"HRN:180\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.180 (HRN.txt leaf 202, running head '— 180 —'), no. 810: 'ferāḵ „weit, breit“, ferāḵī ... aw. fraθah- „Breite“; phlv. frāh bezw. frāh[ē] ... ai. práthas-.'\"},\n   {\"ref\": \"BQT:1444\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p.1444 (rendered with tools/ref_page.py BQT:1444 --image) carries the headword فراخ and Mo'in's footnote: 'اوستا fraθah- (عرض، پهنا). پهلوی [frāh]؛ هندی باستان práthas-، کردی فرا (گشاد)، بلوچی ... «هرن ۸۱۰». در پهلوی frāx که frāhw نوشته شود، از پارسی باستان *fra(θ)uva- مأخوذ است «هوبشمان ۸۱۰». پازند frāh, ferāx «نیبرگ ۷۱».'\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien no. 810 (HUB.txt line 2951)\", \"stance\": \"partial\", \"note\": \"'Np. farax = phl. frāḵv, geschrieben fraxv scheint ein ap. *fra(k)uva- vorauszusetzen. Ebenso Fr. Müller, WZKM. 7, 378.' — same root, but Hübschmann prefers a u-stem preform to the s-stem fraθah-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. frāx, frāxīh, frāxēnīdan\", \"stance\": \"supports\", \"note\": \"PHD.txt: 'frāxīh: plenty, prosperity. frāxēnīdan, frāxēn- [plʾh(w)yn-ytn'] enlarge, make prosper' — the Middle Persian link in the chain is on record.\"},\n   {\"src\": \"BQT\", \"where\": \"p.1444 (Mo'in's حاشیه)\", \"stance\": \"supports\", \"note\": \"as quoted above; Mo'in cites Horn 810, Hübschmann 810 and Nyberg 71.\"}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Germanic\", \"words\": \"flataz\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Proto-Germanic *flataz 'flat' is the regular Germanic form of the *plad- variant of the root: Watkins, s.v. plat-, '1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: FLAT1; b. Old French flater, to flatter: FLATTER1.' Pokorny p.833-834 has the same series 'With final sound voiced-nonaspirated: Old Icelandic flatr, Old High German flaz „even, flat“, Old Saxon flat, Old Icelandic/Old English flet, Old Saxon flet, fletti „floor in the house“'. PIE *d gives Germanic *t by Grimm's law, and initial *p > *f.\",\n \"derivation_fa\": \"ژرمنی آغازین *flataz «صاف، پهن» بازتاب قاعده‌مند گونهٔ *plad- است: د هندواروپایی بر پایهٔ قانون گریم در ژرمنی t می‌شود و پ آغازین f. واتکینز و پوکورنی (ص ۸۳۳–۸۳۴) هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. plat-: '1. Variant form *plad- in Germanic *flataz, flat, in: a. Old Norse flatr, flat: FLAT1.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.833-834 s.v. plat-\", \"stance\": \"supports\", \"note\": \"'With final sound voiced-nonaspirated: Old Icelandic flatr, Old High German flaz „even, flat“, Old Saxon flat ... Old High German flazza „palm“.'\"},\n   {\"src\": \"KLN\", \"where\": \"p.1192 s.v. place\", \"stance\": \"supports\", \"note\": \"Klein lists 'flat, „level“, flat, „floor“' among the derivatives of the base *plāt-/*plet-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"English\", \"words\": \"flat\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English flat (adj., c.1300) is not inherited from Old English but borrowed from Old Norse flatr 'flat' during the Scandinavian settlement — Watkins says so explicitly under plat- §1a ('Old Norse flatr, flat: FLAT1'); the homograph flat 'apartment, storey' (§2) is the native OE flet(t) 'floor, dwelling' from the *plad-yo- variant. Either way the node's parent (#19 Germanic *flataz) is correct.\",\n \"derivation_fa\": \"انگلیسی flat میراث انگلیسی کهن نیست بلکه وام‌واژه‌ای از نورسی کهن flatr است که در دوران اسکان اسکاندیناویایی‌ها (حدود ۱۳۰۰ میلادی در متون) وارد شده است؛ هم‌نگاشتِ flat «آپارتمان» از انگلیسی کهن flett «کف خانه» است. به هر حال پیوند آن با *flataz درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; verified independently against Watkins (AHD appendix s.v. plat-) and Pokorny 833-834.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"appendix s.v. plat- §1a, §2; index line 1517 'FLAT1 plat- FLAT2 plat-'\", \"stance\": \"supports\", \"note\": \"'a. Old Norse flatr, flat: FLAT1' and '2. Suffixed variant form *plad-yo- in Germanic *flatjam in Old English flet(t), floor, dwelling: FLAT2.'\"},\n   {\"src\": \"POK\", \"where\": \"pp.833-834\", \"stance\": \"supports\", \"note\": \"'Old Icelandic flatr ... Old Icelandic-Old English flett n., Old Saxon flet, fletti „floor in Haus“.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 21, \"lang\": \"Greek\", \"words\": \"platus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek πλατύς platús 'flat, broad' is the u-stem adjective of the root, the exact match of Old Indic pṛthú- and Avestan pərəθu-: PIE *pl̥tʰ-ú- > Gk platus (with the regular Greek *l̥ > λα). Pokorny p.833: 'gr. πλατύς „platt, breit“ (= Old Indic pṛthú-), πλάτος n. „Breite“ ... πλατεῖα „broad way“'. Watkins: 'plat- ... 6. Suffixed form *plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE4, PLATE, PLATEAU, PLATITUDE, PLATY-, PLAZA.'\",\n \"derivation_fa\": \"یونانی platús «پهن، صاف» صفت u‌ستاک همین ریشه است و دقیقاً برابر سنسکریت pṛthú- و اوستایی pərəθu- است: *pl̥tʰ-ú- با تبدیل قاعده‌مند l̥ به λα در یونانی. پوکورنی و واتکینز هر دو همین را تأیید می‌کنند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. plat-, §6: 'Suffixed form *plat-u- in Greek platus (feminine plateia), flat, broad: PIAZZA, PLACE, PLAICE, PLANE4, (PLANE TREE), PLATE, (PLATEAU), (PLATITUDE), (PLATY2), PLATY-, (PLAZA).'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.833\", \"stance\": \"supports\", \"note\": \"'gr. πλατύς „platt, breit“ (= Old Indic pṛthú-), πλάτος n. „Breite“ ... πλάτανος „sycamore“ („breitastig“).'\"},\n   {\"src\": \"KLN\", \"where\": \"p.1192 s.v. place\", \"stance\": \"supports\", \"note\": \"'πλατεῖα (ὁδός), „street“, lit. „broad way“, fem. of πλατύς, „flat, wide, broad“.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 22, \"lang\": \"Latin\", \"words\": \"plattus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Late/Vulgar Latin plattus 'flat' is a borrowing of Greek platús, not an inherited Latin cognate — the geminate -tt- and the a-vocalism give it away (inherited *pl̥t- would have yielded Latin lat-/plat- as in latus, planta). It is the source of Italian piatto, Old French plat, Old Provençal plat, Spanish plato/plata, and hence of the whole modern 'flat/plate' family. Klein sets out the parallel case on p.1192: 'VL. *plattea (whence also It. piazza, OProvenç. plasa, Catal. plassa, Sp. plaza, Port. praça), fr. L. platea, „open space, street“, fr. Gk. πλατεῖα (ὁδός)'. Nourai's box is therefore correct, though 'Latin' here means the spoken Latin of the Empire, not Classical Latin.\",\n \"derivation_fa\": \"لاتین متأخر/عامیانهٔ plattus «صاف» وام‌واژه‌ای از یونانی platús است نه هم‌ریشهٔ میراثی آن؛ تشدید -tt- و الف آن گواه وام‌گیری است. از همین صورت، ایتالیایی piatto، فرانسهٔ کهن plat و اسپانیایی plato/plata برآمده‌اند. کلاین در ص ۱۱۹۲ نمونهٔ موازی *plattea > piazza/plaza را می‌آورد. ادعای نورایی درست است؛ تنها باید دانست که مراد لاتین گفتاری است نه لاتین کلاسیک.\",\n \"sources\": [ETY_PLATINUM],\n \"ref_check\": [\n   {\"ref\": \"AHD:1004\", \"status\": \"not_checked\", \"note\": \"An AHD New College main-dictionary page (probably s.v. plate/platinum); the A-Z pages of the 1975/76 edition are only on lending-only archive.org scans. The IE appendix, which is available, confirms the Greek>Romance route under plat- §6.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.1192 s.v. place; s.v. plaice; s.v. platinum\", \"stance\": \"supports\", \"note\": \"'plaice ... fr. Late L. platessa, „plaice, flatfish“, which prob. derives fr. Gk. πλατύς, „flat“'; 'Sp. plata comes either fr. OProvenç. plata or fr. OF. plate, which mean „sheet of metal“, and ult. derive fr. Gk. πλατύς.'\"},\n   {\"src\": \"AHD\", \"where\": \"appendix plat- §6\", \"stance\": \"supports\", \"note\": \"All of PIAZZA, PLACE, PLATE, PLATEAU, PLAZA are traced to Greek platus, i.e. through the Romance plattus/platea forms.\"}\n ]\n})\n\nnodes.append({\n \"id\": 23, \"lang\": \"French\", \"words\": \"platine\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French platine 'platinum' (f., 1752) is real, but it does not come from Latin plattus directly as the arrow implies: it is a borrowing of Spanish platina, the diminutive of plata 'silver', the name the Spanish gave the metal found in New Granada from 1735 ('platina del Pinto', 'little silver of the Río Pinto'). Spanish plata itself is the Romance reflex of the plattus/plata 'sheet of metal' family that does descend from Greek platus. So the chain is Gk platus > VL plattus/plata > Sp. plata > Sp. platina > Fr. platine; Nourai has compressed two Romance steps into one and omitted the decisive Spanish colonial link. (French also has an unrelated homonym platine 'metal plate, turntable', directly from plat.)\",\n \"derivation_fa\": \"فرانسه‌ی platine «پلاتین» (۱۷۵۲ م.) وام‌واژه‌ای از اسپانیایی platina، مصغر plata «نقره»، است که اسپانیایی‌ها بر فلز یافته‌شده در گرانادای نو (۱۷۳۵ م.) نهادند. خود plata بازماندهٔ خانوادهٔ plattus/plata «ورقهٔ فلز» است که از یونانی platys می‌آید. پس زنجیره درست است ولی نورایی حلقهٔ اسپانیایی را حذف کرده است؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [ETY_PLATINUM],\n \"ref_check\": [\n   {\"ref\": \"VOP:120\", \"status\": \"not_checked\", \"note\": \"Moshiri 1992 is undigitised (refs_online.json 'kind': 'none').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. platinum\", \"stance\": \"partial\", \"note\": \"'platinum, n. — ModL., fr. earlier platina, fr. Sp. platina in platina del Pinto, i.e. „little silver of the River Pinto“ ... Sp. plata comes either fr. OProvenç. plata or fr. OF. plate, which mean „sheet of metal“, and ult. derive fr. Gk. πλατύς, „flat, wide, broad“.' — Spanish, not Latin, is the immediate donor.\"},\n   {\"src\": \"AHD\", \"where\": \"index 'PLATINUM plat-'\", \"stance\": \"supports\", \"note\": \"The root assignment is right even though the intermediate steps are not spelled out.\"}\n ]\n})\n\nnodes.append({\n \"id\": 24, \"lang\": \"Persian\", \"words\": \"pelâtîn «پلاتین»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian پلاتین pelātīn is the French chemical name platine [platʲin] taken over whole, with the French final nasal vowel rendered by –ین; had the word come from English platinum or Russian платина the Persian would be *پلاتینوم / *پلاتینا. Like پلاستیک and پلاسما above, it belongs to the layer of French scientific vocabulary that entered Persian through the Dar al-Fonun and the 20th-century school system. The chart's French → Persian arrow is right.\",\n \"derivation_fa\": \"«پلاتین» دقیقاً برگردان فرانسه‌ی platine است؛ واکهٔ خیشومی پایانی فرانسه در فارسی به «–ین» بدل شده است. اگر وام از انگلیسی platinum یا روسی پلاتینا می‌بود صورت دیگری می‌داشت. این واژه هم‌ردیف پلاستیک و پلاسما از راه سنت علمی فرانسه‌زبان وارد فارسی شده است. ادعای نورایی درست است.\",\n \"sources\": [ETY_PLATINUM],\n \"ref_check\": [\n   {\"ref\": \"VOP:120\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e Vâžehâ-ye Orupâyi dar Fârsi — no copy exists online; this is the only reference Nourai gives for the three modern Persian loans on the page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. platinum\", \"stance\": \"supports\", \"note\": \"Klein's chain ModL platinum < Sp. platina < plata < Gk πλατύς is the one the Persian word sits at the end of.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in vol. 4 (foreign words)\", \"stance\": \"silent\", \"note\": \"The local MON OCR files do not carry the پلاتین headword, so Mo'in's own tag ([فر.] = French) could not be quoted from the files on disk.\"}\n ]\n})\n\nnodes.append({\n \"id\": 25, \"lang\": \"English\", \"words\": \"plate, place, plaza, plateau, platinum\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are Watkins's own list under plat- §6 ('PIAZZA, PLACE, PLAICE, PLANE4, PLATE, PLATEAU, PLATITUDE, PLATY-, PLAZA' — plus PLATINUM in the index). Routes: plate < OF plate 'flat sheet of metal' (< VL *plattus); place < OF place < VL *plattea < L platea < Gk plateia (hodós) 'broad way'; plaza is the same word borrowed a second time, from Spanish plaza; plateau < French plateau (OF platel, dim. of plat); platinum < ModL platinum < Sp. platina. All ultimately Greek platús, exactly as drawn.\",\n \"derivation_fa\": \"هر پنج واژه در فهرست واتکینز ذیل plat- آمده‌اند: plate از فرانسهٔ کهن plate؛ place از لاتین عامیانهٔ *plattea از لاتین platea از یونانی plateia «راه پهن»؛ plaza وام دوبارهٔ همین واژه از اسپانیایی؛ plateau از فرانسه؛ platinum از لاتین نو از اسپانیایی platina. همه در نهایت از یونانی platús، دقیقاً همان که نورایی رسم کرده است.\",\n \"sources\": [ETY_PLATINUM],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins index lines 2099-2100: 'PLACE plat- ... PLATE plat- PLATEAU plat- ... PLAZA plat-'; and 'PLATINUM plat-' in the same block.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p.1192 s.v. place; s.v. platinum\", \"stance\": \"supports\", \"note\": \"'place, n. — ME., fr. OF. (= F.), fr. VL. *plattea (whence also It. piazza, ... Sp. plaza ...), fr. L. platea ... fr. Gk. πλατεῖα (ὁδός) ... Cp. piazza and plaza, which are doublets of place. Cp. also ... plateau, plate, platinum, platter, platy-.'\"},\n   {\"src\": \"POK\", \"where\": \"pp.833-834\", \"stance\": \"supports\", \"note\": \"The Greek platus family is the head of the entry; the Romance and English words are its late descendants.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Pele, Pelt, Paita\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *pelə-2 / *plā- 'wide and flat; to spread' (Pokorny 805-807; Watkins pelə-2), with the extension *plat- 'wide, flat' (Pokorny 833-834)\",\n \"note\": \"The root box is three claims in one, and they do not fare equally. (a) 'Pele' = Pokorny's pelə-, plā- 'wide and flat', pp.805-807 — correct in form, language label and gloss, and every Greek, Latin and Germanic branch drawn from it (planasthai, plassein, planus, palma, *felþuz, *flōruz) is in that very entry. (b) 'Pelt' is Mann's headword: IEC p.918 has pelt- (1) 'wrap, cloak, cover, screen' (Skt paṭah, Per. parde, ON feldr) and pelt- (2) 'space, patch, flat surface' (Gk peltē, Gmc feld), with Mann's own parenthesis '(Same as (1)?)'. Nourai has turned that question mark into an identity and hung the whole 'curtain' branch on the 'flat' root. Current handbooks keep them apart: Wiktionary derives MP pardag / Skt paṭa- from *pel- 'to cover, wrap; hide, cloth' (Pokorny's pel- 3b, p.803 = Watkins pel-4 'skin, hide'), and Etymonline analyses parda as OP *pari-dā- 'to place around'. (c) 'Paita' has no counterpart in Pokorny, Walde-Pokorny, Watkins or Mann that I could find; its only support is CEL2:3 (Gupta's Comparative Etymologic Lexicon), which is not digitised anywhere. So: the root is real and the Indo-European half of the chart is sound; the Iranian/Indic 'curtain, cloth' half is filed under the wrong homonym. The gloss 'to spread, make flat' is Watkins's wording for the root and is fine. Note also two internal misplacements (airplane under Greek; plan under Latin plānus) and one structural discrepancy between the printed page and the JSON, described under nodes #2 and #4.\",\n \"note_fa\": \"جعبهٔ ریشه سه ادعای جداگانه دارد. نخست، Pele همان pelə-/plā- پوکورنی (ص ۸۰۵–۸۰۷) «پهن و صاف» است و همهٔ شاخه‌های یونانی، لاتین و ژرمنی نمودار (planasthai، plassein، planus، palma، feld، flōr) دقیقاً در همان مدخل پوکورنی آمده‌اند. دوم، Pelt سرمدخل من (IEC ص ۹۱۸) است، اما من خود دو مدخل pelt- «پوشاندن، پرده» و pelt- «سطح صاف» را جدا آورده و یکی بودنشان را فقط با پرسش مطرح کرده است؛ نورایی آن پرسش را به اثبات بدل کرده و شاخهٔ «پرده» را زیر ریشهٔ «پهنی» آورده است؛ پژوهش امروزی این دو را جدا می‌دارد (ریشهٔ *pel- «پوشاندن»، پوکورنی ص ۸۰۳؛ یا تحلیل *pari-dā-). سوم، Paita در هیچ یک از پوکورنی، والده-پوکورنی، واتکینز یا من یافت نشد و تنها مستندش CEL2:3 است که نسخهٔ دیجیتالی ندارد. نتیجه: ریشه واقعی است و نیمهٔ هندواروپایی نمودار درست است، اما نیمهٔ ایرانی–هندی (پرده، paṭa-) ذیل هم‌آوای نادرست قرار گرفته است.\",\n \"sources\": [WIKT_PEL, WIKT_PARDE, WIKT_PATA, ETY_PURDAH],\n \"ref_check\": [\n   {\"ref\": \"POK:805\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: pelə- plā- / Meaning: wide and flat / Material: Armenian hol „earth, dust ...“; Latin palam ...; Hittite palhi- „broad“; gr. πλάσσω ...; Latin plānus ...; Latin palma ...; Old English flōr ...; OHG/OS feld ... / References: WP. II 61 ff. / Page(s): 805-807'. Page and gloss are exactly as cited.\"},\n   {\"ref\": \"IEC:918\", \"status\": \"partial\", \"note\": \"Mann p.918 (leaf 510) does have the material Nourai draws on, but under two separate headwords — pelt- (1) 'wrap, cloak, cover, screen' (Skt paṭah, Per. parde, ON feldr) and pelt- (2) 'space, patch, flat surface' (Gk peltē, MHG vëlt, OE feld) — with the identification left as a question: '(Same as (1)?)'. Mann's p.918 is NOT a page about 'to spread, make flat', and it has no Iranian *partaka- and no Greek plan-/plass- forms.\"},\n   {\"ref\": \"CEL2:3\", \"status\": \"not_checked\", \"note\": \"S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, vol. 2 p.3 — refs_online.json: catalogue records only, no digitisation found (HathiTrust search-only). This is the sole reference behind the 'Paita' element of the root name.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins appendix s.vv. pelə-2, plat-, pel-4\", \"stance\": \"partial\", \"note\": \"'pelə-2. Flat; to spread. Variant *plā-, contracted from *pləə-. ... [Pok. pelə- 805.]' and 'plat-. To spread. Extension of pelə-2. ... [Pok. plat- 833.]' — both of Nourai's root boxes and their mutual relation are Watkins's. But Watkins keeps 'pel-4. Skin, hide ... Greek peltē, a shield (made of hide) ... [Pok. 3 b. pel- 803]' strictly apart, and no cloth/curtain word appears under pelə-2.\"},\n   {\"src\": \"POK\", \"where\": \"pel- 3b p.803; pelə- p.805; plat- p.833\", \"stance\": \"partial\", \"note\": \"Pokorny runs three distinct entries: the 'Haut, Fell / cover' pel- (p.803, source of Lat. pellis, Gk peltē), the 'wide and flat' pelə-/plā- (p.805) and its extension plat- (p.833). Nourai's chart merges the first into the second.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 61 ff. (via Pokorny's own reference line)\", \"stance\": \"supports\", \"note\": \"Pokorny's entry closes 'References: WP. II 61 ff., WH. II 237, 240 f.' — Walde-Pokorny Bd. II p.61 ff. is the older treatment of the same 'wide and flat' root; only Bd. III (the index) is on disk locally, so the page itself could not be read.\"},\n   {\"src\": \"LAT\", \"where\": \"p.853 s.v. parada\", \"stance\": \"contradicts\", \"note\": \"Ernout-Meillet, on the page Nourai cites for the Persian word, say the primary sense of Iranian *partaka- 'devant être „division“' — i.e. not a 'flat surface' word at all.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 391,\n \"book_page\": 361,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-391.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint('written', len(nodes), 'nodes')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-391.py",
 "description": "Build page-391.json"
}
```


### [2026-09-14T01:11:58.645Z] TOOL RESULT

```
written 25 nodes
```


## [2026-09-14T01:12:07.286Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-391.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 391",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:12:08.602Z] TOOL RESULT

```
JSON OK
nodes verified: 25/25
node verdicts: {'disputed': 2, 'confirmed': 18, 'plausible': 5}
root verdicts: {'plausible': 1}
ref checks: {'partial': 7, 'supports': 15, 'not_checked': 8, 'not_found': 1}
books consulted: {'supports': 39, 'silent': 9, 'partial': 7} | by book: {'KLN': 16, 'POK': 10, 'AHD': 9, 'LAT': 3, 'HUB': 2, 'HJB': 2, 'MON': 2, 'HRN': 1, 'LKT': 1, 'RCH': 1, 'PLA': 1, 'NYB': 1, 'AID': 1, 'SYN': 1, 'SOD': 1, 'BRT': 1, 'PHD': 1, 'BQT': 1}
```


## [2026-09-14T01:12:27.718Z] AGENT

Page 391 (book p. 361) verified — `data/verification/page-391.json`, `verify_check.py 391`: 25/25 nodes, 0 PROBLEM lines.

**Verdicts** — root: 1 plausible; nodes: 18 confirmed, 5 plausible, 2 disputed.

**Disputed**
- Root *Pele/Pelt/Paita* → **#1 Iranian `partaka`**: Nourai hangs the "curtain" branch on PIE *pelə-2 "flat, spread" (POK 805). Modern view puts پرده under the homonymous *pel- "cover, wrap, hide, cloth" (POK 803 = AHD pel-4) or analyses it as OP *pari-dā-. His own source Mann (IEC 918) files it under *pelt- "wrap, cloak, screen" and only *asks* "(Same as (1)?)" of the "flat" root.
- **#6 Sanskrit `patah`**: paṭa- is not a descendant of Iranian *partaka-; at most a collateral (PII *paltas, Fortunatov's law) or a non-IE substrate loan. The retroflex -ṭ- rules out an Iranian loan.

**Plausible (misplacements, not errors of root)**: #4 Hindustani pardah is from *New Persian*, not Pahlavi (HJB 744, AID 242 both say "Pers."); #11 *airplane* belongs under Latin plānus, not Greek; #15 *plan* belongs under `Plat` (L. planta), not plānus; #23 Fr. platine is from Spanish platina, not straight from Latin plattus; #7 Sogdian prδ'nk — Gharib derives the family from *pari-θanj-, not *partaka-.

**Notable ref finds**: LAT:853 turns out to be Ernout-Meillet s.v. *parada*, which states "l'iranien *partaka- 'rideau', pers. parda, emprunté par l'arménien (partak) et le syriaque" — it supports the form but says the primary sense was "division", not "flat". LKT:131 is one page early (Lokotsch no. 1630 is on p.132) and Lokotsch's European route is via **Turkish** perde; the Arabic route (no. 228 bardaʿa) yields barde/albarda, not purdah. BQT:1444 renders correctly and carries Mo'in's footnote citing Horn 810 / Hübschmann 810 for فراخ < Av. fraθah-. Not accessible: VOP (undigitised, 3 nodes), CEL2, FWE, AHD:1061/1004.

**Extraction issue for the owner**: the printed chart connects the Persian `pardeh` box by a plain line to the **Pahlavi** box, and the arrow into `Hindustani` springs from the **Persian** box — i.e. #2 parent should be 3 and #4 parent should be 2; the JSON has #2 parent 1 and #4 parent 3. Everything else (root name "Pele, Pelt, Paita", `prd\`nk, prd\`nkh, prthynq`, all refs incl. LAT:853 and FWE:233) matches the printed page; page PNG saved to `data/verification/sources/refs/ocr/BOOK/391.png`.
