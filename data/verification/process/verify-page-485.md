# Verification process log — verify-page-485


## [2026-09-14T03:08:24.033Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 485 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-485.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-485.json. Write /home/sfmqrb/git/rishe/data/verification/page-485.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 485` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:24.959Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:25.807Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:25.822Z] TOOL RESULT

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


## [2026-09-14T03:08:26.306Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-485.txt"
}
```


### [2026-09-14T03:08:26.328Z] TOOL RESULT

```
1	=== PDF page 485 (book page 455) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Su 1, Esu, Wesu : well, good  (refs POK:342,1037,1174; KLN:548)  PART 2
4	#1 (parent #0) [Old Persian] refs=KNT:175 | hu, u, uv : good
5	  #2 (parent #1) [Avestan / Old Persian] refs=KNT:177 | u-vâra-zmi : good ... land ☞Ghdhem | NOTE: The meaning of "vâra" is not clear
6	    #3 (parent #2) [Avestan / Old Persian] refs=BQT:22(Introduction),781; MON5:488 | huvârazmîš, xvarazmîš, xvârizem : One of the original residences of the Aryan people (Airyanemwaejô).  Now it is known as "Khiva" in central Asia between Uzbekistan and Turkmenistan, along the Amu Darya
7	      #4 (parent #3) [Persian] refs=BQT:781,805; MON5:488,491; KLN:49 | Xârazm, Khârazm «خوارزم» : a city in central Asia, modern Khiva ; Xârazmî «خوارزمی» : from Khârazm ; Xîveh, Xîvaq «خیوه۱، خیوق» : Khârazm | NOTE: Khârazmî is surname of Abŭ Ja`far Mohammad ebn Musâ, the great mathematician of the ninth century. His great work "Al-Jabr wal Moqâbeleh" introduced the Arabic numerals and Algebra in Europe.
8	        #5 (parent #4) [Arabic] refs=None | Al-Xwârazmî : the ninth century mathematician
9	          #6 (parent #5) [Middle Latin] refs=AHD:33; KLN:49 | algorismus : the Arabic system of numerals
10	            #7 (parent #6) [French] refs=AHD:33 | algorisme, algorithme
11	              #8 (parent #7) [Persian] refs=VOP:17 | âlgoritm «آلگوریتم» : algorithm
12	              #9 (parent #7) [English] refs=KLN:49 | algorism, algorithm
13	#10 (parent #0) [Old Persian] refs=KNT:175,176,177 | u-vaxštra : well grown, former king of Media ☞Aueg ; u-xšnav : well satisfied, happy ; u-kâra : good army ☞Koro ; u-câra : well done ☞Kwer ; u-tâna : with good extension (children) ☞Ten 1 ; uv-aspa : with good horses ☞Ekwos
14	  #11 (parent #10) [Persian] refs=KNT:177 | Hovaxšatar «هوخشتر» : a former king of Media
15	#12 (parent #0) [Old Persian] refs=KNT:175,176,177 | u-frašta : well investigated ☞Perk 1 ; u-barta : well born, esteemed ☞Bher 1 ; u-martiya : containing good men ☞Mer 2 ; ŭv-nara : having good men ☞Ner 1 ; u-ratha : having good chariots ☞Ret ; uv-asštika : good spearmen ☞Eres 2
16	
```


## [2026-09-14T03:08:30.292Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-485.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-14T03:08:30.347Z] TOOL RESULT

```
{
  "pdf_page": 485,
  "book_page": 455,
  "entries": [
    {
      "root": {
        "name": "Su 1, Esu, Wesu",
        "lang": "Indo-European",
        "refs": "POK:342,1037,1174; KLN:548",
        "gloss": "well, good"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:175",
          "words": [
            {
              "translit": "hu, u, uv",
              "gloss": "good",
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
          "lang": "Avestan / Old Persian",
          "refs": "KNT:177",
          "words": [
            {
              "translit": "u-vâra-zmi",
              "gloss": "good ... land",
              "script": null,
              "see": [
                "Ghdhem"
              ]
            }
          ],
          "script_extra": null,
          "note": "The meaning of \"vâra\" is not clear",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:22(Introduction),781; MON5:488",
          "words": [
            {
              "translit": "huvârazmîš, xvarazmîš, xvârizem",
              "gloss": "One of the original residences of the Aryan people (Airyanemwaejô).  Now it is known as \"Khiva\" in central Asia between Uzbekistan and Turkmenistan, along the Amu Darya",
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
          "lang": "Persian",
          "refs": "BQT:781,805; MON5:488,491; KLN:49",
          "words": [
            {
              "translit": "Xârazm, Khârazm",
              "gloss": "a city in central Asia, modern Khiva",
              "script": "خوارزم"
            },
            {
              "translit": "Xârazmî",
              "gloss": "from Khârazm",
              "script": "خوارزمی"
            },
            {
              "translit": "Xîveh, Xîvaq",
              "gloss": "Khârazm",
              "script": "خیوه۱، خیوق"
            }
          ],
          "script_extra": null,
          "note": "Khârazmî is surname of Abŭ Ja`far Mohammad ebn Musâ, the great mathematician of the ninth century. His great work \"Al-Jabr wal Moqâbeleh\" introduced the Arabic numerals and Algebra in Europe.",
          "quote": {
            "text": "حافظ تو ترک غمزۀ خوبان نمی‌کنی - دانی کجاست جای تو خوارزم یا خجند",
            "poet": "Hâfez"
          }
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {
              "translit": "Al-Xwârazmî",
              "gloss": "the ninth century mathematician",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Middle Latin",
          "refs": "AHD:33; KLN:49",
          "words": [
            {
              "translit": "algorismus",
              "gloss": "the Arabic system of numerals",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "AHD:33",
          "words": [
            {
              "translit": "algorisme, algorithme",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "VOP:17",
          "words": [
            {
              "translit": "âlgoritm",
              "gloss": "algorithm",
              "script": "آلگوریتم"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "KLN:49",
          "words": [
            {
              "translit": "algorism, algorithm",
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
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:175,176,177",
          "words": [
            {
              "translit": "u-vaxštra",
              "gloss": "well grown, former king of Media",
              "script": null,
              "see": [
                "Aueg"
              ]
            },
            {
              "translit": "u-xšnav",
              "gloss": "well satisfied, happy",
              "script": null
            },
            {
              "translit": "u-kâra",
              "gloss": "good army",
              "script": null,
              "see": [
                "Koro"
              ]
            },
            {
              "translit": "u-câra",
              "gloss": "well done",
              "script": null,
              "see": [
                "Kwer"
              ]
            },
            {
              "translit": "u-tâna",
              "gloss": "with good extension (children)",
              "script": null,
              "see": [
                "Ten 1"
              ]
            },
            {
              "translit": "uv-aspa",
              "gloss": "with good horses",
              "script": null,
              "see": [
                "Ekwos"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "KNT:177",
          "words": [
            {
              "translit": "Hovaxšatar",
              "gloss": "a former king of Media",
              "script": "هوخشتر"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:175,176,177",
          "words": [
            {
              "translit": "u-frašta",
              "gloss": "well investigated",
              "script": null,
              "see": [
                "Perk 1"
              ]
            },
            {
              "translit": "u-barta",
              "gloss": "well born, esteemed",
              "script": null,
              "see": [
                "Bher 1"
              ]
            },
            {
              "translit": "u-martiya",
              "gloss": "containing good men",
              "script": null,
              "see": [
                "Mer 2"
              ]
            },
            {
              "translit": "ŭv-nara",
              "gloss": "having good men",
              "script": null,
              "see": [
                "Ner 1"
              ]
            },
            {
              "translit": "u-ratha",
              "gloss": "having good chariots",
              "script": null,
              "see": [
                "Ret"
              ]
            },
            {
              "translit": "uv-asštika",
              "gloss": "good spearmen",
              "script": null,
              "see": [
                "Eres 2"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}=== MATRIX ===
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:08:38.064Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"--- 484? ---\" && ls data/verification/page-48*.json 2>/dev/null; echo \"--- refs ---\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','KNT','BQT','MON','AHD','VOP']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-14T03:08:39.136Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
--- 484? ---
data/verification/page-48.json
--- refs ---
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
```


## [2026-09-14T03:08:52.683Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK esu ===\"\ngrep -n \"esu-s\" POK_01.txt | head -20\necho \"--- POK su- ---\"\ngrep -n -E \"^su-|su-s|u̯esu-|uesu\" POK_03.txt | head -30\necho \"=== KNT u- entries ===\"\ngrep -n -E \"uvārazmi|uvarazmi|Uvāraz|Uvaxštra|uvaxstra\" KNT.txt KNT_full.txt | head -30"
}
```


### [2026-09-14T03:08:52.776Z] TOOL RESULT

```
=== POK esu ===
5144:Zum  obigen  vielleicht: esu-s  (:  SU-)  ,gut,  tüchtig'.
--- POK su- ---
624:per-tu-,  por-tu-f  Gen.  pr-teus  ^Durchgang,  Furt':  av.  pdvdtu-s  m.  f. (urar.  *prtü-s)  und  pdsu-s  m.  (urar.  *pftu-s)  ^Durchgang^  Furt,  Brücke' niu-pdrdd-wa-  ,gut  zu  überschreiten'- =  ^Euphrat') ;  lat.  portus,  -üs  ,Haus- türe^(XII  tab.); , Hafen',  angi-portus  ,enge  Fassage,  Nebengäßchen';  daneben ä-St.  porta  , Stadttor,  Tor'  =  osk.  \jp']urtam\  illyr.  ON  Nau-portus]  gall. ritu-  ,Furt'  in  Ritumagus,  Äugustoriturrij  acymr.  ri7,  ucymr.  rhyd,  corn. rit  ,Furt';  ahd.  fürt,  ags.  ford  ,Furt'  (hochstufig  aisl.  fjordr  ,enger  Meer- busen' aus  ^^per-tu-s)]  daneben  f.  i-St.  ira  nhd.  ON  Fürth  (^furti-).
1160:su-rdzina  ,gute  Ordnung';
1596:,in  söde';  Nomen  agentis  als  2.  Kompos.-Glied:  ai.  apsu-sdd-  ,der  in  ^en  ' Wassern  wohnt^  av.  maidyöi-säödm  (Akk.)  ,d.er  in  der  Mitte  wohnt';  \^^: prae-ses  , Vorsitzender',  de-ses  ,träge'  =  air.  dM  ds.  (i-Flexion  sekundär),'" zu  deess  ^Trägheit'  (*de-sed-tä)]  mit  lat.  suhsidium  ^Unterstützung'  vgl.  air[ ^ fothae  m.  n.  , Grundlage^  aus  *upo-sodiom,  zu  air.  swid^e;  fei
2501:alit.  skastu,  sTcatau,  skasti  , springen,  hüpfen',  su-skantü,  -skaciaüj  -shäik ,aufhüpfen';
2962:Fem.  *sf:  gr.  l  ,sie'  (Soph.),  air.  sl  ,sieS  got.  si,  ahd.  sl,  si  ,sie';  dazu nach  Rosenfeld,  Forsch,  u.  Fortschr.  29,  176  schwachtonig  si  in  urnord. si-ainaR  Jener',  sa-si  , dieser',  su-si  , diese*,  pat-si  , dieses';  genus-indifferent sind  Akk.  ai.  slm,  av.  hlm,  ap.  sim.
3398:jjjs  untere  Ende  der  Lanze' ;  aisl.  stümi  ,ein  Riese' ;  mhd.  stünende  ^wider- ggtzlicli^  nhd.  staunen  als  ^starr  blicken';  keine  Belege  für  diese  Ablaut- stufe  sind  hingegen  die  w-St.  ai.  su-sthü  Adv.  ^gut,  schön',  anu-sthu,  anu- flhuyä  ^sogleich';
5907:WP.  I  307  f.,  Vendryes  RC.  35,  89  f.,  WH.  II  769;  wohl  zu  uesu-  ,gut'.
5956:uesu-  ,gut*.
5957:Ai;   vdsu-   ,gut'   (dazu   vasvi  ,Nacht*),    vdsu   n.   ,Gut,   Besitztum,  Habe, Reichtum*  (das  Subst.  nach  Akzent  und  Ablaut  das  primäre),  av.  va^hu', vohu  ds.,  ai.  vaslyän  ,besser',  vasistha-  ,best',  av.   vahyäj  vahiStd  ds.J  alt- illyr.  Ves-clevesy  vgl.  ai.  vdsu-sravas-]  germ.  in  Eigennamen,  z.  B.  Wi9U-r%h, -mär,  auch   Wisi-Gothae-,  gall.  in  Eigennamen  wie  Bello-,  Sigo-vesuSf  Fe#u« avus,  air.  *feb  (nur  in  den  Kasus  obliqui  belegt,  z.  B.  Dat.  Sg.  feib)  ,Vor- trefflichkeit*  aus   *uesu-ä,  febas  , Vortrefflichkeit*,  *fehtUj   Gen.  febtad  gl. jSubstantiae* ;  ab  laut.  air.  fö  ,gut,  Güte^  (*wosw-);  daneben  *U68U-  in  ir,/iu , würdig',  cymr.  gwiw  ds.,  bret.  gwiou  ,fröhlich^,  gall.  ülsu-rix]  über  V**^" in  asian.  Sprachen  s.  Bessert  Mitteil.  Inst.  Orientf.  2,  78 ff.; daneben  eus-  (mit  Metathese  wie  in  gr.  sdgog  aus  *J^€Qog)  in: got.  iusiza  , besser',   iusila  ,Erholung,  Erleichterung*   (nach  Wissmann, D.  alt.  Post verb.  d.  Germ.  72  ff.   Postverbale  zu  *iusilon^  wie  inilo  lEnt-, schuldigung,  Vorwand*  zu  Hnilon)]  aksl.  unje  ,besser*  (Kompar.  zu  einem *uno-  aus  *eus-no-)j
=== KNT u- entries ===
KNT.txt:2132:Nom. Sg.: Uvárazmiy Uvārazmiš, Baztriš; Harau- valiá (Skt. sárasvati), Sikalyaluvatis; apis (in айт = dpif-&m), BU ‘earth’ (ideogram only).
KNT.txt:3985:7 : Uvaxštrahya
KNT.txt:5212:Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
KNT_full.txt:9278:Nom. Sg.: Uvárazmiy Uvārazmiš, Baztriš; Harau- 
KNT_full.txt:18852:7 : Uvaxštrahya 
KNT_full.txt:24748:19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, 
KNT_full.txt:24749:DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї.
```


## [2026-09-14T03:09:00.966Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor pat in ['Uvārazmi- sb','Uvaxštra','u- ‘good','hu- ','Uvāraz']:\n    pass\n# find offsets\nfor needle in ['Uvārazmi- sb','Uvaxštra-','Uvnara','u-vaxštra']:\n    i=t.find(needle)\n    print(needle, i, 'leaf', t[:i].count('\\f') if i>0 else None)\nEOF\necho \"=== around 5212 ===\"\nsed -n '5200,5230p' KNT.txt"
}
```


### [2026-09-14T03:09:02.068Z] TOOL RESULT

```
Uvārazmi- sb -1 leaf None
Uvaxštra- -1 leaf None
Uvnara -1 leaf None
u-vaxštra -1 leaf None
=== around 5212 ===
ре
LEXICON
tuva- refi. pron. ‘self? and poss. adj. ‘own’ (8118.1V): Av. z"a-, Skt. sva-, Gk. € and ds, Lt. sé and suos, pIE *sye and *suos (5148.11); in wada-, wvăipašiya-, wdmar kyu-.
watpasiya- adj. ‘belonging to self’ (wrongly ‘wayward’, Sen 246), nt. as sb. ‘own possession’: Ау. x’aépaibya- ‘own’; OP uvai-, nom. of wa-, as in Skt. svay-dm ‘self? (MB Gr. §293), + pAr. *natia-, formed on pIE *poti-, Av. рой ‘master, husband’, Skt. pati-, Gk. тоса ‘husband’, Lt. potis ‘able’, Lith. pats ‘self’: pIE *suoi-potio- (858, §143.- II, $152.11, $161.1Ib). watpasiyahya gsn. DNb 15.
 wüipasiya-, same as preceding, with vriddhi in initial syllable (§126; MB Gr. §298); but wai- may be an error for uvai-, or wai- for wäi- (§53). uvdipasiyam asn. DB 1.47.
‘UvaaStra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-tš-tar-ra, АКК. ú-ma-ku-iš- lar, Gk. Kva£ápys. From u- ‘good’ + varštra- ‘growth’ ($9.11, $79, $148.11), to vaxi-, Av. vazš-, Skt. vaks-, Gm. wachsen, N Eng. wax ($102): 'Hav- ing good growth’ ($164.11, IV). So ВЫ. AiW 1836; but Hz. АрІ 209 interprets ‘having good oversight’, to Av. aiwy-axrstrat (dat.) ‘oversight’ (otherwise Hüsing, OLZ 2.139-40). Стах аһу gsm. DB 2.15f, 81.  Uvaxstrahya (S86.IVb) DB 4.19, 22; DBe 7; ОВр 9f.
Uvaja- Uvajiya-, read Uvja- Uvjiya-: see Uja- Ujiya-.
wadd- sb. ‘abode’, vriddhi-form to Skt. svadha- ‘innate character’, from wa- ‘own’ + dhà- ‘make’ ($142; OP wa- + ?dà-) ; in PaiSiyduvdda-, q.v.
Uvadaicaya- sb. ‘Uvadaicaya’, a town in Persia (§159): Elam. ma-ie-gi-i& Uvadaicaya nsm. DB 3.51.
uvamar Siyu- adj. ‘(having self-death = ) dying by one’s own hand’, either by intent or by acci- dent: wa- ‘own’, with vriddhi, + *mptiu- ‘death’, Av. marabyu-, Skt. mptyii-, to mar- ‘die’ (S30, $80, 8113, §122, §126, $152.1II, §153.1, $161а); used of Cambyses, who, acc. to Herod. 3.646, died from the after-effects of an accidentally self- inflicted wound. This interpretation is strongly supported by the Akk. and (although the exact Elam. text is somewhat in doubt) the Elam. ren-
177
derings. So KT 9; Tm. Lex. 78; Wb. KIA 17 with note; Hz. BSOS 8.589-97 and Ар! 216-9; W. Hinz, Altpers. Wortschatz 141. Not to be taken with W. Schulze, РАЖ 1912.685-703, 1918.331- 2, as ‘by a natural death’, citing semantic par- allels in other languages; who is followed by MB Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus nsm. DB 143.
Uvárazmi- sb. ‘Chorasmia’, a province of the Persian Empire: Elam. ma-ra-18-mi-18, Akk. þu- ma-ri-iz-ma-’, Gk. Xwpaspin, Av. asf. z'airizom. From u- ‘good’ + vāra- ‘0° (8126, 5148.111), + ami- (§95, $120, 5152.) to zam- ‘land’. See also Uvürazmiya-. Uvirazmiy nsf. (SI79.1; Lg. 19.223) DB 1.16, DPe 16f; Uvārazmiš DNa 231, DSe 22°, DSm 9°, XPh 21f. Uvārazmiyā арзї. DSf 39f.
Uvürazmiya- adj. ‘Chorasmian’: deriv. to pre- ceding ($144.11). (Uvarajzm*ya (822) nsm. APP 8. |
war Stika- sb. ‘good spearman’: u- ‘good’ + drStika- ‘spearman’ (8126). шаг Ка пат. DNb 44.
wasabdra- sb. ‘good horseman’: u- ‘good’ + asabāra- ‘horseman’, with vriddhi ($126). uvāsa- bara nsm. DNb 42.
waspa- adj. ‘having good horses’: u- ‘good’ ($118.1V, $140.1V) + aspa- ‘horse’ ($9.11). waspä nsf. AmH 6; DPd 8. uvaspam asn. DSf 11; DSp 3°; рле 4^; for asf. AsH 10 (§52.[11). waspd apn. as sb. ‘good horses’ DSs 5°.
Uvja- Unjiya-, see Uja- Ujiya-: cf. Wb. МОЕ 7.43, Schaeder ShHPAW 1931.636.n3.
twnara- sb. ‘skill, accomplishment’: ad}. form- ation to pAr. *su- ‘good’ + *nar- ‘man’ (§142, 5148.1, V), = ‘having the good quality of a man’, Av. hunara- ‘ability, skill’, Skt. sümára- ‘glad, joyous, merry’, with vriddhi of the first vowel in OP and Skt. to show the derivative nature (523.11, $126: Lg. 15.173, JNES 4.51-2: cf. Hz. RHRel. 113.30, ApI 200-6, who aecepts this meaning but seeks another etymology, as does also Pisani, Riv. Stud. Or. 19.93-4). düvnarü npn. DNb 45, 51. üwnaraibis ipn. DNb 48.
ustaSand- (usta$na- Bv. Ст. $294) sb. 'stair-
178
case’: us- (see ud-, $84, $85) + tašanā- (§102), deriv. (5147 1) to root taš- ‘cut, fashion’ (see under tax’-), pIE *ud-tekbend-. ustaSandm asf. А?Ра 22 (as nom., §56.V).  [usta]canám (§49b) Ае 5f.
ušabāri- adj. ‘camel-borne’: usa- ‘camel’ ($79, $130), Av. ustra- (MB Gr. $109; cf. Justi, GGA 1882.488), + bāri- ‘borne by’ (8122, $126, $51521, 6160.1е), to root bar- ‘bear’. Cf. Jn. Indo-Iranian Studies Sanjana 18-20. ušabārim DB 1.86f.
uši- sb. dual ‘two ears, hearing, understand- ing’ (cf. JNES 4232; Hz. RHRel. 113.30, ApI 342-4): LAv. dual «&, cf. Gk. ois, Lt. auris, Gt. ausó. иу ndn. ($189) DNb 28, [р-а adn. ($136) DNb 32. ušībiyā idn. ($189) DNb 37; udiyd idn. (with sg. ending, $189; Lg. 19.224—5) DNb 35.
uška- adj. ‘dry’; nt. as sb., ‘land, mainland’: Av. hu&ka- ‘dry’, NPers. zusk, Skt. $ügka-, Sisyatt ‘dries’, Lith. saüsa-s ‘dry’, NEng. sere, sear ($146.1). uškahyā gsn. DPe 13.
ushamaranakara- sb. ‘good warrior’: u- ‘good’ + hamaranakara- ‘warrior’ (§140.VI). ushamara- nakara nsm. DNb 34.
uzma- adj. as sb. ‘that which is up from the earth, stake’: from ud- ‘up’ + zma- to zam- ‘earth’ ($84, $95, $120, $130, §142, 5148.11, VI): other- wise Wackernagel, KZ 61.208; Lommel, OLZ 37.180.n2; König, RuID 72. uzmayā-patiy lsn. DB 2.76, 91; 3.52, 92.
ka- interrog.-indef. pron. ‘who’: Av. Skt. ka-, Gk. то-, Lt. quo-, NEng. wha-t, pIE *q*o- ($201). See also Ка, -katy, ci- (§132.2). With encl. -ciy, ‘any’: kaš-ciy (89. VI, $09, $105) nsm. DB 1.49, 53; DSe 37.
kā, generalizing particle after 2d pers. pron.: probably isn. of ka- ($191.11; Kern ap. Caland, 1. Syntax der Pron. im Av. 47; Kieckers, Etymol. Miszellen 1934.135; otherwise Gray, JAOS 23.60). DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46.
-katy, emphatic encl. particle, m ada-katy (q.v.): probably lsn. to ka- ($191.11), ef. Gk. то ‘somewhither’ (Bv. Gr. $336 takes as *ka*<4, cf. naiy from *na-19).
kaufa- sb. ‘mountain’: Av. kaofa-, Phl. kof,
```


## [2026-09-14T03:09:18.746Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"u- adj|ufra|ubart|umart|uratha|ucāra|ukāra|utāna|uxšnau|uxsnau|ušnau|ukara|ucara|utana\" KNT.txt | head -30"
}
```


### [2026-09-14T03:09:18.815Z] TOOL RESULT

```
1337:pIE *su-prek-to-, OP ufrašta- ‘well punished’, cf.
1534:*prek- in ufrastam ‘well punished’, *prk- in aparsam ‘I punished’.
2028:Acc. Sg. martiyam, xsdyatiyam, kăram, hamict- yam; Kabiziyam; Pársam, Madam, Sugdam, Mudrayam, Uvjam, Arminam, Asagartam, ufras- tam.
2043:Acc. Pl. martiyd, xSayatiyd, hamigiyà, Saké, ауа, ufra&ta.
2075:айа DB 1.28, XPh 49, 52, when used with pari-ay- ‘respect’, is probably inst. rather than abl., because of the lack of prep. Ласа; note that the text of DSe 37-9, as now restored, gives no support for the abl. in the other passages, despite my remarks JAOS 54.46, Lg. 13.308, JAOS 58.117. On inst. sg. karšā, loc. sg. karšayā, nt. асе. casam, acc. pl. ufrasta-diy, see Lex. s.vv.
2166:For forms of tanūš, dahydusS, uxsnaus, naus, see
2899:DNb 26 z£nula amiy, cf. the adj. in the parallel clause uxsnaus атту, in line 27.
3431:3 : Cispais : xšãyaðiyahyā : риса ; HaxdmaniSah 4 ув : парӣ : Вапу : Áriyáramna : xšāyaðiya 5 :iyam : dahyau§ : Parsa : tya : adam : dárayá 6 miy : hya : uvaspà : umartiyü : mana : baga 7 : vazraka : Auramazda ; frábara : vašnā : Au 8 ramazdàáha : adam : xXàyafiya : iyam : da 9 hyauS : amiy : 80у : Anyaramna
3444:9 агза : mand : рага : tya : ukāram 10 : uvaspam : vašnā : Auramazdaha : im 11 ām : dahyaum : dàrayàmiy : mam :
3479:22 bartam : abaram : hya : апка : аһа : avam : ufrastam : aparsam : vašnā : Auramazda 23 ha : ima : dahyáva : tyanà : manā : dita : apariyàya : yaðāšām : hacima : абаһ
3832:38 patipayauvi : martàya : hya : draujana : ahatiy : avam : ufrastam : pars : ya
3857:63 yàha : bagitha : tyaiy : hatiy : yaf : палу : апка : Sham : пау : draujana : арат : na 04 iy : zürakara : &ham : поту : adam : поталу : tauma : upariy pev omis ~ 65 yam : naiy : škaurim : naiy : tunuvatam : züra : akunavam : martiya : һуа : hamata 66 xšatā : manā : vityà : avam : ubartam : abaram : hya : viyanüfaya : avam : ufrasta 67 т: aparsam | : фу : Юйгауауац$ : xSayafiya : tuvam : К : xšāyaðiya :
3859:69 iy : avaiy : mā : dauštā : biya : ufraštādiy : eri : (абу : Dara
3885:%A blank space of one character between the di- vider and the following @ #, KT. 2 [akunavam] WB, KT; but KT state that the traces of the last letter are pos- sibly those of &, which leads to a restored akunauS (во also RL), of which Auramazda would have to be the implied subject (ef. Oppert’s restoration, IdA 150). It is more probable that the phrase is here as in DB 5.17, 29, 38, and that akunavam is correct. ? ah*y^ RL, KT; first correctly normalized ёлу by Tm. VS 1.30. So also 4.68, 72, 87. 9 ufraštam КТ. ? manfiydhy} Opp. МА, ete., KT; man(iyahay) Tm. after DPe 20; man[ryáhaiy] Kent, since there is no reason to assume here the defective writing of DPe. |
3889:Маг ат Foy KZ 35.45 (conj.), Jn., KT, for КІ в in- correct, abiStam. 9*5 Definitive жи е by Cameron, upariy | dlyalm [:] пабу : Sakaurim : naty : t[u]nuvatam, confirming uparty[üyam] of WB, HK, Wb. KIA; Sakaurim WB, Jn., fakauri[m] KT, Tm., Wb. KIA (read rather Skaurim, see Lex. s.v. skaudi-); [nay] Spiegel; ... uvata Rl., ]nuvatam Jn., t{ulnuvatam KT. ® zuku RL, züra Ri. later.  hya WB (from Rl.'s squeezes), Jn.; omitted by KT. #06... ВІ; 2076 WB, Jn; 090 KT. 6 piyaná[sa]ya WB, KT, HK, Tm., Wb. KIA; correctly viyana\balya Foy KZ 35.46. “avam : ufrasta- WB; wrongly ava : ufrasta- KT. ® [zu]rakara : ++ : KT, with possibly traces of two characters in the gap; but, Cameron finds [zuü]rakara : ahat- with only а gap for опе
3891:character, perhaps miswritten and erased, after the divider. * daustà WB, KT. 9 ...à KT; biylà WBn, НК, Tm. © atifraštādiy RL; aifrastádiy WB, Jn.; ufrastadvy KT.
3893:8-6 Оп the Helpers of Darius, see Hist. App. IFI. 83 (Лапа : тата WB; Ийла : nlàma, though the middle gap is hardly adequate for two characters and a divider, KT; perhaps the divider was not engraved because it followed an identical stroke as final part of m^. s Daduhyahya WB; [Dadulhyahya KT; (Раа WBn; [Datu|hyahya or [Daduva]hyahyá Wh. KIA; Dat- fupahyahyă Cameron, with і" not absolutely certain and vw damaged but sure. 8-8 {уйт : imatsdm : martiya : и | ++: imim: ...: G++: риат) KT; martiyaná | m : taumdm : {ubart}ém WBn, agreeing with traces noted by KT and slightly emending some other characters.
4048:8 ra : hyà : naibá : uvaspa : umarti
4328:3 Qatiy : Dérayavaus : XS : AMmaty : z$agam : frábara : 4 tya : vazrakam : tya : umartiyam : mdm : z5yatvyam :
4346:9 bam : tya : urafaram : waspam : umartiyam
4400:3 à : һуа : Darayavaum : XSyam : akunaus : hya : Dárayavahaus : Хуй : xfaga 4 m : frübara : tya : vazrakam : tya : waspam : umartiyam : adam : Darayavaus :
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5189:ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
5191:ubarta- adj. ‘well-borne, lifted, esteemed’: u- well’ + barta- ‘borne’, pte. to bar- ‘bear’, pIE *su-bhrio- (830, $122, §242.1). ubartam asm. DB 1.21f;4.66.  ubartàm asf. DB 4.88. On meaning, cf. Altheim, ZII 3.33-5: hardly as taken by König, RulD 69.
5193:umartiya- adj. 'eontainig good men’: u- ‘good’ + martiya- ‘man’. umartiyd nsf. AmH 6; DPd 8f. wmartiyam asn. Р 11f; DSm 4°; DSp 3°; DZc 4.
5209:uvamar Siyu- adj. ‘(having self-death = ) dying by one’s own hand’, either by intent or by acci- dent: wa- ‘own’, with vriddhi, + *mptiu- ‘death’, Av. marabyu-, Skt. mptyii-, to mar- ‘die’ (S30, $80, 8113, §122, §126, $152.1II, §153.1, $161а); used of Cambyses, who, acc. to Herod. 3.646, died from the after-effects of an accidentally self- inflicted wound. This interpretation is strongly supported by the Akk. and (although the exact Elam. text is somewhat in doubt) the Elam. ren-
5380:ucara-. cdra- (5126), see ucüra-.
5554:-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
5658:paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; Азра 6, 7.
5699:fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
```


## [2026-09-14T03:09:33.543Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=5140 && NR<=5215 && (/^1[0-9][0-9]$/ || /^ *1[0-9][0-9] *$/)' KNT.txt\necho \"--- show line numbers of bare page numbers 170-180 ---\"\ngrep -n -E \"^ *17[0-9] *$\" KNT.txt | sed -n '1,40p'"
}
```


### [2026-09-14T03:09:34.873Z] TOOL RESULT

```
175
176
177
--- show line numbers of bare page numbers 170-180 ---
5047:170
5071:171
5083:172
5118:173
5125:174
5165:175
5173:176
5210:177
5220:178
5259:179
```


## [2026-09-14T03:09:46.100Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor needle,label in [(\"u- insep. prefix\",\"u- prefix\"),(\"Uvārazmi- sb\",\"Uvarazmi\"),(\"‘UvaaStra- sb\",\"Uvaxstra\"),(\"umartiya- adj\",\"umartiya\"),(\"war Stika- sb\",\"uvarstika\"),(\"twnara- sb\",\"uvnara\")]:\n    i=t.find(needle)\n    print(label, 'leaf(0-based ff count)=', t[:i].count('\\f'), 'charidx',i)\nEOF"
}
```


### [2026-09-14T03:09:47.456Z] TOOL RESULT

```
u- prefix leaf(0-based ff count)= 197 charidx 705187
Uvarazmi leaf(0-based ff count)= 231 charidx -1
Uvaxstra leaf(0-based ff count)= 199 charidx 713188
umartiya leaf(0-based ff count)= 199 charidx 711596
uvarstika leaf(0-based ff count)= 200 charidx 715405
uvnara leaf(0-based ff count)= 200 charidx 715903
```


## [2026-09-14T03:10:14.827Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5155,5175p' KNT.txt | cat -A | sed -n '1,200p' | cut -c1-120 | head -40"
}
```


### [2026-09-14T03:10:14.889Z] TOOL RESULT

```
isti- sb. M-bM-^@M-^Xsun-dried brickM-bM-^@M-^Y (5152.11, 5179.11): Av. tM-EM-!tya-, NPers. 110, Skt. istaka-, Medieval 
M-PM-5M-QM-^BM-PM-0 or lismar\uy asn., of uncertain mean- ing, possibly M-bM-^@M-^X(gold) inlayM-bM-^@M-^Y (Cameron, Per
IzalM-CM- M-CM-<- sb. 'Izala', a district in Assyria (86, $107): Elam.?5-$1-la.  TizaljM-CM-$ nsf. DB 2.58, as re- store
^u- insep. prefix M-bM-^@M-^Xgood, wellM-bM-^@M-^Y (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-M-QM-^CM-PM-8M-QM-^U 
ukdra- adj. M-bM-^@M-^Xhaving good people or armyM-bM-^@M-^Y: from u- M-bM-^@M-^XgoodM-bM-^@M-^Y + kM-DM-^Ara- M-bM-^@M-
ucsnav- adj. M-bM-^@M-^Xwell satisfiedM-bM-^@M-^Y ($142): from u- M-bM-^@M-^XgoodM-bM-^@M-^Y + zM-EM-!nav- M-bM-^@M-^Xsa
."ucM-CM-<ra- adj. M-bM-^@M-^Xwell done, successfulM-bM-^@M-^Y, as sb. nt.$
M-bM-^@M-^Xgood deedM-bM-^@M-^Y: from u- + cM-CM-#ra-, to root kar- M-bM-^@M-^XdoM-bM-^@M-^Y / (809, M-BM-'122, M-BM-'12
uca$ma, incorrect reading for M-QM-^AM-QM-^B? = M-QM-^AM-PM-0M-PM-0M-QM-^B; see casa-.$
^Uja- ^Uvja (83.1) sb. M-bM-^@M-^XElam, SusianaM-bM-^@M-^Y, a province of the Persian Empire ($166.M-PM-^_); also as$
175$
ethnic, M-bM-^@M-^XElamite, SusianM-bM-^@M-^Y: Elam. hal-tam-ti, Akk. e-lam-mat, ef. MPers. M-PM-^]M-PM-8? (Uja distinct
^Ujya- *Uvjiya- (144.11) adj. 'Elamite, SusianM-bM-^@M-^Y: deriv. of preceding. Uvjiya M-PM-?M-PM-5M-QM-^B. DB 4.10, 5.5
ula (for M-QM-^HM-PM-9, $36.I) conj. M-bM-^@M-^XandM-bM-^@M-^Y (52911-00): Av. ula, Skt. M-QM-^H, Gk. Hom. -M-CM-:re M-b
M-QM-^IM-PM-9 AsH 13; DB 1.34 bis, 34f, 41 ter, 46 bis, 47, 57, 67, 77, 85; 2.3, 4, 18, 74 ter, 77, 81f, 87, 88, 89, 92;
utM-CM-<-maiy M-PM-^PM-PM-^WM-PM-^] 12; DB 4.46 (visible to Cameron; ef. note ad loe.); DPh 10; DNa 52f; DH 8; XPb 29; X
ula-maiy (M-BM-'135) DSe 51M-BM-0; DSf 58; DSj 6M-BM-0; DSt 9M-BM-0; XPa 15, 18f; XPd 18f; XPf 41, 45f; XPg 14; XPh 58 (
UtM-CM-<na- sb. M-bM-^@M-^XOtanesM-bM-^@M-^Y, ally of Darius against Gaumata: Elam, fu-ud-da-na, Akb &M-BM-;mi-it-la-na-
176$
Gk. 'M-CM-^\rM-CM-!vgs; perhaps u- M-bM-^@M-^XgoodM-bM-^@M-^Y + tM-DM-^Ana- to root tan- M-bM-^@M-^Xstretch, extendM-bM-
utava- adj. M-bM-^@M-^Xstrong, in healthM-bM-^@M-^Y: u- M-bM-^@M-^XgoodM-bM-^@M-^Y + deriv. of tav- M-bM-^@M-^Xbe strong
```


## [2026-09-14T03:10:25.886Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"LEXICON\" KNT.txt | sed -n '1,60p'"
}
```


### [2026-09-14T03:10:25.964Z] TOOL RESULT

```
44:GRAMMAR TEXTS LEXICON
128:PART HI. LEXICON
4908:PART III. LEXICON
4932:LEXICON
4971:LEXICON
5017:LEXICON
5062:LEXICON
5105:LEXICON
5153:LEXICON
5201:LEXICON
5246:LEXICON
5305:LEXICON
5351:LEXICON
5403:LEXICON
5448:LEXICON
5504:LEXICON
5546:LEXICON
5589:LEXICON
5636:LEXICON 195
5678:LEXICON
5712:LEXICON 199
5744:LEXICON
5783:LEXICON 203
5833:LEXICON | 205
```


## [2026-09-14T03:11:02.413Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\ndef leafof(f,needle,occ=0):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    idx=-1\n    for _ in range(occ+1):\n        idx=t.find(needle,idx+1)\n        if idx<0: return None,None\n    return t[:idx].count('\\f'), t[max(0,idx-300):idx+900].replace('\\n',' ')\nfor f,n in [('POK_01.txt','esu-s'),('POK_03.txt','uesu-  ,gut*'),('POK_03.txt','su-')]:\n    l,ctx=leafof(f,n)\n    print('==',f,n,'leaf',l)\n    print(ctx[:700])\n    print()\nEOF"
}
```


### [2026-09-14T03:11:03.446Z] TOOL RESULT

```
== POK_01.txt esu-s leaf 355
nheit' ^ u.  dgl. ;  M über  das  vielleicht  hierher  gehörige  gr.  icr-d-lög  ,tüchtig,  gut,  glücklich*,  '^ dor.  iaXög,  arkad.  iaXög  vgl.  Schwyzer  Gr.  Gr.  I  5335,  Specht  Dekl.  256.  | WP.  I  160 f.,  Schwyzer  Gr.  Gr.  I  676ff.,  Trautmanu  71,  usw.  « Zum  obigen  vielleicht: esu-s  (:  SU-)  ,gut,  tüchtig'. Gr.  ivg,  '^vg  ,tüchtig,  gut',  Adverb  e-5   (Akk.  n.),  Präfix  ed-  gehört  zu hitt.  a-a§-§u-u§  (assus)  ,gut';  zum  a-  s.  Pedersen  Hitt.  167  u.  Anm.; vielleicht  als  Schwundstufe  dazu  (Friedrich  IF.  41,  370  f.)  das  Präfix  sm-, s.  dort; hierzu  vielleicht  lat.  erus  ,Herr',  fem.  era,  alat.  esa  , Herrin* ; doch  ist  hitt.  i§-ha-a

== POK_03.txt uesu-  ,gut* leaf 418
eähant-  ^Frühjahr'  s.  A.  Goetze  Lg.  27,  471 51,  467  ff.,  F.  Sommer  M.St.z.Spr.  4,  7,  G.  R.  Solta,  S.-Ber.  österr.  Akad.,* Bd.  232,  1.,  16 f.; WP.  I  301,  WH.  II  755,  Trautmann  356,  Vasmer  1,  192,  Frisk  432  f., 605 f.;  wohl  zu  aues-  ,leuchten*,  oben  S.  86 f. uesu-  ,gut*. Ai;   vdsu-   ,gut'   (dazu   vasvi  ,Nacht*),    vdsu   n.   ,Gut,   Besitztum,  Habe, Reichtum*  (das  Subst.  nach  Akzent  und  Ablaut  das  primäre),  av.  va^hu', vohu  ds.,  ai.  vaslyän  ,besser',  vasistha-  ,best',  av.   vahyäj  vahiStd  ds.J  alt- illyr.  Ves-clevesy  vgl.  ai.  vdsu-sravas-]  germ.  in  Eigennamen,  z.  B.  Wi9U-r%h, -mär,  auch   Wisi-Gothae-,  gall.  i

== POK_03.txt su- leaf 8
der  18.',  gr.  (3xt"w (xa/)  (5sxa,  lat.  octödecim,  ahd.  ahtozehan  18; gr.  (5xTax(5ö'tof,  lat.  octingenti  ^800^ WP.  I  172  f.,  WH.  II  199  f.,  Trautmann  15  f. ökü-s  , schnell',  Kompar.  okiös,  Superl.  ökisto-. Ai.  äsü-  ,schnell',  Kompar.  äälyän,  Superl.  äsistha-,  av.  äsu-  , schnell*, Kompar.  äsyä,  Superl.  äsistö-,  gr.  wxvg,  öjy.Latog,  poet.  wxvraTog,  lat.  öcio7' , schneller',  Superl.  öcissimus  (Positiv  fehlt),  acymr.  di-auc,  ncymr.  di-og^ corn.  di-oc^  bret.  di-ec  , träge',  eigentlich  ,unschnell'; vielleicht  im  Ablaut  zu  ak-y.ok-  , scharf  (oben  S.  18 f.);  dann  könnten lat.  acu-pedius  , schnellfüßig'  und  accipiter  , Habicht
```


## [2026-09-14T03:11:14.510Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,n,occ in [('POK_01.txt','esu-s',0),('POK_03.txt','uesu-  ,gut*',0)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        if n in p:\n            print('==',f,'leaf',i)\n            print('PAGE HEAD:', repr(pages[i][:160]))\n            print('PREV HEAD:', repr(pages[i-1][:120]))\n            print('NEXT HEAD:', repr(pages[i+1][:120]))\n            break\nEOF"
}
```


### [2026-09-14T03:11:15.544Z] TOOL RESULT

```
== POK_01.txt leaf 355
PAGE HEAD: "  sins,   Dat.  Sg.  sentismu,  alit.  Akk.  Sg.  m.  santj,  lit.  s««    ' saficio  (jünger  esqs,  esqs  m.,  esanti  f.),  lett.  eswo^s  , seiend' ;  Gerun"
PREV HEAD: '�stam,  ästäm  :  gr.  hom.  1.  Sg.  ^cc,  2.  Sg.  hom.  att.  ^a&a,  3.  Sg. dor.  usw.  ^g,  PL  hom.  ^[xav,  ^vs, '
NEXT HEAD: ''
== POK_03.txt leaf 418
PAGE HEAD: "t.  vakars  , Abend'  aksl.  vecen, ds.,  wozu  Adv.  aksl.  vhcera  ^gestern'  usw.,  Grundbed.  vielleicht  , Dunkel', zu  lit.  ükanas  ,trübe',   ünkna   ,S"
PREV HEAD: " ysatia'   evövaig  Hes.);\ngot.  wasjaUj  ahd.  werian,  aisl.  veria  ,kleiden*,  ags.  werian  ,ds.,  Kleider tragen*;"
NEXT HEAD: 'e  Bello-,  Sigo-vesuSf  Fe#u« avus,  air.  *feb  (nur  in  den  Kasus  obliqui  belegt,  z.  B.  Dat.  Sg.  feib)  ,Vor'
```


## [2026-09-14T03:11:23.614Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'su-\\s+,wohl', t):\n    print('leaf',t[:m.start()].count('\\f'))\n    print(t[m.start()-200:m.start()+1400].replace('\\n',' '))\n    print('---')\nEOF"
}
```


### [2026-09-14T03:11:24.696Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:11:28.435Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"su-.{0,6},(wohl|gut)\" POK_02.txt POK_03.txt POK_full.txt | head -20\necho \"=== su- hu- ai su ===\"\ngrep -n \"hu-räfrä\\|huuant\\|,gut, tüchtig\\|su-s  ,gut\" POK_03.txt POK_full.txt | head"
}
```


### [2026-09-14T03:11:29.470Z] TOOL RESULT

```
POK_03.txt:5907:WP.  I  307  f.,  Vendryes  RC.  35,  89  f.,  WH.  II  769;  wohl  zu  uesu-  ,gut'.
POK_03.txt:5956:uesu-  ,gut*.
POK_03.txt:5957:Ai;   vdsu-   ,gut'   (dazu   vasvi  ,Nacht*),    vdsu   n.   ,Gut,   Besitztum,  Habe, Reichtum*  (das  Subst.  nach  Akzent  und  Ablaut  das  primäre),  av.  va^hu', vohu  ds.,  ai.  vaslyän  ,besser',  vasistha-  ,best',  av.   vahyäj  vahiStd  ds.J  alt- illyr.  Ves-clevesy  vgl.  ai.  vdsu-sravas-]  germ.  in  Eigennamen,  z.  B.  Wi9U-r%h, -mär,  auch   Wisi-Gothae-,  gall.  in  Eigennamen  wie  Bello-,  Sigo-vesuSf  Fe#u« avus,  air.  *feb  (nur  in  den  Kasus  obliqui  belegt,  z.  B.  Dat.  Sg.  feib)  ,Vor- trefflichkeit*  aus   *uesu-ä,  febas  , Vortrefflichkeit*,  *fehtUj   Gen.  febtad  gl. jSubstantiae* ;  ab  laut.  air.  fö  ,gut,  Güte^  (*wosw-);  daneben  *U68U-  in  ir,/iu , würdig',  cymr.  gwiw  ds.,  bret.  gwiou  ,fröhlich^,  gall.  ülsu-rix]  über  V**^" in  asian.  Sprachen  s.  Bessert  Mitteil.  Inst.  Orientf.  2,  78 ff.; daneben  eus-  (mit  Metathese  wie  in  gr.  sdgog  aus  *J^€Qog)  in: got.  iusiza  , besser',   iusila  ,Erholung,  Erleichterung*   (nach  Wissmann, D.  alt.  Post verb.  d.  Germ.  72  ff.   Postverbale  zu  *iusilon^  wie  inilo  lEnt-, schuldigung,  Vorwand*  zu  Hnilon)]  aksl.  unje  ,besser*  (Kompar.  zu  einem *uno-  aus  *eus-no-)j
=== su- hu- ai su ===
```


## [2026-09-14T03:11:34.657Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"ai\\.  su-|av\\.  hu-|gr\\.  vyirjg|vyiTqg|ůyirjg\" POK_03.txt | head -20\necho \"---\"\ngrep -n \"su-\" POK_03.txt | awk -F: '$1>4500 && $1<5400' | head -20"
}
```


### [2026-09-14T03:11:35.745Z] TOOL RESULT

```
3398:jjjs  untere  Ende  der  Lanze' ;  aisl.  stümi  ,ein  Riese' ;  mhd.  stünende  ^wider- ggtzlicli^  nhd.  staunen  als  ^starr  blicken';  keine  Belege  für  diese  Ablaut- stufe  sind  hingegen  die  w-St.  ai.  su-sthü  Adv.  ^gut,  schön',  anu-sthu,  anu- flhuyä  ^sogleich';
3889:so-  ,wohl,  gut'  als  1.  Kompositionsglied;  su-bhago-  ,beglückend'. Ai.  SU-,  av.  /m-,  apers.  u-,  z.  B.  in  ai.  su-drü-  , starkes   Holz'  su-bhdga- [iClticklich,  beglückend',  av.  hu-baya-  , gutes  Eheglück  gewährend'; ?r.  vyLTJg  ,gesund'  (*su-gni{es  , wohllebend*) ;
3893:lit.  südrus  ,gei\,  üppig*;  aksl.  s^drav^  „tyLrjg"  ,öech.  zdravy  (y^^  *_ ai.  su-drü-)  usw.;  slav.  '^s-bbozhje,  cech.  zhozi  ^Besitztum'  aus  *si>-log^  t^^ suhhdga-,  oben  S.  107);
---
4555:ters-   ,trocknen,  verdorren;   Durst,   dürsten';   trsu-  , trocken',  t^sii    Q^^j zum  Trocknen',  t^sto-  ,trocken,  heiser'.  .    ,,
```


## [2026-09-14T03:11:41.100Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN algorism ===\"\ngrep -n -i \"algorism\\|algorithm\\|al-Khowarazmi\\|Khowarazmi\\|Khwarizmi\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-14T03:11:41.177Z] TOOL RESULT

```
=== KLN algorism ===
KLN_1971.txt:11013:bound together, united’. Cp. algorism. 
KLN_1971.txt:11100:algorism, n., the Arabic system of numerals. — 
KLN_1971.txt:11104:ME. algorisme , fr. OF. algorisme (F. algorith - 
KLN_1971.txt:11105:me), fr. ML. algorismus , from the inexact trans- 
KLN_1966.txt:2173:of  equations,  which  was  the  original  scope  of algebra.  Al-jabr  is  formed  fr.  al-,  ‘the’,  and  jahr, ‘reunion’,  which  is  rel.  to  the  s/crbja'bara,  ‘he bound  together,  united’.  Cp.  algorism.
KLN_1966.txt:2189:algology,  n.,  the  study  of  algae.  —  A  hybrid  coin¬ ed  fr.  L.  alga  and  Gk.  -Xoyla,  fr.  -Xoyo;,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  alga  and  -logy. Derivatives:  algolog-ical,  adj.,  algolog-ist,  n. algor,  n.,  cold;  chill.  —  L.,  fr.  algere,  ‘to  be  cold’. See  algid  and  -or.  For  the  mode  of  formation cp.  terror,  ‘fright’,  fr.  terrere,  ‘to  frighten’,  albor, ‘white  color’,  fr.  albere,  ‘to  be  white’, algorism,  n.,  the  Arabic  system  of  numerals.  — ME.  algorisme,  fr.  OF.  algorisme  (F.  algorith- me),  fr.  ML.  algorismus ,  from  the  inexact  trans¬ literation  of  Arab.  al-Khowarizmi,  ‘the  man  of Khowarizm  (the  modern  Khiva),  surname  of Abu  Jafar  Mohammed  ibn  Musa,  great  mathe¬ matician  of  the  9th  cent.  His  famous  work  Al- jabr  w’al  muqdbalab  (‘Reunion  and  compar¬ ison’),  introduced  the  use  of  Arabic  numerals  in Europe,  which  denoted  a  turning  point  in  the history  of  mathematics.  Cp.  algebra, algous,  adj.,  pertaining  to  algae.  —  L.  algosus, fr.  alga,  ‘seaweed’.  See  Alga  and  -ous. alguazil,  n.,  peace  officer  in  Spain.  —  Sp.  alguacil, fr.  earlier  alguazil,  fr.  Arab,  al-wazfr,  fr.  al-, ‘the’,  and  waztr,  ‘vizier’.  See  vizier, algum,  n.  —  See  almug.
```


## [2026-09-14T03:11:51.557Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('algorism,  n.,  the  Arabic')\nprint('leaf',t[:i].count('\\f'))\n# find page-number-ish tokens on that leaf\npages=t.split('\\f')\nl=t[:i].count('\\f')\nprint(repr(pages[l][:200]))\nprint('...')\nprint(repr(pages[l][-200:]))\nEOF\necho \"=== Klein eu- / hygiene ===\"\ngrep -n \"hygiene\\|‘well’\\|eu-,  pref\\|ev-,  pref\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T03:11:52.677Z] TOOL RESULT

```
leaf 37
'read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. '
...
'cp.  Alison.\nAlice  blue.  —  Named  after  Mrs.  Alice  Roosevelt, wife  of  President  Theodore  Roosevelt, alicula,  n.  a  short  cloak  (Rom.  antiq.)  —  L.  ‘a light  upper  garment’,  a  dimin'
=== Klein eu- / hygiene ===
4621:beatify,  tr.  v., —  to  make  blessed; to  make  happy. —  F.  beatifier,  ‘to  beatify’,  fr.  post-classical  L. beatificare,  ‘to  make  happy’,  which  is  com¬ pounded  of  L.  beatus,  ‘happy,  prosperous’,  and -ficare,  fr.  facere,  ‘to  make,  do’.  Beatus  is  prop, pp.  of  bedre,  ‘to  make  happy,  to  bless’,  which  is prob.  rel.  to  bene,  ‘well’,  bonus,  ‘good’.  See bene-,  bonus,  and  -fy  and  cp.  next  word,  beati¬ tude,  Beatrice.
4628:Derivatives:  beautiful-ly,  adv.,  beautiful-ness,  n. beautify,  tr.  v.  —  See  beauty  and  -fy. beauty,  n.  —  ME.  bealte,  beaute  (F.  beaute ),  fr. L.  bellitdtem,  acc.  of  bellitas,  ‘prettiness,  charm, loveliness,  beauty’,  fr.  bellus,  ‘pretty,  handsome, charming,  fine,  lovely,  beautiful’,  which  stands for  *dwenelos,  *dwenlos,  and  is  rel.  to  L.  bene, ‘well’,  bonus,  earlier  *dwenos,  ‘good’,  prob.  also to  bedre,  ‘to  make  happy’,  beatus  ‘happy’  and cogn.  with  OI.  duvas-,  ‘gift,  honor,  respect’, duvas-yati,  ‘honors,  respects’.  Cp.  bonus,  and words  there  referred  to.  Cp.  also  beatify,  bel- dam(e),  belladonna,  belle,  belles-lettres,  Beilis,  bel¬ vedere,  clarabella,  embellish,  Christabel,  Rosabel, beaver,  n.,  a  rodent  of  the  genus  Castor.  —  ME. bever,  fr.  OE.  beofor,  rel.  to  ON.  biorr,  OS.  bibar, OHG.  bibar,  MHG.,  G.  biber,  ‘beaver’,  and cogn.  with  L.  fiber,  OSlav.  bebru,  Lith.  bebrus (also  dissimilated  into  vebrus,  debrus),  Lett. bgbrs,  bebris,  OPruss.  bebrus,  W.  befer,  Bret. bieuzr,  Avestic  bawra,  ‘beaver’.  All  these  words lit.  denote  ‘the  brown  animal’;  they  derive  fr. I.-E.  *bhe-bhru-s,  ‘very  brown’,  whence  also  OI. babhruh,  adj.,  ‘brown’;  n.,  ‘the  larger  ichneu¬ mon’.  I.-E.  *bhe-bhru-s  is  reduplication  of  base *bhero-,  ‘brown’.  Both  the  bear  and  the  beaver are  called  after  their  color.  See  bear,  n.,  and brown.
4740:bene-,  combining  form  meaning  ‘well’.  —  L.  bene, ‘well’,  fr.  earlier  *dwene,  rel.  to  bonus,  earlier *dwenos,  ‘good’,  bellus,  earlier  *dwenelos,  *dwen- los,  ‘beautiful’.  See  bonus,  beauty, beneath,  prep,  and  adv.  —  ME.  benethe,  bene- othen,  fr.  OE.  beneopan,  fr.  be-,  ‘by’,  and  neopan, ‘below,  beneath’.  See  be-  and  nether  and  cp. underneath.
4745:Benedict),  name  of  the  founder  of  this  order, benediction,  n.  —  L.  benedictid,  gen.  -dnis,  fr. benedictus,  pp.  of  benedicere,  ‘to  bless’,  lit.  ‘to speak  well  of,  to  praise’,  fr.  bene,  ‘well’,  and dicere,  ‘to  say,  tell’.  See  bene-  and  diction  and cp.  benison,  which  is  a  doublet  of  benediction. Cp.  also  bennet,  bensh.
4746:benedictory,  adj.,  pertaining  to  a  blessing.  —  ML. benedictorius,  fr.  L.  benedictus,  pp.  of  benedicere. See  prec.  word  and  adj.  suff.  -ory. benefaction,  n.,  a  good  deed,  donation.  —  L. benefactio,  gen.  -dnis,  fr.  benefactus,  better  writ¬ ten  in  two  words  bene  factus,  fr.  bene,  ‘well’,  and factus,  pp.  of  facere,  ‘to  make,  do’.  See  bene- and  faction  and  cp.  benefit, benefactor,  n.,  one  who  confers  a  benefit.  —  L., ‘who  performs  an  act  of  kindness’,  fr.  bene¬ factus.  See  prec.  word  and  factor, benefactress,  n.  —  See  prec.  word  and  -ess. benefice,  n.,  a  church  living.  —  F.  benefice,  fr.  L. beneficium,  ‘generosity,  kindness,  benefit’,  fr. beneficus,  ‘generous,  kind,  beneficent,  obliging’, which  is  formed  fr.  bene,  ‘well’  and  -ficus,  from the  stem  of  -ficere,  unstressed  form  of  facere, ‘to  make,  do’.  See  bene-  and  fact.
4750:Derivatives :  beneficial-ly,  adv.,  beneficial-ness,  n. beneficiary,  n.,  one  who  receives  benefits.  —  L. beneficiarius,  ‘enjoying  a  favor,  privileged’,  fr. beneficium.  See  benefice  and  subst.  suff.  -ary. benefit,  n.  —  ME.  benefet,  benfet,  fr.  AF.  benfet (rel.  to  OF.  and  F.  bienfait),  fr.  L.  benefaction, bene  factum,  ‘well  done’.  See  benefaction. Derivatives:  benefit,  tr.  and  intr.  v.,  benefit-er, n. benevolence,  n.,  kindliness.  —  OF.  benivolence, fr.  L.  benevolentia,  ‘good  will,  kindness’,  fr. benevolens,  gen.  -entis.  See  next  word  and  -ce. benevolent,  adj.  wishing  to  do  good,  kindly.  — OF.  benevolent,  fr.  L.  benevolens,  gen.  -entis, ‘wishing  well,  benevolent’,  fr.  bene,  ‘well’,  and volens,  gen.  -entis,  pres.  part,  of  void,  velle,  ‘to will,  wish’.  See  voluntary  and  -ent  and  cp. malevolent.
4751:Derivative:  benevolent-ly,  adv. benight,  tr.  v.  (rare)  — •  Formed  fr.  be-  and  night. Derivative:  benight-ed,  adj. benign,  adj.,  kindly.  —  ME.  benigne,  fr.  OF.  be- nigne  (F.  benin,  fern,  benigne),  fr.  L.  benignus, ‘kindly,  kindhearted,  friendly’,  orig.  ‘of  good nature',  compounded  of  bene,  ‘well’ and  *gno-s ,
4955:bienseance,  n.,  propriety.  —  F.,  lit.  ‘well-becom- ingness’,  fr.  bienstant,  ‘well-becoming’,  fr.  bien (fr.  L.  bene),  ‘well’,  and  scant,  pres.  part,  of seoir,  ‘to  sit’,  fr.  L.  sedere.  See  bene-,  sedentary and  -ce.
5338:bonus,  n.  —  L.  bonus,  ‘good’,  fr.  OL.  dvenos, dvonos,  rel.  to  L.  bene,  ‘well’,  bellus,  ‘handsome, charming,  fine’.  See  beauty  and  cp.  bene-,  bene¬ diction,  benefactor,  benefit,  benevolent,  benign, bonanza,  bonitarian,  bonito,  bonne,  bonte,  boon, bounty,  bunt,  ‘to  sift’,  bunting,  ‘cloth’,  debonair, embonpoint,  magnum  bonum. bonze,  n.,  a  Buddhist  priest.  —  F.,  fr.  Port,  bonzo, fr.  Jap.  bonzo,  ‘Buddhist  priest’,  fr.  Chin,  fan- seng,  ‘religious  person’.
13764:eu-,  combining  form  meaning  ‘good,  well’.  —  Fr. Gk.  eu,  ‘well’,  prop.  neut.  of  £64,  ‘good’,  which is  cogn.  either  with  Hitt,  ashshush,  ‘good’,  or — more  probably — with  OI.  vasuh,  Avestic  vohu-, ‘good’,  Ir.  feb  (fr.  I.-E.  *wesw-a),  ‘excellence’. Eu-  is  the  opposite  of  dys-. eucaine,  n.,  name  of  two  synthetic  alkaloids called  alpha-eucaine  and  beta-eucaine. —  Coined fr.  eu-  and  the  second  and  third  syllable  of cocaine.
13765:eucairite,  n.,  a  copper  silver  selenide  (mineral.)  — Swed.  eukairit,  formed  with  suff.  -it  (represent¬ ing  Gk.  -iiry.  see  subst.  suff.  -ite)  fr.  Gk. Euxalpoic,  adv.  of  cuxatpoi;,  ‘seasonable,  op¬ portune’,  fr.  eu,  ‘well’  (see  eu-),  and  xoapXc,  ‘the right  season,  the  right  time’  (see  kairine).  The mineral  was  so  called  because  it  was  found  by the  Swedish  chemist  Baron  Jons  Jakob  Berzelius (1 779- 1 848)  soon  after  the  discovery  of  selenium. Eucalyptus,  n.,  a  genus  of  plants  of  the  myrtle family  (bot.)  —  ModL.,  lit.  ‘well  covered’, coined  by  the  French  botanist  L’Hdritier  de Brutelle  (1746-1800)  in  1788  fr.  eu-  and  Gk. xaXu7tx64,  ‘covered’,  verbal  adj.  of  xocXurexeiv, ‘to  cover,  conceal’  (see  calyptra);  so  called  in allusion  to  the  cap  covering  the  bud.
13766:Eucharis,  n.,  a  genus  of  the  plants  of  the  amar¬ yllis  family  (bot.)  —  ModL.,  fr.  Gk.  e6xaP1?. ‘pleasant,  agreeable’,  fr.  e5,  ‘well’,  and  X“P‘S> ‘favor,  grace’.  See  next  word.
13772:euclase,  n.,  a  brittle  green  silicate  of  beryllium and  aluminum  (mineral.)  —  Lit.  ‘that  which breaks  easily’;  formed  fr.  eu-  and  Gk.  xXamc, ‘a  breaking’,  from  the  stem  of  xXav,  ‘to  break’. See  clastic  and  cp.  words  there  referred  to. Euclea,  n.,  a  genus  of  plants  of  the  ebony  family (bot.)  —  ModL.,  lit.  ‘glorious’,  fr.  eGxXekx,  ‘glory’, fr.  euxXe(£,  ‘famous,  glorious’,  which  is  formed fr.  eu  (see  eu-)  and  xXeo?,  ‘fame’  (see  Eteocles); so  called  in  allusion  to  the  beautiful  foliage. Euclid,  euclid,  n.  —  Short  for  Euclid's  geometry, i.e.  geometry  based  on  the  treatise  of  Euclid, the  great  Greek  mathematician  who  lived  about 300  B.C.E.  (The  name  lit.  means  ‘renowned’, and  is  rel.  to  euv.Xeyp,  ‘renowned’,  prop,  ‘of good  report’,  fr.  e5,  ‘well’,  and  xX(op,  ‘fame’; see  prec.  word.)
13774:eudiometer,  n.,  an  instrument  for  the  volumetric measuring  of  gases.  —  Coined  by  the  English clergyman  and  chemist  Joseph  Priestley  (1733- 1804)  fr.  Gk.  euStoq,  ‘fine,  dear’  (said  esp.  of  air and  weather),  and  pixpov,  ‘measure’.  The  first element  stands  for  ’eu-Stfot;  and  lit.  means ‘having  a  good  day’,  fr.  e5,  ‘well’,  and  8104 (for  ‘Slfiop),  ‘divine’.  Cp.  OI.  su-divdh,  ‘having a  fine  day’,  which  is  the  equivalent  of  Gk.  euSio?. See  eu-  and  deity.  For  the  second  element  see meter,  ‘poetical  rhythm’.
13782:Euglandina,  n.,  a  genus  of  snails  (zool.)  ■ —  A ModL.  hybrid  coined  fr.  eu-,  L.  glans,  gen. g/andis,  ‘acorn’  (see  gland),  and  suff.  -ina. euhemerism,  n.,  theory  of  Euhemerus,  a  Sicilian Greek  philosopher  of  about  300  B.C.E.  — Formed  with  suff.  -ism  fr.  L.  Euhemerus,  fr. Gk.  Eufipspoi;  (a  name  lit.  meaning  ‘bright, happy’,  fr.  e8,  ‘well’  and  f.pipa,  ‘day’). Derivatives:  euhemerist-ic,  adj.,  euhemerist-ic- al-ly,  adv.
13813:euphorbium,  n.,  a  gum  resin  derived  from  Euphor¬ bia  resinifera.  —  ModL.,  fr.  L.  euphorbeum ,  fr. Gk.  eutpopfhov.  named  after  E-j<j>op|Soc,  Euphor- bus,  a  Greek  physician.  (The  name  lit.  means 'well  nourished',  fr.  e5,  ‘well’  and  cpopfSfj,  ‘pas¬ ture,  nourishment’,  which  is  rel.  to  cpsp^civ, "to  feed’.)
15725:gallop,  intr.  and  tr.  v.  —  F.  galoper,  fr.  Frankish *wala  hlaupan,  ‘to  run  well’.  The  first  element  is rel.  to  OHG.  wala,  wela,  wota,  OE.  we  I,  ‘well’; see  well,  adv.  The  second  element  is  rel.  to OHG.  hlauffan,  loufan,  ‘to  run’;  see  leap.  Cp. galop,  wallop.
18409:hygiene,  n.,  the  science  of  health.  —  F.  hygiene, fr.  Gk.  uyieivov,  neut.  of  uytetvfS?,  ‘pertaining to  health,  healthful’,  but  used  by  Aristotle  also as  a  noun  in  the'  sense  of  ‘health’,  fr.  uyifjs, ‘healthy’,  which  stands  for  *su-gwiyes  and  lit. means  ‘living  well’,  fr.  I.-E.  *su-  (Gk.  &-),  ‘well’, whence  also  01.  su-,  OPers.  hu,  OIr.  su-,  so-, ‘well’  (cp.  sundari),  and  *gwiyes,  ‘living’,  enlarge¬ ment  of  *gKi-,  ‘to  live’,  whence  also  Gk.  pro?, ‘life’.  See  bio-  and  cp.  words  there  referred  to. L.  vegere,  ‘to  be  lively,  vigorous,  to  thrive, flourish’,  vegeius,  ‘lively,  vigorous’,  are  not cognate  with  Gk.  uy rijs.  As  a  formative  element, 0-  was  replaced  later  by  eu-  (see  eu-). Derivatives :  hygien-ic,  adj.,  hygien-ic-al-ly,  adv., hygien-ics,  n.,  hygien-ist,  n. bygro-,  before  a  vowel  hygr-,  combining  form meaning  ‘moist,  humid’.  —  Gk.  uypo-,  uyp-,  fr. uypo?,  ‘wet,  moist,  humid’,  rel.  to  L.  (h)umor, ‘fluid,  moisture’.  See  humor  and  cp.  words  there referred  to.
31394:queue,  n.,  1)  (her.)  the  tail  of  a  beast;  2)  plait  of hair  worn  hanging  down  behind ;  pigtail ;  3)  a line  of  persons  waiting  for  their  turn.  —  MF. (=  F.),  fr.  OF.  coe,  fr.  L.  coda,  secondary  form of  cauda,  ‘tail’.  See  caudal  and  cp.  cue,  ‘tail’. Derivative:  queue,  intr.  v. quibble,  n.,  a  petty  evasion.  —  Dimin.  of  obsol. quib,  fr.  L.  quibus,  dat.  or  abl.  pi.  of  qui,  ‘who, which',  used  frequently  in  legal  documents.  See who,  what  and  cp.  quid,  ‘essence’,  quiddity. Derivatives:  quibble,  intr.  v.,  quibbl-er,  n. quick,  adj.,  1)  living,  alive  (archaic)-,  2)  rapid, swift;  3)  prompt;  done  promptly;  4)  alert.  — ME.  quik,  quike,  ‘alive,  lively’,  fr.  OE.  ewieu, ‘living,  alive’,  rel.  to  OS.,  OFris.  quik,  ON. kvikr,  ‘living,  alive’,  Du.  kwi(e)k,  ‘lively,  bright, sprightly’,  OHG.  quec,  chec,  cheh,  MHG.  queck, kec,  ‘lively’,  G.  keck,  ‘bold’,  fr.  Teut.  *q"'iqwa-, ‘living,  alive’,  fr.  l.-E.  *gwigwos,  fr.  base  *gwei-, ‘to  live’,  whence  Goth.  *qius,  gen.  qiwis,  ‘alive’, OI.  jivdh,  ‘alive’,  jfvati,  Avestic  jvaiti,  ‘lives’, OPers.ffva-,  ‘living’,  Gk.  [3toc  (prob.  for  *(3ifoi;, fr.  I.-E.  *gwiwos),  ‘life,Jhe  course  of  life’,  £ijv (fr.  I.-E.  *gwie-),  ‘to  live’,  dorr,,  ‘life’,  L.  vivus, (for  *gwiwos),  ‘living’,  vivo,  there  (for  *gwiwd), ‘to  live’,  vita  (for  *gwiwita),  ‘life’,  OSlav.  iivo, liti,  ‘to  live’,  iivu,  ‘alive’,  iivotu,  ‘life’,  Lith. gyvas,  ‘living,  alive’,  gyratd  '(eternal)  life’,  OIr. biu,  beo,  W.,  Co.  byw,  Bret,  beo,  ‘alive’,  OIr. beothu,  bethu  (for  *biwotut-),  ‘life’,  biad,  'means of  life’,  OIr.  bith,  W.  byd,  'world',  Toch.  A  fol, B  caul,  ‘life’,  A  sofi,  B  saigfe,  'people'  (lit.  ‘the living  ones’),  B  faya/p, ‘he  lives’,  Arm.  keam((ot *gwiya),  ‘I  live’.  Hitt,  huish-  is  not  cognate.  Cp. quitch.Cp.  also  bio-, hygiene,  jiva,  vital  and  words there  referred  to.  Cp.  also  zodiac,  zoetic,  zoo- and  the  second  element  in  usquebaugh,  whisky. Derivatives:  quick,  adv.  and  n..  quick-en,  tr.  and intr.  v.,  quick-ly,  adv.,  quick-ness,  n. quick,  tr.  and  intr.  v.  —  ME.  quiken,  fr.  OE.
37460:sundari,  n.,  name  of  an  East  Indian  tree  ( Heritiera fomes)  —  OI.  sundari,  lit.  ‘beautiful’,  fern,  of sundarah,  a  later  form  corresponding  to  Vedic siinarah,  ‘of  full  vitality’  (cp.  Avestic  hunara-,  of s.m.),  formed  fr.  I.-E.  pref.  *su-,  ‘well,  good, beautiful',  and  base  *ner-,  ‘vital  energy,  vigor'. I.-E.  *su-  appears  also  in  Gk.  u-  in  u-Yir,c, ‘healthy’;  see  hygiene.  I.-E.  *ner-  occurs  also  in OI.  naryab,  ‘virile’,  Gk.  a-vv)p,  ‘man’;  see andro-.
```


## [2026-09-14T03:12:10.298Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor n in ['algorism,  n.,  the  Arabic','eu-,  combining  form','hygiene,  n.,  the  science','sundari,  n.,']:\n    i=t.find(n); l=t[:i].count('\\f')\n    print(n[:20],'leaf',l,'-> printed approx',(l-13)*2+1,'or',(l-13)*2+2)\nEOF"
}
```


### [2026-09-14T03:12:11.454Z] TOOL RESULT

```
algorism,  n.,  the  leaf 37 -> printed approx 49 or 50
eu-,  combining  for leaf 298 -> printed approx 571 or 572
hygiene,  n.,  the   leaf 407 -> printed approx 789 or 790
sundari,  n., leaf 818 -> printed approx 1611 or 1612
```


## [2026-09-14T03:12:15.116Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor l in (286,287,288):\n    print('== leaf',l, repr(pages[l][:150]))\nEOF"
}
```


### [2026-09-14T03:12:16.198Z] TOOL RESULT

```
== leaf 286 ' Gk.  4vteX4xeioc, ‘full  reality’,  coined  by  Aristotle  fr.  bmeXrfi, ‘complete’,  and  ifyEiv,  ’to  have’.  The  first element  is  formed  fr. '
== leaf 287 'nter-.  —  Fr.  F.  entre, ‘between,  among’,  fr.  L.  inter,  of  s.m.  See  ist enter-.\nentreat,  tr.  and  intr.  v.  —  ME.  entreten,  fr.  OF. '
== leaf 288 '  and  £v8iisiv,  ‘to  put  on (clothes)’  (whence  6v8up.a,  ‘garment’);  see  en- dysis.  Considering  the  fact  that  this  membrane consists  of '
```


## [2026-09-14T03:12:33.160Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T03:12:34.053Z] TOOL RESULT

```
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-14T03:12:51.502Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor l in (285,286,287,288,289,297,298,299):\n    txt=pages[l]\n    hw=re.findall(r'(?m)(?:^|\\s)([a-zA-Z][a-zA-Z\\-\\’\\' ]{2,22}),\\s+(?:n\\.|adj\\.|tr\\.|intr\\.|combining|pref|adv\\.)',txt)\n    print(l, (2*(l-12)), hw[:6], '...', hw[-3:])\nEOF"
}
```


### [2026-09-14T03:12:52.620Z] TOOL RESULT

```
285 546 ['enlace-ment', 'enlarg-ed', 'enlarg-ed-ly', 'enlarg-ed-ness', 'enlarge-ment ', 'enlarg-er'] ... ['entasia', 'entasis', 'entelechy']
286 548 ['entellus', 'entelodont', 'entente', 'enter', 'enter-', 'enteric'] ... ['entrap', 'entrapp-er', 'entre-']
287 550 ['entreat', 'entreat- ing', 'entreat-ing-ly', 'entreaty', 'entree', 'entremets'] ... ['epee', 'epeiric', 'ependyma']
288 552 ['ependym-al', 'ependymitis', 'ependymoma', 'epenthesis', 'epenthetic', 'epergne'] ... ['epicycloid', 'epicycloid-al', 'epidemical']
289 554 ['epidemic', 'epidemic-al-ly', 'epidemic-al-ness', 'epidemic-ity ', 'epidemiology', 'epidemiolog-ic-al'] ... ['epiploitis', 'epiploon', 'episcopacy']
297 570 ['eternity', 'eternize', 'etesian', 'also  aether', 'ethereal', 'ethereal-ity'] ... ['Etonian', 'Etrurian', 'Etruscan']
298 572 ['etude', 'etui', 'etymological', 'etymological-ly ', 'etymologicon', 'etymology'] ... ['euosmite', 'Eupatorium', 'eupepsia']
299 574 ['eupeptic', 'euphemism', 'euphemist', 'euphemist-ic-al-ly', 'euphemizc', 'euphemiz-er'] ... ['evacuant', 'evacuate', 'evacuation']
```


## [2026-09-14T03:13:03.051Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 خوارزم ===\"\ngrep -n \"خوارزم\" BQT_v2_pages.txt | head -20\necho \"=== BQT v2 خیوه ===\"\ngrep -n \"خیوه\\|خيوه\\|خیوق\\|خيوق\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T03:13:03.130Z] TOOL RESULT

```
=== BQT v2 خوارزم ===
195: ‫خوارزمی ‪.‬فر(هنگ عربی بفارسی) با اضافات باهتمام وزماو‪. [ . 6 . ¥ 20۵‬لبسيك‬
7361:   ‫و سپس قوم‌اویفور رامنقرض کردودرسال ‪٩۱٩‬‏ بممالك خوارزمشاهی‌حمله برد و درظرف دوسال شهر‬
8613:        ‫خوارزمی است ‪ » ۰‬از بیت ذیل عجدی مروزی برمیابد که درلهجةٌ مرولیز مممول بوده ‪:‬‬
10571:      ‫ورك ‪ :‬اسفا ‪ ۲ :۱‬ص ‪ « ۹۷۱.۰‬خراسان " تفسیره‌المشرق » « مفاتیج‌العلوم خوارزمیس‬
11016: ‫رده «روز شماری ‪ < ۶۲4 -۲۷‬اسفا ‪‎ ۲ : ۱‬ص ‪۰٩۷ ۰۳۷‬‬  ‫هردد» و در خوارزمی « هرو دان“ بکاد‬
12120: ‫*‪ .‬بازندلا ‪ « 2150‬متا ‪ ۹۳۱۰‬معرب آن کسری ؛ ‪ ۵‬مفاتیح خوارزمی‌ص ‪ ۹۷‬؟؛ نام‬                     ‫‪۸‬‬
14190:           ‫‪۰‬‬   ‫ودومقدمه‬   ‫بست‬    ‫" ر کت ‪ :‬ص‬         ‫زبان خوارزم‬        ‫بخوارزم‬         ‫خوارز می ‪ ۳‬منسوب‬                    ‫‪۶‬‬
14534:  ‫روزهای ایرانی ایشروز را (خور) ودرسفدی(خویر) و درخوارزمی (اخیر)یاد کرده‪.‬‬
15643:          ‫ولاسی جک ازاولعای )‪ (۱‬خوارزم ‪¥.‬‬         ‫ن ینا سرودونغه هرا کومند ‪١.‬‏‬
17637: ‫ازیوست خرس بود‪ .‬وبقول دبگرازپوست شیر» و بزرو گوهرآراسته بود ‪ .‬خوارزمی درمفانیح‌الملوم‬
20844:  ‫«ایشان (خوارزمیان) جوزاء را درجملةٌ بروج بجای « نوأمان» محسوب دارند واين جوزاء صورت‬
20845:  ‫(ذوجر كرك ‪ .‬ن ل) کونند‬  ‫جبار است و اهل خوارزم اين برح (جوزا) را« اذويچگريك » ا‬
21374:    ‫‪ - ۷‬نیز بمە‌نیآلت‬       ‫=ور (خوارزمی) = دلو(عر) گداه شماری ‪. » ۳۰۲‬‬
21833:   ‫مشتهااص‪ « »4 ۲‬خرده اوستا‬                ‫ورده‪ ۶ .‬روزشماری ‪۵۲-۹۲‬‬       ‫و درسفدی «ادست؟ و درخوارزمی«دنو»‬
22280:            ‫ایرانی نام این روز را ‪۶‬دین ‪٩‬‏ و درسفدی حم ‪ +‬دین ‪ ۴‬و درخوارزمی نیز «دین؟ بکاد‬
23049:                       ‫ایرانی نام این روز را «رام» و درسفدی «رامن» و در خوارزمی قرام“ بادکرده ‪:‬‬
24206:      ‫بیرونی درفهرست روزهای ابرانی‌اورا رشن“ ودرسفدی «رسن» ودرخوارزمی«رشن» بادکرده است‪.‬‬
27337:                                                             ‫«زامیان» و درسفدی درام جید» ودر خوارزمی «راث» بکار‬
35861:   ‫روز مزبور را «سروش» و درسفدی «سرش» و درخوارزمی «اسروف» بادکرده ‪ .‬در زبان فارسی کاه‬
36031:     ‫و صورت « سربانی لو» در آمده است ‪.‬رك ‪ :‬فاب اص ‪ .۱۹۱-۷۷۱‬خوارزمى كوبد «‪:‬السربالية‬
=== BQT v2 خیوه ===
15657:                                                                                   ‫خیوق ‏‬
15658:                                                                  ‫‪ #‬خيوه ‏ رك‪ :‬خیوق ‪.‬‬
38947:‫دشردفچاهرسی جيم‬  ‫سوز است که اسزوختن با‬                            ‫فارسی » بزبان خیوق که یکی از العای خوارزم‬
```


## [2026-09-14T03:13:08.619Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=14100 && NR<=14200 && /pdf page/' BQT_v2_pages.txt\necho \"--- tags near 15600-15700 ---\"\nawk 'NR>=15500 && NR<=15700 && /pdf page/' BQT_v2_pages.txt\necho \"--- first tags ---\"\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -5\ngrep -n \"pdf page\" BQT_v2_pages.txt | sed -n '395,405p'"
}
```


### [2026-09-14T03:13:09.710Z] TOOL RESULT

```
--- tags near 15600-15700 ---
--- first tags ---
```


## [2026-09-14T03:13:14.646Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt | cat -A | cut -c1-100\necho \"=== formfeed count ===\"\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff pages:',t.count('\\f'))\nlines=t.split('\\n')\nprint('lines',len(lines))\n# leaf for خوارزمی at line 14190\nimport itertools\ndef leaf_for_line(ln):\n    s='\\n'.join(lines[:ln])\n    return s.count('\\f')\nfor ln in (14190,15643,15657,195):\n    print(ln, 'leaf', leaf_for_line(ln))\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['BQT']['page_offset']);print(d['BQT'].get('lookup_hint'))\""
}
```


### [2026-09-14T03:13:15.812Z] TOOL RESULT

```
^L                                         M-bM-^@M-+M-bM-^@M-*7M-bM-^@M-,M-bM-^@M-,$
$
                          M-bM-^@M-+M-XM-1M-YM-^FM-bM-^@M-*M-[M-3M-bM-^@M-,M-bM-^@M-,$
    M-bM-^@M-+M-YM-^FM-XM-'M-XM-*M-bM-^@M-,$
      M-bM-^@M-+M-XM-' M-YM-^EM-bM-^@M-,$
=== formfeed count ===
ff pages: 683
lines 41071
14190 leaf 239
15643 leaf 265
15657 leaf 265
195 leaf 5
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-14T03:13:21.186Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## leaf 238\"; awk 'BEGIN{RS=\"\\f\"} NR==239' BQT_v2_pages.txt | grep -n \"خوارزم\" | head\necho \"########## leaf 239 full-ish\"; awk 'BEGIN{RS=\"\\f\"} NR==240' BQT_v2_pages.txt | sed -n '1,60p'"
}
```


### [2026-09-14T03:13:22.191Z] TOOL RESULT

```
########## leaf 238
########## leaf 239 full-ish
 ‫خوازه‬                                                                                                                     ‫‪۷‬‬           ‫‪-‬‬


‫بمعنی خوردنی ورزق وروزی باشد ‪ -‬و جضم اول‬                    ‫‪ -‬ونام ولاسی‌است درحوالی ری‪٩‬‏ ‪ -‬وعم‬                                        ‫هت‬
‫بروژن شماره » بمعتی دستورباشد که رسم وقاعده‬                 ‫اول و ثانی بالف کشیده بر وزن شمار " بمعنی‬
‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬


 ‫بدن شود ق‪-‬اولبی بائد کهبنایان طاق کونبد‬                    ‫خو ار بار » بائانی معدوله وبای ابجد‬
‫بربالای آن سازند‪٩‬‏ ‪ -‬و بمعنی چوب بندی هم‬                    ‫است که قوت‬                 ‫کارزار» یمعی خوراك ادك‬                        ‫روزن‬
                                       ‫‪9‬‬       ‫فەا‬           ‫باشد ‪ - ۲‬و مره ولذت را نز گوند ‪-‬‬                                       ‫لانموت‬
‫خواری خوار » بائانی معدوله بر‬                               ‫ازديك‬           ‫وخطه‌ای‬           ‫و تومئی است از توه‌نات ضارا‬

     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
 ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬

                 ‫دادن ‪ -‬وزبان‌کاری کردن باشد ‪.‬‬                                                            ‫ازتر کتان ‪۶. ۴‬‬

 ‫بفتح اول بر وزن بماز »‬          ‫خوار ‪-‬‬
 ‫چوبدستی که خر کواو وسایر ستوران را بدان‬                          ‫کارزار ‪ ۰‬ستمکار وخواری کننده راکوبند ® ‪.‬‬
                                               ‫رانند ‪5‬‬
                                                             ‫جو ار کاره = با انی معدوله بر وزن‬
 ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬



 ‫بمفعنریی|ن ‪ -‬وخواهش باشد‪-۱٩‬‏ ومطلق چوب‬                      ‫خوار کادی ‪ -‬بانانی مسوله بروزن‬
 ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬

 ‫بابنایی ونقاشی کردن عمارت یابجهت تاك انگور‬                                                       ‫‪۱‬‬   ‫را نز گوند ‪۸‬‬                    ‫دهنده‬
 ‫وامثال آن بندند کوشکی وقبه‌ای را گنفزتهاند‬
 ‫که بجهت عروسی وآبین بندی ازکل ورباحین‬                       ‫خوا ده = بانانی ممدوله بروزن چاره»‬

   ‫‪ .‬معرب آن‬      ‫‪۳۸‬‬    ‫و حدود المالم ص‬         ‫‪۵۵۳‬‬   ‫کیپان ص‬      ‫‪.‬‬     ‫رك ‪ :‬حفرافیای سیاسی‬                   ‫‪-‬‬           ‫‪۱‬‬

    ‫البارها پر کرد ‪...‬‬    ‫چون بوسف‬     ‫«‬   ‫_‬    ‫‪۳‬‬          ‫«خوار» سم اول وفتح دوم ‪ :‬رلك‪ :‬معدم البلدان ‪۰‬‬


 ‫بوسف و زلیتا ‪ .‬خڅ‬
                 ‫خابنربار های مصر بجهان بیفتاد ‪ .‬خلق روی بمصر نهادند بطلب خواربار ‪.«٩‬‏‬
   ‫"‪ 7‬همان خوار (ھ‪.‬م‪ (.‬است ‪.‬‬       ‫‪۴‬‬                       ‫ص‪ ۹۳‬‏‪ - ٩‬آمروز یزاین کاحه معنتی ارراق بکار رود‪.‬‬

               ‫مقلده‪.‬‬   ‫رکف‪:‬ص؛ ست‌ و دو‬         ‫حدودالمالم رمعم السلدان و‬                 ‫‪ 5 ۳۴‬رکف ‪ :‬فہرست‬


         ‫زشت است خوارکاری»خوبت بردباری ‪.‬‬                          ‫‪ . 6‬توخوارکارتر کی «من بردبار عاشق‬
    ‫«منوچپری د؛مفالی ‪.*۸۸‬‬
    ‫‪ - ۷‬از‪ :‬خوارکار ی ( مصدری ) رك‪ :‬خوارکار ‪.‬‬                                           ‫‪ :‬خوارکار ‪.‬‬     ‫رک‬         ‫۔‬       ‫‪1‬‬


    ‫_؛ مصحف «خوازه» (هم‪).‬‬  ‫‏‪ ٩‬ظ‬                           ‫‪ - ۸‬باين معنی *خوارکار »>صحیح است‬
    ‫‏‪27287۷۲ .1١‬‬     ‫»ور که ‪ :‬کواز ‪۰‬‬                ‫‪۶‬ت ظ ‪ ,‬مصحف «حوازه (ھ‪.‬م‪(.‬‬                                          ‫‪.‬‬       ‫‪ :‬خو‬     ‫ورك‬



    ‫خواستن آرزو کردن)‪ .‬کردی ‪( 01122۷1‬من‌میخواهم) ‪ ۰‬مازندرانی ‪( 22۷722011‬کین‌خواء)‬                                                        ‫‏(‬
                                                                             ‫‪۰‬‬       ‫«واژه امەس ‪۹۳۲‬‬           ‫«اسفا‪۲ :۱‬ص ‪۱۹‬‬
           ‫‪۰‬‬   ‫ودومقدمه‬   ‫بست‬    ‫" ر کت ‪ :‬ص‬         ‫زبان خوارزم‬        ‫بخوارزم‬         ‫خوارز می ‪ ۳‬منسوب‬                    ‫‪۶‬‬

   ‫‪ #‬خوار ی ‪ -‬بروزن کاری » در بهلوی ‪ +012‬بمعنی آسالی است (رکه‪ :‬خوار ) آما‬
```


## [2026-09-14T03:13:31.013Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==266' BQT_v2_pages.txt | sed -n '1,50p'"
}
```


### [2026-09-14T03:13:32.072Z] TOOL RESULT

```
                                                                                     ‫‪=A‬‬‫و‪‎‬‬




‫خیناگر = باکاف فارسی‌بروزن تیرآور‪.‬‬                ‫کردن وباد دربوق انداختن باشد‪ .‬که آنهم کنابه‬
                  ‫و‬    ‫ساز نده ومغنی را گومند ‪۳‬‬
                                                    ‫از برخاستن و برپایشدن آلت تناسل است ‪-‬‬
‫= بفتح واو بروزن بی‌خبر »‬        ‫حینو ر‬            ‫کونابه از فرودآمدن ومقیم شدن ولزول کردن‪.‬‬
                           ‫پل صراط رگاویند ‪.‬‬                           ‫ولشکر کشیدن و نوت نا‬
‫حو ‪ = ۴‬بسراول وسکون‌ثانی وواو‪,‬‬                      ‫خیم نزگادی ‪ -‬کنابه از آسمان‬
‫آب‌دهن راگوبند؛ وبفتح اول وضم ثانی‌هم‌درست‬
                                                                                         ‫است ‪.‬‬
                                        ‫اكت ‪::‬‬      ‫خیمه کبوه = بعنی خيمة زنکاری‬
                                                                           ‫است که آسمان باشد ‪.‬‬
‫حیوق * ‪ -‬بکراولبروزن زببق ‪.‬نام‬
          ‫ولاسی جک ازاولعای )‪ (۱‬خوارزم ‪¥.‬‬         ‫ن ینا سرودونغه هرا کومند ‪١.‬‏‬
                                                                               ‫خینا ‪ 5‬روز‬




                                                                  ‫)‪ ۱‬چك چش‪:‬الکای ‪.‬‬

   ‫(ھ‪ .‬م‪(0‬‬   ‫«چینود»‬    ‫_ مصحف‬   ‫‪۴‬‬         ‫خنبا کر‪.«(.‬م‪).‬‬   ‫سس‬          ‫رك‪ :‬خنبا ‪۵‬‬   ‫‪۱‬‬

   ‫= یوخ » یولهب ‪ ‹ 120016‬نامشیوه ‏‪٩۵۱۷‬و ‪12101‬‬                   ‫‏‪= X۷. e0 _ ۴‬ودخ‬
   ‫‪ - ۵‬کدثرب‌اسلامی‬                  ‫|تال‪ « 6708‬اسشق ‪۷۱‬ه»› رك‪ :‬خدو‪.‬‬
                                                                  ‫و‪. 25‬اوسا _ ‪ ۵۷۵2‬ن‬
                             ‫‪« xiwaq‬دائرة المعارف اسلام‪ .‬فراشه ج ‪ ۲‬ص ‪۳٩٩‬‏ ستون ‪.*۱‬‬
                                                                                   ‫خیوق ‏‬
                                                                  ‫‪ #‬خيوه ‏ رك‪ :‬خیوق ‪.‬‬
```


## [2026-09-14T03:13:44.325Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins su-/wesu- ===\"\ngrep -n -E \"^su-|^wesu-|\\(e\\)su-|esu-\" AHD_watkins1985.txt | head -20\necho \"=== BRT hvairizem ===\"\ngrep -n -i \"airizem\\|hvairiz\\|airizəm\\|xvairiz\" BRT.txt | head -10\necho \"=== BRT hu- prefix ===\"\ngrep -n -E \"^hu-|hu-, \" BRT.txt | head -10"
}
```


### [2026-09-14T03:13:44.413Z] TOOL RESULT

```
=== AHD watkins su-/wesu- ===
460:es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
462:esu-. Good. Extension of es-. Greek ews, good, combining form eu-, well: EU-. [Pok. esu-s 342.]
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1033:su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gia-es-, “living in good condition” (see g"ei-). [Pok. su- 1037.]
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
=== BRT hvairizem ===
=== BRT hu- prefix ===
23310:Kntiname  mit  demKoseinffixauia-;  vgl.np. fuiarS  {bei  HoBN  GIrPb.  /  b.  185)   und  die EN.  ÄonWims,  Satlaim,  und  vll,  Dayaukku  - Jiiamii.  —   I)  NA,  vaAui-.    Da«  so  gelesen werden   könne,    hat   »nch   HOwng  IrEN.  3a nicht  erwiesen;  s.  daiu  auch  KZ.  j/.  510. •   p.   (vaAav- :  va*u-,)   j.,  g.  'vashav-: vaahv-,  vanhu-,  vohu-  (fem.  vatehvl-)  Adj, 'gut",  d.  i.  so  wie  etwas  oder  Jemand  ent- spiechend   seiner  Bestimmung  beschaffen sein  soll,  'geeignet,  tauglich,  günstig,  förder- lich, genehm,  gütig,  religiös  und  moralisch gut';    eine    scharfe    Scheidung    der    Be- deutungen ist  nicht  durchzuführen,    a)  im gAw.;   a)  von  Sachen:    damayä  'tshuyS »jrSä  Jyatr'^ana^ä  y. ^^.1 ;  jy.  ^i  —  'nkuyh
```


## [2026-09-14T03:13:55.467Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Chorasmien ===\"\ngrep -n -i \"chorasmi\\|choresmi\\|Choraam\\|Xvairiz\\|hvairiz\\|airizom\\|airizem\" BRT.txt | head -15\necho \"=== AHD wesu ===\"\ngrep -n \"wesu\\|Pok. uesu\\|1174\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-14T03:13:55.545Z] TOOL RESULT

```
=== BRT Chorasmien ===
=== AHD wesu ===
1164:wesr. Spring. Latin vér, spring (phonologically irregular): VERNAL; PRIMAVERA. [Pok. wes-r 1174.]
```


## [2026-09-14T03:14:09.300Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T03:14:09.306Z] TOOL RESULT

```


```


## [2026-09-14T03:14:13.229Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85",
 "prompt": "Give the full etymology section(s) for Persian خوارزم (Khwarazm) — Old Persian/Avestan/Old Iranian forms, the analysis of the compound, and any competing etymologies. Quote exactly."
}
```


## [2026-09-14T03:14:14.715Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/algorithm",
 "prompt": "Quote the full etymology entries for 'algorithm' and, if shown, 'algorism' — dates, Medieval Latin algorismus, Old French, the al-Khwarizmi connection and the confusion with Greek arithmos."
}
```


### [2026-09-14T03:14:20.043Z] TOOL RESULT

```
# Etymology of Algorithm

**Algorithm (1690s):**
"Arabic system of computation," from French *algorithme*, reshaped under mistaken connection with Greek *arithmos* "number" from Old French *algorisme* "the Arabic numeral system" (13c.), from Medieval Latin *algorismus*, a mangled transliteration of Arabic *al-Khwarizmi* "native of Khwarazm" (modern Khiva in Uzbekistan), surname of the mathematician whose works introduced sophisticated mathematics to the West.

The meaning broadened from the Arabic numeral system to any method of computation; from mid-20th century onward, it especially referred to computing processes.

**Algorism (early 13c.):**
The earlier Middle English form was *algorism*, derived from Old French *algorisme*, which came from Medieval Latin *algorismus*. This chain of transmission ultimately traces back to the Arabic mathematician al-Khwarizmi of Khwarazm.

The key etymological point: the word's path shows how a Persian mathematician's name became the foundation for a fundamental computational concept, though the specific connection to Greek *arithmos* resulted from a scholarly misunderstanding rather than actual linguistic origin.
```


### [2026-09-14T03:14:22.210Z] TOOL RESULT

```
# Persian Etymology for خوارزم (Khwarazm)

## Full Etymology Section

According to the Wiktionary entry, the Persian term is "[Inherited](/wiki/Appendix:Glossary#inherited "Appendix:Glossary") from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭧𐭥𐭥𐭦𐭬](/w/index.php?title=%F0%90%AD%A7%F0%90%AD%A5%F0%90%AD%A5%F0%90%AD%A6%F0%90%AD%AC&action=edit&redlink=1 "𐭧𐭥𐭥𐭦𐭬 (page does not exist)")_ (ḥʿʿzm /⁠Xwārazm⁠⁠/), from [Old Persian](https://en.wikipedia.org/wiki/Old_Persian "w:Old Persian") _[𐎢𐎺𐎠𐎼𐏀𐎷𐎡𐏁](/wiki/%F0%90%8E%A2%F0%90%8E%BA%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%80%F0%90%8E%B7%F0%90%8E%A1%F0%90%8F%81#Old_Persian "𐎢𐎺𐎠𐎼𐏀𐎷𐎡𐏁")_ (u-v-a-r-z-m-i-i-š /⁠ʰUvārazmiš⁠/)."

## Analysis

The source provides a transmission pathway (Old Persian → Middle Persian → Persian) but does not include a detailed morphological breakdown of the Old Persian compound or discussion of competing etymologies. The entry references "More at [Khwarazm](https://en.wikipedia.org/wiki/Khwarazm#Names_and_etymology "w:Khwarazm")" for additional information, suggesting fuller analysis exists elsewhere in Wikipedia.
```


## [2026-09-14T03:14:28.368Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Khwarazm",
 "prompt": "Quote the \"Names and etymology\" section in full: the Old Persian/Avestan forms, proposed analyses (hu- 'good' + *zam- 'earth'; vara; Khiva/Khiveh), and any scholars named (e.g. Bailey, Henning, MacKenzie)."
}
```


## [2026-09-14T03:14:30.254Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-",
 "prompt": "Quote the entry: reconstruction, meaning, descendants (Indo-Iranian su-/hu-, Old Persian u-, Greek eu-), and the references cited (Pokorny page)."
}
```


### [2026-09-14T03:14:35.528Z] TOOL RESULT

```
# Khwarazm: Names and Etymology

## Historical Names

Khwarazm has been referred to by numerous designations throughout history, including "Chorasmia, Khaurism, Khwarezm, Khwarezmia, Khwarizm, Khorezm, Khoresm, Khorasam, Kharazm, Harezm, Horezm, and Chorezm."

## Ancient Language Forms

The name appears across multiple ancient languages:

- **Avestan**: 𐬓𐬁𐬌𐬭𐬌𐬰𐬆𐬨 (_Xvairizəm_)
- **Old Persian**: 𐎢𐎺𐎠𐎼𐏀𐎷𐎡𐏁 (_u-v-a-r-z-mi-i-š_)
- **Middle Persian**: 𐭧𐭥𐭥𐭦𐭬 (_ḥʿʿzm_)
- **New Persian**: خوارزم (_Xwārazm_)
- **Arabic**: خَوَارِزْم (_Ḵawārizm_)

## Proposed Etymologies

Scholar Yaqut al-Hamawi suggested the name combined Persian elements meaning abundance of "cooked fish" as a dietary staple. C.E. Bosworth proposed it derived from __xwar__ ('the sun') and __zam__ ('earth'), designating "the land from which the sun rises." An alternative interpretation suggests the Iranian compound means "lowland," from __xwār__ ('low') and __zam__ ('land').
```


### [2026-09-14T03:14:35.912Z] TOOL RESULT

```
# Proto-Indo-European *h₁su- (Good)

## Entry Overview
This Wiktionary reconstruction documents the Proto-Indo-European prefix *h₁su-, meaning "good." The term is not directly attested but reconstructed through comparative linguistic analysis.

## Etymology
The prefix possibly derives from metathesis of *h₁wes- ("good") or relates to *h₁es- ("to be"). Evidence includes Hittite āššuš and Epic Greek ēǘs, both meaning "good," suggesting a reduplicated root origin.

## Key Descendants
- **Proto-Celtic**: *su-
- **Proto-Balto-Slavic**: *su-
- **Proto-Hellenic**: *ehu-
- **Proto-Indo-Iranian**: *Hsu- (yielding Old Persian u-)
- **Phrygian**: ev-

## Related Terms
The prefix appears in *h₁sumenēs and compounds like Proto-Balto-Slavic *sùdarwas and *suwrēˀstei, with descendant forms in Lithuanian and Proto-Slavic.

## Primary References
Pokorny (1959) documents this in the *Indogermanisches etymologisches Wörterbuch* (pages 1037-1038), alongside references from Kloekhorst (2008) and Dunkel (2014) on Indo-European particles.
```


## [2026-09-14T03:14:46.377Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/chorasmia-i",
 "prompt": "Quote what the article says about the NAME Chorasmia/Xwārazm: the Old Persian Uvārazmiš, Avestan form, and the etymological analyses proposed (hu- 'good' + *zam- 'land'; xwar 'sun'; xwār 'low'), and which scholars (Henning, MacKenzie, Bailey) hold which view."
}
```


## [2026-09-14T03:14:47.143Z] TOOL CALL #36: WebSearch

```json
{
 "query": "Khwarazm etymology \"Uvārazmiš\" Old Persian \"hu-\" \"zam\" Henning MacKenzie \"lowland\" OR \"good land\""
}
```


### [2026-09-14T03:14:47.439Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T03:14:54.279Z] TOOL RESULT

```
Web search results for query: "Khwarazm etymology "Uvārazmiš" Old Persian "hu-" "zam" Henning MacKenzie "lowland" OR "good land""

Links: [{"title":"Chorasmian Online | Digital Resources for the Chorasmian Language | Page 2","url":"https://chorasmianonline.melc.berkeley.edu/page/2/"},{"title":"Chorasmian, Choresmian, Khwarazmian, Khwarezmian, or Khwarizmian? | Chorasmian Online","url":"https://chorasmianonline.melc.berkeley.edu/2021/12/23/chorasmian-choresmian-khwarazmian-khwarezmian-or-khwarizmian/"},{"title":"Khwarazmian","url":"https://en.wikipedia.org/wiki/Khwarazmian"},{"title":"خوارزم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85"},{"title":"Khwarazm - Reference.org","url":"https://reference.org/facts/Khwarazm/DIhw5ofr"},{"title":"Khwarezm","url":"https://en-academic.com/dic.nsf/enwiki/189748"},{"title":"Khwarazm — Grokipedia","url":"https://grokipedia.com/page/Khwarazm"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/317992"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/44406/concepts?page=2"}]

Based on the search results, I found relevant information about the etymology of Khwarazm that addresses your query:

The Old Persian form is attested as (h)uvārazmiš. The word itself looks like a compound, with the first part derived from *hwāra- "low" (as was already recognized by MacKenzie), and the second part could be *zm-, the zero-grade of *zam- "land".

This etymology suggests the name means "lowland" or "low land," which is consistent with the geography of the region. Another view is that the Iranian compound stands for 'lowland' from 'low' and 'land'. Khwarazm is indeed the lowest region in Central Asia (except for the Caspian Sea to the far west), located on the delta of the Amu Darya on the southern shores of the Aral Sea.

However, there are alternative etymologies proposed by other scholars as well. These forms have been interpreted by scholars as either "nourishing land" (from hwāra- denoting abundance or fertility) or "friend-land" (from hwar- meaning "friend" or "ally," implying a hospitable or allied territory).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:15:07.343Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nhits=[i for i,p in enumerate(pages[:230]) if 'خوارزم' in p]\nprint('intro leaves with خوارزم:',hits)\nfor i in hits[:6]:\n    import re\n    txt=pages[i]\n    idx=txt.find('خوارزم')\n    print('--- leaf',i)\n    print(txt[max(0,idx-400):idx+400])\nEOF"
}
```


### [2026-09-14T03:15:08.526Z] TOOL RESULT

```
leaves 777
intro leaves with خوارزم: [30, 31, 37, 38, 40, 53, 113, 114, 151, 216, 219]
--- leaf 30
0۳۵۵۲۵ 18 تاه ه۱۱۵)6 ر ](ا)ارل1۳ . 8
,1938 ,.۸.] تجدید طبم از . ۳۳6۱6 نومه
0 . ۵۲۵۱ . 4وعا. اذه موه اهع01م5
۲ .1934
ما 1۳21:۲۵۵۸ ر ۳۳۸۲۷۱۷۲۸۲ . ۸ .۸
0 . ۲202۲۱۳۷۸۵۸۸۵ ب عصال نخجمع و اصع ام
۰ 6 ۲۵۱۸۱۱۵۸۳۵۸ . 5591 و۱۲
خوارزم با خبوه» سر زمینیاست‌در مجر ای سفلی آمو
دریا؛ و آن ازقدیم در تمدن آسیای مر کزی موّنر
بوده‌استو عضده مار کوارت۱ در بن باب قر یب تحقیات است که گو یدائیر انم
و ئجو ۸۱۳۷۵6۵۱۷۵616 (سرزمیت اصلی ایرانیان) -موطن اوستا -
همان خوارزم است؟ وخوارزهبان‌ایر انیت خود را درطی‌قرون متمادی حفقظط
کردند. ابوریحان بیرونی گوید ۴ : «اهل خوارزم ... کانواغصنا من‌دوحة-
الفرس . >
نام خو ارزم دراوستا خوارزم 98۲12610 و
--- leaf 31
پیست و ضه زیانبای ایرانی
لغات ز بان خوارزمی نیژ بواژه‌های فارسی‌شباهت دارد.اينك نمونه‌ای
ازی لفات ۲ :
اردو شت <- ارد سپشت» هر وداد <خرداد » جبری ح بر » اخشر بوری
شهر یور» اسبندارمجی < |سیندارعذ» ریمژد -هر مزد. دذو دی » اخیر
خور ماه ما غوشت <- گوش . اسروف سزوش ۰ رشن رشن +
رام رام؛ واذح باد؛ دینی <دین؛ وی ۳۷ اشتاذ - اشتاد»اسمان
- [سمان؛ مر سبند << مار اسفنده "اونرغ <انیر ان ۴
بر ای اطلاع بیشتر از"زبان خوارزمی بمآخذ ذیل رجوع شود:
۵۳۵2۲
--- leaf 37
و | لخو زیة‌والسر یانیه۴. فاماا لفهلو بة
فنسوب‌الی فیلة - اسمیقم‌علی‌خمسة بلدان وهی‌اصفهان والری‌وهیدان وماه
نپاو ندو اذر بیجان؛و اما| لدر يةفلفة مدنالمدائن و بپاکان‌یتکلم من بیاب|لملك‌و
هی‌منسو بة الی‌حاضرةالباب و القا لب‌علیپامن لفة اهل‌خر اسان والمشر لهة‌اهل
بلخ ؛ و اما الفارسية فیتکلم بهاالوابدة و الطماه واشباههم و می لفةاهل
فارس . ۳
از این عبارت صر بحا ۳ میاأید که رز در ردیف پپلوی
بوده‌است ,
خوارزمی در مفاتیع العلوم آرد ۴ : < الدریة » لفت اهل شبرهای
مدائن است و کساننکه در دربار شاه بودند بدان ستن میگفتند ۰ س آین
کلمه منسوب بحاضر ان در دار است» واز س لفات اهل‌مشرق لغت مردم
بر آن غالب است .>
باقفوت در معجم البلدان ذیل < فپلو > نوسده :حیز ماصفهانی در
کتاب|لتنبیه۱ گوید :
کلام‌ایرانیان۷ در قدیم برینج زبان جاری بود ازاینقرار : پپلوی »
دری ؛ پارسی»خوزی وسریانی . امابپلوی؛ کلام پادشاهان‌در مج
--- leaf 38
دوز بان
بپلوی و بارسی اختلافات [نهارا آشکار میسازد ازقبیل آوردن فل مفرد
برای‌فاعل جمم‌وحذف ضیرمتکلم وقدیم ضایر متصل بر فعل در پپلوی که
لاف بر سر انست 0
2-۱ ر: جهانگیری و برهان قاطم .(مقدمةٌ مولف ص ی)۲"رل: ديباچة مولفصی-یا .
۳- مرحوم‌بهارنوشته‌اند (سيك‌شناسی‌ج۱ ص۲۸):درین"موردباید فرض کرد که‌نوسن دکان
مز بوردر فرن‌های درم وسوم هجری غالبا ازانحاء ابران و لهجه‌های مختلف این کشور و زبان عای
ء.الکی جون خوارزم وسقد وسگتان وطبرستان وآذربایجان بی‌خبی بوده‌اند و از حدود مداین
وفاری وعراقعجم وخوزستان بیرون نرفته واطلاعی نداشته‌اند. تنها بذ کر لغات این اماکن ولفت
سربانی ولغت درباری که ازآن بدری تعبیر هیکنند » اکتفا کرده‌اند . » وفرهنگه نوسان نیز از
آنان تفلید کردماند . 4- ر: پورداود . فرهنگه ابران باستان ح ۱ص ۱۷۱ سمد .
ه - مرحوم‌بهار(مبك‌شناسی ج۱ ص۳۰4ببمد) درین‌پاب نظربات خودرا آورده‌اند وسزاوار
است‌ا
--- leaf 40
مقدمه سی و دو
«دری» و«پارسی» دوزبان جدا گانه بشماررفته است»[یا چنین‌است؛
وری منسوب است‌به «در> بمعنی‌دربار » چنانکه ابن‌المقفع وحمزه
وخوارزمی ودیگران تصر یح کر ده‌|ند ۱ واشتفاقات دیگر که برای این کلمه
ذکر کرده اند یی ارزش است ۴ .
شك نیست که دری در دورء اسلامی بهمینز بان معمول پارسی بس‌از
اسلام‌اطلان میشده‌است؛ اينك شواهد آن :
همان بیورسیش؟ همی خو اند ند چنین نام بر پهلوی راند ند
کجا بیور از بهلوانی شمار بود در زبان دری ده هزار.
فردوسی‌طوسی. شاهنامه بخج۱ص۲۸.
دل‌بدان یافتی‌ازمن که نکودانی خواند مدحت خواجه آزاده ۴با لفاظدری.
فرخی‌س
--- leaf 53
ف و تحرف سیار شدهء‌است» از جمله:
در نسخ شاهنامه آعده:
(عیسی) یکی یینوا مرد درویش بود که نانش ز رنج تن خویش‌بود
جزاز برف وشیرش نبودی خورض فزو نیش روغن بدی پرورش ۱ .
خورش ساختن از برف وشیر چه معنی دارد ۲ صحیح < ترف > است
در مصزاع اول و < رخبن > است در مصراع دوم که علامه دهغدا تصحیح
کرده‌اند بدلایل وقرائن ذیل :
بشمر تر فند ار قرف بودم و دخیین «یند وحکمت اکنون چوشکر وقندم.
۱ سوزنی سمرفندی .
و از وی ( خوارزم ) روی مشده و قز ۲ کند و کر باس ونمد و ترف
ور خیبی خیزد. «حدودا لعا لم >.رخبین» ترف‌سرخ <مپذب‌الاسماه>. فره‌قروت
< بحرالجواهر >. کشکی است که از دوغ سازند < حاشيةٌ فرهشگ اسدی
۱- شاهنامة بخ ج ه ص ۱۷۱۱ ( متن وع)
```


## [2026-09-14T03:15:23.588Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[30]\ni=p.find('خوارزم با خبوه')\nprint(p[i:i+1500])\nprint('===== HEADER leaf30 =====')\nprint(p[:200])\nprint('===== HEADER leaf40 =====')\nprint(pages[40][:120])\nEOF"
}
```


### [2026-09-14T03:15:24.672Z] TOOL RESULT

```
خوارزم با خبوه» سر زمینیاست‌در مجر ای سفلی آمو
دریا؛ و آن ازقدیم در تمدن آسیای مر کزی موّنر
بوده‌استو عضده مار کوارت۱ در بن باب قر یب تحقیات است که گو یدائیر انم
و ئجو ۸۱۳۷۵6۵۱۷۵616 (سرزمیت اصلی ایرانیان) -موطن اوستا -
همان خوارزم است؟ وخوارزهبان‌ایر انیت خود را درطی‌قرون متمادی حفقظط
کردند. ابوریحان بیرونی گوید ۴ : «اهل خوارزم ... کانواغصنا من‌دوحة-
الفرس . >
نام خو ارزم دراوستا خوارزم 98۲12610 ودر کتیبه‌های هخامنشی
(یارسی باستان) هو ارزمیش ۷۵۳22۵18 (11) آمده (ست ۴
خوارزمی زبانی است که در خوارزم قدیم معمول بوده و فقط درین
اواخر برائر حفریاتی که درچندسال اخیردر خوارزم کرده‌انده شناخته شده
است ۵ . در نتیجهٌ حفر بات مز بور گاه‌شاری خوارزمی‌واعلام تاریخیی بدست
آمده که برای روشن کردن بخشی ازتاریخ ايران و نيزدر تصحیح کتا بهایی
مانندآثار الباقيةٌ بیرونی مورد استفاد؛ بسیار است ۲ . بیرو نی درین‌تألیف
نیس خود خوارزمی ۰۷ روزهای‌خوارزمی ۸ ,ومنازل قمررا
بر بان خوارزمی * تقل کرده است *۱
اخیراً کتایی وق اما با , خوارزمی‌دراستانبول بیدا شده است ۷۱.
5۰ ۳ ,1901 47118 ,۳۲۳۵۸0۵۵۵ رن را ٩‏
_ دائرقالیمارف اسللام : خوارزم بقلم بارتولد. آثار الباقیه چاپ زاخاو ص
۳۹7 ۴ - دائیتالمعارف اسلام: ۳665 ۰ زبان 8  *‏ هننگ.
کتبه‌های پهلوی نرجمهٌ نگارنده ص٩۱‏ . 1 استاد فرربمان ۸-۳۲6۷۳020 درنامهٌ مورخ
همه ۱۹6۵ بنگارنده توشته‌اند: «من مقاله‌ای درخصوص زبان خوارزمی «مقالهٌ دمگر درباب مواد
حتامنشی نوشتهلم. اگر آنها شاستة اهداء با قای پورداود باشند. بنام ابشان اتحاف ودر اینجاطبم
خولعم کرد. » ۷ - آارالبافه ص4۷ و۲۳۹ -۳۹. ۸ - همان کتاب ص4۷ سه4.
٩‏ _ همان کناب ص *۲۸. * . رل : روزشماری دراران باستان بقلم نگارنده .
صحمداحا
===== HEADER leaf30 =====
0۳۵۵۲۵ 18 تاه ه۱۱۵)6 ر ](ا)ارل1۳ . 8
,1938 ,.۸.] تجدید طبم از . ۳۳6۱6 نومه
0 . ۵۲۵۱ . 4وعا. اذه موه اهع01م5
۲ .1934
ما 1۳21:۲۵۵۸ ر ۳۳۸۲۷۱۷۲۸۲ . ۸ .۸
0 . ۲202۲۱۳۷۸۵۸۸۵ ب عصال نخجمع و اصع ام
۰ 6 ۲۵۱۸۱۱۵
===== HEADER leaf40 =====
مقدمه سی و دو
«دری» و«پارسی» دوزبان جدا گانه بشماررفته است»[یا چنین‌است؛
وری منسوب است‌به «در> بمعنی‌دربار » چنانکه ابن‌
```


## [2026-09-14T03:15:38.183Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON parts خوارزم ===\"; grep -c \"خوارزم\" MON_part1.txt MON_part2.txt 2>/dev/null\necho \"=== LKT algorismus ===\"; grep -n -i \"algorism\\|Alchwarizmi\\|Chwarizmi\" LKT.txt | head -6\necho \"=== SKT algorism ===\"; grep -n -i \"algorism\\|algebra\" SKT.txt | head -6\necho \"=== HRN/HUB خوارزم ===\"; grep -n -i \"Chwarezm\\|Chwarizm\\|Choresm\\|Chorasm\" HRN.txt HUB.txt | head -6\necho \"=== PHD xwarazm ===\"; grep -n -i \"xwarazm\\|hwarazm\\|Xwārazm\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -6"
}
```


### [2026-09-14T03:15:38.310Z] TOOL RESULT

```
=== MON parts خوارزم ===
MON_part1.txt:7
MON_part2.txt:9
=== LKT algorismus ===
2144:"NTpr.,  eine  Landschaft  in  Mittelasien  [dem heutigen  Chanate  Ghiva-HIwa  entspre- chend]; davon  das  ar.  Adj.  hnärizmi  od. härizmi  'aus  Hwarizm  stammend,  der Gharizmier',  Beiname  des  Mathematikers ABÜ  GA'FAR  MUHAMMAD  IHN  MÜSÄ [s.  hier  Nr.  631];  durch  sein  Werk  über Algebra  kam  das  dekadische  Zahlensystem und  das  Rechnen  mit  ar.  Zahlen  um  das Jahr  1200  nach  Europa;  daher  wurde  lat. algorithmus,  algorismus  [mit  Anlehnung an  gr.  öpi&|ui6<;]  die  Bezeichnung  für  das Rechnen  mit  ar.  Ziffern  u.  schließlich  für Rechnungsverfahren  überhaupt.  Hieraus afrz.  algofisme,frz.  algorithme,it.alguaris- nio  'Rechenart,  Arithmetik',  sp.  alguaris- nio,  guarismo  'Ziffer',  engl,  algorism, algorithm  'Rechenart'.  [DE  130/131. WOEPGKE  in  JAs  (1863)  I,  519.  Devic DEt  18.  Lammens  Rem  13.  Schirmer WortschdMath  4/5.
5918:algorism  890
7423:Aegidius  951 aegyptus  1222 alambicum  79 alchanna  867 algorismus  890 algorithmus  890 alleluia  793 ahnageshim  1348 almutium  1520 amaracum  1411 amen  68
=== SKT algorism ===
104:therefore  introduce  this  symbol  +  by  way  of  warning.     It.  has ttsual  algebraical  value  o^ plus  or  additional  \  and  indicates  *addiLioi information  to  be  obtained  from  the  comparison  of  cognate  forms.*
514:ALGEBRA.  7
529:Algebra.   (Low  L.  —  Arab.)      J-ow  L
23694:Low  lAtin  from  Ar&he:  Algebra, aaraccn.
=== HRN/HUB خوارزم ===
HUB.txt:9794:mehrerer Tage, chorasmisch etwa daiu (Al-
HRN.txt:8806:Artaky§]midan, Stadt in Chorasmien (Yäqüt), Xas-
HRN.txt:8881:Brot'; vergl. chorasm. pekend (Vullers); hei. nagan,
=== PHD xwarazm ===
```


## [2026-09-14T03:15:50.153Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خوارزم\" MON_part1.txt | head -8 | cut -c1-300\necho \"=== الگوریتم ===\"\ngrep -rn \"الگوریتم\\|آلگوریتم\" MON_part1.txt MON_part2.txt BQT_v1_pages.txt 2>/dev/null | head -5\necho \"=== ARY خوارزم ===\"\ngrep -n \"خوارزم\" incoming/ARY/ARY_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-09-14T03:15:50.321Z] TOOL RESULT

```
7532:اجفار: 21۳3 [خوارزمی» آنشن افر و خته ] 
7533:(.) روز شانزدهم ماه چهارم مغان خوارزم: 
18235:خوارزمشاهیان. (امص.) سپری شدگی» 
57662:بنابراین رخوارزم» را «خوارزم» به فتح خاو 
60883:شعیره کمتر است.» خوارزمی در مفاتیح 
75068:غزنوی» سلجوقی و خوارزمشاهی تعقیب 
92721:(خوارزمی ص ٩‏ ۵). صورت مالیاتی (تاریخ 
=== الگوریتم ===
=== ARY خوارزم ===
1157:تومشرگی (71718771701788)) سغدی (80001۸30) با کتربایی (8۸2771۸0 خوارزمی
```


## [2026-09-14T03:15:53.411Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57640,57680p' MON_part1.txt"
}
```


### [2026-09-14T03:15:53.541Z] TOOL RESULT

```
نید ۵: (2:۸-12)۵ (امف.) مسعروف» 
شهرت افته. 

حنید ه۵: (0-)2]-2:7 (امف.) سروده خوانده 
شده. دانای در کار سرود؛ مصنف» 
موسیقی‌دان. (ا.) صدا و آوازی که در میان 
دو کوه و گنبد و خم و مانند آن تود: 
حنید ۵: (۵-)۵2-10۸ (ص.) سند یده. 

حو: ۷ یکی از حروف صامت در زبان 
پهلوی و دری قدیم» و واوی را که بعد از 
حرف «خ» قرار میگرفته «واو معدوله» 
می‌نامیده‌اند و تلفظ آن ترکیبی از خ + و 
بوده و در تلفظ بایستی حرف اول را ابتدا به 
ساکن خواند و واوی مفتوح را در آن فرو 
برد (مانند: خواب؛ خورشید). در قرون اخیر 
تلفظ این حرف فراموش شد و تنها کردان 
مرت ابران آن را درست تلفظ می‌کنند و 
بختیاریان خای مفتوح و طبرستانیان خاء 
مکسور و دیگران خاء مضموم ادا سازند و 
تازیان نیز اين حرف را نداشته و ندارند. 
بنابراین رخوارزم» را «خوارزم» به فتح خاو 
به تصریح واو گویند و گاه واو بعد از خ 
حذف می‌شود مثل خراسان و خرداد. 

حو:. ۵۷۷۵۷۷ (۰۱) ( کیا.) کیاه خو درو که در 
میان غله‌زارها و باغ‌ها روید؛ علف هرزه. 
(گیا.) هر گیاه که خود را به درخت پیچد 
(عموما). (گیا.) عشقه؛» لبلاب اتضوش . 
حو: (۷00۷:() چوب بنایی که ننایان و 
نقاشان در درون و بیرون عمارت ترتیب 


۴۰ 
دهند و بر بالای آن کار کنند؛ جوبت ست. 
قالبی که بنایان طاق بر بالای آن زنند. 
خواب: (قد. 56050 (.) حالتی توأم با 
آسایش و آرامش که بر اثر از کار بازماندن 
حواس ظاهر در انسان و حیوان پدید آید؛ 
نوم؛ مق. بیداری» یقظه. غفلت. پرز جامه
```


## [2026-09-14T03:16:08.271Z] TOOL CALL #42: Bash

```json
{
 "command": "pdftoppm -f 485 -l 485 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg485 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg485.png",
 "description": "Render PDF page 485 to PNG"
}
```


### [2026-09-14T03:16:09.993Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 90150 Sep 13 23:16 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg485.png
```


## [2026-09-14T03:16:10.335Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://chorasmianonline.melc.berkeley.edu/2021/12/23/chorasmian-choresmian-khwarazmian-khwarezmian-or-khwarizmian/",
 "prompt": "Quote what this page says about the etymology of the name Khwarazm / Chorasmia: the Old Persian form, the analysis *hwāra- 'low' + *zm- 'land' (MacKenzie), and any rejection of 'good land' or 'sun land' etymologies."
}
```


### [2026-09-14T03:16:13.942Z] TOOL RESULT

```
# Etymology of Khwarazm/Chorasmia

According to the page, the Old Persian form is attested as "nom.sg. _(h)uvārazmiš_ <u-v-a-r-z-mi-i-š>" in sources like XPh.

The analysis proposed by MacKenzie breaks down the name as a compound: "the first part derived from \*hwāra- 'low' (as was already recognized by MacKenzie (1983, p. 1244). The second part could be \*zm-, the zero-grade of \*zam- 'land'." This yields a meaning of "low-lands," which makes geographical sense given the region's marshy terrain.

The page does not explicitly reject alternative etymologies like "good land" or "sun land," so no dismissal of those interpretations is documented here.
```


## [2026-09-14T03:16:16.357Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg485.png"
}
```


### [2026-09-14T03:16:17.113Z] TOOL RESULT

```

```


## [2026-09-14T03:16:17.110Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:16:36.993Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"urada-|uraθa|uratha|uradana\" KNT.txt | head -5 | cut -c1-500\necho \"--- copy png ---\"\nmkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg485.png ocr/BOOK/485.png && ls -la ocr/BOOK/485.png"
}
```


### [2026-09-14T03:16:38.006Z] TOOL RESULT

```
1182:ardastina-, Ardumants, avahar|da], uradana-, dan-
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.
5196:urafara- adj. ‘having good charioteers’: deriv. of urada- ($148.1). [u|raüaram asn. DSp 3 (Bv. BSLP 33.2.0451 and Hz. AMI 4.126 restore |f\raBaram).
5197:uradana- adj. ‘of good regulation’: u- ‘good’
5855:?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
--- copy png ---
-rw-rw-r-- 1 sfmqrb sfmqrb 90150 Sep 13 23:16 ocr/BOOK/485.png
```


## [2026-09-14T03:16:59.004Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT algorism ===\"; grep -n \"^Algorism\\|Algorism\\b\" SKT.txt | head -5 | cut -c1-400\necho \"=== DEV/PHN algorithme ===\"; grep -n -i \"algorithme\\|algorisme\" DEV.txt PHN.txt LAM.txt | head -6 | cut -c1-400\necho \"=== FSD/WEB algorism ===\"; grep -n -i \"algorism\" FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -4 | cut -c1-400\necho \"=== BRT huvaxsatra / Kavi ===\"; grep -n -i \"huvaxs\\|Huvaxšatra\\|Kyaxares\\|Kyaxaves\" BRT.txt | head -6 | cut -c1-300"
}
```


### [2026-09-14T03:16:59.135Z] TOOL RESULT

```
=== SKT algorism ===
=== DEV/PHN algorithme ===
LAM.txt:1499:Algorithme. Aux formes romanes citées par M. Devic
LAM.txt:4279:(1) Comp. algorithme de VJtjïjiJI . galanga de ol^^Ui.- Pihan dérive gala
LAM.txt:8363:Algorithme
DEV.txt:399:Algorithme.  Au  xiif  siècle,  ce  mot  signifiait  l'arithmé- tique avec  les  chiffres  arabes;  on  écrivait  algorisme  et  an- gorisme  ^  Esp.  aJguarismo ^  guarismo,  aJgorithmo;  portug. garismo.  C'est  la  transcription  plus  ou  moins  altérée  du nom  d'un  des  plus  anciens  auteurs  de  traités  d'arithmé- tique, Abou  Dja'far  Mohammed  ben  Mousâ,  surnomm�
DEV.txt:2565:Algorisme,  voy.  Algorithme.
DEV.txt:2566:Algorismus,  b.  lat.  voy.  Algorithme,
=== FSD/WEB algorism ===
WEB_vol1.txt:5481:al’gi-rism, al’g6-rithm, n. [OFr. algorisme;
WEB_vol1.txt:5486:L. algorismus, the Arabic system of numbers; from Ar. al-Khowdrazmi, a native of Khwar- azrn (Khiva), z Arabic mathematician of the ninth century. a L. namena computation, or the decimal systern of counting. aes 2. the common rules of computation in any branch of numerical analysis; as, the algo- rism of the differential calculus. ao al’/gous, a. pe alga, ci bile, pertaining to
FSD_vol1.txt:11700:metlclan.—  aFgo-ris'tlc,  a.  Of  or  pertaining  to  an  algorist or  algorism.
=== BRT huvaxsatra / Kavi ===
```


## [2026-09-14T03:17:03.901Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '399p' DEV.txt | cut -c1-1400\necho \"=== LAM 1499 ===\"; sed -n '1499,1502p' LAM.txt | cut -c1-600"
}
```


### [2026-09-14T03:17:03.973Z] TOOL RESULT

```
Algorithme.  Au  xiif  siècle,  ce  mot  signifiait  l'arithmé- tique avec  les  chiffres  arabes;  on  écrivait  algorisme  et  an- gorisme  ^  Esp.  aJguarismo ^  guarismo,  aJgorithmo;  portug. garismo.  C'est  la  transcription  plus  ou  moins  altérée  du nom  d'un  des  plus  anciens  auteurs  de  traités  d'arithmé- tique, Abou  Dja'far  Mohammed  ben  Mousâ,  surnommé ^'^^]^  al-khowârezmi ,  dont  l'ouvrage  a  été  traduit  ou  imité en  latin  dès  le  commencement  du  xif  siècle.  Ces  sortes de  livres  furent  désignés  sous  le  nom  à'Algorismus.  M.  De- frémery  a  raison  de  dire  ^  que  cette  étymologie  est  hors de  doute  depuis  les  recherches  de  MM.  Reinaud  ^,  Chastes  ' et  Woepcke^.  Dans  les  ouvrages  d'astronomie,  le  terme ^^'^^\yâ^  khowârezmi  s'est  dit  des  tables  des  sinus  et  des tables  des  ombres  (tangentes  et  cotangentes  trigonomé- triques).
=== LAM 1499 ===
Algorithme. Aux formes romanes citées par M. Devic
ajoutez les suivantes : Esp : algurismo, alguarismo, argo-
rismo. Ptg: algarismo, algorismo. Val: algoritme;de
ç^3j*j>* alkhauâri;[mi, Mathématicien arabe ( V. Devic et
```


## [2026-09-14T03:17:12.644Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://fa.wikipedia.org/wiki/%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85",
 "prompt": "What does the article say about the Persian word الگوریتم — its spelling, its origin (from French/European languages, and ultimately from خوارزمی)? Quote the etymological sentence in Persian."
}
```


### [2026-09-14T03:17:17.794Z] TOOL RESULT

```
# Etymology of الگوریتم

The article traces the Persian word الگوریتم back to the name of the Persian scholar al-Khwarizmi. Here is the key etymological statement:

"واژه _الگوریتم_ اقتباسی از نام همه‌چیزدان ایرانی، [خوارزمی](https://fa.wikipedia.org/wiki/خوارزمی "خوارزمی") است."

This translates to: The word الگوریتم is borrowed from the name of the Persian polymath al-Khwarizmi.

The article explains that the term evolved through several linguistic stages:
- His name was Latinized as "Algoritmi" in the 12th century
- By the 13th century, it became "Algorismus" (meaning "Arab numeral system")
- In the 19th century, it transformed into the French form "Algorithme"
- Finally, it entered English as "Algorithm" in the late 19th century with its modern, broader meaning
```


## [2026-09-14T03:17:29.143Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85' --note 'page 485, root Su 1/Esu/Wesu, node 4: Persian خوارزم < MP Xwārazm < OP Uvārazmiš' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/algorithm' --note 'page 485, nodes 6-9: algorism/algorithm < ML algorismus < Ar. al-Khwarizmi; -ithm by contamination with Gk arithmos' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wikipedia.org/wiki/Khwarazm' --note 'page 485, nodes 2-4: Names and etymology of Khwarazm; Avestan Xvairizəm, OP Uvārazmiš; competing etymologies (xwar sun / xwār low + zam land)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-' --note 'page 485, root box: PIE *h1su- good, possibly metathesis of *h1wes-; descendants OP u-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://chorasmianonline.melc.berkeley.edu/2021/12/23/chorasmian-choresmian-khwarazmian-khwarezmian-or-khwarizmian/' --note 'page 485, node 2: MacKenzie 1983 p.1244 *hwara- low + *zm- land = lowland, vs Kent u- good + vara- + zmi-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://fa.wikipedia.org/wiki/%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85' --note 'page 485, node 8: Persian الگوریتم/آلگوریتم borrowed from French algorithme, ultimately from خوارزمی' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-14T03:17:32.277Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/113b483b9044df4a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4d7501a1c70bce5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/665ecff8e7934338.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0796cdb8411b4cf9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65eedfdfd0160a01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0af916cb2dd502d8.txt
```


## [2026-09-14T03:17:34.847Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T03:17:34.899Z] TOOL RESULT

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


## [2026-09-14T03:17:50.829Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 esu/su ===\"; grep -n \"esu-s\\|esu-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -6 | cut -c1-300\necho \"=== WLD Bd1 uesu ===\"; grep -n \"uesu\\|u̯esu\\|ųesu\\|vesu-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt WLD_band3.txt | head -6 | cut -c1-300\necho \"=== WLD su- gut ===\"; grep -n \"su-, *,gut\\|su- ,wohl\\|apers. u-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -6 | cut -c1-400"
}
```


### [2026-09-14T03:17:50.940Z] TOOL RESULT

```
=== WLD Bd1 esu/su ===
13407:eine von euch beiden". sethar „euer“: und mit Anlaut esu- got. izicis „euch“. 
15563:I 4 545f. ; doch s. Pedersen KG. I 75, 74 und *tiesu- „gut“i, aksl. vest ho 
19498:Uber das wahrscheinlich verwandte idg. 'uesu- ,,gut‘‘ s. d. — Urspriing- 
19505:„agere. gerere" (Brugmarin IF. 15, 90). Allerdings steht neben *nesu- „gut -< 
19531:ues- „yerweilen“ s. d., wo aueh iiber lat. Vesta. S. ferner *uesu- ,,gut“. 
19649:uesu- — ues-r, ues-(e'n- 
=== WLD Bd1 uesu ===
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19498:Uber das wahrscheinlich verwandte idg. 'uesu- ,,gut‘‘ s. d. — Urspriing- 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19531:ues- „yerweilen“ s. d., wo aueh iiber lat. Vesta. S. ferner *uesu- ,,gut“. 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19649:uesu- — ues-r, ues-(e'n- 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19664:uesu- ,,gut" (voller tuts-, s. u.). 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19673:trefflichkeit" aus *uesu-d, fehus ..Yortreffliehkeit", *fehtu, gen. fehtad gl. 
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:19692:riickzugehn scheint, dagegen uesu- wegen got. iusiza auf *curs- ; Mittelbegriff 
=== WLD su- gut ===
```


## [2026-09-14T03:17:57.627Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3889,3900p' POK_03.txt | cut -c1-900\necho \"=== WLD Bd2 su- ===\"\ngrep -n \"su- ,,wohl\\|su-, ,,gut\\|su- „wohl\\|su- „gut\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5 | cut -c1-300"
}
```


### [2026-09-14T03:17:57.728Z] TOOL RESULT

```
so-  ,wohl,  gut'  als  1.  Kompositionsglied;  su-bhago-  ,beglückend'. Ai.  SU-,  av.  /m-,  apers.  u-,  z.  B.  in  ai.  su-drü-  , starkes   Holz'  su-bhdga- [iClticklich,  beglückend',  av.  hu-baya-  , gutes  Eheglück  gewährend'; ?r.  vyLTJg  ,gesund'  (*su-gni{es  , wohllebend*) ;
gall.  SU-    (z.  B.   Su-carus  =)    cymr.    hy-gar   , Hebens  würdig',   corn.   hy-, fet,  he-,  air.  su-,  so-  (z.  B.  su-thain  ,ewig',  so-scel{a)e  , Evangelium') ;
1038  •
germ.  su-  in  Su-gamhri  VN,   aisl.   sü-svort  f.   ,Schwarzamsel'  (,^ Schwarze');
lit.  südrus  ,gei\,  üppig*;  aksl.  s^drav^  „tyLrjg"  ,öech.  zdravy  (y^^  *_ ai.  su-drü-)  usw.;  slav.  '^s-bbozhje,  cech.  zhozi  ^Besitztum'  aus  *si>-log^  t^^ suhhdga-,  oben  S.  107);
SU-  ist  Tief  stufe  zu  *swe-  (oben  S.  882  f.);  vgl.  ai.  sva-  in  sva-dhä  ^  g^. ,süßer  Trank'  (oben  S.  241),  svd-dhita-  =  sü-dhita-  ,fest,  gesund*;
WH.  II  512,  E.  Fraenkel  Mel.  Pedersen  443  ff.,  Vasmer  1,  450  f.
sü-Sf  suu-ös  , Hausschwein,  Sau';  erweitert  su-ko-]  suuino-  ,zum  Scl»W|^ gehörig'.  -
Av.  hü  (Gen.  Sg.  für  *huvö)  , Schwein';  gr.  ^g,  vög,  Akk.  h  m.  J^
f.  ,Sau'  (davon  ilaiva  f.  , Hyäne')  neben  (xvg,  avög  ds. ;  dazu  ovfjlai' t4n^
ßoQßoQwösig  Hes. ;  av(pE{C)6g,  ov(p6g  m.  ^Schweinestall  {*-q)£J^iog,  m
idg.  bheu-j  oben  S.  146 ff.);  Sternbild  der  'Yddsg  , Gruppe  von  Schi
=== WLD Bd2 su- ===
```


## [2026-09-14T03:18:08.840Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"su-bhago\\|subhago\\|su-drü\\|sudru\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5 | cut -c1-300\necho \"--- Bd1 ---\"\ngrep -n \"su-bhago\\|apers. u-\\|av. hu-,\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5 | cut -c1-300\necho \"--- IEC su ---\"\ngrep -n \"^su- \\|su- 'good'\\|esu-\" IEC.txt | head -5 | cut -c1-250"
}
```


### [2026-09-14T03:18:08.947Z] TOOL RESULT

```
--- Bd1 ---
--- IEC su ---
2228:deus- ‘evil. Cf. dus- and next. Cf. also desu- Skt. dosah ‘defect, crime, evi’; OE teosu *harm'; Hes. cf. deulós 'grievous'; W Ger. cf. zies-ig ‘regressive’; Sw. tjusa, fórtjusa “be- witch'. (Oxytonic root in OE teorian “fail, ce
17774:su- (2) ewell" Aphetic (z-gde) of esus , q. v. WP II, 512 Skt. cf. sú-krtah ‘well-made’; Av. hu-korefs ‘shapely’; hu-naro ‘virtue’; Per. hu-nar “art, science" (LW in Arm. hnark, id.); Arm. h-lu, adj. ‘obedient’; h-mut, gs: h-
17775:su- (3) z-gde of type sue-, suo-, q. v. (Alb. type susios, à) Gk. cf. huiós E huiüs, m. ‘son’; hui-dé 'grand- daughter; hui-deós and -doüs ‘grandson’; hui-onós, m. id.; Alb. cf. gjysh ‘grandfather’; gjyshe, f. ‘grandmother�
17776:su- (4) *with-, together-. See sum
18017:suesios “apart, alone; own, private’. Cf. suetios, suesue, seue, suelos, etc. WP II, 455. See next. (Variants in Iran.) Per. xwi$ “own; self; kinsman, son-in-law'; xwisan ‘kinsfolk’; xi3i, s. ‘kinship’; Kurd, xó$ ‘kinsman’; O
```


## [2026-09-14T03:18:16.883Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"esus \" IEC.txt | head -4 | cut -c1-400\necho \"--- WLD Bd2 p512 su ---\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt',encoding='utf-8',errors='replace').read()\ni=t.find('esu-s')\nprint('esu-s idx',i)\nfor k in ['su- „gut','su-, ,,gut','esus','hu-kdrdfs','sukrta']:\n    print(k, t.find(k))\nEOF"
}
```


### [2026-09-14T03:18:18.047Z] TOOL RESULT

```
3433:eds-, edsmn- “eating; food’. See ëd- and de- rivatives Per. aš ‘pap’; Lat. cf. sem-esus 'half-eaten'; OLat. cēsnās, pl., Lat. cena ‘mealtime’; Umb. cersnåf “food, supply’ (if fr. *ko-edsno-, -eds- na-); MHG as ‘carrion’; Du. aas ‘pasture’; OE æs, n. “food, bait, carrion’; Li. cf. ésena “fod- der”
3722:esros “good, fine, noble, grand'. Cf. es-mi, esulos, esus Lat. *ebrus (in in-ebrae aves 'inauspicious birds”); Ir. earr ‘noble, grand"
3733:esus (əsus, su-) (1) ‘good, true’. Cf. su-, uesus. Cf. WP II 512; I, 161 Skt. cf. su-, px.; Av. hu-, id.; Arm. ge ‘rich, powerful; Oss. äx-, px. ‘good-; Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós; áotos (*osu- + Gk. -atos); Hitt. assus; Umb. (?) eruhu (suitable. A wd. of ambig. spg. and mng.); Ligurian (?) Esu- (in Esu- biani, an Alpine tribe); Mir eo (2) ‘goog�
3745:esus (esos, esi-) (2) “animal, breath, being”. Cf. es-mi, etc. Skt. ásuh (Ð “breath, life; Av. àhus (2) ‘world, place’; cf. áha ‘mind’; áhva “self, being’; Per. ahü deer": Arm. cf. ir, -i, -av, a-st. ‘thing, fact’; irav ‘rightly’; iravi, adj. ‘true’ from a type *esiiə)
--- WLD Bd2 p512 su ---
esu-s idx -1
su- „gut -1
su-, ,,gut -1
esus 353350
hu-kdrdfs -1
sukrta -1
```


## [2026-09-14T03:19:12.258Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://fa.wikipedia.org/wiki/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87",
 "prompt": "What Persian spellings of the Median king Cyaxares' name does the article give (هووخشتره، هوخشتر ...), and what Old Persian/Median original and etymology does it state?"
}
```


### [2026-09-14T03:19:13.959Z] TOOL RESULT

```
socket hang up
```


## [2026-09-14T03:19:16.983Z] TOOL CALL #56: WebSearch

```json
{
 "query": "\"هوخشتر\" OR \"هووخشتره\" کیاکسار پادشاه ماد نام اوستایی هوخشثره معنی"
}
```


### [2026-09-14T03:19:26.241Z] TOOL RESULT

```
Web search results for query: ""هوخشتر" OR "هووخشتره" کیاکسار پادشاه ماد نام اوستایی هوخشثره معنی"

Links: [{"title":"هوخشتر","url":"https://dehkhoda.ut.ac.ir/fa/dictionary/335998/هوخشتر"},{"title":"هوخشتره کیست | بیوگرافی و اقدامات مهم پادشاه ماد - کجارو","url":"https://www.kojaro.com/history-art-culture/192275-great-king--media/"},{"title":"هووخشتره سومین پادشاه ماد چه کسی بود؟ - تاریخ ما","url":"https://tarikhema.org/ancient/iran/42453/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87-%D8%B3%D9%88%D9%85%DB%8C%D9%86-%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87-%D9%85%D8%A7%D8%AF-%DA%86%D9%87-%DA%A9%D8%B3%DB%8C-%D8%A8%D9%88%D8%AF%D8%9F/"},{"title":"هووخشتره - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87"},{"title":"هوخشتر در دیکشنری های کمانک, تصویر هوخشتر","url":"https://fa.kamanak.com/pedia/subject/هوخشتر"},{"title":"هوخشتره؛ پادشاه قدرتمند مادها - کجارو | هوشمند نیوز | SHMI News Agency","url":"https://shmi.ir/%D9%87%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87%D8%9B-%D9%BE%D8%A7%D8%AF%D8%B4%D8%A7%D9%87-%D9%82%D8%AF%D8%B1%D8%AA%D9%85%D9%86%D8%AF-%D9%85%D8%A7%D8%AF%D9%87%D8%A7-%DA%A9%D8%AC%D8%A7%D8%B1%D9%88/"}]

بر اساس نتایج جستجو، اطلاعات زیر درباره هوخشتر (هووخشتره) و معادل‌های نام او ارائه می‌شود:

## هوخشتر/هووخشتره - پادشاه ماد

کیاکسار یا هوخشتره (۶۲۴-۵۸۵ قبل از میلاد) را بنیان‌گذار دولت ماد دانسته‌اند.

### نام‌های مختلف

هرودت نام این پادشاه را کرآکسار یا کیاکسار نوشته، اما از کتیبه‌ی بیستون داریوش اول معلوم می‌شود که نامش هوخشتر بوده است.

### معنی نام

برخی هوخشتره را ترکیبی از دو واژه پارسی باستان هو به‌معنای خوب و خشثره به‌معنای شهریار است که در مفهوم پادشاه خوب به کار می‌رود. همچنین برخی نیز نام هوخشتره را به معنی خوش نشانه دانسته‌اند؛ یعنی کسی که در نشانه گرفتن، ماهر است.

### موقعیت تاریخی

هوخشتره، سومین و بزرگ‌ترین پادشاه ماد بود که در زمان حکومت او، قدرت سیاسی، اقتصادی و نظامی مادها به اوج خود رسید.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:19:35.804Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://fa.wikipedia.org/wiki/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87' --note 'page 485, node 11: Persian هووخشتره/هوخشتر = Cyaxares, OP Uvaxštra' 2>&1 | tail -2",
 "description": "Archive fa.wikipedia Cyaxares page"
}
```


### [2026-09-14T03:19:37.723Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/380b706294cc5410.txt
```


## [2026-09-14T03:19:40.541Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -o \"هوخشتر[^.]\\{0,120\\}\" data/verification/sources/web/380b706294cc5410.txt | head -6\necho \"---\"\ngrep -o \"پارسی باستان[^.]\\{0,150\\}\" data/verification/sources/web/380b706294cc5410.txt | head -4"
}
```


### [2026-09-14T03:19:41.559Z] TOOL RESULT

```
هوخشتره را آمیزه ای از دو واژه پارسی باستان هو (خوب) و خشثره (شهریار) می‌دانند که در کل به معنی «پادشاه خوب» است
هوخشتره 
---
پارسی باستان : h Uvaxštra ، اکدی : m Ú-ak-sa-tar و m Uk-sa-tar ، ایلامی : m Ú-ak-sa-tar , m Uk-sa-tar و m Ú-ma-ku-iš-tar ، فریگی باستان : Ksuwaksaros ، یونانی : K
پارسی باستان «هو» (خوب) و «خشثره» (شاه) دانسته‌اند که در کل به معنی «پادشاه خوب» است
پارسی باستان هو (خوب) و خشثره (شهریار) می‌دانند که در کل به معنی «پادشاه خوب» است
```


## [2026-09-14T03:28:59.062Z] TOOL CALL #59: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/draft-485.py",
 "content": "# -*- coding: utf-8 -*-\nimport json\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-\"\nW_XWR = \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%B1%D8%B2%D9%85\"\nW_KHW = \"https://en.wikipedia.org/wiki/Khwarazm\"\nETY = \"https://www.etymonline.com/word/algorithm\"\nBERK = \"https://chorasmianonline.melc.berkeley.edu/2021/12/23/chorasmian-choresmian-khwarazmian-khwarezmian-or-khwarizmian/\"\nFA_ALG = \"https://fa.wikipedia.org/wiki/%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85\"\nFA_CYA = \"https://fa.wikipedia.org/wiki/%D9%87%D9%88%D9%88%D8%AE%D8%B4%D8%AA%D8%B1%D9%87\"\n\nKNT_U = (\"KNT.txt line 5158 (Lexicon, the page that ends at the '175' break): \"\n         \"\\\"u- insep. prefix 'good, well' (uv- before vowels): Av. hu-, Skt. su-, Gk. u-gies \"\n         \"'having good life, healthy', pIE *su- (140.IV): in uxsnav-, ukara-, ucara-, Utana-, utava-, \"\n         \"ubanwaniya-, ufrasta-, ubarta-, umartiya-, uratha-, uradana-, Uvaxstra-, Uvarazmi-, \"\n         \"uvarstika-, uvasabara-, uvaspa-, uvnara-, uhamaranakara-.\\\" (grep -n 'u- insep' KNT.txt)\")\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Su 1, Esu, Wesu\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *h₁su- 'good, well' (prefix; Pok. su- 1037), beside *h₁esu- (Pok. esu-s 342) and *h₁wesu- 'good' (Pok. u̯esu- 1174)\",\n  \"note\": (\"All three of Nourai's root shapes are real Pokorny headwords and all three are 'good': \"\n           \"IEW 342 'esu-s (: su-) gut, tüchtig' (Gk. ἐüς, Hitt. assus), IEW 1037 'su- wohl, gut als \"\n           \"1. Kompositionsglied' (Skt. su-, Av. hu-, OP u-), IEW 1174 'u̯esu- gut' (Skt. vasu-, Av. vohu-, \"\n           \"OIr. feb < *wesu-ā). Grouping them in one box is not Nourai's invention: Mann (IEC) writes \"\n           \"\\\"esus (əsus, su-) (1) 'good, true'. Cf. su-, uesus\\\", and Wiktionary's *h₁su- says the prefix is \"\n           \"'possibly a metathesis of *h₁wes- \\\"good\\\"' or belongs with *h₁es- 'to be'; Watkins likewise makes \"\n           \"esu- 'an extension of es-'. Whether su-/esu- and wesu- are ultimately one root is still open \"\n           \"(Beekes and Kloekhorst keep *h₁su- and *h₁wesu- apart), so the box is right on the gloss and the \"\n           \"language label, and merely optimistic in merging the three. PART 2 of the chart draws only the \"\n           \"Old Persian prefix u-/uv- and its compounds, which belong to IEW 1037. \"\n           \"KLN:548 does not check out: Klein 1966 p.548 is the entellus–entre- stretch; the Klein entry that \"\n           \"carries exactly this material ('eu-, combining form meaning \\\"good, well\\\" ... OI. vasuh, Avestic \"\n           \"vohu-, Ir. feb (fr. I.-E. *wesw-a), Hitt. ashshush') stands on p.~572.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *h₁su- «خوب، نیک» است که در زبان‌های هندوایرانی به صورت پیشوند \"\n              \"به کار رفته است: سنسکریت su-، اوستایی hu-، پارسی باستان u-/uv-. پوکورنی سه مدخل جداگانه دارد: \"\n              \"esu-s (ص ۳۴۲)، su- (ص ۱۰۳۷) و u̯esu- (ص ۱۱۷۴)؛ نورایی هر سه را در یک جعبه آورده است و این کار \"\n              \"بی‌پشتوانه نیست (مان در فرهنگ تطبیقی خود su- را صورت کوتاه‌شدهٔ esus می‌داند و ویکی‌واژه نیز احتمال \"\n              \"قلب (metathesis) از *h₁wes- را پیش می‌کشد)، اما یکی دانستن قطعی آن‌ها هنوز پذیرفتهٔ همه نیست. \"\n              \"ارجاع POK درست است، ولی ارجاع KLN:548 نادرست است: مدخل مربوط در کلاین (eu-) در صفحهٔ ۵۷۲ است. \"\n              \"کوتاه سخن: ادعای نورایی دربارهٔ ریشه درست است.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"POK:342\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt line 5144 (leaf 355): \\\"Zum obigen vielleicht: esu-s (: SU-) ,gut, tüchtig'. Gr. εὐς, ἠύς ,tüchtig, gut', Adverb eῦ ... hitt. a-aš-šu-uš (assus) ,gut'\\\" — Watkins independently cites the same page: \\\"esu-. Good. Extension of es-. ... [Pok. esu-s 342.]\\\" (AHD_watkins1985.txt line 462).\"},\n    {\"ref\": \"POK:1037\", \"status\": \"supports\",\n     \"note\": \"POK_03.txt line 3889: \\\"su- ,wohl, gut' als 1. Kompositionsglied; su-bhago- ,beglückend'. Ai. su-, av. hu-, apers. u-, ... gr. ὑγιής ,gesund' (*su-gʷiiēs ,wohllebend')\\\"; the OCR carries the printed page marker '1038' a few lines below, so the article does begin on 1037. Watkins: \\\"su-. Well, good. ... [Pok. su- 1037.]\\\"\"},\n    {\"ref\": \"POK:1174\", \"status\": \"supports\",\n     \"note\": \"POK_03.txt line 5956: \\\"uesu- ,gut'. Ai. vásu- ,gut' ... av. vaŋhu-, vohu- ds. ... air. *feb ... aus *uesu-ā\\\"; it sits immediately beside u̯es-r̥ 'Frühjahr', which Watkins cites as [Pok. wes-r 1174] — so p.1174 is right.\"},\n    {\"ref\": \"KLN:548\", \"status\": \"not_found\",\n     \"note\": \"Klein 1966 p.548 (KLN_1966.txt leaf 286, page = 2*(leaf-12)) runs entellus, entelodont, entente, enter-, ... entre- — nothing about 'good'. The entry Nourai means is 'eu-, combining form meaning ‘good, well’. — Fr. Gk. eu ... cogn. either with Hitt. ashshush, ‘good’, or — more probably — with OI. vasuh, Avestic vohu-, ‘good’, Ir. feb (fr. I.-E. *wesw-a)' at leaf 298 ≈ p.572.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 342, 1037, 1174\", \"stance\": \"supports\",\n     \"note\": \"three separate articles, all glossed 'gut': esu-s (: su-), su- 'wohl, gut als 1. Kompositionsglied' with 'ai. su-, av. hu-, apers. u-', and u̯esu- 'gut'. Pokorny adds \\\"su- ist Tiefstufe zu *swe-\\\" (POK_03 line 3893 f.).\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 307 (u̯esu-); WP II 512 for su-/esus\", \"stance\": \"supports\",\n     \"note\": \"WLD_Bd1 line 19664 \\\"uesu- ,,gut“\\\" with running head \\\"uesu- — ues-r, ues-(e)n-\\\"; line 19498 \\\"Über das wahrscheinlich verwandte idg. *uesu- ,,gut“ s. d.\\\" Mann and Pokorny both give WP II 512 for su-/esus.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. esu-, su-\", \"stance\": \"supports\",\n     \"note\": \"\\\"esu-. Good. Extension of es-. Greek eus, good, combining form eu-, well: EU-. [Pok. esu-s 342.]\\\" and \\\"su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gʷia-es- ... [Pok. su- 1037.]\\\" — no separate *wesu- root in Watkins.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.vv. esus (1), su- (2)\", \"stance\": \"supports\",\n     \"note\": \"IEC.txt line 3733: \\\"esus (əsus, su-) (1) 'good, true'. Cf. su-, uesus. Cf. WP II 512; I, 161. Skt. cf. su-, px.; Av. hu-, id.; ... Hitt. assus\\\"; line 17774: \\\"su- (2) 'well'. Aphetic (z-gde) of esus, q.v.\\\" — i.e. Mann groups exactly Nourai's Su / Esu / Wesu.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"hu, u, uv\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Old Persian has an inseparable prefix u- 'good, well', uv- before vowels (uv-aspa- 'having good \"\n                 \"horses'), continuing Proto-Iranian *hu- < PIE *h₁su-; the cognates are Av. hu-, Skt. su-, Gk. \"\n                 \"ὑ- in ὑγιής 'healthy' (*su-gʷi̥iēs 'living well'). Kent p.175 states this in so many words. The \"\n                 \"'hu' of the chart is not an OP spelling — OP cuneiform writes <u->/<uv-> — but it is the standard \"\n                 \"etymological transliteration (h)u-: the Elamite and Akkadian renderings of the Achaemenid names \"\n                 \"(Akk. ḫu-ma-ri-iz-ma-ʼ for Uvārazmiš) show that the initial *h- was still there, and Wiktionary \"\n                 \"accordingly prints the OP name /ʰUvārazmiš/. So hu / u / uv are one prefix, and Nourai's arrow \"\n                 \"from the IE root is right.\"),\n  \"derivation_fa\": (\"در پارسی باستان پیشوند u- (و پیش از واکه uv-) به معنای «خوب، نیک» هست که از ایرانی باستان *hu- \"\n                    \"و آن از هندواروپایی آغازین *h₁su- بازمانده است؛ هم‌ریشه با اوستایی hu- (همان «هو» در هوخشتر و هنر < hu-nara-)، \"\n                    \"سنسکریت su- و یونانی eu-. صورت hu در خط میخی پارسی باستان نوشته نمی‌شود، ولی آوانویسی معیار آن (h)u- است، \"\n                    \"زیرا صورت‌های ایلامی و اکدی همان نام‌ها هـ آغازین را نشان می‌دهند. ادعای نورایی درست است.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [{\"ref\": \"KNT:175\", \"status\": \"supports\", \"note\": KNT_U}],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon, s.v. u- (p.175 region)\", \"stance\": \"supports\", \"note\": KNT_U},\n    {\"src\": \"POK\", \"where\": \"IEW 1037\", \"stance\": \"supports\",\n     \"note\": \"\\\"su- ,wohl, gut' als 1. Kompositionsglied ... Ai. su-, av. hu-, apers. u-\\\" — the three shapes of the chart's node in one line (POK_03.txt line 3889).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. su-\", \"stance\": \"supports\",\n     \"note\": \"\\\"su-. Well, good.\\\" with the compound *su-gʷia-es- that gives Gk. ὑγιής, the same example Kent uses for the OP prefix.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. su- (2)\", \"stance\": \"supports\",\n     \"note\": \"\\\"su- (2) 'well'. ... Av. hu-kərəfš 'shapely'; hu-narō 'virtue'; Per. hunar 'art, science'\\\" — the Iranian prefix with the same value.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Avestan / Old Persian\", \"words\": \"u-vâra-zmi\", \"verdict\": \"disputed\",\n  \"derivation\": (\"The segmentation u- 'good' + vāra- (?) + zmi- 'land' is taken verbatim from Kent: \\\"Uvārazmi- sb. \"\n                 \"'Chorasmia', a province of the Persian Empire ... From u- 'good' + vāra- '?' ... + zmi- ... to zam- \"\n                 \"'land'\\\" — the chart's NOTE 'The meaning of \\\"vāra\\\" is not clear' simply reproduces Kent's question \"\n                 \"mark, and is honest. But this is a 1950 analysis that current Iranian scholarship has abandoned. \"\n                 \"MacKenzie (1983, p.1244), followed by the Berkeley Chorasmian project, reads the OP name \"\n                 \"(h)uvārazmiš as *(h)wāra- 'low' + *zm-, the zero grade of *zam- 'land', i.e. 'lowland' — \"\n                 \"geographically apt for the Amu Darya delta, the lowest part of Central Asia; Bosworth's variant \"\n                 \"takes the first element as xʷar- 'sun', 'land from which the sun rises'. On either modern view \"\n                 \"the first element is xʷār-/xʷar-, not the prefix u-/hu- 'good', and the whole Khwarazm branch of \"\n                 \"this chart (nodes 2-9, hence algorism/algorithm) does not belong under *h₁su- at all. The rest of \"\n                 \"the chain (Khwarazm > al-Khwārizmī > algorismus) is unaffected and correct.\"),\n  \"derivation_fa\": (\"تجزیهٔ u- (خوب) + vāra- (نامعلوم) + zmi- (زمین) عیناً از کنت (۱۹۵۰) گرفته شده و خود کنت هم برای \"\n                    \"جزء دوم علامت پرسش گذاشته است. اما ریشه‌شناسی امروزی این تحلیل را رد می‌کند: مکنزی (۱۹۸۳) جزء نخست را \"\n                    \"*xʷāra- «پست، فرودین» و جزء دوم را *zm- (صورت صفرمرتبهٔ *zam- «زمین») می‌داند، یعنی «سرزمین پست» \"\n                    \"— که با جغرافیای دلتای آمودریا سازگار است؛ بازوورث نیز xʷar- «خورشید» را پیشنهاد کرده است. در هر دو \"\n                    \"دیدگاه جزء نخست پیشوند «هو/او» نیست؛ پس پژوهش امروزی این پیوند را به ریشهٔ *h₁su- رد می‌کند، \"\n                    \"هرچند بقیهٔ زنجیره (خوارزم ← خوارزمی ← algorismus) درست است.\"),\n  \"sources\": [BERK, W_KHW, W_XWR],\n  \"ref_check\": [\n    {\"ref\": \"KNT:177\", \"status\": \"supports\",\n     \"note\": \"KNT.txt line 5212 (Lexicon, the page after the '177' break): \\\"Uvārazmi- sb. 'Chorasmia', a province of the Persian Empire: Elam. ma-ra-iš-mi-iš, Akk. ḫu-ma-ri-iz-ma-ʼ, Gk. Χορασμίη, Av. asf. xʷairizəm. From u- 'good' + vāra- '?' ... + zmi- ... to zam- 'land'.\\\" Kent says exactly what the chart says (the OCR renders his '?' as '0°'); the entry sits on the 177/178 boundary of the printed lexicon.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon s.v. Uvārazmi- (pp.177-178)\", \"stance\": \"supports\",\n     \"note\": \"see ref_check; Kent also lists Uvārazmi- among the u- 'good' compounds in his u- article (p.175).\"},\n    {\"src\": \"BRT\", \"where\": \"grep 'chorasmi|choresmi|airizem|hvairiz' BRT.txt\", \"stance\": \"silent\",\n     \"note\": \"no hit: Bartholomae's Chorasmia entry could not be located in this OCR (the file's Avestan diacritics are badly mangled), so AiW gives neither support nor contradiction here.\"},\n    {\"src\": \"web: Chorasmian Online (UC Berkeley)\", \"where\": \"post of 2021-12-23\", \"stance\": \"contradicts\",\n     \"note\": \"\\\"the first part derived from *hwāra- 'low' (as was already recognized by MacKenzie (1983, p. 1244). The second part could be *zm-, the zero-grade of *zam- 'land'\\\" — i.e. 'lowlands', not 'good land'.\"},\n    {\"src\": \"web: Wikipedia Khwarazm\", \"where\": \"Names and etymology\", \"stance\": \"contradicts\",\n     \"note\": \"\\\"C.E. Bosworth proposed it derived from xwar ('the sun') and zam ('earth') ... An alternative interpretation suggests the Iranian compound means 'lowland', from xwār ('low') and zam ('land')\\\" — neither analysis contains the prefix u-/hu- 'good'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"huvârazmîš, xvarazmîš, xvârizem\", \"verdict\": \"plausible\",\n  \"derivation\": (\"The three forms are the real attested ones: OP nom. sg. Uvārazmiš (<u-v-a-r-z-mi-i-š>, DNa 23, \"\n                 \"DSe 22, DSm 9, XPh 21, beside Uvārazmiy DB 1.16) and Av. xʷāirizəm. Nourai is here copying Mo'in \"\n                 \"word for word: Borhan-e Qate', Mo'in's introduction p.22, prints 'نام خوارزم در اوستا خوارزم \"\n                 \"Xʷārizem و در کتیبه‌های هخامنشی (پارسی باستان) هوارزمیش Huvārazmiš آمده است' — which is where the \"\n                 \"'huvārazmīš / xʷārizem' pair and even the Airyanəm Vaeējā claim come from. The gloss is the weak part: \"\n                 \"the identification of Khwarazm with Airyanəm Vaējah is Markwart's (Mo'in calls it 'قریب به تحقیق'), \"\n                 \"defended later by Henning, but it is a minority position today — most Avestan scholars (Gnoli, Witzel) \"\n                 \"put Airyanəm Vaējah in the east (Helmand/upper Oxus) or treat it as mythical geography. The modern \"\n                 \"equation with Khiva and the Amu Darya is fine as a description of the region.\"),\n  \"derivation_fa\": (\"صورت‌های این گره درست‌اند: پارسی باستان Uvārazmiš در کتیبه‌های داریوش و خشایارشا و اوستایی \"\n                    \"Xʷāirizəm. نورایی این بند را عیناً از مقدمهٔ معین بر برهان قاطع (ص بیست و دو) گرفته است؛ همان‌جا معین به پیروی از \"\n                    \"مارکوارت می‌نویسد «ایران‌ویج (سرزمین اصلی ایرانیان) همان خوارزم است». این یکسان‌انگاری در پژوهش امروز \"\n                    \"اقلیتی است (گنولی و ویتسل ایران‌ویج را در شرق ایران یا جغرافیای اسطوره‌ای می‌دانند). پس: صورت‌ها درست، \"\n                    \"ولی معنای پیشنهادی با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_XWR, W_KHW],\n  \"ref_check\": [\n    {\"ref\": \"BQT:22(Introduction)\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 30 (intro page بیست و دو = 22; calibrated by leaf 40, whose running head reads 'مقدمه سی و دو'): 'خوارزم یا خیوه، سرزمینی است در مجرای سفلی آمودریا ... عقیدهٔ مارکوارت در این باب قریب به تحقیق است که گوید ایران‌ویج Airyanem Vaejo (سرزمین اصلی ایرانیان) موطن اوستا همان خوارزم است ... نام خوارزم در اوستا خوارزم Xʷārizem و در کتیبه‌های هخامنشی (پارسی باستان) هوارزمیش Huvārazmiš آمده است'. This is Nourai's source, verbatim.\"},\n    {\"ref\": \"BQT:781\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 239 (printed ≈ leaf+543 = 782): 'خوارزم: نام شهری است معروف و مشهور از ترکستان' with Mo'in's footnote 6 'خوارزمی: منسوب به خوارزم، زبان خوارزم. رک: ص بیست و دو مقدمه' — which is precisely the cross-reference Nourai's 'BQT:22(Introduction),781' records.\"},\n    {\"ref\": \"MON5:488\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in vol. 5 (اعلام) is not in the local library and vajehyab/abadis carry only the lexicon volumes; the same author's statement is however verifiable in his Borhan introduction (above).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Mo'in's introduction p.22; vol.2 p.~782\", \"stance\": \"supports\", \"note\": \"see ref_check — both the Avestan/OP forms and the Airyanəm Vaējah identification are Mo'in's.\"},\n    {\"src\": \"KNT\", \"where\": \"Lexicon s.v. Uvārazmi-\", \"stance\": \"supports\",\n     \"note\": \"\\\"Uvārazmiy nsf. DB 1.16, DPe 16f; Uvārazmiš DNa 23, DSe 22, DSm 9, XPh 21f\\\" — the attested OP nominative that Nourai writes 'huvârazmîš'.\"},\n    {\"src\": \"web: Wikipedia Khwarazm / Wiktionary خوارزم\", \"where\": \"Names and etymology\", \"stance\": \"supports\",\n     \"note\": \"Avestan 𐧓𐦁𐥭𐥭𐥰𐦨 (Xvairizəm), Old Persian u-v-a-r-z-mi-i-š, Middle Persian ḥʿʿzm /Xwārazm/, New Persian خوارزم — the same chain, with MP as the missing link the chart does not draw.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Persian\",\n  \"words\": \"Xârazm, Khârazm «خوارزم»; Xârazmî «خوارزمی»; Xîveh, Xîvaq «خیوه۱، خیوق»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"خوارزم Xwārazm is the regular New Persian continuation of OP Uvārazmiš through Middle Persian \"\n                 \"ḥʿʿzm /Xwārazm/: the OP initial (h)uv- gives MP/NP xʷā- written خوا- with 'واو معدوله' (Mo'in, \"\n                 \"Farhang, s.v. خو: 'بنابراین خوارزم را خَوارزم به فتح خا و به تصریح واو گویند'), and خوارزمی is the \"\n                 \"ordinary Arabic-Persian nisba in -ī. Borhan-e Qate' has the entry 'خوارزم: نام شهری است معروف \"\n                 \"و مشهور از ترکستان'. The third pair is the soft spot: خیوه/خیوق is not a phonetic development of \"\n                 \"خوارزم but a separate toponym — Borhan (vol.2, p.~808) glosses 'خیوق ... نام ولایتی از ولایات \"\n                 \"(الکای) خوارزم' with Mo'in's footnote 'xiwaq, دائرةالمعارف اسلام', i.e. a district (later the \"\n                 \"khanate's capital) inside Khwarazm, not a synonym of it. Equating the two is the shorthand of \"\n                 \"Klein and the older Europeans ('Khowarizm (the modern Khiva)'), which Nourai copies.\"),\n  \"derivation_fa\": (\"«خوارزم» دنبالهٔ مستقیم پارسی باستان Uvārazmiš است که از راه فارسی میانه Xwārazm به فارسی نو \"\n                    \"رسیده است؛ واو پس از خ همان «واو معدوله» است که معین در فرهنگ خود ذیل «خو» توضیح داده است. \"\n                    \"«خوارزمی» نیز نسبت معمولی با یای نسبت است. اما «خیوه/خیوق» دگرگونی آوایی خوارزم نیست؛ برهان قاطع \"\n                    \"آن را «نام ولایتی از ولایات خوارزم» می‌داند و معین در حاشیه صورت xiwaq را از دائرةالمعارف اسلام نقل \"\n                    \"می‌کند؛ پس یکی گرفتن خیوه و خوارزم ساده‌سازی است. در مجموع ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_XWR, W_KHW],\n  \"ref_check\": [\n    {\"ref\": \"BQT:781\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 239 ≈ p.782: 'خوارزم نام شهری است معروف و مشهور از ترکستان' + footnote 'خوارزمی منسوب بخوارزم'.\"},\n    {\"ref\": \"BQT:805\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 265 ≈ p.808 (±3 by the volume's leaf offset): 'خیوق بکسر اول بر وزن زبیق، نام ولایتی یکی از الکای خوارزم' and 'خیوه رک: خیوق'; Mo'in's footnote 5 gives 'xiwaq' from the Encyclopaedia of Islam. Both of the chart's Persian spellings are there.\"},\n    {\"ref\": \"MON5:488,491\", \"status\": \"not_checked\", \"note\": \"Mo'in vol.5 (اعلام) not available locally or online.\"},\n    {\"ref\": \"KLN:49\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 37 = p.49, s.v. algorism: \\\"Arab. al-Khowarizmi, 'the man of Khowarizm (the modern Khiva)', surname of Abu Jafar Mohammed ibn Musa\\\" — including the Khwarazm = Khiva equation the chart repeats.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"vol.2 pp.~782 (خوارزم) and ~808 (خیوق/خیوه)\", \"stance\": \"partial\",\n     \"note\": \"confirms both headwords but makes Khiva a district of Khwarazm rather than another name for it.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. خو (MON_part1.txt line ~57662)\", \"stance\": \"supports\",\n     \"note\": \"'در قرون اخیر تلفظ این حرف فراموش شد ... بنابراین خوارزم را خَوارزم به فتح خا و به تصریح واو گویند و گاه واو بعد از خ حذف می‌شود مثل خراسان و خرداد' — Mo'in on the خوار- of خوارزم and on why Arabic renders it خَوارزم.\"},\n    {\"src\": \"KLN\", \"where\": \"p.49 s.v. algorism\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n    {\"src\": \"web: Wiktionary خوارزم\", \"where\": \"Etymology\", \"stance\": \"supports\",\n     \"note\": \"\\\"Inherited from Middle Persian ḥʿʿzm (/Xwārazm/), from Old Persian u-v-a-r-z-m-i-i-š (/ʰUvārazmiš/)\\\".\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Arabic\", \"words\": \"Al-Xwârazmî\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Abū Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī (c. 780-850), of the Baghdad Bayt al-Ḥikma, is named \"\n                 \"by the Arabic nisba الخوارزمی 'the one from Khwārizm', with the definite article al- and the \"\n                 \"relative suffix -ī on the Persian toponym — the Persian place-name taken over unchanged, only \"\n                 \"vocalised in the Arabic way (Kh́awārizm, since Arabic has no xʷ). His الجبر والمقابلة and his \"\n                 \"book on Indian reckoning are the texts that carried the decimal numerals westward; it is the \"\n                 \"nisba, not the given name, that became the European word.\"),\n  \"derivation_fa\": (\"ابوجعفر محمد بن موسی خوارزمی (د. حدود ۲۳۲ هـ.ق.)، ریاضی‌دان بیت‌الحکمهٔ بغداد، با نسبت \"\n                    \"«الخوارزمی» شناخته می‌شد؛ عربی نام جای فارسی را بی تغییر گرفته و تنها آن را بر وزن عربی مصوت‌گذاری \"\n                    \"کرده است (خَوارزم، چرا که در عربی واو معدوله نیست). همین «نسبت» است که در اروپا به صورت واژه درآمد، \"\n                    \"نه نام کوچک او. ادعای نورایی درست است.\"),\n  \"sources\": [ETY, FA_ALG],\n  \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\",\n                 \"note\": \"the chart gives no reference for this node; the claim is however covered by KLN:49 and AHD:33 cited on the neighbouring nodes.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p.49 s.v. algorism\", \"stance\": \"supports\",\n     \"note\": \"\\\"Arab. al-Khowarizmi, 'the man of Khowarizm (the modern Khiva), surname of Abu Jafar Mohammed ibn Musa, great mathematician of the 9th cent.'\\\" — Nourai's NOTE is a paraphrase of this sentence.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 890\", \"stance\": \"supports\",\n     \"note\": \"\\\"davon das ar. Adj. ḥuārizmi od. ḫārizmi 'aus Ḩwarizm stammend, der Ḩwarizmier', Beiname des Mathematikers ABŪ ǦAʿFAR MUḤAMMAD IBN MŪSĀ\\\".\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dict. étym. s.v. Algorithme (p.~18)\", \"stance\": \"supports\",\n     \"note\": \"\\\"le nom d'un des plus anciens auteurs de traités d'arithmétique, Abou Dja'far Mohammed ben Mousâ, surnommé al-khowârezmi, dont l'ouvrage a été traduit ou imité en latin dès le commencement du XIIᵉ siècle\\\".\"},\n    {\"src\": \"MON\", \"where\": \"s.v. خو\", \"stance\": \"supports\",\n     \"note\": \"'تازیان نیز این حرف را نداشته و ندارند' — explains the Arabic vocalisation خَوارزم of the Persian name.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Middle Latin\", \"words\": \"algorismus\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"The Latin translations/adaptations of al-Khwārizmī's arithmetic, from the first half of the 12th \"\n                 \"century on (the 'Dixit Algorizmi' version), transliterated the nisba as Algorizmi / Algorismi, and \"\n                 \"the resulting Medieval Latin noun algorismus came to mean the decimal reckoning itself, whence the \"\n                 \"13th-century genre of 'algorismus' textbooks (Sacrobosco, Alexander de Villedieu). Klein calls it \"\n                 \"'ML. algorismus, from the inexact transliteration of Arab. al-Khowarizmi'; Lokotsch adds that the \"\n                 \"by-form algorithmus arose 'mit Anlehnung an gr. ἀριθμός' — a learned folk-etymology that the chart \"\n                 \"does not mention but that explains the -th- of the next node.\"),\n  \"derivation_fa\": (\"ترجمه‌های لاتین رسالهٔ حساب خوارزمی در سدهٔ دوازدهم میلادی نسبت او را Algorizmi/Algorismi \"\n                    \"آوردند و از آنجا واژهٔ لاتینی میانه algorismus به معنای «حساب با ارقام هندی/عربی» ساخته شد. \"\n                    \"کلاین آن را «آوانویسی نادقیق الخوارزمی» می‌خواند و لوکوچ می‌افزاید که صورت algorithmus بر اثر \"\n                    \"ریشه‌شناسی عامیانه و آمیزش با یونانی arithmos «عدد» پدید آمده است. ادعای نورایی درست است.\"),\n  \"sources\": [ETY],\n  \"ref_check\": [\n    {\"ref\": \"AHD:33\", \"status\": \"not_checked\",\n     \"note\": \"AHD:33 is a page of the American Heritage main dictionary (s.v. algorism/algorithm), not of the Indo-European appendix; the only AHD text on disk is Watkins's root list (AHD_watkins1985.txt), which has no such entry.\"},\n    {\"ref\": \"KLN:49\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 37 = p.49: \\\"algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus, from the inexact transliteration of Arab. al-Khowarizmi\\\" — word for word the chart's gloss.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p.49\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 890 (index: algorismus 890, algorithmus 890)\", \"stance\": \"supports\",\n     \"note\": \"\\\"daher wurde lat. algorithmus, algorismus [mit Anlehnung an gr. ἀριθμός] die Bezeichnung für das Rechnen mit ar. Ziffern u. schließlich für Rechnungsverfahren überhaupt\\\".\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. algorism\", \"stance\": \"supports\",\n     \"note\": \"\\\"al'gə-rism, al'gə-rithm, n. [OFr. algorisme; ... L. algorismus, the Arabic system of numbers; from Ar. al-Khowarazmi, a native of Khwarazm (Khiva), an Arabic mathematician of the ninth century]\\\".\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Algorithme\", \"stance\": \"supports\",\n     \"note\": \"\\\"Ces sortes de livres furent désignés sous le nom d'Algorismus. M. Defrémery a raison de dire que cette étymologie est hors de doute depuis les recherches de MM. Reinaud, Chasles et Woepcke\\\".\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"French\", \"words\": \"algorisme, algorithme\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Old French algorisme (13th c., also angorisme) is the regular popular reflex of ML algorismus; the \"\n                 \"modern French algorithme is a learned remodelling under the influence of Greek ἀριθμός 'number' \"\n                 \"(the same contamination already visible in the Latin doublet algorithmus). Devic s.v. Algorithme: \"\n                 \"'Au XIIIᵉ siècle, ce mot signifiait l'arithmétique avec les chiffres arabes; on écrivait algorisme \"\n                 \"et angorisme'; Lammens adds the Iberian offspring (Sp. guarismo, Ptg. algarismo). Both French \"\n                 \"forms the chart prints are therefore real, and the order algorisme > algorithme is right.\"),\n  \"derivation_fa\": (\"فرانسهٔ کهن algorisme (سدهٔ ۱۳م) دنبالهٔ عادی algorismus لاتینی میانه است و صورت امروزی \"\n                    \"algorithme بازسازی عالمانه‌ای است که زیر تأثیر یونانی arithmos «عدد» درست شده است (همان آمیزشی \"\n                    \"که در لاتین algorithmus پدید آورده بود). دویک ذیل Algorithme می‌نویسد در سدهٔ ۱۳م این واژه به \"\n                    \"معنای حساب با ارقام عربی بوده و آن را algorisme و angorisme می‌نوشتند. ادعای نورایی درست است.\"),\n  \"sources\": [ETY],\n  \"ref_check\": [{\"ref\": \"AHD:33\", \"status\": \"not_checked\",\n                 \"note\": \"main-dictionary page of AHD (s.v. algorism), not in the local Watkins-appendix file.\"}],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"Devic s.v. Algorithme\", \"stance\": \"supports\", \"note\": \"see derivation — 'on écrivait algorisme et angorisme; Esp. alguarismo, guarismo, algorithmo; portug. garismo'.\"},\n    {\"src\": \"LAM\", \"where\": \"Lammens, Remarques, s.v. Algorithme\", \"stance\": \"supports\",\n     \"note\": \"\\\"Aux formes romanes citées par M. Devic ajoutez les suivantes: Esp: algurismo, alguarismo, argorismo. Ptg: algarismo, algorismo. Val: algoritme; de alkhawārizmi, Mathématicien arabe\\\".\"},\n    {\"src\": \"LKT\", \"where\": \"no. 890\", \"stance\": \"supports\", \"note\": \"\\\"Hieraus afrz. algorisme, frz. algorithme, it. alguarismo ... engl. algorism, algorithm 'Rechenart'\\\".\"},\n    {\"src\": \"web: Etymonline s.v. algorithm\", \"where\": \"entry\", \"stance\": \"supports\",\n     \"note\": \"\\\"from French algorithme, reshaped under mistaken connection with Greek arithmos 'number' from Old French algorisme 'the Arabic numeral system' (13c.)\\\".\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Persian\", \"words\": \"âlgoritm «آلگوریتم»\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Modern Persian الگوریتم/آلگوریتم is a 20th-century technical loan taken over from French algorithme \"\n                 \"(the usual channel for Persian scientific vocabulary before English became dominant), with French \"\n                 \"final -e dropped and the stress-less vowel written with alef; the commoner spelling today is \"\n                 \"الگوریتم, Nourai's آلگوریتم being the older, more phonetic one. It is thus a round trip: \"\n                 \"Persian خوارزمی > Arabic nisba > Medieval Latin > French > back into Persian as an unrecognisable \"\n                 \"European word, exactly as the chart draws it (French node → Persian node).\"),\n  \"derivation_fa\": (\"«الگوریتم/آلگوریتم» وام‌واژه‌ای است از فرانسهٔ algorithme که در سدهٔ چهاردهم خورشیدی از راه \"\n                    \"زبان علمی فرانسه وارد فارسی شده است؛ این همان «بازگشت» واژه است: خوارزمی فارسی ← نسبت عربی ← \"\n                    \"لاتینی میانه ← فرانسه ← فارسی نو. ویکی‌پدیای فارسی می‌نویسد «واژهٔ الگوریتم اقتباسی از نام همه‌چیزدان \"\n                    \"ایرانی، خوارزمی است». املای رایج امروز «الگوریتم» است و صورت «آلگوریتم» کهنه‌تر است. ادعای نورایی درست است.\"),\n  \"sources\": [FA_ALG],\n  \"ref_check\": [{\"ref\": \"VOP:17\", \"status\": \"not_checked\",\n                 \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (1371) — refs_online.json records that no scan of this book exists anywhere online; not obtainable.\"}],\n  \"consulted\": [\n    {\"src\": \"web: Persian Wikipedia الگوریتم\", \"where\": \"lead / etymology\", \"stance\": \"supports\",\n     \"note\": \"'واژهٔ الگوریتم اقتباسی از نام همه‌چیزدان ایرانی، خوارزمی است' with the chain Algoritmi (12th c.) > Algorismus (13th c.) > Fr. Algorithme > Eng. algorithm.\"},\n    {\"src\": \"MON\", \"where\": \"grep 'الگوریتم|آلگوریتم' MON_part1/2, BQT_v1\", \"stance\": \"silent\",\n     \"note\": \"no hit — the loan is later than (or outside) these dictionaries' European-word coverage; Mo'in's vol.4 (لغات خارجی) is not on disk.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 890\", \"stance\": \"supports\",\n     \"note\": \"documents the French form algorithme that Persian borrowed, and the whole Arabic-to-European route.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"English\", \"words\": \"algorism, algorithm\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"Middle English algorisme (early 13th c., Chaucer's 'augrim stones') from Old French algorisme; the \"\n                 \"form algorithm, with -th- after Greek ἀριθμός, appears in English in the 1690s and only in the 20th \"\n                 \"century takes on the general sense 'a finite procedure of computation'. Klein's entry is the chart's \"\n                 \"wording; Webster and Funk & Wagnalls give the same chain. The chart derives English from French \"\n                 \"rather than straight from Latin, which is right for algorism and effectively right for algorithm.\"),\n  \"derivation_fa\": (\"انگلیسی میانه algorisme را از فرانسهٔ کهن گرفته (سدهٔ ۱۳م میلادی؛ نزد چوسر augrim) و صورت \"\n                    \"algorithm با ث (به قیاس یونانی arithmos) از دههٔ ۱۶۹۰ میلادی دیده می‌شود و معنای امروزین «روش \"\n                    \"گام‌به‌گام محاسبه» را در سدهٔ بیستم گرفته است. کلاین، وبستر و فانک و واگنالز همین زنجیره را \"\n                    \"می‌دهند. ادعای نورایی درست است.\"),\n  \"sources\": [ETY],\n  \"ref_check\": [{\"ref\": \"KLN:49\", \"status\": \"supports\",\n                 \"note\": \"\\\"algorism, n., the Arabic system of numerals. — ME. algorisme, fr. OF. algorisme (F. algorithme), fr. ML. algorismus ...\\\" (KLN_1966.txt leaf 37 = p.49).\"}],\n  \"consulted\": [\n    {\"src\": \"WEB\", \"where\": \"Webster's 2nd, s.v. algorism/algorithm\", \"stance\": \"supports\",\n     \"note\": \"\\\"1. a Latin name for computation, or the decimal system of counting ... 2. the common rules of computation in any branch of numerical analysis; as, the algorism of the differential calculus\\\".\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.vv. algorist, algoristic\", \"stance\": \"supports\",\n     \"note\": \"\\\"algo-ris'tic, a. Of or pertaining to an algorist or algorism\\\" — the word family is in English lexicography from the 19th c.\"},\n    {\"src\": \"web: Etymonline s.v. algorithm\", \"where\": \"entry\", \"stance\": \"supports\",\n     \"note\": \"\\\"algorithm (1690s) 'Arabic system of computation' ... The earlier Middle English form was algorism (early 13c.)\\\".\"},\n    {\"src\": \"KLN\", \"where\": \"p.49\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"Old Persian\",\n  \"words\": \"u-vaxštra; u-xšnav; u-kâra; u-câra; u-tâna; uv-aspa\", \"verdict\": \"confirmed\",\n  \"derivation\": (\"All six are Old Persian compounds of the prefix u-/uv- 'good', every one of them listed under Kent's \"\n                 \"u- article. Kent p.176-177: 'Uvaxštra- sb. \\\"Cyaxares\\\", former King of Media ... From u- \\\"good\\\" + \"\n                 \"vaxštra- \\\"growth\\\" ... to vaxš-, Av. vaxš-, Skt. vakṣ-, Gm. wachsen, NEng. wax: \\\"Having good \"\n                 \"growth\\\"'; 'uxšnav- adj. \\\"well satisfied\\\": from u- \\\"good\\\" + xšnav- \\\"satisfy\\\"'; 'ukāra- adj. \"\n                 \"\\\"having good people or army\\\"'; 'ucāra- adj. \\\"well done, successful\\\", as sb. nt. \\\"good deed\\\": from \"\n                 \"u- + cāra-, to root kar- \\\"do\\\"'; 'uvaspa- adj. \\\"having good horses\\\" ... + aspa- \\\"horse\\\"' (DPd 8, \"\n                 \"DSf 11). Two details are softer than the chart lets on: for Utāna- (Otanes, the conspirator of DB \"\n                 \"4) Kent writes only 'perhaps u- \\\"good\\\" + tāna- to root tan- \\\"stretch, extend\\\"', and the \"\n                 \"'(children)' of Nourai's gloss is his own addition; and for Uvaxštra- Kent notes that Herzfeld \"\n                 \"read it instead as 'having good oversight' (Av. aiwy-āxštar-). The prefix itself is not in doubt \"\n                 \"in any of the six.\"),\n  \"derivation_fa\": (\"هر شش صورت، ترکیب‌های پارسی باستان با پیشوند u-/uv- «نیک»‌اند و کنت همه را ذیل همین \"\n                    \"پیشوند آورده است: uvaxštra- (هوخشتر، «خوب‌بالنده»)، uxšnav- («خشنود»، از ریشهٔ xšnav-)، \"\n                    \"ukāra- («دارای سپاه نیک»)، ucāra- («نیک‌کردار»، از ریشهٔ kar-)، Utāna- (اوتانه) و uvaspa- \"\n                    \"(«دارای اسبان نیک»، در کتیبهٔ DPd و DSf). دو نکته: کنت دربارهٔ Utāna- تنها «شاید» می‌گوید و \"\n                    \"قید «(فرزندان)» افزودهٔ نورایی است؛ و در جزء دوم uvaxštra- هرتسفلد تفسیر دیگری دارد. \"\n                    \"در مجموع ادعای نورایی درست است.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"KNT:175,176,177\", \"status\": \"supports\",\n     \"note\": \"the u- article (p.175) lists uxšnav-, ukāra-, ucāra-, Utāna-, Uvaxštra-, uvaspa- among its compounds; the individual entries follow on pp.175-177 (KNT.txt lines 5158-5208), e.g. \\\"uvaspa- adj. 'having good horses': u- 'good' (§118.IV, §140.IV) + aspa- 'horse'. uvaspā nsf. AmH 6; DPd 8\\\".\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon pp.175-177\", \"stance\": \"supports\", \"note\": \"see ref_check; for Uvaxštra- Kent adds \\\"So Bthl. AiW 1836; but Hz. ApI 209 interprets 'having good oversight'\\\".\"},\n    {\"src\": \"POK\", \"where\": \"IEW 1037\", \"stance\": \"supports\",\n     \"note\": \"\\\"Ai. su-, av. hu-, apers. u-, z. B. in ai. su-drū- ,starkes Holz', su-bhága- ,glücklich'\\\" — the compound type the node illustrates.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. su- (2)\", \"stance\": \"supports\",\n     \"note\": \"gives the parallel Avestan compounds hu-kərəfš 'shapely', hu-narō 'virtue', showing the same prefix productive in Old Iranian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Persian\", \"words\": \"Hovaxšatar «هوخشتر»\", \"verdict\": \"plausible\",\n  \"derivation\": (\"هوخشتر is the name Persian historiography uses for the Median king whom Herodotus calls \"\n                 \"Κυαξάρης (Cyaxares, r. 625-585 BCE); it is not an inherited New Persian word but a modern scholarly \"\n                 \"restitution from the Old Persian form of DB 2.15f, 4.19-22 (Uvaxštrahyā), itself the OP rendering \"\n                 \"of a Median name. The first element hu-/u- 'good' is agreed by everyone. The second is not: Kent \"\n                 \"(after Bartholomae AiW 1836) takes it as vaxštra- 'growth' (→ 'having good growth'), Herzfeld as \"\n                 \"'oversight'; but the Persian form the chart prints, هوخشتر / Hovaxšatar with -xšatar, is the one \"\n                 \"Persian authors read as هو 'good' + خشثره xšaθra- 'rule, kingship' — i.e. 'good king' (so Persian \"\n                 \"Wikipedia s.v. هووخشتره). The arrow from the OP node is right; the segmentation behind Nourai's \"\n                 \"spelling is a different one from the one his source (Kent) gives.\"),\n  \"derivation_fa\": (\"«هوخشتر» نام سومین پادشاه ماد (کیاکسار در هرودوت) است که از روی صورت پارسی باستان \"\n                    \"Uvaxštra- در کتیبهٔ بیستون بازساخته شده؛ واژه‌ای موروثی در فارسی نو نیست بلکه اصطلاح ایران‌شناسی \"\n                    \"است. جزء نخست (هو «نیک») پذیرفتهٔ همه است، اما جزء دوم محل اختلاف است: بارتولومه و کنت \"\n                    \"vaxštra- «بالش، رویش» می‌خوانند، هرتسفلد «نگاهبانی»، و منابع فارسی بیشتر آن را خشثره \"\n                    \"«شهریاری» گرفته‌اند («پادشاه خوب») — و املای نورایی (Hovaxšatar) همین خوانش را می‌رساند نه \"\n                    \"خوانش منبع خودش (کنت). پس با احتیاط پذیرفتنی است.\"),\n  \"sources\": [FA_CYA],\n  \"ref_check\": [\n    {\"ref\": \"KNT:177\", \"status\": \"partial\",\n     \"note\": \"KNT.txt (p.176/177): \\\"Uvaxštra- sb. 'Cyaxares', former King of Media: Elam. ma-ak-iš-tar-ra, Akk. ū-ma-ku-iš-tar, Gk. Κυαξάρης. From u- 'good' + vaxštra- 'growth' ... 'Having good growth'. ... Uvaxštrahyā DB 4.19, 22\\\" — Kent supports the identification and the prefix, but he analyses the second element as vaxštra- 'growth', not as xšaθra- 'rule', which is what Nourai's Persian spelling هوخشتر implies.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon s.v. Uvaxštra-\", \"stance\": \"partial\", \"note\": \"see ref_check; Kent explicitly records the rival interpretation of Herzfeld (ApI 209).\"},\n    {\"src\": \"web: Persian Wikipedia هووخشتره\", \"where\": \"name section\", \"stance\": \"partial\",\n     \"note\": \"'پارسی باستان: ʰUvaxštra ... اکدی: Ū-ak-sa-tar ... یونانی: Κυαξάρης' and 'برخی هوخشتره را ترکیبی از دو واژه پارسی باستان هو به‌معنای خوب و خشثره به‌معنای شهریار است' — the Persian form and the rival second element.\"},\n    {\"src\": \"BRT\", \"where\": \"grep 'huvaxš|Kyaxar' BRT.txt\", \"stance\": \"silent\",\n     \"note\": \"no usable hit in this OCR; Kent's citation of AiW 1836 is the standard reference for Bartholomae's view.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"Old Persian\",\n  \"words\": \"u-frašta; u-barta; u-martiya; ŭv-nara; u-ratha; uv-asštika\", \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"uv-asštika\",\n  \"correct_form\": \"uv-ṛštika (Kent uvaṛštika-)\",\n  \"derivation\": (\"Five of the six are exactly Kent's: 'ufraša- ufrasta- adj. \\\"well punished\\\": u- \\\"well\\\" + pte. \"\n                 \"frašta- or frasta- \\\"questioned, investigated\\\" to root fraθ-: pIE *su-prekto-' (DB 1.22, 4.66f); \"\n                 \"'ubarta- adj. \\\"well-borne, lifted, esteemed\\\": u- \\\"well\\\" + barta- \\\"borne\\\", pte. to bar- \\\"bear\\\", \"\n                 \"pIE *su-bhṛto-' (DB 1.21f); 'umartiya- adj. \\\"containing good men\\\": u- \\\"good\\\" + martiya- \\\"man\\\"' \"\n                 \"(AmH 6, DPd 8f — Nourai's gloss is Kent's, verbatim); 'ūvnara- sb. \\\"skill, accomplishment\\\": adj. \"\n                 \"formation to pAr. *su- \\\"good\\\" + *nar- \\\"man\\\" = \\\"having the good quality of a man\\\", Av. hunara- \"\n                 \"\\\"ability, skill\\\", with vriddhi of the first vowel' (DNb 45, 51 — here Nourai's 'having good men' \"\n                 \"is a mis-gloss: the word means 'skill, prowess', and it is the ancestor of NP هنر); uraθa- \"\n                 \"'having good chariots' is implied by Kent's uraθara- 'having good charioteers': deriv. of uraθa-' \"\n                 \"and is listed in the u- article. The sixth, printed 'uv-asštika', is not a possible Old Persian \"\n                 \"shape: Kent's word is uvaṛštika- sb. 'good spearman': u- 'good' + ṛštika- 'spearman' (DNb 44), \"\n                 \"from ṛšti- 'spear'. The printed page (pdf 485, book 455) really does read 'uv-asštika', so this is \"\n                 \"Nourai's own misprint/mis-transliteration of the vocalic ṛ, not a scanning error — the extraction \"\n                 \"is faithful.\"),\n  \"derivation_fa\": (\"پنج صورت نخست عیناً از کنت است: ufrasta- «نیک بازخواست‌شده» (< *su-prekto-)، ubarta- \"\n                    \"«نیک‌برده، گرامی» (< *su-bhṛto-)، umartiya- «دارای مردمان نیک»، ūvnara- «هنر، توانایی» \"\n                    \"(اوستایی hunara-، نیای «هنر» فارسی — معنایی که نورایی داده دقیق نیست) و uraθa- «دارای گردونهٔ نیک». \"\n                    \"اما صورت ششم که در کتاب «uv-asštika» چاپ شده در پارسی باستان ممکن نیست؛ صورت درست \"\n                    \"uvaṛštika- «نیزه‌ور نیک» (از ṛšti- «نیزه»، کتیبهٔ DNb 44) است. تصویر صفحهٔ چاپی (ص ۴۵۵ کتاب) \"\n                    \"همین صورت نادرست را دارد؛ پس خطای چاپی کتاب است و نه خطای خوانش اسکن.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"KNT:175,176,177\", \"status\": \"supports\",\n     \"note\": \"KNT.txt lines 5189-5197 (p.176/177): ufraša-/ufrasta-, ubarta-, umartiya-, uraθara- (deriv. of uraθa-), and line 5158 lists uraθa-, ūvnara-, uvaṛštika- among the u- compounds; the uvaṛštika- entry itself (p.177/178) reads \\\"uvaṛštika- sb. 'good spearman': u- 'good' + ṛštika- 'spearman' (§126). uvaṛštika nsm. DNb 44.\\\" Kent supports every arrow; only Nourai's spelling of the last word is wrong.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Lexicon pp.175-178\", \"stance\": \"supports\", \"note\": \"see ref_check; also \\\"ūvnara- sb. 'skill, accomplishment' ... = 'having the good quality of a man', Av. hunara- 'ability, skill'\\\".\"},\n    {\"src\": \"POK\", \"where\": \"IEW 1037\", \"stance\": \"supports\",\n     \"note\": \"Pokorny's su- article gives the same compound type with participles (ai. su-kr̥ta-, av. hu-...), matching u-barta-/u-frašta- < *su-bhṛto-, *su-prek-to-.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. su- (2)\", \"stance\": \"supports\",\n     \"note\": \"\\\"Av. hu-narō 'virtue'; Per. hunar 'art, science' (LW in Arm. hnark)\\\" — the Iranian cognate of ūvnara-, confirming that the word means 'skill', not 'having good men'.\"},\n    {\"src\": \"BOOK (printed page)\", \"where\": \"pdf page 485 = book p.455, bottom-left box\", \"stance\": \"supports\",\n     \"note\": \"the page image (copied to data/verification/sources/refs/ocr/BOOK/485.png) shows 'uv-asštika : good spearmen' exactly as the JSON has it — the extraction is faithful and the odd form is the book's.\"}\n  ]\n})\n\ndoc = {\n  \"pdf_page\": 485,\n  \"book_page\": 455,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-485.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-14T03:28:59.098Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/draft-485.py (file state is current in your context — no need to Read it back)
```


## [2026-09-14T03:29:03.232Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/draft-485.py && python3 -m json.tool data/verification/page-485.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 485",
 "description": "Generate and validate page-485.json"
}
```


### [2026-09-14T03:29:04.501Z] TOOL RESULT

```
written
JSON OK
nodes verified: 12/12
node verdicts: {'confirmed': 7, 'disputed': 1, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 6, 'partial': 1}
books consulted: {'supports': 36, 'silent': 3, 'contradicts': 2, 'partial': 3} | by book: {'KNT': 6, 'KLN': 4, 'LKT': 4, 'POK': 3, 'IEC': 3, 'MON': 3, 'DEV': 3, 'BRT': 2, 'BQT': 2, 'WEB': 2, 'web: Etymonline s.v. algorithm': 2, 'AHD': 1, 'web: Chorasmian Online (UC Berkeley)': 1, 'web: Wikipedia Khwarazm': 1, 'web: Wikipedia Khwarazm / Wiktionary خوارزم': 1, 'web: Wiktionary خوارزم': 1, 'LAM': 1, 'web: Persian Wikipedia الگوریتم': 1, 'FSD': 1, 'web: Persian Wikipedia هووخشتره': 1, 'BOOK (printed page)': 1}
```


## [2026-09-14T03:29:11.401Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io,re\np='data/verification/page-485.json'\ns=open(p,encoding='utf-8').read()\nbad=[l for l in s.split('\\n') if '𐧓' in l]\nprint(bad)\ns=s.replace(\"Avestan 𐧓𐦁𐥭𐥭𐥰𐦨 (Xvairizəm)\",\"Avestan Xᵛairizəm\")\nopen(p,'w',encoding='utf-8').write(s)\njson.load(open(p,encoding='utf-8'))\nprint(\"ok\")\nEOF\npython3 tools/verify_check.py 485 | tail -4",
 "description": "Fix placeholder Avestan glyphs"
}
```


### [2026-09-14T03:29:12.577Z] TOOL RESULT

```
['              "note": "Avestan 𐧓𐦁\U0001096d\U0001096d\U00010970𐦨 (Xvairizəm), Old Persian u-v-a-r-z-mi-i-š, Middle Persian ḥʿʿzm /Xwārazm/, New Persian خوارزم — the same chain, with MP as the missing link the chart does not draw."']
ok
node verdicts: {'confirmed': 7, 'disputed': 1, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 6, 'partial': 1}
books consulted: {'supports': 36, 'silent': 3, 'contradicts': 2, 'partial': 3} | by book: {'KNT': 6, 'KLN': 4, 'LKT': 4, 'POK': 3, 'IEC': 3, 'MON': 3, 'DEV': 3, 'BRT': 2, 'BQT': 2, 'WEB': 2, 'web: Etymonline s.v. algorithm': 2, 'AHD': 1, 'web: Chorasmian Online (UC Berkeley)': 1, 'web: Wikipedia Khwarazm': 1, 'web: Wikipedia Khwarazm / Wiktionary خوارزم': 1, 'web: Wiktionary خوارزم': 1, 'LAM': 1, 'web: Persian Wikipedia الگوریتم': 1, 'FSD': 1, 'web: Persian Wikipedia هووخشتره': 1, 'BOOK (printed page)': 1}
```


## [2026-09-14T03:29:29.463Z] AGENT

Page 485 (book p. 455) verified — `data/verification/page-485.json` written; `verify_check.py 485` reports 12/12 nodes, **0 PROBLEM lines**.

Counts: root `confirmed` 1 · nodes: 7 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 11 supports, 1 partial, 6 not_checked (AHD:33 = main-dictionary page, only the Watkins appendix is on disk; MON vol. 5 اعلام and VOP have no scan anywhere; node #5 carries no ref).

- **disputed — #2 `u-vâra-zmi` (Khwarazm)**: Nourai reproduces Kent 1950 exactly (`u-` 'good' + `vāra-` '?' + `zmi-` 'land', including Kent's own question mark), but MacKenzie 1983 p.1244 — followed by the Berkeley Chorasmian project — reads OP (h)uvārazmiš as *xʷāra- 'low' + *zm- 'land' ("lowland"); Bosworth reads xʷar- 'sun'. On either modern view the name contains no prefix hu-/u- 'good', so the whole Khwarazm→algorithm branch does not belong under *h₁su-. The chain itself (Khwarazm > al-Khwārizmī > algorismus > algorithme) is correct.
- **transcription_suspect — #12 `uv-asštika`**: `error_in: "book"`. The printed page really prints "uv-asštika" (page PNG saved to `data/verification/sources/refs/ocr/BOOK/485.png`); Kent's word is `uvaṛštika-` 'good spearman' (u- + ṛštika-, DNb 44). Nourai's misprint of vocalic ṛ, not an extraction error.
- plausible: #3 (forms right, but "Airyanem Vaejô = Khwarazm" is Markwart's minority view, taken straight from Mo'in's Borhan introduction p. 22), #4 (خیوه/خیوق is a district inside Khwarazm per Borhan, not a phonetic development of خوارزم), #11 (Persian هوخشتر is fine, but its -خشتر implies xšaθra- 'rule', whereas Kent — Nourai's own cited ref — analyses vaxštra- 'growth').

Also worth the owner's attention (not extraction errors): **KLN:548 on the root box is wrong** — Klein 1966 p. 548 is the *entellus–entre-* stretch; the entry that carries this material (`eu-` 'good, well', citing OI vasuḥ, Av. vohu-, Ir. feb < *wesw-a, Hitt. aššuš) is at p. ~572. POK:342/1037/1174 all check out verbatim.

No extraction errors found: the JSON matches the printed page throughout (the only thing the extraction omits is an empty box drawn beside node #12).
