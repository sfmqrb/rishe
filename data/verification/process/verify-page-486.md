# Verification process log — verify-page-486


## [2026-09-14T03:08:26.848Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 486 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-486.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-486.json. Write /home/sfmqrb/git/rishe/data/verification/page-486.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 486` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:27.766Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:28.487Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:28.521Z] TOOL RESULT

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


## [2026-09-14T03:08:29.051Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-486.txt"
}
```


### [2026-09-14T03:08:29.106Z] TOOL RESULT

```
1	=== PDF page 486 (book page 456) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Su 1, Esu, Wesu : well, good  (refs POK:342,1037,1174; KLN:548)  PART 3
4	#1 (parent #0) [Avestan] refs=POK:1174 | vohu, vahu : good ; vahya, vahištô
5	  #2 (parent #1) [Persian] refs=BRT:1405; BQT:322 | beh «به (بهتر ، بهترین)» : good | extra: بهداشت ، بهبود ، بهداری ، بهرخ ، بهنام ، بهداد ، بهروز ، بهراد ، بهزاد
6	#3 (parent #0) [Avestan] refs=SYN:1176; KLN:169, 401 | vahu-man : well mannered ☞Men 1 ; vah-išta : best (place), heaven ☞Isto ; vau-misa : ?
7	  #4 (parent #3) [Persian] refs=BQT:101,326,328,1819; MON:327; ZMA:19 | Bahman «بهمن» : "well mannered" ; behešt «بهشت» : "best" ; goštây «گشتای» : "best", heaven
8	#5 (parent #0) [Avestan] refs=SYN:1176; KLN:169, 401 | aša-vahišta, artha-vahišta : best justice ☞Ar ; dâraya-vauš, dârayat-vahu : he holds goodness ☞Dher 1
9	  #6 (parent #5) [Persian] refs=BQT:101,326,328,1819; MON:327; ZMA:19 | Ordîbehešt «اردیبهشت» : "best justice" ; Dârîuš «داریوش» : "he holds goodness"
10	#7 (parent #0) [Greek] refs=AHD | hu, eus : good
11	  #8 (parent #7) [Greek] refs=KLN:548,549; AHD | eu-kaliptos : well covered (flowers) ☞Kel 2 ; eu-klidos : well famed, (a 300 BC. mathematician) ; ev-angelion : good news (Bible) ☞Agaru ; eu-genos : well born ☞Gene 1 ; hu-gies : living in good health ☞Gwei
12	    #9 (parent #8) [Persian] refs=MON:404; MON5:165,190 | okâlîptus «اوکالیپتوس» : a type of plant ; Oqlîdos «اقلیدس» : "famous" ; Angelyŭn «انگلیون (انجیل)» : Bible
13	    #10 (parent #8) [English] refs=AHD | eucalyptus, Euclid, Evangelical, Eugene, hygiene
14	#11 (parent #0) [Sanskrit] refs=AHD:1298 | su : good ; su-asti, svasti : well being, good luck ☞Es 2
15	  #12 (parent #11) [English] refs=AHD:1298 | swastica, swastika : an ancient religious symbol adopted in 1935 as an emblem of Nazi Germany
16	
```


## [2026-09-14T03:08:32.005Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-486.json | head -200",
 "description": "Read source JSON page 486"
}
```


### [2026-09-14T03:08:32.064Z] TOOL RESULT

```
{
  "pdf_page": 486,
  "book_page": 456,
  "entries": [
    {
      "root": {
        "name": "Su 1, Esu, Wesu",
        "lang": "Indo-European",
        "refs": "POK:342,1037,1174; KLN:548",
        "gloss": "well, good"
      },
      "part": 3,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1174",
          "words": [
            {
              "translit": "vohu, vahu",
              "gloss": "good",
              "script": null
            },
            {
              "translit": "vahya, vahištô",
              "gloss": null,
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
          "refs": "BRT:1405; BQT:322",
          "words": [
            {
              "translit": "beh",
              "gloss": "good",
              "script": "به (بهتر ، بهترین)"
            }
          ],
          "script_extra": "بهداشت ، بهبود ، بهداری ، بهرخ ، بهنام ، بهداد ، بهروز ، بهراد ، بهزاد",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:1176; KLN:169, 401",
          "words": [
            {
              "translit": "vahu-man",
              "gloss": "well mannered",
              "script": null,
              "see": [
                "Men 1"
              ]
            },
            {
              "translit": "vah-išta",
              "gloss": "best (place), heaven",
              "script": null,
              "see": [
                "Isto"
              ]
            },
            {
              "translit": "vau-misa",
              "gloss": "?",
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
          "refs": "BQT:101,326,328,1819; MON:327; ZMA:19",
          "words": [
            {
              "translit": "Bahman",
              "gloss": "\"well mannered\"",
              "script": "بهمن"
            },
            {
              "translit": "behešt",
              "gloss": "\"best\"",
              "script": "بهشت"
            },
            {
              "translit": "goštây",
              "gloss": "\"best\", heaven",
              "script": "گشتای"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "زانکه گشتای خوب کاران راست - جمله عقبیٰ حلال خوارانست",
            "poet": "Sanâî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:1176; KLN:169, 401",
          "words": [
            {
              "translit": "aša-vahišta, artha-vahišta",
              "gloss": "best justice",
              "script": null,
              "see": [
                "Ar"
              ]
            },
            {
              "translit": "dâraya-vauš, dârayat-vahu",
              "gloss": "he holds goodness",
              "script": null,
              "see": [
                "Dher 1"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:101,326,328,1819; MON:327; ZMA:19",
          "words": [
            {
              "translit": "Ordîbehešt",
              "gloss": "\"best justice\"",
              "script": "اردیبهشت"
            },
            {
              "translit": "Dârîuš",
              "gloss": "\"he holds goodness\"",
              "script": "داریوش"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "hu, eus",
              "gloss": "good",
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
          "lang": "Greek",
          "refs": "KLN:548,549; AHD",
          "words": [
            {
              "translit": "eu-kaliptos",
              "gloss": "well covered (flowers)",
              "script": null,
              "see": [
                "Kel 2"
              ]
            },
            {
              "translit": "eu-klidos",
              "gloss": "well famed, (a 300 BC. mathematician)",
              "script": null
            },
            {
              "translit": "ev-angelion",
              "gloss": "good news (Bible)",
              "script": null,
              "see": [
                "Agaru"
```


## [2026-09-14T03:08:32.711Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:32.773Z] TOOL RESULT

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


## [2026-09-14T03:08:35.944Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-486.json'))\nprint(json.dumps(d['entries'][0]['nodes'][7:], ensure_ascii=False, indent=1))\nprint('num entries', len(d['entries']))\n\"",
 "description": "Read rest of JSON"
}
```


### [2026-09-14T03:08:36.998Z] TOOL RESULT

```
[
 {
  "id": 8,
  "parent": 7,
  "lang": "Greek",
  "refs": "KLN:548,549; AHD",
  "words": [
   {
    "translit": "eu-kaliptos",
    "gloss": "well covered (flowers)",
    "script": null,
    "see": [
     "Kel 2"
    ]
   },
   {
    "translit": "eu-klidos",
    "gloss": "well famed, (a 300 BC. mathematician)",
    "script": null
   },
   {
    "translit": "ev-angelion",
    "gloss": "good news (Bible)",
    "script": null,
    "see": [
     "Agaru"
    ]
   },
   {
    "translit": "eu-genos",
    "gloss": "well born",
    "script": null,
    "see": [
     "Gene 1"
    ]
   },
   {
    "translit": "hu-gies",
    "gloss": "living in good health",
    "script": null,
    "see": [
     "Gwei"
    ]
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 9,
  "parent": 8,
  "lang": "Persian",
  "refs": "MON:404; MON5:165,190",
  "words": [
   {
    "translit": "okâlîptus",
    "gloss": "a type of plant",
    "script": "اوکالیپتوس"
   },
   {
    "translit": "Oqlîdos",
    "gloss": "\"famous\"",
    "script": "اقلیدس"
   },
   {
    "translit": "Angelyŭn",
    "gloss": "Bible",
    "script": "انگلیون (انجیل)"
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": {
   "text": "ولی خط مرا افزون ، کرم کن تاکنم موزون - کلامی همچو انگلیون، به لحنی همچو یوحنّا",
   "poet": "Sohbat Lârî"
  }
 },
 {
  "id": 10,
  "parent": 8,
  "lang": "English",
  "refs": "AHD",
  "words": [
   {
    "translit": "eucalyptus, Euclid, Evangelical, Eugene, hygiene",
    "gloss": null,
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 11,
  "parent": 0,
  "lang": "Sanskrit",
  "refs": "AHD:1298",
  "words": [
   {
    "translit": "su",
    "gloss": "good",
    "script": null
   },
   {
    "translit": "su-asti, svasti",
    "gloss": "well being, good luck",
    "script": null,
    "see": [
     "Es 2"
    ]
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 },
 {
  "id": 12,
  "parent": 11,
  "lang": "English",
  "refs": "AHD:1298",
  "words": [
   {
    "translit": "swastica, swastika",
    "gloss": "an ancient religious symbol adopted in 1935 as an emblem of Nazi Germany",
    "script": null
   }
  ],
  "script_extra": null,
  "note": null,
  "quote": null
 }
]
num entries 1
```


## [2026-09-14T03:08:37.536Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BRT','BQT','MON','SYN','AHD','ZMA']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T03:08:38.672Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}
```


## [2026-09-14T03:08:59.573Z] AGENT

Now let me research. First, the local reference greps.


## [2026-09-14T03:09:02.632Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 1174 area (u̯esu-) ===\"\ngrep -n \"u̯esu-\\|vesu-\\|u̯esu\" POK_full.txt | head -20\necho \"=== POK esu- ===\"\ngrep -n \"^esu-\\|esu-, su-\\|esu-:\" POK_full.txt | head -20\necho \"=== POK su- 1037 ===\"\ngrep -n \"su-, su̯o-\\|su- 'gut'\\|su-, sū-\" POK_full.txt | head -20",
 "description": "Grep Pokorny for esu-/su-/wesu-"
}
```


### [2026-09-14T03:09:02.725Z] TOOL RESULT

```
=== POK 1174 area (u̯esu-) ===
=== POK esu- ===
51768:esu-c' he, she, it, the one mentioned '; Oscan /di-k, Umbrian ere-k' he, she, it, the one 
=== POK su- 1037 ===
```


## [2026-09-14T03:09:04.402Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins esu/wesu/su ===\"\ngrep -n -i \"esu-\\b\\|wesu-\\|^su-\\|swastika\\|eucalypt\\|hygiene\\|Euclid\" AHD_watkins1985.txt | head -40",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-14T03:09:04.500Z] TOOL RESULT

```
=== AHD watkins esu/wesu/su ===
460:es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
462:esu-. Good. Extension of es-. Greek ews, good, combining form eu-, well: EU-. [Pok. esu-s 342.]
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
1033:su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gia-es-, “living in good condition” (see g"ei-). [Pok. su- 1037.]
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
```


## [2026-09-14T03:09:11.913Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK vohu/vahu ===\"\ngrep -n \"vohu-\\|vanhu\\|vaŋhu\\|u̯esu\" POK_full.txt | head -20\necho \"--- grep esu-s ---\"\ngrep -n \"esu-s\\|esu-s, su-s\\|Pok. esu\" POK_full.txt | head\necho \"--- files ---\"\nls POK*",
 "description": "Grep Pokorny variants"
}
```


### [2026-09-14T03:09:12.005Z] TOOL RESULT

```
=== POK vohu/vahu ===
--- grep esu-s ---
28606:Root / lemma: esu-s{\ su-) 
28773:See also: esu-s 
--- files ---
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
```


## [2026-09-14T03:09:13.503Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT vohu ===\"\ngrep -n \"vohu-\\|vahyah\\|vahišta\\|vahista\" BRT.txt | head -30",
 "description": "Grep Bartholomae for vohu"
}
```


### [2026-09-14T03:09:13.566Z] TOOL RESULT

```
=== BRT vohu ===
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
4153:künftige  (jenseitige)  Leben':  disyäl  aAmai naire  oval  mlzd>m  parS.asn3i  °fguhe  vazd- fary  vahistahe  omAsusV. p. 44;  ij.8,  Y.55. a,  A.3.7.  d)  s.  zu  A  1  d.  3)  mit  a) vaAista-  Adj.,  b)  acisla-  Adj.;  a)  'das  beste Sein,  Dasein,  Leben;  Ort  des  besten  Daseins, Paiadies':  vahisfym  'hüm  asaonam  raoca- wAbb  (Stverz.)  vIspB.ci^iJ^rjm'^.g.iii  usw.; S./.a?;  —  nöithl. .  bi-at. .  vaAi/tJ  '»Aus ySmanayat  ahurahe  masdä  oval  vispanqm *aastpm  (sd.)  .  .  yat  srrfoi  daoiarihum P.  40, ;  Y,  (to.  1 1 ;  —  as^m  yS  ahurS .  .  aoi urune  uri'äsma  (sd.)  dalsayeni  vakUtimca 'hüm  P.  3S;  V. /<?.  2  9 ;  —  vazdvar»  vahisiahe 'ai^is  V.  5. 44;  —  vahistajtSs>m  (sd.) TohUtahe  'riASusV.  1S.6;  —  tarS p^r^tümcit hl  urvänmt  vahisl^m  'ham  fraparaymi  .  . it  vahistät  'tihapt  Y.  if),6;  7;  —  i'lsp^m asmanpm  vahtst^m  3  °hüm  baraiti'S.24; V.7.S2,  '^f^. 3.1"^;— vahistahe  'vASu^ vahistqm  ayanqm  yazamatde  Vr.  7. 2 ;  — yatJrS  paurrd  usshistaiti  paräiti  vahistahe •w>i7»/V.;Ä26;5.6i,Y.7/.i6,YLy.i34. P. 4:9;  —  vahislai  •r^heYyi.33;  —  ia^ä 'uhSuS  vaAistahyS  paourvJm  ku%S  (sd.) Y.  44. 3.  b)  'das  schlechteste  Sein,  Da- sein, Leben;  Ort  des  schlechtesten  Seins, HöUe':  vTspa  humaia  ..  vaAistpm*°tAlim"'' *asaiti  vispa  dusmala  acisl^m  *'ijhüm"^ *asaüt  FrW.  3. 2 ;  — ya^ääl  anhat  apsniim (sd.)  '»Aus  aaslS  ärygt'atqm  at  asäum vakistim  manö  Y.30. 4 ;  —  avi  lim  spayüt. . t)mS  .  .  äca  aastpm  äla  'hüm  ä  V.J. 35;
4842:dayil(sd.)  SiSvä  marftaHbyU  Y.2g.'];  —  «j.  ayaptö.dä't^ma- Adj. 'der  am  meisten 34.2  (^adhanä); — ydha  ta  r..»(5><fÄriiSi 'Almosen  gibt',  mit  Dat.:  ^Jt  ^awÄiw  «a«ij'^ .  .  yä  voha  y.3<).  4;  35. 3  (vahista).  S.  \  asavabyS  'masca  (statt  NP.)  asp»rjzö.dät?- noch  r,  (/.  masca  P.  4Q.
6068:cistfm  'sa  (Instr.)  manta..  ahurSX.^i.  läj  fravasays..  barPsnUsca  'saht yat  vahistahe
6072:^aoi^anäil  hizvascä  (sd.)  'sahyä  nqsvä  i  vaahJus  'sähe  b/njä  dalnayä  vaahuya /a^tf  Y.5/.  13*'.  p)  Abl.mitÄa<5i 'demJY. ,35.  i;  f5. 1,  6'2,  lo,  A.J.4;  —  'sähe heiligen,  göttlichen  Recht  gemäss,  ent-  { vahistahe  *6fn)ja  F.  48.  y)  GS.  mit sprechend'  (s.Iabe):  nnii  alr>a  ahB(s&.)  ratav  (sd-, auchfdSt):  aäbyB  rattifys ySt vistö  'sältU  hacä  Y.  25.  6;  27.  13,  38.  i ; !  h^titi  'sähe  ratavS  %rayatea  %risqsca  ysi
6073:—  yS  möi  'säi  haülm  (sd.)  hatä  var9saiti\hnii  'sähe  yat  vahistahe  (näml.  ratavö) Y.  46.  19;  —  spinia  mainyB  vahiiiäcä  \  mazds.frasästa  .  .  Y.  7. 10;  usw.  0)  GS. manatjhä  'säl  haiä  lyaohanäcä  valaahälä  ,  mit  gai'^ä-  (sd-,  auch  fdSt)'*:  'sähe  gatia ahmäi  dqit  .  .  mazda  "für  den  heiligen  |  Y.  ^.  3 ;  usw.  e)  AbL  mit  haca  dnw. Geist  und  für  das  nach  dem  göttlichen!  2  a  ß,  mit  vahista-,  yazatoHbyB  . .  y5i Recht  beste  Denken,  Handeln  und  Reden  I  h^nii  yasnyäca  vahmyäca  'sül  haca  yat wird  uns   -"  Y,  47.  i.         b)  im  jAw.:  1  vahiltät  Y,  1. 19;  77.  10,  V.  j.  2,  Yt  8. 15,
6075:—  h3  dd'iS  'Aw  upaj-aooayeite  (sd.)  yd  xsa'^fjm/a  Y.  2<?,  1 1 ;  —  vohü  iwil drvaite  *daöiliti  P.  50;  —  vistäsps  'sähe  manauha  rcha  'iwä  'sä  patrT.jasSmaiäg hamayä  iaisfmnS  (sd.)  Yt /p.  93;  —  i-Jj- ■  Y.  j6'.  4;  —  at  ySng  'säatca  vöistä  vat*- taspahe  .  .  yS  .  .  'ssi  ravB  yaisa  (sd.)  Yt  hSu^lä  manauhs  pr^^iuSng  (sd.)  Y.  28. 10; '.?-99i99i — yd 'saht  cintnaiastsmS  atihat  \ —  'sä  (Instr.)  vS  anyd  ainim  (sd.) P.  4^;  —  frsaaiti  's'pm  P.  24;  Yt  6.  i,\vJfltighatü  Y.5J.  5;  —  ^?  -  -  dayat  .  . Vyt  ;5; —  'Sake  datsis  vahistahe  F.  4  c;  vahista    astm    (sd.)    "säi    vohs    xsä^r^m
6083:tl  cü  asra^fyanatn  tanunqm  'iahe .  .*vToiliti P-'i"**;  —  ndit..  "iahe  nöii  asayä  fräSmti (sd)  P.4J;  —  nöit  he  gäul  bvcU  nßit  'um oMt  "raola  ndit  vahUtö  ankui  Y.40;  — ahuräi  masdai  . .  yaihe  gäus  yetihe  °hm ye^ke  raolh  Y.i2.  i;  — ■  ä  vahiliaf  atfhaot d  vahiitj/  -iat  ä  vahistaiibyö  raolsbyS  Y, /p.  6;  —  sara^uHrahe . .  paoiryäi  hanka- nuie  gqmca  '/pmca  Yl  13. 88;  —  vahilbm 'snn  .  .  vaMitqm  Jstlm  (sd.)  yazammäe yqm  'Iahe  vahistahe  Vr.  2j.  1;  —  ya^aea ttajenie  asaom  'sim  HnasH  (sd.)  V.  20.  3; f^K  Anhang  zu  II  und  HI.  Ein  be- abdchtigtes  Spiel  mit  den  Bedeutungen leigt:  '!»n  vohB  vahisttm  astt  usta  astl «Al  ahmai  hyat  °iai  vahiMi  'hm  "A/a (Bcd.  n,  III)  ist  das  beste  Gut;  nach Wunsch  wird  es,  nach  Wunsch  uns  zu  teil, das  Asa  (Bed.  III)  fUr  das  beste  A/a (BeAn)"Y.27.i4-'').  A)  als  Gottheit {A»ui'a  Sfijnta*i).  i)  im  gAw.:  '&m  .. vahiibm  . .  hyai  srazll?m  kyat  sptntim awuirm  Y.^-j.^;  —  aää  (sd.)  tasä  gSus^ P^nsal  *hm  . .  ahmai  'lä  (als  Subj.)3> paiajnravat    Y.  29.  af;    —   yä    töi    '.
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pairljasäi  .  .  maibyO  dävBi akvh..  Jj-iT/t/J  (sd.)  'iilihacaY.28.2;sj.i; —  yahä  'sät  hacä  gqm  vJäal  (sd.)  västryS Y.5:.5;  43.14;  —  a/M  ahmai  mazda  'iä a»haüT..  ys..  "und  dem  o  M.,  wird  es (das  Rind)  durch  A.  zu  teil  werden . ., der  .  ."  Y.50.  3;  —  yehya  mUi  'iät  haia vahistsm  . .  valdä  (sd.)  mazdä  Y.5J.  12; 27. 15;  —  yqm  da  . .  °säcä  cBü  raneibyä (sd.)  xinOiim  Y.^i.$;  —  yj  vlänaet  da- iipmcä  (sd.)  aäa'Samli  dangrä  mante  -ia (Instr.)  mazdä  ahurö  ".  .  durch  seinen kundigen  Berater  Aia,  er  MAh."  Y.  46. 17;  3^-  '3;  —  vahista  säsnanqm  (sd.) yqm  .  .  sästl  'sä  ahurJ  Y.  48.  3;  34.  12, 46.  2;  —  maxdä  *yä  da  'iä  vanhSui mayh  (sd.)  manauAs  Y.  4y.  a;  44- ij  — yezl  ahyä  °iä psi  mat  xiayehl  (sd.)  ..mazdä Y.44~  15;  —  at  ahyäi  'iä  mazdä  urvarS vaxiat{sA.)  Y.48. 6;  —  ätrJm  ..  aojSt»hvan- tsm  'iä  Y.34-4'i  —  ^^  adr'ärum  . .  dalnk saoiyantqm  yä  ^haJc?r?tll  'iäcTt  urväxsat (sd.)  y'34.\z;  —  ks  vä  'iä  äfraiiä  (sd.) Y.5/.  11;  44- S;  —  'sät  hacä..  vaidä (sd.)  yS  Im  dat  Y.  45.  4;  —  vidui  (sd.) 'iä  ySm  mazdqm  ahur?tn  Y.  4S-  8 ;  — va»kSui  'iä  Aaozq%7Väi  (sd.)  ä  mananhs Y.45.  9;  —  ärmatsii  kasilt  'sä  hutSntus (sd.)  Y.  49.  S;  —  tSm  vS  'sä  mShmaidt huiJiaxäim  (sd.)  Y.  46.  13;  —  mazdä ahurS  'iä  hui.haxä  ifmvatä  Y.  32.  2 ;  — mazdä  ..%wävqs..  at  ns  fryä  °iä  dazdyäi häkurmä  (sd.)  Y.  44.  i;  —  spmtaHyäiä tur?i.. yehya  urvä  'iä  haiaifl (sd.)  Y.34. 2 ;  44. 1  o,  46- 16;  —  neit  'iahyä  adlvyeintj (sd.)  *hacsna  Y.  44. 13;  —  'iä  vyqm  (sd.) yehyä  hihäui(sd.)  nä  spmtö  Y.4^.  7;  — ärmaitlm  ..hi%qm  (sd.)  'iahyä  Y. ^4- ro; 4ß.  16;  —  tqm  dainqm  .  .  yä  msi  gai'iih •iä  frädBit  haiSmnä\sA)  Y.  44. 10;  43. 6,  34.14,  44-to,  4o-i',  —  'iahyä..  sairJ (sd,)  'iahyä  Virszsm  Y.35.Z;  41.6;  — /praiaaiträi  urväzistqm  (sd.)  'iahyä  da. sarSm  Y.49-8;  5J.  3,  31. 2\;  —  'i^miä ^ fradat.gal%Jm  Y.  j;j.  1 1 ;  —  'ia  (Vok.) kal  %wä  dar}sänl  (sd.)  Y.2ÄS,  45.6,  ;^. 6;  —  humqsdrä  (sd.)  °ia  (Instr.)  yeiä  yä
6091:—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  i^.  18, 50. 9;  —  atvs  staoiä  aojäi (sd.)  mazda..  'sa  Y.50,11;  2,  6,8,  2Ä  i, 34.T,  —  hvö  zi  "Sil  .  .  ahamMs  (sd.) urväkS  masds  Y.44.2;  18;  —  ara' (sd.) sf  xsmä  mazda  °s3  ahurä^^''  hyal  .  . yoorjaaäa  (sd.)  Y.  50.  5;  —  in  GHapt: masda  aAura  .  .  fava/ä  haxamS  (sd.) -sahyala  \.4a.ii.;  41.6; —  *aAura.mazda °ia  (Vok.)  srira  Y.j'5.3;  —  masdai  ahurai 'säila  vahistai  Y.  JJ.  j ;  4/.  i .  «)  in dualiscjiei  Verbindung  mit  ahura-:  yöi  vS syaoianäissärMil{%d.)aAurff*asa*Aisvä^''''> axhai/ ..  Y.51.3  (s.c).  b)  neben  VoAu- ManaA:  yäcS  vehü  uxoa  fral%  (sd.)  ma- nauAä  yOcs  °sa  (Instr.)  aahlus  Y.  44-  8; '31  —  yf  «""'^  "^  (Instr.)  tmüi  hvö *mainyJus  a  vaMstat  kaya{iA.)..  Y.S3.6; 4g,$;  —  %wavas  . ,  masda  hadtmsi  (sd.) -ia  vohulä  yyas  manavkä  Y.  44-  9 ;  2Ä  5 ;
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6186:■  /.,  g.  aäay-  f  'was  einem  auf  Grund seiner  Leistung  —  in  gutem  und  schlimmem Sinn  —  zukommt;  Anteil,  Los,  Verdienst, Lohn,  Belohnung*,  bes.  beim  letzten  Ge- richt": kä  ahmäi  °sis  ?r3nävi  Y.g.y,  4 —  yaia  ad  masis/äsca  . .  asayö  »nnavanU Y.52.3;  —  'itm  fyao^anäis  vohü  äaiält mofuiMhii  "(je)  nach  den  Taten  (die  einer getan  hat)  soll  VM.  das  Los  zuweisen" Y..^j.i6";  —  ia  zasta  yä  tä  haßt  (sd.) az<i  yä  da  -Sil dr^äin asäunaka  ". .  jene Lose,  die  du  dem  Drug-  und  dem  Afa- anhänger  zuweisen  wirst  .  ."  Y.4y-4;  — ail  .  .  ya  vi  'Itf  *ranöibya  savSi  (sd.) ndoyai  Y.43.12;  —  vTdyai  (sd.)  saoi);_ jdiä  hsi  '/is  anhat  Y.  4^.  9 ;  —  yada  'sifis maAjä  VOSS  xsayä  (sd)  Y,50.9;  -^.S; iiSit..asahe  nSi£  '/ayä{GS.y^/räi'fnti{sA.) P.44;  —  >r>kyä  amatai^yä  °Ms..aslöis Vr.^.4;  —  däidl  aiä  tarn  'sim  vanhsus Syafta  manar^hs  Y.  28. 7 ;  — yS  mHi  nä  va gMa  (sd.)  va  .  .  dayät  ■  ■  vahista  'slm  asäi vehü  xiair»m  mananha  "wer  . .,  als  Lohn für  seine  Gerechtigkeit  das  Reich  durch VM.  (verldhe  ihm)"  Y.4ö.io*>;
6298:steht,  dem  das  Paradies  sicher  ist';  im jAwf.:  yaia  i>aH  (sd.)  a^äum  *a<ia  atiAs 'sota  . .  z'ahiäa/u  atihSus  °sava  jasB  Y. j/,i6;  —  jvasHt  nöit  dval  °sava  miSascit fwii  ^axsaitHsd.)  vahistahe  ataksu^"^^  lang er  lebt,  erwirbt  er  sich  das  Anrecht  nicht, ood  - ,"  V,5,6ii — /si!mä{sä.)  asil 'fava ■nrüraja  vaktäd  \.s8.i,^
6537:vahyah-,  —  J)  Vgl.
6567:sva.  da  sein,  vorhanden  sein,  extstiien ;  es  hat  am  ku'-äst»iram  Yt.  /j.  i  s  * ;  153';  — gibt..".  A)  II  im  Ap.:  /  gaumätc^dafväis . .  Aatam  dracjistais  \.12.^;  ^', ttämt^  »lagul  ahJ'  hauv  . .  Bh.^.z;  — !2i?.3;  —  kahmäiclt  hätqm  jiß'qm  .  .ädä t/'urJ'ma^ä  .  .  ulä  antya  ba^äkJ'  (yay'  (sd.V'JcdemderSeienden.."  Y.jj.S;/^.!!, h(ftiy  "AHM. . .  und  die  andern  Götter,  \  12.  4,  27. 15,  A. J.  7;  —  tqtn  daenqm  yn die  es  gibt"  Bh.^^.  13;  12;  —  negirt:  naiy  kätam  vahista  "die  Religion,  die  für  die J>io*  martiyt^  naiy  pirsa^  naty  . .  hyJ' . . '  Seienden  die  beste  ist"  V.  44. 10;  —  ya'ia "es  war  kein  Mensch  da,  weder  ein  Perser  haribis  jijisam  (sd.)  .,  Y.2/.1;  —  ysi noch  . .,  der . ."  Bh.  M  3.  B)  im  Avf.:'A»nti    (APn.)    aiüha    z>mS   kan^nii    (sd.)
6568:yezi  a>ä  sia  Aai'iJm  (sd.)  \.34.fi;  — ■".  .  Wesenheiten  (animalta)  .  ."  V,^.  40 h)nH*^  anyhHt  aiasca  söi>r<hca  "es  gibt  PiiZ.;  — yä  kstqm  syaoianartqm  vahista auch  noch  andre.."  V.J. 20;  —  at'a  h>nii' hyäl  "welche  unter  den  Werken,  die  es paritöJanunqm  (sd.)  syao^nanqtn  asi^arj- ;  gibt,  die  besten  sind"  Y.  jj.  3;  Vr.  72.  4; tayS  ¥.7,52  PüZ.;  —  kapta  hanti , —  daatayli  yat  hattinqm  vahistayäi *hävanayl  miat'S 'S.  102  Q);  — yfAud>i\"dN  besten  aller  Religionen"  YL/j.  91, ySi  /antl  "der  es  wohlmcint  mit  denjga;  —  aisam  aukunam  hatam  VyL Seienden"  Y.  45.  6;  44^  i6S>,  5/.  io;_— |J0(?);  —  ot'j  .  .  vasiniAe  hat's  (GS.)"» yehyä  .  .   vahUl}m    vaidä    (sd.)    mazdh  .  .  i  aoäitlm  (sd.)    vao'ait  V.  4-  46.  I )  mit
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
6993:drang-  V.  ('festhalten')  'an':  ydi  ä  vanhsus mananAs  didray%S.duy?  Y.  4S.  7.  b)  un- räumlich,  zur  Angabe  a)  des  Mittels  'mit- telst, durch,  kraft':  ys  zaotä  aSä  imüS hvS "mait^Sui  3  vahistat  kayä  (sd.)  , .  västrya ^-  JJ'6;  —  fnasdä  dadat  ,  .  Aaurvats  ,  . bärßis  a  osaAyäca  j^apai^yaj (sd.)  ..  sars \. 31.21.  ß)  der  Veranlassung 'wegen, (ziun  Dank,  in  Vergeltung)  für  — ':  gavSi ärdis'isA.)  *a  unäa  (sd.)  "> . .  ys  is
8172:f.  EN.  einer  gläubigen  Frau: i  staffi-ri  vahistalu  asake .140.
10420:Weib' :  yJ  vH  mSt  nJ  °tiä  v3  mazdä ahtirä  däyHl  .  .  y3  tu  jvistä  (sd.)  vahista "wer  mir,  Mann  oder  Weib,  das  tut, o  MAh.,  was  .  ."  Y.  46.  jo;  —  'nasca (AP.)  vlrö.vq^wh  Y.2.6;  —  'tianqmca vird.t'oiwanqm'H . t.6;  —  'naiiqm  *pouru.- tarpfJii&A.)  vJrS.vaiwanqm  Vr./,  5; —  °iia hubafa  hufo'irTs  kurao''at3hBYz.2.T,  F.23; —  'mnqm  ratnm  amruyiY.  ij.  i .  a)  bes.  [ von  Götterfrauen:  imam  .  .  sqm  'tiäbjl hakrä  yazamaidl  yü  tiä  baraitl  yas^ä  töi •na  aAura  mazdä  \.jS.i;  z\t.:  yäsea  U •nä    aAura    masda  Vr.  J.  4.  S.    noch  j
11009:vas?iS  (^ur^masdähe^  mana^a  dä- fD.4.2.  B)imAwr.;  i)die Glieder  sind  nominal'';  a)  sie  folgen  sich unmittelbar:  pita  pu%rasea  .  .  iatarasüi ^■9-5i  —  pu^ra  (ND,)  ..  urvSxsayB k»r>s3spauaY.g.\a\  —  tum  akB  vahistasca ahi  YtJO.  29;  —  kanta  aiwyäxstaca Y.57.  IS  (s.  dagegen  Yt.;o.  103,  Sp.  567  u.);
11016:—  %ioähü  gathaha  tanmica  Y. 43.T;  — 3^ai^  syaö^anai^  hisvasca  Y.5J.  13;  — msr^tB  bpfstaca  damayäi  V,  2.3;  —  dasä aspa  aHnavaitlS  idtrtmcä  Y.^^iS;  — vokB  manatsha  aläls  Y.34-151 —  asoAe vahistahe  a^rasca  Y.  i.  4;  —  ahya  artlOui astvalB  manarfhasca  Y,4j.  3;  —  narqm asaonqm  dafnayasca  Yt.  7^.69;  69;  — hävöya  bäzvB  dannaca  V.?.  25;  —  afys dsikrabyS  aiwyasca  yaoxstibyB  Yt/o.  Sa;
11319:•  j.,  g.  'äöra-  i)  Adj,  (fem.  °ra-)  'mani- festus,  offenbar,  klar,  sichtbar,  augenfällig': ttü  Im  vTspa''>  °r7(NSm.)  zi''>  mazdanhs.- düm(sd.)  Y.43-i;  —  "nm  ahurim  mazdam Yt.j.  4;  —  ävil  nh  atUar?  hSntü  ..  °rS raiays  (■&&.)  Y.  JJ.  7 ;  —  -ri  (NPn.)  mi'irahe /rayans(sd.)Yt.  10.112;  —  'ra  vS  buyärss masänä  'ra  vö  zatan^.savS  (sd.)  'nm  bsit yäifmÜt  :^ar3n3  .  .  dayata  Ny.j.  n;  in ungeschickter  Verwendung  Vyt.  7f.;  —  "nl (NPn.)  J  kudiiahs  .  .  valdymnai  (sd.)  ■  . Y.J/.  32;  —  °/vm'>  dasvan  bassaz?m  Y. 10.  7.  2)  n.  'Gesicht';  a)  sva.  'Anblick': taica  .  .  awÄÄ/  vahistahe  're  paityanie "und  die  Werden  des  Anblicks  des  Para- dieses teilhaftig  werden"  P.  4g.  b)  sva. 'Anthtz':  yB  paoirys  'nm  urvaäayaia  (sd.) .  .  haolat  Yt.  13.  89;  —  mßinm  ..  *yahmi paiti  'rim  vlhatsm  vJspais  avi  karsvqn Yt  10. 64.  c)  sva.'  Vision,  Erscheinung' : 'ra  (IS.)  msi  dam  *ahUmMLratüm  (sd) ciidi  '^.44-i(>.'  d)  sva.  'äussere  Er- scheinung, Gesammtheit  der  äusseren  Merk- male', spez.  von  der  Menstruation:  ya} kl  'ra  daxst>m  havaiti  yat  kl  daxsta 'r?m  bavaiH  V.  16.  i4[?)^'I  —  s.  Ab- leit*' 3)  'Kundgebung';  vJ  daSväis  .  . sarpm  mruyi .  .  vi  manSbTs  vi  valsbxl  vT syao^anais  vi  'rai/  Y.  12,  4.  a)   sva
11323:'Offenbaiung* :  vahista  'ra  (AP.)  yatamaide y3  itaota  yesnya  Vr.aj.  i.  Undeutlich: :fahmi  dam  :^ahmi  're  Vr.  i4-'i;  —  tat 'nmca  N,  65*';  —  'nmctt  N.  67*';  —  äat haca  'nm  FrW.^.  2;  —  wertlos:  'nm buya  tämäi  ..  Vyt^.         [Yt/o.  67:  lies
11360:—  jvasHt  nSit  bvat  asava  vnsasHp  tüSti bax/aiti (sd.)  vahistahe  at3kSusY.^,6i;  — fraia  fraydit  . .  ä  sangaäbyasa^  apn  ä inubyoicit  .  .  3  matiyqnas^t . .  ä  ripr^m- zasät  äpS  Y.6.aj;  —  isavasHt  al^qm  .. ar/tayascit  .  .  zarstvaat  . .  kantacit . .  va- zracit  . .  Yt.  10.  39  f.  a)  das  zweite  ^ steht  unregelmässig:  kasSusÜli  nä  ..  isvä- (sd.)(?i/'*  hqs  paraos  Y.  47.  4.  Anhang, lU  wechselt  mit  iS:  tä^^.,vasfml  anyäüä vTduyl  Y.  44. 4.         2)  wie   bei   I ;    aber
11375:—  aiatcjt  haca  Y.2p.  6,  27. 13;  j4. 13;  — hurayasHl  aoa  . .  daidyal . .  astmanqmcit ' . . K.3.4V,  —  aiwi.niticit  .,  span:>m  ..  aisa druxs  .  .  apadvqsaiH  V.  Ä  16;  —  tut  RS ttäcit  vansansY.51.1;  —  zusammen  mit U  (Sp.  367  o.,  586  o.):  f<M:"J«(sd.)  ..ya zl  vävfnzöi  pairl.cihlt  .  .  yScä  var?saiti aipT.ä^Tt  Y.  2g.  4;  —  bei  Zahlwör- tern: spiimm  zairitpm  .  .  xsvaiayacit  .  . vTväoayantu  \ .  8.  IT,  iS'^';  —  puxhmHl nä  arydu/qm  tanBm  ptrydte  V,  4. 17;  — para  mS  .  .  'hrifSt"^  vahista  .  ,  vlsata (sd.)  P.  J5; —  %risHi"'>  ..  hamahe  ayqn Vyt  41;  —  bes.  beim  Pron.  pers.  und dem.:  haxsaya  azsmat ys zara'kustm /ra- timq  .  .  anumatayaica  ..  Y.8.  7;  — pairi ml  tümcit  dayä  kaoma  . .  vahistptn  ahQm Y.ii.\o;  jo.  I9(?),  Vytj;  —  tun  vaimlit yazamaide  YL75.  i;  1;  —  ciknm  bsil yüi>mcil  :^armS . .  ääyaia  Ny.  J.  1 1 ;  VyL •S';  —  Aasat  va  nsit  vä  "der  (kanns)  oder (es  geht)  gar  nicht"  Yt/^- 20;  —  Jrä Mmat  nidar^zaypn  V.  J^.  31; —  tanu.mas5 (sd.)  zX  *altqmcit  alayqm  *pqfre  yat  ,  , P,  i8\    —    mä    ml   aetayasa£    tao^rayä
11915:j  machen  (Jmdn.  sva.  es  Jmdm.)':  täpayäii mqm  asa  vahista  mqnayfn  ahe  ya%a nyaoxivst)m  Hx.1-.2q.  a)  absolut  'Wärme bringen,  schaffen',  von  Sonne  und  Mond: yai  hvara  raoxlne  täpayatt  \t6.i\  i,  7.4.
12787:a)  als  Akk.  ohne  Kiicksicht  auf  Numerus  und Genus*',  zurückweisend:  y5  .  .  vamäsca hqm.räzayäti  . .  srvaiia  . .  a%a  'im  *upa.- tagsayäH  *unähva  dim  rat?aya{%A^ca  V. 17,2; — srväbya  may>m  ava-kansis  ..paiti 'im  äbarsii  ".  .  für  die  Nägel  sollst  du eine  Grube  graben  . .  du  sollst  sie  hin- bringen" y.ij.T,  5;  —  sao%rä  ..  a%a yS  'im  *frahinHn  (sd.)  N.  68-,  —  hqm.- vaniflm  .  .  framm.narqm  .  .  yä  d°  (näml. narSuil)  jasaiti  bafs'baxttmcii  (sd.)  yä narqm .  .Nt.-j  .^.  b)  alsGen.'';  a)  zurück- weisend auf  ein  Relativ:  yas^a  ..  aparao- oayete . . pairi  'im  lanava  anm..urvän3m haca  vahistat  a»haoi  ".  .  procul  eius dislinebo..animama.."Y.jp.7">.  ß)  vor- ausweisend :  ÄS  ba  aisS  äs  .  .  yS  .  .  paiti.- hincaiti  ä  'im  nBit  apivatäite  dainayh  ,  .
13101:paiti.jasätB  ii3ca  Ozüitisca  ..yat..  aäaahs °iA^/..'V.g.$${.; — räma  i^ästr?m  *aöhä 'i^hsul  afrlnami  V.6S.i$;  —  at  tsi  at?h^i saofyantS  (sd.)  'Jiptnam  \.  i0.  12;  70.4, Vr./J.i3;  — ä^ravanS  'hyunqm  Yt/J.147; — ySi  *iyefqm  .  .  alB.lsS  (sd.)  'hyunqm  Y. 42.(>\  —  mihfpm  ..  vJspanqm  'hyunqm daitihufaitim  Yt  70.145,  ^P-3S)  Y,  2. 11; J.  1 1 ;  —  fravasayS  .  .  vJspä  vtspanqm 'hyunqm  Vty.  ai;  21,  5.  22,  98; — bäna joff  ä/rasane  -ahuiyU  V.^.  27;  —  ^^agpai'ie nö  'iähuif  nibätal^a(Sp.j2i  o.)  haosiitalca YtJj.66;  68;  —  tis/rim  . .  yhn  . ,  *kisp5.- smti  huyairyUta  "i'ähavt  uzjaimt^m  äui- yairyäea  Yt.  Ä  36;  V.  4.2;  —  huyairyJ avi  'iähu/\LS.g;  —  usia  a.bav,it  'iii/iavö (P.)  US  vB  apqm  alavS  .  .  jasanti  Yt Ä  29;  —  ilbyd  'iiihubyö  snislB  ydi,a alm  (näml.  iistryö)  bavaitt  yallB  Yt  8. 47 ; '^■34j  —  m»rm(aite  vtspqm  'iühaom mairyS  mPbrB.änixs  Yt,  10.2;  —  tBm  akB vahistasla  mii:ra  ahi  'irihubyB  Yt. /o,  29J
13282:—  ij  airyamä  ks  x''affus  (sd.)  '■tisis  a»hal yS  .  .  Y.4p.  7";  —  matd:'  'ta  .  .  gayeliyj (sd.)  syadianäil  vahyO  Y.5/.  19;  —  «Äj' urvai:ä  'tsityascä  karapanS  vilsträi  arlm (sd.)  Y.5/.14A  B)  im  jAw.:  vispaca .  .  frärai'iya  (sd.)  asa?u  'läis  vahistake F.  4e'>;  —  y<Ahe  toa  (Sp.  364  u.)  mazda yastam  Hnasti  ya%a  'ta  ahurake  ". .  An- betung .  .,  wie  sie  nach  dem  Gesetz  des Ah.  (sein  soll)"  Y.  2;.  i  (?);  —  *far5  darr/a 'ta  . .  zara'huHraAe  P.  ^6;  —  nffil  xshäva- yeiti  ahunm  mazdqm  .  .  y3  .  .  larS  man- yete  .  .  'ttmla  rasnumea  arstUtimca  Yl  10.
```


## [2026-09-14T03:09:21.949Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== vohu in BRT ===\"\ngrep -n -i \"vohu\" BRT.txt | head -20\necho \"=== vanhu / vaiihu ===\"\ngrep -c \"vanhu\\|vaiihu\\|vaühu\" BRT.txt\necho \"=== leaves count ===\"\nawk 'BEGIN{RS=\"\\f\"} END{print NR}' BRT.txt",
 "description": "Locate vohu in Bartholomae"
}
```


### [2026-09-14T03:09:23.067Z] TOOL RESULT

```
=== vohu in BRT ===
3023:matiö  vohu  manö  tat  vanaili  "besiegt  wird   •  j.  akaran^m.driway- '>  Adj.  'über  und
3024:auch    Aka  Manah,    Vohu  Mattah    besiegt  j  über  mit  Flecken  bedeckt':  druxi yä  nasus
3732:JCaväta'^:    kavsis  *'var»A}ui''>  asaonö  \i. ^3-^3'i  — yiml'a  karagm  'vohum  Ytig.
4222:yänäis  zaranaemä  (sd. )  Y.2Ä  8  £  b)  sub- stantivisch: jajA  mg . . /rabarät . .  *st»ri- naoiti  'na  *  avavat  starsm  (sd.)  . .  ya"iia  . . P.22f.  2)  vorausweisead;  i)  adjek- tivisch, a)  auf  direkte  Rede :  apasca  vajmhls yatnda'^äne  hala  °na  ga^ivya  vaca:  garS nmane  (usw.,  Y.jj.rs)  Ny.4.8;  Y.ö'5.14, Y.  10. 19.  b)  auf  ein  Relativ  als  dessen Korrelat:  °na  ^wa  yasnayazane  -na  ^wä yasna  frayazäne  yasi  ircd  yazaia  vlstäspö Yt/7,61;  —  Aauca  ^'nayiVi  nara  vohu manS  jag?r?buitarS  {anhat)  yö  .  .  ya"^a hau  yS  .  .  V.  4-48-  2)  substantivisch, a)  auf  ein  mit  ya'^anä  angeschlossenes ' Nomen,  sva.  'er,  wer  es  auch  sei,  jed- . weder':  vi.,  'tiä  sanm  mruyg  ya'kana dngvatä  rqxsyantä  "ich  entsage  der  Ge- meinschaft mit  jedwedem  feindseligen  ^r." Y.  J2.4*>.  b)  auf  einen  Satz:  tum  "na miirs^rujqm  .  .  "ä^wyqm  avaiarahi:  apa alsqm  .  .  at^d  .  .  barahi  Yl  10. 23.
4665:*vivär»ivahe  °vahe  asaonS  "des  V.,  Sohns des  A.  .  ."  YtJj.iza;    —    vohupgrgsahe vahe  asaonJ  "des  K,  Sohns  des  A."  Yt y.124. Eig.  Bed.?
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4791:mit  antarp,  pairi  und  ava  'umstellend dazwischen  treten':  yai  titarat  anrö  main- yuf  dähltn  .  .  aiahe  antan  pairi.avail^m (3DPrA.) '"  vohuca  manO  atarsca  "als  an- drang AM.  gegen  die  Schöpfung  . .,  da traten  schützend  dazwischen,."  yt./j.??.
4934:•  j.  ayö-xäusta-",  ayaoxSusta-'^  n.  'ge- schmolzenes(flüssiges)MetaIl(Eisen)':Ai^ff- yäli  mam..ya>a  "ftffi  Yt.z/.ao,  a)  Be- zeichnung des  feurigen  Metallstroms  beim letzten  Gericht*:  vohu  x^aHnm  . .  xia- "^rjm  vairim  .  .  °t3m  yasamaide  Vr.  20.  i ; —  'tim  ..  marzdikam  %räyB.driyüm  S.2. 4;  —  °tahe  tnarzdikai  ^mySjiriyaove  S, /.4-
5182:•  j.  aväraoätrt-  m.  EN.  eines  Gläubigen: 'r5is  '*  asaoiiS  Yt.  13. 103;  —  vohu.nimaT3hö 'rsW*  aiaons  "des  K,  Sohns  des  A.  .  ." Yt7^.i04.
5386:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
6074:ys. .  mazdayasnö  aojanö  'sähe  raima  (sd.)  \  13.  42,  Y.  68.  7,  14-  48;  —  a^al  nS  vacö jlsti^amnS  "V .  8.  y, —  uxltie  (sd.)  xraiwe  .  ,  *sixsaimca  (sd.)  .  .  °jvW  haäz  yat vTdrvanahe  °sät  'V.4-AS',  — yaüra  nard  vahiHät  Y.iff.ii.  LS.  'Saya  als  Adv, asavatts  'um  h^tüi  zrazdatsma  (sd.)  YL  j  sbes.  II)  '(dem  heiligen  Recht  ent- y-  'S;  —  tha  5%ravanS  .  .  ma/iyetiU  sprechtnics,  ^/«mässigesj  rechtes,  recht- vanh^s  'sähe  Yt7j.  147;  —  vahistmi  schafTenes  Tun,  Gerechtigkeit,  Recht- °i3m  yatamaide  Vr.  2g.  i ;  —  ySi  'iäi  schaffenhcit';  auch  in  kollekt  Sinn  'alles vaonarp  (sd.)  Y.  26.  4,  S;**  —  yö  yaomwas  einer  recht  tut,  bona  opera'.  i)  im iärayeiti  hs  'hm  iarayeiti  [sA.)  V._J,  31;  ■  gAw.:     huää    (sd.)    'Sim    vohucä    manä
6091:—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  i^.  18, 50. 9;  —  atvs  staoiä  aojäi (sd.)  mazda..  'sa  Y.50,11;  2,  6,8,  2Ä  i, 34.T,  —  hvö  zi  "Sil  .  .  ahamMs  (sd.) urväkS  masds  Y.44.2;  18;  —  ara' (sd.) sf  xsmä  mazda  °s3  ahurä^^''  hyal  .  . yoorjaaäa  (sd.)  Y.  50.  5;  —  in  GHapt: masda  aAura  .  .  fava/ä  haxamS  (sd.) -sahyala  \.4a.ii.;  41.6; —  *aAura.mazda °ia  (Vok.)  srira  Y.j'5.3;  —  masdai  ahurai 'säila  vahistai  Y.  JJ.  j ;  4/.  i .  «)  in dualiscjiei  Verbindung  mit  ahura-:  yöi  vS syaoianäissärMil{%d.)aAurff*asa*Aisvä^''''> axhai/ ..  Y.51.3  (s.c).  b)  neben  VoAu- ManaA:  yäcS  vehü  uxoa  fral%  (sd.)  ma- nauAä  yOcs  °sa  (Instr.)  aahlus  Y.  44-  8; '31  —  yf  «""'^  "^  (Instr.)  tmüi  hvö *mainyJus  a  vaMstat  kaya{iA.)..  Y.S3.6; 4g,$;  —  %wavas  . ,  masda  hadtmsi  (sd.) -ia  vohulä  yyas  manavkä  Y.  44-  9 ;  2Ä  5 ;
6092:—  masda  . .  ahurö  hyal  höi  °/a  vohucä cöist  (sd.)  manatihs  Y,  4^5. 10;  —  akurB mazdä  sar^mra  {^.)  vohä  manattha ..°sa hulAaxa  Y.j2.a;  —  at  hvö  'sahyä  anhat vatihsusca  vastrl  (sd.)  manauhS  Y.  33.  3 ;
6093:—  hvd  nJ  mazda  valtt  'saica  car3kir>%ra (sd.)  sravayetihl  Y.sp.S  {VM.  spricht);  — ta  v!  vohü  tnatuwha  'iaica  savai^*avlit (sd.)  Y.$s.  I S ;  ^  apanS  (sd.) . .  ä  xid^rtm rarihius  manatjhs  °/iJt  ä  ^^2S/(sd.)  päitö ^■33-  5 i  —  '"^"^  gatdr  maitan/hä  daidl  ^-sa (Instr.)  *dä  '*>  dangäyü  snrväii'  (sd.)  tu ti.voai/  mazda  Y.2Ä6.  c)  neben  Ahura- Mazdah  und  VohuManah  yöi  vi , .  särmig ahurö  *°jä'*'. .  ttX'-ais  vanhSu^  mananhö Y.J/.  3  (s.  1  aa);  —  anais  vä  nöij  aAura
6096:—  vohü  , ,  manaaha  . .  masdä  '/a  Y.  33. 8;  —  °M  masda  . .  vohu  manauhä  Y.^. I ;  —  masdä  .  .  vohü  mananhä  'faia  Y. 34,  1 5.  d)  neben  VohuManah  und X/a'ira:  ahmäica  .xsa'hra  (sd.)  jasai  (sd.) manatfha  vohü  'säcil  (als  Subj.)^*  Y._J0. 7;
6104:20;  —  ia  GHapt:  ahunm  masdam  .  . 'wm  ai  vahilt>m  vokula  manJ . .  vohuca xsa>r^m  .  .  Y.J7.  i-g.  2)   im  jAw.:
6105:•Ijm  vahiititn  sralihm  aiiuhm  sptnt^m Yl^.i8^  1.2,3',  14,  Y.;6.3,S.2.3,VyL42; —  "ÄJ  z'aAisia  'sa  srailla  dansama  %wä Y.öo.  13;  P-J5;  —  °-i5«  vahistitn  äinmca.. Y.  2.4;  J.4,  S. /.  7,  2,  7,  A.4,  2;  —  'sitnca vohiia  manö  Y.55.  5;  —  ahuräi  masdäi . .  'sai  vahUtäi  xla\räi  vairyäi  ärmatse V.ig.  11;  —  akunm  maidqm  . ,  vo/iu wiara  'ÄOT  vahi/t?m..G.5.S\^.l.i.i.,57- 34, 70. 1,  Vr.  II.  16,  Yt  /.  25,  FrW.  /.  i;  — ärmaitlm  , .  yehe  dähre  (sd.)  '^aheca  Vr. J9.2;  —  H5it  A3«  Jffr?, .  yS  ndtt  '/a  sBrÖ nsit  hau  taxmS . .  yS  ndit  *'la  taxms  P. 46.£;  —  tamaaha  °säi  usdatä  (sd.)  paitl Y. /3.  3;  —  ifanvaitU  °sake  virisS  Y, i6.  7.  a)  als  besonderer  Gegner  des Aima:'^  sp>ntö  mainyul alfym  frarfhari- cayat  vohuca  manS  °s»mca  vahist>m  .  . anrö  mainyui  asüm  franharxayat  aiamca mtnS  atsjmfmüa  . .  Yt  ig.  46;  —  vUfe  zT ante  *maoäaiS  (sd.)  oEsma  haSiäe . .  äat hs  yS  haotnahe  maus  °sa  hacaiU  urväs- mana  Y./o.S;  YtJ?.«;.  a)  aiahe  vaki-
6165:•  j.  aSa-ä^ra-,  aäö.ÜdTa-'*  Adj.  'der seinen  Ursprung  im  Asa  hat':  vispanam vohunqm  vispanam  'ranam  H.  1. 1 ;  —  vis- palsu  var»hufu  vUpagsuca  -ra^iu  YL  1/.3'*; P.  27'';  -^  äps  ..  urvara  .  .  vitpa  voka 'ra  y.8.^.  a)  vlspa  *voAli  maxdaoäla 'ra  Y.ig.2,  22.3,  YL5.89,  y.88,  H.i.3, 16,  V.ii.i,  2,  10,  Vd.4;  —  i7^»t(  ..  vispa *voAa  mazdatiäta  'ra  Yti.  7.
6388:•  j.  aäsmao^'a-  (Adj.  'der  das  heilige  ■  auch  Josti  NB.  ik.  —  o  Ein  wenig  sinnvolles. Recht  verwirrt',  als)  m. 'Verbreiter  ketze-!  ^^  "'"'"  und  j''  r'  nicht  lusammengehören. rischer  Lehre,  Irrlehrer">:  j'J^jföffi /«(Vi- ,  •  j-  aSam  vohu  (oder  «•  v  vahis'bm kanamra     s3>ram     kaoyam     kära/nam'a  \'"f^)-   wird  das  damit  beginnende  Gebet
6389:'yanqmla    üzansrättam   Y.27.14  zitirt,  zB.  Yt.  5.0:  staomi  asm: "       ■'      aspm    vohu    "ich    bete    das    .^/«(gcbet): '■Ahm  vohu"".    Oft  in  PüErl.
=== vanhu / vaiihu ===
33
=== leaves count ===
1041
```


## [2026-09-14T03:09:25.641Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 548 eu- ===\"\ngrep -n \"eu-, before a vowel\\|^eu-\\|eu-, pref\\.\" KLN_1966.txt | head\necho \"=== KLN eucalyptus ===\"\ngrep -n -i \"eucalyptus\" KLN_1966.txt | head\necho \"=== KLN Euclid ===\"\ngrep -n -i \"Euclidean\\|Eukleides\" KLN_1966.txt | head\necho \"=== KLN evangel ===\"\ngrep -n -i \"evangel\" KLN_1966.txt | head\necho \"=== KLN hygiene ===\"\ngrep -n -i \"hygiene\" KLN_1966.txt | head\necho \"=== KLN swastika ===\"\ngrep -n -i \"swastika\" KLN_1966.txt | head\necho \"=== KLN Eugene ===\"\ngrep -n -i \"eugenic\\|Eugene\" KLN_1966.txt | head",
 "description": "Grep Klein for relevant entries"
}
```


