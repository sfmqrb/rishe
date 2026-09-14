# Verification process log — verify-page-429


## [2026-09-14T01:21:52.569Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 429 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-429.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-429.json. Write /home/sfmqrb/git/rishe/data/verification/page-429.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 429` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:53.626Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:54.425Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:54.442Z] TOOL RESULT

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


## [2026-09-14T01:21:54.910Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-429.txt"
}
```


### [2026-09-14T01:21:54.930Z] TOOL RESULT

```
1	=== PDF page 429 (book page 399) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Saka : name of an Aryan tribe N.E. of Iran, Scythians  (refs MON5:772; BQT:1158)
4	#1 (parent #0) [Avestan / Old Persian] refs=BQT:1158 | saka 1 : Scythians ; saka-stâna : "land of Sakas", referring to an area S.E. of Iran after Sakas defeated its native people in 130 B.C.
5	  #2 (parent #1) [Persian] refs=BQT:1158; MON5:772 | sakâ «سکا» : Scythians ; sagzî «سگزی» : of or pertaining to Scythians ; sîstân «سیستان» : an area in S.E. Iran | extra: سکّه ، ساک ، ساسا
6	سجزی
7	سگستان
8	#3 (parent #0) [Greek] refs=BQT:1158; MON5:772 | Scythe : Scythians
9	  #4 (parent #3) [English] refs=AHD:1169 | Scythia, Scythian
10	--- entry 1 ---
11	ROOT [Sanskrit] Sakah : teak wood  (refs KLN:1578)
12	#1 (parent #0) [Hindustani] refs=HJB:910 | sâgun : teak
13	  #2 (parent #1) [Arabic] refs=HJB:910; KLN:1578 | sâj : teak
14	    #3 (parent #2) [Persian] refs=MON:1783 | sâj «ساج» : teak tree
15	#4 (parent #0) [Malaysian] refs=KLN:1578 | těkka : teak
16	  #5 (parent #4) [Portuguese] refs=None | teca : teak
17	    #6 (parent #5) [English] refs=AHD | teak
18	--- entry 2 ---
19	ROOT [Greek] Salamandra : salamander  (refs FSD:2161; AHD:1144)
20	#1 (parent #0) [Persian] refs=FSD:2161; BQT:1166; MON:1921 | samandar «سمندر» : a lizard-like amphibian believed not to burn in fire | extra: سالامندر ، سمندور
21	#2 (parent #0) [Arabic] refs=TAD:37 | samandar
22	#3 (parent #0) [Latin] refs=AHD; KLN:1374 | salamandra
23	  #4 (parent #3) [French] refs=AHD | salamandre
24	    #5 (parent #4) [English] refs=AHD; FSD:2161 | salamander
25	--- entry 3 ---
26	ROOT [Sanskrit] Šâli : grains, cereals  (refs BQT:1229)
27	#1 (parent #0) [Persian] refs=BQT:1229; MON:2000 | šâlî «شالی» : rice, especially in the husk
28	  #2 (parent #1) [Persian] refs=BQT; MON:2070 | šâlîzâr «شالیزار» : rice field ☞Kwel ; šaltŭk «شَلتوک» : rice in the husk | extra: چلتوک
29	
```


## [2026-09-14T01:21:57.888Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-429.json",
 "description": "Read source JSON for page 429"
}
```


### [2026-09-14T01:21:57.960Z] TOOL RESULT

```
{
  "pdf_page": 429,
  "book_page": 399,
  "entries": [
    {
      "root": {
        "name": "Saka",
        "lang": "Indo-European",
        "refs": "MON5:772; BQT:1158",
        "gloss": "name of an Aryan tribe N.E. of Iran, Scythians"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "BQT:1158",
          "words": [
            {
              "translit": "saka 1",
              "gloss": "Scythians",
              "script": null
            },
            {
              "translit": "saka-stâna",
              "gloss": "\"land of Sakas\", referring to an area S.E. of Iran after Sakas defeated its native people in 130 B.C.",
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
          "refs": "BQT:1158; MON5:772",
          "words": [
            {
              "translit": "sakâ",
              "gloss": "Scythians",
              "script": "سکا"
            },
            {
              "translit": "sagzî",
              "gloss": "of or pertaining to Scythians",
              "script": "سگزی"
            },
            {
              "translit": "sîstân",
              "gloss": "an area in S.E. Iran",
              "script": "سیستان"
            }
          ],
          "script_extra": "سکّه ، ساک ، ساسا\nسجزی\nسگستان",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "BQT:1158; MON5:772",
          "words": [
            {
              "translit": "Scythe",
              "gloss": "Scythians",
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
          "lang": "English",
          "refs": "AHD:1169",
          "words": [
            {
              "translit": "Scythia, Scythian",
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
        "name": "Sakah",
        "lang": "Sanskrit",
        "refs": "KLN:1578",
        "gloss": "teak wood"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hindustani",
          "refs": "HJB:910",
          "words": [
            {
              "translit": "sâgun",
              "gloss": "teak",
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
          "lang": "Arabic",
          "refs": "HJB:910; KLN:1578",
          "words": [
            {
              "translit": "sâj",
              "gloss": "teak",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1783",
          "words": [
            {
              "translit": "sâj",
              "gloss": "teak tree",
              "script": "ساج"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Malaysian",
          "refs": "KLN:1578",
          "words": [
            {
              "translit": "těkka",
              "gloss": "teak",
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
          "lang": "Portuguese",
          "refs": null,
          "words": [
            {
              "translit": "teca",
              "gloss": "teak",
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
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "teak",
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
        "name": "Salamandra",
        "lang": "Greek",
        "refs": "FSD:2161; AHD:1144",
        "gloss": "salamander"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FSD:2161; BQT:1166; MON:1921",
          "words": [
            {
              "translit": "samandar",
              "gloss": "a lizard-like amphibian believed not to burn in fire",
              "script": "سمندر"
            }
          ],
          "script_extra": "سالامندر ، سمندور",
          "note": null,
          "quote": {
            "text": "به آتش درون بر مثال سمندر - به آب اندرون بر مثال نهنگان",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "TAD:37",
          "words": [
            {
              "translit": "samandar",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; KLN:1374",
          "words": [
            {
              "translit": "salamandra",
              "gloss": null,
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
          "lang": "French",
          "refs": "AHD",
          "words": [
            {
              "translit": "salamandre",
              "gloss": null,
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
          "refs": "AHD; FSD:2161",
          "words": [
            {
              "translit": "salamander",
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
        "name": "Šâli",
        "lang": "Sanskrit",
        "refs": "BQT:1229",
        "gloss": "grains, cereals"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1229; MON:2000",
          "words": [
            {
              "translit": "šâlî",
              "gloss": "rice, especially in the husk",
              "script": "شالی"
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
          "refs": "BQT; MON:2070",
          "words": [
            {
              "translit": "šâlîzâr",
              "gloss": "rice field",
              "script": "شالیزار",
              "see": ["Kwel"]
            },
            {
              "translit": "šaltŭk",
              "gloss": "rice in the husk",
              "script": "شَلتوک"
            }
          ],
          "script_extra": "چلتوک",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:22:00.181Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','AHD','KLN','HJB','FSD','TAD','POK','WLD','HRN','HUB','PHD','NYB','ARY','BRT','KNT','SKT','WEB','AID','IEC','SYN','LKT','PLA','AFM','FVQ']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T01:22:01.650Z] TOOL RESULT

```
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
```


## [2026-09-14T01:22:24.206Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60 && echo ---- && sed -n 1,80p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:22:24.293Z] TOOL RESULT

```
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
----
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
```


## [2026-09-14T01:22:24.683Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,60p tools/verify_check.py"
}
```


### [2026-09-14T01:22:24.730Z] TOOL RESULT

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
```


## [2026-09-14T01:22:30.991Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 teak ===\"; grep -n -i -m8 \"teak\" KLN_1966.txt | head -20\necho \"=== KLN teak context ===\"; grep -n -i -A12 \"^teak\" KLN_1966.txt | head -40\necho \"=== HJB teak ===\"; grep -n -i -m20 \"TEAK\" HJB.txt | head -30\necho \"=== HJB sagun ===\"; grep -n -i -m10 \"sagun\\|sāgun\\|s√Ågun\" HJB.txt | head -20"
}
```


### [2026-09-14T01:22:31.109Z] TOOL RESULT

```
=== KLN 1966 teak ===
17132:from  the  stem  of  dpotp-rdveLv,  ‘to  miss  the  mark, fail  of  one’s  purpose,  err,  sin’,  which  is  of  un¬ certain  origin  (for  sense  development  cp.  Heb. hatd'  ‘he  sinned’,  prop,  ‘he  missed  the  mark’); cp.  Nemertinea.  The  second  element  comes  fr. -Xoyop,  ‘one  who  speaks  (in  a  certain, manner); one  who  deals  (with  a  certain  topic)’ ;  see  -logy, hamburger,  n.,  1)  ground  beef;  2)  cooked  patty of  ground  beef;  3)  sandwich  made  of  such  a patty.  —  Short  for  Hamburger  steak;  named after  Hamburg  in  Germany, hame,  n.,  either  of  the  two  curved  pieces  lying round  the  collar  of  a  horse.  —  ME.  hame,  fr. OE.  hama,  ‘cover,  skin’,  rel.  to  MDu.  hamme, Du.  haam,  ‘collar  of  a  horse’,  ON.  hamr,  ‘skin, covering’,  OHG.  hamo,  of  s.m.,  OHG.  hemidi, ‘shirt’,  and  cogn.  with  OI.  samulyah,  ‘woolen shirt’;  fr.  I.-E.  base  *kam-,  *kem-,  ‘to  cover’. See  heaven  and  cp.  chemise, hamesucken,  n.,  assaulting  of  a  person  in  his  own dwelling  house.  —  ME.  hamsoken,  fr.  OE.  hdm- sden,  compounded  of  ham,  ‘home’,  and  socn, ‘attack’,  which  is  rel.  to  ON.  sdkn,  of  s.m.,  and to  OE.  secan,  ‘to  seek;  to  try  to  get,  attack’.  Cp. OFris.  hamsekenge,  ‘attack  on  a  house’,  G. Heimsuchung,  ‘visitation’,  and  see  home  and seek.
36672:Derivatives:  steadfast-ly,  adv.,  steadfast-ness,  n. steak,  n.  —  ME.  steyke,  steke,  fr.  ON.  steik; prop,  ‘something  stuck  (on  a  spit)’,  and  rel.  to ON.  steikja,  ‘to  roast  on  a  spit’,  and  to  OE. stician,  ‘to  stick’.  See  stick,  v. steal,  tr.  and  intr.  v.  —  ME.  stelen,  fr.  OE.  stelan, rel.  to  OS.  stelan,  ON.,  Norw.,  OFris.  stela, Dan.  stjeele,  Swed.  stjdla,  Du.  stelen,  OHG.  ste¬ lan,  MF1G.  stein,  G.  stehlen,  Goth,  stilan,  and prob.  cogn.  with  Gk.  axepeiv,  Att.  axepiaxEtv, ‘to  deprive  of’,  Mir.  serbh  (for  *ster-wa),  ‘theft’, fr.  I.-E.  base  *ster-,  ‘to  steal’.  The  change  of I.-E.  *ster-  to  *stel-  in  Tent,  is  prob.  due  to  the influence  of  OS.,  OE.,  OHG.  helan,  OFris.  hela, ‘to  hide,  conceal’  (see  hall),  with  which  the  verb steal  is  often  associated.  Cp.  stalk,  ’to  walk furtively’.
36789:stick,  tr.  and  intr.  v.  —  ME.  stikien  (weak  v.),  ‘to prick;  to  be  infixed’,  and  steken  (strong  v.),  ‘to prick,  fix’,  fr.  OE.  stician,  ‘to  stab,  prick,  pierce’, rel.  to  OS.  stekan,  OFris.  steka,  Du.  steken, OHG.  stehhan ,  MHG.,  G.  stechen,  ‘to  stab, prick’,  OHG.  stechhon,  MHG.  stecchen,  stec- ken,  G.  stecken,  ‘to  stick  (intr.),  OHG.  stecchen, MHG.,  G.  stecken,  ‘to  stick’  (tr.).  Du.  stikken, G.  sticken,  ‘to  embroider’,  ON.  steikja,  ‘to roast’,  lit.  ‘to  fix  to  the  spit’ ;  fr.  I.-E.  base  *steig-, ‘to  prick,  stick,  pierce’,  whence  also  L.  instigare, ‘to  goad’,  instinguere,  ‘to  incite;  impel’,  distin- guere,  ‘to  distinguish’,  Gk.  or ££ew  (for  *ax(- Yielv),  ‘to  prick,  puncture’,  oxixxo?  (prop, verbal  adj.  of  crxt£ei.v),  ‘embroidered;  spotted’, axiyp.a,  ‘mark  made  by  a  pointed  instrument’, Lith.  stingu,  stigti,  ‘to  remain  (lit.  be  stuck)  in  a place’,  Russ,  stegdti,  stegnuti,  ‘to  quilt’,  stezka, ‘seam,  suture’,  Bret,  stiogan,  ‘cuttlefish’.  Cp. — without  initial  s — OI.  tejute,  ‘is  sharp,  sharpens’, tejdyati,  ‘sharpens,  pricks,  stings’,  tigmah, ‘pointed’,  Avestic  tiyra-,  ‘pointed’,  tiyri-,  ‘ar¬ row’.  Base  *steig-  is  an  enlarged  form  of  base *stei-,  ‘pointed’,  whence  L.  stilus,  ‘pointed  in¬ strument’,  stimulus,  ‘a  goad,  sting,  incentive’. Cp.  stick,  n.,  and  the  first  element  in  stickle¬ back.  Cp.  also  astigmatism,  distinct,  distinguish, etiquette,  extinguish,  instigate,  instinct,  steak, stigma,  stimulus,  stipple,  stitch,  style,  ‘pointed instrument’,  thistle,  ticket,  tiger,  Tigridia. Derivatives:  stick-er,  n.,  stick-y,  adj.,  stick-i-ly, adv.,  stick-i-ness,  n.,  stick-ing,  adj.,  and  n. stick,  n.  —  ME.  sticke,  fr.  OE.  sticca,  rel.  to  ON. stik,  stikka,  OHG.  stehho,  stecko,  MHG.  steche, G.  Stecken,  ‘stick,  staff’,  and  to  OE.  stician,  ‘to stab,  prick,  pierce’;  in  many  meanings  directly fr.  stick,  v.  (q.v.)  Cp.  the  second  element  in tandstickor.
38339:teak,  n.,  an  East  Indian  tree  ( Tectona  gradis).  — Port,  teca,  fr.  Malayalam  tekka,  fr.  OI.  sakah (whence  also  Arab.  saj).  G.  Tiekbaum  is  an English  loan  word.
=== KLN teak context ===
38339:teak,  n.,  an  East  Indian  tree  ( Tectona  gradis).  — Port,  teca,  fr.  Malayalam  tekka,  fr.  OI.  sakah (whence  also  Arab.  saj).  G.  Tiekbaum  is  an English  loan  word.
38340-teal,  n.,  any  of  certain  fresh  water  ducks  of  the genera  Nett  ion  and  Querquedula.  —  ME.  tele, rel.  to  MDu.  feting,  Du.  taling.
38341-teallite,  n.,  a  lead  sulfostannate  (mineral.)  — Named  after  the  English  geologist  J.  J.  Harris Teall.  For  the  ending  see  subst.  suff.  -ite.
38342-team,  n.,  1)  animals  harnessed  to  the  same  vehicle or  plow;  2)  a  number  of  persons  associated  in the  same  action.  —  ME.  teme,  fr.  OE.  team, 'progeny,  race,  family,  team,  animals  harnessed in  a  row',  rel.  to  ON.  taumr,  Norw.  taunt,  Swed. tom,  Dan.  tomme,  OFris.  tarn,  Du.  toom,  OHG., MHG.  zoum,  G.  Zaum,  ‘bridle’,  lit.  ‘that  which draws,  pulls’,  fr.  I.-E.  base  *deuk-,  ‘to  draw, puli’,  whence  also  Gk.  SatS'joosa&a'.  (Hesy- chius),  ‘to  drag’,  L.  ducere,  ‘to  draw,  lead’.  See duke  and  cp.  tow,  ‘to  draw’,  tug,  ‘to  pull,  drag’. Cp.  also  teem,  ‘to  bring  forth'.
38343-Derivatives:  team,  tr.  v.,  team-ing,  n.,  team-less, adj.,  team-ster,  n.,  team-wise,  adv.
38344-teapoy,  n.,  tea  table.  —  Hind,  tipdi,  ‘a  three-legged table’,  fr.  tin  (fr.  OI.  tri ),  ‘three’,  and  pdi  (fr.  OI. padah),  ‘foot’.  See  three  and  foot  and  cp.  char- poy  and  pajama.  The  spelling  teapoy  is  due  to folk  etymology  which  connected  this  word  with tea.
38345-tear,  n.,  drop  of  liquid  from  the  eye.  —  ME.  tere, ter,  tear,  fr.  OE.  tear,  contraction  of  teagor,  rel. to  ON.,  OFris.  tar,  OHG.  zah(h)ar,  MHG.  za- her,  G.  Zdhre,  Goth,  tagr,  ‘tear’,  fr.  l.-E.  *dakru- ‘tear’,  whence  also  Gk.  Saxpn,  Stxxpuov, Saxpujza  (whence  OL.  dacruma,  L.  lacruma,  la- crima ),  OIr.  der,  W.  deigr,  Co.  dagr,  OBret.  dacr\ cp. — without  the  initial  dental  sound — OI. dsru,  Avestic  asru,  Toch.  A  akar,  Lith.  asara, Lett,  asara.  Cp.  also  Arm.  artasuk ‘  (pi. ;  the  sing, is  artausr ),  with  change  of  dr-  to  rt-.  See  lachry¬ mal  and  cp.  train  oil.
38346-Derivatives:  tear-ful,  adj.,  tear-ful-ly,  adv.,  tear¬ fulness,  n.,  tear-less,  adj.,  tear-less-ly,  adv.,  tear- less-ness,  n.,  tear-y,  adj.
38347-tear,  tr.  and  intr.  v.,  to  putfapart,  rend.  —  ME. teren,  fr.  OE.  teran,  rel.  to  OS.  terian,  ‘to  con¬ sume’,  far-terian,  ‘to  destroy’,  MLG.,  MDu., Du.  teren,  ‘to  consume’,  OHG.  zeran,  fir-zeran, ‘to  destroy;  to  consume  (whence  MHG.  zern, ver-zern,  G.  zehren,  ver-zehren,  ‘to  consume’), OHG.,  MHG.,  G.  zerren,  ‘to  tear’,  Goth,  dis- tairan,  ga-tairan,  ‘to  tear,  destroy;  to  tear  to pieces’,  fr.  I.-E.  *dere-,  *der-,  ‘to  rend,  divide; to  flay’,  whence  also  OI.  drnati,  ‘cleaves,  bursts’, Gk.  SspE'.v,  ‘to  flay’,  8sp(j.a,  ‘skin’,  Sopa,  ‘skin’ Sapaii;,  ‘tearing,  flaying,  separation’,  OSlav. dero,  dlrati,  ‘to  tear,  flay’,  Lith.  dir  it,  dirti,  ‘to flay’,  Arm.  terem,  ‘I  flay’,  W.,  Co.  Bret,  darn, ‘piece’.  Cp.  also  Toch.  tsar,  ‘a  hand’,  prop,  ‘that which  tugs  or  tears’.  Cp.  derma  and  words  there referred  to.  Cp.  also  darn,  dartars,  Derris,  drab, ‘a  kind  of  cloth’,  drape,  tart,  ‘sour’,  tetter,  trap, ‘clothes’.
38348-Derivatives:  tear,  n.,  rent,  division,  tear-er,  n., tear-ing,  adj.
38349-tease,  tr.  v.,  1)  to  card  or  comb  (wool,  flax,  etc.); 2)  to  worry,  vex.  —  ME.  tesen,  teesan,  fr.  OE. teesan,  ‘to  pluck,  pull  apart;  to  tease  (wool)’,  rel. to  Dan.  ttese,  MDu.  tesen,  Du.  tezen,  OHG. zeisan  and  to  E.  touse  (q.v.)  Cp.  next  word. Derivatives:  tease,  n.,  teas-er,  n.,  teas-ing,  adj., teas-ing-ly,  adv.,  teas-y,  adj.
38350-teasel,  also  teazel,  teazle,  n.,  a  plant  of  the  genus Dipsacus',  esp.  Dipsacus  fullonum,  i.e.  the  fuller’s teasel.  —  ME.  tesel,  fr.  OE.  txsel,  rel.  to  txsan, ‘to  pluck;  to  tease'.  See  prec.  word. Derivatives:  teasel,  tr.  v.,  teasel-er,  teazl-er,  n.
38351-teat,  n.  —  ME.  tete,  fr.  OE.  tete,  fr.  OF.  tele  (F. tette),  which,  together  with  It.  tetta,  OProven?. and  Sp.  teta,  is  of  Teut.  origin.  Cp.  OE.  tit,  LG. titte,  Du.  tit,  MHG.,  G.  zirze,  Swed.  tiss.  The Teut.  words  themselves  are  of  imitative  origin. Cp.  tit,  ‘a  teat’.
=== HJB teak ===
143:The  words  with  which  we  have  to  do,  taking  the  most  extensive  view  of the  field,  are  in  fact  organic  remains  deposited  under  the  various  currents of  external  influence  that  have  washed  the  shores  of  India  during  twenty centuries  and  more.  Rejecting  that  derivation  of  elephant*  which  would connect  it  with  the  Ophir  trade  of  Solomon,  we  find  no  existing  Western term  traceable  to  that  episode  of  communication  ;  but  the  Greek  and  Roman commerce  of  the  later  centuries  has  left  its  fossils  on  both  sides,  testifying to  the  intercourse  that  once  subsisted.  Agallochum,  carba^us,  camphor, sandal,  musk,  nard,  pepper  (Wire/w,  from  Skt.  pippali,  *long  pepper'),  ginger (^tyyi^pis,  see  under  Ginger),  lac,  costus,  opal,  malabathrum  or  folium  indicum, beryl,  sugar  {adjcxap,  from  Skt.  sarkara,  Prak.  saJdcara),  rice  (Upvia,  but  see  s.v.), were  products  or  names,  introduced  from  India  to  the  Greek  and  Roman world,  to  which  may  be  added  a  few  terms  of  a  different  character,  such  as Bpax/taret,  ^apfidyes  {sramanas,  or  Buddhist  ascetics),  ^;Xa  ffayaXLpa  koI  <r<urafi[va (logs  of  teak  and  shisham),  the  ffdyycLpa  (rafts)  of  the  Periplus  (see  Jangar in  Gloss.)  ;  whilst  dindra,  dramma,  perhaps  kastira  (*  tin,'  Kaafflrepos),  kasturl (*musk,'  Koardpiov,  properly  a  different,  though  analogous  animal  product), and  a  very  few  more,  have  remained  in  Indian  literature  as  testimony  to  the same  intercourse.t
164:Southern  India  has  contributed  to  the  Anglo-Indian  stock  words  that  are in  hourly  use  also  from  Calcutta  to  Peshawur  (some  of  them  already  noted under  another  cleavage),  e.g,  betel,  mango,  jack,  cheroot,  murigoose,  pariah, bandicoot,  teak, patcharee,  chatty,  catechu,  tope  (*a  grove'),  curry,  mulligatawny, congee.    Mamooty  (a  digging  tool)  is  familiar  in  certain  branches  of  the
4292:of  teak  from  India.  It  seems  to  be  a corruption  of  the  Span,  and  Port,  hajdy bcuulj  haixel,  baxeUa,  from  the  Lat.  vas- ceUvm  (see  Diez,  Etym,  JV&rterh,  i.  439, 8.  v.).  Cobarruviaa  (1611)  gives  in  his Sp.  Diet.  ^^Baxel,  quasi  vi^ael"  as  a generic  name  for  a  vessel  of  any  kind going  on  the  sea,  and  quotes  St.  Isidor^ who  identifies  it  with  phoMltiSy  ana from  whom  we  transcribe  the  ^usage- below.  It  remains  doubtful  whether this  word  was  introduced  into  the  East by  the  Portuguese^  or  had  at  an  earlier date  passed  into  Arabic  marine  use. The  latter  is  most  probable.    In  Gorrea
9103:DTJQQIBy  s.  A  word  used  in  the Pegu  teak  trade,  for  a  long  squared timber.  Milbum  (1813^  says:  "Dog- gies are  timbers  oi  teak  from  27  to 30  feet  lon^,  and  from  17  to  24  inches square."  Sir  A.  Phayre  believes  the word  to  be  a  corruption  of  the  Burmese htdp-gyi.  The  first  syllable  means  the 'cross-beam  of  a  house,'  the  second, 'big';  hence  *  big-beam.'
19368:SThe  botanical  name  is  taken  from  Sir ^ohn  Shore.  For  the  peculiar  habitat of  the  Sal  as  compared  with  the  Teak, see  Forsythj  Highlands  of  G.L  25  seqq,] It  Ls  strong  and  durable,  bat  very heavy,  so  tnat  it  cannot  l)e  float«<i without  more  buoyant  aids,  and  is,  on that  and  other  accoimts,  inferior  to teak.  It  does  not  appear  among  eight kinds  of  timber  in  general  use,  men- tioned in  the  Ain.  The  saul  has  been introduced  into  China,  perhaps  at  a remote  period,  on  account  of  its  con- nection with  Buddha's  history,  and it  is  known  there  by  the  Indian  name, 8o-lo  {Bretschneidtr  on  Chinese  Bot^tn. Works,  p.  6).
19372:1810.— "The  lanl  is  a  verv  solid  wood .  .  .  it  is  likewise  heavy,  yet  by  no  means so  ponderous  as  teak ;  both,  like  many  o# our  former  woods,  sink  in  fresh  water."— Waiiamson,  V,M,  ii.  69.
20007:A  term  in  the  Burmese  teak-trade ; apparently  a  corruption  from  Barm. shin-bytn.  The  first  monosyllable (shin)  means  *  to  put  together  aide  by side,'  and  &yin, '  plank,'  uie  compound word  beinff  usea  in  Burmese  for  'a thick  plank  used  in  constructing  the side  of  a  ship.'  The  shinbin  is  a  thick plank,  about  15"  wide  by  4"  thick, and  running  up  to  25  feet  in  length (see  MiUnim,  L  47).  It  is  not  sawn, but  split  from  green  trees.
20008:1791.  — "Teak  Timber  for  sale,  consistr ingof
21812:TEAK,  s.  The  tree,  and  timber  of the  tree,  known  to  botanists  as  Tec- tona  grandis,  L.,  N.O.  Verberuiceae.  The word  is  Malayal.  tekka,  Tam.  tekku. No  doubt  this  name  was  adopted owing  to  the  fact  that  Europeans  first became  acouainted  with  the  wood  in Malabar,  wiiich  is  still  one  of  the  two great  sources  of  supply  ;  Pegu  being the  other.  The  Skt.  name  of  the  tree is  idka,  whence  the  modern  Hind, name  sdgwdn  or  sdaun  and  the  Mahr. sdg.     From    this   last   probably  was
21813:taken  idj,  the  name  of  teak  in  Arabic and  Persian.  And  we  have  donbtles the  same  word  in  the  ^^aToXira  of  the Periplus,  one  of  the  exports  from Western  India,  a  form  which  may  be illustrated  by  the  Mahr.  adj.  tOffoU^ '  made  of  the  teak,  belonging  to  teak/ The  last  fact  shows,  in  some  degree, how  old  the  export  of  teak  is  trom India.  Teak  beams,  still  undecayed, exist  in  the  walls  of  the  great ''palace of  the  Sassanid  Kings  at  Selencia  or Ctesiphon,  dating  from  the  middle  of the  6th  century.  [See  Birdwood,  First Letter  Book,  Intro.  XXIX.]  Teak  has continued  to  recent  times  to  be  im- ported into  Egypt.  See  Fordeal,  quoted by  Royle  (Hindu  Medicine,  128).  The gopher-wood  of  Genesis  is  translated  tdj in  the  Arabic  version  of  the  Penta- teuch (Royle).  [It  was  probably  cedar (see  Eneycl.  Bibl.  s,v,)]
21814:Teak  seems  to  have  been  hardly known  in  Gangetic  India  in  former days.  We  can  nnd  no  mention  of  it in  Baber  (which  however  is  indexless^ and  the  only  mention  we  can  find  in the  Ain,  is  in  a  list  of  the  weights  of a  cubic  yard  of  72  kinds  of  wood, where  the  name  ^^Sdgaun"  has  not been  recognised  as  teak  by  the  learned translator  (see  Blochmann^e  E.T.  L  p. 228).
21816:*' Sailing  past  the  mouth  of  the  Gulf, after  a  course  of  6  days  you  reach  another port  of  Persia  called  Omana.  Thither  they are  wont  to  despatch  from  Barygaaa,  to both  these  ports  of  Persia,  great  T«sseU with  brass,  and  timbers  and  bMms  of  teak (^Xb^'  (rayaXbfuv  koI  docciir),  and  horns  and spars  of  shisham  (see  818800)  (tf-ao-a^iiPMr), and  of  ebony.  .  .  ." — Peripl,  Maris  Erytkr. §  35-36.
21817:c.  800.— (under  Hariin  al  Bashid)  "Fa^l continued  his  story  *.  .  .  I  heard  load wailing  from  the  house  of  AbdaUah  .  .  . they  told  me  he  had  been  struck  with  the jud&m,  that  his  body  was  swollen  and  all black.  ...  1  went  to  Rashid  to  teU  hxm, but  I  had  not  finished  when  they  came  to say  Abdallah  was  dead.  Going  out  at  onoe I  ordered  them  to  hasten  the  obeequiee;. ...  I  myself  said  the  funeral  prayer.  As they  let  down  the  bier  a  slip  took  place, and  the  bier  and  earth  fell  in  together; an  intolerable  stench  arose  ...  a  eeoood slip  took  place.  I  then  called  for  planks  of teak  {Mi,  .  .  .*'— QuoUtSon  in  Mafwdi, Prairiet  tTOr,  vi.  298-299.
21818:c.  880.— "From  Kol  to  Sindin,  where  they collect  teak-WMMi  (alj)  and  eane,  18  far-
21819:TEAK.
21823:a  940.— <'.  .  .  The  teak-iree  (sfij).  This tree,  which  is  taller  than  the  date-palm, and  more  bulky  than  the  walnut,  can belter  under  its  branches  a  great  number of  men  and  cattle,  and  you  may  judge  of  its dimensions  by  the  loes  that  arriye,  of  their natural  length,  at  iuie  depdts  of  Basra,  of 'IrSk,  and  of  Egypt.  .  .  ."— if<l*'arfl,  iii.  12.
21827:And  ivory  there,  and  teak  (al-8ij)  and aloeswood  and  sandal.  ..."
21829:The  following  order,  in  a  King's Letter  to  the  Goa  Government,  no doubt  refers  to  Peeii  teak,  though  not naming  the  particular  timber  :
21831:1602. — ".  .  .  It  was  necessary  in  order to  appease  them,  to  give  a  promise  in writing  that  the  body  should  not  be removed  from  the  town,  but  should  have public  burial  in  our  church  in  sight  of everybody;  and  with  this  assurance  it  was taken  in  solemn  procession  and  depoflited in  a  box  of  teak  (teca),  which  is  a  wood  not subject  to  decay.  .  .  ."  —  *Sb«*a,  OrienU Conquist.  (1710),  ii.  265.
21833:1681.— Bontius  gives  a  tolerable  cut  of the  foliage,  &c.,  of  the  Teak- tree,  but writing  in  the  Archipelago  does  not  use that  name,  describing  it  under  the  title **  Qu^rcus  InduxL,  Kiati  Malaiis  dicta."— Lib.  vi.  cap.  16.  On  this  Rheede,  whoseplate of  the  tree  is,  as  usual,  excellent  {Hortta Malabaricut,  iv.  tab.  27),  observes  justly that  the  teak  has  no  resemblance  to  an  oak- tree,  and  also  that  the  Malay  name  is  not Eiaii  but  Jati:  Kiati  seems  to  be  a  mistake of  some  kind  growing  oat  of  Kayti-jaUj •Teak-wood.
=== HJB sagun ===
```


