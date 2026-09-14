# Verification process log — verify-page-425


## [2026-09-14T01:21:41.215Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 425 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-425.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-425.json. Write /home/sfmqrb/git/rishe/data/verification/page-425.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 425` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:42.294Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:43.182Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:43.196Z] TOOL RESULT

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


## [2026-09-14T01:21:43.683Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-425.txt"
}
```


### [2026-09-14T01:21:43.721Z] TOOL RESULT

```
1	=== PDF page 425 (book page 395) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Reuto, Routo, Rut : intestines, bowels  (refs POK:873)
4	#1 (parent #0) [Avestan] refs=POK:874 | uruthwara, uruthwan, uruthwasča : abdomen, belly
5	  #2 (parent #1) [Pahlavi] refs=SNS:36 | aškumb : abdomen
6	    #3 (parent #2) [Persian] refs=SNS:36 | eškam «اشکم ( شکم ، شکمبه )» : abdomen, belly
7	#4 (parent #0) [Pahlavi] refs=POK:874 | rôt 1 : intestine
8	  #5 (parent #4) [Persian] refs=POK:874; HRN:139; BQT:970 | rŭdeh «روده» : intestine
9	--- entry 1 ---
10	ROOT [Indo-European] Rewe, Rŭ 3 : to open, open space  (refs POK:874)
11	#1 (parent #0) [Avestan] refs=POK:874; SYN:465; KLN:1356 | ravah : space ; ravas-čarât : moves in free space (freely) ☞Kwel
12	#2 (parent #0) [Germanic] refs=AHD | rumaz : space, room
13	  #3 (parent #2) [English] refs=AHD | room ; ream 2 : to widen ; reamer
14	#4 (parent #0) [Latin] refs=POK:874 | rŭs : open land
15	  #5 (parent #4) [English] refs=AHD | rural
16	--- entry 2 ---
17	ROOT [Semitic] R.f.a' : to repair  (refs KLN:1301)
18	#1 (parent #0) [Arabic] refs=KLN:1301 | r.f.a', rafŭ : to repair (damaged cloth)
19	  #2 (parent #1) [Persian] refs=FVA:167 | rofŭ «رُفو» : to repair torn cloth
20	#3 (parent #0) [Hebrew] refs=KLN:1301; FSD:2051 | râphâ : he repaired, healed ; râphâ-e'l : God has healed or is a healer ☞Layh
21	  #4 (parent #3) [Greek] refs=KLN:1301 | Raphael
22	    #5 (parent #4) [Latin] refs=None | 
23	      #6 (parent #5) [French] refs=None | 
24	        #7 (parent #6) [Persian] refs=None | Râfâel «رافائل» : "God is a healer"
25	      #8 (parent #5) [English] refs=KLN:1301 | Raphael, Raffael
26	
```


## [2026-09-14T01:21:46.627Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-425.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-14T01:21:46.682Z] TOOL RESULT

```
{
  "pdf_page": 425,
  "book_page": 395,
  "entries": [
    {
      "root": {
        "name": "Reuto, Routo, Rut",
        "lang": "Indo-European",
        "refs": "POK:873",
        "gloss": "intestines, bowels"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:874",
          "words": [
            {"translit": "uruthwara, uruthwan, uruthwasča", "gloss": "abdomen, belly", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "SNS:36",
          "words": [
            {"translit": "aškumb", "gloss": "abdomen", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:36",
          "words": [
            {"translit": "eškam", "gloss": "abdomen, belly", "script": "اشکم ( شکم ، شکمبه )"}
          ],
          "note": null,
          "quote": {
            "text": "شیر بی دمّ و سر و اشکم که دید؟ - این چنین شیری خدا هم نأفرید",
            "poet": "Molavî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "POK:874",
          "words": [
            {"translit": "rôt 1", "gloss": "intestine", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:874; HRN:139; BQT:970",
          "words": [
            {"translit": "rŭdeh", "gloss": "intestine", "script": "روده"}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Rewe, Rŭ 3",
        "lang": "Indo-European",
        "refs": "POK:874",
        "gloss": "to open, open space"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:874; SYN:465; KLN:1356",
          "words": [
            {"translit": "ravah", "gloss": "space", "script": null},
            {"translit": "ravas-čarât", "gloss": "moves in free space (freely)", "script": null, "see": ["Kwel"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "rumaz", "gloss": "space, room", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "room", "gloss": null, "script": null},
            {"translit": "ream 2", "gloss": "to widen", "script": null},
            {"translit": "reamer", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:874",
          "words": [
            {"translit": "rŭs", "gloss": "open land", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "rural", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "R.f.a'",
        "lang": "Semitic",
        "refs": "KLN:1301",
        "gloss": "to repair"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1301",
          "words": [
            {"translit": "r.f.a', rafŭ", "gloss": "to repair (damaged cloth)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:167",
          "words": [
            {"translit": "rofŭ", "gloss": "to repair torn cloth", "script": "رُفو"}
          ],
          "note": null,
          "quote": {
            "text": "نه بدستی زده ام چاک گریبانِ سلامت - گر ملامت کشم از کرده توان کرد رفویی",
            "poet": "Yaghmâ Jandaghî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:1301; FSD:2051",
          "words": [
            {"translit": "râphâ", "gloss": "he repaired, healed", "script": null},
            {"translit": "râphâ-e'l", "gloss": "God has healed or is a healer", "script": null, "see": ["Layh"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": "KLN:1301",
          "words": [
            {"translit": "Raphael", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Râfâel", "gloss": "\"God is a healer\"", "script": "رافائل"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1301",
          "words": [
            {"translit": "Raphael, Raffael", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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
```


## [2026-09-14T01:21:59.576Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','SNS','HRN','BQT','SYN','KLN','AHD','FSD','FVA','FVQ','MON','ARY','PHD','NYB','BRT','WLD','IEC','SKT','LEW','LAT','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


## [2026-09-14T01:22:00.108Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '120,260p' SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:22:00.694Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-14T01:22:00.745Z] TOOL RESULT

```
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


## [2026-09-14T01:22:04.370Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['POK']['page_offset']);print(d['POK'].get('lookup_hint'));print();print(d['SNS']);print();print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'))\n\""
}
```


### [2026-09-14T01:22:05.484Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config

{'title': 'Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986', 'kind': 'archive_djvu', 'url': 'https://archive.org/details/VajnameShayest', 'lookup_hint': "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'], 'page_offset': '242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image', 'covers_etymology': True, 'notes': 'OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image.'}

KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-14T01:22:07.971Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: reu\" POK_full.txt | head -40; echo \"---pages---\"; grep -n \"Page(s): 87[34]\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:22:08.043Z] TOOL RESULT

```
70434:Root / lemma: reu-b-ax\6 reu-g- 
70479:Root / lemma: reuA^-{*uereuA'^^ (zero grade of *hieleuRh-) 
70485:Root/ lemma: reu6!^-\ "red' derived from a zero grade of Root/ lemma: el-1, ol-, J-\ "red, 
70576:Root / lemma: reugh-m(e)n- 
70592:Root/ lemma: reu-1, reu- ru- 
70664:Root / lemma: reu-2, reus- : ru- 
70856:Root / lemma: reu-3, reu-s- 
70866:Root / lemma: reu-4 
70871:Root / lemma: reu-smen- 
70888:Root / lemma: reus- 
70898:Root / lemma: reuto-, routo- rut- 
70914:Root / lemma: reua- : ru- 
---pages---
70590:Page(s): 873 
70886:Page(s): 873 
70896:Page(s): 873 
70912:Page(s): 873-874 
70939:Page(s): 874 
70961:Page(s): 874 
71143:Page(s): 874 
71151:Page(s): 874 
71167:Page(s): 874
```


## [2026-09-14T01:22:09.969Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '70888,70975p' POK_full.txt"
}
```


### [2026-09-14T01:22:10.028Z] TOOL RESULT

```
Root / lemma: reus- 
Meaning: elm 

Material: Irish rua/mm ^be\.u\a ainus, ainus glutinosa' {*reus-men); 

to Old High German rust. Middle High German Modern High German RusteH 

References: WP. II 361. 
Page(s): 873 

Root / lemma: reuto-, routo- rut- 

Meaning: stomach, intestines (of an animal) 

Material: Middle Persian rot^ intestines, entrails of Rindes', npers. ruda, PI. rudag-anf 

intestines, intestines, entrails ' {*reuto-ko-)\ jav. uru&wara, -wan-n. {*rut-uar-, -uan-) " 

intestines, entrails, belly'; 

Old English /■eao'a Tiermagen', engl. Aeao^'Labmagen' {* routo). Old Dutch roode^ 
psalterium '; Swedish dial, ruddai. "Labmagen' {*rudddn-). 

References: Liden KZ. 61, 14 f. 
Page(s): 873-874 

Root / lemma: reua- : ru- 

Meaning: to open; wide 

Material: Avestan ravah-n. "Raum, Weite', ravas-carat- '\Nas sich in Freien bewegt'; 

Latin rus, rur/sland (in contrast to town, city), estate' {*reuos); Middle Irish roe, ro/t 
"ebenes field' (because of Eigennamens Cu Roi, welcher older Cu /?ai// lautet, from 
*rduia); 

Germanic ru-ma-\n Gothic rums' capacious, wide', rumn. 'Raum', Old Icelandic rumr' 
capacious ', rumn. 'Raum, place'. Old Saxon rumm. 'Raum', Old Frisian Old English rum 
' capacious ', m. 'Raum, stretch of time, possibility, opportunity'. Old High German Middle 
High German rumm. 'Raum, aperture, free Raumlichkeit', Middle High German rum' 
capacious '; Old High German rum/. Middle High German rOme' capacious, wide, afar'; 
abgel. verb Germanic *rumian .Old Icelandic ryma' capacious make' etc.; 



Old Church Slavic ravbnbirom *orvbnb' even '; russ. /ci/es-ZTK/r'Altersgenosse'; Old 
Prussian arm's'true, certainly '; 

Tocharian AB riz-'open'. 

References: WP. II 356 f., WH. II 454, Trautmann 14. 
Page(s): 874 

Root / lemma: rezg- 

Meaning: to plait, wind 

Material: Old Indie rajju-i. 'rope, band'; Latin rest/'s ds. {*rezgtis) = Old Lithuanian rekstis 

"basket'; Old English resc(e), risc(e). Middle Low German risch^ bulrush'; Norwegian rusk 

m. ryskjeu. 'Schmiele', Old English rysc, ryscei. ' bulrush'; Middle Low German rusch 

"reed, bulrush'. Middle High German rusch(e)i. " bulrush'; Lithuanian rezgu, rekst/l\ax, 

wattle, braid, knit, bind, lace, tie ', Latvian rezgetl\ax, wattle, braid', rezg/s' wickerwork '; 

Old Bulgarian rozga'ro6, twig, branch', through secondary Beeinflussung of prefixes raz-: 

russ. -Church Slavic razga. 

References: WP. II 374, WH. II 431, Trautmann 245. 

Page(s): 874 

Root / lemma: red-1 

Meaning: to excite; joyful 

Note: only Germanic and balto-slavisch 

Material: Old English roV gleeful, blithe, glad, good', a-/'e/5/7'aufmuntern'; Old Icelandic 

/p/a5/r"heiter become', /77a/-/i0///7/7"redeliebend'; Lithuanian rods^ gladly, willing'; Old 

Church Slavic /'5o'b"libens', Serbo-Croatian rad, Czech rad6s. 

References: WP. II 369, Trautmann 235.
```


## [2026-09-14T01:22:26.695Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT uruth ===\"; grep -n \"uruθwar\\|uruθwan\\|uruθwas\\|uru\\?war\" BRT.txt | head -20; echo \"=== BRT alt ===\"; grep -n \"urutSwar\\|urudwar\\|uru9war\\|uruSwar\" BRT.txt | head -20"
}
```


### [2026-09-14T01:22:26.766Z] TOOL RESULT

```
=== BRT uruth ===
=== BRT alt ===
```


## [2026-09-14T01:22:28.519Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 139 area: roude ===\"; grep -n \"rūda\\|ruda\\b\\|rūdah\\|roude\" HRN.txt | head -30; echo \"=== HRN škam ===\"; grep -n \"šikam\\|sikam\\|škamb\\|skamb\\|aškamb\" HRN.txt | head -20"
}
```


### [2026-09-14T01:22:28.592Z] TOOL RESULT

```
=== HRN 139 area: roude ===
=== HRN škam ===
```


## [2026-09-14T01:22:31.189Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la HRN.txt BRT.txt && echo \"--- HRN leaf 160 (printed 139) ---\" && awk 'BEGIN{RS=\"\\f\"} NR==161' HRN.txt | head -60"
}
```


### [2026-09-14T01:22:32.210Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4803500 Sep  4 14:06 BRT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  688044 Sep  4 14:06 HRN.txt
--- HRN leaf 160 (printed 139) ---
- 139 -
624. {2)renff *Bergschaaf* (Vis und RäniTn, S. 144 Vers 13,
245 Vers 2 v. u.; Scliefer, Chrest. pers. 11, 249,
17 «.).
skr. ranku- *eine Art Antilope' (Nöldeke, münd-
liche Mitteilung).
625. revän 'Seele'.
aw. urvan- (d. i. tiruvan') *Seele*; phlv. riivän (ge-
schrieben )X2n), ruvdmk.
626. robäh *Fuchs'.
g. rüwüs *Fuchs (Semn. rüwä *Katze').
aw. raopis (?) ; plilv. röpäs, röbas ; ai. löpa^d- (skr.
lopäka- 'Art Schakal') *Fuchs'; arm. a)Me8 *Fuchs'
(Hübschmann No. 9).
Verg]. Bartholomae, Bß. 10, 294, der gr. dhimfj^
für ein Lehnwort hält; ebenso G. Meyer, Indog.
Forsch. I, 328 Anm.
kurd. rüwi 'Fuchs'; oss. d. robas, t. rübas (215);
bei. ropask (323; röba LW.); sar. rapc.
627. röd *Fluss', rödbar^ röd/ßne.
Kas. K.Z. röxönd^ rö/önS.
ap. rautah' Tluss'; phlv. röt, rötbar (Bund.); ai.
sr6tas- 'Strömung, Strombett, Strom, Fluss'.
kurd. rö; bei. röt (330).
628. rüde {*röde) 'Eingeweide'.
Käs. rävd, rüvS.
phlv. rötlk 'Eingeweide* (AV.).
kurd. rum; bei. rö^, rös (331); sar. raud.
Das neupersische Wort muss dem Bai. und Sar. zu
Folge auch ursprünglich einen Majhülvokal gehabt
haben ^).
629. rö^ (röj) 'Tag', rdzäne, rözgär (lX:i^Tn, Is. 1, 1), rö^e,
rözT (arab. LW. rizq-),
g. rüj.
^) von Staokelberg, Fünf ossetische Erzählungen, 83 ver-
gleicht 088. (t.) rüd 'Wurst'.
2) Wohl zuerst erkannt von Rückert, ZDMO. 10, 279.
```


## [2026-09-14T01:22:40.127Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"uru.war\\|uru.wan\\|uru.was\" BRT.txt | head -30; echo \"=== Eingeweide in BRT ===\"; grep -n \"Eingeweide\" BRT.txt | head -30"
}
```


### [2026-09-14T01:22:40.229Z] TOOL RESULT

```
6617:daHtaya  .  .   urukwan  V.J. 30;  Vt.j.if.',  bäzava  Ytj.?;  —  ydhaca  .  .  ßtäna  .  .
20780:(sd.);  nur  b)  im  jAmr.;  das  Relativ  ist  sub- stantivisch: hä  yä  dapta  (sd.)  apanasytiH Y,  JO,  isj  —  cvat  hs  nä  anhuyäiie  (sd.) ivat  ahmäi  (sd.)  naire  mizibm  aahat  yS .  .  rapi%win)m  .  ./ramaraite  A.  4-  4^-;  V.7. 78,  79',  9-47,  Yty,  41,  P.50.  c)  alm (Sp.  160  u.);  nur  b)  im  jAw.;  das  Re- lativ ist  substantivisch:  iuäaoaii»  vatö väiti  (sd.)  yim  .  .  kubaot'jitgmim  Jigaurva H.  2. 8^36.  d)  ^Ju  (sd.);  nur  b)  im jAw.;  das  Relativ  ist  substantivisch :  hSula vohu  manS  jag^rtbustarS  atahat  yö  gSus uru%warp  ham.pa/räiti  (sd.)  ya%a  hau yd  nöii  i^a  V.4.48;  9.51,  17.2; —  nSit hau  SS  vaeze  (sd.)  . .  yS  ndti  .  .  mayä vaoze  yO  nSit  nanm  aiavaium  . .  xSnaosta vä..  Y.4SU  *46'^\  47-  e)  ■"■  (Sp.9); a)  im  gAvr.;  das  Relativ  ist  a)  substan- tivisch; zu  1):  *ya%ä  ''äis  t^ä  varaiaitl _^j(NPn.)  data  atshsus  paouruyekya  ". .  se- cimdum  ea  ..  quae  (sunt)  praecepta  (als Praed.)  . ."  Y.j'j.  i.  zu  2):  ahyS  *main- ySus  .  .  yP  .  .  gqm  .  .  hSmJasai   Y.  47.  3;
20945:•  j.  yao-kars-  den.  Praes.  32  'Getreide säen,  bauen':  kat  asti  damaya  . .  uru>wan (sd.)  i . .  yal  ttyr^m  paiti  yaokarsti  {3SPA.) ". .  wenn  man  tüchtig  Getreide  baut"  V.
21257:•  j.  yat  paiti "  adv.-artige  Verb. ;  sie  leitet überall  einen  Satz  ein,  der  auf  eine  Frage antwortet;  i)  'wo,  ubi':  kva..z)mö  säist)in1 ■  •  yl  ^''  p^iti  fraistim  kärayeiti  .  . yavanqtttca  västranqm{sd.)ca  V.  J.  4;  i, 2.  5i  6,  8—13*,  32.  2) 'wenn,  wofern': kaf  asti  damaya  uruhwan  {sd)i  ..  ya^ w/rim  paiti  yaokarsti  (sd.)  V.  _j.  30;  — kö  .  .  tarn  . .  x^nUvayeitil  ..yat  bä  paiti .  ,  naire  aSaone  vtnzyät  asaya  daoäiti  V.
28717:I  hye^  avahyä  kärahyä  mdküt^  ähc^  .  . Aauv(zat)..  Bh.j.  11;  s.nochBh.J.  19,  2.6, i2,_j.6,  9  (Sp.  i730u.).l  ß)  substan- tivisch: käuca  *anayä  »arä  vahu  manö jäginbuitarB  anhat  yS  gSui  uru^wari hqm.pä/räiti  (sd.)  ya'ha  hau  yS  nSit  iia V.^.48;  —  a/  hau  as  . . yS  ml asadayat . . V.5.S1;  J7.a;  —  nSii  hau  *taxm5  yH mit  *aj'a  *taxmd  F.  47;  46,  48,  26;  — pairi%wS  bavaiH  pantä  yim  dänus  päiti *häu^  dit  atvö  apairi%ws  yS  vayaos anamansdikahe  Aog.  77.  3)   auf  den
=== Eingeweide in BRT ===
20024:der  (tierischen)  Eingeweide:  ya^  antar» vfrüika  *as  'ja  "was  zwischen  den  Nieren sitzt,  (näml.)  M."  V.i6:joPuZ.'\
25521:•  j.  umd'wan-,  'iwar-  n.  'Eingeweide, Bauch':  'wan  F._?g;  —  yB  gSus  'wart hqmpnfraiti  (sd.)  V.  4.48;  —  auch  Plur. : astila  gaonala  ^dimohaca  *''wqmca  pah- yasca  fraväxlas^a  YL  /_J.  1 1 ;  —  yB  nars aiaonB  kaca  "wqn  bt/asyät  "der  bei  einem Gläubigen  die  Eingeweide  kurirt"  V.  7. 44(?);  —  alte  äaxma  (sd.)  upanAanzalta an/aräj  naiMät  barp%ri/va  'WBJiva  "die Leicheostätten  soll  sie  (damit)  besprengen innen  im  Mutterleib,   im  Eingeweide"  V.
25523:VgL  np.  rüda,  nbal.  rS%  'Eingeweide';  Bthl. IF.  5.  »28.  —  Pü.  (ru  F.):  itamb,  (in  V.  /): an  ddprn  ad,  (sonst):  tranaakr.—  '>S.  *»ra!rya-.
```


## [2026-09-14T01:22:49.014Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25505,25530p' BRT.txt"
}
```


### [2026-09-14T01:22:49.081Z] TOOL RESULT

```
•  j.  katarasHl  "urütatahe  kmiahe  .  . Vyt.  47-
•  j.  urud-  f.  'Flusslauf,  Bett':  mafye  vä ?äiH  v3  vaimi  vä  'rBihi  vä  aps  [z/j] nävayi  ". .  oder  in  das  Bett  eines  fliessen- den Wassers"  V.  ij.  37.
Zum  V.  'roffJ-,  —  ai.  Vgl.  wiriiA-  f.(?).  —  Pü. :
•  j.  urujtayant-  f.  £N.  eines  gläubigen Mädchens:  kanyä  'yantö  alaonyh  Yt. 13. 141.
Eig.  Bed.?     Sehr  fragwürdiges  Wort.
•  j.  ^uniSav-''  m.  EN.  eines  Gläubigen: •Sflff/  poun^äxstayartahe    oiecnB   Yt.  13.
113. Eig.  Bcd.  ?  Ob  elwi  zu  ai.  rudiirä-  Adj.?  — i)  So  F  I ;  NA.  urül'  nach  MI  3.
j.  »ruiitjiiiä  F.  g :  liet  tiniüyei/i ;  1.  urvard-.
•  j.  uniÖa-  n.  'Wachstum';  yavanamca västranamla  '%3m  V,(j.  53.
Zum  V.  'tuBd-,   S  jj  b.  —  PÜ.J  ärlAün.
•  j.  uru^man-  n,  i)  'Wachsen,  Wachs- tum': *hixsäne  narim  alavatam ..mpära- yanta  .  .yavanqm  'mqm  (AP.)  V. /p.  a6;  — yal  nBit  äp5  takäÜ  stayat  (sd.)  t^it  urvara 'mabyB  Yt.  13.  78.  2)  'Gewächs'  (nur Komp.).
KompE.  —    Zum  V.  »raad-;    S  'i  *>■  — (zu  V.);  iuriäk  i  nutak.
•  j.  uruOmay-f.  i)  'Schoss,  Spross";  'milca paiti  variaßica  (sd.)  Y,  yi.  9.  2)  'Plan- tage, Garten' ":  yä  urvaranqm  .  .  srjrä 'ml/  äalsayeinti  Yt  13.  55.
Abieil.  —  Zum  V.  'ra«I-;  %  23\>.  ~  Pü.: ärüiin.  —  I)  Gdn.  KZ.  »5.  ssg.
•  j.  uruSmya-  Adj.  (fem.  yä-)  'schossend, sprossend':  urvaranqm^a  °myanqm  V.ig. 18,  Vyt.  22.
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
```


## [2026-09-14T01:23:08.618Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD aškamb ===\"; grep -n -i \"škamb\\|skamb\\|aškumb\\|askumb\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== PHD rot intestine ===\"; grep -n -i \"rōdīg\\|rotik\\|rōdī\\|rōd \\|entrails\\|intestin\" PHD.txt | head -30"
}
```


### [2026-09-14T01:23:08.697Z] TOOL RESULT

```
=== PHD aškamb ===
PHD.txt:221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
PHD.txt:974:belly aSkamb(ag), aškom(b); (daevic) mulān.
PHD.txt:4992:karbāš karbunag karg kirīh- askamb! kirrén- kirrēnīdan kilēl
PHD_mackenzie.txt:1265:askamb [KL{iE < A krs'; )/kmb l I M c/kmb, N Iikam] belly, womb.
PHD_mackenzie.txt:1266:  .....ag [_kl I N !ikamba] = askamb.
PHD_mackenzie.txt:1271:askom(b) ['/kwm(b l )] = askamb.
PHD_mackenzie.txt:6058:belly aSkamb(ag), askom(b); (daevic)        blinking mezisn.
PHD_mackenzie.txt:7965:whatever cegam-iz-e(w).                'womb askamb(ag), askom(b), burdar,
PHD_mackenzie.txt:9519:kamun                                 askambI               ~,
PHD_mackenzie.txt:9535:                                      askambI             ~,
PHD_mackenzie.txt:11318:askamb                                    asyanag                    \~~
=== PHD rot intestine ===
559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
1780:entrails rodigàn.
2471:intestine(s) ródig, uruspar.
```


## [2026-09-14T01:23:10.129Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS ===\"; grep -n -i \"kumb\\|kamb\" SNS_pages.txt | head -30; echo \"=== NYB ===\"; grep -n -i \"škamb\\|skamb\\|rōtīk\\|rotik\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:23:10.207Z] TOOL RESULT

```
=== SNS ===
2231:                                                                                                                                       (*^*ii   :^) wnSil.fSil. fii:askumb:__y.fc»3-Mj-**
3639:                               532)kumbha'                 *#**»* xumba-: L-                          I                            -p/Y>£     fftfPS.   p.    241. No. 1074. \Sj
14967:                                agemat 243/3         kumbha 73/7                       cit 246/20
=== NYB ===
737:aškamb ['škmb'], aškam ['škm], aškom [škwm], also [KLSH 1013-18, 1111, 6513], belly, stomach, womb 3? etc. — MPrs škmb (A-H II; Sogd. 3176); Paz. aškum (Mx), iškam (SGV); NP iškam, šikam. Aškān ['ik?n!] n. pr., the ancestor of the Aškanian, or Arsacid, dynasty; Zēndān
2101:i [Prs inscr., Ps.. ZY; BP contracted to a ligature coinciding with y: ZY, except when connected with an encl. pron.: ZY- m = i-m, ZY -t = i-t, ZY -š = 4-6, ZY-m’n' = i-mān, ZY-Vn' = i-tün, ZV šin! +-šān] A. a) relative pron., may be used as the subj. or the dir. obj. of its clause: hān i ó man mat 12°; én fradand + andar aškamb därem 1013; has no cas. obl; instead it takes an encl. pron. referring to the correlate: hàn ... i- dmocišn he whose education 80" (rare, commonly k&-$); cannot be governed by a prep.; instead the prep. is placed ?n the clause and governs a pron. referring to the corre- late: *sīh-ē (v. ?sih) ... $ hac han nēva- koktar butan ne šāyist ‘splendor quo nullus pulchrior esse poterat’, a *splend- our that was the most beautiful. ever existent 717-18; or the prep. is changed into an adv. connected with the vb. of the clause: méx i patiš bandēnd 300 xirs poles on which they fasten 300 *rings 2026 (bastan construed with pat; patiš the adv. of pat, v.s.v. patiš); in such cases ke is more usual. — b) conj.: &on l . $ so ... that 2016-17, 3226-27; cand i as much as 3119; 4 ka, hān 4 ka, v. ka; —i-šān 4, 1-8 $ when, as soon as 5811,
2103:(1249) yada yat. — B. Izäfat. Relative clauses are often nominal without the copula, e.g. hàn + hac tō kas he who is thy inferior 685; han fradand +-$ andar aškamb this child that is in her womb 123; hence the :izäfat construction de- veloped: by means of 4, originally the subj. of a nominal clause without the copula, a subst., an adj., a prepositional attribute or an adv. is added to a subst. as its qualifier; I shall call these qualifiers relative attributes. A subst. added to a subst. in this way is the equivalent of our genitive, or it is in apposition. The relative attribute is 1. placed after its headw.: duxt % en varzekar the
3675:šutan [ZLWN-tn'] šav- [ZLWN-), forms v. I, 177, to go, opp. (G)matan to come: hac ki mat hom u apāc 6 ku šavom? whence have I come and whither shall I go? 6245; pat druyist šutan u āmatan that they may go and come safely 8723; ka han damistan Sut when this winter has gone 972; hac man šavdi thou shalt go (fly) off from me 2715; — regularly be ~ to go away, passim; bē o ... ~ to go (away) to; bé ~ to disappear, vanish 9416, to escape 2415-16 ; bē-šutak baxt whose luck is gone, who is off his luck 5?; — andar ~ : tigr tai parr pat aškamb andar šut the arrow penetrated right up to the feather into its belly 3%; to enter 181%, also andar-rón 1813, andarón 1912-13; 7525. 10278; — apāc ~ to go back, to
3845:*ud(a)rài [*^wdPy] some kind of noxious reptile 581. 987. — Seems to be a shortened or mutilated form of the BP w. by which Av. (387) udaré.6rqsa- Vd. 14° is rendered: uóra-[Paz.] (kšk' =) kašak: ul sräyisn, with the explanation & ki pat aškem [sic = aškamb] dvārēt, cf Skr udara- ‘belly’. All the noxious animals mentioned 58! are also found in Vd. 14°, except pazdok. — My first reading ’wyl’y cannot be main- tained.
6132:Shry’r: Sahridär Shry’ryy: šahridārēh šhryst'n: Sahristän Skmb: aškamb Sr’syn-: Särs-
6391:aškum: aškamb
6662:iškam: aškamb izišn: ~
7216:iškam, šikam: aškamb
```


## [2026-09-14T01:23:26.571Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=25521 && /\\[pdf page/ {p=$0} END{}' SNS_pages.txt >/dev/null; echo \"=== SNS page tag near 2231 ===\"; awk 'NR<=2231 && /pdf page/{p=$0; n=NR} END{print n\": \"p}' SNS_pages.txt; sed -n '2225,2240p' SNS_pages.txt"
}
```


### [2026-09-14T01:23:27.973Z] TOOL RESULT

```
=== SNS page tag near 2231 ===
: 
                                                                                                                                                                    ,                           :   askOb: «Jld-M_M*       i
\o                              1
                                                                                     j^ov^->-«^
                                                                                                                                        *T/Y»5 -o^jt "x^^^lj^U ir-1 * ,i' **=?• y* j
      ^j*j>»J£i*S          _»*>      I*     Mjf-6-^ usWv)         ^^ jj^o^^^y
                                            .   W/Y ^       -   «^-^ Crfjj («-*>* Jr- 5 **—*t
                                                                                                                                       (*^*ii   :^) wnSil.fSil. fii:askumb:__y.fc»3-Mj-**
                                                     .   j^ii     .   •»>*£!:      asnaved: yu ^^U j    c-
                                                                                                         skrab    :>:t .o-luru0wasca
      {Mir. Man.              >snwij:L (Mir. Man. II,                               47) 'Inw: .P*                                                      oVo^MJ^Mh/A* *fr/W
                                                                                                         /W«^ -6A/T «* .(ijo-yv) askum :^ (Mir. Afcwi.II, 63).
va         ta~l      Uunfcer         L.Jw^isoV^^ 111,51)                                                                                                                                                                   16
                                                                                                                                                                                                t/M ^        VA-1T
```


## [2026-09-14T01:23:30.462Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"uniS'wan-\")\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest preceding line that looks like a column number\nfor n in range(25521,25400,-1):\n    l=lines[n-1].strip()\n    if re.fullmatch(r'\\d{3,4}',l) or re.match(r'^\\d{3,4}\\s*$',l):\n        print(\"col marker at line\",n,\":\",l); break\n# print any 4-digit standalone numbers nearby\nfor n in range(25450,25560):\n    l=lines[n-1].strip()\n    if re.fullmatch(r'\\d{3,4}',l): print(n,l)\nEOF\ngrep -c $'\\f' BRT.txt"
}
```


### [2026-09-14T01:23:31.772Z] TOOL RESULT

```
col marker at line 25460 : 1530
25457 1539
25460 1530
25533 1533
1037
```


## [2026-09-14T01:23:37.679Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SNS_pages.txt | head -5; echo \"---\"; awk 'NR<=2231 && /\\[pdf page [0-9]+\\]/{n=NR;p=$0} END{print n\": \"p}' SNS_pages.txt; echo \"=== wider context 2215-2245 ===\"; sed -n '2200,2250p' SNS_pages.txt | grep -n \"askumb\\|uru0\\|pdf page\""
}
```


### [2026-09-14T01:23:38.751Z] TOOL RESULT

```
---
: 
=== wider context 2215-2245 ===
32:                                                                                                                                       (*^*ii   :^) wnSil.fSil. fii:askumb:__y.fc»3-Mj-**
34:                                                                                                         skrab    :>:t .o-luru0wasca
```


## [2026-09-14T01:23:42.251Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nc=0\nfor i,l in enumerate(t[:2231]):\n    c+=l.count('\\f')\nprint('formfeeds before line 2231:',c)\nprint('total leaves:',open('SNS_pages.txt',encoding='utf-8',errors='replace').read().count(chr(12))+1)\n\""
}
```


### [2026-09-14T01:23:43.312Z] TOOL RESULT

```
formfeeds before line 2231: 34
total leaves: 243
```


## [2026-09-14T01:23:52.449Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD reuə ===\"; grep -n -i \"reu.*-\\bopen\\|rural\\|reamer\\|^room\\|rumaz\" AHD_watkins1985.txt | head -20; echo \"=== AHD reue root block ===\"; grep -n \"reuə\\|reua-\\|reu -\\|reu(ə)\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:23:52.531Z] TOOL RESULT

```
=== AHD reuə ===
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
2204:RUNE! riino- RUNE? riino- RUNNEL rei-3 RUPICOLOUS reup- RUPTURE reup- RURAL reue- RUSH? rezg- RUSSET reudh-! RUsT reudh-1 RUSTIC reue- RUT? reu-1 RUTABAGA wrad- RUTH kreue-2 RUTILANT reudh-1 Rx _ kap-
=== AHD reue root block ===
2199:ROOF kropo- ROOK! ker-2 ROOM reua- ROOST kred- ROOT! wrad- ROOT? wrdd- ROPE rej-1 RORQUAL = reudh-1, (s)kWal-o- ROSE! wrod- ROSEMARY ers-2 ROSTRUM_ réd- ROTA ret- ROTARY ret- ROTATE ret- ROTE? reu-! ROTE3 krut- ROTIFORM ret- ROTOGRAVURE ret- ROTUND ret- ROTUNDA ret- ROUGE reudh-1 ROUGH ruk-2 ROULETTE ret- ROUND! ret- ROUND? riino- ROUT! reup- ROUTS = reu-1 ROUX reudh-1 ROVER reup- Row! rej-1
```


## [2026-09-14T01:23:55.042Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN room ===\"; grep -n \"^room,\" KLN_1966.txt | head; grep -n \"^ream,\" KLN_1966.txt | head; grep -n \"^rural,\" KLN_1966.txt|head; echo \"=== KLN Raphael ===\"; grep -n -i \"^raphael\\|Raphael,\" KLN_1966.txt | head; echo \"=== KLN rafa ===\"; grep -n -i \"rāphā\\|rapha'\\|to heal.*Heb\\|refa\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T01:23:55.321Z] TOOL RESULT

```
=== KLN room ===
33094:room,  n.  —  ME.  roum,  rum,  fr.  OE.  rum,  ‘space’, rel.  to  ON.,  OS.,  OHG.,  MHG.,  Goth,  rum, G.  Raum,  Dan.,  Swed.  rum,  ‘space’,  Du.  ruim, ‘hold  (of  a  ship),  nave’.  These  nouns  are substantivations  of  the  Teut.  adj.  *ruma-  ap¬ pearing  in  OE.,  MHG.  rum,  OHG.  rumi,  ON. riimr,  Dan.,  Swed.  rum,  Du.  ruim,  Goth,  rums, ‘roomy,  spacious';  fr.  I.-E.  base  *re"'-,  ‘wide, open',  whence  Toch.  AB  ru-,  ‘to  open’,  Avestic ravah-,  'space',  L.  rus,  ‘open  country',  OIr.  roi, roe,  ‘plain  field'.  Cp.  ream,  ‘to  enlarge  a  hole', rummage.  Cp.  also  rural,  rustic.
31826:ream,  n.,  20  quires  of  paper.  —  ME.  reme,  fr.  OF. ray  me  (F.  rame),  fr.  Sp.  resma,  fr.  Arab.  rizmah, ‘bundle,  bundle  of  paper’.
31827:ream,  n.,  cream;  froth.  —  ME.  rem,  fr.  OE. ream,  ‘cream’,  rel.  to  MLG.  rom,  rome,  Du. room,  MHG.  roum,  G.Rahm,  Icel.  rjomi,  ‘cream’, fr.  Teut.  base  *rauma-,  which  corresponds  peril, to  I.-E.  *raugma-,  whence  Avestic  raoyna-,  ‘but¬ ter’.  Cp.  ramekin.
31829:ream,  tr.  v.,  to  enlarge  a  hole.  —  Lit.  ‘to  make room’,  fr.  ME.  remen,  rumen,  fr.  OE.  ryman,  ‘to make  room,  widen’,  fr.  rum,  ‘spacious,  wide’. Cp.  OS.  riimian,  ON.  ryma ,  OFris.  rema,  OHG. rumen,  ‘to  make  room,  widen’.  Cp.  also  E.  dial. rime,  ‘to  enlarge  a  hole’,  and  see  room, reamer,  n.,  a  tool  for  enlarging  a  hole.  —  Formed fr.  prec.  word  with  agential  suff.  -er. Derivatives:  reamer,  tr.  v.,  reamer-er,  n. reanimate,  tr.  v.,  to  bring  back  to  life.  —  Formed fr.  re-  and  animate,  v.
33359:rural,  adj.,  of  the  country.  —  ME.,  fr.  L.  ruralis, ‘pertaining  to  the  country’,  fr.  riis,  gen.  riiris, ‘the  country’,  which  is  cogn.  with  OSlav.  ravind , ‘level’,  Oir.  roi,  roe,  ‘plain  field’,  OE.  rum,  etc., ‘space’.  See  room  and  cp.  roister,  Ruritanian, rustic.  For  the  ending  see  adj.  suff.  -al. Derivatives:  rural-ism,  n.,  rural-ist,  n.,  rural-ite, n.,  rural-ity,  n„  rural-ize,  tr.  v.,  rural-iz-ation, n.,  rural-ly,  adv.
=== KLN Raphael ===
12751:El,  n.,  Hebrew  name  for  God.  —  Heb.  El,  ‘God’, of  uncertain  etymology;  possibly  related  to  el, ‘strong’  (cp.  e.g.  Gen.  31: 29  yesh  ESI  yadt,  ‘it is  in  my  power’).  Cp.  Elohim.  Cp.  also  the  first element  in  the  PN.s  Eleazar,  Eliezer,  Elihu, Elijah,  Elishah,  Elizabeth,  and  the  second  ele¬ ment  in  Babel,  bethel  and  in  the  PN.s  Daniel, Emmanuel,  Ezekiel,  Gabriel,  Gamaliel,  Ishmael, Israel,  Joel,  Michael,  Nathaniel,  Raphael, Samuel.
30125:Pre-Raphaelitism,  n.,  the  style  of  the  Pre-Raphae¬ lites.  —  Formed  with  suff'.  -ism  from  the  fore¬ name  of  Raphael  Sanzio  (1483-1520)  and  the suffixes  -ite  and  -ism.  The  members  of  the  Pre- Raphaelite  Brotherhood,  founded  in  England  in 1847,  called  themselves  Pre-Raphaelites,  to  inti¬ mate  that  their  style  resembled  that  of  the  Italian painters  before  Raphael, prerequisite,  n.  —  Formed  fr.  pre-  and  requisite, prerogative,  n.,  a  special  privilege.  —  ME.,  fr. OF.  (=  F.)  prerogative,  fr.  L.  praerogativa,  ‘a previous  choice  or  election’,  prop.  fem.  of  prae- rogativus,  ‘asked  for  a  vote  before  others’,  fr. praerogatus,  pp.  of  praerogare,  ‘to  ask  first’,  fr. prae  (see  pre-)  and  rogare,  ‘to  ask’.  See  pre-, rogation  and  -ive.
31684:rape,  n.,  refuse  of  grapes.  —  F.  rape,  fr.  ML. raspa,  fr.  WTeut.  *raspdn,  ‘to  scrape;  to  sweep off’.  See  rasp,  v. ,  and  cp.  words  there  referred  to. '  Raphael,  1)  masc.  PN.  2)  an  archangel  mention¬
=== KLN rafa ===
27:Preface
1250:absorbent,  adj.  —  L.  absorbens,  gen.  -entis,  pres, part,  of  absorbere.  See  absorb  and  -ent. absorption,  n.  —  L.  absorptid,  gen.  -onis,  fr.  ab- sorptus,  pp.  of  absorbere.  See  absorb  and  -ion. abstain,  intr.  v.  —  ME.  absteynen,  fr.  OF.  as- tenir,  fr.  VL.  *abstenire,  corresponding  to  L. abstinere,  ‘to  abstain’,  which  is  formed  fr.  abs, ab,  ‘away  from,  from’  (see  ab-),  and  tenere,  ‘to hold’.  See  tenable  and  cp.  appertain,  contain, detain,  entertain,  maintain,  obtain,  pertain,  re¬ tain,  sustain.  Cp.  also  abstention,  abstinence. The  ME.  and  E.  forms  have  been  refashioned after  L.  abstinere.
1348:accolade,  n.,  an  embrace,  formerly  used  in  con¬ ferring  knighthood ;  now,  a  touch  of  the  shoul¬ der  with  the  flat  blade  of  the  sword  in  conferring knighthood.  —  F.,  refashioned,  on  analogy  of words  ending  in  -ade,  fr.  OF.  acolee,  prop, subst.  use  of  the  fern.  pp.  of  acoler,  ‘to  embrace round  the  neck’,  fr.  VL.  *accoIIdre,  fr.  ad-  and L.  collum,  ‘neck’.  Cp.  It.  accollata  and  see  collar and  -ade.  Cp.  also  next  word.
1744:adventure,  n.  —  ME.  aventure,  fr.  OF.  (=  F.) aventure,  fr.  VL.  *adventura,  ‘a  happening’,  fr. L.  aventurus,  ‘that  which  is  going  to  happen’, fut.  part,  of  advenire,  ‘to  arrive,  happen’.  The English  word  was  refashioned  after  L.  advenire, adventurus.  See  advent  and  cp.  venture.  Cp.  also saunter.
1755:Derivatives:  adverse-ly,  adv.,  adverse-ness,  n. adversity,  n.,  misfortune.  —  OF.  aversite,  later adversite  (F.  adversite).  See  prec.  word  and  -ity. advert,  intr.  v.,  to  refer  to.  —  F.  avertir,  fr.  L.  ad¬ vertere,  ‘to  turn  toward’,  fr.  ad-  and  vertere,  ‘to turn’.  In  English,  the  word  has  been  refashion¬ ed  after  L.  advertere.  See  version  and  cp.  adver¬ tise  and  the  second  element  in  animadvert.  Cp. also  avert,  controvert,  convert,  covert,  culvert, divert,  extrovert,  introvert,  overt,  pervert,  subvert, advertence,  n.,  attention.  —  OF.  avertence,  later (=  F.)  advertence,  fr.  Late  L.  advertentia.  See advertent  and  -ce.
1863:firm,  adj.  F.  affirmer  and  E.  affirm  have  been refashioned  after  Latin  affirmare. affirmation,  n.  —  F.  affirmation,  fr.  L.  affirma- tionem,  acc.  of  affirmatio,  fr.  affirmatus,  pp.  of affirmare.  See  prec.  word  and  -ion. affirmative,  adj.  —  F.  affirmatif  (fern,  affirma¬ tive ),  fr.  L.  affirmativus ,  fr.  affirmatus ,  pp.  of  af¬ firmare.  See  affirm  and  -ative.
2453:Amelia,  fern.  PN.  —  A  Teutonic  name  lit.  mean¬ ing  ‘laborious’.  Cp.  ON.  ama,  ‘to  trouble’,  and Amal,  name  of  the  ruling  family  of  the  Ostro¬ goths.  The  name  was  confused  later  with  the name  of  the  Roman  gens  Aemilia  (see  Emily). ameliorate,  tr.  v.,  to  make  better;  intr.  v.,  to  be¬ come  better.  —  Formed  with  verbal  suff.  -ate fr.  F.  ameliorer,  which  is  refashioned  after  L. melior,  ‘better’,  fr.  OF.  ameillorer,  fr.  OF.  meil- lor  (whence  F.  meilleur),  ‘better’,  fr.  L.  melio- rem,  acc.  of  melior,  ‘better’.  See  meliorate. Derivatives:  amelioration  (q.v.),  amelior-at-ive, adj.,  amelior-at-or ,  n.
2683:Derivative:  ancestral-ly,  adv. ancestry,  n.  —  OF.  ancesserie;  refashioned  after OF.  ancestre.  See  prec.  word  and  -y  (represent¬ ing  OF.  ie).
3439:arithmetic,  n.  —  ME.  arsmetike,  fr.  OF.  aris- metique,  fr.  L.  arithmetica,  fr.  Gk.  dpiffpnrjxixr] (scil.  styyr),  'the  art  of  counting’,  fr.  apiU- jietv,  ‘to  number,  count,  reckon’,  fr.  dpi-Ofiop, ‘number’,  fr.  I.-E.  base  *rf-,  ‘to  count,  number’, whence  also  Gk.  v()-pi-xo4,  ‘numberless’,  OE., OHG.  rim,  ‘number’,  Olr.  rim,  ‘number’,  do- rimu,  ‘I  count,  number,  enumerate’,  L.  ritus, ‘religious  custom,  usage,  ceremony’.  Base  *rf-, ‘to  count,  number’,  is  prob.  an  enlargement  of base  *ar-,  ‘to  join’,  whence  L.  arma,  ‘weapons’, ars,  ‘art’,  Goth,  arms,  OE.  earm,  arm,  etc.,  ‘the upper  limb’.  See  arm,  ‘the  upper  limb’,  arm, ‘weapon’,  and  cp.  rhyme,  rite.  The  a-  in  dpiffpio? is  prosthetic  and  due  to  the  fact  that  the  Greek (as  well  as  the  Armenian)  never  begins  a  word with  primary  r.  Initial  p  in  Greek  words  goes back  either  to  *sr-  or  *wr-  (see  red).  The  s  in  OF. arismetique  is  the  phonetic  rendering  of  L.  th  = Gk.  1>;  the  ME.  forms  arismetric,  arsmetrik were  developed  from  ME.  arsmetike,  which  was associated  erroneously  with  L.  ars  metrica,  ‘the art  of  measure’.  ModF.  arithmetique  and  E. arithmetic  have  been  refashioned  after  the  Greek. Cp.  aparithmesis  and  the  second  element  in logarithm.
3599:-ase,  suff.  denoting  enzymes  ( biochemistry ).  — The  ending  of  diastase  (q.v.),  the  first  enzyme isolated,  became  the  regular  suffix  for  forming nouns  denoting  enzymes.  Cp.  -ese. aseity,  n„  being  by  itself  (philos.)  —  ML.  aseitas, ‘state  of  being  by  itself’,  fr.  L.  a  se,  ‘from,  or  of, himself’.  See  a-,  ‘from’,  sui  and  -ity. asepsis,  n.,  absence  of  sepsis  (med.)  —  Medical L.,  formed  fr.  priv.  pref.  a-  and  sepsis, aseptic,  adj.,  pertaining  to  asepsis,  not  producing sepsis  (med.)  —  Formed  fr.  priv.  pref.  a-  and cFY]7rTix6^,  ‘putrefactive  .  See  septic.
4117:aviator,  n.  —  Refashioned  after  F.  aviateur.  See prec.  word  and  agential  suff.  -or. aviatress,  aviatrix,  n.,  a  woman  aviator.  —  For¬ med  fr.  aviator  with  suff.  -ess,  resp.  -trix. Avicennism,  n.,  the  teachings  of  the  Arab,  philo¬ sopher  Avicenna  (=  Ibn  Sina)  (980-1037).  For the  ending  see  suff.  -ism.
4392:Derivatives:  bank,  intr.  v.,  to  keep  a  bank;  to keep  money  in  a  bank;  tr.  v.,  to  keep  (money) in  a  bank ;  bank-able,  adj.,  bank-er,i\.,bank-ing,n. banket,  n.,  the  conglomerate  in  the  Witwaters- rand  gold  district  in  the  Transvaal.  —  S.  Afr. Du.,  lit.  ‘sweetmeat’,  fr.  F.  banquet.  See  banquet, bankrupt,  n.  and  adj.  —  Refashioned  after  L. rupta,  fr.  F.  banqueroute,  fr.  It.  banca  rotta,  lit. ‘a  broken  bench’,  fr.  banca,  ‘bench’,  and  rotta (fr.  L.  rupta),  fern.  pp.  of  rompere,  ‘to  break’, fr.  L.  rumpere,  (sec  bench  and  rupture) ;  so  called from  the  habit  of  breaking  the  bench  of  bank¬ rupts.
4414:baptism,  n.  —  ME.  bapteme,  fr.  OE.  baptesme (F.  bapteme),  fr.  Eccles.  L.  baptisma,  fr.  Gk. Pa7tTicrpa,  ‘a  dipping  in  water’,  in  Eccles.  Gk. ‘baptism’,  fr.  paTrriCetv,  ‘to  dip’,  in  Eccles.  Gk. ‘to  baptize’,  fr.  pdbrmv,  ‘to  dip,  steep,  dye, color’,  which  is  rel.  to  (3a<pf),  ‘a  dyeing’,  and cogn.  with  ON.  kvefja,  ‘to  plunge’,  OSwed.  kvaf, ‘a  deep  place’.  For  sense  development  it  should be  borne  in  mind  that  baptism  orig.  consisted in  immersion.  E.  baptism  has  been  refashioned after  Eccles.  L.  baptisma,  Gk.  piimopia.  For the  ending  see  suff.  -ism.  Cp.  Baphia,  Baptisia, baptist,  baptistery,  baptize  and  the  second  ele¬ ment  in  phlobaphene.
6551:Caridea,  n.,  a  group  of  crustaceans  (zool.)  — ModL.,  formed  with  suff.  -idea  fr.  Gk.  y.ipiq, gen.  xapiSop,  ‘shrimp,  prawn’,  which  is  prob. rel.  to  xipxflop,  ‘horned  beetle’.  See  scarab  and cp.  Carabidae.  Cp.  also  Epicarides,  Syncarida. caries,  n.,  decay  ( med .)  —  L.  caries,  ‘decay,  rot¬ tenness-,  fr.  I.-E.  base  *ker-,  ‘to  hurt,  hit’, whence  also  Gk.  xf,p,  ‘death,  destruction’, jtxypx rop,  ‘unhurt’,  xepxtljs'.v  (for  *x£pxfl^eiv), 'to  lay  waste’,  xspxuvop  [for  *xspx-.r(s)vd;], ‘thunderbolt,  lightning’,  lit.  ‘smasher,  crusher'. OI.  srnSti,  ‘breaks,  crushes’,  iiryate,  siryate, ‘falls  asunder’,  OIr.  ar-a-chrinim,  ‘I  fall  to pieces’,  irchre,  ‘fall,  ruin',  crin,  ‘withered,  faded'. Cp.  cerauno-  and  the  second  element  in  sincere, carillon,  n.,  musical  bells.  —  F.,  ‘peal  of  bells’, fr.  OF.  quarregnon,  carignon,  fr.  VL.  quadrini- onem ,  acc.  of  *quadrinid,  refashioned  on  anal¬ ogy  of  words  beginning  with  quadri-  (see  qua- dri-),  fr.  L.  quaternid,  ‘a  group  of  four  things’ (here  used  in  the  sense  of  ‘a  group  of  four bells’).  See  quaternion.
6841:caulescent,  adj.,  having  a  visible  stem.  —  Formed fr.  L.  caulis,  ‘stalk,  stem’,  with  the  inchoative suff.  -escent,  on  analogy  of  arborescent.  See cole  and  cp.  next  word.  Cp.  also  acaulescent. cauliflower,  n.  —  Refashioned  after  L.  caulis, ‘stem’,  and  E.  flower  fr.  earlier  colyflory,  fr.  F. chou-fleuri,  chou-fleur,  which  is  formed  on  ana¬ logy  of  It.  cavolo  fiore,  ‘cauliflower’,  fr.  L.  caulis, ‘stem,  stalk’,  and  flos,  gen.  /Idris,  ‘flower’.  See cole.
7968:closure,  n.  —  OF.,  fr.  L.  clausiira  (whence  also It.  chiusura),  fr.  clausus,  pp.  of  claudere,  ‘to shut’.  See  close,  adj.,  and  -ure.  F.  cloture,  ‘clo¬ sure’,  has  been  refashioned  fr.  OF.  closure  on analogy  of  nouns  ending  in  -ture.  Cp.  cloture. Derivative:  closure,  tr.  and  intr.  v.
8144:Derivatives :  cognizable-ness,  n.,  cognizabl-y,  adv. cognizance,  n.,  knowledge,  notice.  —  ME.  coni- saunce,  fr.  OF.  conoissance  (F.  connaissance), ‘knowledge’,  fr.  conoistre  (F.  connaitre),  ‘to know’,  fr.  L.  cognoscere;  see  cognition  and -ance.  E.  cognizance  was  refashioned  after  L. cognoscentia.
8340:Derivative:  comma,  tr.  v. command,  tr.  and  intr.  v.  —  OF.  comander,  (F. commander),  ‘to  command,  order’,  fr.  VL.  *com- mandare,  refashioned  after  mandare  fr.  L.  com- mendare,  ‘to  commit  to  one's  charge’,  fr.  com- and  mandare,  ‘to  commit  to  one’s  charge’,  lit. ‘to  place  in  one’s  hands’,  fr.  manus,  ‘hand’;  see manual  and  cp.  mandate.  For  the  change  of Latin  d  (in  mandare)  to  e  (in  com-mendare)  see accent  and  cp.  words  there  referred  to.  Cp. commend,  which  is  a  doublet  of  command. Derivatives:  command,  n.  (q.v.),  commandant (q.v.),  command-er,  n.,  command-er-ship,  n., commandery  (q.v.),  command-ing,  adj.,  com- mand-ing-ly,  adv.,  commandment  (q.v.) command,  n.  —  F.  commandc,  fr.  commander.  See command,  v.
9002:contrast,  tr.  and  intr.  v.  —  F.  contraster,  ‘to  con¬ trast’,  refashioned  after  It.  contrastare,  fr.  OF. contrester,  ‘to  strive  against,  dispute’,  fr.  VL.
9418:counterfeit,  adj.  —  OF.  contre  fait,  contre fet  (F. contrefait),  pp.  of  contrefaire,  ‘to  counterfeit’, fr.  contre,  ‘against’,  and  faire  (fr.  L.  facere),  ‘to make,  do’.  See  counter-  and  fact.
```


## [2026-09-14T01:24:08.980Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31684,31690p' KLN_1966.txt; echo \"=== leaves ===\"; python3 -c \"\nimport sys\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace')\nimport itertools\nlines=t.read().split('\\n')\nfor target,name in [(31684,'Raphael'),(33094,'room'),(33359,'rural'),(31829,'ream v')]:\n    c=sum(l.count(chr(12)) for l in lines[:target])\n    print(name,'line',target,'leaf',c,'-> printed p ~',2*(c-12),2*(c-12)+1)\n\""
}
```


### [2026-09-14T01:24:10.335Z] TOOL RESULT

```
rape,  n.,  refuse  of  grapes.  —  F.  rape,  fr.  ML. raspa,  fr.  WTeut.  *raspdn,  ‘to  scrape;  to  sweep off’.  See  rasp,  v. ,  and  cp.  words  there  referred  to. '  Raphael,  1)  masc.  PN.  2)  an  archangel  mention¬
ed  in  the  Apocrypha.  —  Late  L.,  fr.  Gk.  'Piora-
y{k,  fr.  Heb.  R^pha’el,  lit.  ‘God  has  healed’.  Heb. raphd,  ‘he  healed’  (whence  riphu'ah,  ‘medicine, remedy’,  marpe,  ‘healing,  cure’),  the  first  ele¬ ment  of  this  compound  word,  is  rel.  to  Syr. repha,  ‘he  healed’,  Arab,  rafa'a,  ‘he  darned, mended,  repaired’,  Ethiop.  rafaa,  ‘he  stitched together,  mended’.  For  the  second  element  in Raphael  see  El.
Raphalesque,  Raffaelesque,  adj.,  in  the  style  of the  painter  Raphael.  —  Formed  fr.  the  name  of Raffaello  Sanzio  (1483-1520)  with  suff.  -esque. raphania,  n.,  a  disease  causing  convulsive  con¬ tractions  of  the  limbs  (med.)  —  Medical  L., coined  by  the  Swedish  botanist  Carolus  Lin¬ naeus  (1707-78)  fr.  Gk.  patpavT?,  ‘radish’.  See rape,  the  plant,  and  1st  -ia.
Raphanus,  n.,  a  genus  of  plants  of  the  cabbage family  (bot.)  —  L.,  fr.  Gk.  pebpavos,  ‘cabbage’, which  is  rel.  to  pdbrui;,  ‘rape’.  See  rape,  the  plant, raphe,  n.,  a  seam,  suture  (anat.  and  bot.)  — ModL.,  fr.  Gk.  paprj,  ‘seam,  suture  (of  the skull)’,  fr.  partTsiv,  ‘to  sew  together,  stitch’, which  prob.  derives  fr.  I.-E.  base  *wer-p-, *wre-p-,  ‘to  turn,  twist,  sew,  spin’.  See  vervain and  cp.  the  first  element  in  Raphiolepis  and  in rhapsody.
Raphia,  n.,  a  genus  of  palms  (bot.)  —  ModL. ;  see raffia.
Raphiolepis,  n.,  a  genus  of  plants  of  the  apple family  (bot.)  —  ModL.,  compounded  of  Gk. pa<p(?,  ‘needle’,  and  Xenti;,  ‘scale,  flake’.  The first  element  is  rel.  to  pa qri),  ‘seam’;  see  raphe. For  the  second  element  see  leper, rapid,  adj.  —  F.  rapide,  fr.  L.  rapidus,  ‘tearing away,  seizing,  swift,  rapid’,  fr.  rapere,  ‘to  seize and  carry  off,  to  snatch  away,  to  seize,  plunder, ravish’,  which  is  cogn.  with  Gk.  ep^itTEoftat,  ‘to pluck  off,  feed  on’,  Alb.  rjep,  ‘I  strip,  rob’, Lith.  raples,  ‘tongs’,  ap-repiu,  ‘I  take,  seize’,  fr. I.-E.  base  *rep-,  ‘to  snatch,  seize’.  Beside  ♦rep- stands  prob.  *srep-,  *s(p-  in  Gk.  ap7rx£etv,  ‘to snatch,  seize’,  apnaS,  ‘rapacious’,  ip-avr;, ‘hook;  rake’,  apm),  ‘sickle’,  (Sprojtou,  ‘harpies’, lit.  ‘snatchers’.  Cp.  conception,  erepsin,  rap,  ‘to seize’,  obreption,  obreptitious,  rape,  ‘to  seize’, rapine,  rapt,  ratero,  raven,  ‘to  prey’,  ravin,  rav¬ ish,  subreption,  surreptitious,  usurp.  Cp.  also harpy,  sarmentose.
=== leaves ===
Raphael line 31684 leaf 692 -> printed p ~ 1360 1361
room line 33094 leaf 721 -> printed p ~ 1418 1419
rural line 33359 leaf 726 -> printed p ~ 1428 1429
ream v line 31829 leaf 696 -> printed p ~ 1368 1369
```


## [2026-09-14T01:24:18.387Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\n# print lines that are just numbers 1250-1450 between 31000 and 33500\nfor i in range(31000,33500):\n    l=lines[i].strip()\n    if re.fullmatch(r'1[23]\\d\\d',l): print(i+1,l)\n\" | head -40"
}
```


### [2026-09-14T01:24:19.633Z] TOOL RESULT

```
31007 1273
31070 1274
31071 1275
31104 1276
31154 1278
31186 1279
31209 1280
31293 1285
31349 1286
31360 1287
31391 1288
31501 1294
31502 1295
31549 1297
31587 1298
31652 1300
31800 1307
31866 1309
31907 1311
31954 1312
31971 1313
32011 1314
32012 1315
32054 1316
32055 1317
32106 1318
32107 1319
32154 1320
32165 1321
32203 1322
32204 1323
32256 1324
32275 1325
32306 1326
32380 1329
32576 1336
32691 1341
32727 1342
32817 1345
32840 1346
```


## [2026-09-14T01:24:23.342Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\nfor i in range(32900,33500):\n    l=lines[i].strip()\n    if re.fullmatch(r'1[34]\\d\\d',l): print(i+1,l)\n\""
}
```


### [2026-09-14T01:24:24.514Z] TOOL RESULT

```
32993 1353
33039 1354
33040 1355
33085 1356
33156 1359
33200 1360
33339 1365
33487 1373
```


## [2026-09-14T01:24:36.159Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN 465 area ===\"; python3 -c \"\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint(len(t))\nprint(t[465+24][:2500])\n\""
}
```


### [2026-09-14T01:24:37.234Z] TOOL RESULT

```
=== SYN 465 area ===
1545
rndlus, or- Sw. prydnad, smycke ChSl. ukraSentje q namentum OE gearwe SCr.  nakit, ures, ukras It. ornamento ME ornement Boh. okrasa Fr. parure NE adornment Pol. ozdoba, okrasa k Sp. adorno Du. versiering Russ. ukraSenie ¢ Rum. podoabi OHG  garawi Skt. bhigana-, alarikara- } Ir. cumlach, ornaid MHG gerwe, gesmuc Ay. pis-, pacsa- Nir. Grnaidhedcht, sciamh- NHG schmuck 6 acht W. addurnaid, trwsiad I Br. kinklou, bragerezou 0 Collective terms for articles of ‘adorn- 1.1) : adj. mundus ‘clean, elegant’ | ment’ are mostly based on still more (15.87).
Lat. orndtus, 6rndmentum (both words are used in the sense of ‘personal adorn- ment, embellishment’ as well as ‘fur- nishings, equipment’), fr. Ornare ‘put in order, equip, adorn’, for *drdindre : ordé (4nis) ‘order, row’, this perh. fr. the root *ar- ‘fit? in Grk. dpaploxw, Lat. arlus, ete., but details dub. Hence, di- rectly or new formations fr. vbs. derived fr. Lat. drnare, It. ornamento, Sp. adorno, Ir. 6rnaid, NIr. drnaidheacht, W. addurnaid, ME ornement (fr. OF. ornement), NE adornment (fr. OF. aournement, with spelling-pronunciation
: parer ‘gdorn, deck
j rare), 1 Lat. parare pre (it. Pr 929. Gamillscheg 673.
oa bs fr, Slavic, cf. ChSl. a Heol ozdoba (below, 6).
# jit. ‘building, construc-
f conulgim ‘build, erect’.
é parry § 5
aut’
sen 2.000: aie seiamhacht (also beauty ), fr ie earance’, Ir. scram, fr.
ad ‘shape, form’.
ramh Bs oe hama, {t. OTE oxtHe
Jat. schema,
sen 1.208. ised (also ‘dress, apparel’), fr.
+, ‘dress, deck out, trim, adorn’ be-
{ricst0 side early (rws ‘ornament, dress’, trwsa
ick, bundle’, fr. ME trusse ‘pack, bundle’ (fr. Fr. trousse). Cf. the special- ination in Fr., NE drousseau, orig. ‘bundle’ fr the same source. Parry-Williams 95, 161.
Br, kinklou (pl.), kinkladur, with vb. kinkla ‘adorn’, fr. some deriv. of OFr. diquer, clinquer ‘ring, clink’ (fr. Du. Hinken) like clinguant ‘gold leaf’. Henry 07. NED s.v. clinquant.
Br. bragerezou (pl., sg. bragerez), fr. bragal ‘parade, show off one’s clothes’, ong, ‘put on breeches’, fr. bragou ‘breeches’ (6.48). Henry 42.
4 ON skraut with vb. skreyta ‘adorn’, peth. : Sw, skyrta ‘boast’, Dan. skryde eae boast’. Falk-Torp 1033,
prgoi, Dan. (pryd arch.) prydelse,
ea with vbs. ON pryoa, Dan iW. . ¢ 7 : rid fale ee aN
7 magnificent in appear-
sae ‘proud’, whence vat. preuz) ‘e ae pied (nom. . prode b *pable, valiant’, fr. 4 abstracted fr, prod- "all-Torp 851 (but wr
nee’
esse ong REW
Lat. 59 8766,
OE earwe (
Urce),
Pl), OHG garawt, MHG
-0. In Public D
```


## [2026-09-14T01:24:37.352Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 روده ===\"; grep -n \"روده\" BQT_v2_pages.txt | head -20; echo \"=== BQT رفو ===\"; grep -n \"رفو\" BQT_v2_pages.txt | head -10"
}
```


### [2026-09-14T01:24:37.453Z] TOOL RESULT

```
=== BQT v2 روده ===
470: ‫کی که ازروی ناز وغمزه براه روده وبایشمعنی‬           ‫تر‬
2040:  ‫( عرمی‬    ‫یب‬   ‫‪ - ۵‬ظ ‪ .‬سختو‪ ,‬جهودانه‪ ,‬چرغند رونج» کیا مدار‪ ,‬گدك‪ .‬چرب روده »‬
3495:‫آفراعنزروت گونند ‪ -‬وچرب روده رایز گفته‌ا ند‬           ‫وزن طیش » بمعنی سرشت وخلقت و طعت‬
4291:            ‫‪۰‬‬   ‫تاباك شود‬    ‫سقشانند‬   ‫وغله را بدان‬        ‫روده باشد‬
4974:                                                          ‫روده ‪ -‬فتح اول و‬                         ‫چرب‬
8403:‫روده برةٌ قربه باشد که آن را قطعه قطعه کنند‪,‬‬       ‫بنتماول وثانی وسکون‌کاف»‬   ‫حسكت ‏‬
10583:      ‫کشف رود ورود‬‫گکارن و‬  ‫نزديك به ‪ ۰۰۰۰۲۳‬کیلومتر ھربح است ‪ .‬رودهای مهمی مانند اترك و‬
13884:                             ‫‪ ۴‬از ‪ :‬خنگه (هم) ‪ +‬يه ‪.‬‬                                ‫سروده که ازميان رفته است ‪.‬‬
13935:                                                           ‫‪ - ۱‬بمعنی سروده و خوانده شده ‪:‬‬
15559:‫روده‬       ‫و‬   ‫از شکنده‬    ‫انجه‬   ‫ەی‬
17867: ‫‪ 0‬درو دگر‪ -‬صم اول وقتح پنجم » از‪ :‬درود ‪ +‬گر(یسوند شفل) رك ‪ :‬دروده در و گر‪.‬‬
17892:‫درون اروده کنابه از صاحب دل‬                               ‫فارسی » مخفف درود گر الست که استاد چوب‬
20887:  ‫درضخة چاپ هرن‪« :‬روخ چکاد ‪.‬کامتی است فولوی ‪ .‬روخ روده باشد «چکادبالای پیشالی‬
20953: ‫دودآهنج‪.‬‬      ‫=‬       ‫آن «رودهنگه»‬                    ‫آ هنگه(ه‪.‬م‪.).‬ومخفف‬        ‫(«‪.‬م‪+ ).‬‬     ‫از‪:‬دود‬    ‫‪۳‬‬   ‫‪۷‬‬           ‫ی دودهنج* ‪1‬‬
23574:        ‫روده ‪( .‬هام‪1 ‎).‬‬     ‫=‬   ‫روت « لعن" امه ‪ +‬لشت»‬          ‫اور =‬    ‫لدز ص‬    ‫بمعٹی تخسن‬         ‫‪١‬‬
25270:  ‫‪0712۷021‬‬        ‫استی‬    ‫فاعلی) ویمعتی حال مکار روده‬            ‫آن ( يوند‬      ‫‪+‬‬    ‫)‬    ‫(رفتن‬        ‫از‪ :‬رو‬      ‫‪-‬‬        ‫‪۵‬‬
25400:        ‫‪.‬‬     ‫ارحنی غ ‪tor‬‏ (رود)«هوشمان ‪۷‬‬               ‫مسر روده رود)‪ .‬کردی ‪ ۵41‬بلوچی‪« ۵۲‬اسشق ‪۷۲‬‬
25412:                         ‫مفرد روده همگفته‌اند ‪:‬‬         ‫کوحار » نامبلوکی است و شهری است مابین‬
25428:‫» معروف انح‬      ‫سوده‬   ‫بروزن‬    ‫=‬   ‫زروده‬
25439: ‫روده کرده هم‌میگویند وبعربی سمیط خوانند‪.‬‬                                                             ‫کردد ‪*.‬‬
=== BQT رفو ===
34:‫دربارة لغات مربوط بلهجه‌های محلی وشاهدهای شان ونادر مرفوم‌دارند‪ .‬چندتن دعوت‌وبرا‬
13615:          ‫بر کش تو ازین خنبم نارنگد گرګیرم ‪.‬‬                          ‫برینك فررفوتم در عشق نو ای دلبر‬
23743:  ‫ربطی باکلمة هرخش» فارسی‌بمعنای تابش ندارد ‪ ».‬توصیف فردوسی ازرخش که نولد که‌درفوق اشاره‬
24463:‫رفیده د بفتح اول بروزن رسده ‪ ,‬لته‬                       ‫رفو ‪ - ۴‬بفتح اول و ثالی بواو مجهول‬
24487:   ‫معرب آن » رفو (یفتح‌اول وسکون دوم) قس ‪ :‬بونانی ‪ 0704163۲‬خ(یاطی کرد »‬                       ‫‪۴‬‬
24560:                                                                 ‫٭ رفوگر ‪ -‬نم‬
24562:                                                          ‫أ‬      ‫شغل‬     ‫رفو ‪ +‬کر ( یوند‬
24563:                                                            ‫و مبالفه ) ‪ ۰‬آنکه رفو کند ‪۰ ۱ ۰‬‬
24564:                                                                 ‫کیکه ‏ شخلش رفوکردن‬
27732:                                                 ‫ونابه از رفوم منجمان هم‌هت‪.‬‬
```


## [2026-09-14T01:24:45.758Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== tag near 25400 ===\"; awk 'NR<=25400 && /pdf page/{n=NR;p=$0} END{print n\": \"p}' BQT_v2_pages.txt; echo \"=== tag near 24487 ===\"; awk 'NR<=24487 && /pdf page/{n=NR;p=$0} END{print n\": \"p}' BQT_v2_pages.txt; echo \"=== 25390-25420 ===\"; sed -n '25390,25420p' BQT_v2_pages.txt"
}
```


### [2026-09-14T01:24:47.452Z] TOOL RESULT

```
=== tag near 25400 ===
: 
=== tag near 24487 ===
: 
=== 25390-25420 ===
            ‫(‪ )۳‬چك ‪ - :‬ابجد ‪.‬‬              ‫(‪ )۲‬جك ‪ - :‬بی‌نقعاه ‪۰‬‬               ‫(‪ )۱‬چك‪ :‬بگر حا‪.‬‬

                   ‫ورك‪ :‬اریبان در کتاب حاضر ولغت نامه‪.‬‬          ‫‪Jd homard‬صس‏ ‪۷۱۰‬‬             ‫=‬   ‫‏‪٩‬‬

      ‫لوخ‪ .‬و رك‪ :‬دوخ‪.‬‬    ‫رخ‬     ‫‪ ۳‬ےت رك‪:‬‬         ‫رك راه روح ‪.‬‬         ‫‪۴‬‬           ‫رك ‪ :‬روز‪.‬‬
                                                                                          ‫‪- ۴‬‬
   ‫‪ - ۱‬پپلوی‬              ‫‪ :‬روخ جکاد ‪.‬‬      ‫‪ ۲ :۱‬ص‪۸۹۱‬‬         ‫‪:‬ا‬
                                                               ‫اكسف‬
                                                                  ‫© _رك‪ :‬دوخ جکاد )‪ (۱‬ور‬
   ‫‏‪( ٤‬رود) “ پارسی باستان ‪« 12]218۲-‬بارتولمه ‪ ۰۹4۱2۰‬هندی باستان_‪( 58]679‬جربان آب»‬
        ‫‪.‬‬     ‫ارحنی غ ‪tor‬‏ (رود)«هوشمان ‪۷‬‬               ‫مسر روده رود)‪ .‬کردی ‪ ۵41‬بلوچی‪« ۵۲‬اسشق ‪۷۲‬‬
   ‫کنار دیده من‌همسو رود جنحون است‪:‬‬                 ‫‪ - ۲‬ازآن دمی که زچشمم برفت رود عرز‬
   ‫«حافظ شیرازی ‪. ۹۳۰‬‬
                   ‫آورود |رك‪ :‬لفت نامه ‪ :‬اروت] ورك‪ :‬زژده ‪.‬‬            ‫آرید =‬    ‫‪ _ 4۸‬امروز اروت =‬
                                                                                                 ‫‏‪٩‬‬
   ‫از‪ :‬رود‪ -‬بار ایوند مکان [ساحل])‪ .‬بهلوی ‪ « ۲2۵۸۵۲‬اسشق “‪۷۲٠‬‏ لغة بمعنی‬
                                                                                 ‫کنار رود ومنطقةٌ رودخاله‪.‬‬
  ‫؛‬    ‫‪mm‬‏ روفتن‬   ‫رقن‬    ‫) =‬    ‫مدن (یسوند مصدری‬        ‫‪+‬‬    ‫فتح دال ‪ ۰‬از ‪ :‬روب‬    ‫رو لیدی ‪-‬‬    ‫‪#‬‬

                                                                 ‫جلروب کردن ‪ .‬پاك ساختن ازکرد وغبار ‪.‬‬
    ‫سه‬                                                                                                   ‫رودزم‬

                         ‫مفرد روده همگفته‌اند ‪:‬‬         ‫کوحار » نامبلوکی است و شهری است مابین‬
‫رودلاخ ‪ - ۴‬بلام بالفکید وبخای‬                            ‫گیلان وقزوین‪ -‬وبمعنی جداول آب ورودخانهای‬
 ‫یطه دار زده ‪ ۰‬جابیکه دران رودخانه و جشمه‬
                                          ‫نق‬             ‫بز رکے وجابیکه درآن رودخاله (‪ )۱‬بیارجاری‬
                                                                                          ‫باشد ‪#.‬‬
                           ‫‪ 3‬زهاب مار باشد ‪۰‬‬

‫باشد»‬   ‫رونای‬   ‫بروزن سوزن»‬          ‫رودن‬
                                                         ‫رودزم ‪ -‬بكر () ثالك و تم‬
```


## [2026-09-14T01:24:52.853Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25420,25470p' BQT_v2_pages.txt"
}
```


### [2026-09-14T01:24:52.910Z] TOOL RESULT

```
                                                         ‫رودزم ‪ -‬بكر () ثالك و تم‬
‫وآن کاهی است که چیزها بدان رنگه کنند ‪1‬‬                    ‫زای‌فارسی وسکون میم نامرودخاله است‌مشهور‪.‬‬

 ‫‌ بادال ابجد بروزن‌هوشنگه‪,‬‬       ‫رودن‬
                                                         ‫رودساد ‪ -‬با سین بی‌قطه (‪ )۳‬بالف‬
                                                         ‫وسازنده‬   ‫مطرب‬      ‫نقطه‌دار(‪ )4‬رده‬    ‫ویزای‬     ‫که‬
             ‫باشد‬   ‫است که رونای‬        ‫یمه‌نی رودن‬
                                                                                                     ‫رگاوند ‪.‬‬
‫» معروف انح‬      ‫سوده‬   ‫بروزن‬    ‫=‬   ‫زروده‬
‫که اممای گوسفند وغره باشد ‪ - ۳‬وباین‌معنی‬
                                                         ‫‪ -‬باانی مجهول بوزن (ه)‬                 ‫دوك‬
                                                                                                  ‫ر‬
                                                         ‫ون جانوریست که از‬
                                                                         ‫وبند آ‬
                                                                              ‫گا‬‫خوبك ‪ ۰‬وشق ر‬
‫مرغ بابره ایرا نیزکوبند که پروموی او را‬                  ‫پوستش پوستین سازند ‪ .‬کوبند هر چند او را‬
‫رده بروغن بربان کرده باشند ‪ , ۴‬و انرا‬
                                    ‫بکاك‬                 ‫ووستش نفیس تر )‪(٩‬‏‬
                                                                          ‫بیشتر زنند فربه تر پ‬
 ‫روده کرده هم‌میگویند وبعربی سمیط خوانند‪.‬‬                                                             ‫کردد ‪*.‬‬
‫رورمتاا = بضم اول و سکون ثالی‬
                                                            ‫‪۳‬‬   ‫است‬   ‫روده‬   ‫جم‬   ‫‪۰‬‬   ‫رده‬   ‫بالف کش دہ ويون‬
‫مجپول ورای قرشت (‪ )۸‬و فتح میم و نون بالف‬
‫رکه‬
  ‫بازند )‪(٩‬‏ بمعتی انا‬    ‫بلفت زند و‬        ‫»‬   ‫کشیده‬    ‫رود گانی ‪ - ۷‬بروزن کوزمدانی(‪)۷‬‬
                           ‫بعربی رمان خوالند ‪.‬‬           ‫باشدویمعنی‬      ‫روده‬   ‫ممعنی رود کان‌است که مج‬



  ‫‌ن‪-‬قطه ‪.‬‬
         ‫(ی‪)۳‬یچك‬                  ‫(‪ )۲‬چك »چش ‪ :‬بسکون‪.‬‬                   ‫(‪ )۱‬چش‪ :‬رودخانهها ‪.‬‬
  ‫)‪ (٩‬چك» چش ‪ :‬فیس‪۰ ‎‬‬                   ‫‪.‬‬       ‫وزن‬
                                                  ‫بشر‪:‬‬
                                                     ‫(‪ )0‬چك ؛ چ‬                 ‫(‪ )4‬چك‪ :‬ویزا‪.‬‬
  ‫‪‎‬كچ ‪:‬‬   ‫(‪)۹‬‬               ‫( ‪ ) ۸‬چك ‪ :‬ورا ‪.‬‬                    ‫(‪ )۷‬چك » چش ‪ :‬کوزدالی ‪.‬‬
                                                                                                ‫زلف و مارند‪.‬‬


           ‫از ‪ :‬رود ‪ ۳‬لاخ (یسوندهکان)‬             ‫‪۳‬‬        ‫از ‪ :‬رود گان ‪ +‬ی (ست)‪.‬‬                ‫‪۱‬‬

   ‫‪ - ۴‬پپلوی)‪«۵۲‬اونوالا ‪(6]۸۵۳ ۹۱46۰‬امماه واحشاء)» کردی‪ .1۷۷1۱۲‬بلوجی )‪۵۲‬و‪۵۲‬‬
  ‫‪ ۴‬ر=ود کت معرب آن روذق «بمون(الفرس) السمرط‪:‬‬                                ‫سریکلی ‪« 412۲‬اسشق ‪۸۷4‬‬
‫‪-‬میط هوان بلقی‬
             ‫ا©لس‬                       ‫الروزق » «جاحظ‪ .‬البیان‌والتبین چاپ سندوبی ج‪ ۱‬ص‪. >۲۳‬‬
  ‫بالحیوان بعدن محه‌فی‌الماء الحارئم نتف عله صوفه‌آورشه او شعره‪ .‬رك‪ :‬السان والتیبین اشا ج‘ وأین‬

             ‫آن تک‬       ‫ویرهای‬      ‫کردن است که مر غ را درآب گرم اندازند‬             ‫(اورت)‬   ‫«اورید»‬   ‫همان‬


  ‫‪ .‬انار « بوتکر ‪> ۵۰۱‬‬          ‫‪ .‬پهلوی ‪۲802‬‬          ‫‪- ۱‬مز ‪8۵(2)2۳۲۵۲. ۵۵۵۳۵۲۵۲.‬‬
                                                                                                ‫ورك ‪:‬روهنا‪.‬‬
```


## [2026-09-14T01:25:09.621Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nlines=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor tgt in (24463,24487,25428,25456):\n    c=sum(l.count(chr(12)) for l in lines[:tgt])\n    print(tgt, 'leaf', c)\nprint('total', sum(l.count(chr(12)) for l in lines))\n\"; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3"
}
```


### [2026-09-14T01:25:10.793Z] TOOL RESULT

```
24463 leaf 415
24487 leaf 415
25428 leaf 430
25456 leaf 430
total 683
```


## [2026-09-14T01:25:21.003Z] TOOL CALL #30: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-14T01:25:21.067Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

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
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-14T01:25:32.185Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint('leaves',len(t))\nfor i in (0,1,2,3,680,681,682):\n    print('--- leaf',i,'---')\n    print(t[i][:300].replace(chr(10),' | '))\n\""
}
```


### [2026-09-14T01:25:33.374Z] TOOL RESULT

```
leaves 684
--- leaf 0 ---

--- leaf 1 ---
                                         ‫‪7‬‬ |  |                           ‫رن‪۳‬‬ |     ‫نات‬ |       ‫ا م‬ |               ‫لض‌بال ‪ ۰ ۲۶‬رک‬ | ‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬ |                                      ‫‪7‬‬ | ‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬ |  |                       ‫‪۴2 ۱‬‬ | 
--- leaf 2 ---
                   ‫م‬ ‫و‬ | ‫نآکو سخنیم بیاموزد مرا‬ |                        ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬ | ‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬ |  | ‫داربان مقدمهٌ مجلد اول برحان قاطع ( صفحدٌ صد وسی ودو ) نگارنده از‬ |                                    
--- leaf 3 ---
                                                     ‫‪ar‬‬ |                                      ‫مااضحاذفی‪‎‬‬ |  ‫است‪‎‬‬    ‫و رساله‌هابی استفاده شده‬   ‫نیز ( از ‪5‬‬    ‫در محلد دوم (وطماً مجلد سوم‬ |  |  | ‫اسم‪‎‬‬    ‫اسك‬        ‫ای ‪ 3:‬تنامده ‪.‬‬    ‫وریت ماح مندرج در پابان دق‬           ‫اا‬    
--- leaf 680 ---
  ‫وفاجر و کنه کار وید کاره ونامه صاه باشد ‪۰‬‬       ‫را ګوبند که سودا‬   ‫کی‬    ‫سیه هقز »‬ |  |  | ‫انی‬     ‫اوفلتاوح‬       ‫ر‬ |                        ‫پ‪4‬ک"‪-‬‬ |                            ‫سیه‬                    ‫داشته‬       ‫الغ‬ |                                                                 ‫
--- leaf 681 ---

--- leaf 682 ---
              Mohammad Hosayn ebn ~e Khalaf |                                    de Tabriz |  |  |             BORHAN                                . QATE |                 ) DICTIONNAIRE DE LA LANGUE PÊRSANEÊ j |                                    maras    Per |  |  |  |  | Edıtion   60۱۵۲۵۲6۵۱    revue. antêdée
```


## [2026-09-14T01:25:51.284Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol3/4 Raphael ===\"; grep -n \"Raphael\" FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -10; ls FSD_vol*.txt"
}
```


### [2026-09-14T01:25:51.352Z] TOOL RESULT

```
=== FSD vol3/4 Raphael ===
FSD_vol3.txt:201679:r» 1 . List or Puiim Pum-peiny, 1 pnm-pori; 2 pftm-usr^. Raphael (»/*l837-
FSD_vol4.txt:4230:SofnethiQR  bc^ido  genius  drew  all  these  men  and  aeorea  of others  to  Raphael  Sarah  K   Bolton  Famoua  European  Arltata, EaphatlP  IH  [t  T   cl
FSD_vol4.txt:6703:Sem'mer-Ing,  l   scm'er-in  2   gSm'er-lng  n   A   mountain between  Austria  and  Styria  pierced  by  several  tunnels Semmos,  1   semz  2   s^mg  Raphael  (*/s  1809-*/jol87D An  American  Confe  erate  naval  officer,  captain  of  the  Con- federate cruiser  Alauauia
FSD_vol4.txt:28945:often  hardly  to  be  distinguished  from  p-oee-  The  Lteraturea  of  SyZil  zne-frlst,  1   Sim  l-trlst*  2   Sjui  e-tri^,  n Gc-manj'  and  Ea^And  the  music  of  Wagner  and  the  ii-e-  studlous  of  symmeTy.  sym^me-trl'clanj  {RareJ Raphaelite  movement  had  some  share  m   the  development  of  Sjm'niO-friZC,  1   Sim'l-trcxz,  2   sjm'e-triz,  tf  {*T22ZEP, sj-mboLsm  but  its  heralds  m   France  were  A   de  iigay  and  above  -THIz'lXG  1   To  make  svmm^trical  07  proporiioasi- Ch.  -nc  lreulworor  lie»-hool  TO  Stfchsn,  sj-m'rae-tTlset.-sjTii"me-trI-ia'[o--S3'itlon.  n
FSD_vol4.txt:110332:1903:  Chinese  Board  of  Commerce  created  1837:  Raphael  Pumpelly,  American  geolo- by  an  edict  ^   gist  and  writer,  born.
FSD_vol4.txt:111668:1868*  Battle  of  Alcolea*  Spanish  royalists  1814;  Convention  of  Vienna  signed, under  Novaliches  defeated  by  Insurgents  1834:  Alexander  Raphael,  ehenff  of  Lon- under  Serrano  don  first  Catholic  to  hold  office  since  the
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
```


## [2026-09-14T01:25:53.060Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA rafw ===\"; grep -n -i \"rafw\\|rafu\\|رفو\" incoming/PLA/PLA_pages.txt | head -10; echo \"=== AFM رفو ===\"; grep -n \"رفو\" AFM_pages.txt | head -10; echo \"=== TAD رفو ===\"; grep -n \"رفو\" TAD_pages.txt | head -10"
}
```


### [2026-09-14T01:25:53.147Z] TOOL RESULT

```
=== PLA rafw ===
=== AFM رفو ===
97:ان العرب كثيرًا ما يتصرفون تصرفاً غرياً في الالفاظ الاعجمية من ذلك
=== TAD رفو ===
196: ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
878:‫«بجرفويخه» وفي الفارسية «جوخا» وهو نسعج منصوف صفيق‬
1226:                                        ‫اليونانية ‪0608‬م خاط‬         ‫في‬     ‫ر فارفو‬
1748:‫طاق ‪ -‬فارمي دطاق» تعناةقنوق رفو وقاطرة وسد ويهدظافحه»‬                       ‫‪١‬‬
1945:                                            ‫فرفور ‪ -‬ابطالى ‪ ]8118412‬وهو الفراسشة‬
```


## [2026-09-14T01:26:01.204Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD 1218-1232 ===\"; sed -n '1218,1232p' TAD_pages.txt; echo; echo \"=== BQT 24455-24500 ===\"; sed -n '24455,24500p' BQT_v2_pages.txt"
}
```


### [2026-09-14T01:26:01.282Z] TOOL RESULT

```
=== TAD 1218-1232 ===
         ‫‪1‬‬                                                                   ‫لد‬


             ‫رصيد ‪ -‬لفظةعامية تستعملبا التجارمأخوذةمن الابطالية ‪ 8415‬ومعناءالباز‬
                              ‫اة‬
                               ‫بلارا»د به‪٠‬و‪١‬ق‏ي‬
                                              ‫للا‪-‬رفايمية هرط‬
                                                            ‫راّط‬
                                        ‫اليونانية ‪0608‬م خاط‬         ‫في‬     ‫ر فارفو‬

                                           ‫فل‬
                                            ‫رار‬‫درص‬
                                                 ‫عا‬
‫تَوْخدذ للنسل وفي العبرانية‬           ‫ييل‬
                                        ‫خوه‬

=== BQT 24455-24500 ===

‫کون دکه آن شش سار کوچك باشد که در‬                      ‫=فتح اول بروزن زبان * شفیم‬
                                                                                ‫رفان ب‬
         ‫‪.‬‬   ‫نباند‬
                 ‫ویاثر‬
                     ‫خعرب‬
                        ‫کوهان ثور است وب‬                                          ‫وشفاعت کننده باشد ‪¥.‬‬

‫رفیده د بفتح اول بروزن رسده ‪ ,‬لته‬                       ‫رفو ‪ - ۴‬بفتح اول و ثالی بواو مجهول‬

‫و کهنٌچند باشد که بره‌ثال کردبالشی درهمدوز ند‬           ‫رسیده » پیوند شال وجامةٌ پاره وسوراخ دارباشد‬
  ‫وخمیران‌را بربالای آن کترانیده برتنوربندند‪.‬‬                                    ‫بنوعیکه مملوم شود (‪)۱‬‬




                                                      ‫معلوم نشود ‪.‬‬        ‫‪-‬که‬
                                                                            ‫ع‪:‬ی‬
                                                                              ‫و‪۱‬‬‫ب)نخم‬
                                                                                    ‫(‪۱‬‬
   ‫‪ - ۱‬تهرانی وکیاکی ]‪( 2۲‬طافچهُ اطاق تزدبك بقف)‪ .‬معرب آن هم رف ( بفتح اول‬
                                                            ‫‪:‬‬   ‫‪۹۳6‬‬       ‫‪۱‬ص‬     ‫وتشدىف دوم ( رك‪ :‬دری‬


              ‫اررو ‏‬
                   ‫مخبا‬
                      ‫و با‬
                         ‫ارش‬
                           ‫بفسی‬
                              ‫بت‬                          ‫کند مشحون همه طاق و رف آن‬
   ‫‪۶‬سعود سعد لاهوری ‪٤۲۲‬‏ > ‪.‬‬
                           ‫م‬
   ‫معرب آن » رفو (یفتح‌اول وسکون دوم) قس ‪ :‬بونانی ‪ 0704163۲‬خ(یاطی کرد »‬                       ‫‪۴‬‬
                                                         ‫‪ :‬رمه ‪.‬‬     ‫رك‬    ‫‪۴‬‬          ‫‪۸‬‬   ‫( انفی»‬     ‫دوخت‬

  ‫‪ #‬وفتار ‪ -‬بفتح اول‪ ,‬حاصل مصدر رفتن (ه‪ .‬م‪ ).‬روش» سیر » ح ركت ‪ -‬سلوك طرز‬

                                                                               ‫عمل شیوه ‪.‬‬           ‫حر کت_طرز‬
   ‫‪ #‬رفتی ‪ -‬بفتح‌اول و سوم » چهلوی ‪ 02627‬از ربشة ‪ « ۷2۲‬نیبر کے ‪۰ ۰۹۱‬او“ستا‬
   ‫ریعة ‪( 08۲ -‬رفتن) (‪ )0‬فی‪ :‬لانینی ‪ . ۵۳6۳‬لیتوابی ‪ , 14۵۱1۳6۲‬لتویی ‪( ۷06۲‬خزبدن )‪.‬‬
   ‫کردی ‪ ,01۲۷6۲ ۰‬بلوچی ع ‪ 82۷70۲ , 22۵۲‬و ‪ .827۳2۲‬وخی ‪ ۸۷۰ 7125]6۲‬سربکلی‬
   ‫تفییر جا ومکان دادن» رحلت‬          ‫ن‪:‬‬
                                       ‫ردکت‬
                                          ‫کا؛ح‬
                                             ‫د«اسشق ‪ ۹6‬ورك‪ :‬هوبشمان اس‬                            ‫‪0‬‬
                                                                      ‫کردن » سر کردن » کنر کردن ‪.‬‬
```


## [2026-09-14T01:26:28.591Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T01:26:28.598Z] TOOL RESULT

```


```


## [2026-09-14T01:26:32.709Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%85",
 "prompt": "Give the full Persian etymology section for شکم (šekam): Middle Persian form, Proto-Iranian/Proto-Indo-Iranian reconstruction, cognates, and any cited authorities (Hasandust, MacKenzie, Cheung). Also any mention of Avestan uruθwan- or of a root meaning 'bend'."
}
```


## [2026-09-14T01:26:34.689Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D9%87",
 "prompt": "Give the full Persian etymology for روده (ruda) 'intestine': Middle Persian form, Proto-Iranian and Proto-Indo-European reconstruction, cognates (Avestan, English 'reed'/'read'?), and cited authorities."
}
```


### [2026-09-14T01:26:36.825Z] TOOL RESULT

```
# Persian Etymology for شکم (šekam)

Based on the Wiktionary content provided, here is what is explicitly stated:

**Middle Persian origin:** The word derives from Middle Persian *𐭠𐭱𐭪𐭬𐭡* (aškamb).

**Limitations of the source:** The Wiktionary entry contains no additional etymological details beyond this Middle Persian form. Notably absent from this particular page are:

- Proto-Iranian or Proto-Indo-European reconstructions
- References to cognates
- Citations of scholarly authorities (Hasandust, MacKenzie, Cheung)
- Mention of Avestan *uruθwan-*
- Discussion of root meanings like 'bend'

The entry simply states: "From Middle Persian _aškamb_" without further etymological development or comparative linguistic analysis.
```


### [2026-09-14T01:26:39.447Z] TOOL RESULT

```
# Persian Etymology of روده (rōda/rude)

Based on the Wiktionary entry provided, here's the available etymological information:

## Direct Etymology

The entry states: "From Proto-Iranian *Hrawtáh, from Proto-Indo-Iranian *Hrawtás."

## Limitations of Available Information

The source document does not provide:
- A Middle Persian intermediate form
- Avestan cognates
- English cognates (such as "reed" or "read")
- Cited historical authorities beyond the reference works listed

The etymological chain given traces only back to the proto-language level, without intermediate historical stages or comparative Indo-European evidence. The "Further reading" section lists historical dictionaries and lexicons but does not elaborate on the etymology itself.

To obtain the comprehensive etymological details you're seeking—including Middle Persian forms, Avestan parallels, and Proto-Indo-European connections—you would need to consult specialized historical linguistic sources beyond this dictionary entry.
```


## [2026-09-14T01:26:48.914Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp && for w in \"%D8%B1%D9%88%D8%AF%D9%87\" \"%D8%B4%DA%A9%D9%85\" \"%D8%B1%D9%81%D9%88\"; do echo \"=== $w ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | sed -n '1,200p' | grep -n -A6 -i \"Persian\\|etym\\|inh\\|der\\|bor\" | head -60; done"
}
```


### [2026-09-14T01:26:50.598Z] TOOL RESULT

```
=== %D8%B1%D9%88%D8%AF%D9%87 ===
14:===Etymology===
15:{{bor+|ota|fa|روده|tr=rude|t=intestines}}.
16-
17-===Noun===
18-{{ota-noun|tr=rude}}
19-
20-# [[intestine]], [[bowel]], the [[alimentary canal]] of an [[animal]] through which [[food]] passes
21-#: {{syn|ota|باغرساق|tr1=bağırsak|معی|tr2=miʿa}}
--
34:==Persian==
35-{{wp|fa:}}
36-
37:===Etymology===
38:From {{inh|fa|ira-pro|*Hrawtáh}}, from {{inh|fa|iir-pro|*Hrawtás}}.
39-
40-===Pronunciation===
41-{{fa-IPA|rō`da}}
42-
43-===Noun===
44-{{fa-noun|cls=رودَه|pl=روده‌ها}}
--
48:====Derived terms====
49-* {{fa-l|پَس‌رودَه|t=colon}}
50-
51-====Descendants====
52-* {{desc|klj|rôda}}
53-* {{desc|ota|روده|tr=rude}}
=== %D8%B4%DA%A9%D9%85 ===
1:==Persian==
2-
3-===Alternative forms===
4-* {{alt|fa|شکنب|tr=šekanb}}
5-* {{alt|fa|اشکم|tr=eškam}}
6-* {{alt|fa|شیکم|tr=šikam||dialectal}}
7-* {{alt|fa|کم|tr=kom||dialectal}}
--
9:===Etymology===
10:From {{inh|fa|pal|𐭠𐭱𐭪𐭬𐭡|tr=aškamb|sc=Phli}}.
11-
12-===Pronunciation===
13-{{fa-IPA|šikam}}
14-* {{audio|fa|LL-Q9168 (fas)-Darafsh-شکم.wav|a=Iran}}
15-
16-===Noun===
--
25:====Derived terms====
26-* {{l|fa|شکمی|tr=šekami|t=abdominal}}
27-* {{l|fa|شکمو|tr=šekamu|t=voracious}}
28-* {{l|fa|شکم‌گنده|tr=šekam-gonde|t=potbellied}}
29-* {{l|fa|شکمبه|tr=šekambe|t=rumen}}
30-
31-====Descendants====
--
38:===Etymology===
39:{{bor+|ur|fa-cls|شِکَم}}, from {{der|ur|pal|𐭠𐭱𐭪𐭬𐭡|tr=aškamb|sc=Phli}}.
40-
41-===Noun===
42-{{ur-noun|m|head=شِکَم|hi=शिकम}}
43-
44-# [[belly]]
45-# [[abdomen]]
=== %D8%B1%D9%81%D9%88 ===
1:==Persian==
2-
3:===Etymology===
4:{{bor+|fa|ar|رَفْو|tr=rafw|t=finedrawing}}
5-
6-===Pronunciation===
7-{{fa-IPA|rafū}}
8-{{fa-regional|رفو|رفو|рафу}}
9-
10-===Noun===
```


## [2026-09-14T01:27:01.467Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp && echo \"=== PI Hrawtah ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Iranian/Hrawt%C3%A1h&action=raw\" | head -60; echo \"=== fa رود ===\"; curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%B1%D9%88%D8%AF&action=raw\" | grep -n -B2 -A6 \"Etymology\" | head -60"
}
```


### [2026-09-14T01:27:02.993Z] TOOL RESULT

```
=== PI Hrawtah ===
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1112 cp1112, Varnish XID 2754799<br>Upstream caches: cp1112 int<br>Error: 404, Not Found at Mon, 14 Sep 2026 01:27:02 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.22</details></code></p>
</div>
</html>
=== fa رود ===
2-==Old Tati==
3-
4:===Etymology===
5-Cognate with {{cog|lrl|رود|tr=rud|t=son}} and {{cog|luz|رود|tr=rūd|t=child, offspring}}
6-
7-===Noun===
8-{{head|xme-ott|noun|tr=rud}}
9-
10-# {{lb|xme-ott|Old Azari}} [[son]]
--
16-{{wp|fa:}}
17-
18:===Etymology===
19-{{etymon|fa|:inh|pal:lwd<ts:rōd><t:river><ety:inh<peo:𐎼𐎢𐎫<ts:rautaʰ⁠><t:river, torrent><ety:inh<ira-pro:*hráwtah>>>>|text=++}}. Cognate with {{cog|yai|рута}}, {{cog|sgh-ros|рӯд}}, {{cog|yah|рәд}}, {{cog|isk|ру̊чик}}.
20-
21-===Pronunciation===
22-{{fa-IPA|rōd,rūd|ir=rūd}}
23-
24-===Noun===
--
55-[[File:Jhelum River-Pakistan.jpg|thumb|'''رُود''']]
56-
57:===Etymology===
58-{{etymon|ur|:bor|fa-cls:رُود|text=++}}
59-
60-===Pronunciation===
61-* {{ur-IPA|rūd}}
62-
63-===Noun===
```


## [2026-09-14T01:27:20.285Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Bauch ===\"; grep -n \"Bauch\" HRN.txt | head -20; echo \"=== HRN sikam ===\"; grep -n -i \"ikam\\|kamb\" HRN.txt | head -20; echo \"=== HUB ===\"; grep -n -i \"ikam\\|kamb\\|Bauch\" HUB.txt | head -20"
}
```


### [2026-09-14T01:27:20.383Z] TOOL RESULT

```
=== HRN Bauch ===
7424:skr. kuksi- 'weiblicher Leib' (ai. allgemein 'Bauch,
10757:'Bauch*.
=== HRN sikam ===
7727:gomesy syr. LW. IS?"»?!:!, oss. LW. kambec, kambec.
21148:kambec 888.
=== HUB ===
876:= arm. kust 'Bauch, Weichen, Seite* und phi. kiist,
1392:arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
1394:patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
1397:persischen wurde *patskamb zu *paskamb, ehe pat-
1663:kommen doppelt vor!), 339, osset. dxtong 'Bauchgurt*,
3107:kamna-, ^kanbiyah--, *kanbista- (= zd. kambiSta-), vgl.
8953:auf ap. *amakam = zd. ahmakem^ skr. asmcikam zuriick-
9055:kambistem; nam *feucht' = ap. *namna' = idg. *nabhna-y
9171:paskam 'domus aestiva' = arm. patskam, patskamb *6emach*
9172:= ap. *pati'skamba' (oben p. 41).
9189:arisch *natnbha' sein k5nnte ; Sikam (A. M. '^S, 6) == Sikanb
9190:*Bauch', phi. Sk(u)mb ZPGl. 10, 7; Damavand (Pird. I, 61),
9636:paitivad-, Im Ap. bestand also *dviikam (ace.
```


## [2026-09-14T01:27:22.474Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY شکم ===\"; grep -n \"شکم\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY روده ===\"; grep -n \"روده\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY latin index ===\"; grep -n -i \"ESKAM\\|SHEKAM\\|RUDE\\|ROUDE\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T01:27:22.631Z] TOOL RESULT

```
=== ARY شکم ===
3146:معنی اين واژه در زبان ژرمنی: کیسهشکم.
3361:۱- معنی اين واژه در روسی و چند زبان دیگر: شکم.
9148:: چم اين واژه در انگلیمی نوین: شکم جانور
=== ARY روده ===
850:نیز از ریشه‌ی ایرانی هستند. مثلاً نام رودهای «دن» (00/1) و «دونتز» (0027875) و «دونپر)
1052:ویژگی‌های ابر انسانی ضامن خوبی محصول و زایندگی دام‌ها و پر ماهی بودن رودها و فراوانی
1147:حاوی سرودهای نیایشآمیز بنام «پشت‌هاء (۷۸81778) و وردهایی برای طرد دیوها پنام «ویدیوداده ...۰
9110:۰/_روده رودخانه
=== ARY latin index ===
3335:‘REFERENCES chan BRUDER (GERMAN) galt
6692:(CRUDE) 109, (RAW) 129 AMARUS LATIN) 3
```


## [2026-09-14T01:27:28.528Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY 9100-9160 ===\"; sed -n '9100,9160p' incoming/ARY/ARY_pages.txt; echo \"=== pdf tag ===\"; awk 'NR<=9110 && /pdf page/{n=NR;p=$0} END{print n\": \"p}' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T01:27:29.611Z] TOOL RESULT

```
=== ARY 9100-9160 ===
سانسکریت (54۸/507): 1072۹ ایرلندی کهن (9ل1# 012): 317
8۸8 ,فکلم1.02 برتونی (270۸ل8): آجهدتاما
ارمنی (/4۵/8/140): ۰ - 8 تالم
یونانی 0750): ۸35 پسگشت‌ها اک ند
اه لاین ییتمه: ۷5 9 ۸0808000
اسپانیایی امعم نار 5۸ 5 (۸83۸3۵) 1
پرتغالی (۳07707010885): 5۸ 5 ([۲0) ماد ها
دانمارکی (0۸۷/377): 7۸ برهان قاطع : ۹۶۸
سوئدی (5772/57). 7۹۷
[pdf page 309]
۰/_روده رودخانه
اوستایی (/4887۸): از هلندی (073): 1 نوی
۸۸۸7 اسلاوی کهن (ع۲1اشا؟ نابز صاه):
پارسی باستان (۲28۶14(۷ صا0): 8۸۲1۸ 0 ه577
پهلوی (۸47ا۳۸): 0 ,207 لهستانی (۳0(/53): ندداا با ان
کردی (0[57/(): ,30 روسی ((#18514): 85777۸
بلوچی (#1قتلمه): 37 چک (بن25): هه
افغانی (پشش) (/۸۳0۸(۷): 0 اسلواکی (81.01۸0): 8158۸
سانسکر بت (54/۷55/7):_ ,ل88 ,584۷۸31 لینرانی (40 4۸ 517177:72 ,8۸۷511
ادن لنونی (لتی) (71۵۸0ما): 5۸۸
ارمنی (۸7042/1421): 07 نا رای بان
پرنانی (0۵20): 7381 ایرلندی کهن (لادتة[ 0): 577۸13184
ایسلند یکهن (/۸2 5010۸۷ ضام). ولزی (7۴1): زاره نت
3 ای ان
ساکسرنی کهن ((2200 طا۵): 857801 پسگشت‌ها برد ۲
فریزی کهن (۲/94۷ صزم): 978300 03 ق۶006
آلمانی کهن (/0520/۸0 زاب صا0): |1075 (5788۸34) +81
اد ان 1 (8183) داد ها
آلمانی (022۵/2)+ ای ان 4142 هی
انگلیسی کهن (8۸۷0/3(7 صا۵): 8783۸31 4 (30ف8785) 0/05
انگلیسی (4لول6(/0): 1 ان 46 (31ه5775) +547
دانمارکی (0۸0۷/8): آبازا ان 130 :7 :
سوئدی (8/80157): رای ان 279 ۸0
نروژی (۸/0/۴0۸7)+ ان برهان قاطع : ۹۶۹
بادداشت:
این واژه در برخی زبان‌های هند و اروپایی (ثلاً یونانی) چم جاری بودن را نیز دارد.
[pdf page 310]
۹
۲۱۱/۶ ۱
ِ

! پهلوی (/4ال2۸): ۸0716 ,30 ,20016 هلندی کهن (تلآتاظ صا0): 100
کردی (80/51). رای
1 بلرچی (التل‌نالمه): 5 ,8077 پسگشت‌ها رده اد ان اد
۱ افغانی (پشتو) (/4۳037): ۸10۸ زر کر ۳
انگلیسی کهن (8۸/015/0 ۰:00 ۸5۸0۸ 0 (۳18871۲۴]) دا ام
انگلیسی (7ل5لل8(/01): زا دی برهان قاطع + ۹
پادداشت.
: چم اين واژه در انگلیمی نوین: شکم جانور
1 :07۳7103۸ 5۳۵۲5۲ 02۳02۵ 5130878 ۷8۵۷۷ 7158
۱
۱
۱ اوستایی (4789740): ۸ بونانی 07280): 180665
پارسی باستان (287500 0۵10): ,۸06۸ لاتین ((اما: نان تا
: الا ناه
پهلوی (۲7الل۸): 306 پسگشت‌ها : هار درد
کردی (4021574): 7 ,81273 0 2000
۱ بلوچی (اللعتا :8۸‏ ۷۶۸3 9 (0۸3) :25
۱ افغانی (پشتر) (اللهتا۵70: ۰ 300 ,80513 1 ,60 8۸0
۱ ی سانمکر 160859 نش 16 برهان قاطع : ۹۱
۷ ری (۸۸/۵(۷۸۸: ۱۵ ی 1015
=== pdf tag ===
9109: [pdf page 309]
```


## [2026-09-14T01:27:57.713Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"raph.a-el\\|Ra'pha-el\\|rapha-el\" FSD_vol3.txt | head -10; echo \"---\"; sed -n '201670,201690p' FSD_vol3.txt"
}
```


### [2026-09-14T01:27:57.860Z] TOOL RESULT

```
213534:- Mar'ra-el-lt''lsm, Raph'a-el-lt''lsm. n.
---
pump, especially of a wooden pump p.-trect.— p.*
atopper* n JVaut A plug for stopping a pump-barrel —
p. •thunder* r (U 8) The bittern; thunder-pumper — p.^
well* n SMp^uilding A easing or onmpartment. In the
hold of a vessel, containing the pump-stocks and usually a
strainer - rotary p.. eee rotary — hprengel p.* see
MBRcnfRY-puMF — unllmiCed p.* a deep-well pump oper-
ated from the level of the ground aboveKxt 1: al8le;aa a ottt; 0 ll: IQ afeud, ffain; go; Jet; q astnj;; to; Ailp: Chin, Oils; ajure; F. boh dttne; s » loch. t, obBoleteit, variant. pulse
Kay 2: bdbk, bdbt; fyll, rule, cQre, b^t, bQru; All, bhy ; « a k, hem, ink; r » z; Chiu, this; F. boh, dttne; u a loch. PUDChlnellO
r» 1 . List or Puiim Pum-peiny, 1 pnm-pori; 2 pftm-usr^. Raphael (»/*l837-
pumpu not deftned below, as air-pump. •/ioin23) An American genli^st, author, and explorer
POBCB*PDifP. etc , see vocabulary place 1 pump'er, 1 punip'ur, 2 pQinpVr, n 1. One who or that
^**®*'‘ ?'**‘P‘*®*' ®'’ ®** ^hieh pumps 2. An oil-well in which a pump I8
rMifnn*nw*nr^Mri^ muT “**' •*^*^*®** puinp (a uscd. as (listiiiauiMhed trom one that flows
S?thln tho?J2dSk iTSLrtftiM Prowure puni'per-nlrk«el. I mim'p8r-filk*l 2 pam'|ier-nlk‘I. ri fO 1
aupe D (J mtliS.mn?hhfrfn? i A bwad of coarse unlnilted r> e. usuall\ heav ^ . arid, nourlsh-
auro aotiuu direetiv uoon 7 “ l«K.HUd wholesome, but not eusllv diaesled. orlKlimlly used
ISS^ln n bored wein chSuUftiM n i *® p. (for pj peasants In Germaiij . espeelalb In iwiphaliu. but now
SStrtruaal Sumo L fofnnl SSn.?; ^ « widely used as a delleateHRoii article I * c; . orliflnullv dolt.
SSSSSr of*a?ml!?r SSiiruiiS blockhead. < pumpir. sound of a full (v pumpir, full). +
nSSia%aJes\ JoSSito^^ »»*»’«* «' ^’icoiaus Nicholas 1
```


## [2026-09-14T01:28:07.416Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='FSD_vol3.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nnums=[(i+1,l.strip()) for i,l in enumerate(lines) if re.fullmatch(r'(1[5-9]\\d\\d|2[0-4]\\d\\d)',l.strip())]\nprint('markers found:',len(nums))\nprint(nums[:10], nums[-5:])\nEOF"
}
```


### [2026-09-14T01:28:08.890Z] TOOL RESULT

```
markers found: 94
[(39536, '1578'), (41918, '1584'), (52123, '1610'), (54052, '1893'), (54060, '1883'), (54064, '1805'), (61990, '1631'), (62729, '1640'), (74308, '1679'), (78325, '1684')] [(225493, '2074'), (227760, '2080'), (238697, '2110'), (251908, '2148'), (253320, '2159')]
```


## [2026-09-14T01:28:12.037Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='FSD_vol3.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nnums=[(i+1,int(l.strip())) for i,l in enumerate(lines) if re.fullmatch(r'20[3-7]\\d',l.strip())]\nprint(nums)\nEOF"
}
```


### [2026-09-14T01:28:13.479Z] TOOL RESULT

```
[(216580, 2050), (223092, 2068), (225493, 2074)]
```


## [2026-09-14T01:28:15.764Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '216580,216780p' FSD_vol3.txt | grep -n -i \"raph\\|heal\\|Heb\" | head -30"
}
```


### [2026-09-14T01:28:15.852Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:28:17.791Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '216575,216600p' FSD_vol3.txt | cut -c1-300"
}
```


### [2026-09-14T01:28:17.864Z] TOOL RESULT

```
rank, n 1. A seines nf obje>etM range el in a lim* or row ,
a range Spe*cif (]) Mil («) A lim of seildiers drawn
lip sleie liy Hide uppemnd to file (/>) Degree of offlclitl
■tandlng, ospttlttily lu the navy and army la the navyRanke Kwr l: artiRttc, firt; f«t, fare; fust; cet, prfr; Mt, police; obey, g6; not, ®r; foil, lille; but, bOrn; osflnml; is habit, renew;
rarefy Keys: art, ape, fat, fare, fi»t, all; mO, gfit, pr^y, fern; hft. Ice; 1 = 6; 1 = 5; gO, ndt, 6r, w6n, wolf, do.
2050
and army of lh« \Tnlu«l Kiatrs the followins KrwlcK are
equivalent In rank eiisUn hihI w mnd iKMitiJuant, llculen-
ant Uuuiur arade) and lirm lunti'iiiiit. llfiitununl (wnlor
anidc) and captain, liiMiU'n.ini'f oiunmnder and major,
commander and llcutcn ini-n»lorn*l, c.ipt dn and colonel,
rear-admiral and inaj(«r««K* iht.iI. a'J( c*.iilmiral andilcutenanl-
Kuiicrai, aclmlral and Kcncral (n /;/ The maim of sjildlerv,
the order of common HiiJdlcs wIMi the delinitc article, aa,
the colonel had rlwn fiorii f/-i ranLi
Nitw ofiwiird mill in vinw.
'1 h<< I oiiiitl. M ranU iif 1 iikIiuhJ clruw
>S( fit 1 hard of the J^lrn can fi. Mi 21«
(2) Orqan-buiUUnv ^ tw't f»f f'**' *‘‘‘*'*^*
Any row rniinlna or rea irdcd ai runnirm from wide to Hide,
HH dlsiln.'ul*<ind from ///. a line, im u row of jajuarcM on a
cliowmhfVird or of life * ’/ml HO T), all AiiuTlcin genwal. commindcd dlvlalon on
the rn/irof ail to the lea. 2. A coiiiuy in b E North
I oi r I
ofTenae 2. Rcleaik* from captivity, bondaRe, or tho
poHWNsion nf an eiietuv, fur a cunmduraUoii
```


## [2026-09-14T01:28:23.196Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=216580 && NR<=218200' FSD_vol3.txt | grep -n -i \"raphael\\|rapha\" | head -20"
}
```


### [2026-09-14T01:28:24.349Z] TOOL RESULT

```
333:radish, and Ji raphanistrum Is the wild or Jointed eliar-
334:loek. l< L raphanus (ir rAnpAanos). radish ]
467:Inferior iiiidyisl wool, rap'lacht; rapHackt; rap'lockt.
```


## [2026-09-14T01:28:30.455Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '216905,216935p' FSD_vol3.txt | cut -c1-250"
}
```


### [2026-09-14T01:28:30.541Z] TOOL RESULT

```
said to cause the disease ] raph'a-nyf.
rapli'a-nol. l ruro-nOl or -nol. Z rAf'u-nOI or -nfii n Chtm
A crystalline oompoiind ncourrlng In the black radish
Baph'a-nust 1 raf'u-utis. 2 rftf'a-ntiH n Bot A sinnil old
Uorld genus of annual or perennial plants of the fumllv
Cructferx, having lyrate leaves and linear nods eonstrli tccl
betwxjcn the seeds ft mUouh is the cultivated fir black
radish, and Ji raphanistrum Is the wild or Jointed eliar-
loek. l< L raphanus (ir rAnpAanos). radish ]
ra'pIlCf 1 rC'^n, 2 ra'fc. n 1. (1) •\iiat A h< niii'likc
appearance often seen in organs, especially iif tin*
median line of the bodv, us. the raphe of the loiigm
At the raphe, when* the two latorul halvws of thr brain oiiki-
nally uoitiH!, a Mcimmtioii an it wore l4ikraplacn
Balvuijk tvomp hnUtrptd vo| ii, p .t'ifl Iv^cm IS8I 1
(2) Ornith The depression whu h runs ulniiK the i.icliH
of a feather on its under side 2. Hut (1) 'Die fihro-
't oscular cord that eoiinecls the hiluiii of an unalroiMJiis
nr aniphitrnpous ovule with the iliiila/a (.') A lin« or
rib eoiineeting the nocliil(‘s on u diatorn*\ alv<‘ (.j) 'I’he
suture between tlie merieurps in an apiaecous plant
[ < Gr rhapfu , Neam, < rhaidu, sLitch 1
Ba'phl-a, 1 rO'fi-u, 2 ra'fi-u, n lud A genus of lututl-
somc pinnntely leavid palnis having lurgi tiunks iitul
a long spieatp infloreseenee fonipais' kai ha ( ^
Madugaseun raffia, kind of palni'tns' ]
raph''l-an*klH'trftn. l iflri<un>klH'irnn, 2 raf'l-ftn-kls'tron, v
fturg An Instrument used In forming an artUlel.il pupil
[<. Or rhaphlH, needle, + antUtrnn, lunik |
rapli 'l-<leK, l rari-ul*', 2 v IMural of luruis
— raph^l-dircr-oiis, a Hot rrodiumg ruphuh f
```


## [2026-09-14T01:28:48.904Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp && for u in \"%D8%B1%D9%81%D8%A3\" \"%D8%B1%D9%81%D9%88#Arabic\" \"Raphael\" \"Reconstruction:Proto-Indo-European/re%CA%B0w-\"; do echo \"===== $u =====\"; curl -s \"https://en.wiktionary.org/w/index.php?title=$u&action=raw\" | head -80; echo; done 2>&1 | head -150"
}
```


### [2026-09-14T01:28:50.617Z] TOOL RESULT

```
===== %D8%B1%D9%81%D8%A3 =====
==Arabic==

===Etymology===
{{ar-rootbox|ر ف ء}}
{{inh+|ar|sem-wes-pro|*rpʔ|t=to heal, protect}}.

===Pronunciation===
{{ar-pr|رَفَأَ}}

===Verb===
{{ar-verb|I/a~a.vn:رَفْء}}

# {{lb|ar|transitive}} to bring ship near to the bank of a river, to [[land]] at a [[harbour]], to [[dock]]
#: {{uxa|ar|قَدْ عَادَ البَحَّارُونَ وَ'''رَفَأُوا''' السَفِينَةَ|The sailors have returned and '''docked''' the ship.}}

====Conjugation====
{{ar-conj|I/a~a.vn:رَفْء}}

====Derived terms====
* {{l|ar|مَرْفَأ}}

===References===
* {{R:ar:Lane}}
* {{R:sem-pro:SED|id=16327|entry=rfˀ|word=1}}
===== %D8%B1%D9%81%D9%88#Arabic =====
<!DOCTYPE html>
<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-menu-disabled vector-feature-language-in-main-page-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-pinned-clientpref-1 skin-theme-clientpref-day vector-sticky-header-enabled vector-toc-available skin-thumbsize-clientpref-standard" lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<title>رفو - Wiktionary, the free dictionary</title>
<script>(function(){var className="client-js vector-feature-language-in-header-enabled vector-feature-language-in-main-menu-disabled vector-feature-language-in-main-page-header-disabled vector-feature-page-tools-pinned-disabled vector-feature-toc-pinned-clientpref-1 vector-feature-main-menu-pinned-disabled vector-feature-limited-width-clientpref-1 vector-feature-limited-width-content-enabled vector-feature-custom-font-size-clientpref-1 vector-feature-appearance-pinned-clientpref-1 skin-theme-clientpref-day vector-sticky-header-enabled vector-toc-available skin-thumbsize-clientpref-standard";var cookie=document.cookie.match(/(?:^|; )enwiktionarymwclientpreferences=([^;]+)/);if(cookie){cookie[1].split('%2C').forEach(function(pref){className=className.replace(new RegExp('(^| )'+pref.replace(/-clientpref-\w+$|[^\w-]+/g,'')+'-clientpref-\\w+( |$)'),'$1'+pref+'$2');});}document.documentElement.className=className;}());RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"d668854a-0b59-4455-8a60-c40a174ec132","wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"رفو","wgTitle":"رفو","wgCurRevisionId":85058986,"wgRevisionId":85058986,"wgArticleId":10090891,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Arabic terms with redundant transliterations","Pages with entries","Pages with 1 entry","Persian terms borrowed from Arabic","Persian terms derived from Arabic","Persian terms with IPA pronunciation","Rhymes:Persian/uː","Rhymes:Persian/uː/2 syllables","Persian lemmas","Persian nouns","Persian terms with quotations"],"wgPageViewLanguage":"en","wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"رفو","wgRelevantArticleId":10090891,"wgTempUserName":null,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgNoticeProject":"wiktionary","wgConfirmEditCaptchaNeededForGenericEdit":"hcaptcha","wgConfirmEditForceShowCaptcha":false,"wgConfirmEditHCaptchaSiteKey":"5d0c670e-a5f4-4258-ad16-1f42792c9c62","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgMediaViewerMobileBeta":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"watchlist":true,"tagline":false,"nearby":true},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":600,"wgTestKitchenUserExperiments":{"overrides":[],"enrolled":[],"assigned":[],"subject_ids":[]},"wgEditSubmitButtonLabelPublish":true,"wgVisualEditorPageIsDisambiguation":false,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":false,"wgVector2022LanguageInHeader":true,"wgULSisLanguageSelectorEmpty":false,"wgULSLanguageSelectorV2Enabled":true,"wgCheckUserClientHintsHeadersJsApi":["brands","architecture","bitness","fullVersionList","mobile","model","platform","platformVersion"]};
RLSTATE={"ext.gadget.LanguagesAndScripts":"ready","ext.gadget.Palette":"ready","ext.gadget.Site":"ready","ext.gadget.InflectionTable":"ready","ext.gadget.reflist":"ready","ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","ext.wikimediamessages.styles":"ready","skins.vector.search.codex.styles":"ready","skins.vector.styles":"ready","skins.vector.icons":"ready","jquery.makeCollapsible.styles":"ready","mediawiki.skins.legacy":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready"};RLPAGEMODULES=["site","mediawiki.page.ready","jquery.makeCollapsible","mediawiki.toc","skins.vector.js","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.gadget.PagePreviews","ext.gadget.ReferenceTooltips","ext.gadget.defaultVisibilityToggles","ext.gadget.DialectMap","ext.gadget.DocTabs","ext.gadget.Edittools","ext.gadget.UnsupportedTitles","ext.gadget.SiteJS","ext.gadget.WiktGadgetPrefs","ext.urlShortener.toolbar","ext.centralauth.centralautologin","ext.testKitchen","ext.wikimediaCustomizations.donorAccountCreation","mmv.bootstrap","ext.visualEditor.desktopArticleTarget.init","ext.echo.centralauth","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.interface","wikibase.databox.fromWikidata","ext.checkUser.clientHints"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.impl(function(){return["user.options@12s5i",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
}];});});</script>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediamessages.styles%7Cjquery.makeCollapsible.styles%7Cmediawiki.skins.legacy%7Cskins.vector.icons%2Cstyles%7Cskins.vector.search.codex.styles&amp;only=styles&amp;skin=vector-2022">
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector-2022"></script>
<meta name="ResourceLoaderDynamicStyles" content="">
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.gadget.InflectionTable%2CLanguagesAndScripts%2CPalette%2CSite%2Creflist&amp;only=styles&amp;skin=vector-2022">
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector-2022">
<meta name="generator" content="MediaWiki 1.47.0-wmf.19">
<meta name="referrer" content="origin">
<meta name="referrer" content="origin-when-cross-origin">
<meta name="robots" content="max-image-preview:standard">
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=1120">
<meta property="og:site_name" content="Wiktionary">
<meta property="og:title" content="رفو - Wiktionary, the free dictionary">
<meta property="og:type" content="website">
<link rel="alternate" type="application/x-wiki" title="Edit" href="/w/index.php?title=%D8%B1%D9%81%D9%88&amp;action=edit">
<link rel="apple-touch-icon" href="/static/apple-touch/wiktionary/en.png">
<link rel="icon" href="/static/favicon/wiktionary/en.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/w/rest.php/v1/search" title="Wiktionary (en)">
<link rel="EditURI" type="application/rsd+xml" href="//en.wiktionary.org/w/api.php?action=rsd">
<link rel="canonical" href="https://en.wiktionary.org/wiki/%D8%B1%D9%81%D9%88">
<link rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">
<link rel="alternate" type="application/atom+xml" title="Wiktionary Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom">
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<link rel="dns-prefetch" href="auth.wikimedia.org">
</head>
<body class="skin--responsive skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-رفو rootpage-رفو skin-vector-2022 action-view">
<div id="mw-aria-live-region" class="mw-aria-live-region" aria-live="polite"></div><a class="mw-jump-link" href="#bodyContent">Jump to content</a>
<div class="vector-header-container">
	<header class="vector-header mw-header no-font-mode-scale">
		<div class="vector-header-start">
			<nav class="vector-main-menu-landmark" aria-label="Site">
				
<div id="vector-main-menu-dropdown" class="vector-dropdown vector-main-menu-dropdown vector-button-flush-left vector-button-flush-right"  title="Main menu" >
	<input type="checkbox" id="vector-main-menu-dropdown-checkbox" role="button" aria-haspopup="true" data-event-name="ui.dropdown-vector-main-menu-dropdown" class="vector-dropdown-checkbox "  aria-label="Main menu"   >
	<label id="vector-main-menu-dropdown-label" for="vector-main-menu-dropdown-checkbox" class="vector-dropdown-label cdx-button cdx-button--fake-button cdx-button--fake-button--enabled cdx-button--weight-quiet cdx-button--icon-only " aria-hidden="true"  ><span class="vector-icon mw-ui-icon-menu mw-ui-icon-wikimedia-menu cdx-button__icon"></span>

<span class="vector-dropdown-label-text">Main menu</span>
	</label>
	<div class="vector-dropdown-content">


				<div id="vector-main-menu-unpinned-container" class="vector-unpinned-container">
		
<div id="vector-main-menu" class="vector-main-menu vector-pinnable-element">
	<div
	class="vector-pinnable-header vector-main-menu-pinnable-header vector-pinnable-header-unpinned"
	data-feature-name="main-menu-pinned"
	data-pinnable-element-id="vector-main-menu"
	data-pinned-container-id="vector-main-menu-pinned-container"
	data-unpinned-container-id="vector-main-menu-unpinned-container"
>
	<div class="vector-pinnable-header-label">Main menu</div>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-pin-button" data-event-name="pinnable-header.vector-main-menu.pin" aria-label="Move Main menu to sidebar">move to sidebar</button>
	<button class="vector-pinnable-header-toggle-button vector-pinnable-header-unpin-button" data-event-name="pinnable-header.vector-main-menu.unpin" aria-label="Hide Main menu">hide</button>
</div>

	
<div id="p-navigation" class="vector-menu mw-portlet mw-portlet-navigation"  >
	<div class="vector-menu-heading">
		Navigation
	</div>
	<div class="vector-menu-content">
		
		<ul class="vector-menu-content-list">
			
			<li id="n-mainpage-description" class="mw-list-item"><a href="/wiki/Wiktionary:Main_Page" title="Visit the main page [z]" accesskey="z"><span>Main page</span></a></li><li id="n-portal" class="mw-list-item"><a href="/wiki/Wiktionary:Community_portal" title="About the project, what you can do, where to find things"><span>Community portal</span></a></li><li id="n-requestedarticles" class="mw-list-item"><a href="/wiki/Wiktionary:Requested_entries"><span>Requested entries</span></a></li><li id="n-recentchanges" class="mw-list-item"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r"><span>Recent changes</span></a></li><li id="n-randompage" class="mw-list-item"><a href="/wiki/Special:Random" title="Load a random page [x]" accesskey="x"><span>Random entry</span></a></li><li id="n-help" class="mw-list-item"><a href="https://en.wiktionary.org/wiki/Help:Contents" title="The place to find out"><span>Help</span></a></li><li id="n-Glossary" class="mw-list-item"><a href="/wiki/Appendix:Glossary"><span>Glossary</span></a></li><li id="n-contact" class="mw-list-item"><a href="/wiki/Wiktionary:Contact_us"><span>Contact us</span></a></li><li id="n-specialpages" class="mw-list-item"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q"><span>Special pages</span></a></li>
		</ul>
		
	</div>
</div>


===== Raphael =====
{{also|Raphaël}}
==English==
{{wp|<dab!>}}

===Etymology===
{{der|en|la|Raphael}}. From {{der|en|grc-koi|Ῥᾱφᾱήλ}}, from {{der|en|he|רָפָאֵל|tr=Rāfāʾēl|lit=God cures/has healed}}.

===Pronunciation===
* {{IPA|en|/ˈɹæf.eɪˌɛl/|/ˈɹæf.eɪ.əl/|/ˈɹæf.ɪ.əl/|/ˌɹæf.aɪˈɛl/|/ˌɹɑː-/|/ˈɹɑː-/|a=UK}}
* {{IPA|en|/ˌɹɑ.faɪˈɛl/|/ˌɹæf.aɪˈɛl/|/ˈɹæf.i.əl/|/ˈɹɑ.fi.əl/|/-eɪ-/|a=chiefly US}}
* {{q|certain Carolina accents}} {{IPA|en|/ˈɹæf.ɛəl/}}
* {{audio|en|LL-Q1860 (eng)-I learned some phrases-Raphael.wav|a=UK}}

===Proper noun===
{{en-proper noun|~}}

# An [[archangel]] in [[Christianity]], [[Judaism]], and [[Islam]].
#* {{RQ:King James Version|Tobit|12|15||I am '''Raphael''', one of the seven holy angels, which present the prayers of the saints, and which go in and out before the glory of the Holy One.}}
# {{lb|en|countable}} {{given name|en|male|from=Hebrew}}.
# {{lb|en|countable}} {{surname|en|from=patronymics}}.
# {{lb|en|arts}} {{w|Raphael|Raffaello Sanzio da Urbino}}, an [[Italian]] [[Renaissance]] [[painter]] (1483–1520).

====Derived terms====
{{col|en|Raphaelesque|Raphaelic|Raphaelism
|Striped Raphael catfish
|Rafe
|Pre-Raphaelite
|* Pre-Raphaelitism
|* Pre-Raphaelite Brotherhood
}}

====Translations====
{{trans-top|Archangel}}
* Arabic: {{t|ar|رُفَائِيل|m}}
* Armenian: {{t|hy|Ռափայել}}
* Bulgarian: {{t|bg|Рафаил|m}}
* Catalan: {{t+|ca|Rafael|m}}, {{t+|ca|Rafel|m}}
* Chinese:
*: Mandarin: {{t+|cmn|拉斐爾|tr=Lāfěi'ěr}}, {{t|cmn|辣法額爾|tr=Làfǎ'é'ěr}} {{q|Catholicism}}
* Coptic: {{t|cop|ⲣⲁⲫⲁⲏⲗ}}
* Dutch: {{t|nl|Rafaël|m}}
* Esperanto: {{t|eo|Rafaelo}}
```


## [2026-09-14T01:29:18.421Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN ravah/rus ===\"; grep -n \"ravah\\|ravas-carat\\|ravas\\|Av. rav\" SYN.txt | head -10; echo \"=== SYN rus open ===\"; grep -n \"12\\.55\\|‘space’\\|'space'\" SYN.txt | head -5; echo \"=== IEC reuto/reue ===\"; grep -n \"reuto\\|reuə\\|rūmaz\\|rūs \" IEC.txt | head -10; echo \"=== WLD Bd2 ===\"; grep -n -i \"reuto\\|routo\\|uru.war\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T01:29:18.547Z] TOOL RESULT

```
=== SYN ravah/rus ===
1036:Ir. 702, perh. : Av. ravah- ‘free room’, Ch8l. ravinii ‘even, level’ (see below, 6). Pedersen 1.251. Stokes 235. Walde-P. 2.356 (adversely).
1686:Ir. ré ‘period of time’, NIr. also esp. ‘moon’ Av. ravah- ‘space, room’, etc.(?). Wendryes, RC 28.141.
11701:Goth. ON, OE, OHG ram ‘space, place’ (: Av. ravah- ‘space’, Lat. rus ‘country’, etc. Walde-P. 2.356), hence also ‘a room’ in ME rowme, NE room, Sw. rum.
22804:flat’; ChSl. raviniw (renders zediwés Lk. 6.17, elsewhere in Gospels tcos), ete., general Slavic for ‘equal, even’ and so sometimes ‘level, flat’, whence words for ‘plain’ sb. (1.23) : Goth. rims ‘roomy, spacious’, Av. ravah- ‘open space’, Lat. ras ‘country’, etc.
23254:6. ChSl. ravint (reg. for isos, but also for zedwés ‘level’), SCr, ravan, Boh. rovny, Pol. réwny, Russ. ravnyj, also ‘even, level, flat’ (but Russ. ravnyj ‘equal’ vs. rounyj mostly ‘level, flat’) : Av. ravah- ‘open space’, Lat. ris ‘coun- try’ vs. ‘town’, Goth. rims ‘roomy, spa- cious’, OF rim ‘space’ (NE room), etc. Walde-P. 2.356 f. Briickner 464.
26224:The logical relation of ‘sound’ to ‘hearing’, parallel to that of obj. ‘taste, smell’ to subj. ‘taste, smell’, is partially reflected in speech, and some of the words for ‘sound’ are cognate with vbs. for ‘hear’. But more often the sbs. de- rived from the latter reflect the use of ‘hear’ with reference to the hearing of speech and are restricted to articulate sound ‘what is heard from speech’, hence esp. ‘report, news, fame’ (Grk. kXéos, Skt. cravas-, Chl. slava) or ‘word’ (ChSI. slovo, Av. sravah-). The majority of the words for ‘sound’ are independent of the ‘hear’ groups, many of them of imitative origin. Out of the great wealth of words for ‘sound’ or some special kind of sound (ringing, rattling, vocal, etc.), it is intended to list those that are gen- eric, covering both inarticulate and ar- ticulate sounds, or those that are the most nearly generic (in a few cases the selection is doubtful). Words like NE noise (though its use has extended to
26230:least for inarticulate sound), Fy. bruit fi NHG gerdusch, larm, etc., are not ane i cluded. Verbs for ‘sound’, parallel to thoge for the obj. ‘smell’ or ‘taste’, are not listed V Where they exist, they are obvious de- 5 rivatives of the words for ‘sound’, as Grk. yopéw, Lat. sondre, Fr. sonner, NE v sound, NHG lauten, etc. in 1. IE *kleu-, *kleu-s-. Widespread in vbs. for ‘hear’ or ‘listen’ (hence also ( ‘obey’, etc.), also ‘be heard, be called, be famous’, sbs. for ‘hearing’ and for what a is heard, ‘fame’, ‘word’, ete. Walde-P. pt 1.494f. Ernout-M. 192. Walde-H. n 1.237 ff. Pedersen 2.494 f. ‘I Grk. xdtw ‘hear’ (poet.), xdurés ‘heard, ai famous’, xdéos ‘report, fame, glory’ (fr. x0 kéfos = Skt. gravas- id., ChSl. slovo G ‘word’), xAéw ‘make famous, celebrate’, mid. ‘be famous’. ni Lat. cluére (later also cluere) ‘be g
28862:16.47 GLORY Grk. __xAéos, 56Ea, Kidos Goth. wulpus Lith. Slove, garbé NG 56Ea ON dyr6, tirr Lett. slava, guodiba Lat. gloria Dan. are, herlighed ChSl.  slava It. gloria Sw. Gra, hdrlighet SCr.  slava Fr. gloire OE wuldor, tir, magen- Boh. _ sldva, chvala Sp. gloria prym Pol. _— slawa, chwala Rum.  slavé, mdrire, glorie ME glorie Russ. slava Ir. gloir : NE glory Skt. — ¢ravas-, yagas- Nir. _— gloir Du. roem, heerlijkheid Av. x¥aranah- W. gogoniant OHG  tiurida, guollichi Br. gloar, hano kaer MHG ruom
28867:Grk. wdé(¢)os; Lat. cluor (only gloss); Lith. glové, Lett. slava; slava, etc. general Slavic (slovo ‘wor! form = Grk. kdéos); Skt. ¢ravas- sravah- ‘word’).
28906:8. Skt. ¢ravas-, above, 1.
=== SYN rus open ===
1035:3. Gall. -magus in Arganto-magus, etc., Ir. mag, NIr. magh, W. maes, Br. maez, prob. as orig. ‘expanse’ : Lat. magnus, Skt. mah-, etc. ‘large, great’ (12.55), Skt. mahi- ‘earth’. Pedersen 1.96. Stokes 198f. Walde-P. 2.258 (ad- versely).
7273:Fr. grosse, lit. ‘big’ (12.55).
11680:Words for ‘a room’ come in part by specialization from those denoting ‘dwelling, abode’, ‘building’, ‘covering’, ‘space’, etc.; in part by extension from those denoting originally a special room, as a ‘bathroom, heated room’, ‘rest- room’, ‘light-room’.
11701:Goth. ON, OE, OHG ram ‘space, place’ (: Av. ravah- ‘space’, Lat. rus ‘country’, etc. Walde-P. 2.356), hence also ‘a room’ in ME rowme, NE room, Sw. rum.
12092:DWELLING, HOUSE, FURNITURE 481 ot of gult, Lith. | *stel-. Walde-P. 2.843. Trautmann e ro (a > Of, also | 286. a ; tt ee g lista C ee ChSI., Boh. loz, Pol. %6zko, Russ. pl nord lax’, Lett. 9 loge, above, 1 * 7 ? a ith gulls gh] End 1.679. 8. Skt. cayya, cayana-, above, 2. igest, Skt. talpa-, perh. : Lith. talpa ‘spatial chsl odrit (in Gospels Hon Seas capacity, room ee telpu, tilpti eG (cee 4pBaros and K Al = | room for’. Walde-P. 1.741. Cf. O yon Eh, pier’, Boh. odr ‘post, | am ‘space’, Av. gatu- ‘place’, both some- Russ ie etym. dub., perh. : OF | times used for ‘resting place, bed’. affolding » 1 etc, Walde-P Av. stairis- (prob. only a ‘carpet, rug’
=== IEC reuto/reue ===
402:Skt. astra (*goad', fr. *aKtrio); Av. astra; Tokh. astar, astare and astre ‘clear, bright"; OCS ostrü ‘sharp’; ostrije ‘cutting-edge’; OCz. ostrev (fr. *-üs ‘barbed pole’); Li. aštrūs “se- vere’; Latv. astrs ‘horsehair
2457:dreutos ‘bold, daring, strong, firm’. Cf. druuo-, dru-, etc. W drud ‘bold, daring; dear": MHG triute ‘darling’; OE treowp ‘truth, pledge, faith’; isophonic w. Li. driáučius “log, beam’
4930:ghreun- (ghreuən, ghreusn-) ‘grit, gravel, groats’ Br. gruan ‘gravel’; W graian, (d: MHG grien, G Grien, id.; ON grjon, npl. ‘groats’; OE cf. greosn 'gravel' (Olr. grian 'gravel fr. *ghrei-)
13487:preuto (preutso, phreut-) ‘snort, blow, spray”. WP II, 28 Skt. prothami, v. id.; Av. frao0-, v. id.; OE à- fréopan, v. ‘foam at mouth"; (z-gde in) E froth, s. & v.; ON cf. (o-gde) frauó, n. beside (z- gde) froóa, f. id.
14581:reut- (reuto, ið, rout-, rut-) ‘fling, dash’. Cf. routeio Skt. cf. lothayàmi, v. ‘plunder’; Alb. rüsem, v.
=== WLD Bd2 ===
```


## [2026-09-14T01:29:28.982Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\n')\nnums=[(i+1,int(m.group(1))) for i,l in enumerate(lines) for m in [re.search(r'\\b(4[5-9]\\d|48\\d)\\b',l.strip())] if m and len(l.strip())<80]\n# simpler: find lines containing 'DWELLING' header with page\nfor i,l in enumerate(lines):\n    if re.search(r'\\b46[0-9]\\b',l) and ('DWELLING' in l or 'HOUSE' in l or len(l.strip())<12):\n        print(i+1, l.strip()[:120])\nEOF"
}
```


### [2026-09-14T01:29:30.555Z] TOOL RESULT

```
9918 2.463 4
11592 461
11619 462
11663 463
11706 465
11722 466
11746 467
11769 468
11805 469
```


## [2026-09-14T01:29:38.468Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ravah\\|rū-mo\\|rums\\|Liden KZ. 61\\|Liden\" incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T01:29:38.655Z] TOOL RESULT

```
340:    S.Liden BB. 21, 93 m. Lit. Wenn ir. an als ‘'^pena aufgefaBt werden
361:„Wasser^ (s. Liden aaO.) ist abzulehnen.       Schulze SBprAk. 1910, 792
441:ziehung tm pel-                usw. (I'ickKZ.19^ 263, Liden BB. 21, 95 Anm.);
690:hinuber schillern, im Germ, ganz alltaglich sind. Liden BB. 21, 95, Stokes
1106:braaen“?? Liden Arm. St. 27 f, unter einer hochst fraglichen Gdf. "^palisna).
1155:(das u nach cucann); ags. (Liden IF. 18, 412f.) a-figen „ger6stet^‘;
1353: sen KZ. 39, 343, 348, -Liden Arm. St. 114,                     Osthoff MU. YI, 18).    Gr. vtio
1428:bestimmtes Getreidema6“ (wenn ass. aus ^padla, -ll; *Liden KZ. 40, 261,
1533:Hauseidechse", wenn nach Liden KZ. 40, 260 das fem. eines "^palla-, pra-
2848:       Liden Arm. St. 85 ff. m.     Lit.
2856:(usw., s. Liden); orot .,DonneP', orotam ,,donnere“; alb. (G. Meyer Wb. 352)
2881:doch reicht es nicht aus, um (nach Grienberger AfslPh. IS, 14 und Liden)
2887:iiber rh aus rk entstanden sei: s. dagegen Liden aaO. 90, Wiedemann
2896:gleicher Bed., aber yon einerWzf. per-q- (Meillet Esq. [100]. Liden aaO.):
2912:Liden aaO.). Sollte ai. parjdnya-li „der Regen- und Gewittergott" dei
2923:„Morden", Zerstoren" {'^'[p\org-no- od. -rih) braucht nicht nach Liden als por-
2926:376, 29), gall. Orgeto-rtx               MK (Lit. bei Liden). — Abg. pr^gnqti, „bersten%
3082:Fisch"; Liden Uppsalastudier 92).          Mir. ere (O'Clery), „bunt, rot**', cymr.
3575:ind.      Formans -nda-^ Liden Stud,            90),   paiala-                wie
3577:Jiataka-, abg. zlato    „Gold“ von ^ghel-, Liden aaO.).
```


## [2026-09-14T01:29:44.803Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace')\ntxt=t.read()\nimport sys\n# search for 'rou-' entries\nfor pat in ['reu9-','reu3-','reua-','rou-','ru-mo','Raum','geoffnet']:\n    idx=[m.start() for m in re.finditer(pat,txt)][:5]\n    print(pat, len(idx))\nEOF"
}
```


### [2026-09-14T01:29:45.982Z] TOOL RESULT

```
reu9- 0
reu3- 0
reua- 0
rou- 5
ru-mo 0
Raum 5
geoffnet 0
```


## [2026-09-14T01:29:54.845Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt'\nleaves=open(p,encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(leaves))\nfor i,L in enumerate(leaves):\n    if 'ravah' in L or 'ravan' in L or ('rums' in L and 'rus' in L):\n        print('HIT leaf',i); print(L[:1500]); break\nEOF"
}
```


### [2026-09-14T01:29:56.005Z] TOOL RESULT

```
leaves 725
HIT leaf 41
                                               per-                                      37

Pormen vci\tth\ urspriingliclie Lagerung unklar; s. Bartholomae IF* 22, 96ff.,
Brugmann 11^ 2, 51). Gr. ^ngo-azog in att nowrog nnd dor. TiQazog „erster“
(Lit. bei Boisacq, bes. Hirt IF. 21, 164 und Hdb.^ 447; die Zuriickfubrung
YOU dor* nQdxog auf *pey9i6s an letzterer Stelle ist offenkundig verfeblt,
Yielmehr ist die Kontraktion -oa- zu -d- statt -co- bedingt durch Pormen
mit betontem -d- wie *7r^odTq?, die mit dsyArq} usw. reimend erhalten
wurden, wenn nicht iiberhaupt -od- iautgesetzlich dor, -d- ergab).
   Gr. TZQojLtog „Yorderster, Yorkampfer, Fuhrer“, umbr. promom adv. „pri-
nium“, got. fram Adv. „weiter“ (Komp. franiis', frmnaldrs           Alter vor-
geschritten, bejahrt^)? Fraep. m. Dat. ,.von-her‘, aisl. fram Adv. „vor-
warts“ (Komp. fremr)^ fra {^fram) Praep. m. Dat. „weg von'S ahd. fram
Adv. „vorwarts, fort, weiter, sogleich“, Praep. m. Dat. „fort von, von
—    her^^ ags. from Adv. „fort‘S Praep. m. Dat, „weg von“; aisL framr
„Yoranstehend, vorwartsstrebend, ausgezeichnet^’ {frami m. „Ruhm, Vor-
teil, Ehre“), ags. fram „tiichtig, keck^‘.

   Daneben idg. *pre-mo-s in gr. jigdifiog „Vorderster, Yorkampfer, Fiihrer’,
got. fruma „er8ter, friiherer, vorhergehend'^ (Sup. frumists\ mhd. fnim^
vrom „tuchtig, brav“ (nbd. fromm\ ahd. as. fruma f. Nutzen‘S nhd. Frommen;
ahnliche Bed.-Entw. in lat. prohus „gut, tiichtig, braY“, u. profe „probe“ aus
"^pro-hliuo-   ai. pra-hh'd-li „he
```


## [2026-09-14T01:30:04.925Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D9%81%D9%88/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for رفو — quote the entry including any origin tag in brackets such as [ع.] or [په.]? Also quote the لغت‌نامه دهخدا line on its origin if present."
}
```


## [2026-09-14T01:30:06.500Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/room",
 "prompt": "Quote the full etymology of 'room', including the PIE root cited and any mention of Avestan ravah- or Latin rus. Also state what etymonline says about 'ream' (verb, to enlarge a hole) if mentioned."
}
```


### [2026-09-14T01:30:10.103Z] TOOL RESULT

```
# فرهنگ معین Entry for رفو

According to the Farhangi Mo'in section:

> "(رُ ) [ معر. ] (اِ. ) دوخت دررفتگی ها و پارگی های پارچه یا فرش به طوری که به آسانی"

The origin tags indicate it's a "معرب" (borrowed word) marked with [اِ.] (indefinite marker).

# Dehkhoda Entry Origin Reference

The Dehkhoda section notes:

> "از رَفْوْ عربی است «واو» را بدل به «او» کنند و فتحه ( را ) رانیز بدل به ضمه گردانند"

This indicates the word originates from Arabic "رَفْوْ" with phonetic modifications in Persian.
```


### [2026-09-14T01:30:12.203Z] TOOL RESULT

```
# Etymology of "Room"

Based on the etymonline article, here is the full etymology:

**Room (noun)** derives from Middle English *roum*, from Old English *rum* meaning "space, extent; sufficient space, fit occasion (to do something)." The word traces back through Proto-Germanic *ruman* to the Germanic adjective *ruma-* meaning "roomy, spacious."

The ultimate root is the PIE *reue-* (1) meaning "to open; space," which also produced Avestan *ravah-* ("space"), Latin *rus* ("open country"), Old Irish *roi/roe* ("plain field"), Old Church Slavonic *ravinu* ("level"), and Russian *ravnina* ("a plain").

The meaning shifted from abstract space to "chamber, cabin" by the early 14th century (as a nautical term), then to "interior division of a building" by the mid-15th century.

---

**Note on "ream":** The article contains information about "ream" (the paper measurement), tracing it from Old French, Spanish, and Arabic origins. However, the page does not include etymology for "ream" as a verb meaning to enlarge a hole, so I cannot provide that information based on this content.
```


## [2026-09-14T01:30:24.601Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%A3\" \\\n \"https://en.wiktionary.org/wiki/Raphael\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\" \\\n \"https://www.etymonline.com/word/room\" \\\n \"https://abadis.ir/fatofa/%D8%B1%D9%81%D9%88/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 425 verification (roots Reuto/Rewe/R.f.a): Persian sekam, ruda, rofu; Arabic rafa'a; Raphael; room/rural\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T01:30:31.977Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3189c255782d3f5e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a593f345b5e17ff7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4387910c749da1fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a8f93e4596ce01e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/027009026b7c3a22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b3ffb8efb102073.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36f94a5c0c69d11a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d95c5e80a4b0330.txt
```


## [2026-09-14T01:30:37.103Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp && curl -s \"https://en.wiktionary.org/w/index.php?title=%F0%90%AD%A0%F0%90%AD%B1%F0%90%AD%AA%F0%90%AD%AC%F0%90%AD%A1&action=raw\" | head -40"
}
```


## [2026-09-14T01:30:38.046Z] TOOL CALL #60: WebSearch

```json
{
 "query": "Middle Persian aškamb \"belly\" etymology Proto-Iranian *skamba Hasandust شکم ریشه‌شناسی"
}
```


### [2026-09-14T01:30:38.455Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1112 cp1112, Varnish XID 1053129788<br>Upstream caches: cp1112 int<br>Error: 404, Not Found at Mon, 14 Sep 2026 01:30:38 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.22</details></code></p>
</div>
```


### [2026-09-14T01:30:44.452Z] TOOL RESULT

```
Web search results for query: "Middle Persian aškamb "belly" etymology Proto-Iranian *skamba Hasandust شکم ریشه‌شناسی"

Links: [{"title":"Hidden in Plain Sight: Illuminating Indo-European Cognates in Persian – borderlessblogger","url":"https://borderlessblogger.com/2023/05/19/hidden-in-plain-sight-illuminating-indo-european-words-in-persian/"},{"title":"(PDF) On the Etymology of Middle Persian baškuč (Winged Monster)","url":"https://www.academia.edu/39995280/On_the_Etymology_of_Middle_Persian_ba%C5%A1ku%C4%8D_Winged_Monster_"},{"title":"Iranian group","url":"https://starlingdb.org/new100/irn.pdf"},{"title":"paunch > shekambeh - English to Persian (Farsi) translation on #KudoZ Term Help Network.","url":"https://www.proz.com/kudoz/english-to-persian-farsi/other/565634-belly-stomach.html"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"},{"title":"شکم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%85"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"},{"title":"Dialectal Layers in West Iranian: a Hierarchical Dirichlet Process Approach to Linguistic Relationships","url":"https://arxiv.org/pdf/2001.05297"}]

Based on the search results, I found relevant information about the Middle Persian term aškamb:

The word "belly" in Persian derives from Middle Persian aškamb. The search results also reference related forms, noting that the word šikampa/iškampa meaning "stomach" is probably of Indo-Iranian origin, with scholars comparing Old Indian stabh- 'fasten' and reconstructing protoforms like *staf- < *stebh-.

Additionally, in Pahlavi (Middle Persian), the word was pronounced as ashkam, ashkambag, ashkom and ashkomb.

The search results indicate that this word has Indo-Iranian etymological roots, though the specific Proto-Iranian form *skamba and details about Hasandust's research on this etymology were not found in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:30:52.090Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://starlingdb.org/new100/irn.pdf",
 "prompt": "Find the entry for 'belly' / šikampa / iškampa / aškamb and quote exactly what it says about the etymology (protoform, comparison with Old Indian stabh-, *stebh-). Also quote any entry for 'intestine' or rōd/rūda if present."
}
```


### [2026-09-14T01:30:59.610Z] TOOL RESULT

```
I appreciate your request, but I'm unable to locate the specific entries you're asking about in this PDF document. The content provided appears to be raw PDF binary data with embedded fonts and compressed streams rather than readable text that I can directly search and quote.

To find the etymological information about 'belly' (šikampa/iškampa/aškamb) and any entries for 'intestine' or 'rōd/rūda', you would need to:

1. Convert this PDF to a readable text format
2. Use a PDF viewer's search function to locate these entries
3. Share the relevant page content in plain text format

If you can provide the actual readable text passages containing these etymological entries, I'd be happy to help quote and analyze them within the character limits you've specified.

[Binary content (application/pdf, 1.4MB) also saved to /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/webfetch-1789349456142-7291b6.pdf]
```


## [2026-09-14T01:31:03.069Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cp /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/webfetch-1789349456142-7291b6.pdf irn-425.pdf && pdftotext irn-425.pdf irn-425.txt 2>/dev/null && grep -n -i -B3 -A8 \"kampa\\|BELLY\" irn-425.txt | head -60"
}
```


### [2026-09-14T01:31:04.727Z] TOOL RESULT

```
126-There is a great number of etymologically obscure words in the Ossetic vocabulary,
127-including its basic layer. Within the 110-item Swadesh wordlist, such terms are as
128-follows:
129:1) 'bark' (cʼar | cʼarɜ); 2) 'belly' (gʷəbən | gubun); 3) 'bird' (cʼiw | čʼew); 4) 'dry' (Digor sor);
130-5) 'feather' (šiš | šes); 6) 'fish' (kɜšag | kɜsalgɜ); 7) 'foot' (kʼaχ | kʼaχ); 8) 'hand' (kʼuχ | kʼoχ);
131-9) 'leaf' (Digor tʼaffɜ); 10) 'meat' (Iron ziza); 11) 'mountain' (kʼɜzɜχ | kʼɜʒɜχ); 12) 'mouth'
132-(zəχ | ʒuχ ~ cʼuχ); 13) 'neck' (bɜržɜy | bɜrzɜy); 14) 'nose' (fənz | fiy); 15) 'rain' (kʼɜvda |
133-kʼɜvda); 16) 'round' (təmbəl | tumbul); 17) 'small' (Iron čəšəl); 18) 'stone' (dur | dor); 19)
134-'tree' (bɜlaš | bɜlasɜ); 20) 'salt' (sɜχχ | cɜnχɜ); 21) 'short' (səbər | cubur).
135-They represent potential loanwords, although exact sources of borrowing are unclear.
136-Since in many such cases we observe phonetically similar (but not identical) forms in
137-modern North Caucasian languages, it is possible to think that we deal with
--
1784-Avestan: Not attested. It is possible that the word paːs-ta- {pąsta-} 'skin (on the head)' [Bartholomae 1904: 904] could have the second
1785-meaning 'bark' (as in many Iranian languages), but there are no data that would definitively prove this.
1786-
1787:4. BELLY
1788-Iron Ossetic gʷəbən {гуыбын} (1), Digor Ossetic gubun {губун} (1), Yaghnobi dˈar-a {dára}
1789-(2), Parachi aštˈaw {aštáw} (3), Avestan udar-a- {udara-} # (2).
1790-References and notes:
1791-Iron Ossetic: The origin of gʷəbən, gubun is unclear. It belongs to a group of words meaning 'round' [Abaev 1958: 528], which are,
1792-according to [Abaev 1979: 330-335], a very broad cross-linguistic class of ideophones that cannot be derived from a single source.
1793:Digor Ossetic: According to Abaev, Digor uses a different word for 'belly' - qɜstɜ (of unknown origin), more often than gubun
1794-[Abaev 1973: 298-299]. The shift to gubun might have been due to secondary Iron influence on Digor (at least it can concern our
1795-Digor informant, which lives in Vladikavkaz).
1796-
1797-19
1798-
1799-Yaghnobi: ALP 1957: 244; Novák 2010: 32. There are some examples in texts: {pódotem áspĕ dárĕ tákĕ vek vant} "Bind my legs
1800:under the horse’s belly!" [AP 1957: 139]; {dár-a-m sẹr av } "I am satiated"; literally, "my belly has become satiated" [AP 1957: 172,
1801-244] (the last phrase belongs to a mouse speaking about itself; however, it is reasonable to think that it speaks from an
1802-anthropomorphic perspective).
1803:Polysemy: 'belly / interior, core', compare dirˈaχti dˈar-a {diráxti dára} 'tree trunk's core' [Khromov 1972: 166]. Secure
1804:Iranian etymology; compare Sogdian (Β) {kδ’r’k} 'belly' etc. [Steblin-Kamensky 1999: 151-152].
1805-Phonetic variants: ALP record a phonetic variant darˈ-a {dará} [ALP 1957: 244], which does not occur in texts.
1806-Distinct from šikˈampa {šĭkámpa} ~ iškampˈa {iškampá} ˈstomach; cow stomachˈ [ALP 1957: 326; Novák 2010: 160], bˈandil
1807-{bándil} ˈstomach / gutsˈ [Novák 2010: 11].
1808-Parachi: Efimov 2009: 172; Morgenstierne 1929: 237. Probably of Indo-Iranian origin; Morgenstierne compares Old Indian {stabh-}
1809-'fasten' and reconstructs such dubious protoforms as {*staf-} < {*stebh-} [Morgenstierne 1929: 237]. Anyhow, this word
1810-seems to be inherited, judging by its phonetic form and by the absence of similar words in neighbour languages.
1811-Phonetic variants: t can also be retroflex in this word, compare ašʈˈaw {ašṭáw} [Efimov 2009: 172].
1812-Dialectal forms: Shutul aštˈaw {aštáf}, Gujulan ašˈaw {ašáw} [Efimov 2009: 172].
1813-The rare word χiːʈ {xīṭ} represents a borrowing from Pashto [Morgenstierne 1929: 301].
1814-The word for 'stomach' is not attested.
1815:Avestan: Bartholomae 1904: 387. Only as a member of the compound udara=θrans-a- {udarō.θrąsa-} 'creeping on belly', attested in
1816-Videvdad.
1817:Distinct from ruθ-wan- {uruθuuan} 'entrails / belly (of Ahuric creatures)' [Bartholomae 1904: 1531-1532] and marš-u{maršu-} 'belly of daevic creatures' [Bartholomae 1904: 1153-1154].
1818:The word udar-a- {udara-} is related to Vedic udˈar-a- {udára-} 'belly'; Indo-Iranian words cannot be separated from Greek
1819:{ὕδερος} 'dropsy', Old Prussian {weders} 'belly / stomach'; it is not clear whether all these cognates are derived from PIE
1820-{*ud-er-} 'water' or not [EWAia I: 216].
1821-
1822-5. BIG
1823-Iron Ossetic štər {стыр} (1), Digor Ossetic ustur {устур} (1), Yaghnobi kˈatː-a {kátta} (-1),
1824-Parachi ghaɳɖ {gʽaṇḍ} (-1), Avestan maz-ant- {mazant-} (2).
1825-References and notes:
1826-Iron Ossetic: Originates from Proto-Iranian *stuːra- 'great' [Abaev 1979: 159].
1827-Yaghnobi: ALP 1957: 271-272; Novák 2010: 84. Plural kˈatː-oːt {káttot}. The word is used with a wide range of objects: {i kátta sank} 'a
--
2413-Iron Ossetic: Probably of North Caucasian origin (cf. [Abaev 1958: 619]), although the exact source of borrowing is unclear.
2414-Yaghnobi: ALP 1957: 308; Novák 2010: 134. Plural: pˈoːd-oːt {pódot}, with the a ~ oː Ablaut. Examples: {i barzangí póda-y-pĕš olówĕ
```


## [2026-09-14T01:31:41.092Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ravah ===\"; grep -n \"ravas.carat\\|ravas-carat\\|ravascarat\\|ravah-\" BRT.txt | head -10; echo \"=== LEW rus ===\"; grep -n \"^rus\\b\\|rus,.*Land\\|rūs\" LEW_1910.txt | head -10; echo \"=== LAT rus ===\"; grep -n \"^rūs\\|^rus \" LAT.txt | head -10; echo \"=== SKT room/ream/rural ===\"; grep -n \"^Room\\|^Ream\\|^Rural\\|^ROOM\" SKT.txt | head -10"
}
```


### [2026-09-14T01:31:41.208Z] TOOL RESULT

```
=== BRT ravah ===
6393:•1  PüEjL   iu    Yl'/.  10   scheid'et    drei   kjXen   Asa  betet.."  H. /.  I  f.** ■il-nakr.ätii/r/ftar.äni^aldäsaki^ü.-.mecchi-,      Komp.  mit  AS.  im  1.  Glied.  —  Pü.:  ahräkih iJrT,  an  i /rtflai.    Aber  die  beigegebenen  Defi-        iläyiinih.    —    1)  Ausg.  trennt    —    ')  Wörtl. : nilionen  sind  undeutlich;   vgL  DsT.  ZA.  /.  9I. '      "ciii  (est)  ..?  eius  qui  .  .",  Bthl.  BB.5.  301; S.  noch  SWienAW.  6/.  839.  8:    .  .  dh'l})  . .  ii       anricblig  JN.  JAOS.  ]-4.  Lxi. a:,,  »,>i«  ,  ^jrdumänja^g  a„M.  |,  j   +asi>m.sravah- '>   n.   'der  As'Md-  i-
13520:•  j.  d9U§.sravah-  n.,  Plur.  'übler  Ruf, schlechter  Leumund':  ula  buya  ..  uta  'vä (AP.)  hacimnS  ".  .  und  Üblen  Ruf  mögest du  bekommen"  Y. //.  i.
14980:•  j.  paiti.par^tö.-sravah-  Adj.  'der  die (heiligen)  Lehren  erfragt,  (durch  Fragen) erkundet  hat' :  narim  . .  vJdus^ga^sm  vtdul.- yasfiim  'vatahsm  mqsdrtm  V.  lÄ  5 1 ;  — ähravans  parsts.vaiarth5  'variks  Yt  5. 91 .
17328:bittm  Jramna  V.  to.  y,    3,  a*,  15;    —  '  j-  ^buji-aravah-')  m.  ES.  eines  Glau-
17662:•  j.  fra'pt«r9-Jät-  Adj.  '(im  Flug  sich  be- wegend, FlUgeltier,  spez.)  Vogel';  vtspamca gqm  .  .  'jätqmca  (ASf.) "'  ravascaratqmca Y.  77. 9;  —  dsmqn  .  .  yäca  °jqn  (APn.)'* yäia  ravascarqn  \k.8.^Z\  —  ratavB  -jäta (APm.)  .  .  ravascarata  Vr.  2.  i ;  —  ratavS 'Jafqm  (GP.)  ..  ravasäiratqm  Vr.7.  i,  Yt
24087:•  j.  viJt'sravah-  m.  EN.  eines  Gläubigen: uxsänS  (sd.)  'vatihS  düralsrstahe  Yt 13.  129.
25202:•  j.  ravah-  n.  'freier  Raum,  Freiheit':  ys
26352:•  j.  Sizdra-  Adj.  'scheu':  spsnim  slidr?» .  .  yim  var?hapartm  "den  scheuen  Hund V.  (Igel)"  V.  13.  z;—  auruna{sA.ya  gairi- säcB  sizdra^a  ravascarats  Yt  8.  36.
27190:•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
27377:•  j.,  g.  sravah-  n.  i)  'Wort'  (in  koll. Sinn),  (Plur.)  'Worte':  at  vS  ximaihyä asünä  va^ä  x^arai^yä (sA.)  vaintyä  'vi" Y.  2tV.  10.  a)  sva.  'Spruch,  Lehre': dusjastis  'vä  mSrindaiisA^  V.^2. 9;  10;  1 —  ya  ränhaym  (Sp.  iji?  u-)  'vanha*''  1 vahistät  syao%anäi  mantiVW  Y.32.  la;  —  j masda  al  insi  vahiHa  'vsscä  iyaohanäcä ' vao/ä  . .  isiidpm  (sd.)  stS/J  Y.  34.  is^^i  — yai  ta    'Vit  dtvn/ayan  ya  ..  al%rapaiayö\
=== LEW rus ===
=== LAT rus ===
9995:rus n'est nulle part atteste directemenb: les gloses ont cario oncarrio-,
13473:rus ire. De IA "eatreprendre, essayer", souvent, mais non n^cessai-
=== SKT room/ream/rural ===
16204:Room,  space,  a  chamber.  (E.)  The  old mcaniri^;  is  Apace,  place.  M.  E.  r<mm. A.  S.  rtim\  'na^fdon  n//w '  =  they  had  no roum,  Lake,  U.  7.  We  also  find  adj.  rUm^ spacious.  +  Da.  ttnm,  adj.,  spacious, ruim,  sb.,  room ;  Icel.  nimr,  spacioas ; rtim,  i^ace,  Dan.  and  Swcd.  nvm,  adj.  and sb. ;  Goth,  rumj^  adj.  and  sb.,  G.  mum, sb.  Allied  to  L.  rus,  open  country.  Der. roomy^  adj.,  used  for  M.  E.  roum,  adj.
```


## [2026-09-14T01:31:48.358Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor n in range(25120,25260):\n    l=lines[n-1].strip()\n    if re.fullmatch(r'1[45]\\d\\d',l): print(n,l)\n\"; echo \"=== ravascarat entry ===\"; grep -n \"ravas.carat-\\|ravascarat-\" BRT.txt | head -5"
}
```


### [2026-09-14T01:31:49.602Z] TOOL RESULT

```
25198 1514
=== ravascarat entry ===
```


## [2026-09-14T01:32:00.173Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://starlingdb.org/new100/irn.pdf\" --note \"page 425: Kassian/Starostin annotated Iranian Swadesh list — Av. uruθuuan- 'entrails/belly (Ahuric)' Bartholomae 1531-32; Yaghnobi šikampa/iškampa 'stomach' separate from it\" 2>&1 | tail -3"
}
```


### [2026-09-14T01:32:04.772Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/62911168abe12f23.txt
```


## [2026-09-14T01:42:46.727Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-425.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\ndata = {\n \"pdf_page\": 425,\n \"book_page\": 395,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Reuto, Routo, Rut\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *reuto-, *routo-, *rut- 'stomach, intestines (of an animal)'\",\n   \"note\": \"Pokorny's entry 'reuto-, routo- rut-, Meaning: stomach, intestines (of an animal)' runs over pp. 873-874, so Nourai's POK:873 for the root box and POK:874 for the nodes are both right. The root label 'Indo-European' is correct only in a weak sense: the root rests on an Iranian-Germanic isogloss (MP rot, NP ruda, Av. uruθwar-/-wan-; OE reada, Du. roode, Swed. dial. rudda), Pokorny's only authority being Liden, KZ 61, 14 f. It is absent from Walde-Pokorny (1927-32) and from Watkins/AHD, so it is a post-1932 addition rather than a classical IE root. The gloss Nourai gives ('intestines, bowels') matches Pokorny.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *reuto-/*routo-/*rut- به معنای «شکم، روده (جانور)» در فرهنگ پوکورنی (ص ۸۷۳–۸۷۴) آمده است و ادعای نورایی درست است. باید دانست که این ریشه فقط بر پایهٔ همسانی زبان‌های ایرانی و ژرمنی بازسازی شده و پوکورنی تنها به لیدن (KZ 61) استناد کرده است؛ در والده–پوکورنی و در فهرست واتکینز (AHD) این ریشه نیست.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D9%87\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:873\", \"status\": \"supports\", \"note\": \"POK_full.txt (indo-european.info dump), block 'Root / lemma: reuto-, routo- rut- / Meaning: stomach, intestines (of an animal) ... Page(s): 873-874'; material: 'Middle Persian rot ‘intestines, entrails of Rindes’, npers. ruda, Pl. rudag-an ... jav. uruθwara, -wan- n. (*rut-uar-, -uan-) ‘intestines, entrails, belly’; Old English reada ... References: Liden KZ. 61, 14 f.' (grep -n 'lemma: reuto' POK_full.txt -> line 70898).\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"pp. 873-874 s.v. reuto-, routo- rut-\", \"stance\": \"supports\", \"note\": \"gloss and all four daughter branches (MP, NP, Av., Gmc.) as drawn by Nourai.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II (1927)\", \"stance\": \"silent\", \"note\": \"Pokorny gives no 'WP.' cross-reference for this root (only 'Liden KZ. 61, 14 f.'), i.e. the root is not in Walde-Pokorny; grep of WLD_Bd2_pages.txt for 'reuto', 'routo', 'uruθwar' found nothing (OCR is also very poor).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots R-\", \"stance\": \"silent\", \"note\": \"AHD_watkins1985.txt has reu-1, reu-2, reudh-1, reudh-2, reuə-, reug-, reugh-men-, reup-, rezg- but NO *reuto- 'intestines' — Watkins does not recognise the root.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. reut-\", \"stance\": \"silent\", \"note\": \"IEC.txt line 14581 'reut- (reuto, ið, rout-, rut-) ‘fling, dash’. Cf. routeio' — Mann's reut- is a different root ('fling'); he has no 'intestine' root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"uruthwara, uruthwan, uruthwasča\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Bartholomae's headword is 'j. uruθwan-, -θwar- n. ‘Eingeweide, Bauch’' (AiW col. 1530-33), an r/n-heteroclitic neuter of the archaic type *rut-uar- / *rut-uan- (Pokorny 874) built on the zero grade *rut- of *reuto-. Initial uru- is the regular Avestan prothetic/anaptyctic rendering of syllabic r (r̥ > ǝrǝu > uru-), and -θw- is *-tw- with the regular Avestan t > θ before w. The third form, uruθwąsca, is not a separate stem but the attested nom.-acc. plural uruθwą with the enclitic -ca 'and' (Yt 13.11 astica gaonaca ... uruθwąsca pasūsca), the -ąs- being the regular sandhi of -ą + ca; Nourai lists an inflected text-form beside two stems. The word is used of the entrails of 'Ahuric' (good) creatures, the daevic counterpart being maršu-. Meaning 'entrails, belly' is correct; V 4.48 yō gəuš uruθwarə ham.pafraιti and the figurative V 5.30 'the core (of the religion)' are Bartholomae's citations.\",\n     \"derivation_fa\": \"در اوستا ستاک uruθwan-/uruθwar- (خنثی) به معنای «روده، اندرونه، شکم» است (بارتولومه، ستون ۱۵۳۰–۳۳) که از نوع نام‌های دوگانه‌ستاک r/n است: *rut-uar-/*rut-uan-. اولِ uru- همان بازتابِ معمولِ rِ هجایی هندواروپایی در اوستایی است و -θw- دگرگونی آوایی *-tw- است. صورت سوم (uruθwąsca) ستاک جداگانه‌ای نیست، بلکه جمع uruθwą به افزودنِ پیوستهٔ -ca «و» است (یشت ۱۳،۱۱). ادعای نورایی درست است.\",\n     \"sources\": [\"https://starlingdb.org/new100/irn.pdf\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. reuto-: 'jav. uruθwara, -wan- n. (*rut-uar-, -uan-) ‘intestines, entrails, belly’' — exactly the arrow drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 1530-33 s.v. uruθwan-, -θwar-\", \"stance\": \"supports\", \"note\": \"BRT.txt line 25521: '• j. uruθwan-, -θwar- n. ‘Eingeweide, Bauch’ ... auch Plur.: astica gaonaca ... uruθwąsca pasūsca fravāxšasca Yt 13.11'; and the closing note 'Vgl. np. rūda, nbal. rōδ ‘Eingeweide’; Bthl. IF. 5.228.' — Bartholomae himself links the Avestan word with NP rūda.\"},\n      {\"src\": \"POK\", \"where\": \"p. 874\", \"stance\": \"supports\", \"note\": \"as in ref_check.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 84 s.v. *uruspar\", \"stance\": \"supports\", \"note\": \"PHD.txt line 599: '*uruspar [ʾwlwspl = Av. uruθβar-] intestines, womb; core, essence' — MacKenzie knows an actual Pahlavi continuation of the Avestan word, and its senses ('intestines, womb; core') match Bartholomae's.\"},\n      {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"no Old Persian cognate of uruθwar- is recorded.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"aškumb\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Pahlavi aškamb / aškom(b) [ʾškmb, ʾskwm(b)] 'belly, womb' is real (MacKenzie p. 12; Nyberg II, s.v.), and it is indeed the word the Zand uses to render Avestan uruθwan-: Bartholomae notes at the end of the entry 'Pü. (ru F.): škamb', and Tavoosi's Šāyest-nē-Šāyest glossary (SNS p. 36) prints aškumb with the Avestan uruθwąsca beside it. But that is a TRANSLATION equivalence in the Pahlavi version, not a phonetic descent: uruθwan-/uruθwar- cannot yield aškamb by any Middle Persian sound law (there is no source for the šk- cluster or the -mb), and MacKenzie records the genuine Middle Persian continuant of Av. uruθβar- separately as *uruspar 'intestines, womb; core, essence'. aškamb is an independent Iranian word: cf. Manichaean MP škmb, Sogdian škmb, Pazand aškum/iškam, Yaghnobi šikampa/iškampá 'stomach', for which Morgenstierne-type reconstructions start from *(s)kamb-/*stamb-, not from *rut-. Nourai's arrow therefore mistakes a Zand gloss for an etymology.\",\n     \"derivation_fa\": \"واژهٔ فارسی میانهٔ aškamb/aškomb «شکم، زهدان» درست است (مکنزی ص‌۱۲؛ نیبرگ)، و در زند، همین واژه برابرِ اوستاییِ uruθwan- آورده شده است (بارتولومه: «Pü. škamb»؛ واژه‌نامهٔ شایست نه شایست ص‌۳۶). اما این فقط برابرنهادِ ترجمه‌ای است و نه تحولِ آوایی؛ از uruθwar- به هیچ روی نمی‌توان aškamb ساخت، و مکنزی بازماندهٔ راستینِ آن را جداگانه *uruspar «روده، زهدان» ثبت کرده است. aškamb واژه‌ای جداست (قیاس کنید سغدی و مانوی škmb، پازند aškum، یغنابی šikampa). بنابراین پژوهش امروزی پیکانِ نورایی را رد می‌کند: این یک «برابرِ زندی» است، نه ریشهٔ آوایی.\",\n     \"sources\": [\"https://starlingdb.org/new100/irn.pdf\", \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"SNS:36\", \"status\": \"partial\", \"note\": \"SNS_pages.txt leaf 35 (≈ printed p. 36), line 2231: '... aškumb : ...' with 'uruθwasca' printed on the next line and 'aškum (Mir. Man. II, 63)' below — Tavoosi's glossary does put the Pahlavi word beside the Avestan one, which is Nourai's source; but the glossary is a word-list of the Pahlavi text Šāyest-nē-Šāyest with its Avestan correspondences, so it documents a translation equivalence, not a descent.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 12 s.v. aškamb; p. 84 s.v. *uruspar\", \"stance\": \"contradicts\", \"note\": \"PHD.txt line 221: 'aškamb [KLSE < A kršʾ; ʾškmb | M škmb, N šikam] belly, womb. ~ag [-k | N šikamba] = aškamb'; 'aškom(b) [ʾskwm(bʾ)] = aškamb' — no Avestan etymon given, while the separate lemma '*uruspar [ʾwlwspl = Av. uruθβar-] intestines, womb' shows what the Avestan word really became in Pahlavi.\"},\n      {\"src\": \"NYB\", \"where\": \"Glossary (Manual of Pahlavi II) s.v. aškamb\", \"stance\": \"contradicts\", \"note\": \"NYB_vol2_glossary.txt line 737: 'aškamb [ʹškmbʹ], aškam [ʹškm], aškom [škwm] ... belly, stomach, womb ... — MPrs škmb (A-H II; Sogd. 3176); Paz. aškum (Mx), iškam (SGV); NP iškam, šikam.' Nyberg derives it from the MP/Sogdian škmb family, not from Avestan uruθwan-.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 1530-33 s.v. uruθwan-\", \"stance\": \"partial\", \"note\": \"BRT.txt line 25523: 'Pü. (ru F.): škamb, (in V. 1): an dāšn ..., (sonst): transkr.' — Bartholomae records škamb only as the Pahlavi VERSION's rendering, and elsewhere the Zand simply transcribes the Avestan word.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 226 (HUB.txt l. 9189)\", \"stance\": \"contradicts\", \"note\": \"'šikam (A. M. 78,6) = šikanb ‘Bauch’, phl. šk(u)mb ZPGl. 10,7' — Hübschmann sets up NP šikam/šikanb < Phl. šk(u)mb with no Avestan antecedent.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"eškam «اشکم ( شکم ، شکمبه )»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP اشکم / شکم (eškam, šekam) continues Middle Persian aškamb [ʾškmb] directly: the final -mb simplified to -m in New Persian (aškamb > aškam > šikam, with the usual loss of the prothetic a- before šC-), while the -mb is preserved in the by-forms شکنب šekanb and شکمبه šekambe 'rumen, paunch' (< MP aškambag). Hübschmann (Pers. Stud. p. 226) already gives 'šikam = šikanb ‘Bauch’, phl. šk(u)mb'; MacKenzie writes 'aškamb ... | N šikam' and 'aškambag | N šikamba'; Nyberg adds Pazand aškum / iškam. Rumi's line quoted in the book (شیر بی دم و سر و اشکم که دید؟) attests the older full form aškam in classical Persian. So the node itself is right — only its attachment through node 2 to the Avestan word fails.\",\n     \"derivation_fa\": \"«اشکم/شکم» مستقیماً از فارسی میانهٔ aškamb آمده است؛ خوشهٔ پایانی -mb در فارسی نو به -m ساده شده (aškamb > aškam > شکم) و همزهٔ آغازین نیز افتاده است؛ اما در صورت‌های «شکنب» و «شکمبه» (از aškambag) مانده است. هوبشمان و مکنزی و نیبرگ همین را می‌گویند، و بیت مولانا که در کتاب آمده گواه صورت کهنِ «اشکم» است. پس خودِ این پیوند درست است؛ ایراد تنها در پیوستنِ آن به ریشهٔ اوستاییِ uruθwan- است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D9%85\"],\n     \"ref_check\": [\n      {\"ref\": \"SNS:36\", \"status\": \"partial\", \"note\": \"SNS_pages.txt leaf 35 gives the Pahlavi aškumb of the Šāyest-nē-Šāyest and the Manichaean aškum; the New Persian outcome شکم is implicit rather than stated, and the Avestan link is a text-correspondence only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 12\", \"stance\": \"supports\", \"note\": \"'aškamb ... | M škmb, N šikam' and '~ag [-k | N šikamba]' — MacKenzie gives exactly NP شکم and شکمبه as the descendants.\"},\n      {\"src\": \"NYB\", \"where\": \"Glossary s.v. aškamb (NYB_vol2_glossary.txt l. 737)\", \"stance\": \"supports\", \"note\": \"'Paz. aškum (Mx), iškam (SGV); NP iškam, šikam.'\"},\n      {\"src\": \"HUB\", \"where\": \"HUB.txt l. 9189\", \"stance\": \"supports\", \"note\": \"'šikam (A. M. 78,6) = šikanb ‘Bauch’, phl. šk(u)mb'.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss, R/Š section\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for 'šikam', 'kamb', 'Bauch' finds no numbered entry for شکم; Horn does not treat the word.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"rôt 1\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian rōd [lwtʾ] 'intestine, gut', with its productive diminutive/derivative rōdīg [lwtykʾ] (pl. rōdīgān 'entrails, guts'), continues Proto-Iranian *rauta- < PIE *reuto- with the regular MP outcome of *au > ō and intervocalic *-t- written -t- but pronounced -d- in late MP. Pokorny prints it under the root: 'Middle Persian rōt ‘intestines, entrails of Rindes’'. Nourai's '1' is his homonym-number, distinguishing this rōd from rōd 'river' (< Proto-Iranian *hrautah-, OP rautah-) and rōd 'stringed instrument' — three homophones MacKenzie also keeps apart. Attaching the Pahlavi word directly to the root (not under the Avestan node) is correct: MP rōd continues the plain *reuto-, whereas Av. uruθwar- continues the r/n-stem extension *rut-uar-.\",\n     \"derivation_fa\": \"پهلوی rōd [lwtʾ] «روده» و صورت مشتقِ rōdīg (جمع: rōdīgān «امعاء و احشاء») از ایرانی باستان *rauta- و آن از هندواروپایی *reuto- است؛ دوگانهٔ au در فارسی میانه به ō بدل شده است. پوکورنی دقیقاً همین را می‌آورد. عدد ۱ در «rōt 1» شمارهٔ همآوایی است تا از rōd «رود، رودخانه» (از *hrautah-، پارسی باستان rautah-) بازشناخته شود. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. reuto-: 'Middle Persian rot ‘intestines, entrails of Rindes’' — the Pahlavi form is Pokorny's first witness for the root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 72 s.v. rōdīg (PHD.txt l. 559)\", \"stance\": \"supports\", \"note\": \"'rōdīg [lwtykʾ | (N rōda)] intestine, gut; ~ān, (pl.) entrails, guts' — listed separately from '1rōd [lwtʾ | M rwd, N ~] river' and '*rōd [lwtʾ | N ~] stringed instrument'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 628, p. 139\", \"stance\": \"supports\", \"note\": \"HRN.txt leaf 161: '628. rūde (*rōde) ‘Eingeweide’. ... phlv. rōtīk ‘Eingeweide’ (AV.).'\"},\n      {\"src\": \"NYB\", \"where\": \"Glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for 'rōtīk'/'rotik' yields no entry — the word does not occur in Nyberg's selected texts.\"},\n      {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to روده (BQT_v2_pages.txt leaf 430)\", \"stance\": \"supports\", \"note\": \"'پهلوی rōt «اونوالا Unvala» (امعاء و احشاء)، کردی ...، بلوچی rōδ/rōs، سریکلی raud' — Mo'in gives the Pahlavi rōt with Unvala as source.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Persian\", \"words\": \"rūdeh «روده»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP روده rōda / rūda 'intestine' is the regular New Persian reflex of MP rōdīg: MP -īg > NP -a (rōdīg > rōda, exactly as MP bālīg > NP bāla); the MP majhūl ō is preserved in the classical pronunciation rōda and only later raised to rūda in Iran. Horn (no. 628, p. 139) explicitly reconstructs the majhūl vowel — 'rūde (*rōde) ‘Eingeweide’ ... das neupersische Wort muss dem Bal. und Sar. zu Folge auch ursprünglich einen Majhūlvokal gehabt haben' — comparing Baluchi rōδ/rōs and Sariqoli raud. Pokorny derives the Persian form from a suffixed *reuto-ko- (= the MP -īg formation). Cognate outside Iranian: OE rēada, English reed 'abomasum of a ruminant', Swedish dial. rudda.\",\n     \"derivation_fa\": \"«روده» دنبالهٔ فارسی میانهٔ rōdīg است؛ پسوند -īg در فارسی نو به -ه (-a) بدل می‌شود و واکهٔ مجهولِ ō در تلفظ کهن مانده و سپس به ū تبدیل شده است. هرن (شمارهٔ ۶۲۸، ص ۱۳۹) بر پایهٔ بلوچی rōδ و سریکلی raud تأکید می‌کند که صورت اصلی *rōde بوده است، و معین در حاشیهٔ برهان قاطع همین را می‌آورد. هم‌ریشهٔ بیرون‌ایرانیِ آن انگلیسی کهن rēada است. ادعای نورایی درست است. (ویکی‌واژه بی مأخذ «روده» را به *Hrawtáh یعنی همان ریشهٔ «رود/رودخانه» برمی‌گرداند که با هرن و پوکورنی نمی‌خواند.)\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF%D9%87\", \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"'npers. ruda, Pl. rudag-an ‘intestines, entrails’ (*reuto-ko-)'.\"},\n      {\"ref\": \"HRN:139\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 161 = printed p. 139, entry '628. rūde (*rōde) ‘Eingeweide’. Kās. rāvə, rūvə. phlv. rōtīk ‘Eingeweide’ (AV.). kurd. rūm; bel. rōδ, rōs (331); sar. raud.' — precisely Nourai's arrow.\"},\n      {\"ref\": \"BQT:970\", \"status\": \"supports\", \"note\": \"the روده entry with Mo'in's etymological footnote stands at BQT_v2_pages.txt leaf 430 ('روده ... امعای گوسفند و غیره باشد'; footnote: 'پهلوی rōt «اونوالا» (امعاء و احشاء)، ... بلوچی rōδ/rōs، سریکلی raud، [پوکورنی] 874'). Our leaf-to-page mapping for vol. 2 is only approximate, but Aryanpur's independent entry for روده (ARY_pages.txt, pdf page 310) cites 'برهان قاطع: ۹۷۰' for the same word, confirming that BQT p. 970 is indeed روده.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 628, p. 139\", \"stance\": \"supports\", \"note\": \"see ref_check; Horn keeps rūde 'Eingeweide' (628) strictly apart from rōd 'Fluss' (627, < ap. rautah-).\"},\n      {\"src\": \"BQT\", \"where\": \"leaf 430 (≈ printed 970)\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote as quoted.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt pdf page 310 (روده)\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry lists پهلوی rōt, rōtīk; بلوچی rōδ; انگلیسی کهن RĒADA, انگلیسی reed with the note 'چم این واژه در انگلیسی نوین: شکم جانور' — i.e. Pokorny's set exactly, and cites برهان قاطع ۹۷۰.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie p. 72\", \"stance\": \"supports\", \"note\": \"'rōdīg [lwtykʾ | (N rōda)] intestine, gut' — MacKenzie writes the New Persian outcome with majhūl ō, as Horn requires.\"},\n      {\"src\": \"BRT\", \"where\": \"col. 1533\", \"stance\": \"supports\", \"note\": \"'Vgl. np. rūda, nbal. rōδ ‘Eingeweide’; Bthl. IF. 5.228.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Rewe, Rū 3\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *rewh₁- / *reuə- : *rū- 'to open; open space, wide'\",\n   \"note\": \"Pokorny p. 874: 'Root / lemma: reuə- : rū-, Meaning: to open; wide', with exactly Nourai's material — Av. ravah- and ravas-carət-, Lat. rūs, Gmc. *rū-ma- (Goth. rūms), plus MIr. róe, OCS ravĭnŭ, Toch. AB ru- 'open'. Watkins/AHD prints the root as 'reuə-. To open; space. [Pok. reuə-, rū- 874]', so Nourai's 'Rewe, Rū 3' (his spelling of reuə- : rū-, numbered 3 to distinguish his other Rū entries) and his gloss 'to open, open space' are both right. This entry is uncontroversial in all the standard handbooks; the modern laryngealist notation is *rewh₁-.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *reuə- : *rū- (در نگارش امروزی *rewh₁-) به معنای «گشودن؛ فضای باز» است؛ پوکورنی (ص ۸۷۴) و واتکینز (AHD) دقیقاً همین مواد را می‌آورند: اوستایی ravah-، لاتین rūs، ژرمنی *rūmaz. نام و زبان و معنای ریشه در جدول نورایی درست است و در هیچ منبعی مورد اختلاف نیست.\",\n   \"sources\": [\"https://www.etymonline.com/word/room\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"POK_full.txt line 70914: 'Root / lemma: reuə- : rū- / Meaning: to open; wide / Material: Avestan ravah- n. ‘Raum, Weite’, ravas-carat- ‘was sich in Freien bewegt’; Latin rus, ruris ‘land ... ’ (*reuos); ... Germanic rū-ma- in Gothic rūms ... / References: WP. II 356 f., WH. II 454, Trautmann 14. / Page(s): 874'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 874\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reuə- (AHD_watkins1985.txt l. 897)\", \"stance\": \"supports\", \"note\": \"'reuə-. To open; space. 1. Suffixed variant form *rū-mo- (< *ruə-mo-) in Germanic *rūmaz ... 2. Suffixed form *reu(ə)-es- in Latin rūs, “open land”, the country: RURAL, RUSTIC. [Pok. reuə-, rū- 874.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 356 f.\", \"stance\": \"supports\", \"note\": \"cited as the authority by both Pokorny ('WP. II 356 f.') and Buck ('Walde-P. 2.356'); the local WLD_Bd2 OCR is too corrupt to quote the page directly.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p. 464-465 (§7.24 'a room')\", \"stance\": \"supports\", \"note\": \"SYN.txt l. 11701, just before the page marker '465': 'Goth. ON, OE, OHG rūm ‘space, place’ (: Av. ravah- ‘space’, Lat. rus ‘country’, etc. Walde-P. 2.356), hence also ‘a room’ in ME rowme, NE room, Sw. rum.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"ravah; ravas-čarât\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. ravah- n. 'free space, freedom' (Bartholomae, AiW col. 1514: 'j. ravah- n. ‘freier Raum, Freiheit’') is an s-stem *rew-os- from *reuh₁-, morphologically identical with Latin rūs (< *rewos, gen. *rewes-os > rūris). The compound ravas-carət- (nom. -carəδ?; attested acc. pl. ravascaratəmca Y 71.9, Vr 2.1, Yt 8.36 of wild beasts and birds) is 'moving in the open', a bahuvrīhi-type governing compound of ravah- with the root car- 'to move, graze' (→ Nourai's cross-reference to his root Kwel, PIE *kʷel- 'to turn, move about', which is indeed the source of Av./Skt. car-). Both words are correctly cited, correctly glossed and correctly attached to the root.\",\n     \"derivation_fa\": \"اوستایی ravah- (خنثی، ستاک s-دار) به معنای «فضای آزاد، گشادگی» از *rew-os- است و از نظر ساخت دقیقاً برابر لاتین rūs (مضاف‌الیه rūris) است؛ بارتولومه (ستون ۱۵۱۴) آن را «freier Raum» معنا کرده است. ترکیب ravas-carət- «آنکه در فضای باز می‌گردد» از همین نام و ریشهٔ car- «رفتن، چریدن» ساخته شده است. هر دو واژه درست و مستنداند.\",\n     \"sources\": [\"https://www.etymonline.com/word/room\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"'Avestan ravah- n. ‘Raum, Weite’, ravas-carat- ‘was sich in Freien bewegt’.'\"},\n      {\"ref\": \"SYN:465\", \"status\": \"supports\", \"note\": \"SYN.txt l. 11701 (the printed page-number '465' stands at l. 11706, so this is the top of Buck p. 465): '... (: Av. ravah- ‘space’, Lat. rus ‘country’, etc. Walde-P. 2.356) ...'.\"},\n      {\"ref\": \"KLN:1356\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l. 33094, immediately after the page marker '1356' (l. 33085) — s.v. 'room': 'fr. I.-E. base *rēu-, ‘wide, open’, whence Toch. AB ru-, ‘to open’, Avestic ravah-, ‘space’, L. rus, ‘open country’, OIr. roi, roe, ‘plain field’.' Nourai's page number is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 1514 s.v. ravah-; col. ~1000 s.v. fra.ptərə-jāt- (ravascaratəmca)\", \"stance\": \"supports\", \"note\": \"BRT.txt l. 25202: '• j. ravah- n. ‘freier Raum, Freiheit’'; l. 17662 quotes the attested forms 'ravascaratəmca Y. 71.9 ... ravascarətqmca Vr. 2.1' and l. 26352 'auruna ... gairišācō sizdrača ravascaratō Yt. 8.36'.\"},\n      {\"src\": \"POK\", \"where\": \"p. 874\", \"stance\": \"supports\", \"note\": \"as in ref_check.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p. 465, also §12.x (SYN.txt ll. 22804, 23254)\", \"stance\": \"supports\", \"note\": \"'ChSl. ravinŭ ... : Av. ravah- ‘open space’, Lat. rus ‘country’ vs. ‘town’, Goth. rūms ‘roomy, spacious’, OE rūm ‘space’ (NE room), etc. Walde-P. 2.356 f.'\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Germanic\", \"words\": \"rumaz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *rūmaz adj. 'roomy, spacious' (and the substantivised neuter *rūma- 'space') goes back to a suffixed *rū-mo- < *ruə-mo-, the zero grade of *reuə- plus the adjectival *-mo-; the Germanic long ū is the regular outcome of *uə/*uH. Attested in Gothic rūms 'roomy' and n. rūm 'space', ON rūmr, OS/OFris./OE rūm, OHG/MHG rūm. Watkins spells it *rūmaz exactly as the chart does; Klein derives the nouns from the Teutonic adjective *rūma-. Correctly attached directly to the root rather than through Avestan.\",\n     \"derivation_fa\": \"ژرمنی آغازین *rūmaz «گشاد، جادار» از *rū-mo- (پایهٔ صفرِ ریشه به‌علاوهٔ پسوند صفت‌ساز *-mo-) است؛ ū کشیده بازتاب معمولِ *uə است. نمونه‌ها: گوتی rūms و rūm، انگلیسی کهن rūm. نگارش نورایی همان نگارش واتکینز است و ادعا درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/room\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l. 897 s.v. reuə-: 'Suffixed variant form *rū-mo- (< *ruə-mo-) in Germanic *rūmaz in: a. Old English rūm, space: ROOM; b. Old French run, ship's hold, space: RUMMAGE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1356 s.v. room\", \"stance\": \"supports\", \"note\": \"'These nouns are substantivations of the Teut. adj. *rūma- appearing in OE., MHG. rūm, OHG. rūmi, ON. rūmr, Dan., Swed. rum, Du. ruim, Goth. rūms, ‘roomy, spacious’.'\"},\n      {\"src\": \"POK\", \"where\": \"p. 874\", \"stance\": \"supports\", \"note\": \"'Germanic rū-ma- in Gothic rūms ‘capacious, wide’, rūm n. ‘Raum’, Old Icelandic rūmr ... abgel. verb Germanic *rūmian.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt l. 16204 s.v. Room\", \"stance\": \"supports\", \"note\": \"'Room, space, a chamber. (E.) ... A.S. rūm ... Goth. rūms, adj. and sb., G. raum, sb. Allied to L. rus, open country.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"room; ream 2; reamer\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"(a) ROOM: OE rūm n. 'space, extent' (substantivised from the adjective rūm) > ME roum/rum > room; the concrete sense 'chamber' is a late-ME nautical specialisation ('space in a ship'), first 14th c. (b) REAM v. 'to enlarge a hole' is Nourai's 'ream 2' (his 2 distinguishing it from ream 'twenty quires', which is Arabic rizma via Spanish resma — an unrelated homonym Klein lists just above). It is OE rȳman 'to make room, widen', a denominative *rūmjan from rūm with i-umlaut ū > ȳ, whence ME rumen/remen and the dialectal rime; so it belongs under the Germanic node, exactly as drawn. (c) REAMER is the English agent noun in -er from that verb (18th c., the tool). Watkins lists only ROOM and RUMMAGE under the root, but Klein covers ream/reamer explicitly.\",\n     \"derivation_fa\": \"سه واژهٔ انگلیسی از همان پایهٔ ژرمنی‌اند: room از انگلیسی کهن rūm «فضا» (معنای «اتاق» تحولی متأخر و نخست دریانوردی است)؛ ream «گشاد کردن سوراخ» از انگلیسی کهن rȳman «جا باز کردن»، فعلی برساخته از rūm با امالهٔ (i-umlaut) ū > ȳ؛ و reamer نام ابزار از همان فعل با پسوند -er. عدد ۲ در «ream 2» برای جدا کردن از ream «بستهٔ کاغذ» است که از عربی رِزمه آمده و بی‌ربط است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/room\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins (AHD_watkins1985.txt l. 897; index l. 2199 'ROOM reuə-') derives ROOM and RUMMAGE from the root but does not list REAM/REAMER; for those Klein has to be used.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1307 s.v. ream (v.), reamer; p. 1356 s.v. room\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l. 31829: 'ream, tr. v., to enlarge a hole. — Lit. ‘to make room’, fr. ME. remen, rumen, fr. OE. rȳman, ‘to make room, widen’, fr. rūm, ‘spacious, wide’ ... reamer, n., a tool for enlarging a hole. — Formed fr. prec. word with agential suff. -er.' l. 33094 s.v. room: 'ME. roum, rum, fr. OE. rūm, ‘space’ ... Cp. ream, ‘to enlarge a hole’.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt l. 16204 s.v. Room\", \"stance\": \"supports\", \"note\": \"'The old meaning is space, place. M.E. roum. A.S. rūm ... Allied to L. rus, open country.'\"},\n      {\"src\": \"FSD\", \"where\": \"New Standard, R-section\", \"stance\": \"silent\", \"note\": \"not consulted for this uncontroversial English chain (Nourai cites only AHD here).\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"rūs\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin rūs, gen. rūris n. 'the country, open land (as opposed to the town), a farm' is an s-stem *rewos, gen. *rewes-os; intervocalic *-s- rhotacised to -r- in the oblique cases (*rewes-os > rūris) while the nominative kept -s, and *rewos contracted to rūs. It is thus the exact Latin match of Avestan ravah-. Pokorny prints 'Latin rus, ruris ‘land (in contrast to town, city), estate’ (*reuos)'; Watkins reconstructs 'Suffixed form *reu(ə)-es-'. Gloss 'open land' is right.\",\n     \"derivation_fa\": \"لاتین rūs (مضاف‌الیه rūris) «دشت، زمین باز، روستا (در برابر شهر)» از ستاک s-دارِ *rewos است؛ s میان‌دوواکه در لاتین به r بدل شده (قلب آوایی معروف به rhotacism) و از این‌رو rūris. این واژه برابرِ دقیقِ اوستایی ravah- است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/room\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:874\", \"status\": \"supports\", \"note\": \"'Latin rus, ruris ‘land (in contrast to town, city), estate’ (*reuos)' — POK_full.txt s.v. reuə- : rū-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. reuə-\", \"stance\": \"supports\", \"note\": \"'Suffixed form *reu(ə)-es- in Latin rūs, “open land,” the country: RURAL, RUSTIC.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck p. 465 and §12.x\", \"stance\": \"supports\", \"note\": \"'Lat. rus ‘country’ vs. ‘town’ ... : Goth. rūms, Av. ravah- ‘open space’. Walde-P. 2.356 f.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. rus\", \"stance\": \"silent\", \"note\": \"grep of LAT.txt for '^rūs'/'^rus ' returns only unrelated lines (9995, 13473); the OCR of the rūs article could not be located.\"},\n      {\"src\": \"LEW\", \"where\": \"Walde 1910 s.v. rus\", \"stance\": \"silent\", \"note\": \"grep of LEW_1910.txt for 'rus'/'rūs' as a headword found no entry in the OCR.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"rural\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin rūrālis 'of the countryside' (adjective in -ālis from the oblique stem rūr- of rūs) > Old French rural > Middle English rural (15th c.). Watkins lists RURAL (and RUSTIC, from rūsticus) as the English continuations of Latin rūs under the root; Klein s.v. rural: 'ME., fr. L. rūrālis, ‘pertaining to the country’, fr. rūs, gen. rūris, ‘the country’ap ... See room.' Nourai's edge Latin rūs → English rural is therefore right, the Old French stage being tacit.\",\n     \"derivation_fa\": \"انگلیسی rural از لاتین rūrālis (صفتِ -ālis از ستاک مایلِ rūr-) است که از راه فرانسهٔ کهن rural در سدهٔ پانزدهم میلادی وارد انگلیسی میانه شده است. کلاین و واتکینز هر دو همین را می‌گویند؛ نورایی مرحلهٔ فرانسه را نیاورده ولی پیکان نادرست نیست.\",\n     \"sources\": [\"https://www.etymonline.com/word/room\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index l. 2204: 'RURAL reuə-'; the root article has '... in Latin rūs, “open land,” the country: RURAL, RUSTIC.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1365 s.v. rural (KLN_1966.txt l. 33359)\", \"stance\": \"supports\", \"note\": \"'rural, adj., of the country. — ME., fr. L. rūrālis, ‘pertaining to the country’, fr. rūs, gen. rūris, ‘the country’, which is cogn. with OSlav. ravinŭ, ‘level’, OIr. roi, roe, ‘plain field’, OE. rūm, etc., ‘space’. See room.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Room\", \"stance\": \"partial\", \"note\": \"Skeat has no separate 'rural' headword in the concise edition, but under Room he already states the connexion with 'L. rus, open country'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"R.f.a'\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-West-Semitic *rpʔ 'to heal, mend, restore'\",\n   \"note\": \"The triliteral رفأ / r-p-ʾ is a genuine Common/West-Semitic root: Hebrew רפא rāṗāʾ 'he healed', Aramaic/Syriac rəṗā 'he healed', Arabic rafaʾa 'he mended, darned, repaired', Ethiopic rafaʾa 'he stitched together, mended'. Klein p. 1301 (s.v. Raphael) states exactly this comparison, so Nourai's KLN:1301 is on the mark, and Wiktionary derives Arabic رفأ from Proto-West-Semitic *rpʾ 'to heal, protect' (citing SED). One nuance: the primary Semitic sense is 'heal/restore', of which Arabic's 'darn, mend (cloth)' and Ethiopic's 'stitch' are specialisations; Nourai's root gloss 'to repair' is therefore the Arabic-Ethiopic meaning generalised to the root, not its oldest sense. The language label 'Semitic' is right.\",\n   \"note_fa\": \"ریشهٔ سه‌حرفی ر–ف–أ ریشه‌ای سامی است: عبری رافا «شفا داد»، سریانی rəṗā، عربی رفأ «رفو کرد، به هم دوخت»، حبشی rafaʾa. کلاین (ص ۱۳۰۱) همین قیاس را می‌آورد و ویکی‌واژه آن را از سامی غربی آغازین *rpʾ «شفا دادن، نگاه داشتن» می‌گیرد. تنها نکته آنکه معنای کهن‌تر، «شفا دادن» است و «ترمیم کردن» تخصیص معنایی عربی–حبشی است؛ با این حال ادعای نورایی درست است.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%A3\", \"https://en.wiktionary.org/wiki/Raphael\"],\n   \"ref_check\": [\n    {\"ref\": \"KLN:1301\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l. 31684-89, between the page markers 1300 (l. 31652) and 1307 (l. 31800), i.e. printed p. 1301: 'Raphael ... fr. Heb. Rəphaʾēl, lit. ‘God has healed’. Heb. raphā, ‘he healed’ (whence riphuʾah, ‘medicine, remedy’, marpē, ‘healing, cure’) ... is rel. to Syr. rəpha, ‘he healed’, Arab. rafaʾa, ‘he darned, mended, repaired’, Ethiop. rafaʾa, ‘he stitched together, mended’.' Nourai's page number is exact.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"p. 1301 s.v. Raphael\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"grep of FVQ_pages.txt for 'rafa'/'rafw' finds no entry — the root is native Arabic, so Jeffery has nothing to say.\"},\n    {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD_pages.txt l. 1226)\", \"stance\": \"partial\", \"note\": \"'رفأ / رفو ... في اليونانية ῥάπτω خاط' — al-Unaysi lists رفأ among 'foreign' words in Arabic and compares Greek rháptō 'to sew'; a minority view that would make the Arabic verb a loan rather than a Semitic inheritance.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"r.f.a', rafū\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic رَفَأ rafaʾa (root ر ف ء), form I with verbal noun رَفْء / رَفْو rafw — 'to mend, darn (a torn garment) so that the repair does not show'; hence the agent noun رفّاء raffāʾ 'darner'. The hamzated root رفأ regularly develops an unhamzated by-form رفا/رفو (rafawā, maṣdar rafw), which is the shape Nourai cites as 'rafū' and the shape Persian borrowed. Wiktionary traces the root to Proto-West-Semitic *rpʾ 'to heal, protect' (SED 16327), and Klein 1301 aligns Arab. rafaʾa directly with Heb. rāṗāʾ. The gloss 'to repair (damaged cloth)' is Lane's.\",\n     \"derivation_fa\": \"عربی رَفَأ (ریشهٔ ر–ف–ء، باب اول، مصدر رَفْء/رَفْو) به معنای «دوختن پارگی جامه به گونه‌ای که پیدا نباشد» است و از آن «رفّاء» ساخته شده است. ریشهٔ مهموز رفأ به‌طور معمول صورت نامهموزِ رفا/رفو نیز دارد که همان صورتی است که فارسی وام گرفته. کلاین آن را هم‌ریشهٔ عبری رافا می‌داند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%A3\", \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D9%88\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1301\", \"status\": \"supports\", \"note\": \"'... Arab. rafaʾa, ‘he darned, mended, repaired’' — Klein's wording is Nourai's gloss verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301 s.v. Raphael\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba\", \"stance\": \"silent\", \"note\": \"grep of AFM_pages.txt for 'رفو' finds only an unrelated line (l. 97); Addi Shir does NOT list رفو among the Persian words arabicised — i.e. he treats it as Arabic.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep of PLA_pages.txt for 'rafw', 'rafu', 'رفو' finds nothing — Asbaghi does not count رفو as a Persian loan in Arabic, which tells against Mo'in's معرّب note (see node 2).\"},\n      {\"src\": \"TAD\", \"where\": \"TAD_pages.txt l. 1226\", \"stance\": \"partial\", \"note\": \"al-Unaysi puts رفأ/رفو among foreign words and compares Greek ῥάπτω 'sewed' — an isolated claim not followed by Klein or the Semitists.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"rofū «رُفو»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian رفو rafū / rofū 'darning, invisible mending' is the Arabic maṣdar رَفْو rafw taken over as a noun and then given the Persian light-verb constructions رفو کردن and the agent noun رفوگر; the Arabic sukun-cluster -fw is resolved by an epenthetic ū (rafw > rafū), and the first vowel is variously a- or o- in Persian usage. Dehkhoda states it flatly: 'از رَفْو عربی است، واو را بدل به او کنند ...', and Wiktionary marks it 'borrowed from Arabic رَفْو (rafw) “fine-drawing”'. A dissenting voice must be recorded: in his footnote to Borhan-e Qāteʿ s.v. رفو, Mo'in writes 'معرّب آن: رَفْو ... قس: یونانی ῥάπτω خیاطی کرد، دوخت', i.e. he takes Persian rafō (with majhūl wāw) to be the source and Arabic rafw its arabicisation. Asbaghi's Persische Lehnwörter im Arabischen and Addi Shir do not include the word, and the Semitic cognate set (Heb./Syr./Eth.) is decisive, so the standard direction — Arabic → Persian, as Nourai draws it — stands.\",\n     \"derivation_fa\": \"«رفو» در فارسی وام‌واژهٔ مصدر عربی رَفْو است؛ خوشهٔ پایانی -fw با واکهٔ کشیدهٔ ū گشوده شده (rafw > rafū) و از آن ترکیبِ «رفو کردن» و نامِ شغلِ «رفوگر» ساخته شده است. دهخدا صریحاً می‌نویسد «از رَفْو عربی است» و ویکی‌واژه نیز آن را وام‌واژهٔ عربی می‌داند. در برابر، معین در حاشیهٔ برهان قاطع آن را فارسی می‌گیرد («معرّب آن: رَفْو») و با یونانی ῥάπτω مقایسه می‌کند؛ اما ازباغی و ادی شیر این واژه را در فهرست معرّبات فارسی نیاورده‌اند و هم‌ریشه‌های عبری و سریانی و حبشی جای تردید نمی‌گذارند. پس ادعای نورایی (عربی ← فارسی) درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D9%88\", \"https://abadis.ir/fatofa/%D8%B1%D9%81%D9%88/\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:167\", \"status\": \"not_checked\", \"note\": \"FVA = S.M. Nahvi, Farhang-e Vāžehā-ye ʿArabī dar Fārsī (1368/1989); refs_online.json records that no digital copy exists on any permitted platform. Note that Nourai's choosing a dictionary OF ARABIC WORDS IN PERSIAN for this node is itself evidence that he, like Dehkhoda, treats رفو as an Arabic loan.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' s.v. رفو with Mo'in's footnote 4 (BQT_v2_pages.txt ll. 24463, 24487; leaf 415 ≈ printed p. 955-965)\", \"stance\": \"contradicts\", \"note\": \"headword: 'رفو — بفتح اول و ثانی بواو مجهول ... پیوند شال و جامهٔ پاره و سوراخ‌دار باشد بنوعیکه معلوم نشود'; footnote: 'معرب آن، رفو (بفتح اول و سکون دوم). قس: یونانی ῥάπτω خیاطی کرد، دوخت' — Mo'in reverses the direction of borrowing.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. رفو (via abadis.ir)\", \"stance\": \"partial\", \"note\": \"'(رُ ) [ معر. ] (اِ. ) دوخت دررفتگی‌ها و پارگی‌های پارچه یا فرش ...' — the tag [معر.] marks the word as arabicised, keeping Mo'in's ambivalence; the Dehkhoda section on the same page is unambiguous: 'از رَفْو عربی است، «واو» را بدل به «او» کنند و فتحه (را) را نیز بدل به ضمه گردانند'.\"},\n      {\"src\": \"PLA\", \"where\": \"Asbaghi 1988\", \"stance\": \"silent\", \"note\": \"رفو is absent from the list of Persian loanwords in Arabic — evidence against the Persian-origin claim.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"supports\", \"note\": \"Klein's Semitic cognate set (Heb. rāphā, Syr. rəphā, Eth. rafaʾa) shows the Arabic verb to be inherited, not borrowed from Persian.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"râphâ; râphâ-e'l\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Hebrew רָפָא rāṗāʾ 'he healed, cured' (whence רְפוּאָה rəṗūʾā 'medicine', מַרְפֵא marpē 'healing') is the Hebrew reflex of the Semitic root; the semantic difference from Arabic ('mend cloth' vs 'heal') is the same metaphor as Latin sarcio / English 'patch up'. The theophoric name רְפָאֵל Rəṗāʾēl is a sentence-name, perfect rāṗāʾ + אֵל ʾēl 'God' = 'God has healed' (so Klein; Nourai's alternative rendering 'God is a healer' is the participial reading and equally current). Nourai's ☞ cross-reference to his root 'Layh' is his entry for ʾēl/Allah, which is the right place for the second element. The name is first attested in the Book of Tobit (Tobit 12:15, 2nd c. BCE).\",\n     \"derivation_fa\": \"عبری רָפָא (rāṗāʾ) «شفا داد» بازتاب عبریِ همان ریشهٔ سامی است؛ اختلاف معنایی آن با عربی («دوختن پارگی») همان استعارهٔ آشنای «ترمیم کردن» است. نام רְפָאֵל نامی جمله‌ای است: فعلِ ماضی rāṗāʾ + אֵל «خدا»، یعنی «خدا شفا داده است» (یا در خوانش وصفی «خدا شفابخش است»). نخستین کاربرد آن در کتاب طوبیت (سدهٔ دوم پیش از میلاد) است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1301\", \"status\": \"supports\", \"note\": \"'fr. Heb. Rəphaʾēl, lit. ‘God has healed’. Heb. raphā, ‘he healed’ (whence riphuʾah, ‘medicine, remedy’, marpē, ‘healing, cure’) ... For the second element in Raphael see El.' — Klein's own 'see El' matches Nourai's ☞ Layh cross-reference.\"},\n      {\"ref\": \"FSD:2051\", \"status\": \"not_found\", \"note\": \"FSD_vol3.txt carries the printed page number 2050 at l. 216580 (headwords rank/ransom) and the raph- run (raphanus, raphe, Raphia) at ll. 216905-216935, but the New Standard's main vocabulary has NO 'Raphael' entry between raphanus and Raphia; the proper name is in F&W's separate biographical/scriptural appendix, which this OCR does not paginate. Could not verify the citation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301 s.v. Raphael and p. 484 s.v. El\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l. 12751 s.v. El: 'Heb. El, ‘God’ ... Cp. ... the second element in Babel, bethel and in the PN.s Daniel, Emmanuel, Ezekiel, Gabriel, Gamaliel, Ishmael, Israel, Joel, Michael, Nathaniel, Raphael, Samuel.'\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III p. ~2050-2053\", \"stance\": \"silent\", \"note\": \"see ref_check — the raph- page range exists but contains no Raphael article.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery\", \"stance\": \"silent\", \"note\": \"grep for 'Raphael'/'rafa' in FVQ_pages.txt yields nothing; the Qur'an does not name Raphael (the Islamic إسرافيل is a different name), so Jeffery has no entry.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Greek\", \"words\": \"Raphael\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Koine Greek Ῥαφαήλ (Rhaphaḗl), the Septuagint/Tobit transcription of Hebrew Rəṗāʾēl: Greek writes the Hebrew ר with rough breathing Ῥ-, renders ṗ (spirantised p) by φ, and drops the guttural א between the vowels, giving -αη-. The name reached Greek through the Jewish Greek Bible in Egypt in the 2nd–1st c. BCE (Tobit 12:15 'ἐγώ εἰμι Ῥαφαήλ, εἷς ἐκ τῶν ἑπτὰ ἁγίων ἀγγέλων'), whence it passed into Christian Latin.\",\n     \"derivation_fa\": \"یونانی کوینهٔ Ῥαφαήλ آوانویسیِ عبری רְפָאֵל در ترجمهٔ هفتادتنی (سبعینیه) و کتاب طوبیت است: راء عبری با دمِ سخت (Ῥ)، ـپـ سایشی با φ، و الفِ میانی افتاده است. این وام‌گیری در سدهٔ دوم–اول پیش از میلاد از راه عهد عتیقِ یونانی رخ داده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1301\", \"status\": \"supports\", \"note\": \"'Raphael ... — Late L., fr. Gk. Ῥαφαήλ, fr. Heb. Rəphaʾēl' (KLN_1966.txt l. 31684-86).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III\", \"stance\": \"silent\", \"note\": \"no Raphael article in the main vocabulary (see node 3).\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 (A-?)\", \"stance\": \"silent\", \"note\": \"only volume 1 is available locally; R- is in the missing volume 2.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through node: Late/Ecclesiastical Latin Raphael, taken straight from the Greek of the Septuagint by the Vetus Latina and the Vulgate (Tobias 12:15 'ego enim sum Raphael angelus'); Latin kept the Greek spelling with ph and the final -el. From this Latin form descend both the French and the English names of nodes 6-8.\",\n     \"derivation_fa\": \"گرهٔ انتقالی: لاتینِ کلیسایی Raphael که مستقیماً از یونانیِ ترجمهٔ هفتادتنی گرفته شده و در وولگاتا (طوبیاس ۱۲:۱۵) آمده است؛ نگارش ph و پایانهٔ -el همان یونانی مانده است. فرانسه و انگلیسی هر دو از همین صورت لاتین برآمده‌اند.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; the Latin link is covered by Klein p. 1301 ('Late L., fr. Gk. Ῥαφαήλ'), the reference cited on the neighbouring nodes.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"supports\", \"note\": \"'Late L., fr. Gk. Ῥαφαήλ.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet\", \"stance\": \"silent\", \"note\": \"a biblical proper name is outside the scope of the Dictionnaire étymologique de la langue latine.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through node: French Raphaël (pronounced [ʁafaɛl]), the learned Church-Latin name adopted unchanged in spelling except for the diaeresis that keeps a-ë in hiatus; used both of the archangel and, from the 16th c., of the painter Raffaello Sanzio, whom French (and after it most of Europe) calls Raphaël. It is this French form, not the Latin or the Hebrew, that supplies the Persian of node 7.\",\n     \"derivation_fa\": \"گرهٔ انتقالی: فرانسه Raphaël که همان صورت لاتینی است با علامت ترما («) برای نگاه داشتنِ فاصلهٔ دو واکه؛ هم نام فرشته است و هم از سدهٔ شانزدهم نامِ نقاش ایتالیایی Raffaello. همین صورت فرانسوی منبع وام‌گیری فارسی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference given in the book for this pass-through node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"partial\", \"note\": \"Klein gives Late L. > E. and, s.v. Pre-Raphaelitism (l. 30125), the Italian painter's name Raffaello Sanzio; he does not track the French form, which is however the obvious European intermediary for Persian.\"},\n      {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"Devic covers Arabic/Persian/Turkish words in French, not Hebrew proper names; no entry.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"Râfâel «رافائل»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Modern Persian رافائل Rāfāʾel is a 19th-20th c. European loan, used for the archangel and above all for the painter (رافائل سانتسیو). The long ā of the first two syllables and the final -el without یـ reproduce French Raphaël [ʁafaɛl] / Italian Raffaele rather than Latin or Hebrew, so Nourai's route Latin → French → Persian is reasonable; Italian mediation for the painter's name is at least as likely, and the book gives no reference for the node. It should also be noted that Persian already had the name through the Arabic-Islamic tradition as روفائیل/رفائیل (Arabic رُفَائِيل), a Syriac-mediated form which is NOT the source of the modern رافائل. The gloss '“God is a healer”' is the meaning of the Hebrew original, not of the Persian word.\",\n     \"derivation_fa\": \"«رافائل» در فارسی وام‌واژه‌ای اروپایی از سدهٔ سیزدهم/چهاردهم هجری است که بیشتر برای نقاش ایتالیایی به کار می‌رود. صورت آوایی آن (دو الف کشیده و پایانهٔ ـئل بی یاء) با فرانسهٔ Raphaël یا ایتالیایی Raffaele می‌خواند و نه با عبری یا لاتین؛ پس مسیرِ نورایی پذیرفتنی است، هرچند واسطهٔ ایتالیایی نیز همان‌اندازه محتمل است و نورایی هیچ مأخذی نیاورده است. باید توجه داشت که صورت کهن‌تر و عربی‌میانجی، یعنی «روفائیل/رفائیل»، منبعِ این واژه نیست. حکم: با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is given in the book for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in, vols 5-6 (a'lam)\", \"stance\": \"silent\", \"note\": \"the proper-name volumes are not in the local library and vajehyab's Mo'in text covers only the lexicon volumes; no entry retrievable.\"},\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"partial\", \"note\": \"Klein confirms the European name and its Latin/Greek/Hebrew ancestry but says nothing about Persian.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"Raphael, Raffael\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Raphael comes from Late Latin Raphael (Klein: 'Late L., fr. Gk. Ῥαφαήλ'), entering with the Apocryphal Book of Tobit and used from Middle English onward as an angel name and a given name. The second spelling 'Raffael' is not an English form but the Italian/German spelling of the painter's name (It. Raffaello, Ger. Raffael); it survives in English only inside the doublet adjective that Klein records — 'Raphaelesque, Raffaelesque, adj., in the style of the painter Raphael. — Formed fr. the name of Raffaello Sanzio (1483-1520)'. So the node is right, with the qualification that 'Raffael' is a borrowed continental spelling and is attached, in English, to the painter rather than the archangel.\",\n     \"derivation_fa\": \"انگلیسی Raphael از لاتینِ متأخر Raphael است که از راه کتاب طوبیت وارد شده و از دورهٔ انگلیسی میانه هم نام فرشته و هم نام اشخاص است. صورت دوم، Raffael، انگلیسی نیست بلکه نگارش ایتالیایی–آلمانیِ نام نقاش است و در انگلیسی فقط در صفتِ Raffaelesque باقی مانده است (کلاین). ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/Raphael\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1301\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l. 31684-90 (printed p. 1301): 'Raphael, 1) masc. PN. 2) an archangel mentioned in the Apocrypha. — Late L., fr. Gk. Ῥαφαήλ, fr. Heb. Rəphaʾēl ...'; immediately after: 'Raphaelesque, Raffaelesque, adj., in the style of the painter Raphael. — Formed fr. the name of Raffaello Sanzio (1483-1520) with suff. -esque.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 1301\", \"stance\": \"supports\", \"note\": \"as quoted; also l. 30125 s.v. Pre-Raphaelitism, 'from the forename of Raphael Sanzio (1483-1520)'.\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise\", \"stance\": \"silent\", \"note\": \"grep of SKT.txt finds no 'Raphael' headword — Skeat excludes proper names.\"},\n      {\"src\": \"FSD\", \"where\": \"vol. III p. ~2050-2053\", \"stance\": \"silent\", \"note\": \"no Raphael article in the main vocabulary (see node 3).\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-425.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-425.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-425.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 425"
}
```


### [2026-09-14T01:42:48.190Z] TOOL RESULT

```
ok
JSON_OK
nodes verified: 18/18
node verdicts: {'confirmed': 16, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 15, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 31, 'silent': 18, 'contradicts': 4, 'partial': 6} | by book: {'KLN': 11, 'PHD': 5, 'BRT': 4, 'SKT': 4, 'FSD': 4, 'POK': 3, 'NYB': 3, 'HRN': 3, 'BQT': 3, 'HUB': 2, 'SYN': 2, 'LAT': 2, 'PLA': 2, 'MON': 2, 'KNT': 1, 'ARY': 1, 'AHD': 1, 'LEW': 1, 'AFM': 1, 'TAD': 1, 'FVQ': 1, 'WEB': 1, 'DEV': 1}
```


## [2026-09-14T01:42:57.122Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport io\np='data/verification/page-425.json'\ns=io.open(p,encoding='utf-8').read()\nassert \"‘the country’ap\" in s\ns=s.replace(\"‘the country’ap \", \"‘the country’ \")\nio.open(p,'w',encoding='utf-8').write(s)\nprint('fixed')\nEOF\npython3 -m json.tool data/verification/page-425.json >/dev/null && echo JSON_OK && python3 tools/verify_check.py 425 | head -5"
}
```


### [2026-09-14T01:42:58.387Z] TOOL RESULT

```
fixed
JSON_OK
nodes verified: 18/18
node verdicts: {'confirmed': 16, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 15, 'partial': 3, 'not_checked': 4, 'not_found': 1}
books consulted: {'supports': 31, 'silent': 18, 'contradicts': 4, 'partial': 6} | by book: {'KLN': 11, 'PHD': 5, 'BRT': 4, 'SKT': 4, 'FSD': 4, 'POK': 3, 'NYB': 3, 'HRN': 3, 'BQT': 3, 'HUB': 2, 'SYN': 2, 'LAT': 2, 'PLA': 2, 'MON': 2, 'KNT': 1, 'ARY': 1, 'AHD': 1, 'LEW': 1, 'AFM': 1, 'TAD': 1, 'FVQ': 1, 'WEB': 1, 'DEV': 1}
```


## [2026-09-14T01:43:18.170Z] AGENT

Done. `data/verification/page-425.json` written; `verify_check.py 425` reports 18/18 nodes, 0 PROBLEM lines.

**Page 425 (book p. 395) — 3 entries, 18 nodes**

- Root verdicts: 3 confirmed (PIE *reuto- POK 873–4; PIE *reuə- : *rū- POK 874; Semitic *r-p-ʾ, Klein 1301 — Nourai's page numbers for POK, KLN 1301, KLN 1356, SYN 465, HRN 139 all checked out exact).
- Node verdicts: 16 confirmed, 1 disputed, 1 plausible.

**disputed**
- Entry 0 (*Reuto*), node 2, Pahlavi **aškumb** ← Av. *uruθwan-*: this is a Zand **translation** equivalence, not a descent. Bartholomae (col. 1530-33) notes only "Pü. škamb"; MacKenzie records the real Pahlavi continuant of Av. *uruθβar-* separately as ***uruspar*** 'intestines, womb'. aškamb is an independent Iranian word (Man. MP/Sogd. *škmb*, Paz. *aškum*, Yaghnobi *šikampa*) — Nyberg and Hübschmann give it no Avestan etymon. Node 3 (اشکم/شکم < MP aškamb) is itself confirmed; only its attachment to the root fails.

**plausible**
- Entry 2, node 7, Persian **رافائل**: unreferenced in the book; the phonetic shape points to French *Raphaël* or Italian *Raffaele*, so the Latin→French→Persian route is reasonable but Italian mediation is equally likely. (Also flagged: the older Arabic-mediated رفائیل/روفائیل is not its source.)

**Notable findings, no verdict change**
- *uruthwasča* is not a third stem but the attested plural + enclitic *uruθwąsca* "and the entrails" (Yt 13.11) — faithful to the book, worth a data note.
- Entry 2 node 2 (رفو): Mo'in's own footnote in Borhan-e Qāteʿ reverses Nourai's direction ("معرّب آن: رَفْو", comparing Gk. ῥάπτω), but Dehkhoda, Wiktionary and Klein's Semitic cognate set (Heb./Syr./Eth.) confirm Arabic → Persian; Asbaghi and Addi Shir do not list رفو as a Persian loan in Arabic. Recorded as `contradicts` in `consulted`.
- Pokorny's *reuto- is absent from Walde-Pokorny and from Watkins/AHD (Pokorny's sole authority is Liden, KZ 61, 14 f.) — noted on the root.
- BQT:970 confirmed indirectly: Aryanpur's own روده entry cites "برهان قاطع: ۹۷۰" for the same word.
- FSD:2051 → `not_found`: F&W vol. III runs raphanus → raphe → Raphia with no *Raphael* article; the proper name is in a separate appendix not paginated in the OCR.

**Extraction errors:** none — no `transcription_suspect` nodes; the JSON matches the chart throughout, so no page image was needed.