### [2026-09-14T03:09:25.811Z] TOOL RESULT

```
=== KLN 548 eu- ===
13764:eu-,  combining  form  meaning  ‘good,  well’.  —  Fr. Gk.  eu,  ‘well’,  prop.  neut.  of  £64,  ‘good’,  which is  cogn.  either  with  Hitt,  ashshush,  ‘good’,  or — more  probably — with  OI.  vasuh,  Avestic  vohu-, ‘good’,  Ir.  feb  (fr.  I.-E.  *wesw-a),  ‘excellence’. Eu-  is  the  opposite  of  dys-. eucaine,  n.,  name  of  two  synthetic  alkaloids called  alpha-eucaine  and  beta-eucaine. —  Coined fr.  eu-  and  the  second  and  third  syllable  of cocaine.
=== KLN eucalyptus ===
6256:of  xaX'j-Tstv,  ‘to  cover,  hide,  conceal’.  See  next word.  For  sense  development  cp.  Circe. caiyptra,  n.,  a  covering  (hot.)  —  ModL.,  fr.  Gk. xxX-j-Tpa,  ‘a  covering,  veil’,  fr.  xccXotteiv,  ‘to cover,  hide,  conceal’,  which  is  rel.  to  xaXupT), ‘hut,  cabin’,  xccXta,  ‘hut,  nest’,  and  cogn.  with L.  cella,  ‘storeroom,  granary’,  celdre,  ‘to  hide, keep  secret'.  See  cell  and  cp.  caliology,  Calypso, apocalypse,  Eucalyptus,  kelyphite. calyx,  n.,  the  outer  whorl  of  leaves  (bot.)  —  L., fr.  Gk.  xoXu4,  ‘the  cup  or  calyx  of  a  flower’, which  stands  in  gradational  relationship  to x’iXiC,  ‘cup,  drinking  cup’,  and  is  cogn.  with  L. calix,  ‘cup,  goblet,  drinking  vessel’,  Umbr. skaice-ta,  scalse-to,  ‘out  of  the  dish  or  saucer’, OI.  kaldsah,  ‘pot,  cup’,  kalika,  ‘bud’.  OE.  celic, ctelic,  carle,  ‘cup’,  is  borrowed  fr.  L.  calix.  Cp. chalice,  cylix.
6927:cell,  n.  —  ME.  cede,  fr.  OF.  cede,  fr.  L.  cella, ‘storeroom,  granary,  bee's  cell,  hut,  cot’,  fr. I.-E.  base  *kel-,  ‘to  hide,  conceal’,  whence  also L.  celdre,  ‘to  hide,  conceal’,  oc-culere,  ‘to  cover, conceal’,  OI.  sdla,  ‘hut,  house,  hall,  stable’, sdlah,  ‘hedge,  enclosure,  wall’,  Gk.  xaXTS,  ‘hut, nest’,  xocX')!3r,,  ‘hut,  cabin’,  xaXu-TEtv,  ‘to  cover, hide,  conceal’,  xsXOtpoc,  ‘sheath,  case’,  xoXeoi;, ‘sheath’,  Mir.  cul,  ‘defence,  shelter’,  culaid, ‘cover’,  OIr.  cttile,  ‘cellar,  magazine’,  OE.  head, hall,  ‘hall’,  hel,  hell,  helle ,  ‘hell’,  helan ,  ‘to  cover, hide’,  Goth,  huljan,  of  s.m.,  hulistr,  ‘covering, veil’,  huhmdi,  ‘cave’,  OE.  heolstor,  ‘that  which veils,  hiding  place,  darkness’.  Cp.  cclla,  cellar, cellule  and  the  second  element  in  Paludicella. Cp.  also  caliology,  calyptra,  cilia,  clandestine, color,  conceal,  dharmsala,  Eucalyptus,  hall,  hell, helmet,  holster,  hull,  kalidium,  kelyphite,  kil-, occult,  superciliary,  Valhalla.
13765:eucairite,  n.,  a  copper  silver  selenide  (mineral.)  — Swed.  eukairit,  formed  with  suff.  -it  (represent¬ ing  Gk.  -iiry.  see  subst.  suff.  -ite)  fr.  Gk. Euxalpoic,  adv.  of  cuxatpoi;,  ‘seasonable,  op¬ portune’,  fr.  eu,  ‘well’  (see  eu-),  and  xoapXc,  ‘the right  season,  the  right  time’  (see  kairine).  The mineral  was  so  called  because  it  was  found  by the  Swedish  chemist  Baron  Jons  Jakob  Berzelius (1 779- 1 848)  soon  after  the  discovery  of  selenium. Eucalyptus,  n.,  a  genus  of  plants  of  the  myrtle family  (bot.)  —  ModL.,  lit.  ‘well  covered’, coined  by  the  French  botanist  L’Hdritier  de Brutelle  (1746-1800)  in  1788  fr.  eu-  and  Gk. xaXu7tx64,  ‘covered’,  verbal  adj.  of  xocXurexeiv, ‘to  cover,  conceal’  (see  calyptra);  so  called  in allusion  to  the  cap  covering  the  bud.
20181:jarosite,  n.,  a  potassium  iron  sulfate  (mineral.)  — Named  after  Barranco  Jaroso,  Almeria,  Spain. For  the  ending  see  subst.  sufF.  -ite. jarrah,  n.,  a  eucalypt  of  Australia  (Eucalyptus marginata).  —  From  Australian  native  name, jarvey,  n.,  a  cabdriver.  —  From  Jarvey  or  Jervis, name  of  a  Dublin  driver  who  lived  in  the  18th century.
=== KLN Euclid ===
=== KLN evangel ===
2753:angary,  n.,  the  right  of  a  warring  nation  to  use or  destroy  the  property  of  neutrals.  F.  an- garie,  fr.  L.  angaria.  See  prec.  word, angel,  n.  —  ME.,  fr.  OF.  angele  (F.  ange),  fr.  L. angelus,  fr.  Gk.  oiyyeXo-,  ‘messenger,  divine messenger,  angel’  (whence  the  verb  dyyeXXetv, ‘to  bear  a  message,  report,  tell’),  which  is  rel.  to dyyapo?,  ‘mounted  courier,  messenger’;  of Persian,  ult.  of  Sem.  origin.  Cp.  Akkad,  agarru, ‘hireling,  hired  laborer’,  fr.  agaru,  to  hire  , which  is  rel.  to  Aram,  agar,  eggdr,  ‘he  hired’, (whence  Arab,  ajara,  of  s.m.),  Heb.  iggereth, Aram.  igglri,  iggartd,  ‘letter’,  prop,  message Cp.  angaria,  the  first  element  in  Ingram  and  the second  element  in  evangel.  The  sense  develop¬ ment  of  Gk.  ayyapo<;,  resp.  6cyyeXo<;,  from  a Sem.  noun  meaning  ‘hireling’,  may  be  illustrated by  the  phases :  ‘hireling,  hired  messenger,  mes¬ senger’.  Gk.  dyyeXoi;  in  the  sense  of  angel ,  is a  loan  translation  of.  Heb.  mat  dkh,  messenger, divine  messenger,  angel’,  fr.  base  l-'-k,  ‘to  send  . Derivatives:  angel-ic,  adj.,  angelica  (q.v.),  angel- ic-al,  adj.,  angel-ic-al-ly,  adv.,  angel-ic-ize,  tr.  v., angel-ize,  tr.  v.
13872:evanescent,  adj.  —  L.  evanescent,  gen.  -entis, pres,  part  of  evansescere.  See  evanesce  and  -ent. Derivative:  evanescent-ly,  adv. evangel,  n.,  the  gospel.  —  ME.  evangile,  fr.  OF. evangile  (F.  evangile),  fr.  Eccles.  L.  evangelium, ‘gospel’,  fr.  Gk.  eua-j-flXiov,  ‘reward  of  good tidings;  gospel’,  fr.  s6<4yyeXo?,  ‘bringing  good news’,  fr.  eu  (see  eu-)  and  ‘messenger’.
13874:Derivatives:  evangelic  (q.v.),  evangel-ic-ity,  n., evangelist  (q.v.),  evangelize  (q.v.) evangel,  n.,  evangelist.  —  Gk.  euayysko?,  ‘bring¬ ing  good  news’.  See  prec.  word, evangelic,  evangelical,  adj.  —  Eccles,  L.  evange- licus,  fr.  Gk.  cuayyeXtzijC,  fr.  euayyiktov.  See evangel,  ‘gospel’,  and  -ic,  resp.  also  -al. Evangeline,  fem.  PN.  —  F.  Evangeline,  ult.  fr. Gk.  euayy£Xiov,  ‘good  news’.  See  evangel, ‘gospel’,  and  -ine  (representing  L.  -ina). evangelist,  n.  —  F.  evangiliste,  fr.  Eccles.  L. evangelista,  fr.  Gk.  euayyeXiaT7ji;,  fr.  euayye- Xl^ccrflai.  See  next  word  and  -ist.
13875:Derivatives:  evangelist-ic,  adj. evangelize,  tr.  and  intr.  v.  —  OF.  evangeliser,  fr. Eccles.  L.  evangelizare,  fr.  Gk.  euayyeXl^ca&at., ‘to  bring  good  news,  to  preach  glad  tidings’,  fr. euayy^Xtov.  See  evangel,  ‘gospel’,  and  -ize. Derivatives:  evangeliz-ation,  n.,  evangeliz-er,  n. evanish,  intr.  v.,  to  vanish.  —  OF.  esvanir  (F. evanouir).  See  e-  and  vanish.
16468:gospel,  n.  —  ME.  godspel,  gospel,  fr.  OE.  god- spell,  lit.  ‘the  good  message’,  fr.  god,  ‘good’,  and spell,  ‘narrative,  story,  saying,  message’  (see good  and  spell,  ‘charm’).  Gospel  is  prop,  a  loan translation  of  Eccles.  L.  evangelium  (see  evangel). gospelize,  tr.  v.,  to  evangelize,  —  A  hybrid formed  fr.  gospel  with  -ize,  a  suff.  of  Greek origin.
30687:Derivative:  protophyt-ic,  adj. protoplasm,  n.  (biol.)  —  G.  Protoplasma,  lit. ‘first  formed’,  compounded  of  proto-  and  Gk. 7rXdt<j[ia,  gen.  TtXxouxTo?.  ‘anything  molded’, from  the  stem  of  TtXd<7CEi.v,  ‘to  mold’;  see plasma.  The  word  Protoplasma  was  coined  by the  Czech  physiologist  Johannes  Evangelista Purkinje  (1787-1 869)  in  1839  to  denote  the  gelat¬ inous  fluid  found  in  living  tissue.  Next  year this  term  was  taken  over  by  the  German  botan¬ ist  Hugo  von  Mohl  (1805-72)  to  denote  the  ma¬ terial  within  tissues  generally.
37129:Stundism,  n.,  the  doctrine  of  the  Stundists.  — Russ,  shtundism,  a  hybrid  coined  fr.  shtunda (see  next  word)  and  -ism,  a  suff.  of  Greek  origin. Stundist,  n.,  member  of  a  Russian  Evangelical sect.  —  Russ,  shtundist,  a  hybrid  coined,  fr. shtunda,  ‘Stundism’,  fr.  G.  Stunde,  ‘hour,  lesson’, and  -ist,  a  suff.  of  Greek  origin;  so  called  from their  Bible  lessons.  For  the  etymology  of  G. Stunde  see  stound.
39630:Torricellian,  adj.,  of,  pertaining  to,  or  discovered by,  Torricelli.  —  Formed  with  suff.  -an  from  the name  of  the  Italian  physicist  Evangelista  Torri¬ celli  (1608-47).
=== KLN hygiene ===
18409:hygiene,  n.,  the  science  of  health.  —  F.  hygiene, fr.  Gk.  uyieivov,  neut.  of  uytetvfS?,  ‘pertaining to  health,  healthful’,  but  used  by  Aristotle  also as  a  noun  in  the'  sense  of  ‘health’,  fr.  uyifjs, ‘healthy’,  which  stands  for  *su-gwiyes  and  lit. means  ‘living  well’,  fr.  I.-E.  *su-  (Gk.  &-),  ‘well’, whence  also  01.  su-,  OPers.  hu,  OIr.  su-,  so-, ‘well’  (cp.  sundari),  and  *gwiyes,  ‘living’,  enlarge¬ ment  of  *gKi-,  ‘to  live’,  whence  also  Gk.  pro?, ‘life’.  See  bio-  and  cp.  words  there  referred  to. L.  vegere,  ‘to  be  lively,  vigorous,  to  thrive, flourish’,  vegeius,  ‘lively,  vigorous’,  are  not cognate  with  Gk.  uy rijs.  As  a  formative  element, 0-  was  replaced  later  by  eu-  (see  eu-). Derivatives :  hygien-ic,  adj.,  hygien-ic-al-ly,  adv., hygien-ics,  n.,  hygien-ist,  n. bygro-,  before  a  vowel  hygr-,  combining  form meaning  ‘moist,  humid’.  —  Gk.  uypo-,  uyp-,  fr. uypo?,  ‘wet,  moist,  humid’,  rel.  to  L.  (h)umor, ‘fluid,  moisture’.  See  humor  and  cp.  words  there referred  to.
31394:queue,  n.,  1)  (her.)  the  tail  of  a  beast;  2)  plait  of hair  worn  hanging  down  behind ;  pigtail ;  3)  a line  of  persons  waiting  for  their  turn.  —  MF. (=  F.),  fr.  OF.  coe,  fr.  L.  coda,  secondary  form of  cauda,  ‘tail’.  See  caudal  and  cp.  cue,  ‘tail’. Derivative:  queue,  intr.  v. quibble,  n.,  a  petty  evasion.  —  Dimin.  of  obsol. quib,  fr.  L.  quibus,  dat.  or  abl.  pi.  of  qui,  ‘who, which',  used  frequently  in  legal  documents.  See who,  what  and  cp.  quid,  ‘essence’,  quiddity. Derivatives:  quibble,  intr.  v.,  quibbl-er,  n. quick,  adj.,  1)  living,  alive  (archaic)-,  2)  rapid, swift;  3)  prompt;  done  promptly;  4)  alert.  — ME.  quik,  quike,  ‘alive,  lively’,  fr.  OE.  ewieu, ‘living,  alive’,  rel.  to  OS.,  OFris.  quik,  ON. kvikr,  ‘living,  alive’,  Du.  kwi(e)k,  ‘lively,  bright, sprightly’,  OHG.  quec,  chec,  cheh,  MHG.  queck, kec,  ‘lively’,  G.  keck,  ‘bold’,  fr.  Teut.  *q"'iqwa-, ‘living,  alive’,  fr.  l.-E.  *gwigwos,  fr.  base  *gwei-, ‘to  live’,  whence  Goth.  *qius,  gen.  qiwis,  ‘alive’, OI.  jivdh,  ‘alive’,  jfvati,  Avestic  jvaiti,  ‘lives’, OPers.ffva-,  ‘living’,  Gk.  [3toc  (prob.  for  *(3ifoi;, fr.  I.-E.  *gwiwos),  ‘life,Jhe  course  of  life’,  £ijv (fr.  I.-E.  *gwie-),  ‘to  live’,  dorr,,  ‘life’,  L.  vivus, (for  *gwiwos),  ‘living’,  vivo,  there  (for  *gwiwd), ‘to  live’,  vita  (for  *gwiwita),  ‘life’,  OSlav.  iivo, liti,  ‘to  live’,  iivu,  ‘alive’,  iivotu,  ‘life’,  Lith. gyvas,  ‘living,  alive’,  gyratd  '(eternal)  life’,  OIr. biu,  beo,  W.,  Co.  byw,  Bret,  beo,  ‘alive’,  OIr. beothu,  bethu  (for  *biwotut-),  ‘life’,  biad,  'means of  life’,  OIr.  bith,  W.  byd,  'world',  Toch.  A  fol, B  caul,  ‘life’,  A  sofi,  B  saigfe,  'people'  (lit.  ‘the living  ones’),  B  faya/p, ‘he  lives’,  Arm.  keam((ot *gwiya),  ‘I  live’.  Hitt,  huish-  is  not  cognate.  Cp. quitch.Cp.  also  bio-, hygiene,  jiva,  vital  and  words there  referred  to.  Cp.  also  zodiac,  zoetic,  zoo- and  the  second  element  in  usquebaugh,  whisky. Derivatives:  quick,  adv.  and  n..  quick-en,  tr.  and intr.  v.,  quick-ly,  adv.,  quick-ness,  n. quick,  tr.  and  intr.  v.  —  ME.  quiken,  fr.  OE.
37460:sundari,  n.,  name  of  an  East  Indian  tree  ( Heritiera fomes)  —  OI.  sundari,  lit.  ‘beautiful’,  fern,  of sundarah,  a  later  form  corresponding  to  Vedic siinarah,  ‘of  full  vitality’  (cp.  Avestic  hunara-,  of s.m.),  formed  fr.  I.-E.  pref.  *su-,  ‘well,  good, beautiful',  and  base  *ner-,  ‘vital  energy,  vigor'. I.-E.  *su-  appears  also  in  Gk.  u-  in  u-Yir,c, ‘healthy’;  see  hygiene.  I.-E.  *ner-  occurs  also  in OI.  naryab,  ‘virile’,  Gk.  a-vv)p,  ‘man’;  see andro-.
=== KLN swastika ===
13659:jam,  OSla v.jesmi,  Lith.  esmi,  OIr.  am,  Goth,  im, OE.  eom,  earn,  am,  ‘I  am’,  OI.  small,  Gk.  £<jpiv, Ion.  eEpiv,  Dor.  dpi?,  Lith.  esme,  OSla v.jesmii, L.  sumus,  ‘we  are’  (L.  sum,  ‘I  am’,  has  been formed  on  analogy  of  the  pi.  sumus).  Cp.  ab¬ sence,  absent,  -ent,  entity,  essence,  essential,  in¬ terest,  presence,  present,  prosit.  Cp.  also  am,  art, are,  is,  sin,  ‘transgression’,  sooth.  Cp.  also  ety¬ mology,  etymon,  heteroousian,  homoiousian, homoousian,  onto-,  sattwa,  suttee,  swastika, essence,  n.  —  F.,  fr.  L.  essentia,  ‘being  or  essence of  a  thing’,  fr.  essent-,  pres.  part,  stem  of  esse, ‘to  be’;  prop,  loan  translation  of  Gk.  ouctES, ‘essence’.  See  esse  and  cp.  words  there  referred to.  For  the  ending  sec  suff.  -ence.
15626:L.  -ficare,  fr.  -ficus,  fr.  -ficere,  unstressed  form of  facere,  ‘to  make,  do’.  See  -lie,  -fication. fylfot,  n.,  the  swastika.  —  Prob.  for  fill  -  foot  and orig.  denoting  the  device  that  fills  the  foot  of a  painted  window.
17051:hakeem,  hakim,  n.,  in  Mohammedan  countries, a  physician.  —  Arab,  hakim,  lit.  ‘wise’,  from  the stem  of  hakuma,  ‘he  was  wise’,  whence  also hakam,  ‘judge’,  hikmah,  ‘wisdom,  science’,  hak- kama,  ‘he  was  a  physician’,  hukm,  ‘judgment, sentence’,  rel.  to  Heb.  hakham,  ‘he  was  wise’, hakhdm,  ‘skillful,  learned,  wise’,  hokhmdh, ‘wisdom’,  Aram.-Syr.  hakham,  ‘he  was  wise’. See  hokhmah  and  cp.  next  word, hakenkreuz,  n.,  swastika;  used  as  the  emblem  of Nazism.  —  G.  Hakenkreuz,  lit.  ‘hook-cross’.  See hook  and  cross,  n.
37682:swastika,  n.,  a  symbol  in  the  form  of  a  Greek cross  with  the  ends  of  the  arms  bent  at  right angles;  used  as  the  emblem  of  the  Nazi  party. —  OI.  svastikah,  lit.  ‘being  fortunate’,  fr. svastih,  ‘welfare’,  a  word  compounded  of  su-, ‘good,  well',  and  asti,  ‘is’,  which  is  cogn.  with Gk.  eort,  L.  est,  ‘is’  (see  esse);  so  called  be¬ cause  it  was  regarded  as  auspicious, swat,  tr.  v.,  to  strike,  crush.  —  Of  imitative  ori¬ gin.
=== KLN Eugene ===
5981:L.  butyrum,  ‘butter’  (see  butter)  and  suff.  -ic. butyric  acid  (chem.)  —  So  called  by  its  discoverer, the  French  chemist  Michel-Eugene  Chevreul (1786-1889)  because  it  occurs  in  butter.  See prec.  word.
7508:cholesterol,  n . ,  a  fatty  alcohol  ( biochem .)  —  Form¬ ed  fr.  F.  cholesterine,  a  word  coined  by  the French  chemist  Miehel-Eugene  Chevreul  (1786- 1889),  and  -ol,  a  suff.  denoting  an  alcohol.  F. cholesterine  is  formed  fr.  Gk.  yoklj,  ‘gall,  bile’, and  aTEpeoe,  ‘solid’  (see  chole-  and  stereo-),  and is  so  called  because  it  was  originally  found  in gallstones.
9602:chemist  Michel-Eugene  Chevreul  (1786-1889), the  discoverer  of  this  substance  in  1835,  fr.  Gk. xp£aQ,  ‘flesh’,  which  is  cogn.  with  L.  crudus, ‘raw’,  cruor,  ‘thick  blood,  gore’.  See  crude  and chem.  suff.  -ine,  -in,  and  cp.  the  first  element  in creosote  and  the  second  element  in  Pancreas, creation,  n.  —  F.  creation,  fr.  L.  creatidnem,  ace. of  creatid,  ‘a  creating,  producing’,  fr.  creatus, pp.  of  credre.  See  create  and  -ion.
12516:dysgenic,  adj.,  detrimental  to  the  hereditary constitution  of  the  race;  opposite  to  eugenic.  — Formed  fr.  dys-  and  -genic.  Cp.  eugenic, dyslogistic,  adj.,  unfavorable.  —  A  blend  of  dys- and  eulogistic.
13780:Eugene,  masc.  PN.  - —  F.  Eugene,  fr.  L.  Eugenius, fr.  Gk.  Euy^toi;,  fr.  aiiyevi^,  ‘well  bom’.  See eugenic  and  cp.  Eugenia.
13781:Eugenia,  fem.  PN.  —  L.,  fr.  Gk.  Euyevla,  lit.  ‘no¬ bility  of  birth’,  rel.  to  Euysvio?.  See  prec.  word, eugenic,  adj.,  improving  the  human  race;  per¬ taining  to  the  improvement  of  the  human  race. —  Gk.  euYcvfji;,  ‘well  born’,  fr.  eu  (see  eu-)  and Y^voi;  ‘race,  descent,  gender,  kind’,  See  genus and  cp.  Eugene,  Eugenia, eugenics,  n.,  the  study  of  the  improvement  of  the human  race  by  selection  of  the  parents.  — Coined  by  Sir  Francis  Galton  (1822-1911)  in 1883  from  the  adjective  eugenic.  For  the  ending see  -ics.
13839:europium,  n.,  name  of  a  rare  metallic  element (chem.)  —  ModL.,  named  by  its  discoverer,  the French  chemist  Eugene  Demarpay  (1852-1903) in  1896  after  the  continent  Europe.  For  the  end¬ ing  of  europium  see  suflf.  -ium.
15966:-genic,  combining  form  meaning  ‘producing’,  as in  endogenic,  eugenic.  —  Formed  with  suff.  -ic fr.  nouns  ending  in  -gen  or  -geny. geniculate,  geniculated,  adj.,  having  knots  or joints.  —  L.  geniculatus,  ‘having  knots  or  joints’, fr.  geniculum,  ‘little  knee;  knot  on  the  stalk  of a  plant’,  dimin.  of  genii,  ‘knee’.  See  genu  and the  suff.  -cule,  and  -ate,  resp.  also  -ed. Derivatives:  geniculat-ed,  adj.,  geniculate-ly, adv.,  geniculation,  n.
16003:Derivatives:  genuine-ly,  adv.,  genuine -ness,  n. genus,  n.,  a  class;  a  kind,  sort.  —  L.,  ‘birth, descent,  origin,  race,  sort,  kind,  class;  sex, gender’,  fr.  I.-E.  base  *gen-,  *gene-,  *geno-, *gn-,  ‘to  beget,  bear,  bring  forth;  produce’, whence  also  L.  gens,  ‘race,  clan,  nation,  people  , gignere  (for  gi-gn-ere),  ‘to  beget,  bear,  bring forth,  produce’,  ndsci  (for  *gndsci),  ‘to  be  born’, natus,  gndtus,  ‘born’,  natio ,  ‘birth,  breed,  lace, people,  nation’,  natura,  ‘birth,  nature’,  Gk. Y^voi;,  ‘race,  descent,  gender,  kind’,  YiYvea9'al> (for  Yi-YVE~a^alj’  ‘to  1)0  born’  b^01™’  haP~ pen’,  ybvzait^,  ‘origin,  source,  birth,  race,  des¬ cent’,  ymzd.,  Yevefi>  Yeverk  b'rtb’>  Y*vrrfa> Yev6tci>p»  y£-JET71?>  begetter,  father,  ancestor  , YovEu?,  ‘father,  ancestor’,  yovr),  ‘that  which  is begotten,  offspring;  that  which  generates,  seed, semen;  genitals;  the  act  of  generation;  race, family*,  ybvoz,  ‘that  which  is  begotten,  child, offspring;  procreation;  race,  birth,  descent; seed,  semen;  genitals’,  -yvtqtoi;  (in  compounds), ‘born’,  yvosxb^,  ‘kinsman,  brother  ,  OI.  janati , ‘begets,  bears’,  janitor-,  ‘begetter,  father’,  jani- man-,jdnman-,  ‘birth’,  jdnahjvace,' Jatah,  born  , jdtih,  ‘birth,  family’,  jhatih,  ‘kinsman’,  Avestic zizan'nti,  ‘they  bear’,  zazfnti,  ‘they  beget’,  zala-, ‘born’.  Arm.  cnanim  (aor.  cnay),  ‘I  bear;  I  am born’,  Lett,  znuots,  ‘son-in-law,  brother-in-law  , Lith.  gentis,  ‘kinsman’,  OIr.  ro-genar,  ‘I  was bom’,  W.  geni,  ‘to  be  bom’.  Cp.  Antigone,  ar- cbegonium,  benign,  cognate,  congener,  connate, degenerate,  engine,  epigone,  Erigenia,  eugenic, -gen,  gendarme,  gender,  gene,  genealogy,  gener, general,  generate,  generation,  generous,  genesis.
16339:glycerin,  glycerine,  n.  (chem.)  —  F.  glycerine, coined  by  the  French  chemist  Michel-Eugene Chevreul  (1786-1889)  fr.  Gk.  yX'Jxepic,  ‘sweet’, fr.  yXux'jc;,  ‘sweet’.  See  glyco-  and  chem.  suff.
```