## [2026-09-14T01:22:32.913Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN salamander ===\"; grep -n -i -A10 \"^salamander\" KLN_1966.txt | head -30\necho \"=== KLN Scythian ===\"; grep -n -i -A8 \"Scythian\" KLN_1966.txt | head -40\necho \"=== AHD watkins scyth ===\"; grep -n -i \"scyth\" AHD_watkins1985.txt | head -20\necho \"=== FSD salamander ===\"; grep -n -i \"salamander\" FSD_vol4.txt | head -10"
}
```


### [2026-09-14T01:22:33.046Z] TOOL RESULT

```
<persisted-output>
Output too large (35.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b5vnzgpbx.txt

Preview (first 2KB):
=== KLN salamander ===
33521:salamander,  n.  —  ME.  salamandre,  fr.  MF.  (=  F.) satamandre,  fr.  L.  salamandra,  fr.  Gk.  <rocXa|i.av- Spa,  which  is  of  uncertain  origin.
33522-Derivatives :  salamandr-ian,  salamandr-ine,  adjs. salamandroid,  adj.,  resembling  salamanders.  — Compounded  of  Gk.  ctaXapuivSpa  and  -oeiSfc, ‘like’,  fr.  clSop,  ‘form,  shape’.  See  prec.  word and  -oid.
33523-salami,  also  salame,  n.,  a  highly  seasoned,  orig. Italian,  sausage.  —  It.  salami,  fr.  L.  sal,  gen. salis,  ‘salt’.  See  salt,  n.
33524-sal  ammoniac,  ammonium  chloride.  —  See  1st sal  and  ammoniac  and  cp.  salmiac. salariat,  n.,  the  class  of  those  who  receive  sala¬ ries. — Formed  fr.  salary  on  analogy  of  proletariat. salaried,  adj.  —  Prop.  pp.  of  the  verb  salary  (q.v.) salary,  n.  —  ME.  salarie,  fr.  L.  solarium,  lit.  ‘salt- money’,  i.e.  ‘money  paid  to  soldiers  for  their allowance  of  salt’.  Solarium  is  prop,  the  neut.  of the  adjective  salarius,  ‘pertaining  to  salt’,  fr.
33525-sal,  gen.  salis,  ‘salt’.  See  salt  and  subst.  suff. -ary  and  cp.  salad,  sausage, salary,  tr.  v.  —  Fr.  prec.  word.  Cp.  F.  salarier. salat,  n.,  the  ritual  prayer  of  the  Mohammedans.
...
</persisted-output>
```


## [2026-09-14T01:22:44.760Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN Scythian ===\"; grep -n -i \"Scythia\\|Scyth\" KLN_1966.txt | head -10\necho \"=== AHD scyth ===\"; grep -n -i \"scyth\\|saka\" AHD_watkins1985.txt | head -20\necho \"=== HJB page markers near 21812 ===\"; awk 'NR>=21780 && NR<=21830 && /^[[:space:]]*[0-9]{2,4}[[:space:]]*$|page/' HJB.txt | head\necho \"=== grep TEAK page num ===\"; sed -n '21800,21815p' HJB.txt | grep -n \"9[01][0-9]\" | head"
}
```


### [2026-09-14T01:22:45.865Z] TOOL RESULT

```
=== KLN Scythian ===
2409:Amazon,  n.,  a  member  of  a  race  of  female  war¬ riors  in  Scythia  ( Greek  mythol.)  —  L.,  fr.  Gk. ’A|za£d>v,  which  prob.  derives  fr.  Heb.  ammftz, ‘strong’.  The  form  of  the  word  ’Apatov  was prob.  influenced  by  the  folk  etymology  accord¬ ing  to  which  ’Apia^tov  lit.  means  ‘without breast’,  fr.  A-  (see  priv.  pref.  a-)  and  pa£6 ?, ‘breast’  (the  Amazons  are  said  to  have  cut  off their  right  breasts  in  order  to  use  the  bow  with more  ease).
6595:Carpathian  Mountains.  —  Thracian  Gk.  Kap- nirrrjt;  opop,  lit.  ‘the  Rocky  Mountain’,  rel.  to Kaprroi,  name  of  a  Thracian  tribe,  lit.  meaning ‘the  inhabitants  of  rocky  regions’,  and  cogn. with  Alb.  karpe,  ‘rock’.  See  next  word, carpel,  n.,  a  simple  pistil  (bot.)  —  ModL.  car- pellton,  dimin.  formed  fr.  Gk.  xapTrog,  ‘fruit’, lit.  ‘that  which  is  plucked’,  fr.  I.-E.  base  *(s)qer- (e)p-,  ‘to  cut ;  to  pluck’,  whence  also  OI.  krpanah, ‘sword’,  Hitt,  karp-,  karpiyd-,  ‘to  gather,  take’. Alb.  karpe,  karmc  (for  *karp-n),  ‘rock,  crag’, skrep,  krep ,  ‘rock,  slope’,  Thracian  Gk.  Kap- ■Ki-rrfi  tipoc,  ‘Carpathian  Mountains’  (see  prec. word),  Gk.  xprimot,  ‘scythe’,  L.  carpere,  ‘to pluck,  cull,  gather’,  Mir.  corrdn,  ‘sickle’  cirrim, ‘I  beat  off,  mutilate’,  Lith.  kerpu,  kifpti,  ‘to  cut with  scissors,  shear’,  Lett,  cqrpu,  cirpt,  of  s.m., dial.  Russ,  cerp,  ‘sickle’.  For  Teut.  cognates  of the  same  base  see  harrow,  harvest,  scurf,  sharp. Cp.  carp,  intr.  v.,  carpet,  Carpinus,  acarpous, acrocarpous,  amphicarpic,  cremocarp,  Crepidula, Crepis,  discerp,  endocarp,  epicarp,  excerpt,  me- ricarp,  mesocarp,  monocarpic,  pericarp,  scarce, schizocarp,  syncarp,  xylocarp.  I.-E.  *(s)qer(e)p- is  an  enlargement  of  base  *(s)qer-,  ‘to  cut’, whence  Qk,  y.ei pew  (for  *v.i pieiv),  ‘to  cut,  shear’, L.  card,  ‘flesh,  meat’.  See  carnal, carpenter,  n.  —  ME.,  fr.  ONF.  carpentier  (corre¬ sponding  to  F.  charpentier),  fr.  Late  L.  carpen-
6830:Caucasian,  adj.  and  n.  —  Formed  with  suff.  -ian fr.  L.  Caucasus,  fr.  Gk.  Kauxaau;,  fr.  Scythian Kpoo-xxcu.?,  ‘Caucasus’,  a  compound  meaning lit.  ‘(the  mountain)  shining  with  ice’;  see  Walde- Hofmann,  LEW.,  I,  pp.  295-96,  s.v.  criista.  The first  element  of  this  compound  is  a  derivative  of I.-E.  base  *qreu-,  ‘to  be  icy’.  For  derivatives  of *qrus-,  an  enlarged  form  of  base  *qreu-  see crust,  crystal.  The  second  element  is  rel.  to  Gk. y.odsiv  (for  "xifieiv),  ‘to  burn’ ;  see  caustic, cauchemar,  n.,  incubus.  —  F.,  a  hybrid  coined from  the  blend  of  OF.  chaucer  and  Picard  cau- quer,  ‘to  trample’  (both  derived  fr.  L.  calcare, of  s.m.,  fr.  calx,  gen.  calcis,' heel'),  and  fr.  MDu. marc,  incubus'.  See  Calceolaria  and  mare,  ‘in¬ cubus',  and  cp.  the  first  element  in  caltrop, caucus,  n.,  private  meeting  of  the  leaders  of  a  poli¬ tical  party.  —  A  word  of  Algonquian  origin,  lit. meaning  ‘counselor’.
10300:Danaiis,  n.,  a  king  of  Argos,  who  commanded  his fifty  daughters,  the  Danaides,  to  murder  their husbands  on  the  wedding  night  ( Greek  mylhol.) —  L.  Danaus,  fr.  Gk.  Aavaop  (whence  the  pi. Aavaoi, ‘theDanaans’,  i.e.  ‘descendants  or  sub¬ jects  of  Danaiis’,  whence  ‘the  Greeks’,  in  gen¬ eral),  which  prob.  derives  fr.  Heb.-Phoen.  Dan, and  lit.  means  ‘one  who  judges’;  see  Dan,  PN., and  cp.  Danae,  Danaides.  This  etymol.  is  cor¬ roborated  by  the  fact  that  the  myth  of  Belus and  the  Danaides  “records  the  early  arrival  in Greece  of  Helladic  colonists  from  Palestine” (quoted  from  Robert  Graves,  ‘The  Greek Myths’,  I,  p.203.  Penguin  Books).  For  other Greek  mythological  names  of  Hebrew  origin cp.  Cadmus,  Niobe.  —  According  to  Kretsch¬ mer,  Glotta  24,  15  fT.,  the  Danaans  are  identical with  the  men  of  Tanaus,  king  of  the  Scythians, who  allegedly  came  to  Argos  in  the  15th  cent. B.C.E.  and  became  blended  with  the  Greeks. Kretschmer  also  assumes  that  there  is  a  relation¬ ship  between  Tanaus  and  the  river  names  Tanais and  L.  Danubius  (whence  F.  and  E.  Danube), and  Ddnu-,  name  of  an  Indo-Iranian  people. See  Frisk,  GEW.,  I,  p.347  s.v.  Aavaot  and  cp. Albert  Camoy,  Dictionnaire  etymologique  de la  mythologie  greco-romaine,  p.42  s.v.  *Da- naos.  —  Cp.  Danae,  Danaides.
17558:hemostat,  haemostat,  n.,  anything  that  stops hemorrhage;  specif.,  an  instrument  used  to compress  a  bleeding  vessel.  —  Fr.  hemostatic, hemostatic,  haemostatic,  adj.,  serving  to  stop hemorrhage;  styptic.  —  Compounded  of  hemo- and  Gk.  oxaxixoe;,  ‘causing  to  stand’.  See  static, hemp,  n.  —  ME.,  fr.  OE.  hsnep,  henep,  rel.  to OS.  hanap,  ON.  hampr,  Swed.  hampa,  Dan. hamp,  MDu.,  Du.  hennep,  OHG.  hanaf,  MHG. hanef,  hanf  G.  Hanf(—  Teut.  *hanap).  Cp.  Gk. xawotfki;  (whence  L.  cannabis),  Arm.  kanap‘. Alb.  kanep,  Russ.-Church  Slav.  konoplja(  whence Lith.  kanapes),  ‘hemp’.  All  these  words  are loan  words  from  a  foreign,  possibly  Scythian, language.  Cp.  canvas,  canvass.  Cp.  also  sunn. Derivative:  hemp-en,  adj.
18299:hyal-,  form  of  hyalo-  before  a  vowel, hyalin,  n.  — -  See  hyaline,  n. hyaline,  adj.,  glassy;  transparent.  —  L.  hyalinus, fr.  Gk.  udXtvo;,  ‘glassy’,  fr.  oaXo;,  ‘alabaster, crystal,  amber’,  prop,  ‘a  transparent  stone’,  later ‘glass’,  which  prob.  stands  for  *sualo-.  Cp.  L. suali-ternicum,  ‘a  kind  of  reddish  amber’,  which, according  to  Pliny  37,  33,  »s  of  Scythian,  i.e. North  European,  origin.  See  Boisacq,  DELG., p,996,  s.v.  uaXo;,  and  Walde-Hofmann,  LEW, II,  61 1,  s.v.  sualiternicum.  For  the  ending  see suff.  -ine  (representing  Gk.  -ivo;). hyaline,  n.,  1)  something  glassy,  as  the  smooth sea  or  the  clear  sky;  2)  (in  this  sense  spelled  also hyalin)  a  substance  forming  the  walls  of  hydatid cysts.  —  See  hyaline,  adj.
32823:rhombus,  n.,  an  oblique-angled  equilateral  paral¬ lelogram.  —  L.  See  rhomb, rhoncial,  also  rhonchal,  adj.,  pertaining  to  arhon- chus.  See  next  word  and  adj.  suff.  -al. rhonchus,  n.,  a  whistling  sound  heard  on  the auscultation  of  the  chest.  —  L.,  ‘a  snoring’,  fr. Gk.  poy-/_o;,  which  is  rel.  to  (56yxo;,  friyyoq, ply xo;,  of  s.m.  plyysiv,  peyxEtv,  ‘to  snore’; prob.  of  imitative  origin, rhotacism,  n.,  mispronunciation  of  the  letter  r.  — ModL.  rhotacismus,  fr.  Gk.  ptoTaxiopoc,  fr. pwraxlqEiv.  See  next  word  and  -ism. rhotacize,  intr.  v.,  to  mispronounce  the  letter  r. — Gk.  ptoTaxi^Eiv,  ‘to  use  the  letter  r  excessive¬ ly’,  fr.  p<7>,  name  of  the  letter  r.  See  rho  and  -ize. rhubarb,  n.,  a  garden  plant  with  large  leaves  and edible  leaf  stalks.  —  ME.  rubarbe,  fr.  MF.  reu- barbe,  rubarbe  (F.  rhubarbe),  fr.  ML.  rheubar- barum.  The  first  element  in  ML.  rheubarbarum derives  fr.  L.  rheum,  fr.  Gk.  ptjov,  ultimately  fr. Pers.  rewend,  ‘rhubarb’  (whence  also  Russ. reven).  Cp.  the  ML.  form  rhabarbarum,  which comes  fr.  Gk.  pec  fSxppapov,  lit. ‘foreign  rhubarb’ ; px,  ‘rhubarb’,  is  a  blend  of  pvjov,  ‘rhubarb’,  with 'Pa,  the  Scythian  name  of  the  Volga;  see  roric. The  second  word  in  pa  |3xp!3xpov  refers  to  the foreign  origin  of  the  plant.  It.  rabarbaro  (whence G.  Rhabarber)  derives  fr.  Gk.  pa  |3dpj3xpov.  Cp. rhapontic,  rheum.
33106:roric,  adj.,  pertaining  to  dew.  —  Formed  with suff.  -ic  fr.  L.  ros,  gen.  roris,  ‘dew’,  which  is  cogn. with  Lith.  rasa,  OSlav.  rosa,  ‘dew’,  Ol.  rasah, ‘sap,  juice,  fluid,  essence’,  rasa,  ‘moisture’,  Rasa, name  of  a  mythic  river  (=  Avestic  Rahha), aryati,  ‘flows',  rsabhdh,  ‘bull,  steer’,  Avestic  and OPers.  arshan,  ‘man’,  Hitt,  arszi,  ‘flows’,  Gk. Sp  ary,  jipp  tjv.  ‘male,  masculine’,  prob.  also  'Pa, Scythian  name  of  the  Volga,  fr.  I.-E.  base  *ras-, *eras-,  *eres-,  *ers-,  ‘to  flow,  wet,  moisten’.  Cp. rasa,  romerillo,  rosemary,  rosolio,  rouse,  ‘to pickle'.  Cp.  also  the  first  element  in  rhubarb  and the  second  element  in  Ahasuerus  and  in  Xerxes, rorqual,  n.,  any  whale  of  the  genus  of  large  whales, the  Balaenoptera.  —  F.,  fr.  Norw.  reyrhval,  fr. ON.  reydarhvalr,  fr.  reydr,  ‘rorqual’  (fr.  raudr, ‘red"),  and  hvalr,  ‘whale’.  See  red  and  whale. Rosa,  1)  fern.  PN.;  2)  a  genus  of  plants,  the  rose (bot.)  —  L.  rosa,  ‘rose’.  See  rose.
34001:Derivative:  sccnographic-al-ly,  adv. scenography,  n.,  painting  in  perspective.  —  F. scenographic,  fr.  L.  scaenographia,  fr.  Gk. axTjvoypacptS,  ‘scene-painting’,  which  is  com¬ pounded  of  ax7]V7],  ‘stage,  scene’,  and  -ypoctpia, fr.  ypx9£tv,  ‘to  write’.  See  scene  and  -graphy. scent,  tr.  and  intr.  v.  —  ME.  senten,  fr.  OF.  (  = F.)  sentir,  ‘to  feel,  to  smell’,  fr.  L.  sentire,  ‘to feel’.  See  sense.  The  c  in  the  present  English spelling  shows  the  influence  of  the  spelling  of the  word  science.  For  a  similar  insertion  of  the letter  c  cp.  scythe.
34323:Derivative:  scyph-ose,  adj. scythe,  n.,  a  mowing  implement.  —  ME.  sithe,  fr.
=== AHD scyth ===
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
900:a. Old English risan, to rise: RISE; b. Old English drisan, to arise (G-, up, out): ARISE. 2. Germanic causative *raizjan in: a. Old English réran, to rear, raise, lift up: REAR?; b. Old Norse reisa, to raise: RAISE.] rtko-. Bear. 1. Latin ursus, bear (< *orcsos): URSINE. 2. Greek arkios, bear: aRcTIC, ARcTURUS. 3. Celtic *arto- in Welsh arth, bear, in the name Arthur (> Medieval Latin Artorius, Arthur): ARTHUR. [Pok. tktho-s 875.] ruk-1, Fabric, spun yarn. Celtic and Germanic root. 1. Germanic *rukk6n- in: a. Italian rocca, distaff: ROCKET!; b. Old High German rocko, distaff: ROCAM- BOLE; C. Old French rocquet, head of a lance: RATCHET. 2. Germanic *rukka- in Old French rochet, rochet: ROCH- ET. [Pok. ruk(k)- 874.] ruk-2. Rough. Extension of reu-2. 1. Lengthened-grade form *rik- in Germanic *riéhwaz in Old English rih, rough, coarse: ROUGH. 2. Lengthened variant form *rig- in Latin riga, wrinkle: RUGA, RUGOSE; CORRUGATE. [In Pok. 2. reu- 868.] runo-. Mystery, secret. Germanic and Celtic technical term of magic. Germanic *riinaz in: a. Old English riinian, to whisper: ROUND?; b. Old Norse riin, secret writing (akin to the Germanic source of Finnish runo, song, poem): RUNE!, RUNE?. [In Pok. 1. reu- 867.] sa-. To satisfy. Contracted from *sas-. 1. Suffixed zero-grade form *s9-to- in: a. Germanic *sadaz, sated, in Old English sed, sated, weary: SAD; b. derivative Ger- manic verb *sadon, to satisfy, sate, in Old English sadian, to sate: SATE!. 2. Suffixed zero-grade form *s9-ti- in Latin satis, enough, sufficient: SATIATE, SATIETY; (ASSAI2), ASSET, SATISFY. 3. Suffixed zero-grade form *s9-tu-ro- in Latin satur, full (of food), sated: SATIRE, SATURATE. 4. Suffixed zero-grade form *so-d-ro- in Greek hadros, thick: HADRON. [Pok. sd- 876.] sab-. Juice, fluid. 1. Germanic *sapam, juice of a plant, in Old English sp, sap: SAP}. 2. Illyrian sabaium, beer, probably akin to the source of Italian zabaglione, zabaione, a frothy dessert: ZABAGLIONE. [In Pok. sap- 880.] sag-. To seek out. 1. Suffixed form *sdg-yo- in Germanic *sdkjan in Old English sécan, sécan, to seek: SEEK. 2. Suffixed form *sdg-ni- in Germanic *sdkniz in Old English sdcn, attack, inquiry, right of local jurisdiction: SOKE. 3. Zero-grade form *sog- in Germanic *sak- in: a. derivative noun *saké, “a seeking,” accusation, strife, in Old English sacu, lawsuit, case: SAKE}; b. Germanic *sakjan, to lay claim to (denominative of *sak6), in Old French seisir, to take possession of, seize: (SEISIN), SEIZE; c. Germanic *sakan, to seek, accuse, quarrel, in (i) Old English forsacan, to renounce, refuse (for-, prefix denot- ing exclusion or rejection; see per'): FORSAKE (ii) Old Norse saka, to seek: RANSACK. 4. Independent suffixed form “sdg-yo- in Latin sdgire, to perceive, “seek to know”: PRESAGE. 5. Zero-grade form “sog- in Latin sagdx, of keen perception: SAGACIOUS. 6. Suffixed form *sdg-eyo- in Greek hégeisthai, to lead (< “to track down”): EXEGESIS, HEGEMONY. [Pok. sdg- 876.] sai-. Suffering. 1. Germanic *sairaz, suffering, sick, ill, in Old English sdr, painful: sore. 2. Derivative Germanic adjective *sairigaz, painful, in Old English sarig, suffer- ing mentally, sad: SORRY. [Pok. sdi-, 877.] sak-. To sanctify. 1. Suffixed form *sak-ro- in: a. Latin sacer, holy, sacred, dedicated: SACRED; CONSECRATE, EXECRATE; b. compound *sakro-dhét-, “performer of sacred rites” (*-dhét-, doer; see dhé-'), in Latin sacerdés, priest: SACERDOTAL. 2. Nasalized form *sa-n-k- in Latin sancire (past participle sanctus), to make sacred, conse- crate: SAINT, SANCTUM; CORPOSANT, SACROSANCT, SANC- tiFy. [Pok. sak- 878.] sal-1, Salt. 1. Extended form ‘*sald- in: a. suffixed form *sald-o- in Germanic *saltam in Old English sealt, salt: SALT; b. Germanic zero-grade suffixed extended form *sult-j6 in (i) Old French sous, pickled meat: SOUSE (ii)
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
=== HJB page markers near 21812 ===
=== grep TEAK page num ===
6:910
```


## [2026-09-14T01:22:46.173Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT saka ===\"; grep -n -i \"saka-\\|Sakastāna\\|sakasta\" BRT.txt | head -20\necho \"=== KNT saka ===\"; grep -n -i \"Sak\\|Scyth\" KNT.txt | head -30"
}
```


### [2026-09-14T01:22:46.256Z] TOOL RESULT

```
=== BRT saka ===
3510:•  j.  apajcraosaka-  Adj.  'schmähsUchtig' : nivayaka  mpalnaka  apa.skaraka  'ia(NP.) ima  paiti.vJsfTUe  Yt5.95.
17240:Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
22169:Ableit  aus  "vatsaka-  m.  EN.,  Feldherr  de* Fraarasyan  (mp.  veiak,  np.  i'iSra);  vgl.  Bd.  J/. 16,  Ük.  s-   15.  a  (,  23.  6),  JusTi  NB.  366.
25898:■  p.  saka-  Adj.,  bezeichnet  ein  Volk 'Sake,  Skythe'*':  iyam  sku'ki^  hyi^  'kJ' Bh,k;S.j; —  'kä  *Aaumavaria  (sd.)  'kä tigraxauda  (sd.)  .  .  *ka  tyaiy  *tara^drayc^ (sd.)  D.  6. 3;  5.  a.  a)  Sing,  in  kollekt. Sinn :  ima  dahyäv(^  tyä  mana  paHyaisi^ ..  -itf*  Bh.l.6;2.2.
=== KNT saka ===
335:III. Among the less known Old Iranian lan- guages the most important was Median, known only from glosses, place and personal names, and its developments m Middle Persian, apart from borrowings in OP, which are of considerable im- portance for the understanding of OP itself. Others were the language of the Carduchi, pre- sumably the linguistic ancestor of modern Kurd- ish; Parthian, the language of a great empire which contended against Rome in the time just before and after the beginning of the Christian era; Sogdian in the northeast, the ancestor of the medieval Sogdian; Scythian, the language or languages of the various tribes known in OP аз Saká, located to the east of the Caspian and north of Parthia and Sogdiana, but also to the west of the Caspian on the steppes north of the Euxine Sea.
343:dialects, including the Arsacid and the Sasanian types, the Sogdian (known also from a trilingual inscription of Kara-Balgassün), and a dialect known as ‘Eastern Iranian’, perhaps a derivative of northeastern Scythian, in which there are texts of the Buddhists of Khotan. The notable peculiarity of these Turfan texts is that they are written in relatively pure Iranian, without the Semitic writings for the words which are to be spoken by the Тташап equivalent.
344:V. Among the earliest traces of Pahlavi, how- ever, are certain legends in Greek characters on coins of Indo-Scythic rulers of the Turuska dy- nasty in northwestern India, belonging to the first two Christian centuries.
352:VII. The Ossetic dialects, in the general re- gion of the Caucasus; derived from the Scythian of Southern Russia. |
774:аз in $172. — н XSakya = Х$аһуй A'Bd 2, for XSley'a XShyà or Хюу уа = XSyahyé.
824:DN xv iyam : Saké : hgraza|udá] ‘this is the
825:Pointed-Cap Scythians’.
826:DN xxix Фуат: Maciya ‘this is the men of Maka’. А?Р 9 tyam : така ‘this is the Drangians’. А?Р 14 туат : Sakü : hawmavarga ‘this is the
827:Amyrgian Scythians’.
828:А?Р 15 йат : Saka : tigraralud|a (as above). А?Р 23 iyam : Yaund ‘this is the Ionians'. A?P 24 бат : ака : paradratya ‘this is the
892:IV. The following clusters of two consonants occur medially between vowels: zt z6* xn zm* zr ak, gd gn gm gr, jy, tp* tr*, üb* Om Gr*, dr du, ny то, fr, br, mn my, rk rz rg rc rj rtrd rd rn rb rm ry то r$ T$, ld*, st sp sm, Šk Sc М $d* $n. šp šm Sy &, zd 2b* zm гт, hy. In the clusters nk nz* ng nt nd mp mb hm hv, all of which actually occur, the prior sound is omitted in the writing. Of those marked with *, 00 occurs by analogical formation; 10 only in an uninterpretable word; zm, 67, and zb, only in Median words; nz only in a Scythian name; tp, tr, ld only in non-Iranian names of persons and places; Sd only in apparently cor- rupt writings.
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1447:only after ? and и): Kapisakani-, Kūša-, Cispi-, Patisuvari-, Adukanatsa-, Cüsa-, ete.
1580:The place name Káp?Sakám-.
1583:kasaka-, kásakaina-.
1770:-I- stems: Arakadri-, Küpisakàni-, Cicirri-, Cišpi-, Pütisuvüri-, Vispauzüti-.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1812:ПІ. Secondary -ina-, forming adjectives: afa^- ga-ina-, küsaka-ina-, nauca-ina-.
1943:ШЇ. Names of other Iranians: the Margian (Bactrian) Frada-; the Scythian Sku*xa-; un- specified Afiyabaukna-, Arsake-.
1951:ably = Artazáaga), Vasdasaka, Vahyav'Sdapaya, Hadaxaya.
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
2010:57 Same as Fem. as Derivative Pl. Ethnic Masc. as Province Ethnic Province Ethnic as Province Province Babirus X Babiruviya Maka Maciya* Мастӣ Майа X Mudraya X Mudraya Yauna X Yauna Saka X Saká Saka Sug(u)da Skudra x* Sparda Spardtya Zraka x* Натайа Harawats§ Harauvatiya* Hiduš Hiduya*
2027:Nom. Sg. martiya, х$йуабтуа, Ката, baga, drauga, hamiciya, атиќа; man’s name, Kabijiya; place names and ethnics Раза, Майа, Sugda Suguda, Saka, Sparda, Mudréya, Uja боја, Yauna, Parðava, Armina, Arminiya, Asagaria, Gadāra, Márgava, Uyjiya.
2043:Acc. Pl. martiyd, xSayatiyd, hamigiyà, Saké, ауа, ufra&ta.
2044:Inst. Pl. asabára:b$, martiyaibiš, hamigtyaibis, bagaibi, vibaibiš, kamnarbis; Мааа, Sakai- b, Pardavaibis, Mārgavaibiš, Üvjiyaibis; nt. ünaraibiš,
2047:Nt. Nom. Sg. zsacam, dusiyaram, ardatam, darant- yam, aruvastam, dàtam, Sakatam, kartam, visam, kamnam; aec. xsagam, stánam, daraniyam, aru- vastam, kartam, visam, uvdipasiyam, uvaspam, probably casam.
2124:Nom. Sg.: skauliš, pasti&, barmiS, yaumainis aydu- (та)йи$; the personal names Fravarti§, Da- dar Sis, Cišpiš; the ethnic PatiSuvaris; perhaps the place-names Arakadri$, KapiSakaniS, Viš- [pa]uz[a]ti$.
2648:§244, Tue FUTURE PASSIVE PARTICIPLE IN -elo- is typified by Skt. yajatá-, Av. yazata- ‘worthy of worship’, to (Skt.) yaj- ‘worship’; but the forma- tion often comes to have virtually the force of a perfect passive in -/0-: cf. Skt. pacaid-, but Gk. merrós, Lt. coctus ‘cooked’. Cf. also СК, &-exeros ‘unchecked’, to éyw ‘I hold, have’. The OP ex- amples happen to be from intransitives, and are therefore active in meaning: nsn. dakatam, npn. Sakata ‘past’, to root ak- ‘pass’; and -gmata- ‘gone’ to gam- ‘go’, in npm. ha"-gmatd ‘assembled’, nsf. pará-gmalü ‘gone forth’, perhaps nsf. [ava- дтађа ‘gone down, fallen’, cf. Av. yomata- as well as the regular passive participle gata- (pIE *g*m- to-, also in Skt. gald-, Gk. -Baros, Lt. ventum).
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
2717:Е. With Ласа, to denote place from which: DPh 5 (and DH 4) hacé Факат ‘from the Scythians’; but perhaps the ablative form in the plural had been lost, and its functions been taken over by the instrumental form, for there is no distinctly abla- tive plural form recorded in OP.
```


## [2026-09-14T01:22:56.098Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-14T01:22:57.415Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
```


## [2026-09-14T01:22:58.485Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 سکا ===\"; grep -n \"سکا\\b\\|سگزی\\|سیستان\\|سگستان\" BQT_v2_pages.txt | head -20\necho \"=== BQT v2 pdf page tags sample ===\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3; grep -c \"\\[pdf page\" BQT_v2_pages.txt"
}
```


### [2026-09-14T01:22:58.569Z] TOOL RESULT

```
=== BQT v2 سکا ===
1939:                                                                                 ‫جفت گاو سکاو زر‬
2097:  ‫آدمی لیز بکار میرفته‪« :‬دیدم که بیاوردند اورا دریار؟ جل بصوف سپیدتر ازحربر‪ « ».‬تاریخ‌سیستان‬
5528:    ‫ی بت آمروز ‪atbsec‬‏ ‪.‬‬       ‫(‪ « )۲‬تاریخ سیستان ‪ ۸۲‬متن وحاشیه»‬      ‫شت‬
5577:      ‫در مروشاهجان نیز ‪11‬ا‪٥‬‏‬   ‫در بیتی از رود کی چمش «تارینسیستانص‪۷٩ ۹۱۳‬‏ ورك ‪ :‬چمش ‪.‬‬
10158:  ‫که از اسکاندیناوی مأخوذست و در اصطلاح علمی آنرا ‪ 8000201۷1 50۲6608021‬کوبند‬
12135:                                                 ‫فرخی سیستانی ‪« .‬رشددی»*‪.‬‬
12738:                   ‫خط سکام‬
13382:            ‫ببانگ شیشم‪ .‬بابانگك افسرسگزی‬                  ‫‪ - ۷‬بگیربادة نوشن ونوش کن بصواب‬
13748:          ‫‪ ۱ ۸‬خنده خرش » خندیدن و چون مسخره بود ‪ .‬فرخی (سیستانی) گوید ‪:‬‬                                                            ‫مکان) ‪.‬‬
13843: ‫است که ماه تابان (‪ )۳‬باشد ‪ -‬وصبح صادق رائیز‬                        ‫تالی وکاف فارسی‌وضم بای ابجد وفوفانی سکان»‬
14047:  ‫‪ +‬فرخی سیستانی‪.> ۹۷۱‬‬
14062:  ‫نزدیکی درباچة زره (هامون ) سیستانست ‪.‬انرا هم « کوه خدا» گویند وهم «کوء خواجه » (اين‬
15527:‫درسیستان متعارفست؟ ‪ -‬ودرسرمه‌سلیمانی بمعنی‬                                ‫خیره » بمعنی خیزبگیر است‪,‬وآن نوعی ازباز‬
16116:‫داسفاله (داسکاله)‬             ‫سر کج باشد‪.‬‬                ‫و مثل باشد ‪ - ۴‬و حکات و افانه را لز‬
20417: ‫دندان داشتی سکابه از چشم‌داشت‬
22383:                             ‫زورین راء بعد ازان دبوالآ قرا ببرید ‪« »...‬تاریخ سیستان ‪4۸۳٩‬‏ ‪.‬‬
22581:                                                                   ‫نیگ‪-‬لیی ‪ .‬لبدل واسکات › ‪.‬‬
24082:     ‫جذاب ‪ 7728۵0۷۳6‬و قصر واقع در «کوه خواجه» (سیستان) بارویگر درسغنرانی (هرتسفلد)‬
25132:                                                               ‫وبز کوهی باشد ‪ .‬فرخی (سیستانی گ‬
25136:                              ‫‪ «۴‬رنگه‪ ۰‬حیلت و وستانبافشدرخ»ی (سیستانی) فت ‪:‬‬
=== BQT v2 pdf page tags sample ===
0
```


## [2026-09-14T01:23:02.114Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json; d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:23:03.243Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
```


## [2026-09-14T01:23:07.810Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## BQT v2 leaf 618 (printed ~1158)\"; awk 'BEGIN{RS=\"\\f\"} NR==619' BQT_v2_pages.txt | head -80"
}
```


## [2026-09-14T01:23:08.699Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## BQT v2 leaf 626 (printed ~1166)\"; awk 'BEGIN{RS=\"\\f\"} NR==627' BQT_v2_pages.txt | head -80"
}
```


### [2026-09-14T01:23:08.847Z] TOOL RESULT

```
########## BQT v2 leaf 618 (printed ~1158)
  ‫اه‬       ‫هی‬
                                                                                                                ‫سکوبا‬
 ‫وره‌ومس‬
       ‫است ‪ -‬ودرعربی لقشی که برروی طلا نف‬
                                                                    ‫سکو با ‪ » ۱‬منم اول وثائی وبای ابجد‬
 ‫وبند که نقش‌زر‬
              ‫گز‬‫رایج باشد ‪ - ۷‬وآهنی را ی‬                            ‫بالف کشیده ‪ ,‬لام عایدی است صاری که دبری‬
‫ننده باشند ‪ -‬وآحتیکه زمین‌را‬ ‫رابج را بکرآ‬
                                                                    ‫ساخته بود و بناماو مشهور شد ‪ .‬کوبند عیسی؟‬
‫بدان شیا رکنند ‪ -‬و کوچه وبازار ‪ - ۷‬ودرختان‬
 ‫خرما که صف زده باشند ‪ -‬و کنابه از صورت‬
                                                                    ‫بدبر او رفت و ارآنجا بآسمان صعود کرد و؛با‬
                                                                     ‫بای فارسی هم‌بنظر آمده است که سکویا باشد‪.‬‬
‫و رخاری که خط برآورده‌باشد ‪ -‬وهرچیزی که‬
                                                                    ‫سکو ره ‪ = ۲‬یم اول وثانی و فتح‌رای‬
                      ‫خوب بنظر درآید ‪.‬‬
                                                                      ‫ہة کی باشد‪.‬‬    ‫کتاکه‬
                                                                                         ‫قرشت " بمعنی‌سکره اس‬
‫سکی رغلا ‪ ۰ ۸‬بنتح اول و رای‬
‫ایاست‪ .‬وآن‬   ‫قرشت » بر وزن و مرعنغیلسق‬                              ‫سکو هنج؟ بم اولوثائی وواوه‌جهول‬

 ‫نی بلشد ان و ککوبرند‪ .‬خان ومع‬                                      ‫گوند»‬   ‫وجیم ‪ ۳‬خارخسك!‬       ‫و فتح ها وسکون‌لون‬


 ‫آن بعربی کثیرالارجل باشد یعنی بسیار پا "آون‬                                          ‫‪۳‬‬   ‫باشد مە گوشه‬        ‫وآن خاری‬


 ‫درایی است که بسفایج گوبندش و بسقایج معرب‬                           ‫آخر‬   ‫بقتح اول و سکون‬       ‫‪-.‬‬   ‫سکوی‬

 ‫بس پايك است‪ .‬اکر قدری از آن درشیراندازند‬                           ‫که تحتانی باشد ‪ ۰‬بمعنی سکو است که بلندی‬
                                              ‫شیر را ببندد ‪.‬‬        ‫درخت و امثال آن‬            ‫دخراله و بیاغابوهای‬
‫سگیزژ * » بکر اول بر وزن ستبز ‪۰‬‬                                                                                  ‫باشد ‪.‬‬
 ‫بمعنی برجستن ‪ -‬وآلیز زدن و جفته انداختن‬                            ‫سکو بنه * ‪ -‬ختح ارل و کر الك »‬
   ‫ختیوز‬  ‫ستور باشد ‏ و بمعنی جهنده و ج‬
         ‫‪ -‬و امر بدین معتی همآمده ات‬                   ‫که‬
                                                                    ‫آست‬      ‫ین‬
                                                                              ‫وب‬‫باشد دوابی شبیه بخیار زه و بهت‬
‫سگیز ان ^ ‪ -‬بکر اول و رای نقطه‬                                       ‫که بروش سفید و درواش بسرخی مابل‌باشد‪.‬‬
      ‫یتز‬
        ‫خ جس‬
           ‫ونی‬
             ‫دار بالف کشیده و بنون زده » بمع‬                        ‫اول و فتح ثالیمشدد »‬       ‫بکر‬       ‫سگه =‬
                                 ‫کنان باشد‪.‬‬                          ‫بمعنی طرز وروش وقاعده و فالون باشد وسیرت‬
                                                                    ‫و اموس را یز گویند ‪ -‬ویتعتی‌لبای‌هم آمده‬
      ‫لفغت ابرانی‌شده از‪, 50006810‬ونانی (مدبر‪ ,‬ملاحظ‪,‬بعدها مقامی‌برای روحایان‬                             ‫‪۱‬‬
                                                                               ‫اسقف (عر) (ھ‪.‬م‪: (.‬‬        ‫میحی) =‬

          ‫که (کر) ازبهر مریم سکویا شدم‪.‬‬                                     ‫بموبد لماید که ترسا شدم‬
  ‫‪.‬‬     ‫ورك ‪ :‬مزدستا ‪۹۷۴‬‬               ‫‪TAT‬‏‬     ‫‪ ۹‬ص‬     ‫‪ 2‬شاهنامه بخ‬


      ‫گریزم بر در دیر سکوبا ؟ د خاقانی شروانی ‪۱۲۰۰‬‬                             ‫چرهمائی که از ظبلهمودی‬
                                                                                                    ‫ف‬
       ‫سکیینه (ھ‪.‬م‪(.‬‬       ‫<‬       ‫‪۵‬‬     ‫سکو(ه‪.‬م‪).‬‬     ‫=‬    ‫‪۴‬‬   ‫ن‬    ‫‪ ۴‬رلك ‪ :‬شکوهنج‬        ‫‪۰‬‬   ‫سکره («‪.‬م‪).‬‬       ‫=‬   ‫‪۲‬‬


                                              ‫‪ - ۱‬نبید تلخ‌چه انگوری وچه‌مویزی(میویزی ‪.‬دهشدا)‪.‬‬
       ‫دامفایی ‪۸‬ص‬      ‫«منوچهری‬          ‫بی‌سکه ‪۰‬‬     ‫سم جه باسکه وجه‬         ‫يفف‬

          ‫گوی دز که ‪۰‬‬              ‫ار‬   ‫خود یږ دراو‬                 ‫‪ - ۲‬من ولبیدو بخاله درون سماعو رباب‬
  ‫‪.‬‬      ‫دامغالی ‪۰‬‬      ‫‪ ۶‬هنوچېری‬

  ‫) سيار ‪ ۰,‬زباره ‪ 0‬زر گه) ‪۰‬‬              ‫‪igas‬‏ از رشه ‪aS‬‏‬            ‫سی رغلا («‪.‬م‪ ).‬از ‪ :‬ا‬          ‫=‬    ‫‪۸‬‬

      ‫‪ = ( 21۵6۲ +‬رجل عربی ‪ ,‬با) رك ‪ :‬فرهنکه سریانی انگلیی تألیف طانص‪enyaP ۹‬‏‬
  ‫ودلیل الراغبین فی‌لفة آلارامیین تألیف القس عمقوب اوجین‌منا الکلدالی‌چاپ‌موصل ‪ = ۰۰۹۱‬کثیر‬
  ‫‪.‬‬    ‫سکیزیدن‪‎‬‬   ‫‪:‬‬   ‫رك‬       ‫‪٩‬‬              ‫الارجل (عر) = بسفایج == ‪( 600810۳‬فر) «لك ‪۲‬ص ‪۲۷۲٩‬‏ ‪.‬‬
```


### [2026-09-14T01:23:09.919Z] TOOL RESULT

```
########## BQT v2 leaf 626 (printed ~1166)
  ‫‪-۱۱۲ -‬‬
‫آن گذارند ‪ -‬و هر سبد را لمز‬                 ‫که چزها در‬            ‫وثانی‌درعربی‬    ‫ویفتح اول‬      ‫ے‬   ‫باین معنی آ مده است‬


 ‫کویند عموماً و سبدی که مار گیران مار درمیان‬                      ‫پیشی فروختن وخربدن غله‌است که هنوزنرسیده‬
                              ‫آکننند (‪ )۲‬خصوصا ‪.‬‬                  ‫باشد و بیع سلم همان است ‪ -‬و بممنی گردن‬
                                                                 ‫صم ارل‌وفتح‬      ‫تاو‬       ‫‪r‬‏‬   ‫کردن هم‬
 ‫سکون‬      ‫اول و الی و‬      ‫یک‬      ‫‪ ۴‬ه‬     ‫سلح‬                                                               ‫لپادن واطاعت‬


                                                                  ‫تالی مشدد ؛ در عربی زینه پایه ودردباترا گوبند‬
‫که مستمد قتال و جدال و شخص سلاح بته‬                              ‫و بکر اول و سکون ثانی عم در عربی اشنی‬

                                ‫باشد ‪۰‬‬      ‫ومةدمةالجش‬
                                                                          ‫وصلح راکوبن دکه درمقابل جنگ است‪.‬‬
 ‫سلحه = بةتح اول وخای نقطه‌داروثانی‬                               ‫بروزن‌مردك»‬     ‫یقح اول و مم‬           ‫=‬    ‫سلمك‬

 ‫‪۴‬‬     ‫دوای‬   ‫است‬   ‫درخعی‬     ‫دوست‬    ‫‪۰‬‬    ‫زسیده‬      ‫سمحتالی‬


‫و سطتر باشد و مانند‬           ‫ان سرخ رن‬              ‫هترین‬   ‫و‬    ‫آن شهناز و کردانیه و کوشت و مابه و نوروز‬
  ‫دارچینی درهمپیجیده بود‪ .‬گر وم خشك استدرسوم‬                                                ‫و لمك باشد ‪.‬‬
                                                                  ‫ت‌ بقتح اول و ثالت و سکون‌تانی»‬                ‫سلمه‬
 ‫سلیس * = بروزن افیس »بمعنی‌سلمیس‬
‫ننوعی از سنگه‬    ‫است که سنگ با باشد و آ‬                           ‫تخم خارست که بدان چرم رادبافت کنندوان‬
                                      ‫‪.‬‬     ‫است متخلاغل‬           ‫مالشدخر نوب‌شامی‌باشد» لیکن اآزن سفیدتراست ‪.‬‬
‫سلیسون = بفتح ابورلوزن‌فر بدون نام‬                                ‫سلنج = یکر اول وضم تاني و سکون‬
 ‫برادر پادثا می‌بوده که| نرافلغراط میگفته اند‪1‬‬                    ‫نون و جیم» مخذف سەلج است می سهلب‪.‬چه‬
                                            ‫‪4‬ھ‬                   ‫را لیز‬   ‫کی‬      ‫و‬    ‫‪-‬‬    ‫للج پمعنی لب هم آمده است‬
 ‫بتحتانی‬      ‫ونی‬
                ‫‪ = ۲‬بفتح اول ا‬                   ‫د‬
 ‫کہ ده و بشن نقطه دار )‪(٤‬‏ زده » بلغت زند‬                         ‫کوبند که لب بالایمن الب زیرین او چاك باشد‪.‬‬
 ‫و پازند (‪ )0‬بمعنی‌بد وزبون باشد که لقیض‌خوب‬
                                                 ‫ونىك ات‬                                                 ‫واو و‬       ‫و سکون‬
 ‫سلیط = بر وزن شربط › بلفت ہونانی‬                                                                         ‫(‪)۱‬؛‬      ‫رای قرشت‬
                               ‫روغن زبتونرا گویند ‪.‬‬                                                       ‫بوعی از ماهی‌باشد‬
 ‫سلیقون ی = بفتح اول و ضم‌قاف‌بروزن‬                                                                      ‫و آن در رود لیل‬
 ‫‪,‬ردون » بلفت روهی‌سر نج را گویند‪,‬وآن‌رنگی‬  ‫ف‬                                      ‫سلور‬                   ‫بهم مفرسد وقارا‬
                    ‫است که نقاشان بکار برند ‪.‬‬                                                    ‫بحربی جری میگوبند ‪.‬‬
‫سلیلث = بروزن شريك ‪ ,‬مخفف بوسليك‬
                    ‫‪ :‬وحا ‪.‬‬    ‫جك‬    ‫(‪)۳‬‬                ‫(‪)۲‬چش ‪:‬نوند ‪.‬‬              ‫(‪ )۱‬چك ‪ -- :‬فرشت ‪.‬‬
                                           ‫‏)‪ (e‬جك ‪ :‬زند وباژند‪.‬‬                 ‫لشطه دار ‪.‬‬      ‫‪-‬‬   ‫‪:‬‬   ‫چك‬   ‫(‪)4‬‬



   ‫(‬    ‫(عر) «سله (بفتح اول ودوم هشدد‬                ‫‪- ۳‬‬         ‫‪( 6۲10115 = ۱‬فر)«لك‪۲‬س ‪. ۰۸۲۰‬‬
     ‫‪ - ۳‬ممال‌سلاح‬               ‫خنور کهطعام‌وجامه وبار دروی هند ‪.‬سلال (بکس)جمه ‪«#‬منتمیالارب*‪.‬‬
     ‫‪٩‬‏ = لانینی‬       ‫‪.‬‬       ‫‪( 61160026 = ۴‬فر) د لك‪ ۲‬ص‪۲۷۲‬‬                           ‫(عر) معتی ابزار جنگ است ‪.‬‬
       ‫‏‪muici( Silicea‬ا‪)iS‬‏ ‪( .‬فر) ‪( 661115‬؛)دزی املاء «سلیی» راباتردید تقل وآنرا (گنایماهی)‬
     ‫‪- ۲‬ازوامق‌وعذرای‬          ‫ترجمه کرده ونوعی‌از (عینون) دانسته‌است*دزیج‪ ۱‬ص‪“٦۳۷‬‏ رك‪:‬سلسىس ‪۰‬‬

     ‫‪- ۷‬هز»‪ , 5112۹‬حا‪ . . .51125‬پهلوی ‪ ۸۵۷۰‬بد «بونکر ‪۱:۱‬؟‪:‬‬                                 ‫عنصر ی ‪ ۰‬رك‪ :‬لت فوس ‪. ۳*۰4‬‬

                                                                           ‫‪ ۸‬برك ‪ :‬سریقون » زرفون‪.‬‬
```


## [2026-09-14T01:23:20.962Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== leaf numbers containing سمندر ===\"; awk 'BEGIN{RS=\"\\f\"} /سمندر/ {print NR}' BQT_v2_pages.txt | head\necho \"=== leaf numbers containing سگزی ===\"; awk 'BEGIN{RS=\"\\f\"} /سگزی|سکزی/ {print NR}' BQT_v2_pages.txt | head\necho \"=== leaf with سگستان ===\"; awk 'BEGIN{RS=\"\\f\"} /سگستان|سجزی/ {print NR}' BQT_v2_pages.txt | head"
}
```


### [2026-09-14T01:23:22.005Z] TOOL RESULT

```
=== leaf numbers containing سمندر ===
196
538
539
631
632
657
=== leaf numbers containing سگزی ===
227
622
623
=== leaf with سگستان ===
623
```


## [2026-09-14T01:23:23.580Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 429 -l 429 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429.png"
}
```


### [2026-09-14T01:23:25.379Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78202 Sep 13 21:23 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429.png
```


## [2026-09-14T01:23:27.367Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429.png"
}
```


### [2026-09-14T01:23:27.890Z] TOOL RESULT

```

```


## [2026-09-14T01:23:27.887Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:23:37.574Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; pdftoppm -f 429 -l 429 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg429hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg429hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.55),int(h*0.12),int(w*0.80),int(h*0.20))).save('$S/pg429-crop1.png')\nim.crop((int(w*0.55),int(h*0.53),int(w*0.80),int(h*0.63))).save('$S/pg429-crop2.png')\nim.crop((int(w*0.45),int(h*0.72),int(w*0.80),int(h*0.80))).save('$S/pg429-crop3.png')\n\""
}
```


### [2026-09-14T01:23:42.580Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-14T01:23:44.762Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429-crop1.png"
}
```


### [2026-09-14T01:23:44.785Z] TOOL RESULT

```

```


## [2026-09-14T01:23:56.576Z] TOOL CALL #21: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:23:56.586Z] TOOL RESULT

```


```


## [2026-09-14T01:24:00.043Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Scythian",
 "prompt": "Give the full etymology section: origin of Latin Scythes/Scytha, Greek Σκύθης, and its relation (or not) to Old Persian Sakā / Old Iranian *Skuda-. Quote exactly."
}
```


## [2026-09-14T01:24:01.989Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%B3%D8%AA%D8%A7%D9%86",
 "prompt": "Give the full etymology of Persian سیستان (Sistān): Middle Persian forms, Sakastān, sound changes. Quote exactly."
}
```


### [2026-09-14T01:24:04.369Z] TOOL RESULT

```
# Etymology Response

The Wiktionary page provided does **not contain** a full etymology section addressing the origins you've requested. 

The only etymological information present states:

> "From *[Scythia](/wiki/Scythia#English "Scythia")* + *[\-an](/wiki/-an#English "-an")*."

This merely explains how the English word "Scythian" was formed by adding the suffix "-an" to "Scythia." It does not trace the origin of Latin *Scytha*, Greek *Σκύθης*, or their relationship to Old Persian *Sakā* or Old Iranian *Skuda-*.

To answer your question fully, you would need to consult sources beyond this Wiktionary entry, such as specialized etymological dictionaries or historical linguistic studies on Indo-European and Iranian language connections.
```


### [2026-09-14T01:24:09.412Z] TOOL RESULT

```
# Etymology of Persian سیستان (Sistān)

Based on the Wiktionary entry, here is the etymological chain:

The word derives from earlier Persian سِجِسْتَان (sijistān), which came from Arabic سَجِسْتَان (sajistān). The Arabic form traced back to Middle Persian "skstʾn" (/⁠sagē̆stān⁠/), which ultimately descended from Old Persian "*Sakastānah."

The entry specifically states: "From earlier _[سِجِسْتَان](/wiki/%D8%B3%D8%AC%D8%B3%D8%AA%D8%A7%D9%86#Persian "سجستان")_ (sijistān), from [Arabic](https://en.wikipedia.org/wiki/Arabic "w:Arabic") _[سَجِسْتَان](/wiki/%D8%B3%D8%AC%D8%B3%D8%AA%D8%A7%D9%86#Arabic "سجستان")_ (sajistān), from [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[𐭮𐭪𐭮𐭲𐭠𐭭](/w/index.php?title=%F0%90%AD%AE%F0%90%AD%AA%F0%90%AD%AE%F0%90%AD%B2%F0%90%AD%A0%F0%90%AD%AD&action=edit&redlink=1 "𐭮𐭪𐭮𐭲𐭠𐭭 (page does not exist)")_ (skstʾn /⁠sagē̆stān⁠/), from [Old Persian](https://en.wikipedia.org/wiki/Old_Persian "w:Old Persian") _[\*Sakastānah](/w/index.php?title=Reconstruction:Old_Persian/Sakast%C4%81nah&action=edit&redlink=1 "Reconstruction:Old Persian/Sakastānah (page does not exist)")_."

The word is cognate with Latin *Segestan* and *Sacastene*, reflecting the ancient Sakastān region.
```


## [2026-09-14T01:24:15.028Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%A3%CE%BA%CF%8D%CE%B8%CE%B7%CF%82",
 "prompt": "Give the full Ancient Greek etymology of Σκύθης: proposed origin (Iranian *skuda- 'archer'?), relation to Assyrian Aškuza, and whether it is connected to Old Persian Sakā. Quote exactly."
}
```


## [2026-09-14T01:24:16.205Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Scythian",
 "prompt": "Full etymonline entry for Scythian and Scythia: Greek Skythes, origin, any mention of Saka. Quote exactly."
}
```


### [2026-09-14T01:24:19.817Z] TOOL RESULT

```
# Ancient Greek Etymology of Σκύθης

Based on the Wiktionary entry provided, the etymology section states:

"Borrowed from Proto-Scythian *Skuδi. Cognate with Akkadian 𒆳𒅖𒆪𒍝𒀀𒀀 (Iškuzāya)."

The document does not propose an Iranian origin (*skuda- 'archer'), nor does it discuss connections to Old Persian Sakā. It only identifies the word as borrowed from Proto-Scythian and notes its cognacy with the Akkadian term Iškuzāya, without elaborating on broader Indo-European etymological connections.
```


### [2026-09-14T01:24:20.314Z] TOOL RESULT

```
# Scythian Etymology

Based on the etymonline entry, here's what's stated about the Greek origin:

**Greek Origin:**
The term derives from Greek *Skythia*, with the root being *Skythes* meaning "a Scythian." According to the source: "said to be from an Indo-European root meaning 'shepherd'" [Room].

The entry notes that this referred to "the region along the north coast of the Black Sea and extending indefinitely north."

**Important Note:**
The provided etymonline entry makes **no mention of "Saka"** anywhere in the text. The entry does not connect the Scythian etymology to Saka origins or terminology.
```


## [2026-09-14T01:24:29.867Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Saka",
 "prompt": "Etymology of Saka (the Iranian people): Old Persian Sakā, Proto-Iranian form, meaning, and relation to Scythian. Quote exactly."
}
```


## [2026-09-14T01:24:31.562Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DA%AF%D8%B2%DB%8C",
 "prompt": "Etymology of Persian سگزی (sagzi): Middle Persian form, relation to Sakastan/Sistan. Quote exactly. Also any Arabic form سجزی."
}
```


### [2026-09-14T01:24:33.044Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:24:34.446Z] TOOL RESULT

```
# Etymology of Saka (Iranian People)

Based on the Wiktionary entry, here is the etymological information:

**Old Persian Origin:**
The term comes from Old Persian "𐎿𐎣𐎠" (s-k-a /⁠Sakā⁠/, "Scythian"), which derives from "𐎿𐎣" (s-k /⁠Saka⁠/, "Scythia"), ultimately tracing back to Scythian languages.

**Direct Quote:**
The entry states: "from Old Persian _𐎿𐎣𐎠_ (s-k-a /⁠Sakā⁠/, 'Scythian'), from _𐎿𐎣_ (s-k /⁠Saka⁠/, 'Scythia'), from Scythian."

**Relationship to Scythian:**
The Wiktionary source indicates the word is ultimately derived from Scythian languages, with the Old Persian form serving as an intermediary in the etymological chain that eventually reached Sanskrit and subsequently English through learned borrowing.
```


## [2026-09-14T01:24:38.721Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/teak",
 "prompt": "Full etymology of English teak: Portuguese teca, Malayalam, Sanskrit śāka, and any mention of Arabic sāj. Quote exactly."
}
```


## [2026-09-14T01:24:40.260Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%AC",
 "prompt": "Give the Arabic entry ساج (sāj) 'teak': etymology (from Persian? from Sanskrit śāka?), and the Persian entry ساج if present. Quote exactly."
}
```


### [2026-09-14T01:24:43.007Z] TOOL RESULT

```
# Etymology of English "Teak"

Based on the Wiktionary entry, here's the documented etymology:

**Direct Etymology Chain:**
"Derived from Portuguese _teca_, from Malayalam _തേക്ക്_ (tēkkŭ) / Tamil _தேக்கு_ (tēkku)."

The entry traces the word through Portuguese as an intermediary language, ultimately sourcing it from South Indian languages. However, the document does not mention Sanskrit śāka or provide Arabic sāj in the etymology section for English teak—though Arabic سَاج (sāj) does appear in the translation tables as the Arabic term for the timber itself.

No Sanskrit connection is explicitly stated in the etymology provided.
```


### [2026-09-14T01:24:45.254Z] TOOL RESULT

```
# Arabic and Persian ساج (sāj)

## Arabic Entry Etymology

The Arabic term ساج (sāj) meaning 'teak' derives from Sanskrit. According to the etymological note: "Ultimately from Sanskrit शाक (śāka, 'vegetable; herb; teak-tree')." The entry also notes comparative forms in Aramaic and Persian before tracing the ultimate source to Sanskrit.

## Persian Entry

The Persian dictionary includes two separate etymologies for ساج (sâj):

**Etymology 1** (teak meaning): "Ultimately from Sanskrit शाक (śāka, 'vegetable; herb; teak-tree')."

**Etymology 2** (griddle meaning): Described as "A Turkic borrowing, see Turkish sac / ساج." This noun refers to a cooking griddle and has Turkic rather than Sanskrit origins.

The Persian entry thus documents that the same word form carries two distinct etymological paths and meanings depending on context.
```


## [2026-09-14T01:24:48.221Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/salamander",
 "prompt": "Full etymology of English salamander: Middle English, Old French salamandre, Latin salamandra, Greek σαλαμάνδρα, and any statement about the ultimate (Persian/Anatolian/Pre-Greek) origin. Quote exactly."
}
```


## [2026-09-14T01:24:50.040Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%85%D9%86%D8%AF%D8%B1",
 "prompt": "Give the Persian entry سمندر (samandar): etymology — is it from Greek salamandra, or from sām/samm + andar, or native? Quote exactly. Also any Arabic entry سمندل/سمندر."
}
```


### [2026-09-14T01:24:52.257Z] TOOL RESULT

```
# Etymology of "Salamander"

**Full etymological chain:**

The English word traces back through Middle English *salamandre*, from Anglo-Norman *salamandre*, from Latin *salamandra*, from Ancient Greek *σαλαμάνδρα* (salamándra).

**On ultimate origins:**

According to the source: "of uncertain origin (per Beekes, likely Pre-Greek); possibly of Iranian origin, see Persian سمندر (samandar) for more information."

The entry acknowledges the word's origin remains uncertain, with scholarly consensus suggesting a Pre-Greek substrate source, though Persian *samandar* is noted as a possible parallel worthy of investigation.
```


### [2026-09-14T01:24:56.068Z] TOOL RESULT

```
# Persian Etymology of سمندر (samandar)

The etymology is **disputed**. According to the Wiktionary entry:

**Traditional Persian view:** Most Persian dictionaries considered it a compound of "sām" (fire) + "andar" (inside), suggesting a mythological creature living in fire.

**Dehkhoda's alternative view:** The lexicographer Dehkhoda "rejects this derivation and contends that it is folk etymology, as سمندر (samandar) is most likely from Ancient Greek σαλαμάνδρα (salamándra)."

However, the entry notes: "The origin of the Greek term is uncertain, however, so there remains a small possibility that it may itself be from Persian."

**No Arabic entries** for سمندل or سمندر appear in this Wiktionary page—only entries for Pashto, Persian, Urdu, and Ushojo are documented.
```


## [2026-09-14T01:25:02.241Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84%DB%8C",
 "prompt": "Persian شالی (šāli) 'rice in the husk': etymology — from Sanskrit शालि (śāli)? Quote exactly. Also any mention of شالیزار."
}
```


## [2026-09-14T01:25:04.051Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D9%84%D8%AA%D9%88%DA%A9",
 "prompt": "Persian شلتوک (šaltuk) 'rice in husk': etymology. Is it linked to شالی or to Turkish çeltik? Quote exactly."
}
```


### [2026-09-14T01:25:05.591Z] TOOL RESULT

```
# شالی (Persian: Rice-Related Term)

**Etymology:** The word is "Borrowed from Sanskrit _शालि_ (śāli, "rice")."

**Definition:** شالی (šâli) means:
1. Rice-hull or rice-husk
2. Rice still in the husk

**Related Term:** The document mentions شالیزار (šâlizâr) as a derived term, though it doesn't provide its definition on this page.
```


### [2026-09-14T01:25:08.263Z] TOOL RESULT

```
# Etymology of شلتوک (šaltôk)

According to the Wiktionary entry, the word is linked to Persian origins. The etymology states:

"From _[شالی](/wiki/%D8%B4%D8%A7%D9%84%DB%8C#Persian "شالی")_ (šâli), same, + _[توک](/wiki/%D8%AA%D9%88%DA%A9#Persian "توک")_ (tôk, "bundle, fagot; handle, grip")."

Regarding Turkish çeltik, the entry shows it as a descendant language form rather than an etymological source. The word passed from Persian through Ottoman Turkish and subsequently into modern Turkish, rather than originating from Turkish.
```