## [2026-09-14T03:09:44.880Z] TOOL CALL #13: Bash

```json
{
 "command": "ls site/pages/486.jpg 2>/dev/null; pdftoppm -f 486 -l 486 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg486 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg486.png",
 "description": "Render page 486"
}
```


### [2026-09-14T03:09:46.731Z] TOOL RESULT

```
site/pages/486.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 89081 Sep 13 23:09 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg486.png
```


## [2026-09-14T03:09:46.913Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN GOOD section ===\"\ngrep -n \"16\\.71 GOOD\\|16\\. 71 GOOD\\|^16.71\" SYN.txt | head\ngrep -n \"GOOD (adj\" SYN.txt | head\necho \"=== SYN vohu ===\"\ngrep -n \"vohu\" SYN.txt | head",
 "description": "Grep Buck for GOOD"
}
```


### [2026-09-14T03:09:46.998Z] TOOL RESULT

```
=== SYN GOOD section ===
27469:16.71 Goop
29618:16.71 GOOD (adj.)
29618:16.71 GOOD (adj.)
=== SYN vohu ===
5427:Goth. 5/6, Lith. kraujas ae ec ee) ON 3s Lett. asins Lat. sanguts, cruor Dan. blod ChSl.  kritvy It. sangue Sw. blod SCr.  krv Fr. sang OE blod Boh.  krev Sp. sangre ME _sblode Pol. krew Rum. singe NE blood (gore) Russ. krov’ Tr. fuil, crit Du. bloed Skt. asan- (Ved.), rakta-, Nir. futl, cro OHG _bluot rudhira-, ete, W. gwaed (crau) MHG bluot Av. vohuni- Br. gwad NHG  Dlut
5446:Av. vohuni- (NPers. xin ‘blood’), etym.? Barth. 1434.
29654:Skt. vasu- (Vedic in this sense; later mostly as neut. sb. ‘goods, wealth’), AY. vanhu-, vohu- (OPers. only in prop c names, as Dadraya-vaus, Vau-misa) : Gall. -vesus (in Bello-, Sigo-vesus, ete), Gme. Wisu-rth, -mar, Wisi-Gothae, ett,
```


## [2026-09-14T03:09:54.733Z] TOOL CALL #15: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg486.png"
}
```


### [2026-09-14T03:09:55.429Z] TOOL RESULT

```

```


## [2026-09-14T03:09:55.427Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:09:57.505Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {if (NR>=1) print NR\": \"substr($0,1,0)}' SYN.txt >/dev/null\n# find leaf containing line 29654\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:29650])\nprint('leaf#', t[:idx].count('\\f')+1)\nEOF\necho \"--- context ---\"\nsed -n '29610,29670p' SYN.txt",
 "description": "Read page image and Buck context"
}
```


### [2026-09-14T03:09:58.645Z] TOOL RESULT

```
leaf# 1264
--- context ---
titi (Pol. odpuscié bibl. in this sense), epds. of pustiti ‘let go’ (11.34).
Chl. prostiti (Supr. ‘set free, release’
and ‘forgive’), SCr. oprostiti, Russ. pro- stit’ (Boh. prostiti ‘set free’), deriv. of
ChSl. prostté ‘simple, upright’, etc., for which see 12.73.
Pol. przebaczyé, epd. of baczyé ‘be at- tentive, take heed’ with prze- ‘over across’, semantic development through ‘overlook’ (cf. przemilczec ‘pass over in silence’). But also wybaczyé, with per- fect. wy-. Briickner 10.
7. Skt. ksam- ‘have patience, endure’, hence ‘forgive’, etym.?
Skt. mrd-, Av. marazda- ‘be gracious, forgive’ (cf. NPers. amurzidan ‘forgive’), fr. an extension of Skt. mrj-, Av. maraz- ‘rub, stroke’. Walde 2.298. Barth. 1175.
Av. apaharaz- (‘remit’ a penalty, Vd. 5.26), cpd. of harez- ‘let go, release’ (11.34). Barth. 586 s.v. 4i@a-, 1793.
16.71 GOOD (adj.)
Gi Bice fede (ct-) Gott gods, piupeigs, séls er eee labas
KaNbs, dyads goor UUs AEACS Lat. bonus Dan. god ChSl.  dobrit, blagit It. buono Sw. god SCr. dobar Fr bon OE god Boh. dobry *. bueno ME gode Pol. dobry ; um, bun NE good Russ. chorosij Mi fa fe s0-) Du. goed Skt.  sddhu-, bhadra-, vasu-
* maith (deagh-, so-) OHG quot (su-) ¥, da, mad (hy-) MHG guot Ay. vawhu- (hu-), OPers.
™ ‘mat NHG gut naiba-
t Ant 4 aa 1s understood as the most ge- | adjs. (e.g. Lat. bene : bonus) or be quite fae nee of approval, by no means | unrelated (e.g. NE well, NHG wohl, ih *¢ to moral qualities, All the | etc., general Gmc.), and the comps. and
we doubtless more specific origi- ee ay among those the etymology e ‘Rttings clear We note as sources such ‘orderly cg nee right’, ‘beautiful’, rtain Well” ae ortant prefixes for ‘zood-, treatment more comprehensive Which clude also the advs., & with the common
ent would in may belon
superls. For the adjs. for ‘good’ and ‘bad’ are among those in which irregular (supplementary) comparison is most widespread (e.g. Lat. bonus, melior, op- timus, NE good, better, best, etc. general Gmce.).
1. Prefix IE *su-, Walde-P. 2.512. Pedersen 2.9.
Skt. su-, Av. hu-; Grk. b- in dyes ‘in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ats pa cele
ses =e Se
. |
t Digitized by Arya Samaj Foundation Chennai and eGangotri
1176 SELECTED INDO-EUROPEAN SYNONYMS
good health’; Gall. Su- in proper names, Ir. so-, W. hy-. For traces in Balto- Slavic, cf. Fraenkel, Mélanges Peder- sen 443 ff.
Grk. e-, the semantic equivalent (eb- related to dvco- precisely as Skt. su- to dus-), beside Hom. éts, #bs ‘good, brave’, prob. : Hitt. assus ‘good’ fr. IE *es- ‘be’. Friedrich, IF 41.370 f.
2. Grk. dya6és, etym. disputed, perh. : dya- ‘very’, &yapar ‘admire’, etc. Boi- sacq 4f.
Grk. xadés, mostly ‘beautiful’ (16.81), but often also ‘good’, and so reg. in NG, where aya6és is less common.
3. Lat. bonus (> Romance words), OLat. duenos, duonus, etym. dub. Walde-P. 1.778. Ernout-M. 114. Walde-H. 1.111.
4. Ir. maith, W. mad, Br. mat, Corn. mas (cf. Gall. Teutomatos), prob. : Lat. Matita ‘Goddess of morning’, matirus ‘seasonable, early’, md@ne ‘morning’, OLat. manus ‘good’. Walde-P. 2.220 f. Ernout-M. 588. Walde-H. 2.54.
Ir. dag-, deg-, NIr. deagh-, W. da (Br. da in phrases da eo d’in ‘je veux bien’), Gall. Dago-vassus, etym. dub. Walde-P. 1.784. Pedersen 1.39.
5. Goth. gods, ON godr, OE gid, etc., general Gme.:OHG gigat ‘fitting’, MLG gaden ‘fit, please’, OF geador ‘to- gether’, etc., ChSl. godii ‘(proper) time’, u-goditi ‘please’, etc. Walde-P. 1.532, Feist 218. Falk-Torp 336.
Goth. piup neut. (renders 76 é&yabdy), whence also piupeigs (freq. for ayaés) : ON yor ‘kind’, OF gepiede ‘good, vir- tuous’, perh. fr. the root in Lat. tuérz ‘re- gard, protect’, tatus ‘safe’, etc. Walde- P. 1.705 f. Feist 498. Falk-Torp 1306.
Goth. séls ‘good, kind’ (aya6bs, xpn- o7és), with sb. sélei : OE ges@lig ‘blessed, happy’, etc., outside connections dis- puted (16.24).
6. Lith. geras : girti ‘praise’, Skt. gr-
‘sing, praise’, etc. (16.79), 1.686. Buga, Kalba ir Secor Meee
Lith. labas (usual only in greetings a labas rytas, laba diena ‘good Mornin 3 good day’), Lett. labs, OPruss, rae Lith. ee ‘possessions, riches’, lobtj ‘wet rich’, Skt. labh- ‘seize, grasp’
2.385. gente or
7. ChSl. dobrii, ete., genera] Slavic (Russ. dobryj now in phrases like ‘good day’, but mostly ‘kind’) : po-doba jesttt ‘it is becoming’, po-dobiti ‘make fitting’, Goth. Gutatan ‘happen’, OF ge-dafen becoming’, etc. Berneker 208-5, Walde-P. 1.824 f.
ChSl. blagt (reg. for dyaGss and xpn- orés ‘good’ in moral sense, cf. Jagié, Ent- stehungsgesch. 326), in modern Slavic mostly ‘gentle, blessed, noble’, etc., never general for ‘good’, etym. dub. Walde-P. 2.182. Berneker 69.
Russ. chorosij (has displaced dobry; as the common word for ‘good’), orig. ‘or- derly, neat’, hypocoristic formation fr. ORuss. choronent, pple. of choroniti ‘put in order’: ChSl. chraniti ‘guard, keep’. Berneker 397. Jagié, Arch. sl. Ph. 6.282 ff.
8. Skt. sddhu-, orig. ‘straight, right, ready’, fr. sadh- ‘reach one’s goal, ac- complish, guide aright, etc.’. Walde-P. 2.450.
Skt. bhadra-, also ‘blessed, auspicious, fair’, prob. : Goth. batiza ‘better’, ba- tists ‘best?. Walde-P. 2.151f. Falk- Torp 67.
Skt. vasu- (Vedic in this sense; later mostly as neut. sb. ‘goods, wealth’), AY. vanhu-, vohu- (OPers. only in prop c names, as Dadraya-vaus, Vau-misa) : Gall. -vesus (in Bello-, Sigo-vesus, ete), Gme. Wisu-rth, -mar, Wisi-Gothae, ett,
Ir. feib ‘excellence’ (dat. sg.), W- a ‘fine, splendid, gay’, etc. Wa. 1.310. site
OPers. naiba (clearly ‘g00
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
igitized by Arya Samaj Foundation Chennai and eGangotri
. TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1177 3 and so, rather than For the numerous other Indo-Iranian 7 jnscr- 4 5) = ¢ ’ ¢ J Dsiva y, elsewhere) : Ir. noib ‘holy’, | words that may be used for ‘good’ (and ipeautifu ’- bho-) fr, the root seen in Ir. | ‘bad’), cf. Schwyzer, Die altindischen und b. ( tia ce’, Lat. nitére ‘shine, glit- | altiranischen Worter fiir gut und bése, niam Pade. 9.321. Festgabe Kaegi 12 ff. ter’: 16.72 BAD 4s (8v0-) Goth. ubils Lith. blogas, negeras, piktas Grk. og ON vandr, illr, daligr Lett. sltkts, nelabs, l’auns NG Bae i Dan. ond, slet, slem, daarlig Chsl.  zitlit Lat. a tivo, malo Sw. ond, elak, ddlig SCr.  nevaljan, zao It. Eats OE yfel (earg) Boh. &patny, zly Fr. mal(o) ME _ wvel, ill, badde Pol. aly Be wil NE bad (ill, evil) Russ. plochoj, chudoj, dur- He Pie (Grach-, do-) Du. slecht, kwaad, erg noj Nir. ole (droch-, do-) OHG ubil Skt.  pdpa-, asddhu-, abha- WV * drwg (dy-) MHG tibel, bese dra- (dus-) Br. fall, gwall, drouk NHG schlecht, schlimm Ay. aka-, aya-, avawhu- : ; (bése, tibel, arg) (dus-)
For ‘bad’ as the opposite of ‘good’ there are equally generic words in some of the IE languages, but in others a vari- ety of terms partly differentiated in feel- ing and according to the object qualified, so that it may be difficult to say which is the more nearly generic. Some are mainly ‘evil, wicked’ in the moral sense.
An adj. denoting any undesirable quality, physical or mental, any oppro- brious epithet, may easily be generalized to ‘bad’. Thus, either in earlier attested meanings or in cognates, ‘disgusting, Ugly, defective, faulty, weak, timid, eee ete. In some languages neg. Pas. of words for ‘good’ are in fairly Common use, banca egteement between different tts’, maoge : is in a prefix for ‘ill-,
PAnian, eee in Greek and Indo- iit €n in the same branch there
Y great i : ; Words for ‘good’. diversity than in the
Iz it . P, ig ag “dus- ‘ill-, mis’. Walde-
dersen 2.9,
TK. dug- (dug. 3 ;7? TE: OPP. of eb-; Skt. dus- 0
*0
duj : ") dur-), Ay. dug- (duz-), reg.
» W-; Gme. tuz- in Goth. tuz-
werjan, ON tor-iryggja ‘mistrust, doubt’, etc.; Ir. do- in do-cruth ‘ugly’ (vs. so- cruth), W dy- in dybryd ‘sad’.
```


## [2026-09-14T03:10:10.848Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nprint(d['KLN'].get('page_offset'));print(d['KLN'].get('lookup_hint'))\nprint('SYN off:', d['SYN'].get('page_offset'))\nprint('BRT off:', d['BRT'].get('page_offset'))\nprint('BQT off:', json.dumps(d['BQT'],ensure_ascii=False)[:2000])\n\"",
 "description": "Check page offsets"
}
```


### [2026-09-14T03:10:11.958Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
SYN off: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BRT off: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
BQT off: {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volu
```


## [2026-09-14T03:10:12.862Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Klein Darius / Bahman ===\"\ngrep -n -i \"Darius\\|Bahman\\|Behistun\" KLN_1966.txt | head -10\necho \"=== Klein besht/best ===\"\ngrep -n \"^best,\\|best,  adj\" KLN_1966.txt | head -5",
 "description": "Grep Klein Darius etc"
}
```


### [2026-09-14T03:10:12.985Z] TOOL RESULT

```
=== Klein Darius / Bahman ===
1147:abductor,  n.  ( anat .)  —  Medical  L.,  name  of  a muscle,  lit.  ‘that  which  leads  away’,  fr.  L.  ab¬ ductus,  pp.  of  abducere,  ‘to  lead  away’.  See  ab¬ duct  and  agential  suff.  -or. abeam,  adv.,  at  right  angles  to  the  keel  ( naut .)  — Lit.  ‘on  the  beam’,  fr.  a-,  ‘on’,  and  beam, abecedarian,  adj.,  elementary,  rudimentary.  — ML.  abecedarius,  ‘pertaining  to  the  alphabet’, a  word  formed  from  the  names  of  the  first  four letters  of  the  alphabet.  For  the  ending  see  suff. -arian.
1148:abecedarium,  n.,  an  ABC  book.  —  ML.,  prop, neut.  of  the  adjective  abecedarius,  used  as  a noun.  See  prec.  word.
3981:aumildar,  n.,  a  revenue  collector  in  India.  — Hind.  ‘ amaldar ,  lit.  ‘one  holding  an  office’,  a hybrid  coined  fr.  Arab,  'dmal,  ‘work’  (see  au¬ mil),  and  the  Persian  agential  suff.  -dar,  meaning ‘holder,  possessor’,  which  is  rel.  to  Avestic darayeiti,  ‘holds,  supports’,  OI.  dhardyati,  of s.m.,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold,  support’, whence  also  L.  firmus,  ‘firm,  steadfast,  stable, strong’.  See  firm,  adj.,  and  cp.  the  first  element in  Darius.  Cp.  also  the  second  element  in  baha- dur,  chobdar,  chokidar,  dizdar,  dufterdar,  en- amdar,  foujdar,  havildar,  jaghiredar,  jemadar, killadar,  ressaldar,  silladar,  sirdar,  subahdar, tahsildar,  talukdar,  thanadar,  zemindar, auncel,  n.,  a  weight  used  in  England  in  the  Middle Ages.  —  AF.  auncelle,  fr.  It.  lancella,  dimin.  of lance,  ‘balance’,  fr.  L.  lanx,  gen.  lands,  ‘plate, dish;  scale  of  the  weighing  machine’.  See  bal¬ ance.  The  loss  of  the  initial  l  in  E.  auncel  is  due to  the  circumstance  that  the  initial  /  in  It.  lan¬ cella  was  mistaken  for  the  It.  def.  art.  V  and consequently  dropped.
4678:beheld,  past  tense  and  pp.  of  behold, behemoth,  n.,  a  huge  beast,  probably  the  hippo¬ potamus.  —  Heb.  behemdth,  used  in  the  sense of  a  plural  of  intensity  of  blhemah,  ‘beast’  (see Job  40 : 1 5-24).  The  assumed  connection  of  Heb. behemoth  with  Egypt,  p-ehe-mau,  ‘ox  of  the water’,  was  justly  rejected  by  W.Max  MUller. behen,  n.,  the  plant  Centaurca  behen.  —  Arab. bahman,  in  vulgar  pronunciation  behmen,  fr. Pers.  bahman,  a  kind  of  root  resembling  a  large radish.
5361:borax,  n.,  a  white  crystalline  salt  used  as  a  flux and  an  antiseptic.  —  F.,  fr.  Arab,  bauraq (VArab.  boraq),  fr.  Pers.  burah. bordage,  n.,  the  tenure  of  a  border  ( Feudal  sys¬ tem),  —  ML.  bordagium.  See  next  word  and  -age. bordar,  n.,  tenant  ( Feudal  system).  —  ML.  bor- darius,  fr.  borda,  ‘cottage’,  fr.  OF.  borde,  which is  a  Teut.  loan  word.  See  board,  ‘table,  plank’, and  cp.  border.
6168:caldarium,  n.,  the  hot  room  in  the  Roman  bath.  — L.,  prop.  neut.  of  the  adj.  calidarius,  calddrius, ‘pertaining  to  warming’,  used  as  a  noun,  fr. calidus,  ‘hot’.  See  next  word, caldron,  cauldron,  n.  —  ONF.  cauderon,  caudron (corresponding  to  OF.  chauderon,  F.  chaudron), formed  fr.  OF.  caudicre  (F.  chaudiere),  fr.  Late L.  caldaria,  ‘caldron’,  fr.  L.  calidarius,  caldarius, ‘pertaining  to  warming’,  fr.  calidus,  caldus,  ‘hot’, fr.  calere,  ‘to  be  warm’,  which  derives  fr.  I.-E. base  *kel-,  ‘warm’,  whence  also  Lith.  s[lu,silti,  ‘to become  warm’,  siltas,  ‘warm  ,  situs,  more  exact¬ ly  stilus,  ‘August’  (lit.  ‘the  warm  month’),  W. clvd,  ‘warm’  (whence  MW.  claer,  cluyar, ‘warm’),  OI.  sarad-,  ‘autumn’,  Avestic  sarf6, ‘year’,  ModPers.  sal,  of  s.m.  Cp.  It.  caldaia, Rum.  caldare,  OProveng.  caudera,  Catal.  cal- dira,  Sp.  caldera.  Port,  caldeira,  ‘caldron’,  which all  derive  fr.  VL.  caldaria.  Cp.  calefacicnt,  ca¬ lenture,  calescence,  callant,  calorescencc,  calo¬ ric,  caudle,  chafe,  chaldron,  chauffeur,  chawdron, chowder,  rechauffe,  scald,  nonchalant.  For  prob.
6929:cellar,  n.  —  ME.  celler,  fr.  OF.  celier  (E.  cellier), fr.  L.  cedarium,  ‘a  receptacle  for  food,  pantry’, prop.  neut.  of  the  adjective  cedarius,  ‘pertaining to  a  storeroom’,  used  as  a  noun.  fr.  ceda.  Cp.  It. cellaio,  OProven?.  celier,  Catal.  celler,  Sp.  cillero and  Port,  celleiro,  ‘storeroom",  and  see  cell. Derivatives  \  cellar, cellar-age, n.,cellar-er,n. cellaret,  n.  —  Diminutive  formed  fr.  cellar  with sulf.  -et.
10341:dargah,  also  durgah,  n.,  the  shrine  of  a  Moham¬ medan  saint  in  India.  —  Hind,  dargah,  fr.  Pers. dargah,  lit.  ‘royal  gate’.  Pers.  dar,  ‘door,  gate’, is  rel.  to  Avestic  dvarlm  (acc.  sing.)  ,‘gate, court’,  OPers.  duvaraya-,  ‘at  the  door’,  and  to OI.  dvdrah,  ‘door’.  See  door  and  cp.  the  first element  in  durbar  and  in  durwaun. daric,  n.,  an  ancient  Persian  gold  coin.  —  Fr.  Gk. Aapeix6g,  also  written  Aapixoc,  Aapr/6p,  fr. Aapeiog,  ‘Darius’,  hence  lit.  meaning  ‘of,  or pertaining  to,  Darius’.  See  next  word  and  -ic. Darius,  masc.  PN.  —  L.  Darius,  fr.  Gk.  Aapeto;, fr.  OPers.  Darayava(h)ush  (whence  also  Heb. Darydwesh),  a  compound  lit.  meaning  ‘he  who holds  firm  the  good’.  The  first  element  of  this compound  derives  from  the  stem  of  OPers. darayamiy,  ‘I  hold’,  fr.  I.-E.  base  *dher(e)-,  to hold’;  see  firm,  adj.,  and  cp.  the  second  element in  aumildar  and  in  words  there  referred  to.  The second  element  in  OPers.  Daraya-va(h)ush means  ‘the  good’,  and  is  related  to  Avestic vahhu,  vohu,  OI.  vasuh,  ‘good’.  Cp.  prec.  word, dark,  adj.  —  ME.  deork,  derk,  darke,  fr.  OE. deorc,  re!  to  OHG.  tarchanjan ,  ‘to  hide,  con¬ ceal',  MHG.  terken,  ‘to  make  dark,  soil’,  and cogn.  with  Lith.  darga,  ‘rainy  weather’,  and prob.  also  with  OIr.  derg,  ‘red’.
12291:dromedary,  n.  —  OF.  dromedaire  (F.  dromadaire), fr.  Late  L.  dromeddrius  ( camelus ),  fr.  dromas , gen.  -adis,  ‘running’,  fr.  Gk.  Spoprap,  gen.  -aSop, of  s.m.,  which  is  rel.  to  Spapiciv,  ‘to  run’, 8£8popa,  ‘1  ran’,  Spoprop,  ‘a  running,  course, race,  racecourse',  fr.  I.-E.  base  *drem-,  ‘to  run  , whence  also  OI.  dramati,  ‘runs’.  Base  *drem-  is  a collateral  form  of  base  *dra-,  ‘to  move  quickly,  to run’,  whence  OI.  drdti,  ‘runs,  hastens’,  Gk.  dbroSi- Sp&axeiv,  ‘to  run  away’  (with  reduplication  of base  *8pa-).  Spaaed?,  ‘a  running  away,  flight’, iiSpaaxop,  ‘not  inclined  to  run  away’,  ’ASpao- Tcia,  ‘Nemesis’,  lit.  ‘from  whom  there  is  no escape’,  and  prob.  also  ON.  titra,  OHG.  zit- taron,  ‘to  tremble’.  Cp.  Adrastea,  -drome, Dromiacea,  Dromiceius,  dromond,  and  the second  element  in  anadromous,  Boedromion, catadromous,  hippodrome,  lampadedromy,  loxo- dromic,  palindrome,  prodrome,  syndrome.  Cp. also  teeter.  —  The  change  of  a  to  e  in  Late  L. dromeddrius  is  due  to  the  influence  of  Latin words  ending  in  -edarius,  as  essedarius,  ‘a  fighter in  a  British  or  a  Gallic  war  chariot’  (see  es.se- dum),  veredarius,  ‘post  boy,  courier’  (fr.  veredus, ‘a  swift  horse’).  F.  dromadaire — with  a  in¬ stead  of  e — has  been  refashioned  after  Gk. Spopuxp.
14778:firm,  adj.  —  ME.  ferme,  fr.  OF.  (=  F.)  ferme,  fr. L.  firmus,  ‘firm,  steadfast,  stable,  strong’,  rel. to  fere,  ferme,  ‘nearly’,  prob.  also  to  fretus, ‘relying  on’,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold, support’,  whence  also  OI.  dharayati,  ‘he  holds, supports  ,  dharanah,  ‘holding’,  dhdrmah,  ‘cus¬ tom,  law’,  Avestic  darayeiti,  ‘he  holds,  sup¬ ports’,  OPers.  darayamiy,  ‘I  hold’,  Gk.  ffpavo?, bench ,  ffpijvu^,  ‘footstool’,  Hpovo ‘seat’.  Ion. ffpr]<jaaffai  (aor.),  ‘to  sit  down’,  possibly  also and  Ikparrov,  ‘servant,  attendant’.  Cp. firm,  n.,  firmament,  affirm,  confirm,  infirm,  farm, frenum,  refrain,  v.  Cp.  also  therapeutic,  throne, thorax,  dharma,  dhama,  the  first  element  in Darius  and  the  second  element  in  aumildar  and in  words  there  referred  to.
=== Klein besht/best ===
4827:best,  adj.  —  ME.,  fr.  OE.  best,  dissimilated  fr. betst,  rel.  to  ON.  beztr,  Du.  best,  OHG.  be^isto, MHG.,  G.  best,  Goth,  batists,  ‘best’,  OE.  batian, ‘to  become  better’,  bot,  ‘remedy,  cure,  improve¬ ment,  compensation’,  and  possibly  cognate  with OI.  bhadrah,  ‘favorable,  good’,  Avestic  hubadra-, lucky’.  Cp.  better.  Cp.  also  batten,  ‘to  grow fat’,  boot,  ‘advantage’.  For  the  dissimilation  of
```


## [2026-09-14T03:10:20.144Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (4678,10341,13764,18409,37682,13780,13872):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    leaf=t[:idx].count('\\f')\n    print(ln, 'leaf', leaf, '-> printed p ~', (leaf-12)*2, 'or', (leaf-12)*2+1)\nEOF",
 "description": "Compute Klein page numbers"
}
```


### [2026-09-14T03:10:21.321Z] TOOL RESULT

```
4678 leaf 95 -> printed p ~ 166 or 167
10341 leaf 221 -> printed p ~ 418 or 419
13764 leaf 298 -> printed p ~ 572 or 573
18409 leaf 407 -> printed p ~ 790 or 791
37682 leaf 823 -> printed p ~ 1622 or 1623
13780 leaf 298 -> printed p ~ 572 or 573
13872 leaf 300 -> printed p ~ 576 or 577
```


## [2026-09-14T03:10:30.233Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (95,221,298,407,823):\n    for j in (i,):\n        s=leaves[j]\n        nums=re.findall(r'\\b(\\d{2,4})\\b', s[:300]+' ||| '+s[-300:])\n        print(i, repr(s[:120]), '...', repr(s[-120:]))\n        print()\nEOF",
 "description": "Check page number markers in Klein leaves"
}
```


### [2026-09-14T03:10:31.339Z] TOOL RESULT

```
95 '.  bed,  Swed.  bddd,  MLG.,  MDu. bedde,  Du.  bed,  OHG.  betti,  MHG.  bette,  bet, G.  Belt,  Goth,  badi,  ‘bed’,  ' ... 'he  sense of  a  plural  of  intensity  of  blhemah,  ‘beast’  (see Job  40 : 1 5-24).  The  assumed  connection  of  He'

221 '��.\nDerivative:  dandruff-y,  adj. dandy,  n.,  a  fop.  —  Fr.  Dandy,  a  var.  of  St.  An¬ drews.  The  name  Andrew' ... 'er’,  fr.  Gaulish  L.  der-\nbita,  ‘tetter’,  which  is  rel.  to  W.  darwyden, MBret.  daroueden,  ModBret.  dervoede'

298 '  See  prec. word.\nEtta,  fern.  PN.  —  Orig.  used  only  as  dimin.  of\nHenrietta.\n-ette,  suff.  used  to  form  nou' ... '  of  di¬ gestion’,  fr.  e8  (see  eu-)  and  t-ettto:;,  ‘cooked’, verbal  adj.  of  7x£a<jetv,  ‘to  cook’.  See\npeps'

407 ' (fr.  L.  -dsns).\nhydroxide,  n.,  a  compound  containing  bydroxyl (chem.)  —  Compounded  of  hydr(ogen),  ox(ygen) ' ... 'a<poi;,  fr.  ypo^stv,  ‘to  write’.  See hymn  and  -graph.\nhymnography,  n.,  1)  composition  of  hymns ; writing  ab'

823 ", orig.  ‘of  the  color  of  dirt',  fr.  I.-E.  base  *  sword-, ‘dirty,  dark,  black’,  whence  also  sordes,  ‘dirt" ... 'n,  fr.  OHG.  swintilon,  ‘to  swoon; to  be  dizzy’,  freq.  of  swintan  (whence  MHG. swinden,  G.  schwinden),  ‘to'
```


## [2026-09-14T03:10:54.593Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3\necho \"---\"\ngrep -c \"\" BQT_v1_pages.txt\necho \"=== search اردیبهشت ===\"\ngrep -n \"اردیبهشت\\|ارديبهشت\" BQT_v1_pages.txt | head -5\necho \"=== بهشت ===\"\ngrep -n \"بهشت\" BQT_v1_pages.txt | head -5\necho \"=== بهمن ===\"\ngrep -n \"بهمن\" BQT_v1_pages.txt | head -5",
 "description": "Grep Borhan vol 1"
}
```


### [2026-09-14T03:10:54.718Z] TOOL RESULT

```
---
32486
=== search اردیبهشت ===
10630:۵ اردیهشتگان - جشنی که ابرآنیان‌باستان در روز اردیبهشت (سوم) از ماه
28711:اردیبهشت ماه ۱۳۱۱ بزدگردی. چايشانة بانك ملی ابران.
=== بهشت ===
3385:چند شهر بوده است که‌آن بلخ وبخارا وبدخشان ومروانت؛ و بعضی گوبند دری زبان اهل بهشت
10001:گویند , خواه کدوی فلبه و خواه کدوی‌غلیان بهشت را کر ی رآ
10579:از ۵ یبهشت * « بن‌اول » بمعنیآتش
10584:ندييي آمور و مصالح ماه اردی بهشت و روز
10585:اردی‌بهشت تملق بدو دارد » و بتابر فاعدث کلی
=== بهمن ===
1561:در غیاثاللفاث ذیل«بهمنچه»آمده: «بفتح‌اول وسکون‌ثانی وفتح میم وسکون
1562:نون و کسر‌جیم فارسی و فتح فون ۰ نام عید که بروز دوم بهمن‌ماه کنند » و روزدوم
1563:هرماه شمسی را درپارسی نیز بهمن نام است» چون نام ماه و نام روز مطابق‌افتد در
1564:آن روز عید وجشن میکنند؛ چون درروز بهمن ( از ) ماه بهمن جشن کنند واقسام
1565:طعامها پز ند ۰۰۰ بهمین جهت جشن دوز بهمن را همنچه گویند ۰»
```


## [2026-09-14T03:10:58.367Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count('\\f'))\nleaves=t.split('\\f')\nprint('leaves', len(leaves))\nprint(repr(leaves[1][:200]))\nEOF\nhead -5 BQT_v1_pages.txt",
 "description": "Inspect BQT vol1 structure"
}
```


### [2026-09-14T03:10:59.428Z] TOOL RESULT

```
formfeeds 776
leaves 777
'۱ ۵ ۱! ۱\n7 موم ۳ لام\nم ۱ 0 و طق صفرررنیاعدریرماروی\n۰ ۱ "۳\n۳\nم و اس مر هر وه او\n7 رین خلت ریز یتایب بره ات\nلف\u200cبال ۶۲ .یرک\nا اند کل داي رشب , رمع\nفان تا تا\nرن 9 3\nکرحم تن\nاد شش مرا\nمو رم | مر\nوک رهب اه '
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
```


## [2026-09-14T03:11:02.769Z] TOOL CALL #23: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:322 2>&1 | head -60",
 "description": "Fetch BQT page 322"
}
```


### [2026-09-14T03:11:03.971Z] TOOL RESULT

```
no scan of BQT covers printed page 322 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:11:09.388Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(ln):\n    idx=sum(len(l)+1 for l in lines[:ln-1])\n    return t[:idx].count('\\f')\nfor ln in (10579,1561,3385):\n    print(ln, 'leaf', leafof(ln))\nEOF",
 "description": "Find leaf indices"
}
```


### [2026-09-14T03:11:10.445Z] TOOL RESULT

```
10579 leaf 311
1561 leaf 55
3385 leaf 113
```


## [2026-09-14T03:11:21.456Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(308,315):\n    s=leaves[i].strip()\n    print('--- leaf',i,'---')\n    print(s[:200].replace('\\n',' | '))\n    print(' ...END:', s[-150:].replace('\\n',' | '))\nEOF",
 "description": "Inspect BQT leaves around 311"
}
```