## [2026-09-14T01:25:19.301Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sagzi/sistan/sagestan ===\"; grep -n -i \"Sagzī\\|Sagzi\\|Sagistān\\|Sagastān\\|Sīstān\\|Sîstân\\|Sistan\" HRN.txt | head -10\necho \"=== HUB sistan/saka ===\"; grep -n -i \"Sistan\\|Sīstān\\|Sakastan\\|Saka\\b\" HUB.txt | head -10\necho \"=== PHD sagestan/sagzi ===\"; grep -n -i \"sag\\|Sakastan\" PHD.txt | head -20"
}
```


### [2026-09-14T01:25:19.388Z] TOOL RESULT

```
=== HRN sagzi/sistan/sagestan ===
7988:Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
=== HUB sistan/saka ===
653:assistance, cooperation' Gl. and Ind. p. 9 = paz. awdgl
829:-~ skr. vatsd' *KaIb' (vgl. skr. vatsaka- 'Kalbchen')
1175:'prevailing, resistant' (Shk. 262), also eigentlich *wider-
1575:*sak'Cik von ap. Saka-) gehort selbstverstandlich nicht
1760:sapor, dasldan 'kosten', skr. daSaka- *Becher (aus
2521:lautlichen Differenz zwischen zd. dusaka- und np. ^£a
2523:g. jUjflk (ZDM6. 36, 63) andrerseits. Zd. dusaka- ist
2667:^saka- = np. sag *Hund') angehoren.
4485:Sistan aus ^Sigistan = arab. Sijistan^ gr. SsyeOvavdjiv s&vog
4678:vand *kraftig* = paz. padyavand resistant' Shk. 262 (oben— 134 -
=== PHD sagestan/sagzi ===
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
505:P naxsag [nhšk! | P nxšg] good, fine.
510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
558:résag 72 rózig
562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
```


## [2026-09-14T01:25:21.778Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT teak ===\"; grep -n -i -m3 \"teak\" SKT.txt | head -5\necho \"=== SKT salamander ===\"; grep -n -i -m3 \"salamander\" SKT.txt | head -5\necho \"=== AID teak/sagwan ===\"; grep -n -i \"teak\\|sagwan\\|sagun\" AID.txt | head -10\necho \"=== FSD vol4 salamander/teak? ===\"; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"-- $f\"; grep -n -i -m3 \"salamandra\\|salamander\" $f | head -3; done"
}
```


### [2026-09-14T01:25:22.828Z] TOOL RESULT

```
=== SKT teak ===
18444:atith,    an  an\i.     .,.v.4>.w        .'.<.  ^. —  Icel.  stt^i,  an  anvil;    allied  to  iMl Axed  place;    n.tmei   from    its   firwiOll Swed.  i/tih/,   an  anvil.     Dor.  statA^t  | {^>crly  a  smithy,  also  au  anviL Steak ;  see  SUok  ( 1 ). SteoL  I.E.)     A.  a  Jte/am,  pi  t.  tttL sioien.  +  Da.  steten,  Iccl,  r.V/tf,  Daft,  m S»ed  j{r<ii/<is.  G.  siekttn,  ^'Oth  ^/aj'jn. Gk.  47WXX<ii',  to  put  flwav.
18505:steak,   a    slice  of  ment (Scaud,)     M.  E.   sif- ■    -   '  -■ steak ;    so  called   fi wooden  peg,  nttd  t(>.t IceL  stfikja,   to   roa^l,  on    a Allied  to  Icel.  stika^  a  stick; (1).  ^  Swed.  slek,  roan  mi roftst;   allied  to  cruk^  a  pri< Slick,  stab;    Oan    f/rjf,  a  ri
19249:Teak,  a  tree.  (Malayalam.)  Malayalam fi/Ha,  the  teak  tree :  Tamil  fMAu,  the  same (H.H.Wilson).
=== SKT salamander ===
16398:Salamander,  a  reptile.  (F.-L.-Gk.) F.  salamandrt.  —  L.  salamandra.  —  Gk. txtxXsx^nvhpa,  a  kind  of  lizard.  Of  Eastern origin;  cf.  Pen.  tamatuiar,  a  Balanuin- der.
=== AID teak/sagwan ===
848:BAnkot  Knees.  Curved  teak  logs from  Bdnkot,  highly  prized  for  ship- building.
4143:in  the  bows,  with  hollow  keel,  well rounded  in  the  stern,  and  the  mast slopes  a   little  forward  ;   these  vessels are  chiefly  made  of  teak,  and  cost from  Rs.  300  to  Rs.  400 ;   they  last about  forty  years.
5933:Sdg.  [Mardthi,  from  the  Sanskrit fdka!\  The  tree  tectoffa  grandis,  or teak.
6429:fiiwan.  [Hindi.]  A   large  and  beauti- ful tree  of  the  teak  family,  the  gme- ;   iina  arborea.  It  sheds  its  leaves  in
6763:Tasar.  [Hindi,  from  the  Sanskrit trasara.]  The  name  of  a   silk,  the product  of  the  larvae  of  the  moth antheraea  paphia,  found  over  nearly the  whole  of  India.  The  caterpillars are  about  four  inches  long,  green, with  reddish  spots  and  a   reddish- yellow  band  running  lengthways. They  feed  on  several  plants,  in- cluding the  teak,  the  baer,  the  sdl,
=== FSD vol4 salamander/teak? ===
-- FSD_vol1.txt
13595:Am"by-stom'I-dze,  1   am'bv-stom'i-dl;  2   5m’by-st6m'i-d6,  n. pi.  Herp.  A   family  of  salamanders  with  vomero-palatine teeth  convergent  backward  meslally,  and  the  vertebral  con- vexo-concave. Am"by-sto'ma,  n.  (t.  g.)  Am"by-st<j- mat'l-dmt.  — nm'by-stome,  n.—  am-bys'to-mld,  n.— am-bys'to-mold,  a.
15234:with  two  occipital  condyles  and  a   parasphenoid.  It  Am-phlb'ry-a,  n.  pi.  Bot.  The  Monocoigledones. —   am- includes  frog-like  animals,' salamanders,  and  many  extinct  pblb'ry-o us,  c.  Bot.  1.  Growing  by  additions  to  all  parts  Am”phlg-n3th'*o-don>tl-d3e,  1   am'fig-nath'o-derin-dl;  2 forms.  (2)t  A   including  reptiles,  true  amphibians.  of  the  periphery.  2.  Of  or  pertaining  to  the  Amphihrya.—  am'fig-nath'o-dSriti-de,  n.  pi.  Herp.  A   family  of  ar-
15306:2.  la-)  A   salamander  of  this genus.—  Am"phl-u'ml-dtc,  n. pi.  Herp.  A   family  of  aala- mandroid  amphibians  with  per- sistent gills  and  without  eye- lids, Including  the  Congo-snake  j of  the  southern  United  States.
-- FSD_vol2.txt
20642:an  enemy’s  fiWp  or  fleet.— r. (raising,  n.  [Scot.]  A   setting ■on  lire;  araon.— f,«re(i5  a.  I'UhI  (us  lire.—  f.srcrt,  n.  [Krlt. (iuiana.l  The  pigmy  seecKiater  (.SporopMla  minuta),  a small  Mlllant  Iringllllne  song-bird  ol  brushy  places.— f.« reel,  n.  A   reel  or  .spool  on  which  a   flnvhose  in  colled;  either detached  or  mounted  on  a   cart.— f.  (regulator,  n.  An automatIn  device  lor  controUlns  coinlmstlon,  as  In  a   ateaiu- heating  apparatus,  by  opening  or  closing  a   damper  or  a llre-door,  according  to  the  prc's.sure  of  the  st(>am  or  the tenipcraturo  ol  the  heated  air.—  f.  srisk,  n.  1.  The  posslhlo loss  of  property  by  lire.  2.  Tlie  risk  Iiuhirrcd  by  a   lire- lasuriitice  oornpaiiy  In  the  raise  ol  each  policy.  3.  A   plceo ol  property  insured  agalnat  lire.— f.  (roll,  n.  AhMil.  The roll  ol  a   drum,  or,  in  tho  United  .States  navy,  the  rapid ringing  of  the  sUiii’s  boll,  ordering  men  to  llre'iiuarterH.-- (.•room,  «.  Tim  boiUsr'rooui  (in  a   stmanslilp,  wbero  tbti llring  of  tbc  furnneo  is  done,;  Htolimhole.-- f.»,salaiiiajider, K.  The  common  spotted  salamander  (Saln7nar»lm  imiailosa) of  lOuropc;  in  allusion  to  an  ancient  fable.— f.  (.saw,  ii.  A thin  .strip  of  wood  or  bamboo  drawn  rapidly,  saw'fiisUlon, across  a   concave  block  of  the  same  material,  lor  producing lire  by  friction.  The  spark  appoans  beneath.—  f.fscreen, «.  1.  Any  screen  used  to  protect  Irom  the  heat  of  a   fire, or  froni  flying  .spark.s.  3.  A   llrC'guard  of  baize  or  ihiiuicl in  the  passageway  from  an  open  powder-magazine.—  f.»set, «,  A   sot  of  ilre-tools,  conalatlng  ol  shovel,  poker,  and  tongs, with  tho  holder.— f. (Setting,  n.  A   former  method  of cracking  a   worklng-fac.e  in  a   mine  by  building  a   lire  against it  ami  then  rapidly  cooling  wltli  cold  water.— f.  (Shield,  n. A   flre»guard  of  sheet  metal  or  asbestos,  to  protect  workmen at  a   luruaco  or  firemen  at  a   fire  from  the  Intense  heat.—  f.» ship,  n.  A   Hlilp  mied  wltli  combu.sttbles,  fired  and  floated toward  an  enemy  for  the  purpose  of  destroying  .ships, bridges,  etc.—  f.»shovel,  n.  A   sliovel  used  In  the  uiaiiage- inent  of  a   fire.— f, (silvering,  p..  TIatirig  with  silver  by applying  silver  amalgam  or  a   mixture  eoiitaliiliig  finely  re- duced stiver,  and,  In  elllior  ease,  fixing  the  .silver  by  iKoiting, as  la  a   imutle.~-f.»sla.sh,  ?i.  A   gap  in  a   forest  (mused  by lire. -- f.  (Spirit,  n.  Tiro  persimillod  iis  a   spirit.- ■   f.{.sp«<, rt.  Archrul.  A   liiiWNshajnul  fireplace  in  tlie  ground  eori- talning  iwhes,  calcined  boiic.s,  etc.,  commim  in  .‘^candlnavlau cmmtrles:  somcfiuies  suppo.sed  to  lie  a   vestige  of  fuiierai pyres.  ■r.(spots,  «.  jH.  k'IiUHe.»colorc(l  fipecks  In  the  Iris of  tlie  eye.--  I. (Steel,  w.  A   piece  ol  steel  to  use  with  ii  flint In  striking  fire.  •   f.*stlck,  n.  1.  A   firehrand  or  lighted stick;  a   burning  piece  of  wood.  2.  Any  form  of  liard  dry stick  used  to  obtain  lire  by  frlcUiin,  as  a   llredlrlH.--  f.<Ktlnk, n.  Tho  odor  evolved  by  decompo.slrig  Iron  pyrites.— f.« stone,  n.  1.  Flint  or  pyrites  used  for  .striking  Are.  2.  A atone  that  will  wlilistand  the  action  of  fire.  3.  A   composi- tion of  niter,  sulfur,  re.sln,  ete.,  used  for  eburglng  Incendiary Bhoils.  4.  Mvinl.  .-All  Iron  plate  covering  the  fiiniaccfrout of  a   alagdiearth  lo  wltliin  a   few  liiclie.s  of  the  bedplate.--  f.( 8top,n.  1,  Aflrc«lnidgo,  3.  Any  Incombustlbhi  material used  to  fill  In  open  parts  of  a   tniUdliig  in  order  to  prevent the  passage  of  fire.  -   f. (.surface,  n.  'I'liat  part  of  the  .stir- laco  of  a   boiler  which  Is  expoaetl  to  the  fire;  the  beiitlng* surface,—  r.(swah,  n.  A   swab  of  rope-yarn,  imilBtetK'd  and inaorted  ih  a   emmcin  to  remove  or  put  out  any  glowing particles, —   f.».syrlng«,  «.  A   phlhmoplileal  toy  consisting of  a   clOHfid  cylinder  In  which  tinder  may  be  ignited  by  tho compression  of  air  caused  by  suddenly  forcing  In  a   piston. A   similar  instrument  was  formerly  tmed  practically  by  tho Polynesians,  -   llrc'tall",  n.  1.  Tho  redstart.  2.  A   cuek- oo-fiy,  or  chryatdld  hymenoptor,— f.dttikHl,  a.  Havhig a   tall  In  color  suggeatlng  lire.  Sco  comet.— f.  (teaser,  n. [Slang,  Kng.]  A   stokor.— f.  (telegraph,  «,  1.  A   tele- graphic flro«aIarm  system.  2.  A   system  of  liua(!on*fire.s  for transmitting  latelllgoneo.--  f.dlle,  n.  A   tile,  used  In  a   fur- nace, which  Is  unalleclied  hy  great  heat.— f.  (tongs,  n. Tongs  for  use  ahout  u   fireplace.— Mre'top",  n.  Same  aa FiKBWBKi).—  f. (tower,  »■  1*  A   beacon  or  llglithouse,  2. A   wateh'towor  trow  which  a   eowflagratlon  can  be  seen and  an  alarm  given.— f,  (trace,  »,  Same  as  FiuEdiiiKAK. —   f.(trap,  n.  A   bulUllnK  notoriously  IntlainraaWe,  or  ono not  provided  with  an  escape  for  use  In  case  of  fire,—  f.  "tree, n,  Boi,  Any  one  of  various  trees,  so  eallcd  from  their  fire* like  appearance  when  In  llow'ov,  espeelaUy  the  pohutukawa {Meirosiie.Tost  tomenttm),  of  tho  myrtle  family  of  New  flea- land,  and  the  Australian  ilanien.ree.  iNvvtsla  /lorihimda), of  the  mistletoe  family,  or  the  tiueonsland  tullp^treo, ~   r.  (tube,  rt.  In  steani*))oIIers,  a   tube,  usually  one  of  many, tor  the  passage  of  combustlon'gasos;  a   flue,— f.(Walk,  n. 1.  A   medieval  ordeal  In  wlileli  a   suspected  person  walked through  Are.  2.  A   (lunsl-rellgious  ceremony  in  which devotees  walk  barefooted  on  rod«hot  stO!ie.s  or  cluireoal,  a custom  now  practically  extinet  In  Polynesia,  but  still  pre- vailing In  India.  Tho  flre*walkers  usually  pass  through  the ■ordeal  nnsc.athed.  Tho  rite  Is  performed  by  the  Dosiulhs at  the  annual  worship  of  their  god  Iliilui,  who  Is  believed  to cause  eclipses.  In  northern  India  Hindus  walk  through the  HoU  lire  and  Mohammedans  over  the  Are  In  honor  of Saint  Madar.  flre,walklngl:.-f.(waH,  «.  A   thick  wall to  cheek  fire.—  f.'warden,  «.  An  ofllcer  who  has  charge ol  the  prevention  and  extinguishing  of  fires.  f.(Wardt. -.r.(Watcr,  n.  [IT,  S.]  Whisky;  a   term  first  Used  by or  attributed  to  tho  North^Anierlcan  Indians.— f. "Well, «,  A   spring  of  inflamraable  gas.— f.(W'o(»d,  ».  Wood used,  or  fit  to  use,  as  fuel.— f.(werUert,  n.  An officer  of  artillery.— f. (Worm,  n.  1,  A   glowworm.  2, The  larva  of  a   lortrleid  moth,  which  devours  the  leaves  of the  cranberry,  leaving  It  apparently  burned.— forest  f., a   conflagration  caused  In  heavily  wooded  land,  as  by .sparks  from  locomotives,  etc.;  frc<iuent  in  the  United States  In  March,  April,  and  May,  or  In  the  summer,  after long  periods  of  drought.  They  are  classified  as  (1)  surface or  ground  llres,  a   burning  of  the  Utter  of  solPcoverlng, leaves,  grass,  etc.;  (2)  crown  flre.s,  attacking  the  foliage and  upper  brancluw;  (3)  stem  fires,  unimportant  examples occurring  in  Isolated  hollow  trees;  and  (4)  deep  soUdlres, the  comparatively  rare  ares  occurring  In  peaty  moorlands. Which  can  only  bo  stopped  by  digging  trenches  down  to, the mineral  soli.—  Oreck  f.,  an  Incendiary  composition  n.yed by  the  Byzantine  Greeks;  aum'iosed  to  have  been 'made -of  asphalt,  Saltpeter,  and  sulfur.  It  would  burn  on  and under  tho  water.- -high (angle  f.  (Afil.i,  discharge  at  a height  or  angle  of  more  than  30“.-  hollow  f.,  a   furnace nsed  in  tln*platc  manufacture  for  licaiing  Iron  and  preserv- ing It  from  contamination  by  fuel  and  sulfur,— holy  f, (ir.  0.  Ch.),  a   fiint«madt!  fire  kindled  on  Holy  .Saturday,  and used  to  relight  the  church  lights  (incnelmd  on  Good  Friday. —   horizontal  f,,  artlUcry  fire,  delivered  with  little  or  no elevation.— letters  of  f.  and  sword  (Old  Bcots  Aaiv), Icsttcrs  from  tho  Privy  Cimncil  by  which  the  sliorlfl  could invoke  the  assistance  of  the  county  In  ejecting  a   tenant, —•liciuhl  f.,  a   flaming  liriiild.  as  oil  accompanied  by  douse smoke  elected  through  a   nozzled  apparatus  borne  on  the back  of  a   flame«thrower  (Ger.  flammenwerfer) ;   used  by  the German  army  during  ihe  Great  War  (iai4-l8).-  marsh* f.,  n.  The  ignis  fatuus.—  on  1'.,  burning;  ablaze  (literally or  flguratlvely).  — open  f.  1.  An  expo.sed  forgC'flre  as distinguished  from  one  that  Is  coped  over;  made  In  tho  cen- tral hollow  of  the  earth  of  a   forgo,  with  tuyfire  commonly
31448:Cenlury  Magazine  Out.,  181*1,  p.  953. 3.  Hence,  to  garble  and  misconstrue,  ns  the  premi.se8  in tin  argument,  'so  as  to  arrive  at  a   forced  conclusion;  as, he  gerrymandered  the  question.  3.  [Rare.]  To  dhdtle into  crooked  or  tortuous  parcels,  as  a   district  or  region. [<  Gov.  Elbrtdge  Gerry,  the  supposed  inventor  of  gerry- mandering. -f  -mnmier  In  s.ALAMANnER  (the  .shape  of  one ot  the  districts  In  Massachusctt.s,  formed  while  Gerry  'was governor,  being  thought  to  resemble  a   salamander)  .j  —   ger"- ry-man'der-er,  n.
34934:Gra"dl-en 'ti-a,  1   grS'da-en'Shi-e;  g   gra'dI-Sn'sW-a,  ».  pi. Merji.  An  order  of  amphibians  or  reptllea  with  a   lacertlform body,  e.speoiaIly  the  urodele  amphibians,  as  salamanders. [<  L.  srailietni-'js ;   see  gba.dibnt.1 gra'din,  1   gre'din  or  (,F.)  gro'dan';  2   gra'din  or  (F.) gril'dSn',  n.  1.  One  of  a   aeries  of  rising  seats  or  steps, as  in  an  amphitheater.
-- FSD_vol3.txt
29778:aquatic American salamander-like amphibian of ttie genus
53388:luo'roDi, 1 mOjjcen. 2 mO'rOo, n. (I* .1 A klud of salamander,
161594:Nerp A family of salamanders with vertebi m oplsthocodous, “
-- FSD_vol4.txt
1059:Megalobatrachus  ja-  Spotted  Salamander  Vi
1060:Blant  s.  of  Japan,  which  attains  a   length  of or  more  The  salamanders  were  formerly  fabled to  llie  In  ani  extinqu'sh  Are  muieu
1064:passedover  and  near  their  surfaces  (2)  A   metal  drum  or hot  coals,  etc  ,   used  in  drying  plaster b'  rcolloo rennon.  a   loggerhead, term  He.  ^   fire'Pre°f  onginally  a   trade ^   four-footed  beast  represented  pas- sant, breathing  or  surrounded  by  fiames  7.  Alelal metal  or  siag  remaining  m   the /orewoo  “ftor  the  fires  are  drawn  [   <   r   sata- ”p  Pe?’s™an5arT“"*“'  "‘■'amohdre,  salamander.
```


## [2026-09-14T01:25:35.852Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 1570-1580 ===\"; sed -n '1570,1580p' HUB.txt\necho \"=== HUB 4480-4492 ===\"; sed -n '4480,4492p' HUB.txt\necho \"=== HRN sag/sagzi search 2 ===\"; grep -n \"Sagzi\\|sagzî\\|Segzi\\|Sigistan\\|Sijistan\\|Sedschestan\" HRN.txt | head"
}
```


### [2026-09-14T01:25:35.931Z] TOOL RESULT

```
=== HUB 1570-1580 ===
Laufe?)
367. de Lagarde's falsche Ansicht brauchte nicht wieder-
holt zu werden. Np. taz^'^) 'arabisch* -^ arm. tadik =
phi. ta&ik^) (gebildet von Tai wie np. razi von Raij
np. sagzi 'Sake' = arm. sagcik ^= phi. *8agdtk fiir
*sak'Cik von ap. Saka-) gehort selbstverstandlich nicht
zu np. taj 'Krone' (arabisiert aus *tag) = syr. tdya,
arm. fag 'Krone', die ein ap. *taga- voraussetzen.
Dazu kurd. tanjf 'Krone', Socin, Samml. II, 292.
Die Verbindung von taziyana Teitsche mit taxtan
(WZKM. 8, 93) schon bei Vu 1 1 e r s , vgl. taziyan 'laufend,
=== HUB 4480-4492 ===
giriftan *nehmen siehe Kap. 7. Kein lautlicher Grund ist
ersichtlich fiir den Uebergang von a zu i in np. diham 'icli
gebe' etc. = paz. dahom, zd. dadqmi, ap. *'daddmiy 3. ipf.
adada), zu dem np. dihis 'Gehen = np. dasan *Gabe, Geschenk'
(Horn Nr. 528) aus paz. dahisn gehort. Ebensowenig bei
Sistan aus ^Sigistan = arab. Sijistan^ gr. SsyeOvavdjiv s&vog
(A gat bias), lat. Segestani (Am mi an), arm. Sagastan^
gr. ^juxaavarrj (Isidor Char.). Im modernen Np. ist auch
das a der Prap. ba (= paz. pa) zu i geworden JRAS.
1894, 444.— 129 —
b) Durch Assimilation an vorangehendes oder folgen-
des i:
bihist = bahist Paradies', zd. vahiSta- *beste' (sc. ahu-
=== HRN sag/sagzi search 2 ===
```


## [2026-09-14T01:25:37.275Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD vol4 head ===\"; sed -n '1050,1070p' FSD_vol4.txt\necho; echo \"=== FSD vol4 page nums near ===\"; sed -n '1000,1060p' FSD_vol4.txt | grep -o \"2[0-9][0-9][0-9]\" | head -20"
}
```


### [2026-09-14T01:25:37.388Z] TOOL RESULT

```
=== FSD vol4 head ===
Sa'kaP,  1   Ba'kol.  2   sa'kf,  n   One  of  a   primitive,  probably aboriginal  race  In  the  Malay  Peninsula,  lighter  than  the Malays,  and  Inferior  to  them  in  culture Sa'Ka-1*,  1   sa'ka-l,  2   sa'ka-i,  n   Same  as  MikdaVI Sa"ka-rl'yah,  1   saTa-ri'ya.  2 Asia  Minor,  length.  230  m   to the  Black  Sea  Sa"ka-rl'at Sa-ka'ta,  1   sa-ka'ta  2   sa-ka'ta, n   A   seaport  at  the  mouth  of the  Mogaml  river,  N.  W Honshu  Island,  Japan ija"ka-ta'ya-na,  1   sd'ka-to'ya-na,  2 sa'ka-ta'ya-na,  n   An  ancient  San- skrit grammarian,  known  only  by his  writings  ^
sakes  1   8ek,  2   sak,  n   1.  Pur- pose of  obtaining  or  accomplish- ing with /or  and  the  name  of  the thing  to  be  done  or  obtained  pre- ceded bj  of  now  rarely  with  a possessive ,   as,  to  open  the  wnndow for  the  sake  of  air,  for  honoris sake  2.  Interest  or  regard  felt for  any  person  or  thing,  account commonly  with  for  and  a   posses- sive, less  often  With  of,  as  in  def  1
sal  abslnthll,  an  Impure  potassium  carbonate obtained  from  the  ashes  of  wormwood  — sal  acetosella, the  acid  oxalate  of  potassium  —   sal  aeratus,  same  as  sao* eratus  —   sal  alembroth,  a   combination  of  mercuric  chlo- rld  and  ammonium  cblorld  salt  of  wlsdomt.— sal amarum,  magnesium  sulfate.  Epsom  salts  sal  cathar- tlcust  —   sal  ammoniac  {Mineral ),  a   white,  vitreous,  solu- ble ammonium  chlorld  (NH«C1),  crystallizing  in  the  Iso- metric system  —   sal  cullnarlus,  table  or  common  salt  — sal  Cyrenalcus,  same  as  sal  ammomac  —   sal  de  duobus, potassium  sulfate  sal  dupllcatust.— sal  dlurctlcus, potassium  acetate  — sal  enlxum,  hydrogen  potassium  sul- fate or  potassium  btsulfate  —   sal  gcramte,  rock  salt  —   sal Jovls,  stannic  chlorld  salt  of  tint,— sal  Martls,  Iron sulfate  copperas  green  vitriol  — sa!  rolcrocosmlcura, aramonlum-^odlutn  phosphate,  used  as  a   flux  In  blowpipe anily  sis  -   sal  rairablle,  sodium  sulfate  Glauber’s  saitt. —   sal  plumbl,  same  as  sugar  of  lead —   sal  prunella, same  as  prunella*  —   sal  SaturnI,  sugar  of  lead  —   sal sedativusy  boric  acid  sal  sedatlvus  Hombergllt.— sal sclgnette,  see  under  Seidlitz  powder  —   sal  soda,  sodium carbonate  washing-soda  —   sal  tartre,  potassium  carbonate, purified  pearlash  salt  of  tartart  —   sal  Tltrloll.  zinc  sul- fate —   sal  TOlatlie,  ammonium  carbonate  volatile  saitt. sal ,   1   sal  or  sel,  2   sal  or  sal  n   (E  Ind  )   A   very  large  tree {Shorea  robusta)  growing  m   India  It  yields  a   dark-brown, cross-grained  heart*wood,  that  Is  hard,  heavy,  strong,  and tough,  and  highly  prized  for  building  purposes  A   palo aromatic  oammar-Ilke  resin,  called  dammar  and  saLdam- xnar.  Is  obtained  from  the  tree,  and  the  Tussar  silkworm feeds  on  its  leaves  sal'*tree"t.
Sal*,  1   sal,  2   sal.  n   1.  An  island  of  the  Cape  Verde  group, 20  by  9   m   2.  A   river  In  S   European  Russia,  length,  400 m   to  the  Don  river
sa'lab  1   su'lo,  2   sa'la- n   Dt,Sp,&Portl  A   large  room, especially,  a   dlnlog-room  or  drawing-room Sa'la",  1   s€'ls  2   sa'la,  n   I   George  Augustus  Henry (» /nl828-*V 81895),  an  EngUah  essayist  and  Journalist Btb  Lute  hi,  35
in  the  nlu-  sa-laam',  1   sa-lam'.  2   sa-Iam ,   vt  &   vl  To  greet  with often  in  tne  piu  ^   salaam  -sa-Iaam'lng,  n
oivc,ic»3  oivcu  0.3  OP  maKC  o   saiaaui  —   ^a-•uallI  lufe,  »   ^   —   saia-inan-arorue-an,  a   #3
ral  when  with  a   possessive  plural,  as,  for  your  saKe  n   An  Onental  salutation  or  obeisance  uer-  mat,  1   sa-lo'mat.  2   sa-Ia'mat  interi  rp  n
r   ^   *0  c4lTa*c  wnOn.  fnr  tOfi  SOKe  ,   »__y   .i._  i   l   __J  1   .CfvTiifoUrtr,  .k  . _   -r,   ,   .   .   '   *   J
Megalobatrachus  ja-  Spotted  Salamander  Vi
Blant  s.  of  Japan,  which  attains  a   length  of or  more  The  salamanders  were  formerly  fabled to  llie  In  ani  extinqu'sh  Are  muieu
^   “   fire,  an  elemental
fare-spmt,  the  imaginary  sprite  embodying  6re  hence f21  person  who  can  stand  great  heat.
(2)  A   Boldicr  "ho  13  brave  under  fire  (3)  A   juggler who  cats  fire  3.  A   pouched  or  pocket  gopher  (Geomus tusa)  of  the  southeastern  Umted  States  4.  [Collotf] poker  or  other  imolement  used  in  ann specif  (1)  A   metal  pfate ®   browning  meats,  pastry,  etc  ,   by  being
passedover  and  near  their  surfaces  (2)  A   metal  drum  or hot  coals,  etc  ,   used  in  drying  plaster b'  rcolloo rennon.  a   loggerhead, term  He.  ^   fire'Pre°f  onginally  a   trade ^   four-footed  beast  represented  pas- sant, breathing  or  surrounded  by  fiames  7.  Alelal metal  or  siag  remaining  m   the /orewoo  “ftor  the  fires  are  drawn  [   <   r   sata- ”p  Pe?’s™an5arT“"*“'  "‘■'amohdre,  salamander.
Resembling  or  having  the  form ~   ”   vl  Herp  A
saiamandroldean  amphibians,  especially  those having  opistboccelous  vertebra?,  vomeropalatine  bonM
PostfSsqLmos^ g)— sal"a-man'<irid,  « —
« -Sal"a-raan-drl'na,  n   vl .fferp  The  ^aZamandreftfea  —   Sal"a-m3n-drl'n<o.  n   vi Herp  1,  The  iSaZamandrfda;  as  a   subfamily  2   The  g/iZ/i mamfrofdca-saI"d-man'drln(e3.  I   a   1.  of  uertfin- Ing  to,  or  like  a   salamander,  enduring  fire  ’2  Ot  or pertaining  to  the  Safomandrin^  II  n   Oneof  the5a/aman- drin®  sal  a-man'drold  I.  a   Of  or  pertaining  to  the Salamandridx  -SaF'a- A   super/amlly  or  suborder ^   amphibians,  especially  those  having  two  pairs  of and  stapes  unconnected  with  the  quadrate r”.Bhl"a-man-drol'de-an,  a   &   n
l<  AS  sacu,  strife) -for  old  sake’s  sake,  for  the  sake of  times  gone  by  —   for  one’s  name’s  s   .   out  of  regard  to ones  name  —   la saUes!  land  sakcsl  sakes  allicl  Indeed! rustic  corruptions  of  mild  expletlies,  now  but  Interjec- tions of  surprize  .
sa'kc’,  1   sn'KI,  2   sn’ke.  n   [Jap  1   1.  A   fermented  liquor made  from  rice.  2,  By  extension,  In  Japan,  any  spirit- uous liquor  fia'keef;  sa'kf  f. sa-kecn',  1   so-kin',  2   sa-ken',

=== FSD vol4 page nums near ===
```


## [2026-09-14T01:25:51.862Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY سمندر ===\"; grep -n \"سمندر\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY شالی ===\"; grep -n \"شالی\\|شلتوک\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY ساج ===\"; grep -n \"ساج\" incoming/ARY/ARY_pages.txt | head -5\necho \"=== ARY سیستان/سگزی ===\"; grep -n \"سیستان\\|سگزی\" incoming/ARY/ARY_pages.txt | head -5"
}
```


### [2026-09-14T01:25:51.953Z] TOOL RESULT

```
=== ARY سمندر ===
=== ARY شالی ===
=== ARY ساج ===
5588:۱ چم این واژه در زبان‌های رمانس (ناشی از لاتین) و اسلاوی: نساجی؛ بافندگی.
=== ARY سیستان/سگزی ===
15249:۵- شاهدی برای "وال" و "بال" در زبان‌های پهلوی و اوستایی نیافتم ولی این واژه در زمان فرخی سیستانی (رفات
```


## [2026-09-14T01:25:54.341Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1/2 سمندر ===\"; grep -n -o \".\\{80\\}سمندر.\\{120\\}\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON شالی ===\"; grep -n -o \".\\{60\\}شالیزار.\\{120\\}\" MON_part1.txt MON_part2.txt | head -4\necho \"=== MON شلتوک ===\"; grep -n -o \".\\{60\\}شلتوک.\\{120\\}\" MON_part1.txt MON_part2.txt | head -4\necho \"=== MON ساج ===\"; grep -n -o \".\\{60\\}ساج.\\{100\\}\" MON_part1.txt MON_part2.txt | head -6"
}
```


### [2026-09-14T01:25:54.570Z] TOOL RESULT

```
=== MON part1/2 سمندر ===
=== MON شالی ===
=== MON شلتوک ===
=== MON ساج ===
```


## [2026-09-14T01:26:07.483Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## awk NR==631\"; awk 'BEGIN{RS=\"\\f\"} NR==631' BQT_v2_pages.txt | grep -n \"سمندر\" | head -5\necho \"########## awk NR==632 full\"; awk 'BEGIN{RS=\"\\f\"} NR==632' BQT_v2_pages.txt | head -70"
}
```


### [2026-09-14T01:26:08.660Z] TOOL RESULT

```
########## awk NR==631
37:     ‫سمندر ‪٩‬‏ » بروزن قلندر » نجانوری‬                      ‫‪.‬وبند از سل سام‬  ‫بود گ‬       ‫ه‬‫تو‬
64:               ‫بآب اندرون بر مثال لهنگان ‪.‬‬                        ‫باتش درون بر مثال سمندر‬
########## awk NR==632 full
                                                                                                       ‫—‬

           ‫سهام بممنی آش هم آمده است"‬
                                    ‫چ‬                         ‫است که در آتش متکون میشود ‪ .‬گوبند مافند‬
 ‫‪ = 3‬بفتح اول وکاف فارسی‬                                      ‫موش بزرکی است وچون ازآتش برهیاً بدمیمیرد‬
 ‫ااستهدوراز ‪ ۴‬که‬         ‫رامی‬
                            ‫ه‪,‬‬  ‫و بعضیکوبند همیشه درآتش لیت کاهی بر بالف کشی‬
                              ‫شده‬
 ‫دختر پ"ااده افجا را رستم خواست و سهراب‌ازو‬                   ‫میا بددر آلوفت او را میگیرند و از پوست او‬
‫بوجود آمد ؛ و پم انی حم گفته اند و درىن‬                        ‫کلاء و رومال میازند وچون چر کن میشود در‬
‫زمان آن شهر را رامهرمز خوانند و عوام رامز‬                      ‫آتش میاندازند کچهرای اومیسوزد وپاكمیشود؛‬
‫گوبند ‪ - .‬و بعضی کوبند نام شهپری است در‬                       ‫و بعضی گوبند بصورت سوسمار وچلپاسه است از‬
                                           ‫توران ‪.‬‬
                                                              ‫پوست اچوتر سازند تاگرمی را نگاه دارد و از‬
 ‫د بفتح اول والی و نون‌مضموم‬     ‫سمنو ‏‬                        ‫موی او جامه بافند ودرهوای کرم‌پوشندمحافظت‬
‫‪ ۲‬واو تاکر ‪ ,‬چبزی‌است مالند حلوای نروآنرا‬
                                                              ‫گرماکند ؛ وبعضی دیگر گوبند صورت مرفی‬
                                                               ‫أت اناعلم ‪ -‬و نام ولایتی است از هندوستان‬
‫از شیر ريشة کندم سبز شده پزند ‪ -‬و ضم اول‬
                                                              ‫از آیجا آورند ‪٩‬‏ ؛ و معنی‬              ‫عود‬   ‫که چرب‬
                   ‫آش رشته وآش اکرا باشد‪.‬‬
                                                                ‫اول‌یکسر دال وضم دال هردو بنظر آمده‌است‪.‬‬
‫سمئوق = بفتح اول بروزن ممنون" نام‬
         ‫درویشی بوده صاحب حال ورباخت کش‪.‬‬                         ‫ی‬
                                                                 ‫نو‬‫عزن‬
                                                                     ‫مبرو‬
                                                                        ‫‪ -‬بالام »‬                   ‫سمندل ‏‬
                                                                                ‫سمندر است که جالور آنشی باشد‪.‬‬
‫سمنه ‪ = 1‬بطم اول و سکون انی و فتح‬
‫ثالث » بعربی‌دانه‌ایت‌سیاه رنگه‌ازنخود کوچکتر‬                  ‫» بمعنی‬      ‫ننقور‬
                                                                                ‫بسرقوز‬          ‫سمثك‌ور ‏‬
‫و آن را در خراسان شل خواجه گوبند ‪.‬‬                            ‫س‌ندر است کهجالور آنشی باشد ‪- ۴‬ونام ولایتی‬
                                                                            ‫هم هست که ازا يجا عود آورند ‪. ۴‬‬
 ‫فربهی آورد و باه را برانگیزد ‪ -‬وهر تکریبی‬
 ‫را نیز گویند که‌آدمی‌را فربه کند وآنرا سمینون‬                ‫وبزرن پرستوك » به‬   ‫سمندو لك ‪= ۲‬‬
                                     ‫‪7‬‬                              ‫معنی سمندر است که حیوان آنشی باشد‪.‬‬

 ‫سهو د بروزن عمو تر دشتی‌را گویند‪.‬‬                            ‫سمندول ‪ = ۲‬بالام‪,‬بروزن و معنی‬
       ‫وآن سبزیی باشد که بطاعام خورند ‪. ۷‬‬                     ‫سمندور است؛ و آن جانوری باشد که در آتش‬

 ‫سمو تا ه بنتح اول وضم ثانی و سکون‬                                                                  ‫متکون میشود ‪.‬‬
‫واو و فوفانی » فتراك راگوبند‪.‬وآن دوالی باشد‬                    ‫سمند‌ون ؟ = بروزن شفق کون ب»ه‬
 ‫پاريك که درزین اسب آویزند و بترکی قنجوقه‬                      ‫ممنی سمندر است که جادور آتشی باشد‪ .‬واصل‬
                                         ‫خوالند ‪.‬‬              ‫ابن لفت سام اندرون بوده یعنی دراندرونآتش»‬

  ‫‪« - ۴‬سمندور » دام شهر ست‬                     ‫‪.‬‬   ‫‪ ¦:‬سمنثر‬    ‫رك‬      ‫‪۳‬‬            ‫رك ‪ :‬سمندور ‪.‬‬      ‫‪۱‬‬

   ‫رك‪:‬س لودو چپارمقدمه ‪ :‬سمنگان‪:‬‬         ‫‪۴‬‬                    ‫از آییا آردد» « لذت فر س ‪٥٩)٩‬‏‬        ‫در هند که عود‬


  ‫«سمنسان ‪۰‬‬    ‫درههء‌جم البلدان ‪1۹‬‬   ‫‪nãgnimiS.‬‏‬               ‫‪:۵۳۱ ۰‬‬       ‫‪۰۶‬‬   ‫‪۳‬‬    ‫میئورسکی ‪ .‬حدود‪.‬ص‬        ‫ورك‪:‬‬

   ‫«رعرف حلوای سکموذیكند»«رشیدی»‬
                               ‫© _ د‬            ‫شهری ازطخارستان آنسوی بلخ وبنلان» ‪۰‬‬
  ‫دکرزنباوننی ‪ 0020785‬کرند ‪-« 1 .‬سمنه بالضم کیاهیاست که ببب ستاره های تابستان‬

           ‫کشت زنگار کون همه‌لب کشت‬                               ‫تاسمو سر برآورید ازدشت‬             ‫‪_¥‬‬

                                                                    ‫هریکی کاردی ز خوان برداشت‬

   ‫‪.‬‬   ‫‪£‬‬   ‫کی سمر قندی‪« .‬لخت فری‬         ‫رود‬
```


## [2026-09-14T01:26:19.694Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==631' BQT_v2_pages.txt | sed -n '30,75p'"
}
```


### [2026-09-14T01:26:21.049Z] TOOL RESULT