### [2026-09-14T03:11:22.407Z] TOOL RESULT

```
--- leaf 308 ---
ارجالون | کثتاس را در جنگه کشته بود و لهراسب پدر | کتتاس راکه تركه پادشاهی کرده در بلخ‌بعبادت | مشغول بود بقتل در آورد و به آفرین و همای | راکه دختران کشتاسب بودند گرفته در دوینمدژ | محبوس داشت عافبت اسفندبارین
 ...END: ه , ۶ فابی۱ ص۵۵ * . | بیدا شده. رك : اردشیر. | یه از صفحهٌ ٩۷‏ | از مولف است « حاشه چك ص44 * . | . درشاهنامه : روین دژ‎ ٩ | جزء لامنفك کلمه است .9 مزدستا 4۰4 >.
--- leaf 309 ---
خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین | است وتا کردة اوست . | اردجان س با جیم بر وزن همزبان» | از جد اول اهل نجوم است و در احکام مرقوم. | ار دش 7 س بفتح اول و ثانی وضم‌دال | می نفطه و سکون‌شن نفطه دار , 
 ...END: ۸۳۱۵8 وهرتفلد۷۱:82 ۸۳2 خوانده. منای قولدستة اول را | تأیید میکند و هنینگه قول دستذ دوم را - جزه اول اردا بمعنی مقدس است - وبراز بمعثیکراز | هه درصفحةٌ ۷۰۰
--- leaf 310 ---
اردشیران | " قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان | این همن که اول ماسانان بوده ات و او را | اردشیر بایکان میگفته اند ۰ واک‌لسره ابشان | اند - و تلم پسر شیروبه بن پرویز هم هست - و | کی را نیز گوبند که در قو
 ...END: ی ابران چندان ‌ | زباد نت کلا۱6 850 « دربای خزر ‌ | ۷ > . | بقبه از صفحه ٩٩‏ | است »متیر از مقدی . اما وبراف مشق از وبر بمعنی مرد و هوش و خرد است » کلمه بمعنی
--- leaf 311 ---
آردسهشت | او س باکاف‌فارسی بروزن‌پهلوان, | بمعئی اردجان است و ها ور | سرار ۳ و 4 | بر از جداول و اشکال و ! | وباکاف تازی‌نام موضعی است | ونام دهی است از ی | ار دم بفتح اول و الك و سکون‌نانی | و میم , نام سوره‌های زر 
 ...END: یرون * گونند . | که از شمال بچنوب ۹ | سدوم ریزد « فاعوس مقدس۲ ۳۹-۲ . | ۴ پپلوی ۸۲۵۳۵0 نلم پنج تن از | ۴۳ رك : اردببهشت . | است . شا وهیشته مکی از | فبه + صفیحة ۱۰
--- leaf 312 ---
بخشایش » بمعنی خیر و خیرات و چیزی در راه | خدا بمردم دادن باشد . | . اددانی معروف است که فقیض | گرانی باشد ۵ - ومردم دروش و فقیر ومستحق | را نیز گونند - و بمعنی ملم بتشدید لام هم | امده اسمت . 4 | ار « با زای فار
 ...END: شون و لوازم او - لشکرگاه < کاشفری ج ۱ | ص۱۱۲ » - نام زبان مردم پا کستان که ممزوجی است از فارسی وخربی و هندی و ترکی . ره : | داثرةالمعارف اسلام ولفت‌نامه .
--- leaf 313 ---
مه موم ما ی > ج با | کل فا | درل مخرفا | اردو
 ...END: مه موم ما ی > ج با | کل فا | درل مخرفا | اردو
--- leaf 314 ---
آردو ت | برابر نا | سس ۳ص اس ای دیس ۳۳ | سذ الفبای ار دو | ۳ کیت لا | 2 غ ۹ | کیت عرلا | ف ف‌ ِ؛ | ت | نا 98 | ات 42 | ات 4و | ك 7 ار | ۳ ‌ ۰ ۷ ی | ی ژا خر سر | و ۱ ول و ۷ ا(زم ؛ ساح خزطعرر | ۸ ۳ اج باه | ارف افن‌را) | ۱ ] ح شُرر | 
 ...END: ر سر | و ۱ ول و ۷ ا(زم ؛ ساح خزطعرر | ۸ ۳ اج باه | ارف افن‌را) | ۱ ] ح شُرر | ۵ ۵ 9 | 7 مر عب | #وع لا یکرجنت) | رل ۵ 92۳۱ از ء ک زک ) | 7 بر | -2۳۰۵/0] | 8 | ۶ 7-72" | ۳
```


## [2026-09-14T03:11:33.396Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (532,536,538):\n    s=leaves[i].strip()\n    print('=== leaf',i,' (printed p ~', i-210, ') ===')\n    print(s[:1500])\n    print('   ...tail:', s[-400:])\n    print()\nEOF",
 "description": "Print BQT leaves 532/536/538"
}
```


### [2026-09-14T03:11:34.349Z] TOOL RESULT

```
=== leaf 532  (printed p ~ 322 ) ===
بولی ۱
شیرینی است -
بواس. فتح اول بر دزن ایای 0
محتت وآزّار ورنج وسختی باشد.
بو اسحق طافه‌ای باشند ۱ -و در
نشابور چند ان فیررزه حست دک از آن ر)
بو اشه - بفتح اول بر وزن نراشه ؛
چارشاخ دهقانانرا کویند» وآن چویی چنه باشد
باندام کفدست و دسته ای نیز دارد که دهفانان
بدان غلهٌ کوفته را برباد دهند تاازکاه جدا شود
ء آنرا جربی مذری خوانند .
بو الححدر- با لام و خای نقطه دار
, جیم و دال بی نقطه بروزن کل برسر . ماحد
+ بی‌دهن ومی‌دفات را گویند.
بو القاسیم - کنابه‌از بوالفضول و شوخ
بو )لکد - بفتم کاف وسکون فا ودال
امجد . پمعتی رشوت وپاره باشد ۴ .
+سکون نون و فتح جیم و کاف ساکن, هرچیز
که آن عجیب و غرمب و طرفه باشد و دیدش
تفه آوری ۱
۵ ۳ 2
وس « بروزن خوب . فرش وباط
- ۳۱۲
خابه را گزنند. وباين ممنی بجای حرف اول بای
حطی‌هم آمده است.
بویا ۱ بنم‌اول و سکون ثانی وبای
امجد بالف کشیده » آشی را گون که از گوشت
بز کوهی پخته باشند.
بو لاش ه بسکون شن قرشت. بمعنی
قدیم وجاوید وهميشه و-رعدباشد ۷.
او برك « بنم اول ء ثالث وسکون انی
و را و دال بی نقطه ؛ بلبل را کویند. و بعرمی
عندلیب خواننه .
بو ۵ یر دس ختح دال وسکون کاف »
عصذر بوبرد است که بلبل باشد. :
بو باك بائالی مجهول بروزن خوبك ؛
دختر بکر ودوشیزه را گویشد - و هدهد را نیز
احمق وتادان را گویند .
لو لاو بسن دو بای امجد و سکون دو
واو , شانه سر و هدهد را گونند و آنرا مرغ
خواهر خودرا بوبو خوانند .
بو بو 4 « بفتح بای حطی. بمعنی بوبو
است که شانه‌سر وهدهد باشد۷ .
بو ب4 - نم اول و فتح الث» بمعنی
آرزوهندی وارزو باشد و سربی تمنی گویتد ۸
۳ "۳ رك ۳ مکقد.
0 , پهلوی 0۵۲ (فری) « اسفا ۱
روز دىگرشاه بزمآراست خوب
دساثر ۲۳۹ ».
ممتی ممحف بوبه است ( ۵ . م ) .
9 96۵ در آرهنی
۲ - 
   ...tail:  بای امجد و سکون دو
واو , شانه سر و هدهد را گونند و آنرا مرغ
خواهر خودرا بوبو خوانند .
بو بو 4 « بفتح بای حطی. بمعنی بوبو
است که شانه‌سر وهدهد باشد۷ .
بو ب4 - نم اول و فتح الث» بمعنی
آرزوهندی وارزو باشد و سربی تمنی گویتد ۸
۳ "۳ رك ۳ مکقد.
0 , پهلوی 0۵۲ (فری) « اسفا ۱
روز دىگرشاه بزمآراست خوب
دساثر ۲۳۹ ».
ممتی ممحف بوبه است ( ۵ . م ) .
9 96۵ در آرهنی
۲ - از دساتیر * فرهناك
. ۸ باین
( برهان فاطع ۵ )

=== leaf 536  (printed p ~ 326 ) ===
بورش
باشد که درخانةُ ل و کنند. :
بو د بطش « با ناك بتحتانی رسیده .
وطای حطی مکسور بشین قرشت زده» بیونانی ۱
جوهربت که آنرا مرفشیشا گوبند و آن چند
قفم میباشد : بعریی حجر النور خسوانند و ور
دوا های چشم بکار بر ند گوست اک بر گردن
کودك بندند نترمد .
بور بفتح اول و سکون انی و زای
هوز, سبزبی که بسبب رطوبت برروی نان وجامه
و گلیم وپلای وامثال آن بهم میرسد - و زنبور
سیاهرا نیز گویند که برروی کلها نشبندب و تنه
درخت را نیز کفته‌اند و ضم اول وئانی مجهول.
اسب نبله که رنکش بفیدی کرابد و اسب‌جاد
وتند و تیز را هم میگویند ۴ - و مردم تیزفهم
و صاحب ادراگ را نیز بطربق اسنعاره بوز گویند
چنانکه‌مردم بی‌ادرال کند فهم‌را کودن خوانند ۴
و کودن اسب کمراء بالانی باشد .
وز بضم اول و سکون انی و زای
فارسی؛ گرافی وسنگینی نب وحرارت باشد -
ویفتح اود گرداب را گویند .
بو زار ؟ جم اول و نانی مجهول و زای
نقطه دار بالف کشده و برای می‌نقطه زده ؛ ادوبة
حاره بهء‌نی داروی کرم یکه درطعامها ریز ندهمجو
فلفل وقرنفل ودارچینی وامثال آن. 9
ود لك جتح اول بر وزن حوضك »
بمعنی بوز است ؛ و آن سبزبی باشد که بسبب
رطوت بر روی نان و گلیم و پلای وامثال آن
شدد ۰
نف
ود کف بم اول وفتح کاف وسکون
ثانی وثالث و نون و دال امد . صقه و ابوان را
کونند. وبا رای پفرشت هم‌بنظر آعده است.
بو هخا ت با میم بر وزن کوسفند ؛
کیاهی ماشد‌یغامت خرشوی» ویا رای می‌نقطه حم
بشظر آمده است
هه - ضم اول و قح ثالث »
و میم ۰ بجع بوزمند است که یاه خوشبو
باشد .
ود فه - منم اول و کسر الت و فتح
نون» ممونرا گونند» و دعر بیحمدو نه خوانده ۳
بو له » منم اول و زای فارسی و فتح
تون. غنجه و شکوفه و بهار درخت را کوش دکه "
هنوز نشکفته باشد» وآنرا بعربی کم خوالند.
بور نینه بروزن موی 
   ...tail: وزئه را
کویندکه میمون باشده .
لو ده ه بروذن کوزه» شرابی باشد که
از آرد برنج و ارزن و جو سازند ودر ماوراءالنهر
و حندوستان ۹۹ بسیار خور ند و یه درخت را
یز کوید ٩‏
بود بدان - با دال ابجد بر وزن
حورتطا. ۰ دوس نت ۳ آز مسر آورندوربی
ی آرد برنج حلوا سازند
وبخورند؛ بدنرا فربه کند .
نود دنه _ سس وزن روزشه . میمون را
7
۴ - شاکرد تو میباشم
۴ - مخقف بواوزار هه مواقرار.
۵ بوزرجمهر - رك : بزرگمهر .
۱ رك ؛ بوز .

=== leaf 538  (printed p ~ 328 ) ===
لهراسب ؛ بممتی خواب دیدن باشد و جربی رژبا
خوانند .
بوشیاس - بضم اول و سکون ثانی
مجهول و الث و بای فارسی بالف کشیده و بسین
بی‌نقطةٌ زده» نممئی بوشاسب است که‌خواب‌دیدن
وروّبا اشد ۱ ۴
بو شفح- - با جیم بروزن هوشنگه »
نلم قصبه ایست از خراسان» ومعرب آن فوشنج
ات ۴ ۷
لوصیر- منم اول و سکون ثانی و صاد
می‌فقطه بتحتانی رسیده و برای قرشت زژده . لغئی
بعرییآ نرا آذان‌الدب خوانند من ی کوش خرسء
بسبب شباهتی که بدان دارد - و بسضی گویند
نوعی از ماه زهره است و آن پوست درختی
باشد بغایت سیاه و آن را بعربی شیکران الحوت
کویند وبعضی دیگر گننه‌اند بافلای شامی‌است»
واه اعلي .
بو طا نيه - باطای حطی بروزن‌ساطانیه,
پوست ددختی است که آن را بمربیکرمة السودا
و بفارسی سیاه دارو خواتند ۰ و آن مانند عشفه
پردرخت پیچد .
او جصی - نم اول و سکون ثانی
و غی نقطه دار عضوم بلام زده و صاد بی نقطة
مضموم بثون زده » لفتی است بونانی ۴ » وههمی
۱ ک ۱ : پوشاست.
مس 0 اس
آن مربی ان الئور است که گلوزبان باشد ؛
وآن دوابی است ممروف» ویضی گونند این‌لت .
رومی است. ۱
بونج نم اول و سکون ثانی و فتح
غین نقطه دار و نون و چیم ساکن . شوئیز را
کوه 2 و ان تفن است ره .و سا وگ
و عربی حبة السودا خوانند - و فوشنج را نیز
کفته اند و آن ضبه ایست در خراسان تزديك
قندهار ۴ .
وه » بر وزن صوف » پرنده ایست
که بنحوست اشتهار دارد » و آنرا بوم نیز
گونده . ۳
بو فروش» بکر فا , عطار و مك
فروی را گوبند . :
وق - نم اول و سکون ثانی و قاف »
سفید مهرء باشد و آن چیزیست که در حمامها
وآسیاها و هنگامها نوازند" - و با انی مجهول
چادر بزرکی باشد که رختخواب درآن بندند .
بو قلمون -
دیبای رومی را گونند,
و آن جامه ات که
هراحظه برتگی‌تماید
و کنابه‌از کمی‌است که
هرساعت خودرا برنگی
   ...tail:  - نم اول و سکون ثانی و قاف »
سفید مهرء باشد و آن چیزیست که در حمامها
وآسیاها و هنگامها نوازند" - و با انی مجهول
چادر بزرکی باشد که رختخواب درآن بندند .
بو قلمون -
دیبای رومی را گونند,
و آن جامه ات که
هراحظه برتگی‌تماید
و کنابه‌از کمی‌است که
هرساعت خودرا برنگی
۴ - بونانی 007 -<
۵ در ادییات زرتشتی نام جفد .
توباز سدره نثینی فك نشیمن تست
چرا چو بوف کی‌آشان بوبرانه.
دفاب ۱: ۳۷۲۱ * ورك: اسفا ۱ : ۲ ص۰۷
```


## [2026-09-14T03:11:46.966Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,s in enumerate(leaves):\n    if 540<=i<=560:\n        head=s.strip()[:60].replace('\\n',' | ')\n        print(i, head)\nEOF",
 "description": "Scan leaf headers 540-560"
}
```


### [2026-09-14T03:11:48.012Z] TOOL RESULT

```
540 بو عادران | باینمهنی عربی است - و زمین شیار نکرده رانیز | گفته ا
541 بو همان - بسکون‌ناكث بروزن‌دودمانه | پمعنی رحم است که زهدان و 
542 9 بکر اول وسکون ال | تاتی‌سمعنی خوب وتيك‌باشد ۱ - از | 4 - بکر ا
543 قدید گویندش . # | لها - بکس اول و ثانی بالف کشیده | و بزای نقطه 
544 بهزا | است ۱- ودر عربی بمعنی عجب ازتعجب_ وحلااه | ازهللا کت باشد
545 ی ۳۹ ده | بهر ام تل - هی مر فج توح | کتک | هر اهج -_بنتح میم و سکو
546 له ره بر - بنتح بای‌ابجدبروزن رخده | فرشت . تم میوا حرختی اس
547 ون مت | کاف فارسی وسکون‌نون و کاف‌دیگر؛ دارالملك | نحاك در شهر ب
548 غشب را فرو نشاند ۰ و او موکل است ب رگلوان | و گومقندان , اکثر 
549 ۳۷۹ - | پمنحه 2 با جیم ونون بروزن‌دد | و عجمان در ين روز عید کنن
550 یم - بر وزن فهیم : تلم یکی آزرابان | و بزرگان هند ات۳٩‏ | گزنشد 
551 بجوم | آب با بخون ۱ . | باآب یا بخون ۱ . | نی خساند و ق م کرد - و 
552 که پس رکیوین کودرز باشد . | یحو هر - کنابه از مردم بی هنرویی | ع
553 ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور | هم بنظرآعده است 
554 بید کیا | بید گیا - بکر کاف فارسی و نحتانی | بالف کشیده . نوعی ا
555 - ۳۳ 7 | یر دک بنتم رابع بر وزن نك بی » | بمعئی برژه انته ات صمف
556 بیرونآحدن | بیرون آ هلان - سسروف است که | نفیض درون رفتن باشد- و
557 پیمما -- | لیستون ۱- نام کوهی است | مشپور که فرهاد بفرمودة شیرین
558 از "1 رن اه | لیشه » بر وزن ربشه جنگل و نستانرا | گونند و بعربی 
559 ۳۹۳6 سد | بیقاد ه بنتح اولبروزن نیزار , سرزنش | وطعنه باشد. | بیغا
560 بنم ثانث مر وزث میگفت اه | ستارژ زهره را گوبند . | بیلقان ‏ بنتح
```


## [2026-09-14T03:12:02.997Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (542,546,547,548):\n    s=leaves[i].strip()\n    print('=== leaf',i,'(p~',i-220,') ===')\n    print(s[:1800])\n    print('---tail---')\n    print(s[-500:])\n    print()\nEOF",
 "description": "Print BQT beh/behesht/bahman pages"
}
```


### [2026-09-14T03:12:04.403Z] TOOL RESULT

```
=== leaf 542 (p~ 322 ) ===
9 بکر اول وسکون ال
تاتی‌سمعنی خوب وتيك‌باشد ۱ - از
4 - بکر اولر انی
بالف کشیده. خوبی و زیاییرا به
گویند ۴ - و بغتح اول قیمت هرچیز را .
بهادد - بن دال ابجد بروزن تیاس »
یمعنی شجاع ودلیر بکمال باشد ۴ ِ
لاد - بروزن چهار , ممروف است که
فضصل ریع‌وبودنآفتاب دربرج حمل وئور وجوزا
اشده - وتخانة چن وا که زر اسان
و خانةٌ طلاکاری و عنقس بود - و بت را نیز
خصوصا_ ونام کلی است زردکه آن‌را کل کاو
چشم خوانند. و بحضی کونند بان همنی عربی
است- ونام جزیرمای همرت خوش آب وهوا-
و حرم بادشاهان و سلاطن را نیز کفهاند -
و بکر اول نم ولامتی است در هندوسنان -
وبمعنی تنکه بار که عبارت از يك تای بلر است
بهار بشکته- با بای ابجد و شین
قرشت وکاف ونون وهای هوز, نام نوابی است از
موتیقی.»
بهار جح ف4- بخانه راکویند » چه‌بهار
ممعنی بت هم آهده است ۷ - و بنای رفیم را
نز گفه‌اند .
بهار خوش» بهار معلوم . بنتم خای
نقطمدار وسکون ولو ممدولهوشی قرشت» گوشتی
باشد که آ ترا نمکسود نهوده‌خشك سازندمویثازی
وهو !۷۵31 صفت است بمعنی خوب دنتيك و به « بارتولمه ٩۱۳۹۵‏ . ساتسکربت ۷25۷ پارسی
باستان لالأ ۰۷2 پهلوی ۷۵ «نیب رکب ۲۳۸ «فاب ۱ : ۰۷۲ ۲ اونوالا 2۱۵ . - بهلوی
۵ « تاوادبا ۰۱۵4 < اونوالا ۳۸4» رك : آمی و فرهنگه روستابی ۲۵۹ وگل کلاب ۷۲۷- نیز
» پپلوی )۳2, ابرانی باستان ۰۳241 اوسنابیُ]]۳8» بارسی‌باستان۳2)1
« بارتولمه ۳۲۲ 4 . بازند ۳2 . پهلوی تورفان 02010 « یبر گه ۱۷۸ ».
۴ هن فری ات تیاه یه فشده.. ها پیلور
و5 دلرسی باستان 2 -1۱:۲8 * اسفا ۱: ۲ ص۲۳* ( ثوره واهره ماه دوم‌هضامنشی .
رك : دوازده ماه هخاهنشی بقلم نگارنده .آموزش ویروری سال 46 شمار؛ ۱ ص ۸ ۰ )» کیلکی
۳ «: فرب زندی و برنی 26192۲ « 2 . ۱ ص ۲۸4 ۰ سمنانی 9812۲ ری
۲فت ۱ سرخه 24 294 . لاسگردی ۳ ., ی ۳ اد . ۲ ص ۱۷۹ »
ورك:بهامن_ نیز وزنه ابست هندی «دائرالمعارف اسللام*. - مانسکریت ۷111878 بمعنی
دمر(تخانه). رك: توبهار ومزدینا ۳۲۵. اما بهارچین بابهار خانة 9 نگارستان چی‌وبابهارستان
طاهیآهمان جهشت گنک اس تکه برخی از شعرای ماآن را بتخانه بنداشته‌اند. رك : بهشت کنك .
۴ - رگ : بهار وبپعت کنگ
---tail---
۳* ( ثوره واهره ماه دوم‌هضامنشی .
رك : دوازده ماه هخاهنشی بقلم نگارنده .آموزش ویروری سال 46 شمار؛ ۱ ص ۸ ۰ )» کیلکی
۳ «: فرب زندی و برنی 26192۲ « 2 . ۱ ص ۲۸4 ۰ سمنانی 9812۲ ری
۲فت ۱ سرخه 24 294 . لاسگردی ۳ ., ی ۳ اد . ۲ ص ۱۷۹ »
ورك:بهامن_ نیز وزنه ابست هندی «دائرالمعارف اسللام*. - مانسکریت ۷111878 بمعنی
دمر(تخانه). رك: توبهار ومزدینا ۳۲۵. اما بهارچین بابهار خانة 9 نگارستان چی‌وبابهارستان
طاهیآهمان جهشت گنک اس تکه برخی از شعرای ماآن را بتخانه بنداشته‌اند. رك : بهشت کنك .
۴ - رگ : بهار وبپعت کنگه .