```
    ‫است و کوبند که نظر آن جاور برهرکه‌مبافتاد‬
                                                            ‫عموماً وروغن کاو را خصوصاً ‪ ۴‬و رنوگغارچون‬
    ‫فی‌الحال هىمرد » بارسطو متوسل شد لد ‪.‬اوکفت‬
                                                                     ‫بیار کهنه شود دفم سامفعی کند ‪.‬‬
    ‫که ایینه‌ای در یش روی آن جاتور بدارید تا‬
    ‫چون عکس خود را مشاهده لماند بمیرد‪ .‬چنان‬                ‫سمنار؟ د یکراولرترن بالف کشیده‬
                              ‫کردند چنان شد ‪. ۷‬‬             ‫کلار نام بنابی بوده رومی که سمدیر‬‫بورزن گ‬
     ‫سمندر ‪٩‬‏ » بروزن قلندر » نجانوری‬                      ‫‪.‬وبند از سل سام‬  ‫بود گ‬       ‫ه‬‫تو‬
                                                                                          ‫اقخراا‬
                                                                                               ‫سورن‬
                                                                                                  ‫وخ‬

                                                     ‫(‪ )۱‬خم‪ : ۱‬وتبر ؛ چش ‪ :‬وبر (رك‪ :‬وثير) ‪.‬‬
      ‫‪.« ( €‬م‪ ( .‬است ‪۰‬‬   ‫‪ 2‬سمتگان‬    ‫در معجم اللدان ‪J‬‏ نشبةا لدهروحدودالعالم لیامده وطاعر انف‬           ‫‪-‬‬   ‫‪۱‬‬
      ‫‪( -‬عر) «سمن بالفتح» روغن» «منتهی‌الارب؟ ‪.‬‬                ‫‪ = ۴‬بهلوی ‪ « 020125‬اونوالا ‪۳۲۱٩‬‏ ‪.‬‬
                               ‫ست نظاه‌ی استنماط کردها لد (‪: )۱‬‬     ‫ازن‬   ‫_‬   ‫‪۵‬‬         ‫‪۰‬‬   ‫‪ :‬صنمار‬   ‫راد‬   ‫‪۳‬‬


                ‫(نسلین‪.‬د‪ ).‬ونام او صمنار‬     ‫سام دسی‬             ‫ویرین‌کار‬
                                                                         ‫چابکی چرب دست ش‬
                ‫نظامی گنجوی «هفت یکر چاپ‌ارمفان‪۹‬ه»›‬

                                               ‫کفت ‪:‬‬      ‫» اسپ زرده بود » منجدك (نرمذی)‬        ‫‪«_ ۱‬سمند‬

      ‫همه کوبت( کمیت‪.‬دهخدا) دمایدزخون‌ساه‌سمند ‪.٩‬‏‬      ‫بر آنزمان که برابطال تیره کون کردد‬
                  ‫ص‪ ۵6 ۰ ۶۵ ۰ ۳‬وتعلِقات ص‪. ۲۱‬‬      ‫«لفت فرس ‪ ۶۰۰۱‬ورك ‪ :‬نوروزنامه ‪۵‬‬
       ‫سمند اسلارمی‌باید ‪۳‬‬   ‫اسلار را عکس‬     ‫صمنث‬           ‫‪ - ۷‬علاج ذات شومت‌شومی ذانت کند آری‬
      ‫غعاث لقشیند‪« .‬فرهنگه نظام>‪.‬‬
      ‫‪ - ۸‬از پودانی ‪ . 210040۳2125‬رك ‪ :‬سالا‌ندرا » در فراننوی یز ‪ 67002002189‬بىعنى‬
       ‫( ‪ ۰‬رگ‪:‬سمندل‪.‬‬     ‫(از افادات علامه دهشدا‬      ‫ات‬    ‫وینبهٌ کوهی وحوان معروف‬     ‫فرشتة موکل‌ اش‬

                                       ‫‪:‬‬    ‫ِ ومخصوصاسالامندرا‬    ‫‪ ۰‬صمندون‬    ‫‪a‬‏ صمند وگ * صمتدول‬     ‫سمندور‬


               ‫بآب اندرون بر مثال لهنگان ‪.‬‬                        ‫باتش درون بر مثال سمندر‬
      ‫رود کی سمرقندی ‪.‬لەت فری‪۵۳۱‬؟ ‪.‬‬
            ‫( برهای لاطاع ‪۱۵۱‬‬
```


## [2026-09-14T01:26:37.667Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 614 615 616 617 618; do echo \"##### awk NR==$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | grep -n \"سکا\\|ساک\\|ساس\\|سکه\" | head -6; done\necho \"##### NR==623 (سگزی/سگستان)\"; awk 'BEGIN{RS=\"\\f\"} NR==623' BQT_v2_pages.txt | grep -n -A2 \"سگزی\\|سگستان\\|سجزی\" | head -20"
}
```


### [2026-09-14T01:26:38.758Z] TOOL RESULT

```
##### awk NR==614
36:‫نم اول و انی مالف کشیده‬         ‫ه‬   ‫سکاچه‬              ‫نوی‬
##### awk NR==615
3:‫بروزن خلاصه » نمعتی سکاسته است که‌خاریشت‬                                     ‫‌نهنده‬       ‫ت سخ‬‫سعنی‬
9:‫ده‌هی‬       ‫بروزن گذاشته ‪.‬‬           ‫‪۰ ۸‬‬        ‫سکاشته‬                        ‫کوبند‪,‬وآن سنگنیی است که درخواب برمردم‬
13:                                                           ‫باشد ‪.‬‬        ‫سکاك ‪ ۴‬ت بفتح اول‌بروزن سواد»سر کوه‬
14:‫باشن نقطه‌دار » بروزن‬                 ‫‪۰ 4‬‬       ‫سکاشه‬                                            ‫و فرق سرآدمی را گویند ‪.‬‬
19:                                        ‫و معنی سک‬                         ‫سکار ‪ = ۴‬بکر اول بر وزن شکار »‬
21:‫صم اول‌وئالیءالف کشنده‬               ‫‪٩‬‏ =‬      ‫سکافره‬                         ‫را گیوزبند ‪ -‬و نوعی طامزام هم‌هست؛ بوقتح‬
##### awk NR==616
14: ‫اللوث وسکون‬    ‫سکبه = بنتم او‬                                      ‫سکالو ا‪۲‬ول=ب‌ضومرابع‌بواو کشیده‬
15:‫ثالی » نوعی از طعام است ‪ - ۷‬و روغن با كعك‬                           ‫بممنی سکارو باشد بمنی آنچه برروی زغال‬
17:                                                                    ‫وسکالیو هم گفته‌اند که بعد ازلام بای‬               ‫و غبره‬
25:                                                                     ‫‪ ۴‬بکر اول بورزن‬                    ‫سکالیدن‬
41:                                                                    ‫سکاهن ‪ -‬بکسراول وفتح ها وسکون‬
56:     ‫‪ :‬بگاله ‪۰‬‬      ‫رك‬       ‫‪۴‬‬                 ‫سکالو (ه‪.‬م‪ = ).‬شکالو(ه‪.‬م ) ‪۰‬‬         ‫=‬       ‫سکارو (ه‪.‬م‪).‬‬     ‫=‬   ‫‪۱‬‬
##### awk NR==617
33:‫کردن و آواز بگلو در آوردن باشد ‪ -‬و بمعنی‬       ‫سینبی‌نقطه وفتح فوفالی و نون ساکن ‪ ۰‬بمعنی‬
##### awk NR==618
##### NR==623 (سگزی/سگستان)
62:     ‫واسبت بدان سکزی ومعرب‌آن سجزی‌است‬                   ‫سیستان) معروف شد ‪+‬ابران باستان جح ‪۳۸۵۲۲‬‬
63-          ‫‪ ۴‬رك ‪ :‬سگه کن‪.‬‬              ‫‪- ۴‬رك‪ :‬سگە کنك ‪.‬‬                   ‫‪ - ۴‬رك ‪ :‬سجنبوبه ‪.‬‬
64-     ‫‪ - ۱‬رك ‪ :‬سگەلاب ‪.‬‬               ‫‪. 9‬رك ‪ :‬سک لابی ‪ ۰‬سکهلاو » سکهلاوی »مقلاب ‪.‬‬
```


## [2026-09-14T01:26:44.381Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==623' BQT_v2_pages.txt | sed -n '45,70p'"
}
```


### [2026-09-14T01:26:45.460Z] TOOL RESULT

```
                                              ‫‪۰‬‬   ‫بوزن‬   ‫(‪ )۲‬چك ‪:‬‬         ‫‪ :‬برحامه ‪۰‬‬   ‫س‬


   ‫مر کب‬     ‫‪YC‬‏‬    ‫شپرستانهای ابرانشهر ص ‪۷۱‬‬             ‫پ‪-‬هلوی ‪ « 08050825‬مارکوارت ‪.‬‬
  ‫از ‪ 8685 = ( 7‬نام قومی باستانی (‪-‬ستان یسوندمکان) » در زمانهای باستانی تیرۂ انبوهی‬
   ‫از آرباییان میانةٌ ابران واروپا سکوت داشته‌الد وهميشه بتاخت و تاراح کوشتارمی برداخته‌اند‪.‬‬
   ‫نام این قوم کدتريبة بهستان (یستون) ‪8628‬باد شده ‪ .‬بونایان این مردم را اسکوت ‪6۲۳)165‬‬
    ‫می نامیدند وهمین نام است که درزبان فراسوی «سیت» خوانده مشود « مقالات کروی ج ‪ ۱‬ص‬
    ‫_ ‪ ۰۸۱‬مقارن سلطنت فرهاد دوم اشکالی(‪ ۸۲۱ - ۹۳۱‬ق ‪ .‬م‪ ).‬واردوان دوم (‪۷۲۱-4۲۱‬‬                        ‫‪۹‬‬
    ‫ق ‪.‬م‪ ).‬براثر هجوم «بوشه چبان» ( طایفه‌ای از مغول ) بممالك متمدن » مردمان اطراف‌سیحون‬
    ‫وحتی جیحون ‪.‬ازماکن خود کنده شدند و درصدد تهیهٌ اراضی تازه برآمدند‪ .‬ازجمله «سکه‌هاء‬
    ‫‪۶‬ريك =‬
         ‫سکه ها در ز‬
                   ‫منقوض کردلد و بطرف جنوب راندند ‪.‬‬                          ‫دولت بونالی باختر ( بلخ )‬
    ‫(ج=ستان»سکزستان‪,‬‬
                   ‫(‪ 8081808121‬بونایان)»مستقرشدند ‪,‬ازاین زمان زرنگه بانام‌سگتان س‬
     ‫واسبت بدان سکزی ومعرب‌آن سجزی‌است‬                   ‫سیستان) معروف شد ‪+‬ابران باستان جح ‪۳۸۵۲۲‬‬
          ‫‪ ۴‬رك ‪ :‬سگه کن‪.‬‬              ‫‪- ۴‬رك‪ :‬سگە کنك ‪.‬‬                   ‫‪ - ۴‬رك ‪ :‬سجنبوبه ‪.‬‬
     ‫‪ - ۱‬رك ‪ :‬سگەلاب ‪.‬‬               ‫‪. 9‬رك ‪ :‬سک لابی ‪ ۰‬سکهلاو » سکهلاوی »مقلاب ‪.‬‬
  ‫مبارن قاطي ‪) ۰۵۱‬‬
                 ‫(‬
```


## [2026-09-14T01:27:02.753Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"شالی\\|شالیزار\" BQT_v3_pages.txt | head -10\necho \"=== شلتوک ===\"; grep -n \"شلتوک\\|چلتوک\" BQT_v3_pages.txt | head -10"
}
```


### [2026-09-14T01:27:02.848Z] TOOL RESULT

```
1142:‎oy‏ را «شالی» کوبند . «فرهنگهنظام». ‏ ۴ -رله:شاماخچه»شماخ. وقس:شماخیه«جهانگیری».
1209:کردن باشد ۴ - ومشفف ‎Quiles‏ و شالیدن هم
1320:‏بهر هشتاد ‎cy‏ چل شالی +
5003:lls ‏کاشالی. « فرهتکه‎ glue IT ‏ابوطالب‎
5121:که همت را زنائوبیت از زالو و پیشالی +
5241:آی از آن چون چراغ پیشالی
5886:باشتد و بهندی شالی خوانند.
6220:‏شالی ‎ath‏ که بر دوش اندازند و بر سر
7971:‎Sol,‏ و پربشالی باشد ۴ ۰
10287:متر را پوشالیده است . رث: کرستنین . شاسان ص ۳۹۶ بیعد .
=== شلتوک ===
```


## [2026-09-14T01:27:08.724Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<=1145 && /\\[pdf page/ {p=$0} END{}' BQT_v3_pages.txt >/dev/null\necho \"-- pdf page tag before line 1142:\"; awk 'NR<=1142 && /\\[pdf page/{p=$0} END{print p}' BQT_v3_pages.txt\necho \"-- pdf tag before 5886:\"; awk 'NR<=5886 && /\\[pdf page/{p=$0} END{print p}' BQT_v3_pages.txt\necho; echo \"=== context 1120-1150 ===\"; sed -n '1120,1150p' BQT_v3_pages.txt\necho; echo \"=== context 5875,5895 ===\"; sed -n '5875,5895p' BQT_v3_pages.txt"
}
```


### [2026-09-14T01:27:10.082Z] TOOL RESULT

```
-- pdf page tag before line 1142:
[pdf page 20]
-- pdf tag before 5886:
[pdf page 79]

=== context 1120-1150 ===

‏شاها کی ۷ بروزن ‎SNe‏ سینه
بند زان ‎wath‏

‏شامس ‎oS‏ بکس میم وسکون سین
بی‌شقطه . نام یکی از جزایر بودان است؛وباشین
نقطهدار هم‌آمده است.

‎°

‎the ‏وزن داموی‎ no Sn gald
Ab ‏بلدی است از بلاد بونان ؛ و بستی گوبند‎

‎+ cole po
‏شاهه = بروزن جامه ۰ مقتمه ورویاکی‎
. ‏باشد که زدان بر سر کنند‎

‏شان » بر وزن ‎ME sob‏ زبور صلرا
کوبندکه درآن ‎Le‏ باشد*۱ - و ‎le dies‏
مقید است که از هندوستان آورند - و مشقف

‏۱ - سانسکریت ‎Shali‏ (برنج وغلات مشابه آن) « وبلیامز۱:۱۰۹۸» درمازسران زراعت
‎oy‏ را «شالی» کوبند . «فرهنگهنظام». ‏ ۴ -رله:شاماخچه»شماخ. وقس:شماخیه«جهانگیری».

‏ورك : شا .
شاماکچه )0( = شماخچه «جهانگیری» .

‏شاماخج » شاماخچه , شاماکی . ‎٩‏ = شاماخجه ‎Cem)‏

‏۴ از : ‎cue‏ (هم.) +-چه ‎igs)‏ تصفیر) = ساماخچه ۶ ساما که .
۴ - ظ.مصحف «شابهار» («م.) .

=== context 5875,5895 ===
os

ving ‏با بای حظی‎ - Wd
‏شخصی راکوند که در ابرام افراط کند.‎

شلیو ی ‎be‏ بای فارسی بروزن‌حفگوی,
آراز پای را کوبند که بهتگلم راه رفتن بگوش
آید ۱ .

‎Sgt‏ » با واومجهول بروزن مفلولد؛
‎te‏ راگوبند که هنوز از پوست بر نیاورده
باشتد و بهندی شالی خوانند.

‏شلته = با اول مفتوح و سکون ‎Carel‏
‏فوقالی .جای مردار وناپاك را گوبند .منی‌موضعی
که در آن سرکن و ‎sol‏ و خاکروبه وامثال
آن ریز لد -

‏شلخته - با اول و ثالی مفتوح وسکون
خای قطمدار و قتح ‎ol‏ قرشت » لگدی باشد
```


## [2026-09-14T01:27:25.992Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 ساج ===\"; awk 'BEGIN{RS=\"\\f\"} /ساج/ {print NR}' BQT_v2_pages.txt | head\necho \"=== LKT teak/sag ===\"; grep -n -i \"Teak\\|Teakholz\\|sadsch\\|sāǧ\" LKT.txt | head -10\necho \"=== AFM ساج ===\"; grep -n \"ساج\" AFM_pages.txt | head -10\necho \"=== PLA saj ===\"; ls incoming/PLA/ 2>/dev/null | head"
}
```


### [2026-09-14T01:27:27.322Z] TOOL RESULT

```
=== BQT v2 ساج ===
358
438
529
530
=== LKT teak/sag ===
3995:'Holz  von  Tectonia  grandis'  [aus  sskr. säka,  woraus  andererseits  malayäl.^efcÄ;«, tamil.  tekku  wurde];  hieraus  die  wissen- schaftliche Bezeichnung  lignum  sagali- ntmi;  aus  der  tam.  Form  wurde  engl. teak,  dtsch.  Teckholz  und  der  botanische Name  Tectonia.  [ZDMG  L,  650.  DeSacy ChrAr  450/452.  Hobson-Jobson  910/911.
=== AFM ساج ===
267:١‏ الأسْتاقل ) ܣ .27 10 سش قاقل ويقال له بالتركة مبر ساجان
2169:ܣܘܓܪܐ بمنى الساجور في كتاب كايلة ودمئة طبعة يكل ٠‏ وعندي ان الكلمة
2465:(اساج ) شجر يعظم جدًا قيل لا ينبت الا ببلاد الهند ܐܚܠܬ ساج
=== PLA saj ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-14T01:27:29.699Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 Scythia entry? ===\"; grep -n \"Scythia,\\|Scythian,\\|Scythes\" KLN_1966.txt | head -5\necho \"=== WEB vol1 salamander? ===\"; grep -n -i -m2 \"salamander\" WEB*.txt 2>/dev/null | head -3\necho \"=== IEC / SYN rice ===\"; grep -n -i -m3 \"sali\\b\" SYN.txt | head -5\necho \"=== HJB SAGWAN/SAJ ===\"; grep -n \"sdgwdn\\|sagwan\\|sdgun\\|s.gun\" HJB.txt | head -5"
}
```


### [2026-09-14T01:27:29.817Z] TOOL RESULT

```
=== KLN 1966 Scythia entry? ===
17558:hemostat,  haemostat,  n.,  anything  that  stops hemorrhage;  specif.,  an  instrument  used  to compress  a  bleeding  vessel.  —  Fr.  hemostatic, hemostatic,  haemostatic,  adj.,  serving  to  stop hemorrhage;  styptic.  —  Compounded  of  hemo- and  Gk.  oxaxixoe;,  ‘causing  to  stand’.  See  static, hemp,  n.  —  ME.,  fr.  OE.  hsnep,  henep,  rel.  to OS.  hanap,  ON.  hampr,  Swed.  hampa,  Dan. hamp,  MDu.,  Du.  hennep,  OHG.  hanaf,  MHG. hanef,  hanf  G.  Hanf(—  Teut.  *hanap).  Cp.  Gk. xawotfki;  (whence  L.  cannabis),  Arm.  kanap‘. Alb.  kanep,  Russ.-Church  Slav.  konoplja(  whence Lith.  kanapes),  ‘hemp’.  All  these  words  are loan  words  from  a  foreign,  possibly  Scythian, language.  Cp.  canvas,  canvass.  Cp.  also  sunn. Derivative:  hemp-en,  adj.
18299:hyal-,  form  of  hyalo-  before  a  vowel, hyalin,  n.  — -  See  hyaline,  n. hyaline,  adj.,  glassy;  transparent.  —  L.  hyalinus, fr.  Gk.  udXtvo;,  ‘glassy’,  fr.  oaXo;,  ‘alabaster, crystal,  amber’,  prop,  ‘a  transparent  stone’,  later ‘glass’,  which  prob.  stands  for  *sualo-.  Cp.  L. suali-ternicum,  ‘a  kind  of  reddish  amber’,  which, according  to  Pliny  37,  33,  »s  of  Scythian,  i.e. North  European,  origin.  See  Boisacq,  DELG., p,996,  s.v.  uaXo;,  and  Walde-Hofmann,  LEW, II,  61 1,  s.v.  sualiternicum.  For  the  ending  see suff.  -ine  (representing  Gk.  -ivo;). hyaline,  n.,  1)  something  glassy,  as  the  smooth sea  or  the  clear  sky;  2)  (in  this  sense  spelled  also hyalin)  a  substance  forming  the  walls  of  hydatid cysts.  —  See  hyaline,  adj.
34326:Scythian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Scythia,  fr.  Gk.  SxulKix,  ‘the  country  of  the Scythians',  fr.  2x6&r(?,  ‘a  Scythian’, se-,  pref.  —  L.  se-,  a  collateral  form  of  sed-,  ‘aside, apart’,  rel.  to  the  prep,  sed,  se,  ‘without’,  and to  the  conjunction  sed,  ‘but’,  fr.  I.-E.  reflexive base  *swe-,  *se-,  whence  also  OSlav.  svg-ne, svd-ni,  ‘without’.  See  secret,  sedition,  sedulous, select,  separate,  severus,  solve.  See  also  ebriety, sober,  idio-.  See  also  zenith.  For  an  enlarged form  of  the  above  base  see  sine  and  prep, sunder.
=== WEB vol1 salamander? ===
6439:Am-blys/t6-ma, 2. [L., from Gr, amblys, dull, and stoma, mouth.] a genus of salamanders, the type of the family Amblystomidz. Also called Ambystoma.
6441:Am-bly-stom/i-dae, 7.pl. a family of amphibi- ans of which Amblystoma is the typical genus. They are salamanders found only in America.
=== IEC / SYN rice ===
6039:Skt. kantha-, prob. a Middle Indic form of a *kartra- (> *katta, *kattha-, then kantha- with the secondary nasali- zation frequent in Middle Indic), fr. *kvol-tlo-, deriv. of the same IE *kvel- ‘turn’ as in Lith. kaklas, Lat. collum, Goth. hals, etc. (above, 2). Tedesco (to appear in JAOS).
11376:Bie tupbv, NG Evpadr, Skt. ksura-, thoy. in Grk. tlw ‘scrape, scratch’, etc, a0 extension of *kes- in Chsl. sali ‘comb, scrape’, sb. Ceslit ‘comb’, eto, (6.91). Here also prob. Lat. nova- tila (> Sp. navaja), apparently formed fr.alost vb. *novare based on a parallel extension with nasal infix, namely then-eu- seen in Skt. ksnu- ‘whet’. Walde-P. 1.450. Ernout-M. 679.
25959:1022 SELECTED INDO-EUROPEAN SYNONYMS 15.21-24 SMELL 15.21 15.22 15.23 15,24 vb. subj. vb.obj. sb. subj. sb. obj. Grk.  dc¢palvopar ofw dogpyots éou7 (65%) NG pupltw, -ouac nupltw pupword pupwitd Lat. olfacere, odorari olére, fragrare odordtus odor It. sentire, odorare odorare odorato odore Fr. sentir, flairer sentir odorat, flair odeur Sp. oler oler olfato olor Rum, mirost mirost miros mtros Ir. boltigur bolad, boltunud with vb. boltanugud bolad, boltunud Nir. —bolinuighim boladh with vb. boladh boladh W. arogli arogli arogliad arogl Br. chouesa c’houez with vb. c’houesa c’houez Goth. dauns dauns ON pefja, pefa(ilma) pefa, befja(ilma) ilming Pefr (ilmr, daunn) Dan. lugte lugte lugt lugt Sw. lukta lukta lukt lukt OE gestincan, gesweccan stincan slenc, swacc slenc, swacc ME smelle smelle smelle smelle NE smell smell smell smell, odor Du. ruiken ruiken reuk reuk OHG - stincan slincan, riohhan, swehhan  stanc stanc, rouh, sweche MHG riechen, smecken riechen, smecken geruch ey rouch, geruch (stanc, smac) smac NHG riechen riechen geruch geruch Lith. _uostz, uostyti kvepeti uoslé kvapas Lett. uost, uostit uost, smakuot uoza smaka, uoza ChSI. obonjati, achati vonjalt obonjantje, vonja achanije SCr.  mirisati mirisali, vonjali njuh, njusni miris, vonj osjet Boh. iti, Gichati padchnouli, vonéli éich zépach, viiné Pol. wachaé pachnqé wech zapach, wor Russ. njuchat' pachnit’ obonjanie zapach Skt.  ghra- gandha- with vb. ghrana- gandha-, ghrana- Av. bud- baosi-, ganti-
=== HJB SAGWAN/SAJ ===
9741:1578.  —  " .  .  .  la  qual  (ncm)  on  vasos despuea  distilan,  para  hazer  agrua  ardiente, de  JA  qual  una,  a  que  ellos  Daman  Fola, quequiere  dear  '  flor,'  es  mas  fina  ...  y  la segunda,  que  llaman  Orraca,  no  tanto." — AeoMtOy  p.  101.
15027:1612.—*'.  .  .  Trata  da  causa  primeira, segundo  os  livros  one  tem,  chamadoe Terum  Maadra  mole'*  {matUra-mula,  w^Ata *text ').— C<wto,  Dec.  V.  liv.  vi.  cap.  S.
21812:TEAK,  s.  The  tree,  and  timber  of the  tree,  known  to  botanists  as  Tec- tona  grandis,  L.,  N.O.  Verberuiceae.  The word  is  Malayal.  tekka,  Tam.  tekku. No  doubt  this  name  was  adopted owing  to  the  fact  that  Europeans  first became  acouainted  with  the  wood  in Malabar,  wiiich  is  still  one  of  the  two great  sources  of  supply  ;  Pegu  being the  other.  The  Skt.  name  of  the  tree is  idka,  whence  the  modern  Hind, name  sdgwdn  or  sdaun  and  the  Mahr. sdg.     From    this   last   probably  was
```


## [2026-09-14T01:27:45.324Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM ساج context ===\"; sed -n '2460,2472p' AFM_pages.txt\necho \"-- page tag:\"; awk 'NR<=2465 && /\\[pdf page/{p=$0} END{print p}' AFM_pages.txt\necho \"=== PLA ساج ===\"; grep -n \"sāǧ\\|Saǧ\\|Teak\\|Tectona\\|ساج\" incoming/PLA/PLA_pages.txt | head -10\necho \"=== LKT page tag for 3995 ===\"; awk 'NR<=3995 && /\\[pdf page/{p=$0} END{print p}' LKT.txt; sed -n '3990,3998p' LKT.txt"
}
```


### [2026-09-14T01:27:46.437Z] TOOL RESULT

```
=== AFM ساج context ===
ܥܝ الشديد والمرض ٠‏ وقالوا فمه سهم الى غير ذلك 1 اذ 9 ]<
اي أقرع
* (السَهُم ) !ܐܟܬ تعريب سامّه ومن ܣܗܡܐ بالسر ܐܸܝ الدارجة
( سهنْسآه ) 0( افعل هذا سهنساه اى ]£ كل * شي٠‏ وهي فارسيّة مركة
نخص المستقدل ( حيط المحيط )
(اساج ) شجر يعظم جدًا قيل لا ينبت الا ببلاد الهند ܐܚܠܬ ساج
* (السَجْوَري » الأحق معرب كور اي كلبي
(السور) الضيافة فارسي بجت وهو 091
لجاز ܟܳܠ الفرس تعريب وار ܘܝܐ ܘ الفارس
( السُوس ) فارسي بحض بمنى الطبيعة والأصل
+ 0 ا ܡ وهو نات 6 ترق :مله حايت احص
ܐ 5 = لغة فيه
703 000 3 بالذهب 2 تعر يب سيم اي الع :43054 ܝܨ
-- page tag:

=== PLA ساج ===
=== LKT page tag for 3995 ===

17.Ö3.  Ar.  safat: 'Körbchen  aus  Palmblättern'  [KM  II, 934;  Lammens  Farük  Nr.  1037;  mit  ar. giwälik  <C.  pers.  guwälä  und  kuffa synonym;  aus  pers.  säpäd,  woraus  auch tk.  sepet  'Korb'] ;  hieraus  sp.  pg.  azafate 'flache  Schüssel,  Tablett',  kat.  aqafata, safata,  sard.  saffata  'Präsentierteller'; rum.  sipet,  sepet  'Koffer',  russ.  sapetka 'Korb'.  [DE  222.  Eguilaz  317.  ML  7503.
17.54.  Ar.  bäflu: [Offenbar  stammverwandt  mit  Nr.  1752] 'Rückenarterie',  augebhch  wörtlich  'ver- borgen', weil  die  so  benannten  Venen nicht  durch  die  Haut  schimmern;  nach Avicennas  Känun  wurde  im  Latein  der Anatomen  des  MA.  das  jetzt  noch  ge- brauchte Wort  Vena  Saphena  hieraus zur  Bezeichnung  oberflächlicher  Venen am  Beine:  Saphena  magna,  S.  parva, S.  accessoria.  —  [Das  Wort  kommt  also nicht  aus  gr.  aaqpriq  'deutlich'.]  [HAr HebrAn  212/215.
1755.  Pers.  säftälü;
'Pfirsich'  [vgl.  pers.  älü  'Pflaume'],  tk. seftali  'dass.';  hieraus  serb.  seftelija, septelija  'Pfirsich',  russ.  septala  'ge- trocknete asiatische  Pfirsiche'.
1756.  Ar.  säg:
'Holz  von  Tectonia  grandis'  [aus  sskr. säka,  woraus  andererseits  malayäl.^efcÄ;«, tamil.  tekku  wurde];  hieraus  die  wissen- schaftliche Bezeichnung  lignum  sagali- ntmi;  aus  der  tam.  Form  wurde  engl. teak,  dtsch.  Teckholz  und  der  botanische Name  Tectonia.  [ZDMG  L,  650.  DeSacy ChrAr  450/452.  Hobson-Jobson  910/911.
1757.  Hebr.  säTaT:
'Hin-  und  herwanken,  irren';  aus  der Partizipialform  jüd. -dtsch.  meschugge 'toll,  unsinnig'.
1758.  Pers.  sägbän: 'Ehemaliger  Soldat  oder  Amtsdiener,  der mit  Polizeidienst  betraut  war'  [aus  säg 'Hund'  Horn  NpEt  S.  164,  Nr.  743,  und bän  'Wächter'  ebenda  S.  41,  Nr.  176; also  'Hundewächler',  wie  auch  andere Benennungen  von  Dienstgraden  der Janitscharen  der  Jagd  entlehnt  waren, z.  B.  tu7-negi  'Kranichmann',  sagarg y 'Rüdenmann'],  ebenso  tk.  sejmen  [mit Wechsel  der  Labialen  b  >  »«  und  Er- weichung von  g  zu  j  wie  in  bej,  s.  hier Nr.  282] ;  hieraus  rum.  sehnen,  plr.  sei- meni  'Söldnei'truppen'.  [Löbel  EITAP  84.
```


## [2026-09-14T01:27:57.193Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i tad\necho \"---\"; for f in $(ls | grep -i \"^TAD\"); do echo \"## $f\"; grep -n \"سمندر\\|سمندل\" $f | head -5; done"
}
```


### [2026-09-14T01:27:58.264Z] TOOL RESULT

```
TAD_pages.txt
TAD.txt
---
## TAD_pages.txt
## TAD.txt
```


## [2026-09-14T01:27:59.556Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AF%D8%B1/",
 "prompt": "Quote the \"فرهنگ معین\" (Mo'in) entry for سمندر exactly, including any bracketed origin tag (e.g. [يو.] for Greek). Also quote the Dehkhoda entry's etymology statement if present."
}
```


### [2026-09-14T01:28:05.409Z] TOOL RESULT

```
# Etymology and Definitions from Persian Dictionaries

## Dehkhoda Etymology
The Dehkhoda entry states: "از یونانی «سالامندرا» در فرانسوی نیز «سالامندر» به معنی فرشته موکل آتش" (from Greek "salamandra," also in French "salamander," meaning "the angel in charge of fire").

## Mo'in Dictionary Entry
The Mo'in entry provides: "(سَ مَ دَ ) (اِ. ) جانوری دوزیست شبیه سوسمار، چهارپا دارد و رنگ پوستش تیره است با لکه های زرد" - describing it as an amphibian resembling a lizard with four legs and dark skin marked with yellow spots. The bracketed notation "(اِ.)" indicates the origin classification in that dictionary.

Both sources confirm the Greek origin (salamandra) and note the creature's biological characteristics as an amphibian.
```


## [2026-09-14T01:28:09.469Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l TAD.txt TAD_pages.txt; echo \"---\"; grep -n \"سمند\\|السمند\\|سلمندر\\|صمندر\" TAD.txt | head -10; echo \"--- head:\"; head -30 TAD_pages.txt"
}
```


### [2026-09-14T01:28:09.545Z] TOOL RESULT

```
  3312 TAD.txt
  3117 TAD_pages.txt
  6429 total
---
--- head:
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


           ‫الو مان‬
              ‫دام‬    ‫ده ل‬




                    ‫« طبعة ثانية ‪6‬‬




                    ‫حل '‬
```


## [2026-09-14T01:28:13.170Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== page tags?\"; grep -c \"pdf page\" TAD_pages.txt\necho \"== find page 37 region (leaf) ==\"; awk 'BEGIN{RS=\"\\f\"} {print NR\": \"substr($0,1,60)}' TAD_pages.txt | sed -n '30,50p'\necho \"== grep سمن ==\"; grep -n \"سمن\" TAD_pages.txt | head -10"
}
```


### [2026-09-14T01:28:14.273Z] TOOL RESULT

```
== page tags?
0
== find page 37 region (leaf) ==
‫من « 
16:                                   ‫لدابإاو ده‬

17: ‫من ‪0110‬م تفاح‬      ‫حت ابطالى �
18:                                 ‫‪0 0‬‬


          
19: ‫ينع فيمصر واللفظة مصرية ‪ .‬جا�
20:  ‫بير| ح ايطالى همءنط من المرماني
21:                               ‫ا‪4‬ع‪1‬د‪ #�
22:                                                             
23:                                      ‫« بيت ثور » 
24:                                ‫‪59‬‬   ‫‪9‬�
25:                              ‫اوج سد‬



          
26:                   ‫هفعناه عاموبراد به قا
27:                                           ‫د‬‫د‬
== grep سمن ==
1406:          ‫)موئاة متقصر‬   ‫( ون‬        ‫الاسفلج والسمنج ‪ 7‬وناني ‪5‬‬
```


## [2026-09-14T01:28:23.978Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84%DB%8C/",
 "prompt": "Quote the \"فرهنگ معین\" entry for شالی exactly, including the bracketed origin tag (e.g. [سنس.] for Sanskrit). Also quote Dehkhoda's etymology if present, and any entry for شالیزار."
}
```


## [2026-09-14T01:28:25.879Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D9%84%D8%AA%D9%88%DA%A9/",
 "prompt": "Quote the \"فرهنگ معین\" entry for شلتوک exactly with any bracketed origin tag, and Dehkhoda's note on its origin (Turkish چلتوک?)."
}
```


### [2026-09-14T01:28:28.393Z] TOOL RESULT

```
# Entries for شالی

## فرهنگ معین
"[ سنس . ] (اِ. ) برنجی که هنوز پوستش کنده نشده ."

## لغت نامه دهخدا (Etymology)
The Dehkhoda entry notes that in Sanskrit, شالی means "rice and similar grains" (درسانسکریت شالی بمعنی برنج و غلات مشابه آن است).

## شالیزار Entry
The Dehkhoda dictionary includes: "شالی زار را گویند که برنج زار باشد" — indicating this refers to a rice paddy or rice field.
```


### [2026-09-14T01:28:30.655Z] TOOL RESULT

```
# فرهنگ معین Entry for شلتوک

According to the Farhangs-e Moein dictionary:

**(شَ) (اِ.) برنجی که هنوز پوستش را نکنده باشند.**

This translates to: rice that has not yet had its husk removed.

## Dehkhoda's Note on Origin

The Dehkhoda dictionary entry begins with: **"شلتوک. [ ش َ ] ( اِ ) چلتوک"** — indicating an alternate form "چلتوک" (Cheltuk), suggesting a possible Turkish etymological connection, though the entry itself doesn't explicitly confirm Turkish origin but rather documents this variant spelling alongside the primary form.
```