=== leaf 546 (p~ 326 ) ===
له ره بر - بنتح بای‌ابجدبروزن رخده | فرشت . تم میوا حرختی است که سمخ آنر! مفل
کر . شربك و اباز راگوند. ٩‏ 9 گویند وقتیکه ارو تفزمبلشد» وچون‌خشك‌شودوفل
تست خوانند . و بیار لذیذ است . #
- یمت‌الانظ نمی سوم ۲
۵ هراد یکر اول (ییکو زادهک نام هاش‌شهیر اواخرعهد تیموری و صفویه.
لفب وی کمال‌الدین واز مردم حرات وشاکره بر سید احمد تبریزیاست.نولد اویین۸44 و۸۵۵< .
وی نضت در دربار سلطان حسبن میرزا بااشرا ( ۸۲4 - 4۱۲ ) بود و امیر عطیشیر نوالی وزیر
ممروف مشوق وحامی اوبود. بعدها ذاء اسمعیل سفوی )٩۳۰ - ٩۰5(‏ او را ازهرات ببریز برد
و اوتااوایل سلطنت شاه طهماس‌اول  ٩۳۰(‏ ۸ حیات داشته است وبادشاه اخیر ترداو قاشی
1 است. مینیاتور های سیاری بپزاد منسوب است که اسالت غاب آنها هورد تردید أست.
سرآمدان عنر تالیف کر طاهر زاده بهزاد چاپ برلبن ۱۳4۲ قمری ص ٩‏ - ۱۰ ؛ تاریخ
0 لت جلیم . ترجه عداف قربار »تهران ۱۳۱۷ ص *۱۷- ۱۷۱ ؟ دور تحول
نقاشی ابران هلم ابوالقاسم طاحری درحجله روز کارنو حج ۵ : ۱ ص ٩۳‏ ۰
دونمونه ازکارهای بهزاد ( متعلق بدولت ابران ) ازتاریخ صنایم ابران . وبلسن. برابر ص۱۹۸
---tail---
عدها ذاء اسمعیل سفوی )٩۳۰ - ٩۰5(‏ او را ازهرات ببریز برد
و اوتااوایل سلطنت شاه طهماس‌اول  ٩۳۰(‏ ۸ حیات داشته است وبادشاه اخیر ترداو قاشی
1 است. مینیاتور های سیاری بپزاد منسوب است که اسالت غاب آنها هورد تردید أست.
سرآمدان عنر تالیف کر طاهر زاده بهزاد چاپ برلبن ۱۳4۲ قمری ص ٩‏ - ۱۰ ؛ تاریخ
0 لت جلیم . ترجه عداف قربار »تهران ۱۳۱۷ ص *۱۷- ۱۷۱ ؟ دور تحول
نقاشی ابران هلم ابوالقاسم طاحری درحجله روز کارنو حج ۵ : ۱ ص ٩۳‏ ۰
دونمونه ازکارهای بهزاد ( متعلق بدولت ابران ) ازتاریخ صنایم ابران . وبلسن. برابر ص۱۹۸

=== leaf 547 (p~ 327 ) ===
ون مت
کاف فارسی وسکون‌نون و کاف‌دیگر؛ دارالملك
نحاك در شهر بابل ساخته نود .
بهشتی و بهشتی دوی «کاماز
خوش صورت و خوبروی باشد ,
بهاك - متح اود و نی بر وزن ملك,
میشود , و ممرب‌آن بهق است .
به گز لن ‌ِ بکراول وضم کاف فارسی؛
اتخاب براتخاب - و کز ده را گونند» نی
چیزهای سرمو نیک و که‌ازچیزهاینأسرهبگز ند
و شخصی را نیز گونن دکه‌چیزها را اتخاب کند.
و سیم را سره سازد و او را سربی نقاد و تاقد
خوانند - و بىعنی کزبدن و انتخاب کردن هم
آمده است - و امر پاشمعئی نیز حست .
بهل؟ بکسر اول بروزن خجل . ام
بر گذاشتن است نبعنی بگناو .
بهله - بالاء بر وزن فهوه » یوستی باشد
که باندام ینجهٌ دست دوزند و میرشکاران‌بروست
کشند و چرغ و باز و شاهین را بدست گیرند.
تهم « بکسر اول بر وزن‌شکم , ترجمةٌ
نم باشد «
و متتابم فلان است که چیزی مجهول و غیر
مملوم بلشد ۰ _.
۱ بهم بر آ مان . کنابه از در مب
شدن باشد
لهای « بروزن مخزن» مختف‌برهمن ۴
است که بمعضی راست کفتار و راست کردار
و کوچك بسیار دان و درلز دست وایر بارننمباشد
ونلم فرشتهایست که‌تسکین خشم وقهر ددوآش
. از کتب تاریخی وادبی مابرمیا بدکه « کشگهدژ» درخوارزم (خبو؛ حالیه) واقم‌بودماست‎ - ٩
در فصل ۲٩‏ بند ۱۰ بتدهش آعده : کنگه دیز در طسرف مشرق واقع است » چندین
فرسنگگ دور از دربای فراخکرت. درآبان بشت( اوسنا ) بندهای 64 و۵۷ دویار نام 1682082
بادشده ویکبار تیز در زامیاد بشت ند 4 ۸0۱59-20812 آمده بعنی ( اند رکنکه) . این
کوه غالبا درشاهنامه «بهشت کنکه» نامیده شدم بوستی فاکلا نوسد: «بنظر میرسد این محل
که چینبان نیز بنام کنگه می شناخته اند « يك قسم بپشت روی زمین ابرالبان مصوب
میشده » بدست دسته ای لزایرانبان در وسط خالك نوران در طرف شمال سیر دربا بر با شده
بود » . ( رك : 20020186۳6 عع0 00 , ۱2501 ) لابد همین کتکه است که
برخیاز شمرای ما آنرا بتخانه پنداشته وفرهنگها محل آنرا درترکستان بادر چن قراردادماند.
«شتها حج ۷ ص ۲۰۶۰ >. ۱
۴ - رك : هشتن و هلیدن .
۴ - یز بفتح اول < اسفا ۱: ۲ ص ۰۱۲۱ امروز
هم ختح اول تلفظ کنند .
؟ ‏ رك : پرحمن .
هه ازسفحهٌ ۳۲۹ 7
(خرب) و اقذ (علامت تخضیل
---tail---
ردادماند.
«شتها حج ۷ ص ۲۰۶۰ >. ۱
۴ - رك : هشتن و هلیدن .
۴ - یز بفتح اول < اسفا ۱: ۲ ص ۰۱۲۱ امروز
هم ختح اول تلفظ کنند .
؟ ‏ رك : پرحمن .
هه ازسفحهٌ ۳۲۹ 7
(خرب) و اقذ (علامت تخضیل)؛ بمنی خوبتر . بیکوتره وآن صفت خضیلی است برای موصوف
محذرف که «انکپو 808120 ( جهان. حستی ) باشد و جمعاً بمنی جهان‌بهتر» عالم ییکوتره خد
«رژنگهو سس دوزخ» «بشت ۲ص 2۱۷۰ ۱ »؛ پهلوی ۷۵۱۱1904 «ثیب رکه ۲۳۱ »:فیدوس .خلد»
جنت ؛ جابی خوش آب و هواوفراخ سمت و آراسته که نیکوکاران پس از مر که درآن ملد
باشند. ر : داگرة النه لزف اسلام.

=== leaf 548 (p~ 328 ) ===
غشب را فرو نشاند ۰ و او موکل است ب رگلوان
و گومقندان , اکثر چهار پابان ؛ و تدییر امور
و مصالحی که درماه بهمن رروز بهمن واقم‌میشود
باو تملق دارد ۱ - و عفل اول را نیز .گویند -
و نم اردشیر پسر اسفندبار - و تام ماه بازدهم‌از
هر ماه شمسی و بودنآفتاب در برج دلو» وجشن
سده که یکی از جشنهای بز رکه فارسیان است
در دهم اين ماه باشد - و گیاهی و رستئیی بود
که در ماه بهمن و زستان کل کند و یخ آن
سرخوسفردمیباشدو آنرا بهمنین‌میگویند» وبعضی
کویند کلی‌است که در زمستان هم‌میباشدوداروبی
است که بدبرا فربه کند و بادرا دفم‌سازد و قوت
و پنا بر قاعد کليهٌ فارسیان که چون نام روز با
نام ماه موافق‌آید آنروز را عید کیرند , در این
روز جشن سازند؟ و انواع غلها و کوشتها پزند
ر کل بهمن سرخ و سفید برطمامها پاشند وهردو
بهمن را میده کرده با نبات و قند بخورند وآترا
مب نز و۳ مد
عقوی حافظه دانند , و گویند این رو راخاصیت
تملم است در کندن کاهها و بیخهای دوایی از
کوهپا و صحراهاو کرفتن روغتهاو کردن‌بخورهاء
وييك است در این روز جامهٌ نو بربدن هپوشیدن
و ناخن چیدن و موی پبراستن و عمارت کردن:
واین روز دا بهمنسته خوانند - و نام پرده‌است
از موسیقی - و نام قلمه ایست در نواحی اردییل
و در قدیم در آنجا ساحران و جادو کران بیار
بوده‌اند. وگونند کیضرو در اول سلطنت خوشس
طلسماتآ را شکته‌آن قلمه را فتح کرد - و نام
قلمه‌ای هم هست درهندوسنان- و نام کوهی است
بسیار بلند - و بر کند ها و تختهای پرف را نیز
کوبند که از کوه بسبب حرارت آفتاب جدا شود
و یفتد؟ - ونام چشمه است در جرجان که‌چون
آپ از آنجا بردارند و بر کرمیکه در توابع
آنچاست بای اهند تمام آن آیکه برداشنه اند
شور و تلخ شود اکرچه يك کس يا نهاده و صد
کسآب بردائته باشند 9 .
بمعنی خوب وتيك و « مذد » ازرسشةٌ 1120 بمعنی منش: پس بهمن یعنی به‌منش» نيگ آندیش »
نيك‌نهاد. طبری (ح۲اص4) کوبد: «تفسیربپمن‌بالعریة:الحسن‌النیة». وی‌یکی ازامشامپندان‌وتستین
آفریده اهور مزداست . در جپان روحالی منلهر اتدیشة نيك موخرد و دانابی خداست - دومین ماه
زستان و بازدهمن ماه مال شمسی بنام او بهمن خوانده میشود - و ن
---tail---
 این گیاه درپهلوی نیز ۷۵۵۷۵۳088 است «اونوالا ٩۳۱‏ . ۴ - رك : همنجنه .
۴ - نظر بوقوع آن درماه بهمن بکثرت . ۵ - این نامر معجم‌البلدان
۳ مججمل‌التواریخ وحدود المالم ثیست.در قابوسنامه (س ۷۸- ۲۹*آمده: «روزی ازولابت ما سخن
می‌پرسید (امیر باالسوار) و عجایب‌هاه حرناحیت می‌برفت. می گفتم بروسناء ک رکان دبپی است
در کوهیابه, و چشمه‌ایست ازدیه دور و زنان که آب آرند جمم شوند» هکس باسبوی و از آن
چشمه آب بر گیرد و سبوی برسر نهشد و باز کردند» یکی از ايشان بی‌سبوی همی‌آید و برداه
بقبه درصفحٌ ۳۲۹
( برهان اطع۳۷ ) .
```


## [2026-09-14T03:12:32.997Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== گشتای in BQT v3 ===\"\ngrep -n \"گشتای\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== گشتای elsewhere ===\"\ngrep -rn \"گشتای\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -10\necho \"=== MON parts گشتای ===\"\ngrep -n \"گشتای\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head",
 "description": "Find goshtay"
}
```


### [2026-09-14T03:12:33.095Z] TOOL RESULT

```
=== گشتای in BQT v3 ===
=== گشتای elsewhere ===
=== MON parts گشتای ===
```


## [2026-09-14T03:12:36.443Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nwc -c data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt\npython3 tools/ref_page.py BQT:1819 2>&1 | head -40",
 "description": "Try ref_page for BQT 1819"
}
```


### [2026-09-14T03:12:37.635Z] TOOL RESULT

```
2499427 data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt
REF: BQT:1819  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 616  OCR-lang: fas

-۹۱۸۱۹- ۱ کناب
کنایه از مردم فصیح و بلیغ باشد ‎٩‏ - استعمال مبکنند چنانکه کوبند: ۶« مستم دگشت»
کشاده هنگامان ۲ (۱) - کنابه | بعنی مپیا شد وآماد هگردید - و سیروکشت را
از فصول اربعه است که بپار و تابستان و پاییز | لیزکوبند ۷ - و بمعنی ح كکردن‌ومحوساختن
و زمتان باشد . هم کفته‌اند ۸ - و خریزه را هم میگوبند ‎٩‏ اب
گناس ۲ < بسکون سین بی لاقطه وبمعنی حنظل نیز آمده است ‎٩‏ - ویمعنی دیدن
و بای ابجد » همان کشتاسب مشپور است: که ونظاره کردن هم بنظر رسیده است.
یادشاهی بود پدر اسفندبار رویین تن و بکسد شتا ۱۰ نم اول و فوقالی بالف
وشصت سال پادشاهی کرد . کشیده . بهشت را گونند که مربی‌جنت‌خوانند.
گشاك ؟ - بنم اول ونالی بالف کنیده گشتاسب ۱۱- بن‌اول بروزن‌لهراسب,
وبکاف زده , بازوی درازخانه راگوبند وآن‌ازس نام برزخی است که میان خلق و خالق باشدبرای
دوش است تا ارلج . رسیدن فیض حق ۱۳- و نام پادشاهیاست‌ممروف
گشب * » بنم اول و سکون ثانی‌وبای و او پدر اسفندپار رویین تن بود . گویند یکسد
ابجد » بمعنی جهنده وخیزکننده باشد . و شست سال پادشاهی کرد ودین زردشت پذیرت
گشت ‎٩!‏ - بروزن طشت . بممنی کردید | و چون زردشت کشته کردید بجای او متصوب‌شد
باشد که ماضی گردیدن است ؛ و در مقام شد وآبین زردشت را بریای داشت .
() چش :کعاد هنگامان .
۱ - جوانی بيامدکناده زبان (دقیقی) یخن گفتن خوب و روشن روان .
فردوسی طرصی « شاهنامةٌ بت اج ۱ص ۹ -
۲ - جمم «کناده هنگام » يك افصل‌ازچهار فصل سال؛ برساختهٌ دساتیر«فرهنگه دساتیر
س ۰.۲۹۶ ۴ - مخفف با مصحف «کسباسپ». .۴ -اظ . مصحف «کعال» . قس:
کمالهٌ ران ( در تداول. ) 8 - مخغفف «کگشنپ > کشب (ه.م.) ومعنی‌مذ کوردرمتن
نیز مجعول است : رك : آذرکشپ آذ رگشسپ, کشسب. ‎٩‏ - رك :گت .
۷ - مسدر مرخم . قس ؛کردی ع 865101 ( تفریح ) « ژاباص 6۳۹۳ ۰
۸ سنا او ز لقش‌چهرة خود پرده برگرفت ‏ مالقش دیگران ز ورق میکنیم کشت.
آوحدی 3« رشیدی » .
‎٩‏ - و بمعنی خربزه نیز آهده » لیکن بعی بمعنی حنظل گفته‌ان د که خربزه ابوجهل
باشد .» « رشیدی ؟ وآن مصحف «کیست» (.م.) است بمعنی حنظل و خریزه تلخ -
*- فرائتی از رسم الخط پپلوی ۷201501 ( بهشت ) . رك : بهشت و ر4 : باروچا
صس ۳۳۶ :
زانکه کشتای خوب کاران راست جمله عقبی حلال خوارانت .
سنائی غزنوی « رشیدی » .
۱۱ در اوستا و پارسی باستان ۷1918908 . ( ۳ پونانی ۷51290889 ) » مرکب از
دو جزء : ۷1512 بمعنی از کار افناده » ترسو و محجوب و جزء دوم 85702 همان اسب است »
جمماً یمنی دارلدة-۱سب از:". افتاده « پارتولمه ۱۶۷ > ور : فاب ۱ص ۲۲۷ ؛ مورخان‌ایرانی
و عرب نام او را« بشتاسب " و « بشتاسف » نیز ضبطکرده‌اند . رك : مزدستااص ۳۲۳ ببعد .
۴ این معنی مجعول ات .
```


## [2026-09-14T03:12:58.226Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"اوکالیپتوس\" \"اقلیدس\" \"انگلیون\" \"اردیبهشت\"; do\necho \"=== $w ===\"\ngrep -c \"$w\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null\ndone",
 "description": "Grep Mo'in for the words"
}
```


### [2026-09-14T03:12:59.631Z] TOOL RESULT

```
=== اوکالیپتوس ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:0
MON_part2.txt:0
MON_part1.txt:0
incoming/MON/MON_2vol_Adena_v1_djvu.txt:0
=== اقلیدس ===
MON_part2.txt:2
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1
MON_part1.txt:1
=== انگلیون ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:2
MON_part1.txt:2
MON_part2.txt:1
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1
=== اردیبهشت ===
incoming/MON/MON_2vol_Adena_v2_djvu.txt:5
MON_part2.txt:5
MON_part1.txt:3
incoming/MON/MON_2vol_Adena_v1_djvu.txt:3
```


## [2026-09-14T03:13:02.545Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== اقلیدس MON_part1 ===\"\ngrep -n -A3 -B1 \"اقلیدس\" MON_part1.txt | head -30\necho \"=== انگلیون MON_part1 ===\"\ngrep -n -A3 -B1 \"انگلیون\" MON_part1.txt | head -30",
 "description": "Read Mo'in entries"
}
```


### [2026-09-14T03:13:02.634Z] TOOL RESULT

```
=== اقلیدس MON_part1 ===
13477-راببع اشکال را عکس نخستین شمار 
13478:اشکال اقلیدسی: (هس.) شکل‌هایی که در 
13479-هندسه از آن بحث می‌شود. 
13480-اشکال: اق8« [ع.] (مصل.) بای بستن؛ 
13481-دشوار شدن. بوشیده شدن کاره مشتبه شدن 
=== انگلیون MON_part1 ===
17503-انجیر نده» انجیر ده) سوراخ کردن» 04 
17504:انجیل: ا[[ [معر. شارت < انگلیون] 
17505-(اخ.) هر یکث از چهار کتاب دینی مسیحیان) 
17506-ج. اناجیل. 
17507-
--
18451-
18452:انگلیو ت ز(اخ.) انجیل؛ انگلیون. 
18453-(.) چون مسیحیان شرقی انجیل را در قماش 
18454-
18455-
```


## [2026-09-14T03:13:13.920Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T03:13:13.929Z] TOOL RESULT

```


```


## [2026-09-14T03:13:16.546Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== اقلیدس MON_part2 ===\"\ngrep -n -B2 -A5 \"اقلیدس\" MON_part2.txt | head -30\necho \"=== اردیبهشت MON_part1 ===\"\ngrep -n -B1 -A4 \"اردیبهشت\" MON_part1.txt | head -40\necho \"=== بهمن MON ===\"\ngrep -n -A3 \"^بهمن:\" MON_part1.txt MON_part2.txt | head -20\necho \"=== بهشت MON ===\"\ngrep -n -A3 \"^بهشت:\" MON_part1.txt MON_part2.txt | head -20",
 "description": "More Moin lookups"
}
```


### [2026-09-14T03:13:16.687Z] TOOL RESULT

```
=== اقلیدس MON_part2 ===
75690-که در آن رخ می‌دهد و نیز در مکان مطلق 
75691-غیر قابل تغییر یعنی فضای سه بعدی هندسة 
75692:اقلیدس که مستقل است از اشیایی که در 
75693-آن جای دارد - قرار گرفته است. نیو تن 
75694-معتقد به مفهوم مطلق ثالثی هم بود؛ بدین 
75695-نحو که مقدار ماده را تغییر تاپدیر می‌دانست» 
75696-اعم از اینکه آن در حال سکون باشد یا در 
75697-حال حرکت. «اینشتین» به کلی منکر مطلقیت 
--
75743-خط منحنی که مسر سیارات؛ است 
75744-کوتاه‌ترین فاصله است یعنی بر خلاف آنجه 
75745:در هندسة اقلیدس دیده‌ايم که اقصر فاصله 
75746-بسن دو نقطه خط است - در این 
75747-هندسه؛ اقصر فاصله مبان دو نقطه خط 
75748-منحنی است. اینشتین» از مطالعات خود به 
75749-این نتیجه می‌رسد که جهان؛ هر چند 
75750-نامحدود است (یبعنی از حدود متصور 
=== اردیبهشت MON_part1 ===
77-سعین :701 محمد (و. هفدهم رجب ۱۳۳۲ هجری قمری مطابق ٩‏ 
78:اردیبهشت ۱۲۹۷ شمسی. ف. ۱۳ تیر ماه ۱۳۵۰ ه.ش). فرزند مرحوم شیخ 
79-ابوالقاسم. در شهر رشت در خانواده‌ای روحانی متولد گردید. به هنگام طفولیت 
80-او نخست مادر و پس از پنج روز پدرش در عنفوان شباب درگذشتند. جد پدری 
81-وی شیخ محمدتقی معین‌العلما که در سلک علمای روحانی بود به تربیت وی 
82-همت گماشت. جد مادری او شیخ محمد سعید نیز از علما و مدرسان علوم قدیمه 
--
27932-پاردان: 0 (امر.) جوال. تنگ» ظرف ماه. روزهای پارسی: سی روز ماه شمسی 
27933:شراب. شراب. اپرانیان: «هر مزد» بهمن» اردیبهشت» شهریور 
27934-
27935-
27936-پاردم: 0 ([ - پاره‌دم ] (امر.) چرمی که 
27937-بر زین يا پالان می‌دوزند و زير دم اسب یا 
--
27969-بارسی: دوازده ماه سال شمسی ایرانبان: 
27970:فروردین ماه» اردیبهشت ماه خردادماه» تير 
27971-ماه» مرداد ماه» شهر یور ماه» مهر ماه» آبان 
27972-ماه آذرماه؛ دی ماه» بهمن ماه اسفندارمد 
27973-
27974-
=== بهمن MON ===
MON_part2.txt:33326:بهمن: ( گیا.) گیاهی است از رده تک‌لبه‌ها 
MON_part2.txt-33327-جزو تبرة رگسی‌ها که در زمستان در حالی 
MON_part2.txt-33328-که ریشه‌هایش در برف نیز باشند» گل 
MON_part2.txt-33329-می‌دهد. این گیاه مانند لت کون دارای پیز و 
MON_part1.txt:26524:بهمن: ۳2۲۳20 [نیک منش] (اح.) تکت از 
MON_part1.txt-26525-امشاسیندان. دومین روز از هر ماه شمسی 
MON_part1.txt-26526-(بنام امشاسپند مذکور). یازدهمین ماه سال 
MON_part1.txt-26527-شمسی و دومین ماه رت (بنام امشاسیند 
=== بهشت MON ===
MON_part1.txt:24545:بهشت: ( کد.) حوریان بهشتی. 
MON_part1.txt-24546-
MON_part1.txt-24547-بکر تراشی: آ-0۵۲-۱۸۲۵3 (حامص.) ( کد.) 
MON_part1.txt-24548-ایجاد کردن مضمون غریب و تازه. 
--
MON_part1.txt:26464:بهشت: 000-28 [بهترین (جهان)] (امر.) 
MON_part1.txt-26465-جایی خوش آب و هواو فراخ نعمت و 
MON_part1.txt-26466-آراسته که نیک وکاران پس از مرک در آن 
MON_part1.txt-26467-مخلد باشند؛ جنت» فردوس» خلد.
```


## [2026-09-14T03:13:21.333Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-",
 "prompt": "What is the reconstructed root, its meaning, and which descendants (Avestan, Sanskrit, Greek, Old Persian) are listed? Quote the etymology section."
}
```


## [2026-09-14T03:13:22.997Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%B4%D8%AA",
 "prompt": "Give the Persian entry بهشت: etymology (Middle Persian, Avestan forms), meaning. Quote exactly."
}
```


### [2026-09-14T03:13:26.520Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁su-

**Reconstructed Root & Meaning:**
The root is ***h₁su-***, meaning "good."

**Etymology Section Quote:**
"Possible metathesis of *h₁wes- ('good'), or perhaps related to *h₁es- ('to be')."

**Descendants Listed:**
The page lists these language families as descendants:
- Proto-Celtic
- Proto-Balto-Slavic (Lithuanian, Proto-Slavic)
- Proto-Hellenic (Greek)
- Proto-Indo-Iranian (leading to Sanskrit and Avestan derivatives)
- Phrygian
- Old Persian

However, the document does not specifically itemize individual Avestan, Sanskrit, Greek, or Old Persian descendants by name—only their parent language groups, with references to "see there for further descendants."
```


### [2026-09-14T03:13:28.517Z] TOOL RESULT

```
# Persian Entry: بهشت

**Etymology:** The word derives from Middle Persian _𐭥𐭧𐭱𐭲𐭩_ (wahišt), ultimately from Old Persian _\*vahištah_, tracing back to Proto-Iranian _\*Hwáhišt-Háhuš_.

**Meaning:** "Paradise" or "heaven" in Persian. The entry notes a synonym in جَنَّت (jannat) and antonyms including دوزَخ (dōzax) and جَهَنَّم (jahannam), which refer to hell.

**Note on Avestan:** The provided content does not include Avestan forms—only Middle Persian, Old Persian, and Proto-Iranian etymological ancestry are documented in this Wiktionary entry.
```


## [2026-09-14T03:13:32.498Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87%D9%85%D9%86",
 "prompt": "Persian بهمن: etymology (Avestan Vohu Manah, Middle Persian Wahman), meanings. Quote."
}
```


## [2026-09-14T03:13:34.566Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA",
 "prompt": "Persian اردیبهشت: etymology (Avestan aṣ̌a vahišta, Middle Persian Ardwahišt), meaning. Quote."
}
```


### [2026-09-14T03:13:39.340Z] TOOL RESULT

```
# Bahman: Etymology and Meanings

## Etymology
**Bahman** derives from Middle Persian *wahman*, which traces back to Old Persian *Vahumanāh*. This was the name of the first Amahraspand (divine deity) in Zoroastrianism, guardian of cattle, corresponding to Avestan *vohu.manah*.

## Meanings

The term has multiple applications across Persian-speaking regions:

**As a Proper Noun:**
- The eleventh solar month of the Persian calendar
- The second day of any month in the Persian calendar
- A male given name

**As a Common Noun:**
- Avalanche
- Behen (a plant cultivated for flowers and its bitter, pungent root vegetable)
- Common awn-grass (*Stipa capensis*)

**In Gulf Arabic:**
Bahman also functions as a Kuwaiti family name of Persian descent, belonging to an ethnic group known as *ʕayam*.

The word demonstrates significant cultural and linguistic persistence across Persian, Arabic, and related traditions spanning millennia.
```


### [2026-09-14T03:13:40.008Z] TOOL RESULT

```
# اردیبهشت (Ordibehesht)

**What it is:** اردیبهشت is a Persian proper noun referring to the second month of the Persian solar calendar and the third day of any month in that calendar.

**Etymology:** The word derives from Middle Persian *Ardwahišt*, meaning "right." It's named after the second Amahraspand (divine deity) in Zoroastrianism. The term combines two elements: ارد (ard, "truth") and بهشت (behešt, "heaven").

**Pronunciation:** Various Persian dialects have slightly different pronunciations, ranging from /ʔar.diː.bi.ˈhiʃt/ in Classical Persian to [ʔʊɾ.d̪iː.be̞.ɦɪ́ʃt̪] in formal Dari.

**Position in Calendar:** Ordibehesht is the second of twelve Persian months, following Farvardin.
```


## [2026-09-14T03:13:42.402Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/eucalyptus",
 "prompt": "Etymology of eucalyptus: who coined it, when, from what Greek elements. Quote."
}
```


## [2026-09-14T03:13:43.355Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/swastika",
 "prompt": "Etymology of swastika: Sanskrit svastika, su + asti, and when it was adopted by the Nazi party. Quote."
}
```


### [2026-09-14T03:13:46.057Z] TOOL RESULT

```
# Etymology of Eucalyptus

**Who coined it:** French botanist Charles Louis L'héritier de Brutelle (1746-1800)

**When:** 1788 (the term entered English in 1789)

**Greek elements:** The word combines two Greek components:
- *eu* meaning "well"
- *kalyptos* meaning "covered"

**Reason for the name:** According to the source, it was "so called for the covering on the bud."

The botanist created this Modern Latin term to describe the evergreen genus native to Australia, referencing the characteristic operculum (cap-like covering) that protects the flower bud before it opens.
```


### [2026-09-14T03:13:47.829Z] TOOL RESULT

```
# Swastika Etymology

The term "swastika" originates from Sanskrit, derived from *svastika-s*, which literally means "being fortunate." This breaks down into *su-* (good) and *as-*, the root of *asti* (he is), both ultimately tracing to the Proto-Indo-European root *\*es-* (to be).

Historically, the symbol functioned as an ancient religious or cosmic emblem thought to bring good luck. It carried alternative names including gammadion, cross cramponnee, and Thor's hammer.

The word entered English around 1871 but took on a darker association when the Nazi regime appropriated it. As the source notes, "Use of the word in English in reference to the Nazi emblem is by 1932." The German term for the Nazi version was *Hakenkreuz*, translating to "hook-cross."
```


## [2026-09-14T03:13:55.220Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT Vaumisa ===\"\ngrep -n -i \"vaumisa\\|Vaumiça\\|vahyaz\\|Dārayavauš\\|Darayavaus\" KNT_full.txt | head -20\necho \"=== KNT vahu / naiba ===\"\ngrep -n \"vahu-\\|vahyazdāta\" KNT_full.txt | head -20",
 "description": "Grep Kent for Old Persian names"
}
```


### [2026-09-14T03:13:55.338Z] TOOL RESULT

```
=== KNT Vaumisa ===
2023:Darayavaus : 
3063:short passage (DB 3.38-51): Vahyazddtahyd 
6583:Personal name Vahyaz-data- ‘(Follower of) the 
8109:in personal name Vahyaz-dita (§120); zero grade -$ 
8346:ing à brave army’; Vahyaz-data- Following the 
8411:Marduniya-, Vaumisa- (with -s- which is not Per- 
8412:sian nor Median), Vayaspara-, Vahauka-, Vahyaz- 
9939:Comp. stem vah-yas- in Vahyaz-dàta- (for г, see 
13348:pears in the main clause of DB 2.62f Vaumisa сий 
13350:Madam ‘Vaumisa waited for me so long, until I 
14401:the second, the gen. DarayavauSahyd is repeated 
14428:Darayavaus XSühyà риса, АЎНЬ Darayavaus X Š 
16574:4 Darayavaus : xSayafflya : manā : pita : Vistàspa : Vistaspahyd : pità : Ars 
16587:9 апу: Darayavaus : xSdyaéiya : ҮШ : mana : taumayd : tyoty : paruvam 
16595:13 айту : Dārayavauš : xSayafiya : ima : dahyava : {уа : mand : paliyaisa : vain 
16614:24 ya :avafà :akunavayatà : Oatiy : Darayavaus : xšňyaðiya : Auramazdü 
16648:44 : Darayavaus : xSayafiya : айа : xSacam : tya : Gaumáta : һуа : magus : adin 
16778:: Gitiy : Darayavaus : xSiyadiya : pasiva : adam : Ва 
17117:5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 
17120:8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā 
=== KNT vahu / naiba ===
26497:tie of *ddraya-vahu-manah- ‘Holder of Good 
26891:placing GAv. vahu- ‘good’, and opposite of duš-
```


## [2026-09-14T03:13:59.150Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26485,26510p' KNT_full.txt\necho \"===== Vaumisa context =====\"\nsed -n '8405,8415p' KNT_full.txt\necho \"=====\"\nsed -n '13340,13355p' KNT_full.txt\necho \"===== lexicon Vaumisa =====\"\ngrep -n \"Vaumisa-\\|Vaumiéa\\|Vaumisa \" KNT_full.txt | head",
 "description": "Read Kent context for Darayavaus and Vaumisa"
}
```


### [2026-09-14T03:13:59.245Z] TOOL RESULT

```
JAOS 53.21, against 51.195-6). 


Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, 
king 522-486 ».c.; IT, son of Artaxerxes I, king 
426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- 
ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; 
Keiper, Acta Sem. Phil. Erlangen, 1.253). From 
pAr. *dháragat-, pic. to root in OP dar- (§162, 
§240), + pAr. *yasu asn. ‘the good’ (5158.1), see 
OP vau-: ‘He who holds firm the good’ (Hz. Arch. 
Hist. Iran 40, ApI 255, 267, takes as hypocoris- 
tie of *ddraya-vahu-manah- ‘Holder of Good 
Thought’; this is rejected by Nyberg, Rel. 361). 

Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 
6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 
81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 
64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 
54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 
45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 
5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1; 


190 OLD PERSIAN 

===== Vaumisa context =====
Kabüjiya-, Küru-, XSayarSan-, Gaubaruva-, Cifpi-, 
Darayavau-, Bardiya-, Vistüspa- (M). 

b. Names of other Persians: Artavardiya-, 
Ardumants-, Aspacanah- (M), Ulana-, Өилта-, 
Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, 
Marduniya-, Vaumisa- (with -s- which is not Per- 
sian nor Median), Vayaspara-, Vahauka-, Vahyaz- 
dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- 
manis-. 

=====
beginning of DPd, DNb, DSe, precisely as the 
aorist adà is used in DNa, DSf, and other inscrip- 


SYNTAX AND STYLE 91 


tions of Darius and Xerxes. Action in progress ap- 
pears in the main clause of DB 2.62f Vaumisa сий 
mam amünaya Arminiyary уйй adam arasam 
Madam ‘Vaumisa waited for me so long, until I 
reached Media’. There seems to be no difference 
of aspect between arasam in this clause and its 
compound in DB 2.65 уаба Madam pardrasam 
‘when I reached Media’. Habitual repeated action 
is seen in DB 1.23f yasasam hacüma afahya агаа 
===== lexicon Vaumisa =====
8411:Marduniya-, Vaumisa- (with -s- which is not Per- 
13348:pears in the main clause of DB 2.62f Vaumisa сий 
13350:Madam ‘Vaumisa waited for me so long, until I 
17178:49 dam : іу : Därayavauš : xšāyaðiya : pasáva : Vaumisa : nàma : Pārsa : manā : ba 
17182:51 hya : hamiciya : mana : naiy : gaubataiy : avam : jadiy : pasiva : Vaumisa : a 
17204:62 ya : jiyamnam : рабу : avatiSàm : hamaranam : kartam : pasàva : Vaumisa 
17448:Vaumisa marched off. When he arrived in Ar- 
17450:against Vaumisa to join battle. A district by name 
17462:against Vaumisa to join battle. A district by name 
17468:After that, Vaumisa waited for me in Armenia
```


## [2026-09-14T03:14:14.495Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Kent vau- lexicon ===\"\ngrep -n \"vau- \\|vau-:\\|^vau\" KNT_full.txt | head -10\necho \"---\"\nsed -n '26880,26900p' KNT_full.txt\necho \"=== BRT darayat ===\"\ngrep -n -i \"dārayaṱ\\|darayat\\.\\|dārayat\" BRT.txt | head -10",
 "description": "Kent vau- and Bartholomae darayat"
}
```


### [2026-09-14T03:14:14.585Z] TOOL RESULT

```
=== Kent vau- lexicon ===
8016:Déraya-vau- Vau-misa- Vahau-ka-; substantives 
14396:vaušahyā Artaxsagahya XShyà puça Artaxšaçahyű 
14398:vaušahyā XŠhyā puça D{éralyavausahya Vš- 
18715:roman type, which were not visible to KT :! Da]rayavau- 
26495:OP vau-: ‘He who holds firm the good’ (Hz. Arch. 
28714:vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the 
---
86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 
5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; 
DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy 
(836) DB 4.64. nai-ma DNb 8, 10, 19. nai- 
pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- 
diš ($136) DB 4.73, 78. 


naiba- adj. ‘beautiful, (religiously) good’, re- . 


placing GAv. vahu- ‘good’, and opposite of duš- 
karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē 
‘brave, good’ ($11, §75.V, $148.11). пафа nsf. 
DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 
20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 
43. 


naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап 
‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ 
=== BRT darayat ===
```


## [2026-09-14T03:14:17.749Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28710,28722p' KNT_full.txt\necho \"=== BRT dāraya ===\"\ngrep -n \"dāraya\\|daraya\\.\" BRT.txt | head -10\necho \"=== BRT col 1405 search ===\"\ngrep -n \"1405\\b\" BRT.txt | head -5",
 "description": "Kent vau- entry and Bartholomae"
}
```


### [2026-09-14T03:14:17.929Z] TOOL RESULT

```
29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy 
subj. mid. as pass. ($222.П) DNb 35. 


vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the 
good, (religious) goodness’: Av. nsm. vaphus, nsn. 
vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in 
Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-. 


Va'umisa- sb. ‘Vaumisa’, a Persian officer of 
Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. 
(Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ 
=== BRT dāraya ===
=== BRT col 1405 search ===
25616:•  ].,  g.  urvad-a-  Adj.  'amicus,  befreundet; Freund':  ntpaydis  mallm  '"him yavamiti .. aurva^äj  parö  du^malnyaot  mi  t?m  'htm fräyavaydis  sna%ai  .  .  Yt./.  34;  —  ÄvS. alava  zara>:uitrJ  •'inm  %rätärfm  isöit  1 (Sp.  28f,)  alavamm  te  aiaonat  afyeSiyai\ (sd.)  mraomi  '%>m  ''^■3^  Y.  77.  13;  — /r-ä\ n  vTsai  '"hB  staota  •'iigm  staotärim  van-  ■ AarfApfn(Sp.  1405*1.)  ..aax/a  aAurS  mazda^ ya\a  ..  V.10.9;  —  *dr3gubyS  vastär>m\ änasli  ya^a  'htm  spitamäi  \.  ig.  14; ¥.g; —  '%S  *brätä  *pt3  vü  Y.45.11;  — kvS  il  .  .  ahäm.bis  (sd)  '%5  Y.  44.  2 ; 30.6.  a)  mit  Dat.":  ki  "äff  spitamäi zard^uitrai  nä  matdä  "welcher  Mann ist  Freund  dem  SpZ.,  o  M.T  Y.jr.  11; 4ß.  14;  —  maida  dadäi  ahurS  . .  yS  A^i mainyri  iyao'ianäisca  'i^ö  ".  .  dem  . .,  der im  Geist  und  in  Werken  ihm  Freund  ist"  Y. 31. 2 1  '>.  b)  mit  Gen, :  »ä  J  bavahi  yasata- nqm  ydha  .,Az.4;—a.  noch  Y._J7. 3 1 ,  bei  a.
26514:Ständlich. •  j.,  g.  staotar-  m.  'Lobsänger':  fra- varäni  .  .  'tä  amtlanqm  spmianqm  yaitä amtlanqm  .  .  Y.  i2.  i ;  —  frä  t!  vTsäi urva'hif  'ta  V.io.g;  14.  i  (VJ),  Vr.5.  i;  — urva'h^m  'tar>m  »«»^«»^^«(Sp.  1405  u.) da'is  apxta  ahurS  .  .  yaiha  .  .  Y.  /O,  9; sara~^u!tra    'tanca    zaotarica  .  .  Yt  7.
```


## [2026-09-14T03:14:31.995Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(735,742):\n    s=leaves[i].strip()\n    print('=== leaf',i,'===')\n    print(s[:400].replace('\\n',' '))\n    print()\nEOF",
 "description": "Print Bartholomae leaves near col 1405"
}
```


### [2026-09-14T03:14:33.098Z] TOOL RESULT

```
=== leaf 735 ===
20.1,  Yt.18.%; Religion^)  'Spruch,  Vers;  Gebet;  Zauber-  —  u^ta  tl  apivaiahe  *p0uru  *va(qm** formel':  airiha  damayä  mqs  (sd.)  vaca  fr)zux%anqm  Y.p.as;  27,7;  —  a^S  .. (AP.)  dähänahe  nöit  iyao%fikil  apayanlake  växs  gnzux^B  */ramrvqnB  .  .  sfanvanti (sd.)  Y.5.31;  —  äxstaioa  damaya  vaca  (sd.)  H.7.4;  —  mihr^m  . .  yim  yaaata jramrß  V,  j,  i ;  —  ahunB  vairyB

=== leaf 736 ===
H.  2. 2;  —  bansnüm  hi  'mm pourum  "sein  Oberstes,  den  Vorderkopf V,i?.4o;  41;  —  ^baninvB  .  .  paiti  'nahe "zu  Oberst  des  Kopfes"  N.  6^.  b)  des Kamels:  ys  (nämL  uitrs)  kafim  aipi.- spaynti  . .  vpa  'mm  Yt  14. 13.  2)  'Kopf- stück, Oberstes'  (nur  Komp.).  Wertlos: tiamB  avi  xsmS  °rum  haha  urva  barmtt Vd.7.  [F.^g,  V.Ä43,  ().i6  i.St:  lies pasca.vayl':\ KompE

=== leaf 737 ===
d Feuer).     Praes.  3  uxi'a-,  26  vaxlya-,  27 'sprühen':  Hlfrlm  .  .y5  vTspäts  naeniiaiti (sd.)  sima  apaya  vazpdris  uxsyeitidBty ".  .  der  wegspült  mit  sprühendem  Wasser daherfahtend  . ."  Yt.  S.  43. mit  ä  'besprühen,  sprühend  benetzen': i  iaia  xä  . .  ä  i^ansajU  urvaranam  sBra vaxsyente'^  vaxSa  "wann  werden  die Quellen  . .  die  Wurzeln  der  Pflanzen  mit star

=== leaf 738 ===
Tätigkeitsbezeichnung)';  im  Gegensatz zu  Denken  und  Handeln  (oder  äbnl.),  A)  im gA^.:  at  til  mainyä  ..  manahicä  'cahicä syaohansi  hT  vahyS  ai>M(sd.)cä  Y.30.3; —  ipgrttä  mainys  vahistäcä  mananhä  . . fyaoianäcä  'canhacä  ahmSi  dqn  (Sp. 7120.)  .  .  Y.  4-].  1 ;  —  yS  ahm  dngväitl 'catshä  vä  at  vä  mananhä  tastdibjä  (sd.) vä  vaniaitt  Y.jy, »;  —  yS  dät  mono v

=== leaf 739 ===
pa  gduiisn, —  1)  Vgl.  V.  4.  3;  vaB  faoirim  m^tim  km- naoiti  und  apa.m}r>ta-  5p.  1143  m. •  j.  vatSah'ya-  n.  —  ?  — :  paiti.asti  gSul 'yeheca  Aa'liravataAeca ..Ytis.i.     Wertlos. •  j.  vaäö.marata-  Adj.  'mit  (vernehm- baren) Worten  aufgesagt,  rezitirt';  manS.- Mar^tanniiica'tanqmcaitiä.xai.sravarjAqmy^ "der  in  Gedanken  und  der  laut  rezitirten (Gebete)"  N.22. pü

=== leaf 740 ===
Eig.  Bed.?  —  ■)  Them.  —  '}  Hds.  vatara; '  ■  -      dy).  -   J)  S.  dazu  West  SEE.  24. 103.  ■ -  3»- •  j.  va8ay- :  vaili-  f.  'Wasserlauf,  Be- wässerungskanal': nil  tat  3p»m  hintatä ' yavd.caränlm  (sd.)  ana  tä  '%Tnt  ayä  ana bittm  . .  pasla  tüirJm  nasäum  ava.iansfnti (sd.)  "entlang  dem  Kanal  läuft  es  (das Wasser)  alsdann,  entlang  zum  zweiten Mal  . .,  da

=== leaf 741 ===
aes.  37 ufya: 'besingen,  einen  Sang  dichten  auf  — ' (Akk.):  *yavat3  %ivä  matda  *ilaomT ujyäcä  (iSPA,)  "(immer)  so  lang  ich  dich, Q  M.,  lobe  und  besinge"  Y.4:_J,  8;  — yS  va  asä  ufyäni  manaüS  vohQ  apaourvlm (sd.)  Y.  2Ä  3 ;  —  asäunqm  va>3uhJl . . fravalayS  staomi  zbayemi  ufyemi  Y,  ly.  18; —  k3  nB  stavat  .  .  yazäite  .  .  ufyät  .  . */rinät  .  .  paiti
```


## [2026-09-14T03:14:47.680Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,s in enumerate(leaves):\n    if 735<=i<=760:\n        m=re.findall(r'(vaiihu|vanhu|vaühu|va»hu|vaifhu|vaahu|varihu|vaqhu|vohu)', s)\n        heads=re.findall(r'•\\s*j\\.,?\\s*g?\\.?\\s*([A-Za-zāīūəṇṣšžθδγβŋ\\'\\.\\-]+)', s)\n        print(i, m[:5], heads[:8])\nEOF",
 "description": "Locate vanhu- entry leaf in Bartholomae"
}
```


### [2026-09-14T03:14:48.713Z] TOOL RESULT

```
735 [] ['vaiqm', "vaf'dana-"]
736 ['vohu'] ["'vax"]
737 [] ['ivax', 'vaxSad', 'vax', 'vax', 'kameit', 'yttvat', 'yai', 'vacas-taStay-']
738 [] []
739 [] ["vatSah'ya-", 'va', 'vafc', 'vad-', 'vada-']
740 [] ['va', 'vadar-', 'vaSairyav-', 'va', 'vaSut-', 'vawzaka-', 'g']
741 [] ['vafra-', "vefra'y", 'vattha-', "'vaBhan-", 'vaehana-', "'vanhav-", 'Hankav-', 'vaDhar-']
742 ['vaahu', 'vanhu', 'vanhu', 'vanhu'] ["vaDhaz-dih-'", 'vash', 'vaDh', 'vach', 'vaDh', 'vaohut', "vanhu'd", 'vanhuS']
743 ['vohu'] ['vaDhvi-']
744 [] ['vanatay-']
745 [] ['vanat-pa', 'vanana-', 'vanar-', 'vana-', 'van', 'vanamna-', 'van', 'vand-']
746 [] ['vant', 'vantav-', "'vay-", "'vaya-", 'Jvaya-', "'vayav-"]
747 [] ["'vayav-", 'vayah-', 'vavana-', 'vavanvah-', 'vavaz', 'vay']
748 [] ["ya'"]
749 [] []
750 [] ['svar-', "'varay-"]
751 [] ['varav', "'varah-", "'varah-", 'neil', 'saocayaca', 'varak-', 'vanka-', "'var"]
752 [] ['varaxv', "'varaeah-", "varadah'vant-"]
753 [] ['varaSa-', 'varada', "varvdatgaed'i-", 'varaSant-', 'varaJJ', 'varaJbmna-', 'varadusma-', 'varadva-']
754 [] ['varan', 'varanya-', 'varaman-', 'varamay-']
755 [] ['vairya.st', 'varasa-', 'varas', 'varfsma-', "varasma'p", 'varBsm', "'varaz-"]
756 ['vohu', 'vohu', 'vohu'] []
757 ['vanhu'] ['Jvar', 'varara-', 'varszai', "'var", 'var', 'varflzya-', 'varv']
758 [] ['var', 'var', 'var', 'varstva-', "'var", 'JvarSna-', "'varSnay-"]
759 [] ['varw', 'vaM', 'vas-', "vasaS'a-"]
760 [] ['vas', 'vas', 'TasD.gaoyaotay-', 'vas', 'vas', 'vas', "'vastra-"]
```


## [2026-09-14T03:14:57.039Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ns=leaves[741]\nimport re\ni=s.find(\"'vanhav-\")\nprint(s[max(0,i-200):i+1500])\nEOF",
 "description": "Print Bartholomae vanhav- entry"
}
```


### [2026-09-14T03:14:58.505Z] TOOL RESULT

```
.  y,  —  'lumca  Vd.  ig.
Zum  V.  ivah:  —  ai.  väsaaa-  n.  —  Pü.  (mV.)-. pa  kamvastrakih,  (lu  Vd,):  nihumbit  (3S.I).
•  j,  vaohant-  Adj.,  Pj-AomA,:  s.  ^van- mit  No.  II.
•  j.,  g.  'vanhav-  Adj.  (fem,  vanhvi-^: S.  tmter  vahttv,  Sp.  1395.
•  j,  'vaohav-  m.  EN.  eines  Gläubigen: 'tthSul  ar^eht  asaonS  Yt,  13. 1 08.
VgL  'vaaAirv:     VII.  Kotiname.
•  j.  Hankav-  n.  'Bluf.
KompA.;  Ableit.  (1.  iw*«").  ^-  VgL  vehum-, j.  vaahmiaäbyaila  N.  to8-.  lies  ai»hauaiibyäia.
•  j.  vaDhar-  (,  p.  vaAar-)  n.  'Frühling': wawri  (LS.)  F.  8.
Abteil.  (».  'iiaAara-).  —    aL  vaiar',  np.  iaAär.
—  Pü.;  taiä»-.
•  j.  vashars-Stä-  Adj.  'in  Kleidern  be- findlich, bekleidet"':  'itasaj''  ma^ivnlasat *irävaysit  "sowohl  bekleidet  ais  nackt soll  man  (die  Gs^äs)  aufsagen"  P.  ii ; N.  *<SjJ',  *83*,  *ios<i,  10g.  [S.  noch "varihtaahasla .]
*vanAar-  n,,  lum  V.  it/aA-.  —  Pü. !  viiäfaiii brähnaka  sräytl  ka!  Hin  luvän  AH  "«ach  Oboe Gürtel  und  Hemd  (t,  Sp.  IiSf.),  auch  (gani) nackt  loU  man  aufsagen,  so  wie  man  et  (eben) vermag".  —  ')  Jn.  Cama  Mem.  Vol.  I31 fibersetit  "with  one'«  clothing  thrown  off  i.  e, incompletely  dieiied"  und  leitet  f*  mit Haplologie  aas  *vaaAa-Aarsla-  her.  Die  auf- gestellte Bedeutung  verlangte  aber  vielmehr eine  Grundfor
```