## [2026-09-14T01:28:34.621Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%AC/",
 "prompt": "Quote the \"فرهنگ معین\" entry for ساج exactly, including the bracketed origin tag (e.g. [ع.] Arabic or [سنس.] Sanskrit), and its gloss (teak tree?). Also Dehkhoda's note on origin."
}
```


## [2026-09-14T01:28:35.565Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=salamander",
 "prompt": "Quote the American Heritage Dictionary etymology for salamander exactly."
}
```


### [2026-09-14T01:28:37.727Z] TOOL RESULT

```
According to the American Heritage Dictionary entry shown, the etymology for salamander is:

"[Middle English _salamandre_, from Old French, from Latin _salamandra_, from Greek.]"
```


### [2026-09-14T01:28:39.577Z] TOOL RESULT

```
# Farhangs entry for ساج

**Farhangs Moein entry:**
"(اِ. ) معرب ساک . ۱ - درختی است بلند با چوبی سیاه رنگ"
[A tall tree with black wood; derived from Sanskrit "sak"]

**Dehkhoda's origin note:**
Dehkhoda indicates the word is "معرب درخت ساگ است" (an Arabized form of the Sanskrit term "sag"), with the Hindi equivalent "ساکهو." He notes its use in shipbuilding due to the wood's durability and resistance to decay—notably appearing in the construction of Khosrow's buildings, which remain standing after centuries without deterioration.
```


## [2026-09-14T01:28:54.369Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=Scythian",
 "prompt": "Quote the American Heritage Dictionary entry and etymology for Scythian and Scythia exactly."
}
```


## [2026-09-14T01:28:55.909Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/sakah",
 "prompt": "Does this page exist? If so quote the Proto-Iranian reconstruction *sakah 'Saka, Scythian' and its descendants (Old Persian, Khotanese, Greek)."
}
```


### [2026-09-14T01:28:57.102Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:28:57.697Z] TOOL RESULT

```
# Scythian Dictionary Entry

Based on the provided content, here is the American Heritage Dictionary entry for Scythian:

**Entry Definition:**
"Of or relating to Scythia or its people, language, or culture" (adjective), and referring to either "a member of the ancient nomadic people inhabiting Scythia" or "the Iranian language of the Scythians" (noun).

**Important Note:**
The page does not include an etymology section for the word "Scythian" itself. While the content references the dictionary's Indo-European and Semitic Roots appendices, the specific etymological information for Scythian is not provided in this particular dictionary entry display.
```


## [2026-09-14T01:29:06.031Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/scythians",
 "prompt": "What does Encyclopaedia Iranica say about the names Scythian (Greek Skythai) and Saka — are they the same word or different ethnonyms? Quote any statement about Szemerenyi's etymology (*skuda- 'archer') and about Old Persian Saka."
}
```


## [2026-09-14T01:29:06.817Z] TOOL CALL #60: WebSearch

```json
{
 "query": "Szemerényi \"Four Old Iranian Ethnic Names\" Scythian *skuda archer Saka *sak- different names"
}
```


### [2026-09-14T01:29:07.278Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T01:29:13.886Z] TOOL RESULT

```
Web search results for query: "Szemerényi "Four Old Iranian Ethnic Names" Scythian *skuda archer Saka *sak- different names"

Links: [{"title":"Four Old Iranian Ethnic Names Scythian Skudra Sogdian Saka Oswald Szemerenyi : Oviya Dhingra : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/fouroldiranianethnicnamesscythianskudrasogdiansakaoswaldszemerenyi_164_r"},{"title":"Four Old Iranian Ethnic Names: Scythian - Skudra - Sogdian - Saka","url":"https://ocb.uni-tuebingen.de/Record/KEI00065190/Versions?print=1"},{"title":"Four Old Iranian ethnic names: Scythian, Skudra, Sogdian, Saka (Sitzungsberichte / Österreichische Akademie der Wissenschaften. Philosophisch-historische Klasse): 9783700103677 - AbeBooks","url":"https://www.abebooks.com/9783700103677/Four-Old-Iranian-ethnic-names-3700103670/plp"},{"title":"Oswald Szemerényi, Four Old Iranian Ethnic Names Scythian-Skudra-Sogdian-Saka (Book Review) - ProQuest","url":"https://www.proquest.com/openview/d977c722d08a123928ba80af54f07380/1?pq-origsite=gscholar&cbl=1817606"},{"title":"Four Old Iranian Ethnic Names: Scythian - Skudra - Sogdian - Saka by Oswald John Louis Szemerényi | Goodreads","url":"https://www.goodreads.com/book/show/40734913-four-old-iranian-ethnic-names"},{"title":"Szemerényi (Oswald). Four old Iranian ethnie Names : Scythian-Skiidra-Sogdian-Saka - Persée","url":"https://www.persee.fr/doc/rbph_0035-0818_1982_num_60_1_5848_t1_0197_0000_3"},{"title":"Four old Iranian ethnic names, Scythian, Skudra, Sogdian, Saka | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Four-old-Iranian-ethnic-names,-Scythian,-Skudra,-Szemer%C3%A9nyi/cb09cc5c0f39159884197daed7b0516fbfb94624"},{"title":"Four Old Iranian Ethnic Names: Scythian, Skudra, Sogdian, Saka - Oswald Szemerényi - Google Books","url":"https://books.google.com/books/about/Four_Old_Iranian_Ethnic_Names.html?id=Ti8KAQAAIAAJ"},{"title":"SCYTHIAN LANGUAGE - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/scythian-language/"},{"title":"The Saka Legacy in Ancient Iran – Dr. Kaveh Farrokh","url":"https://www.kavehfarrokh.com/ancient-prehistory-651-a-d/scythian/the-saka-legacy-in-ancient-iran/"}]

Based on the search results, I found information about Oswald Szemerényi's work on old Iranian ethnic names:

"Four Old Iranian Ethnic Names: Scythian - Skudra - Sogdian - Saka" is a work by Szemerényi, published in 1980. This work details an attempt to trace origins and meaning of ethnonyms of Achaemenid-era Northern Iranian tribes from Eurasian steppes.

Regarding the specific linguistic elements you mentioned, the search results provide some relevant information. Szemerényi proposes *Skuδa- as meaning "shooter, marksman", which relates to the archer connection implied by your query. In the Achaemenid royal inscriptions, Greek "Skýthai" is identified as an alloethnonym and not the self-designation of this people.

The work examines how different Iranian-speaking groups from antiquity were known by various names, including variations of Scythian (Saka), Skudra, and Sogdian forms, though the search results don't provide detailed information about the specific linguistic roots (*skuda*, *sak-*) and their relationship you're asking about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:29:20.399Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%B3%D8%AA%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%CE%A3%CE%BA%CF%8D%CE%B8%CE%B7%CF%82\" \\\n \"https://www.etymonline.com/word/Scythian\" \\\n \"https://en.wiktionary.org/wiki/Saka\" \\\n \"https://en.wiktionary.org/wiki/Scythian\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 429, roots Saka/Sali: Scythian-Saka ethnonyms, Sistan etymology\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:29:23.316Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b262fcb8e4ca8935.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65ee082330fa95eb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65da737ef6416688.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bbd8928464a0be7b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ce4163f725f667d.txt
```


## [2026-09-14T01:29:24.224Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/teak\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/salamander\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D9%86%D8%AF%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D9%84%D8%AA%D9%88%DA%A9\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 429: teak/saj, salamander/samandar, shali/shaltuk etymologies\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:29:27.629Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a127dde11d037f87.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ee458c3d953a52e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/141ecbe95398e6a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5fbe9de45e150d7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9358c146459180b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d76008222024735.txt
```


## [2026-09-14T01:29:34.060Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AF%D8%B1/\" \\\n \"https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84%DB%8C/\" \\\n \"https://abadis.ir/fatofa/%D8%B4%D9%84%D8%AA%D9%88%DA%A9/\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%AC/\" \\\n \"https://ahdictionary.com/word/search.html?q=salamander\" \\\n \"https://ahdictionary.com/word/search.html?q=Scythian\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 429: Mo'in/Dehkhoda entries and AHD etymologies\" 2>&1 | tail -2\ndone\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg429.png data/verification/sources/refs/ocr/BOOK/429.png\nls -la data/verification/sources/refs/ocr/BOOK/429.png"
}
```


### [2026-09-14T01:29:42.470Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9190b23e1de8b88c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/316d7b250b74861a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/655d2dd755ff6487.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16ebf5fa2724ad3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fc43f5585a22e2dd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0becd52601b4eb6f.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 78202 Sep 13 21:29 data/verification/sources/refs/ocr/BOOK/429.png
```


## [2026-09-14T01:29:51.610Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN samandar/salamander ===\"; grep -n -i \"samandar\\|salamander\\|salamandra\" HRN.txt | head -5\necho \"=== HRN sali/schali ===\"; grep -n -i \"šālī\\|salī\\|schali\\|Reis\" HRN.txt | head -8\necho \"=== HUB samandar ===\"; grep -n -i \"samandar\\|salamand\" HUB.txt | head -5\necho \"=== HRN saj/teak ===\"; grep -n -i \"\\bsag\\b\\|Teakholz\\|sadsch\" HRN.txt | head -5"
}
```


### [2026-09-14T01:29:51.715Z] TOOL RESULT

```
=== HRN samandar/salamander ===
=== HRN sali/schali ===
38:nerung an die lange Reise, die das Buch vom Verleger zu einer Bibliothek und weiter zu Ihnen hinter sich gebracht hat.
261:neupersischer Worte in den portugiesischen Reiseberichten
432:Preisaufgabe für das Jahr 1892/93 (nach den Zeitungsmitteilungen) *eine
778:aw. afrmami 'ich preise' etc., äfrlna- 'Segen'; phlv.
1041:aw. arejah- 'Preis, Wert'; phlv. arj^ arjniand;
1042:ai. vergl. arghd- 'Preis, Wert'.
2205:208. (i)&fr«tijf, gurinj (AM.) 'Reis'.
2479:'Kaufpreis, Wert*. Dazu gehören gr. wvog 'Kaufpreis,
=== HUB samandar ===
=== HRN saj/teak ===
6478:Herod. I, 110; aw. span- Hund'; phlv. aak^ sag; ai.
21277:t. rü/sag 610.
```


## [2026-09-14T01:29:53.321Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%85%D9%86%D8%AF%D9%84",
 "prompt": "Is there an Arabic entry سمندل (samandal)? Quote its meaning and etymology (from Persian samandar? from Greek salamandra?). Also note any Arabic سمندر."
}
```


### [2026-09-14T01:29:54.608Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T01:29:59.376Z] TOOL CALL #66: WebSearch

```json
{
 "query": "السمندل Arabic samandal salamander معرب سمندر Greek salamandra Arabic dictionary etymology"
}
```


### [2026-09-14T01:30:07.728Z] TOOL RESULT

```
Web search results for query: "السمندل Arabic samandal salamander معرب سمندر Greek salamandra Arabic dictionary etymology"

Links: [{"title":"سمندر - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D9%86%D8%AF%D8%B1"},{"title":"Salamander | Myth and Folklore Wiki | Fandom","url":"https://mythus.fandom.com/wiki/Salamander"},{"title":"Salamanders in folklore - Wikipedia","url":"https://en.wikipedia.org/wiki/Cultural_depictions_of_salamanders"},{"title":"Salamander - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/salamander"},{"title":"Salamander etymology in English","url":"https://cooljugator.com/etymology/en/salamander"},{"title":"salamander - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/salamander"},{"title":"salamander In Arabic - Translation and Meaning in English Arabic Dictionary of All terms Page 1","url":"https://www.almaany.com/en/dict/ar-en/salamander/"},{"title":"salamandra - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/salamandra"},{"title":"Salamander Definition & Meaning | YourDictionary","url":"https://www.yourdictionary.com/salamander"},{"title":"Salamanders in folklore","url":"https://en.wikipedia.org/wiki/Salamanders_in_folklore"}]

Based on the search results, here's information about the etymology of "salamander" and its Arabic variants:

## Arabic Terms

The salamander in Arabic is called سمندل (samandall) or سلمندر (salamandar).

## Etymology and Greek Origin

The Greek word σαλαμάνδρα (salamándra) is of uncertain origin, though it may be of Pre-Greek origin. The Greek term is possibly of Iranian origin.

## Arabic Connection to Greek

According to Dehkhoda, the Persian/Arabic word سمندر (samandar) is most likely derived from Ancient Greek σαλαμάνδρα (salamándra). However, the origin of the Greek term is uncertain, and there remains a small possibility that it may itself be from Persian.

## Folk Etymology Theory

There was a long-standing theory in Persian dictionaries that سمندر (samandar) is a compound of سام (sâm, "fire, flame") + اندر (andar, "inside"). This interpretation is semantically plausible given the ancient belief that the salamander can survive fire or even feeds on it.

## Historical Arabic Usage

Arab and Persian writers described the salamandar (written samandal or samandar) sometimes as a bird or phoenix, but also as a marten-like animal, said to yield cloth which can be laundered in fire.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:30:16.466Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Scythians",
 "prompt": "Quote the section on the name/etymology: Scythian self-designation *Skuδa- (Szemerényi 'archer/shooter'), Assyrian Iškuzaya, and the relation to Old Persian Sakā (is Saka a different name applied by Persians?)."
}
```


### [2026-09-14T01:30:22.613Z] TOOL RESULT

```
# Scythian Names and Etymology

## Self-Designation and Etymology

The Scythians' own name for themselves was *Skuδa*, which meant "archers" or "shooters." According to the Wikipedia article, this term "was derived from the Proto-Indo-European root *(s)kewd-, lit. 'shoot, throw'."

## Assyrian and Persian Designations

The Akkadian-speaking peoples of Mesopotamia referred to the Scythians using variants like *Iškuzāya*. 

Regarding Persian usage, the article clarifies an important distinction: "the ancient Persians used the name Saka to designate all the steppe nomads" and specifically called the Pontic Scythians *Sakā tayaiy paradraya* (meaning "the Saka who dwell beyond the (Black) Sea"). 

So yes—Saka was indeed a separate Persian designation. In modern scholarship, the term "Saka" specifically refers to "the Iranic pastoralist nomads who lived in the steppes of Central Asia and East Turkestan in the 1st millennium BC," distinguishing them from the Pontic Scythians proper.
```


## [2026-09-14T01:30:27.495Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Scythians\" --note \"page 429 root Saka: Scythian self-name *Skuda- vs Old Persian Saka as separate ethnonyms\" 2>&1 | tail -2\npython3 tools/fetch_source.py \"https://archive.org/details/fouroldiranianethnicnamesscythianskudrasogdiansakaoswaldszemerenyi_164_r\" --note \"page 429 root Saka: Szemerenyi 1980 Four Old Iranian Ethnic Names (Skudra vs Saka)\" 2>&1 | tail -2"
}
```


### [2026-09-14T01:30:30.721Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7ae55ed20c165b4a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/57e3d2c8f4f01a0a.txt
```


## [2026-09-14T01:30:49.155Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD Sagestan/Sakastan/sagzi ===\"; grep -n -o \".\\{0,80\\}Sagest\\|.\\{0,80\\}Sakast\\|.\\{0,60\\}sagzig\\|.\\{0,60\\}Sagzi\" PHD.txt PHD_mackenzie.txt | head -5\necho \"=== NYB Sakastan ===\"; grep -n -o \".\\{0,80\\}Sakast.\\{0,80\\}\\|.\\{0,80\\}Sagest.\\{0,80\\}\" NYB_vol2_glossary.txt | head -5\necho \"=== SKT Scythian ===\"; grep -n -i \"scythia\" SKT.txt | head -3\necho \"=== FSD vol4 Scythian ===\"; grep -n -i -m2 \"Scyth'i-an\\|Scythia\" FSD_vol4.txt | head -3"
}
```


### [2026-09-14T01:30:53.262Z] TOOL RESULT

```
=== PHD Sagestan/Sakastan/sagzi ===
=== NYB Sakastan ===
ugrep: error: error at position 161
f][\x80-\xbf]*){0,80}
                     \___exceeds complexity limits


=== SKT Scythian ===
610:paramour.  (K.  —  L.)  M.  K.pammour, With  li>ve  ;  orijj.  nn  adverb,  phrnw  —  V.  /ar tfurwi//-,  with  love  ;  where /wr  =  L>/Vr. Amaze ,-  sec  Maze. AmaEon.  a  female  warrior.  (Gk)  GV, Afia^wv.  one  ot  a  warlike  nation  of  women  in Scythia.  ^  To  account  for  the  luime,  the Greeks  Raid  that  these  women  cut  olt  the right  breail  to  slioot  belter ;  from  Gk,  a-, not :  and  t*a\us,  tlie  breast.  Obviously  an invciitioa
=== FSD vol4 Scythian ===
5088:Scyth'i-an,  a   Of  or  pertaimng  to  the  Scythians,  their country,  or  their  language  Scjth'lcL— Scythian  dis- ease, atrophy  of  the  generative  organs  of  man  resulting  In corresponding  change  of  manners  and  habits  and  often  In  a mental  perversion  called  S   Insanity,  In  which  the  patient assumes  feminine  ways  and  costume  — S.  lamb  (Bot), same  as  dabometz
5089:Scxth'l-au,  1   sifli'i-on,  2   sJtVi-an,  n   1.  One  of  the ancient  nomad  stock  (knowm  to  the  Greeks  as  Scolatt) dwelling  along  the  north  shore  of  the  Black  Sea,  in  a wider  sense,  a   member  of  an  unknown  people  northeast of  these,  extending  far  Into  Asia  "While  the  European Scythians  are  known  to  have  used  an  Indo-European  Idiom, tholr  race  Is  a   question  of  doubt  It  was  probably  Aryan with  a   strong  admixture  of  Mongol  blood  They  disappear from  history  about  100  B   C
```


## [2026-09-14T01:32:40.977Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM/PLA سمندل ===\"; grep -n \"سمندل\\|سمندر\" AFM_pages.txt incoming/PLA/PLA_pages.txt | head -5\necho \"=== LKT celtik/schaltuk ===\"; grep -n -i \"celtik\\|çeltik\\|schaltuk\\|saltuk\\|Reis'\" LKT.txt | head -8\necho \"=== TTS celtik ===\"; grep -n -i \"celtik\\|rice\" TTS.txt 2>/dev/null | head -5; ls | grep -i tts\necho \"=== LEW salamandra ===\"; grep -n -i \"salamandra\" LEW_1910.txt LAT.txt | head -5"
}
```


### [2026-09-14T01:32:41.107Z] TOOL RESULT

```
=== AFM/PLA سمندل ===
AFM_pages.txt:2410:قوم ان السمندر دابة نشبه الطيور»٠‏ ومن الفارمي مأخوذ الاراي ܣܠܡܢܕܪܐ
=== LKT celtik/schaltuk ===
279:[Stamm  ak  'weiß'  Vämbery  TktEtWb Nr.  5].  Die  ursprüngliche  Bedeutung ist  offenbar,  dem  finnischen  uko  'der Alte',  uha  'die  Alte'  entsprechend,  die- selbe wie  pers.  pir,  ar.  sai^,  also  'Alter, Greis'  gewesen ;  im  älteren  Osmanischen kommt  noch  ahy  als  Ehrentitel  für  Ge-
552:'Vater' ;  hieraus  rum.  baba  'Vater,  Greis', babacä,  babaie  'Vater',  babalic  'aller Mann'.  Ebenso  russ.  baba,  babai  'Groß- vater'. Im  Angloindischen  wird  das  tk. Wort  sowohl  von  Europäern  als  Ein- geboienen  als  Kosewort  für  Kinder  be- nutzt :  bäba  oder  im  Plural  bäbälög  [lög 'Leute'  im  Hind.].  [Bern  SlEtWb  36. Hobson-Jobson  42/43.
1217:'Kreis'  [vom  Vb.  dära  'rund  herum- gehen, umkreisen'],  tk.  da^ire;  hieraus rum.  daerea  'Trommel',  dairca  'Schellen- trommel'.
2099:'Tenne',  ebenso  tk.  harman  [Abbildung und  Beschreibung  s.  Globus  LXVIII, 60];  hieraus  rum.  arman  'dass.,  Ein- friedigung, Kreis',  bulg.  harman  'Tenne'.
2440:1023.  Ar.  kalam: 'Schreibfeder'  [aus  gr.  KÖXaiuoi;],  ebenso tk.  kalem;  hieraus  bulg.  kalem  'Rohr- feder', serb.  kalem  'dass.',  kalam  'Pfropf- reis'; rum.  calem  'Büro,  Schreibstube', calemgiü  'Schreiber'.  [Bern  SlEtWb  471 .
2606:Ein  Silber-  oder  Goldgewicht  von  '/400 Tulä;  über  tamul.  oder  konkani  käsu wurde  zunächst  pg.  caixa  'Münze  von 3  Reis'  [Constancio  Dicc  204  c]  und hieraus  engl,  cash,  Bezeichnung  für  jede kleine  Münze  in  verschiedenen  Teilen Ostasiens;  in  China  ist  seit  mehr  als zwei  Jahrtausenden  der  runde,  mit  einer zentralen  viereckigen  Durchbohrung  ver- sehene Käsch  typisch.  Über  seine  Ge- schichte vgl.  MÜLLER  in  MSOS  XXH, ostasiat.  Abtlg.  S.  10  ff.  Hobson-Jobson 167/168.
2773:'Miete,  Mietpreis'  [Vb.  karä  'mieten,  ver- mieten'] ;  hieraus  mit  ar.  Art.  und  Imäla [ä  >  e]  sp.  alquile,  alquiler,  pg.  alquile, alquiler  'Miete',  Vb.  sp.  pg.  alqutlar 'vermieten'  [pg.  nur  bei  Tieren  gesagt, sonst  alugar  <^  lat.  adlocare];  über  tk. kira  wurde  rum.  chiriä  'Miete',  chirigiü 'Fuhrmann',  bulg.  kirija  'Fuhrlohn, Fracht,  Miete',  kiradzija  'Fuhrmann, Mieter',  serb.  kirija  'Miete,  Fracht', kiridzija  'Fuhrmann'.  —  [ML  4692  sp. alqueire  gehört  nicht  hierher,  s.  hier Nr.  1174a.]  [DE  186.  Eguilaz  250. Bern  SlEtWb  505.
3290:'Befehl,  Erlaß",  plr.  maräsim;  hieraus sp.  kat.  orancel,  sp.  alancel,  pg.  aranzel 'Erlaß,  durch  den  der  Preis  einer  Ware festgesetzt  wird;  offizieller  Tarif;  Zoll- tarif.' [DE  l'J7.  Eguilaz  271/!27!2  (wo  als Grundwort  ar.  si'r,  plr.  as'är  'Preis' angegeben  wird).
=== TTS celtik ===
=== LEW salamandra ===
LAT.txt:7448:bolea: salamandra (Gloss.). Sans doute aot dtranger.
LAT.txt:57516:serenas} Pline, 10,188 salamandra magnis imbribus proueniens atque
```


## [2026-09-14T01:32:41.776Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=teak",
 "prompt": "Quote the American Heritage Dictionary etymology for teak exactly."
}
```


### [2026-09-14T01:32:43.851Z] TOOL RESULT

```
According to the American Heritage Dictionary, the etymology for teak is:

"[Portuguese _teca_, from Malayalam _tēkka_.]"
```


## [2026-09-14T01:32:50.971Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2404,2416p' AFM_pages.txt\necho \"=== LAT salamandra context ===\"; sed -n '57512,57520p' LAT.txt"
}
```


### [2026-09-14T01:32:51.043Z] TOOL RESULT

```
وسمندور وسمئدوك ܕܚܢܕ وسمّئدون وسامدئدل ܕܚܝܐܘܐ .ܙ › ܕܦ اقوآل ]܇
قال في البرهان القاطع : « سَمَنْدَر على وزن قلندر دابة قدر ܝ 3
5 ترجا 18( 5 9[ 5( 0 0 05344 39
106 من جلدها عراقيات ومناديل وما شاك ذلك 157 ܨܝ 3 :=<
ل 1 غنات بالصابون ٠‏ وذه|ب قوم الى ܕ ܒ الوزع ܗ من
جادها 5 ومن وبرها ثاب يلبسونبها في الايام المارة فلا يوثر يم 9705 1
قوم ان السمندر دابة نشبه الطيور»٠‏ ومن الفارمي مأخوذ الاراي ܣܠܡܢܕܪܐ
واليونالي 110 واللاتيني 646 ܙ | ܨ 1
والاتكايزى 5 ` وس على دلت اللعات الإخذى ٠‏ 11 ها قيل عن
السمتدل 0 فيه النار فلا اضل له وهو نوع من الحيوانات شّايه بالضفدع ܨ
طويل وذاف طويل ( راجع ل 0
+* ( سنهج ) الرجل أسرع وشدد في الحلف مشتق من سامه اي العهد
والخلف
=== LAT salamandra context ===
serSpud, -a, -un: serein (se dit du ciel, de 1' atmosph.br e, etc.J
puis s'emploie par image); serenum: temps ou ciel serein. Le sens
premier est "sec", cf.Pl., Me .877 hic fauonius est serenus, illic
auster imbricus} Vg.,. G.1,100 umida solstitia atque hiemes orate
serenas} Pline, 10,188 salamandra magnis imbribus proueniens atque
serenitate deficiens ;■ et Lucr. emploie seresco dans le sens de "se
stcher" par opposition k UuSsco, 1,306: denique fluctifrago suspensae
in litore uestes | uuescunt, eaedem dispansae in sole serescunt.
~ Anci en (Bnn.), usuel. Panroman, M.L.7843.1089 -
```


## [2026-09-14T01:40:25.245Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-429.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SAKA = \"https://en.wiktionary.org/wiki/Saka\"\nW_SCYTH = \"https://en.wiktionary.org/wiki/Scythian\"\nW_SKYTHES = \"https://en.wiktionary.org/wiki/%CE%A3%CE%BA%CF%8D%CE%B8%CE%B7%CF%82\"\nW_SISTAN = \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%B3%D8%AA%D8%A7%D9%86\"\nE_SCYTH = \"https://www.etymonline.com/word/Scythian\"\nWP_SCYTH = \"https://en.wikipedia.org/wiki/Scythians\"\nSZEM = \"https://archive.org/details/fouroldiranianethnicnamesscythianskudrasogdiansakaoswaldszemerenyi_164_r\"\nW_TEAK = \"https://en.wiktionary.org/wiki/teak\"\nW_SAJ = \"https://en.wiktionary.org/wiki/%D8%B3%D8%A7%D8%AC\"\nA_TEAK = \"https://ahdictionary.com/word/search.html?q=teak\"\nW_SALA = \"https://en.wiktionary.org/wiki/salamander\"\nW_SAMANDAR = \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D9%86%D8%AF%D8%B1\"\nA_SALA = \"https://ahdictionary.com/word/search.html?q=salamander\"\nA_SCYTH = \"https://ahdictionary.com/word/search.html?q=Scythian\"\nAB_SAMANDAR = \"https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AF%D8%B1/\"\nAB_SHALI = \"https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84%DB%8C/\"\nAB_SHALTUK = \"https://abadis.ir/fatofa/%D8%B4%D9%84%D8%AA%D9%88%DA%A9/\"\nAB_SAJ = \"https://abadis.ir/fatofa/%D8%B3%D8%A7%D8%AC/\"\nW_SHALI = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84%DB%8C\"\nW_SHALTUK = \"https://en.wiktionary.org/wiki/%D8%B4%D9%84%D8%AA%D9%88%DA%A9\"\n\nBQT_SAKA_NOTE = (\"BQT vol.2, Mo'in's footnote on سگستان (leaf 622 of BQT_v2_pages.txt, printed ~1158-1162): \"\n \"«پهلوی Sakastān … مرکب از Saka = نام قومی باستانی (+ ـستان پسوند مکان) … نام این قوم در کتیبهٔ بیستون Saka یاد شده. \"\n \"یونانیان این مردم را اسکوت Skythes می‌نامیدند … مقارن سلطنت فرهاد دوم اشکانی (۱۳۹–۱۲۸ ق.م.) و اردوان دوم (۱۲۷–۱۲۴ ق.م.) … \"\n \"سکه‌ها … دولت یونانی باختر (بلخ) را منقرض کردند و به طرف جنوب راندند … مستقر شدند، از این زمان زرنگ با نام سگستان \"\n \"(= سکستان، سکزستان، سیستان) معروف شد «ایران باستان ج۲ ص۳۸۵»؛ و نسبت بدان سگزی و معرّب آن سجزی است.»\")\n\nHUB_SAGZI = (\"Hübschmann, Persische Studien, p. ~127 (HUB.txt l.1574): «np. sagzi 'Sake' = arm. sagcik = phl. *sagčīk \"\n \"für *sak-čik von ap. Saka-» — sagzī built on OP Saka-.\")\nHUB_SISTAN = (\"Hübschmann, Persische Studien p. 129 (HUB.txt l.4485): «Sistan aus *Sigistan = arab. Sijistan, gr. \"\n \"Σεγεσταναων εθνος (Agathias), lat. Segestani (Ammian), arm. Sagastan, gr. Σακασταναη (Isidor Char.)».\")\nKNT_SAKA = (\"Kent, Old Persian, lexicon/ethnic list (KNT.txt l.1981): «Saka or fem. Sakā 'Scythia' or 'the Scythians'»; \"\n \"attested DNa/DPe/A?P: «iyam : Sakā : tigraxaud[ā] 'this is the Pointed-Cap Scythians'», «Sakā : haumavargā 'Amyrgian Scythians'», \"\n \"«Sakā : paradraya».\")\nBRT_SAKA = (\"Bartholomae, Altiran. Wb. (BRT.txt l.25898): «p. saka- Adj., bezeichnet ein Volk 'Sake, Skythe'» — filed as \"\n \"Old Persian (p. = altpersisch); there is no Avestan saka- entry.\")\n\nKLN_TEAK = (\"Klein p.1578 s.v. teak: «teak, n., an East Indian tree (Tectona grandis). — Port. teca, fr. Malayalam tekka, \"\n \"fr. OI. śākaḥ (whence also Arab. sāj)» (KLN_1966.txt l.38339).\")\nHJB_TEAK = (\"Hobson-Jobson p.910 s.v. TEAK: «The word is Malayal. tekka, Tam. tekku … The Skt. name of the tree is sāka, \"\n \"whence the modern Hind. name sāgwān or sāgun and the Mahr. sāg. From this last probably was taken sāj, the name of teak \"\n \"in Arabic and Persian» (HJB.txt ll.21812-21813).\")\nLKT_SAJ = (\"Lokotsch no. 1756 «Ar. sāg»: «'Holz von Tectonia grandis' [aus sskr. sāka, woraus andererseits malayāl. tekka, \"\n \"tamil. tekku wurde]; … aus der tam. Form wurde engl. teak … [Hobson-Jobson 910/911]» (LKT.txt l.3995) — also confirms \"\n \"that Nourai's HJB:910 is the right page.\")\nAID_SAG = (\"Whitworth, Anglo-Indian Dictionary s.v. Sāg: «Sāg. [Marāthi, from the Sanskrit sāka]. The tree tectona grandis, \"\n \"or teak» (AID.txt l.5933).\")\nSKT_TEAK = (\"Skeat: «Teak, a tree. (Malayalam.) Malayalam tēkka, the teak tree: Tamil tēkku, the same (H. H. Wilson)» \"\n \"(SKT.txt l.19249).\")\nSKT_SAL = (\"Skeat s.v. Salamander: «F. salamandre. — L. salamandra. — Gk. σαλαμάνδρα, a kind of lizard. Of Eastern origin; \"\n \"cf. Pers. samandar, a salamander» (SKT.txt l.16398).\")\nKLN_SAL = (\"Klein p.1374 s.v. salamander: «salamander, n. — ME. salamandre, fr. MF. (= F.) salamandre, fr. L. salamandra, \"\n \"fr. Gk. σαλαμάνδρα, which is of uncertain origin» (KLN_1966.txt l.33521).\")\nFSD_SAL = (\"Funk & Wagnalls, salamander (FSD_vol4.txt l.1059-1064, the sa-la- page = p.2161): «The salamanders were formerly \"\n \"fabled to live in and extinguish fire …», etymology bracket OCRed as «[ < F. sala[mandre] … Pers. samandar … salamandre, \"\n \"salamander]» — F&W does cite the Persian form beside the French/Latin/Greek chain.\")\nBQT_SAMANDAR = (\"BQT vol.2 (leaf 630 of BQT_v2_pages.txt, printed ~1166-1170), s.v. سمندر, Mo'in's footnote 8: \"\n \"«۸ - از یونانی salamandra. رک: سالامندرا؛ در فرانسوی نیز salamandre بمعنی فرشتهٔ موکل آتش و وینبهٔ کوهی و حیوان معروف \"\n \"است (از افادات علامه دهخدا). رک: سمندل.» The same page carries the Rūdakī verse Nourai prints: \"\n \"«باتش درون بر مثال سمندر — بآب اندرون بر مثال نهنگان» (لغت فرس ۵۳۱).\")\nBQT_SAM_FOLK = (\"Borhan's own text on the next page (leaf 631 = printed ~1171), s.v. سمندون: \"\n \"«واصل این لغت سام اندرون بوده یعنی در اندرون آتش» — the سام+اندرون folk etymology, which Dehkhoda (in Mo'in's footnote) rejects.\")\nAFM_SAM = (\"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt ll.2404-2412), s.v. السمندر: quotes Borhan \"\n \"(«قال في البرهان القاطع: سَمَنْدَر على وزن قلندر دابة …») and lists the Persian variants سمندور، سمندوک، سمندون، سالامندل, \"\n \"then states «ومن الفارسي مأخوذ الآرامي ܣܠܡܢܕܪܐ واليوناني … واللاتيني … والانكليزي …» — i.e. he makes the Greek/Latin/English \"\n \"forms come FROM the Persian, the reverse of Nourai's arrow.\")\nBQT_SHALI = (\"BQT vol.3, pdf page 20 = printed 1229 (incoming/BQT/BQT_v3_pages.txt l.1142), Mo'in's footnote 1 on شالی: \"\n \"«۱ - سانسکریت Shāli (برنج و غلات مشابه آن) «ویلیامز ۱:۱۰۹۸». در مازندران زراعت برنج را «شالی» گویند. «فرهنگ نظام».»\")\nBQT_SHALTUK = (\"BQT vol.3, pdf page 79 = printed ~1288 (l.5886), s.v. شلتوک: «شلتوک، با واو مجهول بروزن مفلوک، [برنجی] را \"\n \"گویند که هنوز از پوست بر نیاورده باشد و بهندی شالی خوانند.»\")\n\ndef nc(ref, status, note):\n    return {\"ref\": ref, \"status\": status, \"note\": note}\ndef cs(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\ndata = {\n \"pdf_page\": 429,\n \"book_page\": 399,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Saka\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Old Persian 𐎿𐎣𐎠 Sakā 'Scythians' (Old Iranian ethnonym), not a reconstructed Indo-European root\",\n   \"note\": (\"The name and gloss are right, the LANGUAGE LABEL is not: Sakā is an Old Iranian (specifically Old Persian) \"\n     \"ethnonym attested in Darius's inscriptions, not a Proto-Indo-European root; Nourai's own 'Indo-European' box is a \"\n     \"loose cover-label here. Bartholomae files saka- under Old Persian and knows no Avestan saka-. The whole entry \"\n     \"reproduces Mo'in's footnote to Borhan-e Qate' (BQT:1158) almost point for point, including the Greek equation and \"\n     \"the 130 B.C. date; where modern scholarship parts company with Mo'in is the Greek node (see node 3). \"\n     \"EXTRACTION NOTE: the printed Persian gloss column of node 2 reads «سکا ( سَکه ، ساک ، ساس ۱ )» — a variant list \"\n     \"ending in the footnote marker ۱; the JSON's script_extra «سکّه ، ساک ، ساسا» has swallowed that footnote digit into \"\n     \"«ساس» and gives سکه a shadda it does not have on the page. The three headwords themselves (سکا، سگزی، سیستان) are \"\n     \"extracted correctly.\"),\n   \"note_fa\": (\"«سَکا» نامِ قومی ایرانی‌تبار از کوچ‌نشینان استپ است و در سنگ‌نبشته‌های داریوش به‌صورت پارسی باستان Sakā \"\n     \"(سکاهای تیزخود، هومَ‌وَرگا و آن‌سوی دریا) آمده است؛ بنابراین برچسب «هندواروپایی» در کتاب نادرست است و باید «ایرانی \"\n     \"باستان / پارسی باستان» می‌بود. بارتولومه نیز saka- را ذیل پارسی باستان آورده و در اوستایی چنین واژه‌ای نیست. \"\n     \"معنایی که نورایی داده درست است و سراسر این مدخل بازتاب حاشیهٔ معین بر برهان قاطع (ص ۱۱۵۸) است. ادعای نورایی با \"\n     \"اصلاحِ برچسب زبان پذیرفتنی است.\"),\n   \"sources\": [W_SAKA, WP_SCYTH, SZEM, W_SISTAN],\n   \"ref_check\": [\n     nc(\"MON5:772\", \"not_checked\", \"Mo'in's vols 5-6 (اعلام, proper names) are not on disk and not online (vajehyab's Mo'in has no proper-name entries); page 772 of vol.5 could not be read.\"),\n     nc(\"BQT:1158\", \"supports\", BQT_SAKA_NOTE)\n   ],\n   \"consulted\": [\n     cs(\"KNT\", \"Old Persian, ethnic/place list §§ (KNT.txt l.1981, 824-828)\", \"supports\", KNT_SAKA),\n     cs(\"BRT\", \"Altiranisches Wörterbuch, s.v. saka- (BRT.txt l.25898)\", \"partial\", BRT_SAKA),\n     cs(\"HUB\", \"Persische Studien pp. ~127, 129\", \"supports\", HUB_SAGZI + \" \" + HUB_SISTAN)\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"saka 1; saka-stâna\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"OP Sakā (𐎿𐎣𐎠, sg./collective Saka) is well attested in the Achaemenid inscriptions as the cover-name \"\n       \"for the steppe nomads — DNa/DPe list Sakā tigraxaudā 'pointed-cap Sakas', Sakā haumavargā 'haoma-consuming Sakas', \"\n       \"Sakā tayaiy paradraya 'Sakas beyond the sea' (Kent, Old Persian, lexicon s.v. Saka-). Bartholomae records it as \"\n       \"Old Persian only; AVESTAN saka- does not exist, so the double label 'Avestan / Old Persian' is half wrong. \"\n       \"saka-stāna- 'land of the Sakas' (Saka- + -stāna- 'place', from PIE *steh₂- 'stand') is likewise NOT attested in \"\n       \"Old Persian: it is a post-Achaemenid, Arsacid-era formation, first visible in Greek Σακασταν(ή) in Isidore of \"\n       \"Charax, Armenian Sagastan, Latin Segestani (Ammianus), Middle Persian Sagestān. The historical statement is sound: \"\n       \"Saka tribes pushed south out of Bactria during the reigns of Phraates II (139-128 BCE) and Artabanus II (127-124 BCE) \"\n       \"and settled in Drangiana, which was renamed Sakastāna — Mo'in's footnote in Borhan gives exactly this, citing \"\n       \"Pirniya's Irān-e Bāstān II.385.\"),\n     \"derivation_fa\": (\"در پارسی باستان Sakā در کتیبه‌های داریوش (نقش رستم، پرسپولیس) نام کلّیِ کوچ‌نشینان استپ است: \"\n       \"Sakā tigraxaudā (تیزخود)، Sakā haumavargā و Sakā tayaiy paradraya. بارتولومه این واژه را تنها پارسی باستان می‌داند و \"\n       \"در اوستایی saka- وجود ندارد؛ پس برچسب «اوستایی/پارسی باستان» نیم‌درست است. Sakastāna نیز در پارسی باستان گواهی نشده \"\n       \"و ساختی متأخرتر (دورهٔ اشکانی) است، از saka- + پسوند مکانِ -stāna، که نخست در یونانیِ ایزیدور خاراکسی به‌صورت \"\n       \"Sakastanē و در ارمنی Sagastan و فارسی میانه Sagestān دیده می‌شود. آگاهی تاریخی نورایی (تاخت سکاها به جنوب در حدود \"\n       \"۱۳۰ پیش از میلاد) درست و برگرفته از حاشیهٔ معین بر برهان قاطع است. ادعا با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W_SAKA, W_SISTAN, WP_SCYTH],\n     \"ref_check\": [nc(\"BQT:1158\", \"supports\", BQT_SAKA_NOTE)],\n     \"consulted\": [\n       cs(\"KNT\", \"Old Persian, lexicon/ethnic list (KNT.txt ll.824-828, 1981, 2717)\", \"supports\", KNT_SAKA + \" Also DPh 5 «hacā Sakaibiš 'from the Scythians'».\"),\n       cs(\"BRT\", \"Altiran. Wb. s.v. saka- (BRT.txt l.25898)\", \"partial\", BRT_SAKA),\n       cs(\"PHD\", \"Concise Pahlavi Dictionary\", \"silent\", \"grep for Sagestān / Sakastān / sagzīg in PHD.txt and PHD_mackenzie.txt returns nothing; MacKenzie has sag 'dog' [KLBA] but no Sakastān entry.\")\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"sakâ «سکا»; sagzî «سگزی»; sîstân «سیستان»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three are right. (a) سکا is the modern Persian scholarly rendering of the ethnonym (Mo'in's own \"\n       \"spelling in the Borhan footnote). (b) سگزی 'of Sistan, Sakian' goes back through Middle Persian: Hübschmann, \"\n       \"Persische Studien, sets up phl. *sagčīk (= Armenian sagčik) from OP Saka- — Old Iranian intervocalic/post-vocalic \"\n       \"-k- voices to -g- in Middle Persian, and the denominal suffix -čī(k) yields NP -zī; the Arabicized doublet is سجزی \"\n       \"(Sijzī), the nisba of e.g. the 10th-c. mathematician al-Sijzī, which the chart's script_extra correctly records. \"\n       \"(c) سیستان < earlier سِجِستان (Arabic سَجِستان Sijistān) < MP Sagestān (skstʾn) < OP/Old Iranian *Sakastāna-; \"\n       \"the intervocalic -g- was lost and the resulting vowels contracted to ī (Sagistān > Sigistān > Sīstān), a change \"\n       \"Hübschmann treats explicitly on p.129 beside the Greek Σεγεσταναων and Latin Segestani. سگستان (the chart's variant) \"\n       \"is the regular Middle/Early New Persian form.\"),\n     \"derivation_fa\": (\"هر سه واژه درست است. «سگزی» از فارسی میانهٔ *sagčīk (ارمنی sagčik) از پارسی باستان Saka- است؛ \"\n       \"ک ایرانی باستان در فارسی میانه به گ نرم شده و پسوند نسبتِ ـچیک در فارسی نو به ـزی بدل گشته است (هوبشمان، مطالعات \"\n       \"پارسی). صورت معرّب آن «سجزی» است (نسبتِ ابوسعید سِجزیِ ریاضی‌دان). «سیستان» نیز از «سجستان» (معرّبِ Sagestān فارسی \"\n       \"میانه، خود از ایرانی باستان *Sakastāna-) است: گِ میانی افتاده و واکه‌ها به ای کشیده بدل شده‌اند \"\n       \"(Sagistān > Sigistān > Sīstān)؛ هوبشمان در ص ۱۲۹ همین را در کنار Σεγεσταναων یونانی و Segestani لاتینی آورده است. \"\n       \"«سگستان» هم صورت کهن‌تر همین نام است. ادعای نورایی درست است.\"),\n     \"sources\": [W_SISTAN, W_SAKA],\n     \"ref_check\": [\n       nc(\"BQT:1158\", \"supports\", BQT_SAKA_NOTE + \" The last clause «و نسبت بدان سگزی و معرّب آن سجزی است» is exactly Nourai's sagzī/سجزی.\"),\n       nc(\"MON5:772\", \"not_checked\", \"Mo'in vol.5 (اعلام) is neither on disk nor online; could not be read.\")\n     ],\n     \"consulted\": [\n       cs(\"HUB\", \"Persische Studien pp. ~127 and 129 (HUB.txt ll.1574, 4485)\", \"supports\", HUB_SAGZI + \" \" + HUB_SISTAN),\n       cs(\"BQT\", \"vol.2, Mo'in's footnote to سگستان (leaf 622)\", \"supports\", BQT_SAKA_NOTE),\n       cs(\"HRN\", \"Grundriss der neupersischen Etymologie\", \"silent\", \"grep of HRN.txt for Sagzi / Sigistan / Sijistan / Sedschestan returns nothing — Horn's Grundriss treats appellatives, not toponyms/ethnonyms.\"),\n       cs(\"PHD\", \"Concise Pahlavi Dictionary\", \"silent\", \"no Sagestān / sagzīg entry found in PHD.txt or PHD_mackenzie.txt.\")\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Greek\", \"words\": \"Scythe\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Two problems. (i) Form: the Greek word is Σκύθης Skýthēs (pl. Σκύθαι Skýthai); the printed 'Scythe' \"\n       \"is the French/English spelling, not a Greek form — Mo'in's footnote that Nourai is following actually writes both \"\n       \"(«یونانیان این مردم را اسکوت Skythes می‌نامیدند … در زبان فرانسوی «سیت» خوانده می‌شود»), and Nourai has taken the \"\n       \"French half. (ii) Derivation: modern scholarship does NOT derive Skýthēs from Saka. Greek Σκύθης is borrowed from \"\n       \"the Scythians' own name, Proto-Scythian *Skuδa- (Szemerényi 1980, 'Four Old Iranian Ethnic Names', from PIE \"\n       \"*(s)kewd- 'shoot' — 'archer, shooter'); the same name appears a century earlier in Assyrian as Iškuzāya/Ašgūzāya. \"\n       \"Old Persian Sakā is a separate, Persian-applied cover-name for all steppe nomads (Wikipedia/Iranica; Wiktionary \"\n       \"Σκύθης: «Borrowed from Proto-Scythian *Skuδi. Cognate with Akkadian Iškuzāya»). The two ethnonyms refer to \"\n       \"overlapping peoples but are not the same word, so the arrow Saka → Greek Skythes is a historical identification, \"\n       \"not an etymology.\"),\n     \"derivation_fa\": (\"دو اشکال هست. نخست صورت واژه: در یونانی Σκύθης (Skýthēs) است، و «Scythe» که کتاب چاپ کرده املای \"\n       \"فرانسوی/انگلیسی است؛ خودِ معین در حاشیهٔ برهان هر دو را آورده و نورایی نیمهٔ فرانسوی را برداشته است. دوم و مهم‌تر: \"\n       \"پژوهش امروزی Skýthēs را از Saka نمی‌گیرد. یونانیان این نام را از خودنامِ سکاییان یعنی *Skuδa- وام گرفته‌اند \"\n       \"(زمرنی ۱۹۸۰، از ریشهٔ هندواروپایی *(s)kewd- «تیر انداختن»، یعنی «کمان‌دار»)، همان نامی که یک سده پیش‌تر در \"\n       \"آشوری Iškuzāya آمده است؛ حال آنکه Sakā نامی است که پارسیان بر همهٔ کوچ‌نشینان استپ می‌نهادند. پس این پیکان \"\n       \"یک‌سان‌انگاریِ تاریخیِ دو قوم است، نه ریشه‌شناسی؛ پژوهش امروزی آن را رد می‌کند.\"),\n     \"sources\": [W_SKYTHES, WP_SCYTH, SZEM, E_SCYTH],\n     \"ref_check\": [\n       nc(\"BQT:1158\", \"partial\", BQT_SAKA_NOTE + \" Mo'in equates the peoples («یونانیان این مردم را اسکوت Skythes می‌نامیدند») but does not claim the Greek word is derived from Saka; and his Greek form is Skythes, not 'Scythe'.\"),\n       nc(\"MON5:772\", \"not_checked\", \"Mo'in vol.5 (اعلام) not available.\")\n     ],\n     \"consulted\": [\n       cs(\"KLN\", \"A Comprehensive Etym. Dict., s.v. Scythian (KLN_1966.txt l.34326)\", \"partial\", \"«Scythian, adj. and n. — Formed with suff. -an fr. L. Scythia, fr. Gk. Σκυθία, 'the country of the Scythians', fr. Σκύθης, 'a Scythian'» — Klein stops at Σκύθης and makes no Saka connection.\"),\n       cs(\"FSD\", \"Funk & Wagnalls s.v. Scythian (FSD_vol4.txt ll.5088-5089)\", \"partial\", \"«One of the ancient nomad stock (known to the Greeks as Scolati) dwelling along the north shore of the Black Sea …» — no Saka etymology given.\"),\n       cs(\"KNT\", \"Kent, Old Persian, introduction §III (KNT.txt l.335)\", \"partial\", \"«Scythian, the language or languages of the various tribes known in OP as Sakā» — Kent uses 'Scythian' as the English label for the Sakā, which is the identification Mo'in/Nourai rely on, not a word-derivation.\")\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"Scythia, Scythian\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"The Greek → English leg is uncontroversial: Gk. Σκύθης → Σκυθία 'land of the Scythians' → Latin \"\n       \"Scythia (Pliny, Mela) → English Scythia (14th c., in the Latin form) and Scythian = Scythia + the adjective suffix \"\n       \"-an (Klein: «Formed with suff. -an fr. L. Scythia, fr. Gk. Σκυθία … fr. Σκύθης»; Wiktionary s.v. Scythian: «From \"\n       \"Scythia + -an»). Only the upstream link (Saka → Greek) is in doubt, not this one.\"),\n     \"derivation_fa\": (\"این حلقه بی‌گفتگو درست است: یونانی Σκύθης ← Σκυθία «سرزمین سکوتیان» ← لاتینی Scythia ← انگلیسی \"\n       \"Scythia (سدهٔ چهاردهم) و Scythian = Scythia + پسوند صفت‌ساز -an (کلاین، ویکی‌واژه). تنها حلقهٔ پیشین (سکا ← یونانی) \"\n       \"محل تردید است، نه این یکی. ادعای نورایی در این بند درست است.\"),\n     \"sources\": [W_SCYTH, A_SCYTH, E_SCYTH],\n     \"ref_check\": [nc(\"AHD:1169\", \"partial\", \"The 1975 New College page 1169 is not accessible; the current online AHD entry for Scythian (ahdictionary.com/word/search.html?q=Scythian) gives the definitions ('a member of the ancient nomadic people inhabiting Scythia'; 'the Iranian language of the Scythians') but prints no etymology line, so it neither confirms nor denies Nourai's Greek source — Klein and Wiktionary supply it instead.\")],\n     \"consulted\": [\n       cs(\"KLN\", \"s.v. Scythian (KLN_1966.txt l.34326)\", \"supports\", \"«Formed with suff. -an fr. L. Scythia, fr. Gk. Σκυθία, 'the country of the Scythians', fr. Σκύθης, 'a Scythian'».\"),\n       cs(\"FSD\", \"s.v. Scythian (FSD_vol4.txt ll.5088-5089)\", \"supports\", \"«Scyth'i-an, a. Of or pertaining to the Scythians, their country, or their language»; the noun entry describes the Black-Sea nomads.\")\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Sakah\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit शाक śāka-ḥ 'vegetable, herb; the teak tree (Tectona grandis)'\",\n   \"note\": (\"The root is real: Skt. शाक śāka- is primarily 'vegetable, potherb' and secondarily the teak tree, and Klein \"\n     \"p.1578 — the very page Nourai cites — makes it the source of both the Arabic and the Malayalam words. Nourai's \"\n     \"spelling 'Sakah' is simply Klein's 'OI. śākaḥ' with the diacritics dropped. The one real error on this chart is the \"\n     \"language label of node 4, 'Malaysian' for Malayalam (see that node).\"),\n   \"note_fa\": (\"ریشهٔ سنسکریت شاک śāka- به‌معنی «سبزی، گیاه خوردنی» و نیز «درخت ساج» واقعی است و کلاین (ص ۱۵۷۸) — همان \"\n     \"صفحه‌ای که نورایی ارجاع داده — هم واژهٔ عربی و هم واژهٔ مالایالامی را از آن می‌گیرد. املای «Sakah» در کتاب همان \"\n     \"śākaḥ کلاین بدون علائم آوایی است. تنها خطای جدّی این نمودار برچسب زبانِ گرهِ چهارم است («مالزیایی» به‌جای «مالایالامی»).\"),\n   \"sources\": [W_SAJ, W_TEAK, A_TEAK],\n   \"ref_check\": [nc(\"KLN:1578\", \"supports\", KLN_TEAK)],\n   \"consulted\": [\n     cs(\"LKT\", \"Lokotsch no. 1756 (LKT.txt l.3995)\", \"supports\", LKT_SAJ),\n     cs(\"HJB\", \"Hobson-Jobson p.910 s.v. TEAK\", \"supports\", HJB_TEAK),\n     cs(\"AID\", \"Whitworth, Anglo-Indian Dict. s.v. Sāg (AID.txt l.5933)\", \"supports\", AID_SAG)\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Hindustani\", \"words\": \"sâgun\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Skt. śāka- passes into Middle Indo-Aryan as *sāga (regular MIA voicing of the intervocalic stop and \"\n       \"loss of the palatal ś > s), giving Hindi/Urdu सागौन sāgaun / sāgun and Marathi सागः sāg. Hobson-Jobson p.910 states \"\n       \"it in so many words: «The Skt. name of the tree is sāka, whence the modern Hind. name sāgwān or sāgun and the Mahr. \"\n       \"sāg.» The form sāgwān/sāgun is sāg extended by the Indic -vān/-un suffix. Whitworth's Anglo-Indian Dictionary \"\n       \"independently gives «Sāg. [Marāthi, from the Sanskrit sāka]».\"),\n     \"derivation_fa\": (\"سنسکریت śāka- در زبان‌های هندوآریاییِ میانه به *sāga بدل شده (ش سنسکریت به س، و واکدار شدن ک \"\n       \"میان‌واکه‌ای به گ) و از آن هندی/اردو sāgaun ~ sāgun و مراتی sāg پدید آمده است. «هابسن‌ـ‌جابسن» در ص ۹۱۰ همین را \"\n       \"می‌گوید و ویتورث نیز sāg مراتی را از śāka سنسکریت می‌داند. پسوند ـوان/ـون در sāgwān/sāgun پسوند هندی است. \"\n       \"ادعای نورایی درست است.\"),\n     \"sources\": [W_SAJ],\n     \"ref_check\": [nc(\"HJB:910\", \"supports\", HJB_TEAK + \" (Lokotsch's own reference «Hobson-Jobson 910/911» confirms that 910 is the TEAK page.)\")],\n     \"consulted\": [\n       cs(\"HJB\", \"p.910 s.v. TEAK\", \"supports\", HJB_TEAK),\n       cs(\"AID\", \"s.v. Sāg (AID.txt l.5933)\", \"supports\", AID_SAG),\n       cs(\"LKT\", \"no. 1756 (LKT.txt l.3995)\", \"supports\", LKT_SAJ)\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"sâj\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Arabic ساج sāj 'teak' is certainly the Indic word — Klein p.1578 says Skt. śākaḥ is the source \"\n       \"«whence also Arab. sāj», and Wiktionary's Arabic entry has «Ultimately from Sanskrit शाक (śāka)». Where Nourai \"\n       \"differs from his own source is the immediate donor: Hobson-Jobson derives the Arabic not from Hindustani sāgun but \"\n       \"from Marathi sāg — «From this last probably was taken sāj, the name of teak in Arabic and Persian» — the Konkan \"\n       \"coast being where Arab shipping loaded teak. Phonetically Indic -g is rendered by Arabic ج ǧ, as regularly in \"\n       \"Indo-Iranian loans (cf. Pers. bādingān > Ar. bādinǧān). The word is attested early and heavily: Ibn Khordadbeh \"\n       \"(c.880) «From Kol to Sindān, where they collect teak-wood (sāj)»; al-Masʿūdī (c.940) «The teak-tree (sāj)»; teak \"\n       \"beams of the 6th-c. Sasanian palace at Ctesiphon survive. Marked plausible only because the donor dialect is \"\n       \"Marathi/Konkani rather than the Hindustani form the chart draws.\"),\n     \"derivation_fa\": (\"«ساج» عربی بی‌گمان همان واژهٔ هندی است: کلاین (ص ۱۵۷۸) آن را از śākaḥ سنسکریت می‌گیرد و ویکی‌واژه \"\n       \"نیز «در نهایت از سنسکریت شاک». اختلاف نورایی با مأخذ خودش در واسطه است: «هابسن‌ـ‌جابسن» می‌گوید عربی ساج نه از \"\n       \"sāgun هندوستانی بلکه از sāg مراتی گرفته شده، چون بازرگانان عرب چوب ساج را از سواحل کنکان بار می‌زدند. از نظر آوایی \"\n       \"گِ هندی در عربی به ج بدل می‌شود (مانند بادنگان > باذنجان). این واژه از سدهٔ سوم هجری در ابن خردادبه و مسعودی گواهی \"\n       \"دارد و تیرهای ساجِ کاخ ساسانیِ تیسفون هنوز برجاست. ادعا با احتیاط پذیرفتنی است (واسطه مراتی است نه هندوستانی).\"),\n     \"sources\": [W_SAJ, AB_SAJ],\n     \"ref_check\": [\n       nc(\"HJB:910\", \"partial\", HJB_TEAK + \" Hobson-Jobson routes the Arabic through Marathi sāg, not through Hindustani sāgun as the chart's arrow does.\"),\n       nc(\"KLN:1578\", \"supports\", KLN_TEAK + \" — «(whence also Arab. sāj)» is exactly Nourai's Arabic node, though Klein hangs it directly on Sanskrit rather than on an Indic vernacular.\")\n     ],\n     \"consulted\": [\n       cs(\"LKT\", \"no. 1756 «Ar. sāg» (LKT.txt l.3995)\", \"supports\", LKT_SAJ),\n       cs(\"AFM\", \"Addi Shir, s.v. (الساج) (AFM_pages.txt l.2465)\", \"partial\", \"«(الساج) شجر يعظم جدًا قيل لا ينبت الا ببلاد الهند …» — Addi Shir lists ساج among the foreign words in Arabic and notes it grows only in India, but gives no Indic donor form.\"),\n       cs(\"PLA\", \"Asbaghi, Persische Lehnwörter im Arabischen\", \"silent\", \"grep of incoming/PLA/PLA_pages.txt for ساج / sāǧ / Teak / Tectona returns nothing — Asbaghi does not treat sāj as a Persian loan in Arabic, consistent with an Indic (not Iranian) source.\")\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"sâj «ساج»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian ساج sāj 'teak tree' is the Arabic form taken back into Persian — Mo'in's own entry tags it \"\n       \"«معرب ساک» ('Arabicized from sāk'), and Dehkhoda writes «معرب درخت ساگ است», adding the Hindi ساکهو. Hobson-Jobson \"\n       \"treats sāj as «the name of teak in Arabic and Persian» jointly. The ج of the Persian form is the giveaway: a word \"\n       \"reaching Persian directly from an Indic sāg/sāgun would keep گ, so the ج shows Arabic mediation, exactly as the \"\n       \"chart draws. (Note that Persian ساج 'iron griddle' is an unrelated Turkic word, sac.)\"),\n     \"derivation_fa\": (\"«ساج» فارسی همان صورت عربی است که دوباره به فارسی بازگشته: معین در مدخل خود آن را «معرّب ساک» \"\n       \"می‌داند و دهخدا می‌نویسد «معرّب درخت ساگ است» و صورت هندیِ «ساکهو» را می‌افزاید. گواه مسیرِ عربی، همان «ج» است: \"\n       \"اگر واژه یکراست از هندی sāg وارد فارسی می‌شد «گ» می‌ماند؛ پس معرّب‌شدن (گ ← ج) نشان می‌دهد که از راه عربی آمده است، \"\n       \"درست همان‌گونه که نورایی کشیده است. (ساجِ دیگر به‌معنی تابهٔ آهنی وام‌واژه‌ای ترکی است و ربطی به این ندارد.) \"\n       \"ادعای نورایی درست است.\"),\n     \"sources\": [AB_SAJ, W_SAJ],\n     \"ref_check\": [nc(\"MON:1783\", \"partial\", \"Mo'in's page 1783 itself could not be paged (the 6-vol Farhang is not online/on disk); the entry text is online at abadis.ir/fatofa/ساج: «(اِ.) معرب ساک. ۱ - درختی است بلند با چوبی سیاه رنگ …» — Mo'in derives it from Indic sāk via Arabicization, i.e. the same route as Nourai, so the content of the citation checks out even though the page number could not be verified.\")],\n     \"consulted\": [\n       cs(\"MON\", \"Farhang-e Fārsi s.v. ساج (via abadis.ir)\", \"supports\", \"«(اِ.) معرب ساک. ۱ - درختی است بلند با چوبی سیاه رنگ».\"),\n       cs(\"DKH/BQT\", \"Dehkhoda s.v. ساج (via abadis.ir, same page)\", \"supports\", \"«معرب درخت ساگ است» with the Hindi form ساکهو, and the note that its timber was used in Khosrow's buildings because it does not decay.\"),\n       cs(\"HJB\", \"p.910 s.v. TEAK\", \"supports\", \"«sāj, the name of teak in Arabic and Persian».\"),\n       cs(\"ARY\", \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\", \"silent\", \"grep of incoming/ARY/ARY_pages.txt for ساج finds only نساجی 'weaving' (l.5588), i.e. Aryanpur has no entry for the teak word — expected, since it is not Indo-European-Iranian inherited vocabulary.\")\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Malaysian\", \"words\": \"těkka\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Malaysian\",\n     \"correct_form\": \"Malayalam\",\n     \"derivation\": (\"The word is right, the language is not. Every source — including Nourai's own citation KLN:1578 — \"\n       \"says MALAYALAM (a Dravidian language of Kerala), not Malay/Malaysian: Klein «Port. teca, fr. Malayalam tekka, fr. \"\n       \"OI. śākaḥ»; Skeat «Teak, a tree. (Malayalam.) Malayalam tēkka … Tamil tēkku»; Hobson-Jobson «The word is Malayal. \"\n       \"tekka, Tam. tekku»; Lokotsch «malayāl. tekka, tamil. tekku»; the current AHD «[Portuguese teca, from Malayalam \"\n       \"tēkka.]». The printed page (pdf 429, image saved to data/verification/sources/refs/ocr/BOOK/429.png) plainly reads \"\n       \"'Malaysian', so this is Nourai's own slip, not a mis-extraction. A second, smaller reservation: Klein and Lokotsch \"\n       \"derive Malayalam tēkka from Sanskrit śāka, but Wiktionary treats തേക്ക് tēkkŭ / Tamil தேக்கு tēkku as native \"\n       \"Dravidian, so the root → node-4 arrow is itself only probable.\"),\n     \"derivation_fa\": (\"خودِ واژه درست است، امّا نام زبان نادرست: همهٔ مأخذها — از جمله همان کلاینِ ص ۱۵۷۸ که نورایی به آن \"\n       \"ارجاع داده — «مالایالامی» (زبانی دراویدی در کرالای هند) نوشته‌اند، نه «مالزیایی»: کلاین «Malayalam tekka»، اسکیت \"\n       \"«(Malayalam) tēkka … Tamil tēkku»، هابسن‌ـ‌جابسن، لوکوچ و فرهنگ American Heritage همگی همین را دارند. تصویر صفحهٔ \"\n       \"چاپی (ص ۴۲۹ پی‌دی‌اف) به‌روشنی «Malaysian» دارد؛ پس این خطای خودِ نورایی است، نه خطای خوانش اسکن. نکتهٔ دوم آنکه \"\n       \"برگرفتنِ tēkka مالایالامی از śāka سنسکریت رأیِ کلاین و لوکوچ است، ولی ویکی‌واژه آن را واژه‌ای بومیِ دراویدی \"\n       \"می‌داند؛ پس این پیکان نیز تنها «محتمل» است.\"),\n     \"sources\": [W_TEAK, A_TEAK],\n     \"ref_check\": [nc(\"KLN:1578\", \"contradicts\", KLN_TEAK + \" Klein says Malayalam, the chart says 'Malaysian'.\")],\n     \"consulted\": [\n       cs(\"SKT\", \"Skeat s.v. Teak (SKT.txt l.19249)\", \"contradicts\", SKT_TEAK),\n       cs(\"HJB\", \"p.910 s.v. TEAK\", \"contradicts\", \"«The word is Malayal. tekka, Tam. tekku» — and further «the Malay name is not Kiati but Jati», i.e. Hobson-Jobson explicitly says the Malay word for teak is jati, not tekka.\"),\n       cs(\"LKT\", \"no. 1756 (LKT.txt l.3995)\", \"contradicts\", LKT_SAJ + \" — «malayāl. tekka, tamil. tekku».\"),\n       cs(\"AHD\", \"current online AHD s.v. teak\", \"contradicts\", \"«[Portuguese teca, from Malayalam tēkka.]»\")\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Portuguese\", \"words\": \"teca\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"The Portuguese took the Malabar word directly after Vasco da Gama's landfall at Calicut (1498): \"\n       \"Malayalam tēkka(ŭ) → Port. teca, the Portuguese spelling with -c- rendering the Dravidian retroflex/geminate -kk-. \"\n       \"It is in use in Portuguese sources by the early 17th c. — Hobson-Jobson quotes Sousa, Oriente Conquistado, on the \"\n       \"year 1602: «it was taken in solemn procession and deposited in a box of teak (teca), which is a wood not subject to \"\n       \"decay». Klein and AHD both make Port. teca the immediate source of English teak.\"),\n     \"derivation_fa\": (\"پرتغالی‌ها پس از رسیدن واسکو دوگاما به کالیکوت (۱۴۹۸ م.) واژه را یکراست از ساحل مالابار گرفتند: \"\n       \"مالایالامی tēkka ← پرتغالی teca، که در آن -c- همان ـکّ دراویدی را می‌نمایاند. این واژه از آغاز سدهٔ هفدهم در متون \"\n       \"پرتغالی به‌کار رفته است؛ هابسن‌ـ‌جابسن از «اورینته کونکیستادو» (رویداد ۱۶۰۲) نقل می‌کند: «در صندوقی از چوب ساج \"\n       \"(teca) نهادند که چوبی است پوسیدنی‌ناپذیر». کلاین و AHD هر دو teca پرتغالی را خاستگاه بی‌واسطهٔ teak انگلیسی \"\n       \"می‌دانند. ادعای نورایی درست است.\"),\n     \"sources\": [W_TEAK, A_TEAK],\n     \"ref_check\": [nc(\"(none cited)\", \"not_checked\", \"The book prints no reference for this node; the chain is covered by the adjacent KLN:1578 and AHD citations.\")],\n     \"consulted\": [\n       cs(\"KLN\", \"p.1578 s.v. teak\", \"supports\", KLN_TEAK),\n       cs(\"HJB\", \"p.911, the 1602 quotation\", \"supports\", \"«deposited in a box of teak (teca), which is a wood not subject to decay» — Sousa, Oriente Conquistado (1710), ii.265, s.a. 1602 (HJB.txt l.21831).\"),\n       cs(\"AHD\", \"current online AHD s.v. teak\", \"supports\", \"«[Portuguese teca, from Malayalam tēkka.]»\")\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"teak\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English teak is borrowed from Portuguese teca in the late 17th c. (Anglo-Indian trade usage; \"\n       \"Hobson-Jobson's earliest English quotations for the timber trade are 18th-c., e.g. the 1791 Calcutta advertisement \"\n       \"«Teak Timber for sale»). AHD: «[Portuguese teca, from Malayalam tēkka.]»; Klein p.1578 gives the same chain and adds \"\n       \"that German Tiekbaum is in turn an English loanword. The botanical genus name Tectona and the trade term \"\n       \"'lignum sagalinum' are learned formations on the same word (Lokotsch).\"),\n     \"derivation_fa\": (\"انگلیسی teak در اواخر سدهٔ هفدهم میلادی از teca پرتغالی وام گرفته شده و از راه بازرگانی \"\n       \"هندـ‌انگلیسی رواج یافته است (کهن‌ترین شاهدهای هابسن‌ـ‌جابسن در تجارت چوب از سدهٔ هجدهم است، مانند آگهی ۱۷۹۱ \"\n       \"کلکته: «Teak Timber for sale»). فرهنگ American Heritage: «از پرتغالی teca، از مالایالامی tēkka»؛ کلاین همین \"\n       \"زنجیره را دارد و می‌افزاید که Tiekbaum آلمانی خود وام‌واژه‌ای از انگلیسی است. نام جنس گیاه‌شناسیِ Tectona نیز \"\n       \"ساختی دانشورانه بر همین واژه است (لوکوچ). ادعای نورایی درست است.\"),\n     \"sources\": [W_TEAK, A_TEAK],\n     \"ref_check\": [nc(\"AHD\", \"supports\", \"The current online AHD (ahdictionary.com/word/search.html?q=teak) gives «[Portuguese teca, from Malayalam tēkka.]», i.e. exactly the Portuguese → English leg Nourai draws (and, again, Malayalam not Malaysian).\")],\n     \"consulted\": [\n       cs(\"KLN\", \"p.1578 s.v. teak\", \"supports\", KLN_TEAK),\n       cs(\"SKT\", \"s.v. Teak (SKT.txt l.19249)\", \"partial\", SKT_TEAK + \" — Skeat names Malayalam/Tamil as the source but omits the Portuguese intermediary.\"),\n       cs(\"LKT\", \"no. 1756 (LKT.txt l.3995)\", \"partial\", \"«aus der tam. Form wurde engl. teak, dtsch. Teckholz und der botanische Name Tectonia» — Lokotsch derives English teak from the Tamil rather than the Malayalam form.\")\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Salamandra\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Ancient Greek σαλαμάνδρα salamándra 'salamander', itself of unknown (probably Pre-Greek, possibly Iranian) origin\",\n   \"note\": (\"The Greek word and its gloss are correct, and it is the historically demonstrable ancestor of the Latin, \"\n     \"French and English forms. What the box hides is that σαλαμάνδρα has no Greek etymology: Klein calls it «of uncertain \"\n     \"origin», Beekes files it as Pre-Greek, and Skeat (and Funk & Wagnalls, Nourai's FSD:2161) call it «of Eastern origin; \"\n     \"cf. Pers. samandar». So making Greek the head of the tree, with Persian and Arabic hanging off it, states one of two \"\n     \"live hypotheses as fact — Addi Shir (AFM) argues the exact reverse, that the Greek, Latin, Aramaic and English forms \"\n     \"all come from the Persian.\"),\n   \"note_fa\": (\"واژهٔ یونانی σαλαμάνδρα و معنای آن درست است و بی‌گمان نیای صورت‌های لاتینی و فرانسوی و انگلیسی است؛ امّا \"\n     \"این واژه در خودِ یونانی ریشه‌شناسی ندارد: کلاین آن را «با خاستگاه نامعلوم»، بیکس آن را پیش‌یونانی و اسکیت و فرهنگ \"\n     \"فانک‌ و ‌واگنالز (همان FSD:2161 نورایی) آن را «شرقی‌تبار، قس. سمندرِ فارسی» می‌دانند. پس نشاندنِ یونانی در رأس \"\n     \"درخت و آویختنِ فارسی و عربی از آن، یکی از دو فرضیهٔ زنده را قطعی جلوه می‌دهد؛ ادّی شیر درست وارونهٔ آن را می‌گوید. \"\n     \"با احتیاط پذیرفتنی است.\"),\n   \"sources\": [W_SALA, A_SALA, W_SAMANDAR],\n   \"ref_check\": [\n     nc(\"FSD:2161\", \"supports\", FSD_SAL),\n     nc(\"AHD:1144\", \"partial\", \"The 1975 New College page 1144 is not accessible; the current online AHD s.v. salamander prints «[Middle English salamandre, from Old French, from Latin salamandra, from Greek.]» — it supports the Greek → Latin → French → English chain but says nothing about Persian or Arabic.\")\n   ],\n   \"consulted\": [\n     cs(\"KLN\", \"p.1374 s.v. salamander (KLN_1966.txt l.33521)\", \"partial\", KLN_SAL + \" — Klein confirms the Greek word but explicitly declines to give it an origin.\"),\n     cs(\"SKT\", \"s.v. Salamander (SKT.txt l.16398)\", \"partial\", SKT_SAL),\n     cs(\"LAT\", \"Ernout-Meillet (LAT.txt ll.7448, 57516)\", \"partial\", \"salamandra appears only as a borrowed word in Latin (Pliny 10,188 «salamandra magnis imbribus proueniens»; the gloss «bolea: salamandra … Sans doute mot étranger») — no Latin etymology.\")\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"samandar «سمندر»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Persian سمندر samandar, the fire-dwelling creature of Persian lore, is attested by the 10th c. — the \"\n       \"Rūdakī line Nourai prints («به آتش درون بر مثال سمندر / به آب اندرون بر مثال نهنگان», via Asadi's Loghat-e Fors 531) \"\n       \"is the standard early citation, and Nourai plainly took it, and the variants سالامندر / سمندور, straight from \"\n       \"Borhan-e Qate'. Borhan's own text explains the word as «سام اندرون» 'inside the fire' (sām 'fire' + andarūn), which \"\n       \"Mo'in's footnote — reporting Dehkhoda — rejects and replaces with «از یونانی salamandra», exactly Nourai's arrow. \"\n       \"Phonetically Greek salamándra → Persian samandar requires loss of the first -la- (haplology in sala-man- > sa-man-) \"\n       \"and the regular reduction of the final -ra to -ar, which Dehkhoda's folk-etymological rival, سام‌اندر(ون), plausibly \"\n       \"helped along. Plausible rather than confirmed because the direction of borrowing is not settled: since the Greek \"\n       \"word itself has no Greek etymology, Skeat and Funk & Wagnalls call it 'Eastern' and Addi Shir derives the Greek \"\n       \"from the Persian; Wiktionary concedes «there remains a small possibility that it may itself be from Persian».\"),\n     \"derivation_fa\": (\"«سمندر» جانور افسانه‌ایِ آتش‌زی در ادب فارسی از سدهٔ چهارم هجری گواهی دارد؛ بیت رودکی که نورایی \"\n       \"آورده («به آتش درون بر مثال سمندر ـ به آب اندرون بر مثال نهنگان»، لغت فرس ص ۵۳۱) و گونه‌های «سالامندر» و «سمندور» \"\n       \"همگی یکراست از برهان قاطع گرفته شده‌اند. متنِ برهان خودِ واژه را «سام‌اندرون» یعنی «در میان آتش» می‌داند، ولی \"\n       \"حاشیهٔ معین به نقل از دهخدا این را ریشه‌شناسی عامیانه می‌شمارد و می‌نویسد «از یونانی salamandra» — همان چیزی که \"\n       \"نورایی کشیده است. از نظر آوایی salamándra ← سمندر مستلزم افتادنِ هجای ـلاـ (هم‌گون‌زدایی/حذف در sala-man- > sa-man-) \"\n       \"و کوتاه شدنِ ـرا به ـر است، و همان ریشه‌شناسی عامیانهٔ «سام‌اندر» احتمالاً به این دگرگونی کمک کرده است. چرا «با \"\n       \"احتیاط»؟ چون سویِ وام‌گیری قطعی نیست: خودِ واژهٔ یونانی ریشه‌شناسی یونانی ندارد، اسکیت و فانک‌ و ‌واگنالز آن را \"\n       \"«شرقی» می‌خوانند و ادّی شیر یونانی را از فارسی می‌گیرد.\"),\n     \"sources\": [W_SAMANDAR, AB_SAMANDAR, W_SALA],\n     \"ref_check\": [\n       nc(\"FSD:2161\", \"partial\", FSD_SAL + \" F&W cites the Persian form but as a comparandum, not as a derivative of the Greek.\"),\n       nc(\"BQT:1166\", \"supports\", BQT_SAMANDAR + \" \" + BQT_SAM_FOLK + \" (My leaf→page mapping for BQT vol.2 puts the سمندر page at ~1170; the entry, the footnote and the Rūdakī verse Nourai reproduces are all there, so the citation is substantively right even if the printed number is a few pages off.)\"),\n       nc(\"MON:1921\", \"partial\", \"Mo'in's page 1921 could not be paged (6-vol Farhang not online/on disk); the entry text at abadis.ir/fatofa/سمندر reads «(سَ مَ دَ) (اِ.) جانوری دوزیست شبیه سوسمار، چهارپا دارد و رنگ پوستش تیره است با لکه‌های زرد» — gloss only, no origin tag, so Mo'in's dictionary does not itself state the Greek source (his Borhan footnote does).\")\n     ],\n     \"consulted\": [\n       cs(\"BQT\", \"vol.2, s.v. سمندر + سمندون, with Mo'in's footnote 8\", \"supports\", BQT_SAMANDAR + \" \" + BQT_SAM_FOLK),\n       cs(\"MON\", \"Farhang-e Fārsi s.v. سمندر + Dehkhoda, via abadis.ir\", \"supports\", \"Dehkhoda: «از یونانی «سالامندرا»، در فرانسوی نیز «سالامندر» به معنی فرشته موکل آتش».\"),\n       cs(\"SKT\", \"s.v. Salamander (SKT.txt l.16398)\", \"contradicts\", SKT_SAL + \" — Skeat points the comparison the other way, calling the Greek word 'of Eastern origin'.\"),\n       cs(\"AFM\", \"Addi Shir s.v. السمندر (AFM_pages.txt ll.2404-2412)\", \"contradicts\", AFM_SAM),\n       cs(\"HRN\", \"Grundriss der neupersischen Etymologie\", \"silent\", \"grep of HRN.txt for samandar / salamand returns nothing; Horn does not treat the word.\"),\n       cs(\"HUB\", \"Persische Studien\", \"silent\", \"grep of HUB.txt for samandar / salamand returns nothing.\")\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"samandar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Arabic has the word chiefly as السَّمَنْدَل al-samandal (also السمندر), the fire-proof beast — or, in \"\n       \"some authors, fire-bird — whose skin yields the cloth that is cleaned by being thrown into the fire (the asbestos \"\n       \"story). Addi Shir's article on السمندر quotes Borhan-e Qate' and lists the Persian variants سمندور، سمندوک، سمندون، \"\n       \"سالامندل, then says «ومن الفارسي مأخوذ الآرامي ܣܠܡܢܕܪܐ واليوناني … واللاتيني … والانكليزي» — that is, he treats the \"\n       \"Arabic as Persian and makes the western forms derive from the Persian too. That is the likelier route for the \"\n       \"Arabic: a direct Greek → Arabic borrowing should have kept the -l- (as in the translators' سلمندرا), whereas \"\n       \"samandal/samandar matches the Persian shape. Nourai's arrow (straight from the Greek root) is therefore possible \"\n       \"but not the best-supported path.\"),\n     \"derivation_fa\": (\"در عربی این واژه بیشتر به‌صورت «السَّمَنْدَل» (و نیز السمندر) آمده است: جانور (یا در برخی مؤلفان \"\n       \"مرغِ) آتش‌زی که از پوست و کرک او پارچه‌ای می‌بافند که به‌جای شستن در آتش می‌افکنند (همان داستان پنبهٔ کوهی/آزبست). \"\n       \"ادّی شیر در مدخل «السمندر» از برهان قاطع نقل می‌کند، گونه‌های فارسی سمندور، سمندوک، سمندون و سالامندل را برمی‌شمارد \"\n       \"و سپس می‌نویسد «ومن الفارسي مأخوذ الآرامي ܣܠܡܢܕܪܐ واليوناني … واللاتيني …». همین مسیر (فارسی ← عربی) محتمل‌تر است، \"\n       \"زیرا وام‌گیریِ مستقیم از یونانی باید «ل» را نگاه می‌داشت (چنان‌که در «سلمندرا»ی مترجمان)، حال آنکه samandal/samandar \"\n       \"دقیقاً قالب فارسی است. پس پیکان نورایی (یکراست از یونانی) شدنی است ولی بهترین مسیر نیست.\"),\n     \"sources\": [W_SAMANDAR, W_SALA],\n     \"ref_check\": [nc(\"TAD:37\", \"not_found\", \"Tobia al-Unaysi, Tafsīr al-alfāẓ al-dakhīla — the local OCR (refs/TAD.txt, TAD_pages.txt, ~3300 lines) is of very poor quality and contains no سمندر/سمندل/سلمندر string at all; page 37 could not be located in it (refs_online.json already records that al-Unaysi's Table IV was lost in the OCR).\")],\n     \"consulted\": [\n       cs(\"AFM\", \"Addi Shir s.v. السمندر (AFM_pages.txt ll.2404-2412)\", \"contradicts\", AFM_SAM + \" Addi Shir makes the Arabic Persian, and the Greek derivative of the Persian — the opposite of the chart's Greek → Arabic arrow.\"),\n       cs(\"BQT\", \"vol.2, s.v. سمندل / سمندور / سمندول / سمندون (leaf 631)\", \"partial\", \"Borhan lists the whole Persian family «سمندل … بمعنی سمندر است که جانور آتشی باشد», which is the shape the Arabic word has (samandal), supporting a Persian rather than a direct Greek source.\"),\n       cs(\"PLA\", \"Asbaghi, Persische Lehnwörter im Arabischen\", \"silent\", \"grep of incoming/PLA/PLA_pages.txt for سمندر/سمندل returns nothing — Asbaghi has no article on it.\")\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Latin\", \"words\": \"salamandra\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin salamandra is a straight borrowing of Greek σαλαμάνδρα, taken over unchanged (first declension, \"\n       \"nom. sg. -a) in the technical/natural-history vocabulary: Pliny, Naturalis Historia 10,188 «salamandra magnis \"\n       \"imbribus proueniens atque serenitate deficiens», and 29,74 on the fire legend. Ernout-Meillet treat it as a \"\n       \"loanword with no Latin etymology; Klein p.1374 gives «L. salamandra, fr. Gk. σαλαμάνδρα».\"),\n     \"derivation_fa\": (\"salamandra لاتینی وام‌واژه‌ای است مستقیم از σαλαμάνδρα یونانی، بی هیچ دگرگونی و در صرف نخست \"\n       \"(نهادیِ مفرد ـa)، که در واژگان طبیعی‌نگاری راه یافته است: پلینیوس در «تاریخ طبیعی» ۱۰٬۱۸۸ و ۲۹٬۷۴ آن را به‌کار \"\n       \"برده است. ارنو و مه‌یه آن را وام‌واژه و بی‌ریشهٔ لاتینی می‌دانند و کلاین (ص ۱۳۷۴) همین زنجیره را دارد. ادعای \"\n       \"نورایی درست است.\"),\n     \"sources\": [A_SALA, W_SALA],\n     \"ref_check\": [\n       nc(\"AHD\", \"supports\", \"Current online AHD s.v. salamander: «[Middle English salamandre, from Old French, from Latin salamandra, from Greek.]»\"),\n       nc(\"KLN:1374\", \"supports\", KLN_SAL)\n     ],\n     \"consulted\": [\n       cs(\"KLN\", \"p.1374 s.v. salamander\", \"supports\", KLN_SAL),\n       cs(\"LAT\", \"Ernout-Meillet (LAT.txt ll.7448, 57516)\", \"supports\", \"Latin salamandra cited from Pliny 10,188; the glossary equation «bolea: salamandra (Gloss.). Sans doute mot étranger» confirms it is felt as a foreign word in Latin.\"),\n       cs(\"SKT\", \"s.v. Salamander\", \"supports\", \"«F. salamandre. — L. salamandra. — Gk. σαλαμάνδρα».\")\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"French\", \"words\": \"salamandre\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Old/Middle French salamandre is the learned (semi-learned) continuation of Latin salamandra, with the \"\n       \"regular French treatment of Latin final -a > -e; it is attested from the 12th-13th c. in the bestiaries and became \"\n       \"a heraldic and alchemical emblem (François I's device). Klein p.1374 routes English through «MF. (= F.) \"\n       \"salamandre», and Skeat gives «F. salamandre. — L. salamandra».\"),\n     \"derivation_fa\": (\"salamandre فرانسوی دنبالهٔ (نیمه‌)دانشورانهٔ salamandra لاتینی است با تبدیل عادیِ ـa پایانیِ \"\n       \"لاتینی به ـe فرانسوی؛ از سدهٔ دوازدهم‌ـ‌سیزدهم میلادی در «بستیاری‌ها» گواهی دارد و بعدها نشانِ نمادینِ فرانسوای \"\n       \"اوّل و کیمیاگران شد. کلاین (ص ۱۳۷۴) گذر واژهٔ انگلیسی را از همین صورت فرانسوی می‌داند و اسکیت نیز «F. salamandre \"\n       \"— L. salamandra» دارد. ادعای نورایی درست است.\"),\n     \"sources\": [A_SALA, W_SALA],\n     \"ref_check\": [nc(\"AHD\", \"supports\", \"Current online AHD s.v. salamander: «[Middle English salamandre, from Old French, from Latin salamandra, from Greek.]» — the Old French stage is explicit.\")],\n     \"consulted\": [\n       cs(\"KLN\", \"p.1374 s.v. salamander\", \"supports\", KLN_SAL),\n       cs(\"SKT\", \"s.v. Salamander (SKT.txt l.16398)\", \"supports\", \"«F. salamandre. — L. salamandra».\"),\n       cs(\"FSD\", \"s.v. salamander (FSD_vol4.txt l.1064)\", \"supports\", FSD_SAL)\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"salamander\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle English salamandre (c.1340, Ayenbite; common in the 14th-c. bestiary and encyclopaedic \"\n       \"literature) borrowed from Anglo-Norman/Old French salamandre, with the modern -er spelling generalised from the \"\n       \"16th c. by analogy with the English agent suffix. The fire legend travelled with the word, whence the technical \"\n       \"senses Funk & Wagnalls lists — a fire-spirit, a person who can stand great heat, a metal plate for browning food, \"\n       \"and the mass of slag left in a blast furnace. AHD: «[Middle English salamandre, from Old French, from Latin \"\n       \"salamandra, from Greek.]»\"),\n     \"derivation_fa\": (\"انگلیسی میانه salamandre (نزدیک ۱۳۴۰ م.) از فرانسویِ انگلوـ‌نورمان salamandre وام گرفته شده و \"\n       \"املای امروزیِ ـer از سدهٔ شانزدهم به قیاسِ پسوند فاعلیِ انگلیسی عمومیت یافته است. افسانهٔ آتش‌زیستی نیز همراه واژه \"\n       \"رفته و معناهای فنیِ آن را پدید آورده است (روحِ آتش، کسی که تابِ گرمای سخت دارد، ورقهٔ فلزیِ برشته‌کردن، و تفالهٔ \"\n       \"مانده در کورهٔ بلند) که فانک‌ و ‌واگنالز برمی‌شمارد. فرهنگ American Heritage همین زنجیره را دارد. ادعای نورایی \"\n       \"درست است.\"),\n     \"sources\": [W_SALA, A_SALA],\n     \"ref_check\": [\n       nc(\"AHD\", \"supports\", \"Current online AHD s.v. salamander: «[Middle English salamandre, from Old French, from Latin salamandra, from Greek.]»\"),\n       nc(\"FSD:2161\", \"supports\", FSD_SAL)\n     ],\n     \"consulted\": [\n       cs(\"KLN\", \"p.1374 s.v. salamander\", \"supports\", KLN_SAL),\n       cs(\"SKT\", \"s.v. Salamander\", \"supports\", \"«Salamander, a reptile. (F.-L.-Gk.) F. salamandre. — L. salamandra. — Gk. σαλαμάνδρα, a kind of lizard».\"),\n       cs(\"FSD\", \"s.v. salamander (FSD_vol4.txt ll.1059-1064)\", \"supports\", FSD_SAL)\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Šâli\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit शालि śāli- 'rice (esp. a fine winter rice)'\",\n   \"note\": (\"Correct on every point, and Nourai's citation is exact: Mo'in's footnote on BQT p.1229 reads «سانسکریت Shāli \"\n     \"(برنج و غلات مشابه آن) «ویلیامز ۱:۱۰۹۸»», i.e. Sanskrit śāli glossed 'rice and grains like it' with a Monier-Williams \"\n     \"reference — which is where Nourai's gloss 'grains, cereals' comes from. Wiktionary and Mo'in's dictionary ([سنس.]) \"\n     \"agree that Persian شالی is a Sanskrit loan.\"),\n   \"note_fa\": (\"این مدخل از هر نظر درست است و ارجاع نورایی نیز دقیق: حاشیهٔ معین بر برهان قاطع (ص ۱۲۲۹) می‌نویسد \"\n     \"«۱ - سانسکریت Shāli (برنج و غلات مشابه آن) «ویلیامز ۱:۱۰۹۸». در مازندران زراعت برنج را «شالی» گویند. «فرهنگ نظام».» \"\n     \"— و همین است سرچشمهٔ معنایی که نورایی داده («غلات»). ویکی‌واژه و فرهنگ معین (با نشانِ [سنس.]) نیز شالیِ فارسی را \"\n     \"وام‌واژه‌ای سنسکریت می‌دانند. ادعای نورایی درست است.\"),\n   \"sources\": [W_SHALI, AB_SHALI],\n   \"ref_check\": [nc(\"BQT:1229\", \"supports\", BQT_SHALI)],\n   \"consulted\": [\n     cs(\"MON\", \"Farhang-e Fārsi s.v. شالی (via abadis.ir)\", \"supports\", \"«[ سنس. ] (اِ.) برنجی که هنوز پوستش کنده نشده» — Mo'in tags it Sanskrit.\"),\n     cs(\"BQT\", \"vol.3, printed p.1229, Mo'in's footnote 1\", \"supports\", BQT_SHALI),\n     cs(\"ARY\", \"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi\", \"silent\", \"grep of incoming/ARY/ARY_pages.txt for شالی / شلتوک returns nothing.\")\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"šâlî «شالی»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian شالی šālī 'unhusked rice, paddy' is a loan from Sanskrit शालि śāli, taken over with the stem \"\n       \"vowel reinterpreted as the Persian -ī ending; it travelled with rice cultivation itself and is still the ordinary \"\n       \"word for the crop in the Caspian provinces — Mo'in's own footnote notes «در مازندران زراعت برنج را «شالی» گویند» \"\n       \"(citing Farhang-e Neẓām). Wiktionary: «Borrowed from Sanskrit शालि (śāli, 'rice')»; Mo'in's dictionary entry tags \"\n       \"it [سنس.] 'Sanskrit'. Note that the inherited Persian word for the cereal is برنج (Horn no.208 birinj/gurinj), a \"\n       \"different and older borrowing from the same Indian sphere; شالی is the specialised 'rice in the husk' term.\"),\n     \"derivation_fa\": (\"«شالی» به‌معنی برنجِ پوست‌نکنده وام‌واژه‌ای است از سنسکریت शालि śāli که در آن واکهٔ پایانیِ ستاک \"\n       \"به یای فارسی تعبیر شده است؛ این واژه همراهِ خودِ کشتِ برنج به ایران آمده و هنوز در مازندران و گیلان واژهٔ عادیِ \"\n       \"این کشت است — معین در همان حاشیه به نقل از «فرهنگ نظام» می‌نویسد «در مازندران زراعت برنج را «شالی» گویند». \"\n       \"ویکی‌واژه نیز می‌نویسد «وام‌گرفته از سنسکریت شالی (برنج)» و فرهنگ معین آن را با نشانِ [سنس.] آورده است. یادآور \"\n       \"می‌شود که واژهٔ رایج‌ترِ «برنج» (هرن، شمارهٔ ۲۰۸) وام‌واژه‌ای دیگر و کهن‌تر از همان حوزهٔ هندی است و «شالی» \"\n       \"اصطلاحِ ویژهٔ برنجِ در پوست است. ادعای نورایی درست است.\"),\n     \"sources\": [W_SHALI, AB_SHALI],\n     \"ref_check\": [\n       nc(\"BQT:1229\", \"supports\", BQT_SHALI),\n       nc(\"MON:2000\", \"supports\", \"Mo'in's page 2000 could not be paged (6-vol Farhang not online/on disk), but the entry text at abadis.ir/fatofa/شالی reads «[ سنس. ] (اِ.) برنجی که هنوز پوستش کنده نشده» — the Sanskrit tag and the 'rice in the husk' gloss are exactly what Nourai reports.\")\n     ],\n     \"consulted\": [\n       cs(\"BQT\", \"vol.3 p.1229, Mo'in's footnote 1\", \"supports\", BQT_SHALI),\n       cs(\"MON\", \"s.v. شالی (via abadis.ir)\", \"supports\", \"«[ سنس. ] (اِ.) برنجی که هنوز پوستش کنده نشده»; Dehkhoda on the same page: «درسانسکریت شالی بمعنی برنج و غلات مشابه آن است».\"),\n       cs(\"HRN\", \"Grundriss no. 208 (HRN.txt l.2205)\", \"silent\", \"Horn's article on rice is «208. (i)brinj, gurinj (AM.) 'Reis'» — he has no šālī entry, so the Grundriss neither supports nor contradicts.\"),\n       cs(\"ARY\", \"Aryanpur\", \"silent\", \"no شالی entry found in incoming/ARY/ARY_pages.txt.\")\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"šâlîzâr «شالیزار»; šaltŭk «شَلتوک»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Both are Persian formations on شالی. (a) شالیزار = شالی + the productive place/abundance suffix ـزار \"\n       \"(as in گلزار, نیزار, شوره‌زار), from Middle Iranian *-čāra-; the chart's cross-reference ☞Kwel points to Nourai's \"\n       \"root Kwel = PIE *kʷel- 'turn, move about, dwell', which is indeed the root usually given for this suffix. Wiktionary \"\n       \"lists شالیزار among the derived terms of شالی. (b) شلتوک šaltūk 'rice in the husk' is analysed by Wiktionary as \"\n       \"«From شالی (šâli), same, + توک (tôk, 'bundle, fagot; handle, grip')», with the long ā shortened in the closed first \"\n       \"syllable; Borhan (vol.3, printed ~1288) glosses it «برنجی را گویند که هنوز از پوست بر نیاورده باشد و بهندی شالی \"\n       \"خوانند», and Mo'in's dictionary «(شَ) (اِ.) برنجی که هنوز پوستش را نکنده باشند». The variant چلتوک that the chart \"\n       \"prints is the same word with the initial sibilant affricated; it passed into Ottoman Turkish and is modern Turkish \"\n       \"çeltik 'paddy', from which Dehkhoda's cross-reference شلتوک → چلتوک — the borrowing is Persian → Turkish, not the \"\n       \"reverse (Wiktionary shows çeltik as a descendant, not a source).\"),\n     \"derivation_fa\": (\"هر دو واژه ساخته‌هایی فارسی بر پایهٔ «شالی»‌اند. «شالیزار» = شالی + پسوند مکان/انبوهیِ ـزار \"\n       \"(مانند گلزار، نیزار، شوره‌زار) که از ایرانی میانهٔ *-čāra- است؛ ارجاعِ ☞Kwel در نمودار به ریشهٔ هندواروپاییِ \"\n       \"*kʷel- «گشتن، به‌سر بردن» اشاره دارد که همان ریشه‌ای است که معمولاً برای این پسوند می‌آورند. «شلتوک» را ویکی‌واژه \"\n       \"«شالی + توک» می‌داند (با کوتاه شدنِ آی کشیده در هجای بستهٔ نخست)؛ برهان قاطع (ج۳، ص ~۱۲۸۸) آن را «برنجی … که هنوز \"\n       \"از پوست بر نیاورده باشد و بهندی شالی خوانند» معنی کرده و فرهنگ معین «برنجی که هنوز پوستش را نکنده باشند». گونهٔ \"\n       \"«چلتوک» که در نمودار آمده همان واژه است با بدل شدنِ «ش» آغازین به «چ»، و همین صورت به ترکی عثمانی رفته و \"\n       \"çeltik ترکی امروز شده است؛ پس وام‌گیری از فارسی به ترکی بوده است نه وارونه. ادعای نورایی درست است.\"),\n     \"sources\": [W_SHALTUK, W_SHALI, AB_SHALTUK],\n     \"ref_check\": [\n       nc(\"BQT\", \"supports\", BQT_SHALTUK + \" (the node cites BQT without a page; the شلتوک entry is in vol.3, pdf page 79 = printed ~1288.)\"),\n       nc(\"MON:2070\", \"supports\", \"Mo'in's page 2070 could not be paged, but the entry text at abadis.ir/fatofa/شلتوک reads «(شَ) (اِ.) برنجی که هنوز پوستش را نکنده باشند» — Nourai's gloss 'rice in the husk' verbatim; Dehkhoda's entry «شلتوک. [ش َ] (اِ) چلتوک» supplies the چلتوک variant the chart prints.\")\n     ],\n     \"consulted\": [\n       cs(\"BQT\", \"vol.3 s.v. شلتوک (BQT_v3_pages.txt l.5886, pdf page 79)\", \"supports\", BQT_SHALTUK),\n       cs(\"MON\", \"s.v. شلتوک and شالیزار (via abadis.ir)\", \"supports\", \"«(شَ) (اِ.) برنجی که هنوز پوستش را نکنده باشند»; Dehkhoda s.v. شالیزار: «شالی زار را گویند که برنج زار باشد».\"),\n       cs(\"LKT\", \"Lokotsch, Etym. Wb. der europ. Wörter orient. Ursprungs\", \"silent\", \"grep of LKT.txt for celtik / çeltik / schaltuk / saltuk returns nothing — Lokotsch has no article on the word, so it left no trace in European languages.\"),\n       cs(\"HRN\", \"Grundriss der neupersischen Etymologie\", \"silent\", \"no šālīzār / šaltūk entry in HRN.txt.\")\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-429.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-429.py && python3 -m json.tool data/verification/page-429.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 429"
}
```