## [2026-09-14T03:15:14.019Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('=== leaf 742 (col ~1407) ===')\nprint(leaves[742][:2500])\nEOF",
 "description": "Print Bartholomae leaf 742"
}
```


### [2026-09-14T03:15:15.044Z] TOOL RESULT

```
=== leaf 742 (col ~1407) ===
m  'Aia^sta-vasha-.  —  >)  Nach der  fl-DeU.  ~    3)  Hds.  varllas:    —    i)  Hds.
•  j.  vaDhaz-dih-'>,  va^haz-°  *>  Adj.  'der das  Bessere  gibt,  der  schenkt,  was  besser ist   (als  gut/:    vJspe  yazatanhö  ySi    'da
i(NP.)  aiavans  Y.  ffj.  12;  G.  2.  6,  FrW, .  i.  2".  a)  Name  einer  Bucht  des  Vmtru- \ka!la:  trayavhs  veuruJi<^aht  vairii  .  . ,yS  'da  nqma  Yt  ig.  59.
;       S  304  U.  5,   —    Vgl.  vaahudäk-.  —  PiL:    veh
dahak. —  ')  Oder  'da-;  %  383,  414.  —  *)  So,
mit  äk,  TiVi.  geschr.,  S  363.^0;  s.  auch  die
Var.  IU  Y.  65.
■  j.   vaiähah-,   vashah-  Adj.:   s.  unter
vaAyaA-.
\  •  j.  vashä-  f.  ein  Teil  des  RUckens(?)  '*: '  'Aam  F.  3  g.
kompA.(?J.  ~  Et,  und  Bed?  —  Yä.:  fiust  i pahan  'der  breite  Rücken'.  —  ')  Vgl.  ultAä-. \  •  j.  vaDhäpara-  m.  Name  eines  a^urischen ;  Tiers, 'Igel' 1  spämm  ilkänin  urvisarfm  yim <  'nm  yim  tnasyäka  avi  duivaeatsÄS  duiakftn \  (sd.)  nqma  aofaiU  "den  scheuen  spitz- j  schnauzigen  Hund  V.,  den  die  Ubelreden- !den  Leute  J).  nennen"  V./?.  2. '      Ob  Komp.  mit  i/a>tAä-i  —    Pü.:  transskr.  in
Aw..  Buchst. .  •  j.  vachäna-  Adj.,  PPM.:  s.  h/ah-.
dby  Google
1349
vatthanam
'viin-  2  A
1350
•  j.  vaDhänam  Absol.  'beimAnhaben,  Sich- ' kleiden  in— '(Akk.):  ar3dvtm..yä  hiitaite\ fravai^iimna  (Sp.  1 3 1 7  u.) . .  kainira  JbÄrpa srlrayä .  .frazuitm  a^tm  V  pouru.paxStsm ". .  in  einen  kostbaren  Mantel  gekleidet . ." Yt5. 126.
Zum  V.  iTiah-.  —  Vgl.  iF.  vavtuinim.
•  j.  "vaöhe  :  na^aia  V  paiti  usta  vaahö bvat  Vytjo;  —  räia  f  maidahäta  aiaoru \yl36.
•  j.  "ätara  vaohit  vanat^  (Sp.  1352  o.) V.7.S2  PüZ.
j.  ditö  vaahiti  V.  /p.  17:   lies  dätan  vaah-
•  j.  vaohutät-  t  'Blut':  aslqmia  vansamia spämamla  mOhrqmca  -tätqmca  Y.6.J;  29.
Auffällige  Bildung  ('languini/ai",).  —  Pü.:  xäa ta/U»ii.
•  j.  vanhu'däta-  m.  EN.  eines  Gläubigen: °taAe  i^aiätaAe  asaons  Ytij.  119.
Ableit.  ~~  Vgl.  voku.ääla',  vahyazdäla:  — Eig.  'von  den  guten  (Götlern,  s.  Y.  58-  S) gegeben'  oder  'gesc halfen'.  —  ai.  vgl.  vaiu- daita-  m.  EN.
•  j.  vanhuSätayana-  patr.  Adj.  'von Vavhiitäta  stammend,  dessen  Nachkomme*: utyeAe  fsd.)  -tayanake  Yt.  13.  1 19.
Ableit.  aus  va-ihulila..
•  j.,  g.  vaohu-däh-",  j.  °8äh-''  Adj.  'Gut, Gutes,  das  Gute  schenkend  i  —  schafiend': haikyö  'da  (NS.)  ye^hi  .  .  "er  ist  der rechte  Schenker  des
```


## [2026-09-14T03:15:23.668Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(760,785):\n    s=leaves[i]\n    nums=re.findall(r'\\b(1[34]\\d\\d)\\b', s)\n    print(i, nums[:6], s[:80].replace('\\n',' '))\nEOF",
 "description": "Find Bartholomae leaves with columns 1395/1405"
}
```


### [2026-09-14T03:15:24.786Z] TOOL RESULT

```
760 ['1382', '1383', '1386']  Belieben sva.  Freiheil  der  Bewegung,  Freiheit";  yf U  jyälSus  A}mi>yät  {
761 ['1387', '1388'] m  (sd.)   vag^sii  V.  4.46; —  yat  masyS  astahmat  *T3m "'  N.Sj;  — (cvat) 
762 ['1389']   ä  ahmSl  yai  aHn (näml  tifrii)  paitLapayat  vazimnS s^an- vantim  avi  gai
763 ['1390'] a- yasna  bai^azäi  {%A.)  fravazSnte  V.  7. 36. mit  nt  'nach  unten  führen,
764 ['1392']   S.  garay- No.  5. •  j.  vazö.v^S'wya- ■'  Adj.  'wegführend, raubend  was  z
765 ['1393', '1394', '1338'] , — ')  Im  Gegens,  lu  dav;  a.  V.  ig.  6,  7.  — »)  GDN.S  Fassung  von  a
766 ['1396', '1315'] igste  Geist,  der  die festesten  Himmel  als  Gewand  trägt"  Y. 30.  5.  Wert
767 ['1398', '1395'] ml  a  xla%'r8i Y.  49-  8.  b)  von  Personen,  uzw,  a)  von Menschen:  -nAJui
768 ['1396', '1398']     'hunqm    V.  3.  19; —  'rghuia  *vaiähasca  afrlnami  vlspayh aiaonS  stdi
769 ['1400', '1315', '1400', '1401'] )  mananhs  Y.32. 1 1 ;  — ■  'ta^a manatahs  hala  alat  syao%anaia  valaahalä 
770 []  . .  yqm  asahe °tahe  Vr.  23.  i.  b)  von  Personen  uzw. a)  von  Menschen:
771 [] üm  (sd.)  mazda  'mäi  a  fraor7t yasnqscä  Y.  _y.  a ;  •—  atcä  X . .  vtsp
772 ['1406'] aia  alam  yat  vahiltim "einen  Freund,  der  lobsingt,  nannte  .  . AhM.  noc
773 ['1408', '1409', '1410'] •  j-  vä(y)-  V.  'jagen'.     Praes.  i  va^yY: vy-,  3  vaya-,  'vya-'K  —  P
774 [] in;  vgl.  V.  j,  42, A.  4.  6,  H,  2.  7  (gegenübtr  H.  2.  25). •  j.  vä
775 ['1412', '1413']  seinem  Wohlgefallen"  Y.^.  a;  —  AS. mit  °a  (vanma)  als  Adv.  sbes.  a) 
776 ['1416'] sd.)  .  . a^  yai  *yayä  (GS£)  Y.6.e,o. Ableit.  aus  iz^r-,  —  ai.  värya- 
777 ['1319', '1417', '1418'] er-,  Wiesenmahd  bezeichnend  ist',  von MaihyBiüma  (sd.):  mat^iySiÜmtsm  'ta
778 ['1419'] ake  kainiki '«'■>  Y.  2^.3(?). Vgl.  gaväsiryavanz-.  —  Pü.!  iär  i/arutär. 
779 []  Y.  6.  50;  5.  50  (statt  NS.)j  —  ya^a  maisi Vihrkavatti  °kat  ha^a  ^fr
780 [] ao-.  — ooia.  >-aäj/0^^  YL*.I2.  a)    m.-l>    Gott    des ^irarprui  patrt.v
781 ['1433', '1307', '1425', '1496'] tm    vanaintTmia    upara- ,    Ableit  am  v>rAraina:  —  0  S  368.  32, dby 
782 []    antan    sairi  (sd.)    °zänt    V.  75. 17.        I  o)  imAp,  'cittä3>, 
783 ['1497', '1428'] dayasnsi! G.  2.  7,         S.  noch  v»r>zyata-  mit  No.  z. KompE.  —  Zum  
784 ['1429', '1430'] ffe)  erheben  gegen  Jemanden' des  .  .'  (Gen.):  äiar/  V  matää  ahurahya
```


## [2026-09-14T03:15:30.020Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ns=leaves[766]\nprint('=== leaf766 ===');print(s[:1800])\nEOF",
 "description": "Print Bartholomae leaf 766"
}
```


### [2026-09-14T03:15:31.089Z] TOOL RESULT

```
=== leaf766 ===
igste  Geist,  der  die festesten  Himmel  als  Gewand  trägt"  Y. 30.  5.  Wertlos:  vanhäna  x^aita  raoci :fanvaitT^ia  vsrtsU  Yt  j.  i.
mit  ni  'überziehen,  Überwerfen':  ym "utg)r»snävayö  (sd.)  *niva!3h>nti*^  yeii  .  , N.p4.
ai.  -aäiU,  väsänah.  —  Pfl.;  nihu/lan,  (zuN.^2 2.St.  und  F.  S):  (fia)  niAän,  {lu  N.  34):  mit kt  . .  afi  ätafendil.  —  >)  VgL  BV.  g.  97.  2 : väiträ  .  .  räiänai;  1.  No.  a.  —  >)  Vgl.  RV, 5.  29.  3:  väsinö  iliam.  S.  noch  Absol.  — J>  Hds.  vaite,  aber  Pü.  ni/uiß  wie  lu  Y.  ja  5, V.  4-  49  fü'  vaite;  Bthl.  IF.  zt.  134.  — 4)  Hdi.  nivanä;  i.  aber  Fü.  —  5)  Zu  ai.  drS- fdy-  m.  'Mantel,  Kleid';  vgl.  aach  draßa-. Dai  selbe  Verbnm  findet  sich  auch  N.  p3 (fol.  //O.  io).
•  p.  '''vahauka- '^  m.  EN.  eines  Persers:
dby  Google
I39S
■vanhav-  a
'vanhav-  b  s
1396
ardumanil  nama'  *kahya  fu%''<^  fiarsa" Eh.  4. 18.
Kntiname  mit  demKoseinffixauia-;  vgl.np. fuiarS  {bei  HoBN  GIrPb.  /  b.  185)   und  die EN.  ÄonWims,  Satlaim,  und  vll,  Dayaukku  - Jiiamii.  —   I)  NA,  vaAui-.    Da«  so  gelesen werden   könne,    hat   »nch   HOwng  IrEN.  3a nicht  erwiesen;  s.  daiu  auch  KZ.  j/.  510. •   p.   (vaAav- :  va*u-,)   j.,  g.  'vashav-: vaahv-,  vanhu-,  vohu-  (fem.  vatehvl-)  Adj, 'gut",  d.  i.  so  wie  etwas  oder  Jemand  ent- spiechend   seiner  Bestimmung  beschaffen sein  soll,  'geeignet,  tauglich,  günstig,  förder- lich, genehm,  gütig,  religiös  und  moralisch gut';    eine    scharfe    Scheidung    der    Be- deutungen ist  nicht  durchzuführen,    a)  im gAw.;   a)  von  Sachen:    damayä  'tshuyS »jrSä  Jyatr'^ana^ä  y. ^^.1 ;  jy.  ^i  —  'nkuyh
äsiBufßd.)  iyao^anai^Y.iS.  $;j6.4;  
von  "manoA- "  (Stverz.  Sp.  1137  f.):  ai  Äsi
```


## [2026-09-14T03:15:43.343Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD weh/wahist/wahman ===\"\ngrep -n \"^weh\\b\\|^weh \\|wahišt\\|wahist\\|^wahman\\|Wahman\\|ardwahišt\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n \"wahišt\\|vahišt\\|wahman\\|weh \" NYB_vol2_glossary.txt | head -15\necho \"=== HRN beh ===\"\ngrep -n -i \"vohu\\|vahista\\|behišt\\|bihišt\\|behešt\" HRN.txt | head -15\necho \"=== HUB ===\"\ngrep -n -i \"vohu\\|bihist\\|behist\\|vahista\" HUB.txt | head -15",
 "description": "Grep MacKenzie, Nyberg, Horn, Hübschmann"
}
```


### [2026-09-14T03:15:43.446Z] TOOL RESULT

```
=== PHD weh/wahist/wahman ===
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
PHD.txt:599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:3038:paradise  garódmàn, (garasmān), wahišt; (worthy) оў ~ garēdmānīg, wahištīg.
PHD.txt:3650:sigh swahistan.
PHD.txt:4384:Amahraspandan Wahman Ardwahišt (Urd-, Ašwahišt) Šahrewar Spandarmad Hordād Amurdād
PHD.txt:4388:I Frawardin II Ardwahišt III Hordad IV Tir V Amurdad VI Sahrewar
PHD.txt:4391:2 Wahman
PHD.txt:4411:VIII Abin IX Adur X Day XI Wahman XII Spandarmad + Frawardīgān
PHD.txt:4521:weh! wehīh! šabag
PHD.txt:5241:wasswarih naxsag waxšišn wahistig wahišt wüdám ` wādgirdag wād wādrang wüdrangboy wādbān nabānazdišt tāt
PHD.txt:5242:weh . nihānīg nihān wehih wehdin wihēz wihcz- wihczagig wihezag Iwiydbin wivüftan
PHD.txt:5280:nāydāg wahīg wihīr- nārīg wihīrišn nāysrāy nayizag wan- niyox&- niyox&idan niyoxiián wing wānīdan nān Worübarst Worüjarst nohom nihumb- nihumbidan Wahman naxust nihuftan
PHD.txt:5532:sohistan, swahistan
PHD_mackenzie.txt:1171:Ardwahist prtwhlt l I M 'rdywhy!t, (N urdibihift)] Right, the second
PHD_mackenzie.txt:1287:Aswahist [)lwMt l ] = Ardwahist.
PHD_mackenzie.txt:4724:• swahistan, swah- [swh-stn ' I P swh-] sigh.
PHD_mackenzie.txt:5147:Wahman [whwmn ' I M whmn, N bahman] Good Mind, the first Amahra-
=== NYB ===
375:amahraspand [^mhrspnd] the circle of the six divinities Vahuman, Art-/Urt-/vahišt,
655:Art-vahišt [?rtwhšt'] 402; Urt-vahiSt Pwrtwhst'] 39%,  A&a-vahist [?šwhšt'] 394-5, 401-4, 589. 593, 9727 one of the Amahraspands (g.v.). — art, urt < OlrSkr rta- ‘the right cosmic order, the divine law’, Av. (192) arata-, (349) orota-, (229 sqq.) aša- + vahista- (v. vahišt) 'the best, the heavenly law'. Asa-vahist is directly borrowed from Av. (233 sgg.); also the name of the 2nd month of the year and the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. Cf ahlav, ahläi, artči; Arta-xšahr "he whose dominion is (de- termined) by the divine law’.
734:Ašavahišt [”šwhšt'], v. Artvahišt.
3849:Urt-vahišt [Pwrtwhšt'] v. Art-vahišt.
3908:vahišt [whšt'] 1. the best: ~ 4 Urtvahist 3910; ~ rösneh 6378; with secondary sup. ending vahistom [whstwm] 1152. — 2. Pa- radise, passim; ~ u Garödmän 339-27, 343 twice; without u 3225. — Av. (1399 sqq.) vahista- sup. of vahu- (v.s. v. veh); M . PrthPrs whyst ‘Paradise’; NP bihišt.
3911:vahištik belonging to, destined to Para- dise 914,
4083:veh [wdh; SPYL] good, better, best, of Ohurmazd’s creation; sometimes placed before its headw.: 2719. 738. 7511-13, 1102; hàn i ~ Dāttī 565-15; regularly placed after: vāt 1 ~ 729; mēnēt i ~ 651° ete.; yazdān —-än 5511; together with den, v. this w.; as a comp. with hac ‘than’ 141, 411. 8617-15; as a pred. passim ; —as asubst.: ~ the good men, coll. of the Zoroastrians 611?; pl. cas. obl. —-än the good ones, the believers of the Zoroastrian religion: 5526, 6417 etc. passim; neutr.: ~ kartan to do good 925. 9920.24; — adv. well 1419. 891; better 692°. — Av. (1405 sq.) vahyah- to do good 925, 9970-24; — adv. well 1419, 891. — Av. (1405 sq.) vahyah- (vajhah-) comp. of (1395 sqq.) vahu-; Arm. lw. veh; MPrth why- in compounds (A-H III); MPrs why ‘better’, also wyhdr (A-H II); Paz. vah, vahé, veh, vih eto.; NP bih; sup. vahišt, g. v.
5021:aša + vahišta-: Artvahišt ašāvan-, ašavā: ahlav ašemaoya-: ahramēg Ašišvaņuhi: Ahrišvang ašta-: aštak
5045:ereta-: Art-vahišt
5416:tvah: viyāk vahišta-: vahišt vahyah-: vēh
6170:whyšt: vahišt
7007:ardī (urdī-), bihišt: Art-vahišt
7068:bihišt: vahišt
=== HRN beh ===
4616:aw. vohuni' *Blut'; phlv. yün, yUnömaud,
=== HUB ===
2011:Gerade np. ocun ist am schwersten mit zd. vohuni-
4492:bihist = bahist Paradies', zd. vahiSta- *beste' (sc. ahu-
4502:veh uberlegen, besser', ap. vahyaz-(data-) ^ zd. ntr. vohu,
5465:hist, bihist *Paradies* =■■ paz. vahest Shk. 270, Min. Gl. 204,
5466:zd. vahista-; bayo *Braut', skr. vadhu; bBxtan 'sieben = paz.
5536:= mp. ^vahiStazad Hoffmann, Ausziige p. 15, Nr. 100;
6712:zd. asa-vahista-; Farvardm 'der erste Monat' = phi. fra-
7624:bahist, bihist 'Paradies* = zd. vahista-; dih *Dorf\ arm. deh,
8438:hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-;
```


## [2026-09-14T03:16:00.486Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN bih/beh ===\"\ngrep -n \"bih\\b\\|bihtar\\|bihiSt\\|bihist\" HRN.txt | head -15\necho \"=== POK esu-s entry ===\"\nsed -n '28600,28640p' POK_full.txt\necho \"=== POK su- 1037 ===\"\ngrep -n \"Root / lemma: su-\\|Root / lemma: su\\b\" POK_full.txt | head",
 "description": "Horn and Pokorny"
}
```


### [2026-09-14T03:16:00.582Z] TOOL RESULT

```
=== HRN bih/beh ===
2458:241. bih 'besser, gut', bihln.
2464:Dr. Andreas schon vor mehreren Jahren mitgeteilt: bih,
2475:dings durch den Reim auf bih gesichert.
2518:246. bihiSt^ behist ^Paradies'.
2521:Die Aussprache behist ist die ursprüngliche ; in bihist
3424:ai. pitü'. Vergl. np. ferbih (No. 813).
7098:813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
7202:Verse {bih und girih). Ich stelle das Wort zu den
7203:von Andreas erklärten bih, kih, mih (No. 241).
7640:Zu np. kih vergl. unter bih (No. 241); phlv. kas,
8695:Vergl. zu bih (No. 241).
=== POK esu-s entry ===

doubtful, whether here Middle Irish eorna {* esor-n-Ja) 'barley'; 

References: WP. I 161 f., Trautmann 71, Feist 58 f. 
Page(s): 343 

Root / lemma: esu-s{\ su-) 

Meaning: good, *noble, master, owner, lord 

Material: Gr. £u^, nuc; "proficient, good'. Adverb su (Akk. n.), belongs to prefix £u- 

Hittite a-as-su-us (assus) "good'; to a- s. Pedersen Hittite 167 under Anm.; perhaps as 
zero grade in addition (Friedrich IF. 41, 370 f.) the prefix su- see there; 

moreover perhaps Latin erus' the master of a house, head of a family, mister, master, 
owner, lord ', fem. era, Old Latin esa^ mistress, lady '; 

however, Hittite is-ha-a-as {ishas) "master, mister' is to be kept away, because this 
belongs to Armenian /sa-s/? "master, mister', /5A'a/"rule, reign' (?), even it is not of Indo 
Germanic origin (Couvreur H 9); 

gall. GN Esi/s (with §■) remains far off, probably because of the names with Aes-, A/s- in 
the earliest 1. a/s- or 2. a/s- (above S. 16), less probably 2. e/s- (above S. 299); also the 
Old Irish PN Eogan {*ivogenos) and the cymr. PN Owe/n {o\6er Ywe/n, Euge/n, Ougen) = 
Old Irish PN Uga/ne {*ouo-gen/os), compare in addition Bergin Eriu 12, 224 f. 

References: WP. I 161, WH. I 419, 863. Bin etymol. Versuch by Kretschmer, object. 
Konjugation 16 ff. 
See also: es- 
Page(s): 342 

Root / lemma: es- 
Meaning: to be 

Note: 

Root/ lemma: es-\ "to be' derived from Root/ lemma: eg-, eg(h)om, egd\ I' [Old Indie 

asmi'\ am' = a/iam ( *eg(/i)om) 'I'] 

=== POK su- 1037 ===
71320:Root / lemma: sal- : salt; salty water derived from Root / lemma: su-ro-, sou-ro- : salty, 
83246:Root / lemma: su-, su- 
84507:Root / lemma: su-ro-, sou-ro- 
84546:Root / lemma: su-s, suu-6s
```


## [2026-09-14T03:16:04.018Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '83246,83290p' POK_full.txt\necho \"==== POK u̯esu- around p.1174 ====\"\ngrep -n \"Page(s): 1174\\|Page(s): 1173\\|Page(s): 1175\" POK_full.txt | head",
 "description": "Pokorny su- and wesu-"
}
```


### [2026-09-14T03:16:04.096Z] TOOL RESULT

```
Root / lemma: su-, su- 



Meaning: well, good 

Material: Old Indie su-, Avestan hu-. Old pers. u-, e.g. in Old Indie su-dr'u- "strong wood', 

su-bhaga- lucky, begliJekend', Avestan hu-baya-'good Ehegluek granting '; 

gr. UYin<; "fit, healthy' (*5^-^7/e5"wohllebend'); 

gall, su- (e.g. Su-carus=) eymr. /7y-^a/'"liebenswurdig', eorn. hy-, bret. he-. Old Irish su-, 
so- (e.g. su-thain^ eternal ', so-scel(a)e^Eyax\ge\\wxx\'); 

Germanie sJ-in Su-gambr/\/N, Old leelandie su-svgrtt 'Sehwarzamsel' ("die whole 
Sehwarze'); 

Lithuanian sudrus'horny, lustful, luseious'; Old Chureh Slavie Sbdravb ' u\/\r\q' , Czeeh 
zo'/'aKy (eompare above Old Indie su-dr'u-) ete.; Slavie *si>bozbje, Czeeh Zi&oz/'Besitztum' 
from *s-b-bog-b (= Old Indie subhaga-, above S. 107); 

su-\s zero grade to "s^e- (above S. 882 f.); eompare Old Indie sva- in sva-dha= su-dha 
" sweet drink, beverage, liquid whieh is swallowed to queneh one's thirst, draught, potion' 
(above S. 241), sva-dhita-= su-db/ta- 't\ght, firm, fit, healthy'; 

References: WH. II 512, E. Fraenkel Mel. Pedersen 443 ff., Vasmer 1, 450 f. 
Page(s): 1037-1038 

Root / lemma: suard- 

Meaning: to laugh 

Material: oapSavioc; 'hohniseh, spottiseh', aap5i^£iv 'hohnlaehen'; eymr. chwarddu, eorn. 

hwerthin. Middle Breton/7^e/'5//7 'laugh'. 

References: WP. II 517. 

Page(s): 1 040 

Root / lemma: suad- 

Meaning: sweet 

==== POK u̯esu- around p.1174 ====
92619:Page(s): 1173-1174 
92826:Page(s): 1174-1175 
92991:Page(s): 1175-1176
```


## [2026-09-14T03:16:07.081Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '92780,92830p' POK_full.txt",
 "description": "Pokorny page 1174 root"
}
```


### [2026-09-14T03:16:07.136Z] TOOL RESULT

```
still vappa, i/5/O/o'kahmiger wine '. 

Maybe alb. i/S/oa 'summer heat' 

References: WP. I 379 f., WH. II 732 f. 

Page(s): 1149-1150 

Root / lemma: yes-6{*hyes-) 

Meaning: ' you ' 

See also: see above S. 514 l/'u-). 

Page(s):1173 

Root / lemma: yesu- {*hyesu-) 
Meaning: good 

Material: Old Indie vasu- 'good' (in addition i/asK/"' night'), vasun. 'blessing, Besitztum, 
property, richness ' (das Subst. after pronunciation and ablaut das primare), Avestan 
varjhu-, vohuds.. Old Indie Kas/ya/? 'better', vasistha- 'best', Avestan vahya, vahistods.; 
alt-lllyrian Ves-cleves, compare Old Indie vasu-sravas-, 

Germanic in proper name, e.g. Wisu-rTh, -mar, also Wisi-Gothae; gall, in proper name as 
Bello-, Sigo-vesus, Vesu-avus, Old Irish */ei6'(only in den case oblique covered, e.g. Dat. 
Sg. feib) ' excellence ' from *uesu-a, febas^ excellence ', *febtu. Gen. febtadql 
'substantiae'; ablaut. Old Irish /d'good, Gute' {*uosu-)\ besides *uesu- in Irish fiu^ 
dignified, honorable ', cymr. gwiwds., bret. ^tv/bi/ 'cheerful', gall. UTsu-nx, about uesu- in 
asian. Sprachen s. Bossert Mitteil. Inst. Orientf. 2, 78 ff.; 

besides eus- (with metathesis as in gr. £upo(;from F£po(;) in: 



Gothic /us/za' better', /i/s//a"Erholung, Erieichterung' (after Wissmann, D. alt. Postverb. 
d. Germanic 72 ff. post-verbal to *iusilon, as //7//o"Entschuldigung, excuse, alleged reason 
' to *inilon)\ Old Church Slavic i//7ye 'better' (Kompar. to an *uno- from *eus-no-); 

lllyrian PN l/ese/zaTelicitas'; Latvian 1/^5^/5 "fit, healthy, heil, unbroken, unmarred, 
unscathed, undamaged '; Old Church Slavic veseli^, Czech veselyetc. 'cheerful'; 

Tocharian A wse, B yss/'night' as *uesu^ the good '. 

References: WP. 1311, Vasmer 1 , 191 f.. Frisk 594 f. 
See also: probably to ues-2. 
Page(s): 1174-1175 

Root / lemma: uag- : uag- {*huegh^ 

Meaning: to be bent
```


## [2026-09-14T03:16:18.852Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd1 uesu ===\"\ngrep -n \"vesu-\\|u̯esu\\|vasu-\\|vahista\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== IEC wesu/esu ===\"\ngrep -n \"wesus\\|esus\\|wesu-\\|^su-, \" IEC.txt | head -10\necho \"=== SKT eucalyptus/swastika/hygiene ===\"\ngrep -n -i \"eucalyptus\\|swastika\\|hygiene\\|^evangelist\\|Euclid\" SKT.txt | head -10",
 "description": "Walde-Pokorny, Mann, Skeat"
}
```


### [2026-09-14T03:16:18.960Z] TOOL RESULT

```
=== WLD Bd1 uesu ===
=== IEC wesu/esu ===
348:aksios (2) “like, equivalent, due, true, valid, right’. WP I, 36. Cf. aksulos Skt. aCChab; Av. a$0; Tokh. cf. asan; Kanic (name of a king at Kültepe) Kunut-ahsu- (cf. $nótos below); Arm. a£; Gk. áxios; MIr. aice, adj. ‘worth’; R cf. -oSij (in xor-ošij *good^). For OCS oxolü see aksulos, and for OCS oxvy see esus
3433:eds-, edsmn- “eating; food’. See ëd- and de- rivatives Per. aš ‘pap’; Lat. cf. sem-esus 'half-eaten'; OLat. cēsnās, pl., Lat. cena ‘mealtime’; Umb. cersnåf “food, supply’ (if fr. *ko-edsno-, -eds- na-); MHG as ‘carrion’; Du. aas ‘pasture’; OE æs, n. “food, bait, carrion’; Li. cf. ésena “fod- der”
3722:esros “good, fine, noble, grand'. Cf. es-mi, esulos, esus Lat. *ebrus (in in-ebrae aves 'inauspicious birds”); Ir. earr ‘noble, grand"
3731:esulos (1) ‘noble’. Cf. esros, esus, etc. Skt. ásurab; Av. ahuro; Hitt. assul, assulas “favour, greeting’; Dor. cf. eslós ‘noble, kind” beside Gk. esthlós, id. (cons. obscure); Lat. erulus “lord; Olr. éola “expert, wise’; Br. héal, hael ‘noble, generous’; OHG, OS er ‘man’; OE eorl “chief, noble, earl; ON jarl, id. jarl- (cpds. *noble-"). Cf. Srb. ohol ‘proud’?
3733:esus (əsus, su-) (1) ‘good, true’. Cf. su-, uesus. Cf. WP II 512; I, 161 Skt. cf. su-, px.; Av. hu-, id.; Arm. ge ‘rich, powerful; Oss. äx-, px. ‘good-; Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós; áotos (*osu- + Gk. -atos); Hitt. assus; Umb. (?) eruhu (suitable. A wd. of ambig. spg. and mng.); Ligurian (?) Esu- (in Esu- biani, an Alpine tribe); Mir eo (2) ‘goog’;
3745:esus (esos, esi-) (2) “animal, breath, being”. Cf. es-mi, etc. Skt. ásuh (Ð “breath, life; Av. àhus (2) ‘world, place’; cf. áha ‘mind’; áhva “self, being’; Per. ahü deer": Arm. cf. ir, -i, -av, a-st. ‘thing, fact’; irav ‘rightly’; iravi, adj. ‘true’ from a type *esiiə)
3746:esus (és-) (3) “god, demon’. Cf. esulos, etc. Skt. ásuh, id.; Av. áhus ‘lord’; Hitt. hassus ‘king’ beside eshas (‘master’. The u-st. with umlaut is functional; the a-st., IE o-st. is non- functional); Lat. erus, herus ‘master’; era, OLat. esa ‘mistress’; Gaul. Esus ‘God’; ON ass, i-st. “heathen god'
3859:9SUS, See esus, su-, uesus. Additional forms: Av. anhu- queried ‘good’ beside báhus, váhus ‘perfect; OW hy ‘bold’; Lüneburg Wend. wachwy 'robust
4557:ghaisos ‘lance, pole’. WP I, 528 Av. cf. gaesus ‘lancer’; Gk. khaios *shepherd's crook’; Hes. gaiós (Thrac. or Maced. (?) «lance, pole); Celt. LW in Gk. gaisos ‘javelin’; Olr. gaí, gáe, Ir. gai, gaoi ‘spear’; Gallo-Lat. gae- sum; Br. goaó, goaf, gwat; Cor. gew; W gwaew lance, javelin’, w. induced labialism; OHG gër, MHG geér(e); OE gàr; Du. geer “bias, crosscut, gore’; ON geirr ‘spear’, geiri ‘gore, gusset
5242:guiuos "live, alive, living’. (Variant *guiguos in Gmc.) WP I, 670 Skt. jiváh ; Av. jivyo; Ober jiva-; Per. ziba, jiva- ‘beautiful’; Hitt. cf. hwesus ‘alive’; hwitar ‘livestock’; Gk. bíos m. ‘life’; Lat. vivus; Osc. bivo-; OIr béu, béo, Ir. beo, gs bí; OW byw; cf. OW biw ‘livestock’; Br. Cor. béw, bew; Go. qius; OCS Zivü; Li. gyvas; Latv. dzīvs; Finn. LW kiivas "vehement
=== SKT eucalyptus/swastika/hygiene ===
6036:Evangelist,  writer  of  a  gospel.  (T. Lk  — Gk.)  O.  ?.rvan^tisU.^h  ev^nffi iffa  — Gk.  fta-yytAitfTT^f.- Gk.  fvayyiAdl a  reward  for  good  tidings.  gonieL^G e5,  well;  d77#Aio.  tidings,  fiom  dyytKttf messenger;  sec  An«ol.
24021:Eucalyptus,  a  genus  of  trees,  including the  blue  gum-tree.  (Gk.)  Latinised  from Gk,«5,  well;  icttXinrT«rt,co>JcicA,«Qxtt«ss^A The  reference  \»  \o  0[k&>ua<A  vv^si^»*^^'^ sumcoft.
```


## [2026-09-14T03:16:26.584Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC uesus ===\"\ngrep -n \"^uesus\\|uesus \" IEC.txt | head -5\necho \"---\"\ngrep -n \"uesus\" IEC.txt | head -5\necho \"=== WLD Bd1 check ===\"\ngrep -n \"vàsu\\|vasu- \\|vasistha\\|vahyah\" incoming/WLD/WLD_Bd1_pages.txt | head -10\necho \"=== WLD band3 ===\"\ngrep -n \"vesu\\|vasu-\" WLD_band3.txt | head -5",
 "description": "Mann uesus and Walde-Pokorny"
}
```


### [2026-09-14T03:16:26.687Z] TOOL RESULT

```
=== IEC uesus ===
20155:uesiios (uesios) “better, more, bigger'. Cf. uesus Skt. vásiyah, vásyah, adj. “better”; Per. bis, adj. ‘much, more’; cf. bihin, adj. ‘better, best’; bih ‘better’; Ir. feárr "better fearra, adj. ‘more’. (The radical arises in Gk. es-thlós ‘virtuous’)
---
3733:esus (əsus, su-) (1) ‘good, true’. Cf. su-, uesus. Cf. WP II 512; I, 161 Skt. cf. su-, px.; Av. hu-, id.; Arm. ge ‘rich, powerful; Oss. äx-, px. ‘good-; Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós; áotos (*osu- + Gk. -atos); Hitt. assus; Umb. (?) eruhu (suitable. A wd. of ambig. spg. and mng.); Ligurian (?) Esu- (in Esu- biani, an Alpine tribe); Mir eo (2) ‘goog’;
3859:9SUS, See esus, su-, uesus. Additional forms: Av. anhu- queried ‘good’ beside báhus, váhus ‘perfect; OW hy ‘bold’; Lüneburg Wend. wachwy 'robust
18436:-teros, à, om, comparative suffix; pronomi- nal extn. Skt. ut-tarab, à, am ‘outer’; cf. itara, invar. ‘other’; kataráh “which, of two’; Av. cf. kataro, prn. id.; Oss. kadär, Iron. Cídár ‘someone’; Per. bih-tar, bah-tar (Cbetter', see uesus); bad- tar, bat-tar ‘worse’; Tokh. lyu-tàr, prn. ‘more’; Hitt. kat-taras lower; Gk. hüs-teros (“last': Skt. uttarah); Alb. ja-tér “other”, tje-tër, id.; Lat. de-ter ‘bad, weak? exter & exterus ‘foreign’; MIr. air-ther, adj. (front, eastern": Lat. prac- ter "before, beyond, beside"); Go. (and com. Gmc.) hva-par (^which, of two’. See quoteros); OE hwæðer, id. beside hider, pider “hither, thither’; OCS vü-torü ‘other’; Cz. úterý (*den) ‘Tuesday’; OCS koteryí, kotoryí, prn. ‘which’; Li. añ-tras ‘other’; katràs, à ‘which, of two'; Latv. otrs, adj. "other": katrs, adj. "each", Cf. quoteros (ioteros)
20155:uesiios (uesios) “better, more, bigger'. Cf. uesus Skt. vásiyah, vásyah, adj. “better”; Per. bis, adj. ‘much, more’; cf. bihin, adj. ‘better, best’; bih ‘better’; Ir. feárr "better fearra, adj. ‘more’. (The radical arises in Gk. es-thlós ‘virtuous’)
=== WLD Bd1 check ===
=== WLD band3 ===
```


## [2026-09-14T03:16:35.896Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^uesus\\b\" IEC.txt | head; grep -n \"uesus (\" IEC.txt|head\necho \"---- try line ----\"\nawk 'NR>=20150 && NR<=20175' IEC.txt | grep -n \"uesu\" \ngrep -n \"uesu\" IEC.txt | sed -n '1,20p'\necho \"=== WLD sizes ===\"\nwc -c incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt 2>/dev/null\necho \"=== WLD Bd1 sample p311 ===\"\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nprint(len(t))\ni=t.find('vesu')\nprint(i, t[i-200:i+400] if i>0 else 'not found')\nfor pat in ['vasu','vahista','vohu']:\n    j=t.find(pat); print(pat, j)\nEOF",
 "description": "Find Mann uesus and check WLD"
}
```


### [2026-09-14T03:16:37.093Z] TOOL RESULT

```
---- try line ----
6:uesiios (uesios) “better, more, bigger'. Cf. uesus Skt. vásiyah, vásyah, adj. “better”; Per. bis, adj. ‘much, more’; cf. bihin, adj. ‘better, best’; bih ‘better’; Ir. feárr "better fearra, adj. ‘more’. (The radical arises in Gk. es-thlós ‘virtuous’)
3733:esus (əsus, su-) (1) ‘good, true’. Cf. su-, uesus. Cf. WP II 512; I, 161 Skt. cf. su-, px.; Av. hu-, id.; Arm. ge ‘rich, powerful; Oss. äx-, px. ‘good-; Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós; áotos (*osu- + Gk. -atos); Hitt. assus; Umb. (?) eruhu (suitable. A wd. of ambig. spg. and mng.); Ligurian (?) Esu- (in Esu- biani, an Alpine tribe); Mir eo (2) ‘goog’;
3859:9SUS, See esus, su-, uesus. Additional forms: Av. anhu- queried ‘good’ beside báhus, váhus ‘perfect; OW hy ‘bold’; Lüneburg Wend. wachwy 'robust
13894:quasos, ios (basket. Cf. quesel-, quesul-. WP I, 507 Lat. cf. quas-illus, -illum, mn., id.; OCS (and com. Sl.) kosi, m. id.; cf. also Cz. košina, f. *basketry'
14001:quesel-, quesul- (?) *wicker; basket'. Cf. qua- SOS Cz. cesle, f. “wicker sluice, catchment hurdle’; Li. keselys, m. *wicker-basket'; Latv. kesele, f. *fish-trap, crab-pot'; Lat. (?) quasillus, um, mn. (‘wicker basket" may be r-gde fr. *quosil-, but cf. quasos. Phonology of quatuor: Li. keturi?)
18017:suesios “apart, alone; own, private’. Cf. suetios, suesue, seue, suelos, etc. WP II, 455. See next. (Variants in Iran.) Per. xwi$ “own; self; kinsman, son-in-law'; xwisan ‘kinsfolk’; xi3i, s. ‘kinship’; Kurd, xó$ ‘kinsman’; Oss. sáxi “they, themselves; their”; pn. (self; wäx ‘quality, nature’; xion, Dig. xewon, adj. “own, akin’; Hom. Gk. heós, adj. "own": Gk. eia, npl. (1) ‘provisions’; Umbr. swesu-, adj. own: Lat. cf. suere, inf. "ae custom’; cf. sé-par ‘unequal; Ir. seise, m. ‘comrade’; Go. swes, adj. own: n. ‘property’; OHG swas, adj. as Go. MHG swas, sm. or n. ‘closet, privy’; swàs-, cpds. ‘private’; OS cf. swēslīk, adj. own: OE sw&s, adj. ‘own, inti- mate"; Icel. svás ‘beloved’; OCz. cf. (?) svést, f. ‘mother-in-law’; Latv. svešs, adj. “foreign
18024:suesue (suosue), suésu, sus- 'so, thus, as; anyway' Kurd. xo ‘so, well: Umb. svesu ‘so, thus"; Mir feib, Ir. féibh as: Go. swa ‘so’; swaswe "as": OE swa, swaswa & swæ ‘so’; Norw. Sw. sá, Du. zoo, id. beside Du. zus, id.
18436:-teros, à, om, comparative suffix; pronomi- nal extn. Skt. ut-tarab, à, am ‘outer’; cf. itara, invar. ‘other’; kataráh “which, of two’; Av. cf. kataro, prn. id.; Oss. kadär, Iron. Cídár ‘someone’; Per. bih-tar, bah-tar (Cbetter', see uesus); bad- tar, bat-tar ‘worse’; Tokh. lyu-tàr, prn. ‘more’; Hitt. kat-taras lower; Gk. hüs-teros (“last': Skt. uttarah); Alb. ja-tér “other”, tje-tër, id.; Lat. de-ter ‘bad, weak? exter & exterus ‘foreign’; MIr. air-ther, adj. (front, eastern": Lat. prac- ter "before, beyond, beside"); Go. (and com. Gmc.) hva-par (^which, of two’. See quoteros); OE hwæðer, id. beside hider, pider “hither, thither’; OCS vü-torü ‘other’; Cz. úterý (*den) ‘Tuesday’; OCS koteryí, kotoryí, prn. ‘which’; Li. añ-tras ‘other’; katràs, à ‘which, of two'; Latv. otrs, adj. "other": katrs, adj. "each", Cf. quoteros (ioteros)
20155:uesiios (uesios) “better, more, bigger'. Cf. uesus Skt. vásiyah, vásyah, adj. “better”; Per. bis, adj. ‘much, more’; cf. bihin, adj. ‘better, best’; bih ‘better’; Ir. feárr "better fearra, adj. ‘more’. (The radical arises in Gk. es-thlós ‘virtuous’)
=== WLD sizes ===
4327601 incoming/WLD/WLD_Bd1_pages.txt
2833963 incoming/WLD/WLD_Bd2_pages.txt
 317372 WLD_band3.txt
7478936 total
=== WLD Bd1 sample p311 ===
4216315
1507482 t/d, vuhUto ds.: germ in Eigennamen, z. B. Wisu-rlh, -mtlr,
auch (s. Streitberg IF. 4, 300 ff.) Wisi-Gofhac (das trotz Frantzen KZ. 42,
320 nicht zu dt. TI7c.ce); gall, in Eigennamen vie Bello-, Sigo-vesus, V<‘*u-
avns,     ir.   (nur in den Ivasus obliqui belegt, z. B. Dat. sg. feih) ,.Yor-
                *fel>

trefflichkeit" aus *uesu-d, fehus ..Yortreffliehkeit", *fehtu, gen. fehtad gl.
..substantiae", cymr gwyih ..frohlich"
                                 .        daneben *Hesu- in ir. ftu „wiirdig‘
                                                             ;
                         
vasu 876851
vahista -1
vohu 1507223
```


## [2026-09-14T03:16:41.978Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=1507223\nprint(t[i-900:i+300])\n# find nearest page tag\nimport re\nseg=t[:i]\nm=list(re.finditer(r'\\[pdf page (\\d+)\\]', seg))\nprint('LAST TAG:', m[-1].group(0) if m else None)\nEOF",
 "description": "Walde-Pokorny uesu- entry context"
}
```


### [2026-09-14T03:16:42.897Z] TOOL RESULT

```
bundener Biischel starken Grases" (aus *inzda-s):
schwundstufig vielleicht (nach Petersson IF. 24, 262 f.) ai. itsnlsc:- m. „Kopf-
binde. Turban" (wenn auf Grand eines *us-n7- ..Drehung, Wickel"), ni-
nth a ,,Genickwirbel, PI. Genick" („*Wirbel k                             !




   Aber russ. v'eha s. inner nets- ..drehen" (nicbt nacli Petersson aus *iiesu )
auch seine Heranziehung von gr. ootoi^ov ..Stall, Hiirde" verdient nicbt
den Vorzug vor Bezzenbergers BB. 27, 174 allerdings auch unsicherer Yer-
bindung des gr. Wortes mit ahd. tar ..geflochtener Zaun".
                                                        <




uesu- ,,gut" (voller tuts-,                s. u.).

  Ai. rd'ii- ..gut". vdsti n. ..Gut, Besitztum,                                   Habe. Reichtum" idas Subst.
nach Akzent und       Ablaut das primiire. das Adj. daraus erwachsen nach
Brugmann II 2 I, 178), av. vawhn-s, vohu ds., ai. vastydn ..besser", vosiitha-
,.best", av. vaht/d, vuhUto ds.: germ in Eigennamen, z. B. Wisu-rlh, -mtlr,
auch (s. Streitberg IF. 4, 300 ff.) Wisi-Gofhac (das trotz Frantzen KZ. 42,
320 nicht zu dt. TI7c.ce); gall, in Eigennamen vie Bello-, Sigo-vesus, V<‘*u-
avns,     ir.   (nur in den
LAST TAG: None
```


## [2026-09-14T03:16:49.239Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff', t.count('\\f'))\ni=1507223\nprint('leaf', t[:i].count('\\f'))\nimport re\nprint(re.findall(r'\\[[^\\]]{0,30}page[^\\]]{0,20}\\]', t[:5000])[:5])\nleaves=t.split('\\f')\nprint(repr(leaves[0][:200]))\nEOF",
 "description": "WLD leaf index"
}
```


### [2026-09-14T03:16:50.323Z] TOOL RESULT

```
ff 894
leaf 318
[]
'            GOVERNMENT OF INDIA\n ARCHEOLOGICAL SURVEY OF INDIA\n\n               CENTRAL\n            ARCHEOLOGICAL\n                LIBRARY\nACCESSION NO. jj03?7\nCALL No. gJ3 Wafjpok\n                 f_\nD'
```


## [2026-09-14T03:16:58.385Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87#Persian",
 "prompt": "Persian به (beh) meaning 'good/better': give its etymology (Middle Persian weh, Avestan vaŋhu-/vahyah-, Proto-Iranian) and note the comparative بهتر. Quote."
}
```


## [2026-09-14T03:16:59.735Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hygiene",
 "prompt": "Etymology of hygiene: Greek hygieia/hygies, from PIE *su- 'good' + *gwei- 'to live'. Quote the entry."
}
```


### [2026-09-14T03:17:04.187Z] TOOL RESULT

```
# Persian به (beh) - Etymology and Meaning

## Meaning
The word به (beh) in Persian means "good" or "better" in archaic usage, functioning as an adjective.

## Etymology
According to the Wiktionary entry, the word traces back through several language stages:

- **Middle Persian**: weh ("better, good")
- **Old Persian**: *vahuš* ("good")
- **Proto-Iranian**: *Hwáhuš*
- **Proto-Indo-Iranian**: *Hwásuš*
- **Proto-Indo-European**: *h₁wésus* ("good")

## Related Form
The comparative form **بهتر** (behtar, "better") is derived from this root, demonstrating how the ancient word evolved within Persian morphology.

The entry notes this is an archaic sense, with the modern synonym being **خوب** (xub, "good").
```


### [2026-09-14T03:17:04.455Z] TOOL RESULT

```
# Etymology of Hygiene

Based on the Online Etymology Dictionary, the word "hygiene" has an interesting origin story that doesn't match the premise in your request.

According to the source, hygiene comes from **French *hygiène*, ultimately from Greek *hygieine techne* ("the healthful art").** The Greek root *hygies* means "healthy, sound, hearty," literally "living well."

However, the etymological breakdown differs from what you suggested. The dictionary traces it to the PIE root **\*eyu-gwie-es-** meaning "having a vigorous life," derived from **\*aiw-/\*ayu-** ("vital force, life, long life, eternity"), not from the roots you mentioned.

The entry notes: "The difficult spelling in English is a relic of the struggle to render the Greek vowels into French."

The term was personified as the goddess Hygieia in Greek culture and was used by Aristotle as a noun meaning "health."
```


## [2026-09-14T03:17:21.925Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%91%CE%B3%CE%B9%CE%AE%CF%82",
 "prompt": "Give the full etymology section of Ancient Greek ὑγιής: which PIE reconstruction is preferred, what Beekes says, and whether the older *su-gʷih₃-es- 'living well' analysis is mentioned. Quote."
}
```


## [2026-09-14T03:17:22.870Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Darius",
 "prompt": "Etymology of the name Darius: Old Persian Darayavaush, meaning, elements. Quote."
}
```


### [2026-09-14T03:17:26.453Z] TOOL RESULT

```
# Etymology of Darius

The name Darius comes from Old Persian *Darayavaus*, which likely means "he who holds firm the good." This etymology traces back to the Proto-Indo-European root *dher-, meaning "to hold firmly, support."

The name is most famously associated with Darius the Great, who ruled as Persian emperor from 521-485 B.C.E. The root *dher- is also found in modern English words like "firm," "affirm," and "firmament," as well as Sanskrit *dharmah* (custom or law) and Greek *thronos* (seat).
```


### [2026-09-14T03:17:27.569Z] TOOL RESULT

```
# Etymology of Ancient Greek ὑγιής

The word derives from Proto-Indo-European with two proposed reconstructions:

1. **Preferred analysis**: *h₂yu-gʷih₃-* ("long life")
2. **Alternative analysis**: *h₁su-gʷih₃-* ("good life")

According to the entry: "the former derivation is favored by Beekes and Weiss."

The entry does not explicitly discuss an older *su-gʷih₃-es- analysis or provide detailed commentary from Beekes beyond this brief preference statement. Both reconstructions are presented as legitimate etymological possibilities, with the "long life" derivation receiving scholarly preference, but no extended historical discussion of competing theories is provided in this section.
```


## [2026-09-14T03:17:39.072Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ Injil ===\"\ngrep -n -i \"injil\\|Injīl\\|euangelion\\|ewangeliyon\\|Evangel\" FVQ.txt | head -10",
 "description": "Jeffery on Injil"
}
```


### [2026-09-14T03:17:39.134Z] TOOL RESULT

```
=== FVQ Injil ===
10776:the Injil or what resembles them ", 1 
14097:and the Injil, and xxv, 1, and ii, 181, make it practically the equivalent 
14158:may have thought of as similar to the Taurah and the Injil. This 
14584:for the Jews or Injil for the Christians. 1 It thus looks as though the
```


## [2026-09-14T03:17:41.560Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D9%88%DA%A9%D8%A7%D9%84%DB%8C%D9%BE%D8%AA%D9%88%D8%B3/",
 "prompt": "What do Dehkhoda / Mo'in / other Persian dictionaries say about اوکالیپتوس — its meaning and stated origin (French/Latin)? Quote."
}
```


### [2026-09-14T03:17:45.058Z] TOOL RESULT

```
Based on the provided content, I cannot find specific information about what Dehkhoda, Mo'in, or other Persian dictionaries say about the origin of اوکالیپتوس (eucalyptus).

The page mentions that these dictionaries are included in Abadis' resources: "دانشنامه عمومی، دانشنامه اسلامی" and references to "لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید" but does not quote their specific definitions or etymological information about this term.

The only etymological reference provided is the English scientific name in parentheses: (eucalyptus), with no mention of French or Latin origins stated explicitly.
```


## [2026-09-14T03:17:49.750Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"إنجيل\\|انجيل\\|Injil\\b\" FVQ.txt | head\necho \"--- context around 10776 ---\"\nsed -n '10760,10790p' FVQ.txt\necho \"=== TAD/AFM انجیل ===\"\ngrep -n \"انجيل\\|إنجيل\" AFM.txt TAD.txt 2>/dev/null | head -5",
 "description": "Find Jeffery Injil entry"
}
```


### [2026-09-14T03:17:49.833Z] TOOL RESULT

```
10776:the Injil or what resembles them ", 1 
14097:and the Injil, and xxv, 1, and ii, 181, make it practically the equivalent 
14158:may have thought of as similar to the Taurah and the Injil. This 
14584:for the Jews or Injil for the Christians. 1 It thus looks as though the 
--- context around 10776 ---
Olo sarium, 194. 

Vide Sprenger, Leben, ii, 395. 

Zimmern, Akkad. Fremdw, 29, takes the Arabic form as derived from Aramaic. 

Mutaw, 54, 59. 



FOREIGN VOCABULARY OF THE QUR ? AN 171 

Bekri, Mu'jam, 369, 18, we read of how a<J-Dahhak entered a Christian 
monastery while the monk was reading #ju-*-i j* i^**-, and 

Ibn Duraid, 103, says that Sifr means " the volume of the Torah or 
the Injil or what resembles them ", 1 

It is clearly a borrowing from Aramaic. 2 The common Heb. "15?? 
appears in Aram, as N"]9P ; Syr. ];W>- From Aram, it passed 
on the one hand into Eth. as tl&, and on the other into Arm. as 
un^fy. As the Arm. word seems to have come from Syr., 3 we may 
suppose that it was from the same source that the Arabs got the word. 

J x- 

*'jA-~> (Safara). 

Ixxx, 15. 

^ i ** 
=== TAD/AFM انجیل ===
```


## [2026-09-14T03:17:55.058Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"Injll\\|Inpl\\|wangel\\|Evangelium\\|evangel\" FVQ.txt | head -10",
 "description": "Search Jeffery for Evangelium"
}
```


### [2026-09-14T03:17:55.168Z] TOOL RESULT

```
704:Tawral^ Injll, Sakina, Firdaus, Jahannam, are equally familiar to all 
814:the Taurah and the Christians the Injll. Later writers have a still
```


## [2026-09-14T03:18:00.475Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Injll\" FVQ.txt | head -20\npython3 - <<'EOF'\nimport re\nt=open('FVQ.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Inj[il1l]{2}', t):\n    pass\n# search for the headword section\ni=t.find('J^j\\\\')\nfor kw in ['euayyeAiov','eiayyeAiov','evayyeAiov','Aiov','Ge\\'ez','Eth. ']:\n    j=t.find(kw); print(kw, j)\nEOF\ngrep -n \"Aiov\" FVQ.txt | head",
 "description": "Locate Jeffery Injil headword"
}
```


### [2026-09-14T03:18:01.628Z] TOOL RESULT

```
704:Tawral^ Injll, Sakina, Firdaus, Jahannam, are equally familiar to all 
814:the Taurah and the Christians the Injll. Later writers have a still 
euayyeAiov -1
eiayyeAiov -1
evayyeAiov -1
Aiov -1
Ge'ez 52159
Eth.  111595
```


## [2026-09-14T03:18:13.946Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81su-' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%B4%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%87%D9%85%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D9%87' \\\n 'https://en.wiktionary.org/wiki/%E1%BD%91%CE%B3%CE%B9%CE%AE%CF%82' \\\n 'https://www.etymonline.com/word/eucalyptus' \\\n 'https://www.etymonline.com/word/swastika' \\\n 'https://www.etymonline.com/word/hygiene' \\\n 'https://www.etymonline.com/word/Darius' ; do\npython3 tools/fetch_source.py \"$u\" --note 'pdf page 486, root Su 1/Esu/Wesu part 3: verification of Avestan vohu/vahišta, NP beh/behešt/Bahman/Ordibehešt/Dāriuš, Greek eu-/hygies, swastika' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T03:18:17.576Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0796cdb8411b4cf9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce14895e9777692e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/857276e855e98cef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ecc18995313c60ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2526bb3410bd3e69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82403dbcdb00f47c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14d9f6da68b94717.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b650c66cc7deea31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d17b5a0d1e92f99b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b080c79e2f290a5e.txt
```


## [2026-09-14T03:18:20.144Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T03:18:20.188Z] TOOL RESULT

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


## [2026-09-14T03:20:32.083Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:31:06.916Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-486.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Su 1, Esu, Wesu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁su- 'good, well' (prefixal/adverbial) beside the adjective *h₁wésu- 'good' — Pokorny's esu-s (p. 342), su- (p. 1037) and u̯esu- (p. 1174)\",\n \"note\": \"Nourai's three-way headword 'Su 1, Esu, Wesu' is simply Pokorny's three lemmas put side by side, and his three page references are each exactly right: POK 342 'esu-s (: su-) Meaning: good' (Gk. ἐŰς/ἠŰς, adv. εὖ, Hitt. aššuš), POK 1037-1038 'su-, sū- Meaning: well, good' (OI su-, Av. hu-, OP u-), POK 1174-1175 'u̯esu- Meaning: good' (OI vasu-, Av. vaŋhu-, vohu-, OI vasyah, vasiṣṭha-, Av. vahya, vahišto). Klein p. 548 s.v. eu- ties the same set together: 'Gk. eu, prop. neut. of ἐŰς \\\"good\\\", which is cogn. either with Hitt. ashshush \\\"good\\\", or — more probably — with OI. vasuh, Avestic vohu-, \\\"good\\\", Ir. feb (fr. I.-E. *wesw-a) \\\"excellence\\\"'. The language label (Indo-European) and the gloss ('well, good') are correct. The only reservation is that the relation between *h₁su- and *h₁wésu- is still unsettled: Wiktionary calls *h₁su- a 'possible metathesis of *h₁wes- (good), or perhaps related to *h₁es- (to be)', and Watkins treats esu- as an 'extension of es-' — so joining Su/Esu/Wesu in one box is a scholarly choice, not an established fact. This is PART 3 of the root; the Latin/Germanic derivatives sit on other pages.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁su- «خوب، نیک» (پیشوند) در کنار صورت صفتی *h₁wésu- «خوب». نورایی سه مدخل جداگانهٔ پوکورنی را (esu-s در صفحهٔ ۳۴۲، su- در ۱۰۳۷ و u̯esu- در ۱۱۷۴) یکجا زیر یک عنوان آورده و هر سه ارجاع دقیق است؛ کلاین نیز در صفحهٔ ۵۴۸ همین پیوند را میان یونانی eu-، سنسکریت vasu- و اوستایی vohu- می‌کشد. پس نام ریشه، برچسب زبانی و معنی هر سه درست است. تنها نکته آن که نسبت *h₁su- با *h₁wésu- — آیا قلب آوایی است یا هر دو از *h₁es- «بودن» — هنوز در پژوهش امروزی قطعی نیست، و بنابراین یکی دانستن هر سه صورت در یک جعبه انتخاب مؤلف است، نه امری مسلّم.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81su-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:342\", \"status\": \"supports\", \"note\": \"POK_full.txt l.28606: 'Root / lemma: esu-s (: su-) — Meaning: good, *noble, master, owner, lord. Material: Gr. ἐŰς, ἠŰς \\\"proficient, good\\\". Adverb su (Akk. n.), belongs to prefix εὐ- ... Hittite a-as-su-us (assus) \\\"good\\\" ... Page(s): 342'. Exactly the 'Esu' of Nourai's headword.\"},\n   {\"ref\": \"POK:1037\", \"status\": \"supports\", \"note\": \"POK_full.txt l.83246: 'Root / lemma: su-, sū- — Meaning: well, good. Material: Old Indic su-, Avestan hu-, Old Pers. u-, e.g. ... gr. ὑγιής \\\"fit, healthy\\\" (*su-gʷiyes- \\\"wohllebend\\\") ... Page(s): 1037-1038'. Exactly the 'Su 1' of the headword (and note that Pokorny himself puts ὑγιής here).\"},\n   {\"ref\": \"POK:1174\", \"status\": \"supports\", \"note\": \"POK_full.txt l.~92800: 'Root / lemma: u̯esu- (*hu̯esu-) — Meaning: good. Material: Old Indic vasu- \\\"good\\\" ... Avestan vaŋhu-, vohu- ds., Old Indic vasyah \\\"better\\\", vasiṣṭha- \\\"best\\\", Avestan vahya, vahisto ds. ... Page(s): 1174-1175'. This single sentence underwrites the whole of node #1.\"},\n   {\"ref\": \"KLN:548\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.13764 s.v. eu-: 'combining form meaning \\\"good, well\\\". — Fr. Gk. eu, \\\"well\\\", prop. neut. of ἐŰς, \\\"good\\\", which is cogn. either with Hitt. ashshush, \\\"good\\\", or — more probably — with OI. vasuh, Avestic vohu-, \\\"good\\\", Ir. feb (fr. I.-E. *wesw-a), \\\"excellence\\\". Eu- is the opposite of dys-.' The local scan carries no printed folios, but the entry is Klein's eu- that Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 311 (WLD_Bd1_pages.txt, leaf 318)\", \"stance\": \"supports\", \"note\": \"'uesu- \\\"gut\\\" (voller u̯eus-, s. u.). Ai. vásu- \\\"gut\\\", vásu n. \\\"Gut, Besitztum, Habe, Reichtum\\\" ... av. vaŋhuš, vohu ds., ai. vásyān \\\"besser\\\", vásiṣṭha- \\\"best\\\", av. vahyā, vahišto ds.; germ. in Eigennamen, z. B. Wisu-rīh, -mār ... gall. Bello-, Sigo-vesus ... ir. feib \\\"Vortrefflichkeit\\\" aus *uesu-ā'. This is the page Pokorny cites (WP. I 311).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. esu- and su- (AHD_watkins1985.txt ll.462, 1033)\", \"stance\": \"supports\", \"note\": \"'esu-. Good. Extension of es-. Greek eūs, good, combining form eu-, well: EU-. [Pok. esu-s 342.]' and 'su-. Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. 2. Compound *su-gʷiə-es-, \\\"living in good condition\\\" (see gʷei-). [Pok. su- 1037.]' Watkins keeps esu- and su- apart from u̯esu- (he has no *wesu- lemma at all).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. esus (1) and əsus\", \"stance\": \"supports\", \"note\": \"'esus (əsus, su-) (1) \\\"good, true\\\". Cf. su-, uesus. Cf. WP II 512; I, 161. Skt. cf. su-, px.; Av. hu-, id.; ... Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos ... Hitt. assus'; and 'əsus. See esus, su-, uesus.' Mann too cross-links all three shapes.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71 GOOD, p. 1176\", \"stance\": \"supports\", \"note\": \"'1. Prefix IE *su-, Walde-P. 2.512 ... Skt. su-, Av. hu-; Grk. ὑ- in ὑγιής \\\"in good health\\\"; Gall. Su- in proper names, Ir. so-, W. hy-.' and 'Grk. εὖ-, the semantic equivalent ... beside Hom. ἐŰς, ἠŰς \\\"good, brave\\\", prob. : Hitt. assus \\\"good\\\" fr. IE *es- \\\"be\\\".'\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vohu, vahu; vahya, vahištô\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan has one adjective with several stem shapes: nom. sg. m. vaŋhuš, n. vohu, weak stem vaŋhu-/vaŋhv- 'good' (Bartholomae AiW col. 1395 lemmatises it '(p. vahav-: vahu-), j., g. ¹vaŋhav-: vaŋhv-, vaŋhu-, vohu- (fem. vaŋhvī-) Adj. \\\"gut\\\" ... geeignet, tauglich, günstig, förderlich, genehm, gütig, religiös und moralisch gut'). Its comparative is vahyah- (n. vahyō 'better', AiW col. 1405) and its superlative vahišta- 'best' (AiW col. 1399ff.). Nourai's four citation forms are therefore exact: vohu (n. sg.), vahu (the Old Persian/stem shape vahu-, OP nom. vauš), vahya (compar.) and vahištô (superl., nom. sg. m. vahištō). Phonologically Proto-Iranian *Hwahu- < PIE *h₁wésu-: the PIE *-e- appears as Av. a, the *w- is kept, and the -ŋh- of vaŋhuš is the regular Avestan outcome of *-nh-/*-sw- sandhi in the strong cases. Pokorny p. 1174 lists exactly this quartet (Av. vaŋhuš, vohu ds. ... Av. vahyā, vahišto ds.) beside Skt. vasu-, vasyah, vasiṣṭha-, so the arrow 'IE root → Avestan' is as well founded as an arrow can be.\",\n \"derivation_fa\": \"در اوستایی یک صفت با چند صورت ستاکی هست: vaŋhuš (نهادی مذکر)، vohu (خنثی) و ستاک ضعیف vaŋhu-/vahu- به معنی «خوب، نیک»؛ صورت برتر آن vahyah- (نهادی vahyō «بهتر») و صورت برترین آن vahišta- «بهترین» است. بارتولومه همین مجموعه را در ستون‌های ۱۳۹۵ تا ۱۴۰۷ فرهنگ ایرانی باستان آورده است. این صورت‌ها از ایرانی باستان *Hwahu- و آن از هندواروپایی *h₁wésu- می‌آید و هم‌ریشهٔ سنسکریت vasu-، vasyah، vasiṣṭha- است. پوکورنی در صفحهٔ ۱۱۷۴ دقیقاً همین چهار صورت را برمی‌شمارد؛ پس ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81su-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1174\", \"status\": \"supports\", \"note\": \"Pokorny 1174-1175 s.v. u̯esu-: '... Avestan vaŋhu-, vohu ds., Old Indic vasyah \\\"better\\\", vasiṣṭha- \\\"best\\\", Avestan vahya, vahisto ds.' — Nourai's node is a verbatim excerpt of this line (POK_full.txt, the 'Page(s): 1174-1175' block).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 1395/1396 (BRT.txt leaf 766), with the cross-reference at col. ~1347 (leaf 741)\", \"stance\": \"supports\", \"note\": \"col. 1395 heading '¹vaŋhav- a / ¹vaŋhav- b': '• p. (vahav-: vahu-), j., g. ¹vaŋhav-: vaŋhv-, vaŋhu-, vohu- (fem. vaŋhvī-) Adj. \\\"gut\\\" ... religiös und moralisch gut'. At leaf 741 the alphabetical place of vaŋhav- carries only 's. unter vahuv, Sp. 1395'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 311\", \"stance\": \"supports\", \"note\": \"'... av. vaŋhuš, vohu ds., ai. vásyān \\\"besser\\\", vásiṣṭha- \\\"best\\\", av. vahyā, vahišto ds.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, s.v. veh and vahišt\", \"stance\": \"supports\", \"note\": \"'veh ... Av. (1405 sq.) vahyah- (vaŋhah-) comp. of (1395 sqq.) vahu-'; 'vahišt ... Av. (1399 sqq.) vahišta- sup. of vahu-'. Nyberg's column numbers confirm the internal structure of Bartholomae's article.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71 GOOD, p. 1176\", \"stance\": \"supports\", \"note\": \"'Skt. vasu- (Vedic in this sense; later mostly as neut. sb. \\\"goods, wealth\\\"), Av. vaŋhu-, vohu- ...'\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"beh «به (بهتر ، بهترین)»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian به beh 'good, better' continues Middle Persian weh (Book Pahlavi <wdh>, Aramaeogram SPYL; MacKenzie 'weh, wehih') with the regular Iranian → Persian change of initial *w- to b- (cf. Av. vāta- > NP bād, Av. vīsaiti > NP bīst). Nyberg derives MP veh directly from the Avestan comparative vahyah- (AiW 1405), which explains why beh already means 'better' as well as 'good'; Wiktionary instead starts from the positive OP *vahuš < PIr. *Hwáhuš — both routes end in the same PIE *h₁wésus and the difference is only which Old Iranian stem was generalised. The forms بهتر behtar and بهترین behtarīn are New Persian re-formations: once beh had become a plain positive, Persian rebuilt the degrees with the productive suffixes -tar and -tarīn (Mann lists 'Per. bih-tar, bah-tar' under his comparative suffix -teros and 'bihin, bih' under uesiios). The 'extra' words in the box are compounds in beh-: بهزاد Behzād and بهروز Behrūz are old (MP Wehzād, Wehrōz), while بهداشت behdāšt 'hygiene', بهداری behdārī 'health service' and بهبود behbūd 'improvement' are 20th-century coinages of the Farhangestān built on the same morpheme.\",\n \"derivation_fa\": \"«به» فارسی دنبالهٔ فارسی میانهٔ weh است و تبدیل واو آغازین ایرانی به باء در فارسی نو دگرگونی آوایی قاعده‌مندی است (قیاس کنید vāta- > باد، vīsaiti > بیست). نیبرگ weh را مستقیماً از صورت برتر اوستایی vahyah- می‌گیرد — و همین توضیح می‌دهد که چرا «به» هم «خوب» و هم «بهتر» معنی می‌دهد — حال آنکه ویکی‌واژه آن را از صورت سادهٔ پارسی باستان *vahuš می‌داند؛ هر دو راه به همان ریشهٔ هندواروپایی می‌رسد. «بهتر» و «بهترین» ساختهٔ تازهٔ فارسی نو با پسوندهای زایای ‌-تر و -ترین است، نه بازماندهٔ صورت‌های کهن. از میان مشتقات جعبه، «بهزاد» و «بهروز» کهن (پهلوی Wehzād، Wehrōz) و «بهداشت، بهداری، بهبود» ساختهٔ فرهنگستان در سدهٔ ۱۴ خورشیدی است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%A8%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BRT:1405\", \"status\": \"supports\", \"note\": \"AiW col. 1405 is Bartholomae's article vahyah- 'besser' — confirmed independently by Nyberg s.v. veh: 'Av. (1405 sq.) vahyah- (vaŋhah-) comp. of (1395 sqq.) vahu-; Arm. lw. veh; MPrs why \\\"better\\\" ... NP bih; sup. vahišt'. So the column Nourai cites is precisely the one that yields NP beh.\"},\n   {\"ref\": \"BQT:322\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 322 (BQT_v1_pages.txt leaf 542) headword «به — بکسر اول و سکون ثانی ، بمعنی خوب و نیک باشد» with Mo'in's footnote 1: 'وهو vohu صفت است بمعنی خوب و نیک و به «بارتولمه ۱۳۹۵» ، سانسکریت vasu ، پارسی باستان (u)vahu ، پهلوی weh'. Note that Mo'in cites Bartholomae col. 1395 (the positive) where Nourai cites 1405 (the comparative).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 241 'bih' (HRN.txt l.2458)\", \"stance\": \"supports\", \"note\": \"'241. bih \\\"besser, gut\\\", bihln.' Horn also discusses (l.2464 ff.) Andreas's account of bih/kih/mih as the inherited short comparatives.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt l.4502)\", \"stance\": \"supports\", \"note\": \"'veh \\\"überlegen, besser\\\", ap. vahyaz-(data-) = zd. ntr. vohu'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. weh (PHD.txt l.4521)\", \"stance\": \"supports\", \"note\": \"'weh, wehīh' listed in the Pahlavi glossary; MacKenzie's English index gives 'good ... weh'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. veh (NYB_vol2_glossary.txt l.4083)\", \"stance\": \"supports\", \"note\": \"'veh [wdh; SPYL] good, better, best ... as a comp. with hac \\\"than\\\" ... — Av. (1405 sq.) vahyah- (vaŋhah-) comp. of (1395 sqq.) vahu- ... NP bih; sup. vahišt'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. uesiios and -teros\", \"stance\": \"supports\", \"note\": \"'uesiios (uesios) \\\"better, more, bigger\\\". Cf. uesus. Skt. vásiyah, vásyah \\\"better\\\"; Per. bis ... bihin \\\"better, best\\\"; bih \\\"better\\\"' and 'Per. bih-tar, bah-tar (\\\"better\\\", see uesus)'.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\", \"words\": \"vahu-man; vah-išta; vau-misa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three are genuine Avestan, the third is Old Persian. (a) vahu-man = Av. vohu- manah- 'Good Thought', gen. vaŋhəuš manahaŋhō, the first Aməša Spənta of the Gathas; the compound is vohu 'good' + manah- n. 'thought, mind' (PIE *men-), so the gloss should be 'good-minded / of good thought' rather than Nourai's loose 'well mannered'. (b) vah-išta = Av. vahišta-, the regular superlative of vahu- with the IE superlative suffix *-isto- (AiW 1399ff.); in the phrase vahišta- ahu- 'best existence' it is the Zoroastrian name of paradise, whence Nourai's gloss 'best (place), heaven'. (c) vau-misa is NOT Avestan: it is Old Persian Vaumisa-, the name of a Persian officer of Darius who fought in Armenia (DB 2.49-63). Kent's lexicon s.v. Va'umisa- explains the form Nourai marks with a question mark: 'a Persian officer of Darius: Elam. ma-u-mi-iš-ša, Akk. ú-mi-is-si, Gk. (Plutarch) ...; cpd. of vau- and miθra- \\\"friend\\\"' — i.e. 'having good Mithra', with an -s- that Kent notes 'is not Persian nor Median'. Nourai took the pair Dāraya-vauš / Vau-misa straight out of Buck p. 1176, where they are expressly labelled 'OPers. only in proper names'; carrying them into an 'Avestan' box is the mislabelling that keeps this node from 'confirmed'.\",\n \"derivation_fa\": \"دو واژهٔ نخست اوستایی‌اند و سومی پارسی باستان. vohu- manah- «اندیشهٔ نیک» نام نخستین امشاسپند است و از vohu «نیک» و manah- «منش، اندیشه» ساخته شده؛ بنابراین معنی آن «نیک‌اندیش» است نه «خوش‌رفتار». vahišta- صورت برترین vahu- با پسوند هندواروپایی *-isto- است و در ترکیب vahišta- ahu- «بهترین هستی» نام بهشت است. اما Vaumisa اوستایی نیست؛ نام سرداری پارسی در سنگ‌نبشتهٔ بیستون است که کنت آن را مرکّب از vau- «نیک» و miθra- «مهر» می‌داند — یعنی پرسش نورایی (؟) پاسخ دارد. برچسب زبانی جعبه برای این واژه نادرست است، پس ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%A8%D9%87%D9%85%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"SYN:1176\", \"status\": \"partial\", \"note\": \"Buck p. 1176 (SYN.txt leaf 1264) reads: 'Skt. vasu- (Vedic in this sense; later mostly as neut. sb. \\\"goods, wealth\\\"), Av. vaŋhu-, vohu- (OPers. only in proper names, as Dāraya-vauš, Vau-misa) : Gall. -vesus ..., Gmc. Wisu-rīh, -mar, Wisi-Gothae'. The page is exactly Nourai's source for 'vau-misa', but Buck labels it Old Persian, not Avestan.\"},\n   {\"ref\": \"KLN:169\", \"status\": \"partial\", \"note\": \"Klein's page ~169 (KLN_1966.txt l.4678) is s.v. behen: 'the plant Centaurea behen. — Arab. bahman, in vulgar pronunciation behmen, fr. Pers. bahman, a kind of root resembling a large radish.' It attests the Persian word bahman but says nothing about vohu manah, and it belongs to the Persian box (#4) rather than to the Avestan one.\"},\n   {\"ref\": \"KLN:401\", \"status\": \"partial\", \"note\": \"Klein's Darius entry (KLN_1966.txt l.10341, in the d- run that in the 1966 vol. I falls around p. 401) is relevant to node #5/#6, not to this node; see there for the quotation.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 1395ff. (vaŋhav-) and 1399ff. (vahišta-)\", \"stance\": \"supports\", \"note\": \"Bartholomae lemmatises vaŋhav-/vohu- and, in the same run, the many vohu-/vaŋhu- compounds (e.g. vaŋhu-dāh- 'Gutes schenkend', vaŋhaʒ-dāh- 'der das Bessere gibt', leaf 742 cols. 1349-50).\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.vv. vau- and Va'umisa-\", \"stance\": \"supports\", \"note\": \"'vau- adj. \\\"good\\\"; nt. as sb. \\\"the good, (religious) goodness\\\": Av. nsm. vaŋhuš, nsn. vohu, Skt. nsm. vásuṣ, nsn. vásu, pIE *u̯esu-; in Dārayavau-, Vaumisa-, Vahauka-, Vahyazdāta-.' and 'Va'umisa- sb. \\\"Vaumisa\\\", a Persian officer of Darius ... cpd. of vau- and miθra- \\\"friend\\\"'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Wahman\", \"stance\": \"supports\", \"note\": \"'Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahraspand, guardian of cattle; cal. 11th month; 2nd day.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. vahišt\", \"stance\": \"supports\", \"note\": \"'vahišt [whšt'] 1. the best ... 2. Paradise, passim ... — Av. (1399 sqq.) vahišta- sup. of vahu- (v.s.v. veh); M./PrthPrs whyšt \\\"Paradise\\\"; NP bihišt.'\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"Bahman «بهمن»; behešt «بهشت»; goštây «گشتای»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Bahman and behešt are impeccable; goštāy is a lexicographers' ghost. (a) بهمن: Av. vohu manah- > MP Wahman/Wahuman (Book Pahlavi <whwmn'>, Manichaean whmn) > NP Bahman, name of the first Aməša Spənta, of the 11th month and of the 2nd day of every month; Mo'in glosses it exactly '[نیک منش]'. The medial -hu-ma- of Avestan was contracted already in Middle Persian, and MP a > NP a. (b) بهشت: Av. vahišta- (ahu-) 'best (existence)' > MP wahišt <whyšt> 'paradise' > NP behešt, with the same *w- > b- as in beh; Wiktionary reconstructs the phrase as PIr. *Hwáhišt-Háhuš, and Mo'in's footnote in Borhan (pp. 327-329) spells it out: 'weh (خوب) + išt (علامت تفضیل)؛ بمعنی خوبتر، نیکوتر و آن صفت تفضیلی است برای موصوف محذوف که ahu (جهان، هستی) باشد و جمعاً بمعنی جهان بهتر'. (c) گشتای: Borhan's own headword is گشتا 'بهشت را گویند که بعربی جنت خوانند' (p. 1819), and Mo'in's footnote there says flatly 'قرائتی از رسم الخط پهلوی wahišt (بهشت)' — i.e. it is not a phonetic descendant at all but a mis-reading of the Pahlavi spelling <whyšt>, which the Persian lexicographical tradition (and the Sanaa'i verse quoted from Rašīdī) then treated as a real word. So Nourai's third arrow leads to the same Avestan etymon, but through a scribal accident rather than through speech; that is why the node cannot be called 'confirmed'.\",\n \"derivation_fa\": \"دو واژهٔ نخست بی‌اشکال‌اند و سومی واژه‌ای موهوم است. «بهمن» از اوستایی vohu manah- از راه فارسی میانهٔ Wahman آمده و معین آن را درست «[نیک منش]» معنی کرده است. «بهشت» از vahišta- (ahu-) «بهترین هستی» از راه پهلوی wahišt به فارسی رسیده و حاشیهٔ معین بر برهان قاطع (ص ۳۲۷–۳۲۹) دقیقاً همین تجزیه را می‌آورد. اما «گشتای» — که برهان در ص ۱۸۱۹ آن را «بهشت» معنی کرده — به گفتهٔ خود معین «قرائتی از رسم‌الخط پهلوی wahišt» است؛ یعنی زادهٔ بدخوانی خط پهلوی است نه دگرگونی آوایی، هرچند سرانجام همان واژه است. پس دو پیکان نخست درست و پیکان سوم با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%A8%D9%87%D8%B4%D8%AA\", W + \"%D8%A8%D9%87%D9%85%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:326\", \"status\": \"supports\", \"note\": \"The بهشت run begins on Borhan p. 326 and its footnote spills over on p. 327 (BQT_v1_pages.txt leaf 547): '... (خوب) و ایست (علامت تفضیل)، بمعنی خوبتر، نیکوتر و آن صفت تفضیلی است برای موصوف محذوف که ahu (جهان، هستی) باشد ... پهلوی wahišt ... فردوس، خلد، جنت'.\"},\n   {\"ref\": \"BQT:328\", \"status\": \"supports\", \"note\": \"Borhan p. 328 (leaf 548) is the بهمن article; Mo'in's footnote: '«وهو» بمعنی خوب و نیک و «منه» از ریشهٔ manah بمعنی منش: پس بهمن یعنی به‌منش، نیک‌اندیش، نیک‌نهاد. طبری ... گوید: تفسیر بهمن بالعربیة: الحسن النیة. وی یکی از امشاسپندان ... است'.\"},\n   {\"ref\": \"BQT:1819\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:1819 (vol. 3 pdf p. 616): headword 'گشتا — بضم اول و فوقانی بالف کشیده. بهشت را گویند که بعربی جنت خوانند'; footnote 10: 'قرائتی از رسم الخط پهلوی wahišt (بهشت). رک: بهشت و رک: باروچا ص ۳۳۶' — followed by exactly the Sanaa'i couplet the chart quotes ('زانکه گشتای خوب کاران راست / جمله عقبی حلال خوارانست').\"},\n   {\"ref\": \"BQT:101\", \"status\": \"supports\", \"note\": \"Borhan p. 101 (leaf 311, whose running head reads اردیبهشت) is the اردیبهشت article — it belongs to node #6 rather than here; verified and quoted there.\"},\n   {\"ref\": \"MON:327\", \"status\": \"partial\", \"note\": \"Only the 2-volume Adena abridgement of Mo'in is on disk, so p. 327 of the 6-volume Amir Kabir set cannot be checked. The content is supported: MON_part1.txt l.26464 'بهشت: [بهترین (جهان)] (امر.) جایی خوش آب و هوا ... جنت، فردوس، خلد' and l.26524 'بهمن: [نیک منش] (اح.) یکی از امشاسپندان ...'.\"},\n   {\"ref\": \"ZMA:19\", \"status\": \"not_checked\", \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian (Bonyad-e Neyshabur 1374) is purchase-only; refs_online.json records 'Searched archive.org, ketabnak, noorlib, web: not found.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. wahišt, Wahman\", \"stance\": \"supports\", \"note\": \"'wahišt [whšt' | M whyšt, N bihišt] paradise. ~īg [-yk' | N -ī] (worthy) of paradise.' and 'Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahraspand ...'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. vahišt\", \"stance\": \"supports\", \"note\": \"'— Av. (1399 sqq.) vahišta- sup. of vahu- (v.s.v. veh); M./PrthPrs whyšt \\\"Paradise\\\"; NP bihišt.'\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt ll.4492, 5465, 7624)\", \"stance\": \"supports\", \"note\": \"'bihist = bahist \\\"Paradies\\\", zd. vahišta- \\\"beste\\\" (sc. ahu-)'; 'hist, bihist \\\"Paradies\\\" = paz. vahest ... zd. vahista-'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (2-vol. Adena ed.) s.vv. بهشت, بهمن\", \"stance\": \"supports\", \"note\": \"'بهشت: [بهترین (جهان)]' and 'بهمن: [نیک منش] ... یازدهمین ماه سال شمسی'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 1819 (Mo'in's note 10)\", \"stance\": \"partial\", \"note\": \"Supports the identity goštā = behešt but explicitly calls the form a misreading of the Pahlavi script, not a regular descendant.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"aša-vahišta, artha-vahišta; dâraya-vauš, dârayat-vahu\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The first member of each pair is right; the language label is half wrong. (a) Aş̣a Vahišta 'Best Truth/Right' is the second Aməša Spənta of the Gathas: aş̣a- 'truth, right order' (PIE *h₂er-, the same *rta- that gives OP arta-) + vahišta- 'best'. Nourai's doublet 'aša-vahišta, artha-vahišta' mixes the Avestan and the Old Persian/Median shapes of the first element; Nyberg makes exactly this point s.v. Art-vahišt: 'art, urt < OIr/Skr rta- \\\"the right cosmic order, the divine law\\\", Av. arata-, ərəta-, aş̣a- + vahišta- \\\"the best, the heavenly law\\\"'. 'Best justice' is a defensible but loose rendering of 'best truth/right order'. (b) dāraya-vauš is Old Persian, not Avestan: Dārayavauš, nom. of Dārayavau-, the throne name of Darius I; Kent's lexicon: 'From pAr. *dhārayat-, ptc. to root in OP dar-, + pAr. *vasu asn. \\\"the good\\\", see OP vau-: \\\"He who holds firm the good\\\"'. Nourai's second citation form 'dārayat-vahu' is precisely that unattested Proto-Aryan participial reconstruction, not an attested Avestan word — which is why it too should not sit in an 'Avestan' box. Kent records the competing view (Herzfeld: a hypocoristic of *dāraya-vahu-manah- 'Holder of Good Thought') and Nyberg's rejection of it.\",\n \"derivation_fa\": \"جزء نخست هر دو جفت درست است اما برچسب زبانی جعبه درست نیست. Aša Vahišta «بهترین اشا/راستی» دومین امشاسپند است و از aş̣a- «راستی، نظم راستین» و vahišta- «بهترین» ساخته شده؛ صورت arta- گونهٔ پارسی باستان/مادی همان واژه است نه اوستایی. Dārayavauš نیز پارسی باستان است، نه اوستایی؛ کنت آن را از *dhārayat- (اسم فاعل ریشهٔ dar- «داشتن») به‌علاوهٔ *vasu «نیکی» می‌داند، یعنی «دارندهٔ نیکی». صورت dārayat-vahu که نورایی می‌آورد همان بازسازی فرضی است، نه واژه‌ای مضبوط در اوستا. پس ادعا درست است ولی برچسب زبان باید اصلاح شود.\",\n \"sources\": [W + \"%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA\", \"https://www.etymonline.com/word/Darius\"],\n \"ref_check\": [\n   {\"ref\": \"SYN:1176\", \"status\": \"supports\", \"note\": \"Buck p. 1176: 'Av. vaŋhu-, vohu- (OPers. only in proper names, as Dāraya-vauš, Vau-misa)'. Nourai's Dāraya-vauš comes from here verbatim — including the hyphenation — but Buck calls it Old Persian.\"},\n   {\"ref\": \"KLN:401\", \"status\": \"supports\", \"note\": \"Klein s.v. Darius (KLN_1966.txt l.10341): 'L. Darius, fr. Gk. Δαρεῖος, fr. OPers. Darayava(h)ush (whence also Heb. Daryawesh), a compound lit. meaning \\\"he who holds firm the good\\\". The first element ... derives from the stem of OPers. darayamiy, \\\"I hold\\\", fr. I.-E. base *dher(e)-, \\\"to hold\\\" ... The second element in OPers. Daraya-va(h)ush means \\\"the good\\\", and is related to Avestic vaŋhu, vohu, OI. vasuh, \\\"good\\\".' Exactly Nourai's arrow.\"},\n   {\"ref\": \"KLN:169\", \"status\": \"partial\", \"note\": \"Klein p. ~169 s.v. behen has Pers. bahman only as a plant name; it does not bear on aş̣a-vahišta or Dārayavauš.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. Dārayava'u-\", \"stance\": \"supports\", \"note\": \"'Dārayava'u- sb. \\\"Darius\\\" ... Elam. da-ri-a-ma-u-iš, Akk. da-ri-ja-muš, Gk. Δαρεῖος (by haplology for *Δαρειαῖος ...). From pAr. *dhāraġat-, ptc. to root in OP dar-, + pAr. *vasu asn. \\\"the good\\\" ... \\\"He who holds firm the good\\\" (Hz. ... takes as hypocoristic of *dāraya-vahu-manah- \\\"Holder of Good Thought\\\"; this is rejected by Nyberg, Rel. 361).'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. Art-vahišt\", \"stance\": \"supports\", \"note\": \"'Art-vahišt ... Aša-vahišt ... one of the Amahraspands. — art, urt < OIr/Skr rta- \\\"the right cosmic order, the divine law\\\", Av. arata-, ərəta-, aša- + vahišta- \\\"the best, the heavenly law\\\". Aša-vahišt is directly borrowed from Av.; also the name of the 2nd month ... NP ardi- (urdi-)bihišt.'\"},\n   {\"src\": \"BRT\", \"where\": \"AiW s.v. aş̣a- + vahišta- (BRT.txt leaf ~6130 region)\", \"stance\": \"supports\", \"note\": \"Bartholomae's aş̣a- article repeatedly cites the collocation 'aş̣əm vohū vahištəm astī' and the Aməša-Spənta name '°šahe vahištahe yazamaide'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. Ardwahišt\", \"stance\": \"supports\", \"note\": \"'Ardwahišt [ʾltwhšt' | M ʾrdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day.'\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"Ordîbehešt «اردیبهشت»; Dârîuš «داریوش»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"اردیبهشت is a straightforward inherited descent; داریوش is a learned re-import. (a) Av. aş̣a- vahišta- / OP *arta-vahišta- > MP Ardwahišt, also Urdwahišt and Ašwahišt (MacKenzie lists all three), > NP اردیبهشت ordībehešt / ardībehešt, the second month and the third day of each month — the calendrical use being the reason the word survived at all. The -d- of ard- is the Old Persian/Median arta- with regular MP rt > rd, and the -i- is the MP connecting vowel; Nyberg gives 'MPrs ʾrdywh<yst>, Sogd., NP ardi- (urdi-)bihišt'. (b) داریوش: OP Dārayavauš was borrowed into Greek as Δαρεῖος (haplology for *Δαρειαῖος, Kent), Latin Darius, Hebrew Dāryāweš. The Persian line of descent, however, gave MP Dārāy > NP دارا/داراب (the Dārā of the Šāhnāme); modern داریوش Dāriuš is a 19th-20th-century revival shaped on the cuneiform/Greek form after the decipherment of Old Persian, not an unbroken Middle-Persian inheritance. Nourai's arrow is therefore right about the etymology but silent about the gap, which is why the node is 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"«اردیبهشت» از aş̣a- vahišta- اوستایی از راه فارسی میانهٔ Ardwahišt/Urdwahišt به فارسی نو رسیده است؛ تبدیل rt ایرانی باستان به rd در فارسی میانه قاعده‌مند است و بقای واژه مدیون کاربرد گاهشماری آن است. اما «داریوش» دنبالهٔ پیوستهٔ Dārayavauš نیست؛ صورت موروثی آن در فارسی میانه Dārāy و در فارسی نو «دارا/داراب» (شاهنامه) است و «داریوش» احیای عالمانهٔ سدهٔ سیزدهم/چهاردهم خورشیدی است که پس از خوانده شدن خط میخی از روی صورت پارسی باستان/یونانی ساخته شد. ریشه‌شناسی نورایی درست است ولی راه انتقال دقیقاً آن نیست که پیکان نشان می‌دهد.\",\n \"sources\": [W + \"%D8%A7%D8%B1%D8%AF%DB%8C%D8%A8%D9%87%D8%B4%D8%AA\", \"https://www.etymonline.com/word/Darius\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:101\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p. 101 (BQT_v1_pages.txt leaf 311, running head اردیبهشت) has the اردیبهشت article; the preceding page carries 'اردیبهشتگان — جشنی که ایرانیان باستان در روز اردیبهشت (سوم) از ماه ...' and the note 'رک: اردیبهشت ... شا وهیشته' (the Pahlavi/Avestan form).\"},\n   {\"ref\": \"KLN:401\", \"status\": \"supports\", \"note\": \"Klein s.v. Darius, quoted at node #5: 'fr. OPers. Darayava(h)ush ... \\\"he who holds firm the good\\\"'.\"},\n   {\"ref\": \"MON:327\", \"status\": \"partial\", \"note\": \"6-volume Mo'in not on disk; the abridged edition supports the content of the بهشت/بهمن family but the exact page cannot be confirmed.\"},\n   {\"ref\": \"ZMA:19\", \"status\": \"not_checked\", \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian: no accessible copy (refs_online.json: purchase only).\"},\n   {\"ref\": \"SYN:1176\", \"status\": \"supports\", \"note\": \"Buck p. 1176 names Dāraya-vauš as the Old Persian proper name preserving vasu-/vohu-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. Ardwahišt, Urdwahišt, Ašwahišt\", \"stance\": \"supports\", \"note\": \"'Ardwahišt ... (N urdībihist)'; 'Urdwahišt [ʾwrtwhšt'] = Ardwahist.'; 'Ašwahišt [ʾšwhšt'] = Ardwahist.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. Art-vahišt\", \"stance\": \"supports\", \"note\": \"'MPrs ʾrdywh<yst>, Sogd. 2771; NP ardi- (urdi-)bihišt.'\"},\n   {\"src\": \"KNT\", \"where\": \"Kent s.v. Dārayava'u-\", \"stance\": \"partial\", \"note\": \"Confirms the Old Persian etymology and the Greek/Akkadian/Elamite renderings, but records no New Persian continuant — consistent with داریوش being a modern revival.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann (HUB.txt l.6712)\", \"stance\": \"supports\", \"note\": \"'zd. aša-vahista-; Farvardīn \\\"der erste Monat\\\" = phl. fra-...' — Hübschmann treats the month names as the Avestan/Pahlavi survivals.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Greek\", \"words\": \"hu, eus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Homeric ἐŰς / ἠŰς (eûs, ēûs) 'good, brave', gen. ἐῆος, is the Greek reflex of PIE *h₁su-/*h₁esu-; its neuter εὖ was fossilised as the adverb 'well' and became the immensely productive prefix εὐ- of the compounds in node #8. The second form Nourai gives, hu-, is the same morpheme with the other (zero-grade, aspirated) outcome ὑ- , which Greek preserves only in ὑγιής and a few Mycenaean spellings; Klein notes s.v. hygiene 'I.-E. *su- (Gk. ὑ-), \\\"well\\\" ... As a formative element, ὑ- was replaced later by εὐ-'. Both shapes therefore stand correctly under the root, and the arrow 'IE → Greek' is uncontroversial. Watkins puts it in one line: 'esu-. Good. Extension of es-. Greek eūs, good, combining form eu-, well: EU-.'\",\n \"derivation_fa\": \"صورت هومری ἐŰς/ἠŰς «نیک، دلاور» بازتاب یونانی ریشهٔ *h₁su-/*h₁esu- است و صورت خنثای آن (εὖ) به قید «خوب، نیک» و سپس به پیشوند پرکاربرد εὐ- بدل شده است. صورت دوم، یعنی ὑ- ، همان ماده با دمش (دمهٔ سخت) است که در یونانی تنها در ὑγιής مانده است؛ کلاین می‌نویسد که ὑ- بعدها جای خود را به εὐ- داد. پس هر دو صورت درست زیر این ریشه قرار گرفته‌اند و ادعای نورایی درست است.\",\n \"sources\": [W + \"%E1%BD%91%CE%B3%CE%B9%CE%AE%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt l.462): 'esu-. Good. Extension of es-. Greek eūs, good, combining form eu-, well: EU-. [Pok. esu-s 342.]' The AHD index line also reads 'EU- esu-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 548 s.v. eu-, and s.v. hygiene\", \"stance\": \"supports\", \"note\": \"'eu-, combining form meaning \\\"good, well\\\". — Fr. Gk. eu, \\\"well\\\", prop. neut. of ἐŰς, \\\"good\\\"'; and s.v. hygiene 'fr. I.-E. *su- (Gk. ὑ-), \\\"well\\\" ... As a formative element, ὑ- was replaced later by eu-.'\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p. 342 (esu-s)\", \"stance\": \"supports\", \"note\": \"'Gr. ἐŰς, ἠŰς \\\"proficient, good\\\". Adverb σὖ (Akk. n.), belongs to prefix εὐ-'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71, p. 1176\", \"stance\": \"supports\", \"note\": \"'Grk. ὑ- in ὑγιής \\\"in good health\\\"' and 'Grk. εὖ-, the semantic equivalent ... beside Hom. ἐŰς, ἠŰς \\\"good, brave\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. esus (1)\", \"stance\": \"supports\", \"note\": \"'Myc. Gk. eu-, px.; Hom. ēü-; eüs, gs eéos; cf. also eós'.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Greek\", \"words\": \"eu-kaliptos; eu-klidos; ev-angelion; eu-genos; hu-gies\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Four of the five are textbook εὐ- compounds; the fifth is contested, and the first is not really an ancient Greek word. (a) eu-kaliptos: εὐκάλυπτος 'well covered' (καλυπτός, verbal adj. of καλύπτειν 'to cover') is a possible but marginal Greek formation; the word that matters is the Modern Latin genus name Eucalyptus coined from these elements in 1788 by the French botanist L'Héritier de Brutelle, 'so called in allusion to the cap covering the bud' (Klein). (b) eu-klidos: Εὐκλείδης Eukleidēs, the geometer of c. 300 BC, = εὖ + κλέος 'fame' (PIE *ḱlew-), literally 'of good renown' — Nourai's gloss is right, his transliteration loose. (c) ev-angelion: εὐαγγέλιον 'reward for good tidings; gospel', from εὐάγγελος 'bringing good news', εὖ + ἄγγελος 'messenger' (itself a Persian-mediated word of ultimately Semitic origin, per Klein). (d) eu-genos: εὐγενής 'well born', εὖ + γένος. (e) hu-gies: ὑγιής 'healthy'. Here Klein and Watkins do give Nourai's analysis — Klein: 'ὑγιής ... stands for *su-gwiyes and lit. means \\\"living well\\\"' — but current scholarship prefers *h₂yu-gʷih₃- 'having a long life' (from *h₂óyu- 'life-force'), and Wiktionary notes 'the former derivation is favored by Beekes and Weiss'. So ὑγιής may not belong under this root at all, and that single word pulls the node down to 'plausible'.\",\n \"derivation_fa\": \"چهار تا از پنج واژه ترکیب‌های روشن با پیشوند εὐ- اند: Εὐκλείδης (εὖ + κλέος «آوازه»)، εὐαγγέλιον (εὖ + ἄγγελος «پیام‌آور») و εὐγενής (εὖ + γένος). اما eucalyptus واژه‌ای یونانی کهن نیست، بلکه نام جنسی لاتینی نو است که در ۱۷۸۸ گیاه‌شناس فرانسوی لوریتیه از همین دو جزء ساخت. دربارهٔ ὑγιής دو نظر هست: کلاین و واتکینز آن را *su-gʷiyes «خوب‌زی» می‌دانند (همان که نورایی پذیرفته)، ولی بیکس و وایس صورت *h₂yu-gʷih₃- «دراز‌زی» را ترجیح می‌دهند؛ پس این یک مورد محل اختلاف است و جعبه روی‌هم با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/eucalyptus\", W + \"%E1%BD%91%CE%B3%CE%B9%CE%AE%CF%82\", \"https://www.etymonline.com/word/hygiene\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:548\", \"status\": \"supports\", \"note\": \"The eu- article (quoted at the root) is Klein's p. 548.\"},\n   {\"ref\": \"KLN:549\", \"status\": \"supports\", \"note\": \"The entries that immediately follow eu- in Klein — i.e. his next page — include 'Eucalyptus, n., a genus of plants of the myrtle family (bot.) — ModL., lit. \\\"well covered\\\", coined by the French botanist L'Héritier de Brutelle (1746-1800) in 1788 fr. eu- and Gk. καλυπτός, \\\"covered\\\" ... so called in allusion to the cap covering the bud', 'Eugene, masc. PN. — F. Eugène, fr. L. Eugenius, fr. Gk. Εὐγένιος, fr. εὐγενής, \\\"well born\\\"' and 'eugenic ... fr. eu- and γένος'.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins indexes the compounds under their SECOND elements — 'EUCALYPTUS kel-²', 'EUGENE/EUGENIC genə-', 'HYGIENE gʷei-', 'EU- esu-' — and under gʷei- writes 'IV. Prefixed and suffixed form *su-gʷiə-es- (*su-, well; see su-), \\\"living in good condition,\\\" in Greek hugiēs, healthy: HYGEIA, HYGIENE', i.e. AHD 1985 still backs Nourai on ὑγιής.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. evangel, hygiene, Eugene, calyptra\", \"stance\": \"partial\", \"note\": \"'evangel, n., the gospel. — ME. evangile, fr. OF. evangile, fr. Eccles. L. evangelium, \\\"gospel\\\", fr. Gk. εὐαγγέλιον, \\\"reward of good tidings; gospel\\\", fr. εὐάγγελος, \\\"bringing good news\\\", fr. eu (see eu-) and ἄγγελος \\\"messenger\\\"'; 'hygiene ... fr. ὑγιής, \\\"healthy\\\", which stands for *su-gwiyes and lit. means \\\"living well\\\"'. Klein supports four items outright and the fifth only against the current consensus.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Evangelist, Eucalyptus\", \"stance\": \"supports\", \"note\": \"'Evangelist ... Gk. εὐαγγέλιον a reward for good tidings ... εὖ, well; ἄγγελος, tidings' and 'Eucalyptus, a genus of trees ... Latinised from Gk. εὖ, well; καλυπτός, covered.'\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (not searched successfully for these headwords)\", \"stance\": \"silent\", \"note\": \"The F&W volumes on disk are OCR of a different alphabetical split; no usable entry located for eucalyptus/hygiene.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"okâlîptus «اوکالیپتوس»; Oqlîdos «اقلیدس»; Angelyŭn «انگلیون (انجیل)»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three are ultimately Greek, but none reached Persian from Greek directly, and the chart's single arrow hides three different mediators. (a) اوکالیپتوس okālīptus is a 20th-century botanical loan from French/International eucalyptus (itself the 1788 neo-Latin coinage), brought in with the tree when it was planted in Iran; it is not a Greek word borrowed by Persians. (b) اقلیدس Oqlīdos comes through Arabic: Gk. Εὐκλείδης was rendered in Syriac and then Arabic as أقليدس Uqlīdis/Iqlīdis in the 9th-century translation movement (al-Ḥajjāj b. Yūsuf's and Isḥāq b. Ḥunayn's versions of the Elements), with the usual Arabic treatment of Greek εὐ- as أُ-/إِ- and δ as د; Persian took the name from Arabic, and 'Euclid' became in Persian usage a byword for geometry itself. (c) انگلیون Angelyūn is the Syriac form: Gk. εὐαγγέλιον > Syriac ܕܐܘܢܓܠܝܘܢ ʾewangeliyōn, used by the Eastern-rite Christians of Iran and Mesopotamia, whence both Persian انگلیون and, with the Arabic ʾifʿīl pattern, Qur'anic إنجيل Injīl and hence NP انجیل. Mo'in states the chain explicitly: 'انجیل: [معر. < انگلیون] (اخ.) هر یک از چهار کتاب دینی مسیحیان', and has a separate headword 'انگلیون (اخ.) انجیل'. Nourai's gloss for Oqlīdos ('famous') is the meaning of the Greek name's second element, not of the Persian word.\",\n \"derivation_fa\": \"هر سه واژه در نهایت یونانی‌اند اما هیچ‌یک مستقیماً از یونانی به فارسی نیامده‌اند. «اوکالیپتوس» وام‌واژه‌ای از فرانسه در سدهٔ چهاردهم خورشیدی است که همراه خود درخت وارد شد. «اقلیدس» معرّب Εὐκλείδης است که در نهضت ترجمهٔ سدهٔ سوم هجری از راه سریانی و عربی به فارسی رسیده (وام‌گیری عربی‌میانجی). «انگلیون» صورت سریانی εὐαγγέλιον است (ʾewangeliyōn) که مسیحیان شرق به کار می‌بردند و معین نیز می‌نویسد «انجیل: [معرّب < انگلیون]». پس پیکان یکدست نورایی درست است ولی میانجی‌ها (فرانسه، عربی، سریانی) را نشان نمی‌دهد.\",\n \"sources\": [W + \"%E1%BD%91%CE%B3%CE%B9%CE%AE%CF%82\", \"https://www.etymonline.com/word/eucalyptus\"],\n \"ref_check\": [\n   {\"ref\": \"MON:404\", \"status\": \"not_found\", \"note\": \"Only the 2-volume Adena abridgement of Mo'in is on disk; a grep for اوکالیپتوس in MON_part1/part2 and both Adena volumes returns nothing, so p. 404 of the 6-volume set could not be checked.\"},\n   {\"ref\": \"MON5:165\", \"status\": \"not_checked\", \"note\": \"Mo'in vols. 5-6 (the a'lam / proper-name volumes, where اقلیدس would stand) are not available locally or online; refs_online.json lists only the lexicon volumes via vajehyab/abadis.\"},\n   {\"ref\": \"MON5:190\", \"status\": \"partial\", \"note\": \"Vol. 5 itself is unavailable, but the lexicon volume supports the claim: MON_part1.txt l.17504 'انجیل: [معر. < انگلیون] (اخ.) هر یکی از چهار کتاب دینی مسیحیان، ج. اناجیل' and l.18452 'انگلیون (اخ.) انجیل'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in (2-vol. ed.) s.vv. انجیل, انگلیون\", \"stance\": \"supports\", \"note\": \"'انجیل: [معر. < انگلیون]' — Mo'in derives the Arabic/Persian Injīl from the form انگلیون that Nourai puts in this box.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. angel, evangel\", \"stance\": \"supports\", \"note\": \"'Gk. ἄγγελος ... of Persian, ult. of Sem. origin' and 'Eccles. L. evangelium ... fr. Gk. εὐαγγέλιον' — the Greek side of the chain.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"The book plainly treats Injīl (it is named repeatedly, e.g. pp. 171, ~192, and in the introduction's list 'Tawrāh, Injīl, Sakīna, Firdaus, Jahannam'), but the Arabic headwords in this OCR are unreadable and the إنجيل article itself could not be located to quote.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"eucalyptus, Euclid, Evangelical, Eugene, hygiene\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English took all five through Latin/French, not from Greek directly. eucalyptus: ModL Eucalyptus (L'Héritier 1788) > English 1789. Euclid: L. Euclides < Gk. Εὐκλείδης, in English from the medieval Latin translations of the Elements. Evangelical: Eccles. L. evangelicus < Gk. εὐαγγελικός, English 16th c. (the noun evangel is ME evangile < OF évangile < Eccles. L. evangelium). Eugene: F. Eugène < L. Eugenius < Gk. Εὐγένιος < εὐγενής 'well born'. hygiene: F. hygiène < Gk. ὑγιεινή (τέχνη) 'the healthful art' < ὑγιής — and this last is the one word in the box whose membership of the *su- root is now doubted (Beekes and Weiss prefer *h₂yu-gʷih₃- 'having a long life'; Etymonline follows them, reconstructing *eyu-gʷie-es-). Everything except hygiene is confirmed; hygiene is the reason the node is only 'plausible'.\",\n \"derivation_fa\": \"هر پنج واژه از راه لاتین و فرانسه به انگلیسی رسیده‌اند، نه مستقیماً از یونانی: eucalyptus از لاتین نو (۱۷۸۸) در ۱۷۸۹، Euclid از لاتین Euclides، Evangelical از لاتین کلیسایی evangelicus، Eugene از فرانسه Eugène و hygiene از فرانسه hygiène. تنها واژهٔ محل اختلاف hygiene است که ریشه‌شناسی امروزی آن را به *h₂yu-gʷih₃- «دراز‌زی» می‌برد نه به ریشهٔ «نیک»؛ به همین سبب جعبه روی‌هم با احتیاط پذیرفته می‌شود.\",\n \"sources\": [\"https://www.etymonline.com/word/eucalyptus\", \"https://www.etymonline.com/word/hygiene\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins's index assigns each word to the root of its second element ('EUCALYPTUS kel-²', 'EUGENE/EUGENIC genə-', 'HYGIENE gʷei-'), and only 'EU- esu-' to this root; under gʷei- AHD does derive hugiēs from *su-gʷiə-es-, so the 1985 AHD backs Nourai where Beekes does not.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. Eucalyptus, evangel(ic), Eugene, hygiene\", \"stance\": \"supports\", \"note\": \"Klein gives all the Latin/French intermediate stages quoted above, e.g. 'evangelic, evangelical, adj. — Eccles. L. evangelicus, fr. Gk. εὐαγγελικός' and 'hygiene, n., the science of health. — F. hygiène, fr. Gk. ὑγιεινόν ... used by Aristotle also as a noun in the sense of \\\"health\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Eucalyptus, Evangelist\", \"stance\": \"supports\", \"note\": \"'Eucalyptus, a genus of trees, including the blue gum-tree. (Gk.) Latinised from Gk. εὖ, well; καλυπτός, covered.'\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Sanskrit\", \"words\": \"su; su-asti, svasti\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit su- is the inherited prefix/adverb 'well, good' from PIE *h₁su- (Pokorny 1037: 'Old Indic su-, Avestan hu-, Old Pers. u-, e.g. Old Indic su-dāru- \\\"strong wood\\\", su-bhaga- \\\"lucky\\\"'). svastí- f. 'well-being, welfare, good fortune', attested from the Rigveda, is su- + astí- (a noun to ásti 'is', root as- < PIE *h₁es-), so 'being well'; the spelling su-asti that Nourai gives beside svasti is simply the uncontracted analysis, with the regular Sanskrit sandhi u > v before a vowel. The Avestan cognate of the prefix is hu- (PIE *s- > Iranian h-), which is why Persian has hu-/xš- words rather than su- words and why the Sanskrit branch had to be drawn separately in the chart.\",\n \"derivation_fa\": \"پیشوند su- سنسکریت «خوب، نیک» بازماندهٔ همان *h₁su- هندواروپایی است که در اوستایی hu- و در پارسی باستان u- شده است (سایشی‌شدن s آغازین به h در زبان‌های ایرانی). واژهٔ svastí- «بهزیستی، نیک‌بختی» که از ریگ‌ودا به بعد مضبوط است مرکّب su- + astí- (از ریشهٔ as- «بودن»، هم‌ریشه با یونانی esti و لاتین est) است؛ صورت su-asti همان شکل تجزیه‌نشده پیش از اعمال سندی (u > v پیش از واکه) است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/swastika\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1298\", \"status\": \"partial\", \"note\": \"Nourai's 'AHD:1298' is a page of the New College Edition's main dictionary (s.v. swastika), which is not in the local copy; the local Watkins 1985 appendix supports the analysis twice over — s.v. su-: 'Well, good. 1. Sanskrit su-, well-being, good luck: SWASTIKA. [Pok. su- 1037.]', and s.v. es-: '2.b. Sanskrit asti, is: SWASTIKA'. The index line reads 'SWASTIKA es-, su-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny p. 1037-1038 s.v. su-, sū-\", \"stance\": \"supports\", \"note\": \"'Old Indic su-, Avestan hu-, Old pers. u-, e.g. in Old Indic su-dāru- \\\"strong wood\\\", su-bhaga- \\\"lucky\\\" ...'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. swastika\", \"stance\": \"supports\", \"note\": \"'OI. svastikah, lit. \\\"being fortunate\\\", fr. svastih, \\\"welfare\\\", a word compounded of su-, \\\"good, well\\\", and asti, \\\"is\\\", which is cogn. with Gk. ἐστί, L. est, \\\"is\\\".'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.71, p. 1176\", \"stance\": \"supports\", \"note\": \"'1. Prefix IE *su- ... Skt. su-, Av. hu-' and, in the list of words for 'good', 'Skt. sādhu-, bhadra-, vasu-'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. esus (1)\", \"stance\": \"supports\", \"note\": \"'Skt. cf. su-, px.; Av. hu-, id.' — Mann files the Sanskrit prefix under the same lemma.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"swastica, swastika\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English swastika is a direct 19th-century borrowing of Sanskrit svastika- 'a lucky object; the auspicious mark', a -ka- derivative of svastí- 'well-being' (su- + asti-), taken over by British Indologists and archaeologists (Etymonline dates the English word to 1871; the variant spelling swastica is occasional in the same literature). It is thus one of the very few English words in which the *h₁su- prefix arrives through Sanskrit rather than through Greek. On the date in Nourai's gloss: the hooked cross was adopted as the emblem of the NSDAP in 1920, English use of the word 'swastika' for the Nazi emblem is attested by 1932, and 1935 is the year the swastika flag became the national flag of Germany by the Reichsflaggengesetz of 15 September 1935 — so 'adopted in 1935 as an emblem of Nazi Germany' is defensible for the state emblem but would mislead a reader about the party emblem.\",\n \"derivation_fa\": \"واژهٔ انگلیسی swastika وام‌گیری مستقیم سدهٔ نوزدهم میلادی از سنسکریت svastika- «نشان فرخنده» است، مشتق از svastí- «بهزیستی» با پسوند -ka-؛ هندشناسان بریتانیایی آن را وارد انگلیسی کردند (اتیموآنلاین: ۱۸۷۱). دربارهٔ تاریخی که نورایی می‌دهد: صلیب شکسته در ۱۹۲۰ نشان حزب نازی شد و در ۱۵ سپتامبر ۱۹۳۵ با قانون پرچم رایش به پرچم رسمی آلمان بدل گشت؛ پس تاریخ ۱۹۳۵ برای نشان دولتی درست است نه برای نشان حزبی. ریشه‌شناسی ادعاشده درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/swastika\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1298\", \"status\": \"partial\", \"note\": \"The page belongs to the New College Edition's main dictionary, not available locally; Watkins 1985 s.vv. su- and es- both end their entries with 'SWASTIKA', which is the same claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. swastika, hakenkreuz, fylfot\", \"stance\": \"supports\", \"note\": \"'swastika, n., a symbol in the form of a Greek cross with the ends of the arms bent at right angles; used as the emblem of the Nazi party. — OI. svastikah, lit. \\\"being fortunate\\\", fr. svastih, \\\"welfare\\\" ... so called because it was regarded as auspicious.' Klein adds 'hakenkreuz, n., swastika; used as the emblem of Nazism. — G. Hakenkreuz, lit. \\\"hook-cross\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\", \"note\": \"grep -i 'swastika' SKT.txt returns nothing; Skeat's concise dictionary has no entry.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (WEB_vol1.txt)\", \"stance\": \"silent\", \"note\": \"The single local volume does not reach s-; no entry available.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 486,\n \"book_page\": 456,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-486.json', 'w', encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-486.py",
 "description": "Build page-486.json"
}
```


### [2026-09-14T03:31:08.420Z] TOOL RESULT

```
written
```


## [2026-09-14T03:31:08.811Z] AGENT

You've hit your session limit · resets 2:50am (America/Toronto)