### [2026-09-14T01:40:26.960Z] TOOL RESULT

```
written
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 11, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'plausible': 2, 'confirmed': 2}
ref checks: {'supports': 15, 'not_checked': 3, 'partial': 6, 'contradicts': 1, 'not_found': 1}
books consulted: {'supports': 31, 'partial': 8, 'silent': 12, 'contradicts': 7} | by book: {'KLN': 7, 'SKT': 6, 'BQT': 5, 'LKT': 5, 'HRN': 4, 'FSD': 4, 'HJB': 4, 'MON': 4, 'AFM': 3, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'PLA': 2, 'ARY': 2, 'AHD': 2, 'BRT': 1, 'AID': 1, 'DKH/BQT': 1, 'LAT': 1}
```


## [2026-09-14T01:40:34.620Z] TOOL CALL #74: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/page-429.json && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-429.json'));print(d['pdf_page'],d['book_page'],len(d['entries']),[len(e['nodes']) for e in d['entries']])\""
}
```


### [2026-09-14T01:40:35.793Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 88104 Sep 13 21:40 /home/sfmqrb/git/rishe/data/verification/page-429.json
429 399 4 [4, 6, 5, 2]
```


## [2026-09-14T01:40:56.240Z] AGENT

Page 429 (book p. 399) verified — `/home/sfmqrb/git/rishe/data/verification/page-429.json`, `verify_check.py 429` reports 17/17 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed, 2 plausible. Nodes: 11 confirmed, 4 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 15 supports, 6 partial, 1 contradicts, 1 not_found, 3 not_checked.

**Flagged items**
- `disputed` — Saka / Greek "Scythe": modern scholarship derives Gk. Σκύθης from Proto-Scythian *Skuδa- "archer" (Szemerényi 1980; cf. Akkadian Iškuzāya), a different ethnonym from OP Sakā, which was the Persian cover-name for the steppe nomads. Also "Scythe" is the French spelling, not a Greek form — Mo'in's footnote, Nourai's source, prints both Skythes and French «سیت» and Nourai took the French half.
- `transcription_suspect` (error_in: **book**) — Sakah / "Malaysian tĕkka": the printed page reads "Malaysian", but Klein p.1578 (Nourai's own citation), Skeat, Hobson-Jobson, Lokotsch and AHD all say **Malayalam** (Dravidian, Kerala). Hobson-Jobson even notes the Malay word is *jati*. Page image saved to `data/verification/sources/refs/ocr/BOOK/429.png`.
- `plausible` nodes: OP node (Avestan *saka-* does not exist; *saka-stāna* is post-Achaemenid); Arabic sāj (Hobson-Jobson routes it through Marathi *sāg*, not Hindustani *sāgun*); Persian samandar and Arabic samandar (direction of borrowing unsettled — Greek σαλαμάνδρα has no Greek etymology; Skeat/Funk & Wagnalls call it "Eastern", Addi Shir explicitly derives Greek/Latin/Aramaic/English **from** the Persian).

**Extraction error for the owner to fix** (JSON differs from the page): entry 0, node 2 `script_extra`. The page prints «سکا ( سَکه ، ساک ، ساس ۱ )» — a variant list closing with footnote marker ۱; the JSON has «سکّه ، ساک ، ساسا», which swallowed the footnote digit into ساس and added a shadda to سکه. The three headwords (سکا، سگزی، سیستان) are extracted correctly.

Notable positives: Mo'in's BQT footnotes were located and quote Nourai almost verbatim for Sakastān/سگزی/سجزی (BQT ~1158), for samandar «۸ - از یونانی salamandra … (از افادات علامه دهخدا)» together with the Rūdakī verse Nourai prints (BQT ~1166/1170), and for شالی «سانسکریت Shāli … ویلیامز ۱:۱۰۹۸» (BQT vol.3 pdf p.20 = printed 1229). Lokotsch's own "Hobson-Jobson 910/911" confirms Nourai's HJB:910 is the right page. MON5:772 could not be checked (Mo'in's اعلام volumes are neither on disk nor online); TAD:37 is not findable in the local OCR.
